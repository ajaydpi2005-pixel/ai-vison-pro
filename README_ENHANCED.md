# AI Vision Pro - Production Ready AI Web App
## 100% FREE Tools | Ready to Deploy | Client-Ready

---

## 🎯 Overview

**AI Vision Pro** is a complete, production-ready AI image detection web application built entirely with **free tools and services**. Perfect for startups, portfolio projects, or client demos.

### What It Does
- 📸 **Upload images** → AI detects objects instantly
- 📷 **Camera input** → Real-time analysis
- 🔐 **User accounts** → Email/password authentication
- 📊 **Usage tracking** → Free tier (10/day) + Pro upgrade
- 💾 **History saved** → All predictions stored in database
- 🌐 **Deploy anywhere** → Render + Streamlit Cloud (both FREE)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **AI Prediction** | Uses ResNet-50 from HuggingFace (free) |
| **User Auth** | Secure login/signup with Supabase |
| **Free Tier** | 10 predictions per day |
| **Pro Upgrade** | Unlimited predictions (₹499/month) |
| **History** | Save and view all past predictions |
| **Camera** | Browser-based camera input |
| **Dark/Light Mode** | Premium UI with theme toggle |
| **Mobile Ready** | Responsive design + APK conversion guide |
| **Payments** | Razorpay integration (India) |

---

## 🏗️ Tech Stack (All Free)

| Component | Tool | Cost |
|-----------|------|------|
| **Backend** | FastAPI + Uvicorn | Free |
| **AI Model** | HuggingFace Transformers | Free |
| **Database** | Supabase (500MB) | Free |
| **Auth** | Supabase Auth | Free |
| **Frontend** | Streamlit | Free |
| **Hosting Backend** | Render.com | Free |
| **Hosting Frontend** | Streamlit Cloud | Free |
| **Payments** | Razorpay (test mode) | Free |

---

## 🚀 Quick Start (5 Minutes)

### Step 1: Download & Install
```bash
cd ai-vision-pro

# Windows: Double-click
QUICKSTART.bat

# Mac/Linux:
chmod +x DEPLOY.sh && ./DEPLOY.sh
```

### Step 2: Setup Supabase (2 Minutes)
1. Go to https://supabase.com → New Project
2. Copy URL and Key from Settings → API
3. Create tables (run SQL from SETUP_GUIDE.md)
4. Paste credentials in `.env` file

### Step 3: Run Locally
```bash
# Terminal 1: Backend
python backend/main.py

# Terminal 2: Web App
streamlit run web_app_enhanced/main.py
```

**Open:** http://localhost:8501 🎉

---

## 🌐 Deployment (Free)

### Backend → Render.com
```yaml
# Already configured in render.yaml
# Just push to GitHub and connect to Render
```
**URL:** `https://ai-vision-pro-api.onrender.com`

### Frontend → Streamlit Cloud
1. Push to GitHub
2. Go to https://share.streamlit.io
3. Select repo → `web_app_enhanced/main.py`
4. Deploy!

**Your app is LIVE!** 🚀

---

## 📱 Mobile App (Convert to APK)

### Option 1: WebView (Easiest)
Create Android app that loads your Streamlit URL:
```java
WebView webView = findViewById(R.id.webview);
webView.loadUrl("https://your-app.streamlit.app");
```

### Option 2: PWA
Users can "Add to Home Screen" - works like native app!

---

## 💳 Payments (Razorpay)

### Setup
1. Create account at https://razorpay.com
2. Get test keys from Dashboard → API Keys
3. Add to environment variables
4. Test with card: `5267 3181 8797 5449`

### Pricing Model
| Plan | Price | Features |
|------|-------|----------|
| **Free** | ₹0 | 10 predictions/day |
| **Pro** | ₹499/month | Unlimited + History |

---

## 📂 Project Structure

