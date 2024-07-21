import os
import django
from django.urls import get_resolver

# Set the default settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mybackend.settings')

# Set up Django
django.setup()

# Get and print URL patterns
url_patterns = get_resolver().url_patterns
for pattern in url_patterns:
    print(pattern)
