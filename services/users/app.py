from flask import Flask

from flask_restplus import Api
from s_apis import test

app = Flask(__name__)
api = Api(app)

if __name__ == '__main__':
    api.add_namespace(test.api)
    app.run(host='0.0.0.0', port=5000)
