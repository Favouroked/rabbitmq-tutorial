import os

config = {
    'rabbitmq': {
        'host': os.getenv('RABBITMQ_HOST'),
        'port': os.getenv('RABBITMQ_PORT'),
        'username': os.getenv('RABBITMQ_USERNAME'),
        'password': os.getenv('RABBITMQ_PASSWORD'),
        'queue_name': os.getenv('RABBITMQ_QUEUE_NAME')
    },
    'app': {
        'host': os.getenv('APP_HOST'),
        'port': os.getenv('APP_PORT')
    },
    'mailgun': {
        'domain': os.getenv('MAILGUN_DOMAIN'),
        'apiKey': os.getenv('MAILGUN_API_KEY')
    }
}
