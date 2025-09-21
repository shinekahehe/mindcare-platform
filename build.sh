#!/usr/bin/env bash
# Build script for Render deployment

echo "🚀 Starting MindCare Platform build..."

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Run database migrations
echo "🗄️ Running database migrations..."
python manage.py migrate --noinput

echo "🎉 Build completed successfully!"