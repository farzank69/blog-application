# Cloudinary Setup Guide for Blog Application

## What is Cloudinary?
Cloudinary is a cloud-based image and video management service. We're using it to store blog post images because Render's free tier has ephemeral storage (files get deleted when the service restarts).

---

## Step-by-Step Setup

### 1. Create Cloudinary Account

1. Go to https://cloudinary.com/
2. Click **"Sign Up"** 
3. Choose **"Sign up for free"**
4. Complete registration with your email
5. Verify your email address

### 2. Get Your Credentials

After logging in:
1. You'll see your **Dashboard**
2. Look for the **Account Details** section
3. Copy these three values:
   - **Cloud Name**: (e.g., `dxyz123abc`)
   - **API Key**: (e.g., `123456789012345`)
   - **API Secret**: (e.g., `abcdef1234567890`) - Click "👁️ Show" to reveal

---

## Local Development Setup

### 1. Update Your `.env` File

Replace the placeholder values in `.env` with your actual Cloudinary credentials:

```env
CLOUDINARY_CLOUD_NAME=your_actual_cloud_name
CLOUDINARY_API_KEY=your_actual_api_key
CLOUDINARY_API_SECRET=your_actual_api_secret
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Test Locally

```bash
python manage.py runserver
```

Go to http://localhost:8000/admin and try uploading an image to a post. It should upload to Cloudinary!

---

## Production Setup (Render)

### 1. Add Environment Variables to Render

1. Go to your Render Dashboard: https://dashboard.render.com/
2. Click on your **Web Service** (django-blog)
3. Go to **"Environment"** tab
4. Click **"Add Environment Variable"** for each:

| Key | Value |
|-----|-------|
| `CLOUDINARY_CLOUD_NAME` | Your cloud name from Cloudinary |
| `CLOUDINARY_API_KEY` | Your API key from Cloudinary |
| `CLOUDINARY_API_SECRET` | Your API secret from Cloudinary |

5. Click **"Save Changes"**

Your service will automatically redeploy with Cloudinary configured!

---

## How to Upload Images

### Via Django Admin

1. Go to `/admin/`
2. Login with your superuser account
3. Click on **Posts**
4. Create or edit a post
5. Upload an image in the **Image** field
6. Save

The image will automatically upload to Cloudinary and be accessible from anywhere!

### Image URLs

Images will have URLs like:
```
https://res.cloudinary.com/your-cloud-name/image/upload/v1234567890/posts/image.jpg
```

---

## Verifying Everything Works

### 1. Check Cloudinary Dashboard

After uploading images:
1. Go to your Cloudinary dashboard
2. Click **"Media Library"**
3. You should see your uploaded images in the `posts/` folder

### 2. Check Your Live Site

Visit your Render URL and view posts - images should load from Cloudinary!

---

## Migrating Existing Images (Optional)

If you already have images in your local `uploads/` folder:

### Option 1: Upload via Django Admin
Manually re-upload each image through the admin panel.

### Option 2: Use Cloudinary Upload API
```python
# Run in Django shell: python manage.py shell

import cloudinary.uploader
from blog.models import Post

# Example: Upload a specific image
result = cloudinary.uploader.upload(
    "uploads/posts/woods.jpg",
    folder="posts"
)
print(result['url'])

# Update the post with the new URL
post = Post.objects.get(slug='your-post-slug')
post.image = result['public_id']
post.save()
```

---

## Troubleshooting

### Images Not Showing

**Check 1:** Verify environment variables are set in Render
```bash
# In Render Shell
echo $CLOUDINARY_CLOUD_NAME
```

**Check 2:** Check Cloudinary dashboard for uploaded images

**Check 3:** Look at Render logs for any Cloudinary errors

### Upload Fails

- Verify your API credentials are correct
- Check Cloudinary account is active (free tier is fine)
- Ensure you haven't exceeded free tier limits:
  - 25 GB storage
  - 25 GB bandwidth/month
  - 25,000 transformations/month

### Local Development Not Working

1. Make sure `.env` file has correct credentials
2. Install cloudinary packages: `pip install cloudinary django-cloudinary-storage`
3. Restart development server

---

## Free Tier Limits

Cloudinary free tier includes:
- ✅ 25 GB storage
- ✅ 25 GB bandwidth per month
- ✅ 25,000 transformations per month
- ✅ Perfect for a blog!

---

## Need Help?

- Cloudinary Docs: https://cloudinary.com/documentation
- Django Integration: https://cloudinary.com/documentation/django_integration
- Support: https://support.cloudinary.com/

---

## Summary

✅ Code changes made:
- Added `cloudinary` and `django-cloudinary-storage` to requirements.txt
- Updated `settings.py` to use Cloudinary for media storage
- Added Cloudinary environment variables

🔧 What you need to do:
1. Create Cloudinary account
2. Get your credentials (Cloud Name, API Key, API Secret)
3. Update `.env` file locally
4. Add environment variables to Render
5. Upload images via Django admin

That's it! Your blog images will now be stored reliably in the cloud! 🎉
