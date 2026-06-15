import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rainwatch.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = 'admin'
email = 'admin@exemplo.com'
password = 'senhalegal23'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superuser {username} criado com sucesso!")
else:
    print(f"Superuser {username} já existe.")
