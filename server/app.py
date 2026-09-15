#!/usr/bin/env python3

import os
from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

@app.before_request
def before_request():
    g.path = os.path.abspath(os.getcwd())

@app.route('/contract/<int:id>')
def contract_information(id):
    host = request.headers.get('Host')
    appname = current_app.name
    contract = next((c for c in contracts if c["id"] == id), None)
    if contract:
        response_body = f'''
        <h1>Contract Found: {contract} requested from {host}</h1>
        <h2>App Name: {appname}</h2>
        <h3>The path of this application is: {g.path}</h3>
        '''
        status_code = 200
        return make_response(response_body, status_code)
    else:
        return {"error": "Contract not found"}, 404

@app.route('/customer/<string:customer_name>')
def customer_information(customer_name):
    host = request.headers.get('Host')
    appname = current_app.name
    if customer_name in customers:
        response_body = f'''
        <h1>Customer Found: {customer_name} requested from {host}</h1>
        <h2>App Name: {appname}</h2>
        <h3>The path of this application is: {g.path}</h3>
        '''
        status_code = 200
        return make_response(response_body, status_code)
    else:
        return {"error": "Customer not found"}, 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)
