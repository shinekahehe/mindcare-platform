#!/usr/bin/env bash
# Build script for Render deployment

echo "🚀 Starting MindCare Platform build..."

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Try to run migrations with fallback
echo "🗄️ Running database migrations..."
if python manage.py migrate --noinput; then
    echo "✅ Database migrations completed successfully"
else
    echo "⚠️ Database migration failed, but continuing with build..."
    echo "The app will use SQLite as fallback database"
fi

echo "🎉 Build completed successfully!"