```
ai-vision-pro/
├── backend/
│   ├── main.py              # FastAPI + Payments
│   └── render.yaml          # Render deployment
├── web_app_enhanced/
│   └── main.py              # Streamlit with auth & camera
├── database/
│   └── supabase_client.py   # Database operations
├── config/
│   └── settings.py          # All configuration
├── shared_model/
│   └── classifier.py        # AI model wrapper
├── .env.example             # Environment template
├── requirements_enhanced.txt # All dependencies
├── SETUP_GUIDE.md           # Detailed setup
├── QUICKSTART.bat           # Windows one-click
└── DEPLOY.sh                # Mac/Linux one-click
```

---

## 🎨 UI Preview

### Desktop View
- Dark theme with neon blue accents
- Card-based layout
- Animated loading spinners
- Confidence progress bars

### Mobile View
- Fully responsive
- Touch-friendly buttons
- Optimized camera input
- Clean, premium look

---

## 🧪 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | API status |
| `/predict` | POST | Image classification |
| `/payment/create-order` | POST | Create Razorpay order |
| `/payment/verify` | POST | Verify payment |
| `/subscription/status/{user_id}` | GET | Check user tier |

---

## 🛠️ Customization

### Change Colors
Edit `web_app_enhanced/main.py`:
```python
"neon_blue": "#00d4ff"  # Change accent color
"bg_primary": "#0d0d0d"  # Change background
```

### Change Free Tier Limit
Edit `config/settings.py`:
```python
FREE_PREDICTIONS_PER_DAY = 10  # Change to 5, 20, etc.
```

### Change Pricing
Edit `config/settings.py`:
```python
PRICING["pro"]["price"] = 999  # Change to your price
```

---

## 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| "Module not found" | `pip install -r requirements_enhanced.txt` |
| "Supabase error" | Check `.env` file credentials |
| "Model won't load" | Wait 2-3 minutes, check internet |
| "Camera not working" | Use HTTPS (required for camera) |
| "Payment failed" | Use test card: `5267 3181 8797 5449` |

---

## 📈 Future Features (Code Ready)

- [ ] Multiple AI models (food, animals, objects)
- [ ] Language translation
- [ ] WhatsApp sharing
- [ ] Admin dashboard
- [ ] Google OAuth
- [ ] Email notifications

---

## 💡 Pro Tips

1. **Free Render.com**: Sleeps after 15 min → First request wakes it (takes 30s)
2. **Supabase**: 500MB limit → Compress images before upload
3. **Streamlit**: Unlimited apps → Create multiple instances
4. **Images**: Use Imgur free hosting for production

---

## 🎓 Learning Resources

- **FastAPI**: https://fastapi.tiangolo.com
- **Streamlit**: https://docs.streamlit.io
- **Supabase**: https://supabase.com/docs
- **HuggingFace**: https://huggingface.co/docs

---

## 📞 Support

- 📧 Email: your-email@example.com
- 🐦 Twitter: @yourhandle
- 💼 LinkedIn: Your Profile

---

## 📜 License

**MIT License** - Free to use, modify, and distribute.

---

## 🌟 Show Your Support

If this project helped you:
- ⭐ Star the repo
- 🐛 Report bugs
- 💡 Suggest features
- 📢 Share with friends

---

**Built with ❤️ using 100% free tools.**

Ready to launch your AI startup? Let's go! 🚀

---

## 📸 Screenshots

*(Add your screenshots here)*

- [ ] Homepage - Upload section
- [ ] Camera input
- [ ] Prediction result with confidence
- [ ] History page
- [ ] Login/Signup modal
- [ ] Mobile responsive view

---

**Quick Links:**
- 🏠 [Live Demo](https://your-app.streamlit.app)
- 📖 [Full Setup Guide](SETUP_GUIDE.md)
- 💻 [Backend API](https://ai-vision-pro-api.onrender.com/docs)
- 🐛 [Report Issue](https://github.com/yourname/ai-vision-pro/issues)

---

*Last Updated: April 2026*
