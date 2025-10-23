from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load model
model = joblib.load('decision_tree_mushroom.pkl')

# Daftar fitur setelah encoding (urutan penting!)
with open('feature_names.txt', 'r') as f:
    feature_names = [line.strip() for line in f.readlines()]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "model": "Decision Tree Mushroom Classifier"})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        
        # Dummy values untuk fitur yang tidak diisi (simplified demo)
        # Dalam production, semua fitur harus diisi atau gunakan default yang aman
        full_features = {
            'cap-shape': 'x', 'cap-surface': 's', 'cap-color': 'n',
            'bruises': 't', 'odor': 'n', 'gill-attachment': 'f',
            'gill-spacing': 'c', 'gill-size': 'b', 'gill-color': 'k',
            'stalk-shape': 'e', 'stalk-root': 'e', 'stalk-surface-above-ring': 's',
            'stalk-surface-below-ring': 's', 'stalk-color-above-ring': 'w',
            'stalk-color-below-ring': 'w', 'veil-type': 'p', 'veil-color': 'w',
            'ring-number': 'o', 'ring-type': 'p', 'spore-print-color': 'k',
            'population': 's', 'habitat': 'u'
        }
        
        # Update dengan input user
        full_features.update(data)
        
        # Buat DataFrame dan one-hot encode
        input_df = pd.DataFrame([full_features])
        input_encoded = pd.get_dummies(input_df)
        
        # Pastikan semua fitur ada (sesuai training)
        for col in feature_names:
            if col not in input_encoded.columns:
                input_encoded[col] = 0
        
        # Urutkan sesuai training (copy untuk menghindari PerformanceWarning)
        input_encoded = input_encoded[feature_names].copy()
        
        # Prediksi
        prediction = model.predict(input_encoded)[0]
        proba = model.predict_proba(input_encoded)[0]
        confidence = round(max(proba) * 100, 2)
        
        return jsonify({
            'prediction': prediction,
            'label': 'Edible' if prediction == 'e' else 'Poisonous',
            'confidence': confidence
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
