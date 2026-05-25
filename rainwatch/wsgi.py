import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rainwatch.settings')

application = get_wsgi_application()
app = application

# ----- ADICIONE ESTE BLOCO LOGO ABAIXO DO 'app = application' -----
# Ele vai rodar o migrate e popular o banco automaticamente na nuvem
try:
    from django.core.management import call_command
    import sys
    
    # Executa o comando de migrate no banco Postgres
    print("Rodando migrações automáticas...")
    call_command('migrate', interactive=False)
    
    # Executa o seu script de popular banco
    print("Verificando população do banco...")
    import popular_banco
except Exception as e:
    print(f"Erro ao inicializar o banco: {e}", file=sys.stderr)
# ------------------------------------------------------------------