# AI Vision Pro - Complete Setup Guide
# 100% FREE Tools Only

## 🎯 What You're Building
A production-ready AI image detection web app with:
- ✅ User authentication (email/password)
- ✅ Image upload + Camera input
- ✅ AI predictions with confidence scores
- ✅ History saved to database
- ✅ Free tier (10 predictions/day) + Pro upgrade
- ✅ Premium dark/light UI
- ✅ Deployable for FREE on Render + Streamlit Cloud

---

## 📋 Prerequisites (All Free)

1. **Python 3.11+** → https://python.org/downloads
2. **Git** → https://git-scm.com/downloads
3. **Supabase Account** → https://supabase.com (Free tier)
4. **Render Account** → https://render.com (Free tier)
5. **Streamlit Cloud** → https://share.streamlit.io (Free)

---

## 🚀 Quick Setup (5 Minutes)

### Step 1: Clone & Setup Environment

```bash
# Clone repository
cd c:\Users\Lenovo\CascadeProjects\windsurf-project

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements_enhanced.txt
```

### Step 2: Setup Supabase (Database)

1. Go to https://supabase.com
2. Click "New Project"
3. Name: `ai-vision-pro`
4. Wait for database to be ready (~2 minutes)
5. Go to **Settings → API**
6. Copy:
   - **URL** (e.g., `https://xxxx.supabase.co`)
   - **anon public** key

7. Go to **SQL Editor → New query**
8. Run this SQL:

```sql
-- Users table
CREATE TABLE users (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    tier VARCHAR(20) DEFAULT 'free',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Predictions history
CREATE TABLE predictions (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    image_url TEXT,
    label VARCHAR(255),
    confidence FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Usage tracking
CREATE TABLE usage_logs (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    date DATE DEFAULT CURRENT_DATE,
    count INTEGER DEFAULT 0,
    UNIQUE(user_id, date)
);
```

### Step 3: Configure Environment Variables

```bash
# Copy example file
copy .env.example .env
```

Edit `.env` file with your values:

```env
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIs...
RAZORPAY_KEY_ID=rzp_test_...  # Optional - for payments
RAZORPAY_KEY_SECRET=...        # Optional - for payments
DEBUG_MODE=false
```

### Step 4: Run Locally

```bash
# Terminal 1 - Start Backend
python backend/main.py
# → http://localhost:8000

# Terminal 2 - Start Web App (Enhanced)
streamlit run web_app_enhanced/main.py
# → http://localhost:8501
```

Open browser to **http://localhost:8501** 🎉

---

## 🌐 Deployment (FREE)

### Deploy Backend to Render.com

1. **Push code to GitHub**
```bash
git add .
git commit -m "Production ready"
git push origin main
```

2. **Create Render Account**
   - Go to https://render.com
   - Sign up with GitHub

3. **New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repo
   - Settings:
     - **Name**: `ai-vision-pro-api`
     - **Runtime**: Python 3
     - **Build**: `pip install -r requirements_enhanced.txt`
     - **Start**: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
     - **Plan**: Free

4. **Add Environment Variables**
   - Go to Environment tab
   - Add all variables from your `.env` file

5. **Deploy!**
   - Click "Create Web Service"
   - Wait ~5 minutes
   - Get your URL: `https://ai-vision-pro-api.onrender.com`

### Deploy Frontend to Streamlit Cloud

1. **Push code to GitHub** (ensure `web_app_enhanced/main.py` exists)

2. **Go to** https://share.streamlit.io

3. **Deploy**
   - Sign in with GitHub
   - Click "New app"
   - Select: `yourusername/ai-vision-pro`
   - Branch: `main`
   - File: `web_app_enhanced/main.py`
   - Click "Deploy"

4. **Your app is live!** 🚀

---

## 💳 Enable Payments (Optional)

### Razorpay Setup (India)

1. Go to https://razorpay.com
2. Sign up and complete KYC
3. Dashboard → Settings → API Keys
4. Copy `Key ID` and `Key Secret`
5. Add to Render environment variables

Test card: `5267 3181 8797 5449`
Any future expiry, any CVV, OTP: `1234`

---

## 📱 Mobile App (Convert to APK)

### Method 1: WebView APK (Easiest)

Create a simple Android app that loads your Streamlit URL:

1. Install Android Studio
2. Create new project → Empty Activity
3. In `MainActivity.java`:

```java
WebView webView = findViewById(R.id.webview);
webView.loadUrl("https://your-app.streamlit.app");
```

4. Build → Generate APK

### Method 2: PWA (Progressive Web App)

Add to your Streamlit app:
```python
st.markdown("""
<script>
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js');
}
</script>
""", unsafe_allow_html=True)
```

Users can "Add to Home Screen" on mobile.

---

## 🧪 Testing

### Test API
```bash
curl http://localhost:8000/health
```

### Test Prediction
```bash
curl -X POST "http://localhost:8000/predict" \
  -F "file=@test_image.jpg"
```

### Test Database
```bash
python database/supabase_client.py
```

---

## 🎨 Customization

### Change Colors
Edit `web_app_enhanced/main.py`:
```python
# In get_css() function
"bg_primary": "#0d0d0d"  # Change background
"neon_blue": "#00d4ff"   # Change accent
```

### Change Limits
Edit `config/settings.py`:
```python
FREE_PREDICTIONS_PER_DAY = 10  # Change free tier
PRICING["pro"]["price"] = 499  # Change price
```

### Add New AI Models
Edit `shared_model/classifier.py`:
```python
# Add more models from HuggingFace
self.model_name = "microsoft/resnet-50"  # Change model
```

---

## 🆘 Troubleshooting

### "Module not found"
```bash
pip install -r requirements_enhanced.txt
```

### "Supabase connection failed"
- Check `.env` file has correct URL and key
- Ensure SQL tables were created
- Check internet connection

### "Model failed to load"
- First run downloads ~100MB model
- Check internet connection
- Wait 2-3 minutes

### "Camera not working"
- Use HTTPS (required for camera)
- On localhost, use `localhost` not `127.0.0.1`

---

## 📈 Next Steps

1. ✅ Add your logo
2. ✅ Customize colors
3. ✅ Add Google Analytics
4. ✅ Set up custom domain
5. ✅ Add more AI models
6. ✅ Add WhatsApp sharing
7. ✅ Create admin dashboard

---

## 💡 Pro Tips

- **Free Render**: Sleeps after 15 min inactivity (wakes on request)
- **Supabase**: 500MB database limit on free tier
- **Streamlit**: Unlimited apps on free tier
- **Images**: Use Imgur or Cloudinary for image hosting

---

## 📞 Support

- **Documentation**: See README.md
- **Issues**: Check TROUBLESHOOTING section
- **Community**: Streamlit/Supabase Discord

---

**🎉 You're ready to launch your AI startup!**

Built with ❤️ using 100% free tools.
