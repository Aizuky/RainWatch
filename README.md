>RainWatch

O RainWatch é uma plataforma web desenvolvida em Django para monitoramento de sensores de chuva e saturação do solo em áreas urbanas de Recife/PE, permitindo a visualização de riscos de enchentes e deslizamentos em tempo real.

O sistema centraliza informações de sensores, alertas automáticos e localização de abrigos seguros, auxiliando no gerenciamento preventivo de situações de risco. O projeto possui interface moderna, responsiva e organizada para facilitar a visualização dos dados críticos.

>Equipe

| Nome                        | GitHub         |
| --------------------------- | -------------- |
| João Braga Salgado          | @Joaobsbr      |
| Clécio Francisco de Almeida | @Aizuky        |
| Pedro Henrique              | @pedro06ph-hub |
| Thiago Santos               | @Thtech01      |

>Tecnologias Utilizadas

* Python 3.x
* Django 6.0.4
* SQLite3
* HTML5
* CSS3
* JavaScript
* WhiteNoise
* Django Authentication System

Funcionalidades Implementadas

Escopo Implementado: Avançado

-Monitoramento de Sensores

* Exibição de sensores em "tempo real"
* Monitoramento de chuva (mm)
* Monitoramento de saturação do solo
* Classificação automática de risco:

  * Normal
  * Alerta
  * Crítico

-Central de Alertas

* Geração automática de alertas
* Disparo manual de alertas
* Histórico de alertas
* Controle de status:

  * Enviado
  * Falha
  * Pendente
  * Ignorado

-Gerenciamento de Destinatários

* Cadastro de destinatários
* Configuração de canais:

  * Email
  * SMS
  * Webhook
* Ativação/desativação de notificações

-Sistema de Abrigos

* Visualização de abrigos seguros
* Filtro por bairro
* Busca por nome
* Capacidade máxima dos abrigos
* Associação do abrigo ao nível de risco da região

-Sistema de Usuários

* Login
* Logout
* Proteção de rotas autenticadas

-Interface Responsiva

* Layout adaptável para desktop e mobile
* Dashboard moderno
* Indicadores visuais em tempo real

>Pré-requisitos

Antes de executar o projeto, é necessário possuir instalado:

* Python 3.10 ou superior
* pip
* virtualenv

>Como Executar o Projeto Localmente

1. Clonar o repositório:

git clone https://github.com/SEU-USUARIO/RainWatch.git


2. Entrar na pasta do projeto:

cd RainWatch

3. Criar ambiente virtual:

-Windows:

python -m venv venv

-Linux/Mac:

python3 -m venv venv

4. Ativar ambiente virtual

-Windows

venv\Scripts\activate

-Linux/Mac

source venv/bin/activate

5. Instalar dependências

pip install -r requirements.txt

6. Instalar o dj_database_url

pip install dj_database_url

7. Criar os arquivos de migração

python manage.py makemigrations

8. Executar migrações

python manage.py migrate

9. Instalar o whitenoise

pip install whitenoise

10. Iniciar servidor

python manage.py runserver

11. Acessar no navegador

https://rain-watch-nine.vercel.app/sensores/dashboard/
>>>>>>> bf6ba71 (Fix: Injeção do dynatrace nos arquivos html e alteração no README)

>Usuários de Teste

| Usuário | Senha    |
| ------- | -------- |
| admin   | admin123 |
| teste   | teste123 |

>Estrutura do Projeto

RainWatch-main/
│
├── __pycache__/
├── .vscode/
├── abrigos/
├── alertas/
├── rainwatch/
├── sensores/
├── staticfiles
├── templates/
├── usuarios/
├── .env
├── .env.exemplo
├── .gitignore
├── build.sh
├── db.sqlite3
├── manage.py
├── popular_banco.py
├── README.md
├── requirements.txt
└── vercel.json
venv/

