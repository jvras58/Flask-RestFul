"""Entrypoint de aplicação."""

from config.base import create_app
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from resources.todo import Todo, TodoList

app = Flask(__name__)
CORS(app)

app = create_app()
api = Api(app)

api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
