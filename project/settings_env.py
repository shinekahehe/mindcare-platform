"""
Environment configuration for Django project.
Handles environment variables for both local development and production deployment.
"""

import os
import re
import logging
from urllib.parse import urlparse

logger = logging.getLogger(__name__)

def is_production():
    """Check if running in production environment (Render, Heroku, etc.)"""
    return bool(os.getenv("RENDER") or os.getenv("DYNO") or os.getenv("RAILWAY_ENVIRONMENT"))

def load_env_file():
    """Load .env file only in local development"""
    if not is_production():
        try:
            from dotenv import load_dotenv
            load_dotenv()
            logger.info("Loaded .env file for local development")
        except ImportError:
            logger.warning("python-dotenv not installed, skipping .env file loading")
        except Exception as e:
            logger.warning(f"Failed to load .env file: {e}")

def get_required_env(key, description=""):
    """Get required environment variable with clear error message"""
    value = os.getenv(key)
    if not value:
        error_msg = f"Required environment variable {key} is not set"
        if description:
            error_msg += f" ({description})"
        logger.error(error_msg)
        raise ValueError(error_msg)
    return value.strip()

def get_optional_env(key, default=None):
    """Get optional environment variable with whitespace trimming"""
    value = os.getenv(key, default)
    return value.strip() if value else default

def validate_supabase_url(url):
    """Validate and parse Supabase URL"""
    if not url:
        return None, None
    
    # Pattern: https://<ref>.supabase.co
    pattern = r'^https://([a-z0-9]{20,30})\.supabase\.co/?$'
    match = re.match(pattern, url)
    
    if not match:
        logger.error(f"Invalid Supabase project ref in SUPABASE_URL: {url}")
        logger.error("Expected format: https://<20-30 lowercase alphanumeric chars>.supabase.co")
        return None, None
    
    project_ref = match.group(1)
    logger.info(f"Supabase project ref: {project_ref[:8]}...{project_ref[-4:]}")
    return url, project_ref

def normalize_database_url(url):
    """Normalize database URL and validate format"""
    if not url:
        return None
    
    # Strip whitespace
    url = url.strip()
    
    if not url:
        return None
    
    # Parse URL to validate format
    try:
        parsed = urlparse(url)
        if parsed.scheme not in ['postgres', 'postgresql']:
            logger.error(f"Invalid database scheme in DATABASE_URL: {parsed.scheme}")
            logger.error("Expected: postgres:// or postgresql://")
            return None
        
        # Normalize postgres:// to postgresql://
        if parsed.scheme == 'postgres':
            url = url.replace('postgres://', 'postgresql://', 1)
            logger.info("Normalized postgres:// to postgresql:// in DATABASE_URL")
        
        return url
        
    except Exception as e:
        logger.error(f"Invalid DATABASE_URL format: {e}")
        return None

def get_environment_config():
    """Get and validate all environment configuration"""
    config = {}
    
    # Load .env file if in development
    load_env_file()
    
    # Django settings
    config['SECRET_KEY'] = get_optional_env('DJANGO_SECRET_KEY') or get_optional_env('SECRET_KEY')
    if not config['SECRET_KEY']:
        # Fallback for development
        config['SECRET_KEY'] = "django-insecure-e8%q@h1rxa8tp7r)m91u(7it5wwhe3(e-8uz00!*-d1st7drl%"
        logger.warning("No SECRET_KEY found, using development fallback")
    
    config['DEBUG'] = os.getenv('DEBUG', 'False').lower() == 'true'
    config['ALLOWED_HOSTS'] = get_optional_env('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')
    
    # Database
    database_url = get_optional_env('DATABASE_URL')
    if database_url:
        config['DATABASE_URL'] = normalize_database_url(database_url)
        if not config['DATABASE_URL']:
            raise ValueError("Invalid DATABASE_URL configuration")
    else:
        config['DATABASE_URL'] = None
    
    # Supabase
    supabase_url = get_optional_env('SUPABASE_URL')
    if supabase_url:
        validated_url, project_ref = validate_supabase_url(supabase_url)
        if not validated_url:
            raise ValueError("Invalid SUPABASE_URL configuration")
        config['SUPABASE_URL'] = validated_url
        config['SUPABASE_PROJECT_REF'] = project_ref
    else:
        config['SUPABASE_URL'] = None
        config['SUPABASE_PROJECT_REF'] = None
    
    config['SUPABASE_ANON_KEY'] = get_optional_env('SUPABASE_ANON_KEY')
    config['SUPABASE_SERVICE_ROLE_KEY'] = get_optional_env('SUPABASE_SERVICE_ROLE_KEY')
    
    # Gemini API
    config['GEMINI_API_KEY'] = get_optional_env('GEMINI_API_KEY')
    
    # Log configuration status
    logger.info("Environment configuration loaded:")
    logger.info(f"  Production mode: {is_production()}")
    logger.info(f"  Debug mode: {config['DEBUG']}")
    logger.info(f"  Database configured: {bool(config['DATABASE_URL'])}")
    logger.info(f"  Supabase configured: {bool(config['SUPABASE_URL'])}")
    logger.info(f"  Gemini API configured: {bool(config['GEMINI_API_KEY'])}")
    
    return config

# Load configuration
try:
    ENV_CONFIG = get_environment_config()
except Exception as e:
    logger.error(f"Environment configuration failed: {e}")
    raise
