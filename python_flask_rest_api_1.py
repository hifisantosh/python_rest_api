# Author: Santosh Kumar
# Created On: 11-Apr-2019
# Description: This is sample code to create REST api using Flask in python

from flask import Flask, jsonify, request

app = Flask('Customer')

customers = [
           {
             'id': '100431',
           'name': 'John Lee',
           'type': 'brownze',
           'city': 'New York',
           'country': 'USA'
           },
           {
             'id': '340021',
           'name': 'David Miller',
           'type': 'gold',
           'city': 'Sydney',
           'country': 'Australia'
           }
           ]

# POST - client used to send data
# GET - used to read data by client

# POST /customer data: {name:}
@app.route('/customer', methods=['POST'])
def add_customer():
    request_data = request.get_json()
    new_customer = {
        'id': request_data['id'],
        'name': request_data['name'],
        'type': request_data['type'],
        'city': request_data['city'],
        'country': request_data['country']
    }
    customers.append(new_customer)
    return jsonify(new_customer)

# GET /customer/<string:id>
@app.route('/customer/<string:id>')
def get_customer(id):
    for customer in customers:
        if customer['id'] == id:
            return jsonify(customer)
    return jsonify({'error message': 'customer not found'})

# GET /customer
@app.route('/customer')
def get_customers():
    return jsonify({'customers': customers})

# DELETE /customer
@app.route('/customer/<string:id>', methods=['DELETE'])
def delete_customer(id):
    request_data = request.get_json()
    for customer in customers:
        if customer['id'] == id:
            customers.remove(customer)
            return jsonify({'message': 'customer deleted successfully'})
    return jsonify({'error message': 'customer not found'})

# run localhost at port 1950
app.run(port=1950)
