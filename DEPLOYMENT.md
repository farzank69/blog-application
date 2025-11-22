# Django Blog - Render Deployment Guide

## Project Overview
This Django blog application is now fully configured for deployment on Render. All necessary security settings, database configurations, and static file handling have been implemented.

## What Was Changed

### 1. Settings Configuration (`my_site/settings.py`)
- ✅ Fixed `DEBUG` typo (was `IS_DEVELOPMET`)
- ✅ Configured `DEBUG` to properly read from environment variables
- ✅ Updated `ALLOWED_HOSTS` to accept comma-separated values
- ✅ Added PostgreSQL database configuration using `dj-database-url`
- ✅ Added WhiteNoise middleware for static file serving
- ✅ Configured Whitenoise storage backend
- ✅ Added production security settings (SSL, HSTS, secure cookies)
- ✅ Added `python-dotenv` for loading environment variables

### 2. URL Configuration (`my_site/urls.py`)
- ✅ Fixed typo: `docuemnt_root` → `document_root`
- ✅ Removed redundant static URL pattern (handled by WhiteNoise)

### 3. Dependencies (`requirements.txt`)
Added production-ready packages:
- `gunicorn==22.0.0` - WSGI HTTP server
- `psycopg2-binary==2.9.10` - PostgreSQL adapter
- `whitenoise==6.8.2` - Static file serving
- `python-dotenv==1.0.1` - Environment variable management
- `dj-database-url==2.3.0` - Database URL parsing

### 4. New Files Created

#### `build.sh`
Automated build script that:
- Installs dependencies
- Collects static files
- Runs database migrations

#### `render.yaml`
Render configuration file defining:
- Web service configuration
- PostgreSQL database setup
- Environment variables
- Build and start commands

#### `.env.example`
Template for environment variables needed in production

#### `.gitignore`
Excludes sensitive files and unnecessary directories from version control

#### `runtime.txt`
Specifies Python version (3.12.0) for Render

## Deployment Steps

### Step 1: Prepare Your Repository
```bash
# Add all files to git
git add .

# Commit changes
git commit -m "Configure project for Render deployment"

# Push to GitHub
git push origin main
```

### Step 2: Create Render Account
1. Go to https://render.com
2. Sign up or log in
3. Connect your GitHub account

### Step 3: Deploy on Render

#### Option A: Using Blueprint (Recommended)
1. Click "New +" → "Blueprint"
2. Connect your repository
3. Render will detect `render.yaml` and set up everything automatically
4. The database will be created and linked automatically

#### Option B: Manual Setup
1. **Create PostgreSQL Database:**
   - Click "New +" → "PostgreSQL"
   - Name: `django-blog-db`
   - Choose free tier
   - Click "Create Database"
   - Copy the "Internal Database URL"

2. **Create Web Service:**
   - Click "New +" → "Web Service"
   - Connect your repository
   - Configure:
     - **Name:** django-blog
     - **Environment:** Python 3
     - **Build Command:** `./build.sh`
     - **Start Command:** `gunicorn my_site.wsgi:application`

3. **Add Environment Variables:**
   - `SECRET_KEY`: Generate a new one (use Django's `get_random_secret_key()` or an online generator)
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: Your Render URL (e.g., `django-blog.onrender.com`)
   - `DATABASE_URL`: Paste the Internal Database URL from Step 1
   - `PYTHON_VERSION`: `3.12.0`

### Step 4: Verify Deployment
1. Wait for the build to complete (3-5 minutes)
2. Visit your Render URL
3. Test the application:
   - Homepage loads correctly
   - Static files (CSS, images) display properly
   - Admin panel works at `/admin/`
   - Database operations function correctly

### Step 5: Create Superuser
After deployment, create an admin user:

1. Go to Render Dashboard → Your Web Service
2. Click "Shell" tab
3. Run:
```bash
python manage.py createsuperuser
```
4. Follow the prompts to create your admin account

## Environment Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key for cryptographic signing | `django-insecure-xyz123...` |
| `DEBUG` | Debug mode (should be False in production) | `False` |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hostnames | `myapp.onrender.com,localhost` |
| `DATABASE_URL` | PostgreSQL connection string (auto-set by Render) | `postgresql://user:pass@host/db` |

## Database Management

### Running Migrations
Migrations run automatically during deployment via `build.sh`. To run manually:
```bash
python manage.py migrate
```

### Creating a Backup
```bash
# In Render Shell
python manage.py dumpdata > backup.json
```

### Loading Data
```bash
python manage.py loaddata backup.json
```

## Static and Media Files

### Static Files
- Served by WhiteNoise in production
- Automatically collected during build
- Compressed and cached for performance

### Media Files (User Uploads)
⚠️ **Important:** Render's filesystem is ephemeral. For persistent media storage, consider:
- **Cloudinary** - Free tier available
- **AWS S3** - Industry standard
- **Render Disks** - Persistent storage add-on

To implement Cloudinary:
```bash
pip install cloudinary django-cloudinary-storage
```

Update `settings.py`:
```python
INSTALLED_APPS = [
    # ...
    'cloudinary_storage',
    'cloudinary',
]

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': getenv('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': getenv('CLOUDINARY_API_KEY'),
    'API_SECRET': getenv('CLOUDINARY_API_SECRET'),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

## Security Features Enabled

✅ HTTPS redirect in production  
✅ Secure cookies  
✅ CSRF protection  
✅ XSS filtering  
✅ Content type sniffing prevention  
✅ HSTS (HTTP Strict Transport Security)  
✅ X-Frame-Options protection  

## Troubleshooting

### Build Fails
- Check `requirements.txt` for correct package versions
- Verify `build.sh` has execute permissions
- Review build logs in Render dashboard

### Static Files Not Loading
- Ensure `collectstatic` ran successfully
- Check WhiteNoise configuration in settings
- Verify `STATIC_ROOT` and `STATIC_URL` settings

### Database Connection Issues
- Confirm `DATABASE_URL` is set correctly
- Check PostgreSQL database is running
- Verify database migrations completed

### 500 Server Error
- Set `DEBUG=True` temporarily to see error details
- Check application logs in Render dashboard
- Verify all environment variables are set

## Maintenance

### Updating the Application
1. Make changes locally
2. Test thoroughly
3. Commit and push to GitHub
4. Render auto-deploys from main branch (if enabled)

### Monitoring
- Monitor logs in Render Dashboard
- Set up error tracking (e.g., Sentry)
- Use Render's built-in metrics

### Scaling
Free tier limitations:
- Service spins down after 15 minutes of inactivity
- First request after spin-down takes 30-60 seconds

Upgrade to paid tier for:
- Always-on service
- More resources
- Custom domains
- Better performance

## Additional Resources
- [Render Django Deployment Guide](https://render.com/docs/deploy-django)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)
- [WhiteNoise Documentation](http://whitenoise.evans.io/)

## Support
For issues specific to this deployment:
1. Check Render documentation
2. Review Django deployment best practices
3. Examine application logs in Render dashboard

---

**Your Django blog is now production-ready! 🚀**
