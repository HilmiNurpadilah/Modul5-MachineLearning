# 🍄 Mushroom Classifier - Decision Tree

Web application untuk klasifikasi jamur (edible vs poisonous) menggunakan Decision Tree.

## 📊 Model Performance
- **Algorithm**: Decision Tree with GridSearchCV tuning
- **Dataset**: UCI Mushroom Classification (8124 samples, 23 features)
- **Accuracy**: ~100% (test set)
- **CV Score**: ~100% (5-fold stratified)
- **Top Feature**: `odor_n` (odor=none)

## 🚀 Deployment ke Railway

### Langkah-langkah:

#### 1. Persiapkan Repository Git
```bash
git init
git add .
git commit -m "Initial commit - Mushroom classifier"
```

#### 2. Push ke GitHub
Buat repository baru di [github.com](https://github.com):
```bash
git remote add origin https://github.com/USERNAME/mushroom-classifier.git
git branch -M main
git push -u origin main
```

#### 3. Deploy ke Railway
1. Buka [railway.app](https://railway.app)
2. Login dengan GitHub
3. Click **"New Project"** → **"Deploy from GitHub repo"**
4. Pilih repository `mushroom-classifier`
5. Railway akan auto-detect Flask app
6. Wait for deployment (~2-3 minutes)
7. Click **"Generate Domain"** untuk mendapat public URL
8. Copy URL dan test!

### 📁 File yang Diperlukan
- ✅ `app.py` - Flask application
- ✅ `decision_tree_mushroom.pkl` - Trained model
- ✅ `feature_names.txt` - Feature order (generated from notebook)
- ✅ `requirements.txt` - Python dependencies
- ✅ `Procfile` - Railway/Heroku config

## 🧪 Testing Locally

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Generate Feature Names (jika belum ada)
Jalankan notebook untuk generate `feature_names.txt` dan `decision_tree_mushroom.pkl`

### Run Flask App
```bash
python app.py
```

Buka browser: [http://localhost:5000](http://localhost:5000)

## 🔌 API Endpoints

### 1. Web Interface
```
GET /
```
Web form untuk prediksi interaktif

### 2. Health Check
```
GET /health
```
Response:
```json
{
  "status": "healthy",
  "model": "Decision Tree Mushroom Classifier"
}
```

### 3. Prediction API
```
POST /predict
Content-Type: application/json
```

Request body (minimal 4 features):
```json
{
  "cap-shape": "x",
  "odor": "n",
  "gill-color": "k",
  "spore-print-color": "w"
}
```

Response:
```json
{
  "prediction": "e",
  "label": "Edible",
  "confidence": 100.0
}
```

### Feature Values
- **cap-shape**: b, c, x, f, k, s
- **odor**: a, l, c, y, f, m, n, p, s
- **gill-color**: k, n, b, h, g, r, o, p, u, e, w, y
- **spore-print-color**: k, n, b, h, r, o, u, w, y

## 🛠️ Tech Stack
- **Backend**: Flask
- **ML**: scikit-learn
- **Deployment**: Railway (or Heroku)
- **Model**: Decision Tree (GridSearchCV tuned)

## 📝 Notes
- Model mencapai ~100% accuracy karena dataset ini relatif mudah dipisahkan
- Feature `odor` adalah predictor paling kuat
- Simplified web form hanya menampilkan 4 features utama, sisanya diisi default

## 👨‍💻 Developer
Hilmi - TA-05 - Machine Learning Practicum

---
**Dataset source**: UCI Machine Learning Repository
