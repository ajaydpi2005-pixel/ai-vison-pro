# 🎯 AI Vision Pro - Production Ready

**Premium AI-Powered Image Classification Platform**

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://python.org)
[![Flutter](https://img.shields.io/badge/Flutter-3.0+-blue.svg)](https://flutter.dev)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com)

A complete, client-ready AI image classification product with premium UI, real payments (Razorpay/Stripe), and multi-platform deployment.

![AI Vision Pro](https://img.shields.io/badge/AI%20Vision%20Pro-Premium%20Image%20Detection-00d4ff?style=for-the-badge&logo=artificial-intelligence&logoColor=white)

## 📋 Table of Contents

- [Screenshots](#-screenshots)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Pricing Model](#-pricing-model--business-plan)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Deployment Guide](#-deployment-guide)
- [Payment Integration](#-payment-integration)
- [Mobile App Build](#-mobile-app-build-apk)
- [API Documentation](#-api-documentation)
- [Client Demo Script](#-client-demo-script)

## 📸 Screenshots

> **Note:** Add your screenshots here before showing to clients

### Desktop App
```
screenshots/desktop_home.png
screenshots/desktop_prediction.png
screenshots/desktop_pricing.png
```

### Web App
```
screenshots/web_upload.png
screenshots/web_results.png
screenshots/web_pricing.png
```

### Mobile App
```
screenshots/mobile_home.jpg
screenshots/mobile_camera.jpg
screenshots/mobile_results.jpg
```

---

## ✨ Premium Features

### 1. 🖥️ Desktop App (Tkinter + Premium UI)
- ✨ **Premium dark theme** with neon blue & purple gradients
- 🎨 **Logo branding** with animated spinner
- 💎 **Pricing section** - Free, Pro, Business tiers
- 🖱️ **Hover effects** on all interactive elements
- 📊 **Premium result cards** with progress bars
- 🔒 **Upgrade button** for monetization
- ⚡ **Animated loading spinner** with glow effect
- 📁 **Drag & drop** style upload zone

### 2. 📷 Live Camera Detection (OpenCV)
- 📹 Real-time webcam feed with AI overlay
- 🎯 Classification every 1.5 seconds (CPU optimized)
- 📊 Live prediction display with confidence bars
- 🎮 Keyboard controls ('Q' quit, 'SPACE' capture)
- 📈 FPS counter and system status
- 🎨 Dark overlay UI with neon accents

### 3. 🔌 Backend API (FastAPI + Payments)
- 🔗 `POST /predict` - Image classification
- 💰 `POST /payment/create-order` - Razorpay/Stripe integration
- ✅ `POST /payment/verify` - Payment verification
- 📊 `GET /subscription/status/{user_id}` - Subscription management
- 🔔 Webhook support for Razorpay & Stripe
- 🛡️ Secure signature verification
- 📊 Rate limiting per user tier
- 🌍 CORS enabled for all platforms

### 4. 📱 Mobile App (Flutter - Production Ready)
- 📲 Beautiful dark UI with gradient accents
- 📸 Camera capture + Gallery picker
- 💳 In-app tier selection (Free/Pro/Business)
- 📊 Usage progress bar
- ⚡ Custom animated loading spinner
- 🎴 Premium prediction cards
- 🔗 Connected to live backend API
- 📦 **Ready for APK build**

### 5. 🌐 Web App (Streamlit Cloud Ready)
- 🎨 Premium dark theme with gradients
- 💎 Built-in pricing section
- 📊 Usage tracking with progress bar
- 🎴 Animated prediction cards
- 📱 Responsive design
- 🚀 One-click Streamlit Cloud deploy

---

## 💰 Pricing Model & Business Plan

| Tier | Price | Predictions | Features |
|------|-------|-------------|----------|
| **Free** | ₹0 | 10/day | Basic AI, Email support |
| **Pro** | ₹499/mo | 100/day | Advanced AI, Priority support, API access |
| **Business** | ₹1999/mo | Unlimited | Enterprise AI, 24/7 support, Custom integrations |

### Revenue Projections (India Market)
- **Target:** 1000 Pro users + 100 Business users
- **Monthly Revenue:** ₹4,99,000 + ₹1,99,900 = **₹6,98,900**
- **Annual Revenue:** ~**₹84 Lakhs**

### Payment Integration
- **India:** Razorpay (UPI, Cards, Net Banking)
- **International:** Stripe (Credit/Debit Cards)

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Python, FastAPI, Hugging Face Transformers |
| **Desktop** | Python, Tkinter, OpenCV |
| **Camera** | Python, OpenCV |
| **Mobile** | Flutter, Dart |
| **Web** | Python, Streamlit |
| **ML Model** | Microsoft ResNet-50 (Hugging Face) |
| **Image Processing** | Pillow, OpenCV |
| **Payments** | Razorpay (India), Stripe (International) |

## 📁 Project Structure

```
ai-vision-pro/
├── backend/                  # FastAPI + Payment Integration
│   ├── main.py              # API endpoints + Payments
│   ├── requirements.txt     # Production dependencies
│   ├── Procfile             # Heroku/Render config
│   └── render.yaml          # Render.com deployment
├── camera_app/               # Real-time camera detection
│   └── main.py
├── desktop_app/              # Tkinter + Premium UI
│   └── main.py
├── mobile_app/               # Flutter + Production Ready
│   ├── lib/
│   │   ├── main.dart
│   │   ├── screens/
│   │   ├── services/
│   │   ├── theme/
│   │   └── widgets/
│   ├── android/
│   │   └── app/src/main/
│   │       └── AndroidManifest.xml
│   ├── pubspec.yaml
│   ├── analysis_options.yaml
│   └── BUILD_APK.md         # APK Build Guide
├── shared_model/             # Shared ML model
│   ├── __init__.py
│   └── classifier.py
├── web_app/                  # Streamlit + Premium UI
│   ├── main.py
│   └── requirements.txt
├── .windsurf/workflows/      # Setup & Deploy guides
│   ├── setup.md
│   └── deploy.md
├── requirements.txt          # Master Python dependencies
├── run_all.py               # Development launcher
├── .gitignore
└── README.md                # This file
```

---

## 🚀 Quick Start (Development)

### Prerequisites
- **Python 3.11+** (Download from python.org)
- **Flutter 3.0+** (For mobile app - flutter.dev)
- **Android Studio** (For APK builds)
- **Webcam** (For camera app)

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/ai-vision-pro.git
cd ai-vision-pro
```

### 2. Setup Python Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Install all dependencies
pip install -r requirements.txt
```

### 3. Run All Components

```bash
# Run everything at once (opens multiple terminals)
python run_all.py
```

Or run individually:

```bash
# Terminal 1 - Backend API
python backend/main.py

# Terminal 2 - Desktop App
python desktop_app/main.py

# Terminal 3 - Web App
streamlit run web_app/main.py

# Terminal 4 - Camera (after backend loads)
python camera_app/main.py

# Terminal 5 - Mobile App
cd mobile_app
flutter pub get
flutter run
```

---

## 🌐 Deployment Guide

### Backend - Render.com (Recommended)

1. **Push code to GitHub**
```bash
git add .
git commit -m "Production ready"
git push origin main
```

2. **Create Render Account**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub

3. **New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repo
   - Name: `ai-vision-pro-api`
   - Runtime: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
   - Plan: `Starter` ($7/month) or `Free`

4. **Add Environment Variables**
   ```
   RAZORPAY_KEY_ID=rzp_test_...
   RAZORPAY_KEY_SECRET=...
   STRIPE_SECRET_KEY=sk_test_...
   ```

5. **Deploy!**
   - Click "Create Web Service"
   - Wait for build (~5-10 minutes)
   - Your API is live!

6. **Get your URL**
   - Example: `https://ai-vision-pro-api.onrender.com`

### Web App - Streamlit Cloud

1. **Push to GitHub** (ensure web_app/main.py is present)

2. **Go to** [share.streamlit.io](https://share.streamlit.io)

3. **Deploy**
   - Sign in with GitHub
   - Click "New app"
   - Select repo: `yourusername/ai-vision-pro`
   - Branch: `main`
   - Main file path: `web_app/main.py`
   - Click "Deploy"

4. **Your web app is live!**

### Backend - Railway.app (Alternative)

1. Go to [railway.app](https://railway.app)
2. New Project → Deploy from GitHub repo
3. Add Python service
4. Start Command: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
5. Deploy!

---

## 💳 Payment Integration Setup

### Razorpay (For India)

1. **Create Account**
   - Go to [razorpay.com](https://razorpay.com)
   - Sign up and complete KYC

2. **Get API Keys**
   - Dashboard → Settings → API Keys
   - Copy `Key ID` and `Key Secret`

3. **Configure Backend**
   ```bash
   # On Render dashboard, add Environment Variables:
   RAZORPAY_KEY_ID=rzp_live_...
   RAZORPAY_KEY_SECRET=...
   ```

4. **Test Payment**
   - Use test card: `5267 3181 8797 5449`
   - Any future expiry, any CVV
   - OTP: `1234`

### Stripe (For International)

1. **Create Account**
   - Go to [stripe.com](https://stripe.com)

2. **Get API Keys**
   - Developers → API Keys
   - Copy `Secret key`

3. **Configure Backend**
   ```bash
   # On Render dashboard:
   STRIPE_SECRET_KEY=sk_live_...
   STRIPE_WEBHOOK_SECRET=whsec_...
   ```

4. **Test Payment**
   - Use test card: `4242 4242 4242 4242`

---

## 📱 Mobile App Build (APK)

### Step-by-Step APK Build

```bash
# 1. Navigate to mobile app
cd mobile_app

# 2. Install dependencies
flutter pub get

# 3. Update API endpoint (IMPORTANT!)
# Edit: lib/services/api_service.dart
# Change baseUrl to your deployed backend

# 4. Clean previous builds
flutter clean

# 5. Build Release APK
flutter build apk --release

# 6. Find your APK
# Output: build/app/outputs/flutter-apk/app-release.apk

# 7. Install on device
flutter install
# OR
adb install build/app/outputs/flutter-apk/app-release.apk
```

### Detailed Build Guide
See [mobile_app/BUILD_APK.md](mobile_app/BUILD_APK.md) for complete instructions including:
- Prerequisites setup
- Android Studio configuration
- Signing for Play Store
- Troubleshooting

### APK Size: ~25-30 MB

---

## 📚 API Documentation

### Base URL
- **Local:** `http://localhost:8000`
- **Production:** `https://your-backend-url.com`

### Endpoints

#### 1. Health Check
```http
GET /health
```
Response:
```json
{
  "status": "healthy",
  "model_loaded": true,
  "version": "1.0.0"
}
```

#### 2. Image Classification
```http
POST /predict
Content-Type: multipart/form-data

file: <image_file>
premium_mode: false (optional)
```
Response:
```json
{
  "success": true,
  "predictions": [
    {"label": "golden_retriever", "confidence": 95.42, "label_id": 207},
    {"label": "labrador", "confidence": 3.15, "label_id": 208},
    {"label": "beagle", "confidence": 1.23, "label_id": 162}
  ],
  "processing_time_ms": 245.67,
  "image_size": {"width": 512, "height": 384, "bytes": 45678},
  "timestamp": "2024-01-15T10:30:00"
}
```

#### 3. Create Payment Order (Razorpay/Stripe)
```http
POST /payment/create-order
Content-Type: application/json

{
  "amount": 49900,  // ₹499 in paise
  "currency": "INR", // or "USD" for Stripe
  "tier": "pro",
  "user_id": "user_123"
}
```
Response:
```json
{
  "success": true,
  "order_id": "order_...",
  "amount": 49900,
  "currency": "INR",
  "key_id": "rzp_test_...",
  "message": "Order created successfully"
}
```

#### 4. Verify Payment
```http
POST /payment/verify
Content-Type: application/json

{
  "payment_id": "pay_...",
  "order_id": "order_...",
  "signature": "...",
  "tier": "pro",
  "user_id": "user_123"
}
```
Response:
```json
{
  "success": true,
  "verified": true,
  "tier": "pro",
  "message": "Payment verified and premium activated",
  "subscription_active": true
}
```

#### 5. Get Subscription Status
```http
GET /subscription/status/{user_id}
```
Response:
```json
{
  "user_id": "user_123",
  "tier": "pro",
  "active": true,
  "activated_at": "2024-01-15T10:30:00",
  "payment_id": "pay_..."
}
```

#### 6. Payment Integration Status
```http
GET /payment/status
```
Response:
```json
{
  "razorpay": {
    "available": true,
    "configured": true,
    "key_id": "rzp_test_..."
  },
  "stripe": {
    "available": true,
    "configured": false
  }
}
```

---

## 🎤 Client Demo Script

Use this script when demonstrating to potential clients:

### 1. Opening (30 seconds)
"This is AI Vision Pro - a complete AI image classification platform. It works on Desktop, Web, Mobile, and even real-time camera feed. Perfect for retail, security, healthcare, and education markets."

### 2. Desktop Demo (2 minutes)
1. Open desktop app
2. Point out premium UI: "Notice the dark theme, the animated logo, the pricing section"
3. Upload an image: "Watch the smooth transitions"
4. Show predictions: "Top 3 predictions with confidence scores"
5. Show pricing dialog: "Three tiers - Free, Pro at ₹499, Business at ₹1999"

### 3. Web Demo (1 minute)
1. Open web app in browser
2. "Same premium experience on web - no installation needed"
3. Upload image, show results
4. "Perfect for SaaS model - deploy on Streamlit Cloud for free"

### 4. Mobile Demo (2 minutes)
1. Show Flutter app on phone
2. "Native Android app - can be on Play Store"
3. Demonstrate camera capture
4. Show real-time upload to backend
5. "Users can pay via Razorpay directly in app"

### 5. Camera Demo (1 minute)
1. Launch camera app
2. "Real-time detection - great for retail stores, security"
3. Show predictions overlay
4. Press SPACE to capture

### 6. Revenue Pitch (1 minute)
"Pricing is designed for Indian market:
- Free tier: 10 predictions/day - gets users hooked
- Pro: ₹499/month - target freelancers, small businesses
- Business: ₹1999/month - for enterprises

With just 1000 Pro users + 100 Business users:
- Monthly revenue: ₹6.98 Lakhs
- Annual: ₹84 Lakhs
- Payment integration ready via Razorpay & Stripe"

### 7. Technical Credibility (30 seconds)
"Built with production-grade tech:
- FastAPI backend - same framework used by Uber, Netflix
- Hugging Face AI - world's leading ML platform
- Flutter mobile - used by Google, Alibaba
- Deploy anywhere - Render, AWS, GCP"

### 8. Call to Action
"The product is complete and ready to launch. We just need to:
1. Connect your Razorpay account (5 minutes)
2. Deploy to your domain (10 minutes)
3. Publish Android app to Play Store (1-2 days)

You can start accepting paying customers within 24 hours."

---

## 🎨 UI Theme Reference

### Color Palette
| Color | Hex | Usage |
|-------|-----|-------|
| Background | `#0d0d0d` | Main background |
| Card | `#1e1e1e` | Cards, panels |
| Neon Blue | `#00d4ff` | Primary accent |
| Neon Purple | `#8b5cf6` | Secondary accent |
| Success | `#10b981` | High confidence |
| Warning | `#f59e0b` | Low confidence |
| Premium Gold | `#fbbf24` | Business tier |

---

## ⚡ Performance Specs

- **Model Load Time:** ~3-5 seconds (first run)
- **Inference Time:** ~100-300ms per image
- **Camera FPS:** 30 FPS with 1.5s classification interval
- **Supported Resolutions:** Up to 4K (auto-resized to 512px)
- **CPU Usage:** Optimized for low-power devices
- **Memory:** ~2GB RAM recommended

---

## 🔒 Security Features

- ✅ Input validation on all endpoints
- ✅ File type whitelist (JPG, PNG, WebP only)
- ✅ File size limit (10MB)
- ✅ Payment signature verification (HMAC)
- ✅ Webhook signature validation
- ✅ CORS configuration
- ✅ Environment variable secrets
- ✅ No sensitive data in logs

---

## 🆘 Troubleshooting

### Common Issues

**"Model failed to load"**
```bash
# Solution: Check internet connection
# First run downloads ~100MB model
```

**"Camera not working"**
```bash
# Check webcam permissions
# Update OpenCV: pip install --upgrade opencv-python
```

**"Mobile app can't connect to backend"**
```bash
# Check API URL in lib/services/api_service.dart
# Use 10.0.2.2:8000 for Android emulator
# Use localhost:8000 for iOS simulator
```

**"Payment verification failed"**
```bash
# Check environment variables are set
# Verify Razorpay/Stripe keys are correct
```

---

## 📞 Support & Contact

For technical support or business inquiries:
- 📧 Email: support@aivisionpro.com
- 💬 WhatsApp: +91-XXXXXXXXXX
- 🌐 Website: www.aivisionpro.com

---

## 📄 License

MIT License - Free for personal and commercial use.

**Copyright (c) 2024 AI Vision Pro**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files...

---

**🎯 Ready to launch your AI business!**

*Built with ❤️ in India for the world* 🇮🇳
