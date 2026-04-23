from app import app, init_db

# Inicializa o banco quando o Gunicorn importa este módulo
init_db()

if __name__ == '__main__':
    app.run()
