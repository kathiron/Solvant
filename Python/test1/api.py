from flask import Flask
from flask_restx import Api, fields
from custom.apiresources.customer_resource import *

app = Flask(__name__)

# Initialize the Flask-Restx API
api = Api(app, version='1.0', title='Customer API', description='A simple Customer API')

# Add the namespace to the API
api.add_namespace(customer_ns)

if __name__ == '__main__':
    app.run(debug=True)
