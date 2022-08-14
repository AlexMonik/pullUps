from os import getenv

TOKEN = getenv('BOT_TOKEN')
HEROKU_APP_NAME = getenv('HEROKU_APP_NAME')
# webhook settings
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = getenv('WEBAPP_HOST', default='0.0.0.0')
WEBAPP_PORT = getenv('WEBAPP_PORT', default=8001)
