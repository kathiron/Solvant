from flask_restx import Resource, marshal_with, fields, Namespace
from flask import request
from custom.database.sql_server.repository.customer_repository import CustomerRepository
from custom.utils.api_common import *

# from flask_restx import Resource, fields, Namespace
# from custom.repositories.customer_repository import CustomerRepository
# from custom.utils.api_common_util import ApiCommon

# Define the namespace
customer_ns = Namespace('customers', description='Customer operations')

# Define the expected model for input and output
customer_model = customer_ns.model('Customer', {
    'name': fields.String(required=True, description='The customer name'),
    'age': fields.Integer(required=True, description='The customer age'),
    'city': fields.String(required=True, description='The customer city'),
})

# Combined CustomerResource class
@customer_ns.route('/')
class CustomerResource(Resource):
    @customer_ns.doc('create_customer')
    @customer_ns.expect(customer_model)
    def post(self):
        # Insert new customer
        data = ApiCommon.get_request_data()
        result = CustomerRepository().insert_data(data)
        return ApiCommon.to_data_format_response(result)

    @customer_ns.doc('get_all_customers')
    def get(self):
        # Fetch a specific customer by ID
        data = CustomerRepository().fetch_data()
        print(f"Fetched customer with ID {id}: {data}")
        return ApiCommon.to_data_format_response(data)

@customer_ns.route('/<int:id>')
@customer_ns.param('id', 'The customer identifier')
class CustomerDetailResource(Resource):
    @customer_ns.doc('get_customer')
    def get(self, id):
        # Fetch all customers if no ID is provided
        data = CustomerRepository().get_data(id)
        return ApiCommon.to_data_format_response(data)

    @customer_ns.doc('update_customer')
    @customer_ns.expect(customer_model)
    def put(self, id):
        # Update customer by ID
        data = ApiCommon.get_request_data()
        data['id'] = id
        result = CustomerRepository().update_data(data)
        return ApiCommon.to_data_format_response(result)