#!/bin/bash
# AI Vision Pro - One-Click Deployment Script
# This script sets up everything for production deployment

echo "🚀 AI Vision Pro - Deployment Setup"
echo "===================================="
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}Step 1: Checking prerequisites...${NC}"

# Check Python
if command -v python3 &> /dev/null; then
    echo -e "${GREEN}✓ Python found${NC}"
else
    echo -e "${YELLOW}✗ Python not found. Please install Python 3.11+${NC}"
    exit 1
fi

# Check Git
if command -v git &> /dev/null; then
    echo -e "${GREEN}✓ Git found${NC}"
else
    echo -e "${YELLOW}✗ Git not found. Please install Git${NC}"
    exit 1
fi

echo ""
echo -e "${BLUE}Step 2: Setting up virtual environment...${NC}"
python3 -m venv venv
source venv/bin/activate || venv\Scripts\activate

echo ""
echo -e "${BLUE}Step 3: Installing dependencies...${NC}"
pip install --upgrade pip
pip install -r requirements_enhanced.txt

echo ""
echo -e "${BLUE}Step 4: Checking configuration...${NC}"
if [ -f ".env" ]; then
    echo -e "${GREEN}✓ .env file found${NC}"
else
    echo -e "${YELLOW}! .env file not found. Creating from template...${NC}"
    cp .env.example .env
    echo -e "${YELLOW}! Please edit .env file with your Supabase credentials${NC}"
fi

echo ""
echo -e "${BLUE}Step 5: Testing database connection...${NC}"
python -c "from config.settings import check_supabase_config; print('Supabase:', 'Ready' if check_supabase_config() else 'Not configured')"

echo ""
echo -e "${BLUE}Step 6: Loading AI Model...${NC}"
python -c "from shared_model import get_classifier; c = get_classifier(); print('Model loaded:', c.load_model())"

echo ""
echo -e "${GREEN}====================================${NC}"
echo -e "${GREEN}✅ Setup Complete!${NC}"
echo -e "${GREEN}====================================${NC}"
echo ""
echo "Next steps:"
echo "1. Edit .env file with your credentials"
echo "2. Run: python backend/main.py"
echo "3. Run: streamlit run web_app_enhanced/main.py"
echo ""
echo "Or run everything at once:"
echo "  python run_all.py"
echo ""
echo "Deployment:"
echo "  Backend → https://render.com"
echo "  Frontend → https://share.streamlit.io"
echo ""
