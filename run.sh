#!/bin/bash
# Quick Install & Run Script
# Usage: bash run.sh

echo "🚀 AutoML CSV Evaluator - Quick Setup"
echo "======================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python found: $(python3 --version)"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
python3 -m pip install -q -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully!"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo ""
echo "🎉 All set! Starting AutoML application..."
echo ""
echo "📍 The app will open at: http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Run the app
streamlit run main.py
