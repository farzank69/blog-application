# Django Blog Application

A feature-rich blog application built with Django, featuring posts, comments, tags, and a read-later functionality.

## Features

- 📝 Blog posts with rich content
- 👥 Author management
- 🏷️ Tag system for categorizing posts
- 💬 Comment system for user engagement
- 🔖 Read-later functionality using sessions
- 📱 Responsive design
- 🔒 Admin panel for content management
- 🖼️ Image upload support for posts

## Tech Stack

- **Framework:** Django 5.2.7
- **Database:** SQLite (development) / PostgreSQL (production)
- **Python:** 3.12.0
- **WSGI Server:** Gunicorn
- **Static Files:** WhiteNoise
- **Image Processing:** Pillow

## Project Structure

```
├── blog/                   # Blog application
│   ├── models.py          # Post, Author, Tag, Comment models
│   ├── views.py           # Class-based views
│   ├── forms.py           # Comment form
│   ├── urls.py            # URL routing
│   ├── templates/         # HTML templates
│   └── static/            # CSS and images
├── my_site/               # Project settings
│   ├── settings.py        # Configuration
│   ├── urls.py            # Root URL config
│   └── wsgi.py            # WSGI configuration
├── templates/             # Base templates
├── static/                # Global static files
├── uploads/               # Media uploads
├── requirements.txt       # Python dependencies
├── build.sh              # Render build script
├── render.yaml           # Render configuration
└── manage.py             # Django management script
```

## Local Development Setup

### Prerequisites
- Python 3.12+
- pip
- virtualenv (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Section-11
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

8. **Run development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - Homepage: http://localhost:8000
   - Admin: http://localhost:8000/admin

## Production Deployment

This project is configured for deployment on Render.

### Quick Deploy
1. Push to GitHub
2. Create Render account
3. Use Blueprint deployment with `render.yaml`

For detailed instructions, see:
- **Full Guide:** [DEPLOYMENT.md](DEPLOYMENT.md)
- **Quick Reference:** [DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md)

## Database Models

### Post
- Title, slug, excerpt, content
- Publication date (auto-generated)
- Image upload
- Author (Foreign Key)
- Tags (Many-to-Many)

### Author
- First name, last name
- Email address
- Full name method

### Tag
- Caption (unique identifier)

### Comment
- User name and email
- Comment text
- Related post (Foreign Key)

## URL Structure

- `/` - Homepage (latest 3 posts)
- `/posts` - All posts
- `/posts/<slug>` - Individual post detail
- `/read-later` - Saved posts
- `/admin` - Admin panel

## Configuration

### Environment Variables
```
SECRET_KEY=<your-secret-key>
DEBUG=True|False
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=<postgresql-url>  # Production only
```

### Static Files
- Development: Served by Django
- Production: Served by WhiteNoise

### Media Files
- Development: Local filesystem
- Production: Recommend Cloudinary or S3

## Security Features

Production deployment includes:
- ✅ HTTPS redirect
- ✅ Secure cookies
- ✅ CSRF protection
- ✅ XSS filtering
- ✅ HSTS headers
- ✅ Content type sniffing prevention

## Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Adding Sample Data
Use Django admin panel or Django shell:
```bash
python manage.py shell
```

## Common Tasks

### Add a new blog post
1. Login to admin panel
2. Create Author (if needed)
3. Create Tags (if needed)
4. Create Post with title, content, slug, etc.

### Manage comments
- Comments appear on individual post pages
- Moderate via admin panel

## Troubleshooting

### Static files not loading
```bash
python manage.py collectstatic --clear
python manage.py collectstatic
```

### Database issues
```bash
python manage.py migrate --run-syncdb
```

### Permission errors
```bash
chmod +x build.sh
```

## Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open pull request

## License

This project is for educational purposes.

## Support

For deployment issues, see [DEPLOYMENT.md](DEPLOYMENT.md)

For general Django help, visit [Django Documentation](https://docs.djangoproject.com/)

---

**Built with Django 🎯**
