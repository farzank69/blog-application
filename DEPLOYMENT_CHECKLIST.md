# Quick Deployment Checklist

## ✅ Pre-Deployment Checklist

- [x] Settings configured for production
- [x] Database configured (PostgreSQL)
- [x] Static files setup with WhiteNoise
- [x] Security settings enabled
- [x] Environment variables configured
- [x] Dependencies updated in requirements.txt
- [x] Build script created (build.sh)
- [x] .gitignore configured
- [x] Python version specified (runtime.txt)

## 🚀 Deploy to Render

### 1. Push to GitHub
```bash
git add .
git commit -m "Configure for Render deployment"
git push origin main
```

### 2. Create Render Account
- Visit: https://render.com
- Sign up/Login with GitHub

### 3. Deploy Using Blueprint (Easy Way)
1. Click "New +" → "Blueprint"
2. Select your repository
3. Render auto-configures from `render.yaml`
4. Click "Apply"

### 4. Set Environment Variables
In Render Dashboard, add:
- `SECRET_KEY`: Generate new (use Django's secret key generator)
- `DEBUG`: `False`
- `ALLOWED_HOSTS`: `your-app.onrender.com`
- `DATABASE_URL`: Auto-set by Render database

### 5. Create Superuser
After deployment, in Render Shell:
```bash
python manage.py createsuperuser
```

## 📋 Environment Variables Needed

```
SECRET_KEY=<generate-new-secret-key>
DEBUG=False
ALLOWED_HOSTS=<your-app>.onrender.com
DATABASE_URL=<auto-set-by-render>
```

## 🔧 Post-Deployment

- [ ] Test homepage
- [ ] Test admin panel
- [ ] Verify static files load
- [ ] Check database operations
- [ ] Create superuser
- [ ] Test creating posts

## ⚠️ Important Notes

1. **Media Files**: Render filesystem is ephemeral
   - Use Cloudinary or AWS S3 for uploaded images
   - Current uploads stored in `/uploads/` will be lost on redeploy

2. **Free Tier**: Service spins down after 15 mins inactivity
   - First request may take 30-60 seconds

3. **Database**: PostgreSQL provided by Render
   - Backup regularly using `dumpdata`

## 🆘 Quick Troubleshooting

**Build Fails?**
- Check build logs in Render dashboard
- Verify all dependencies in requirements.txt

**Static Files Not Loading?**
- Check WhiteNoise middleware position
- Verify collectstatic ran in build

**Database Errors?**
- Confirm DATABASE_URL is set
- Check migrations completed

**500 Error?**
- Temporarily set DEBUG=True to see details
- Check application logs

## 📚 Documentation

Full guide: See `DEPLOYMENT.md`
