"""Entrypoint de aplicação."""

from config.base import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
