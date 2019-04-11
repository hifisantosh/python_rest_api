# Author: Santosh Kumar
# Created On: 11-Apr-2019
# Description: This is sample code to create REST api using Flask in python

from flask import Flask, jsonify, request

app = Flask('friends_network')

friends = [
{
    'name': 'John Warner',
    'friend_list': [
        {
        'name': 'David Karter',
        'sex': 'M',
        'city': 'New York'
        },
        {
        'name': 'Mary Augustin',
        'sex': 'F',
        'city': 'Chicago'
        }
    ]
}
]

# POST - client used to send data
# GET - used to read data by client

# POST /friend data: {name:}
@app.route('/friend', methods=['POST'])
def add_friend():
    request_data = request.get_json()
    new_friend = {
        'name': request_data['name'],
        'friend_list': []
    }
    friends.append(new_friend)
    return jsonify(new_friend)
# GET /friend/<string:name>
@app.route('/friend/<string:name>')
def get_friend(name):
    for friend in friends:
        if friend['name'] == name:
            return jsonify(friend)
    return jsonify({'error message': name + ' is not in your friend list'})
# GET /friend
@app.route('/friend')
def get_friends():
    return jsonify({'friends': friends})

# POST /friend/<string:name>/friend_list {name:, sex:, city}
@app.route('/friend/<string:name>/friend_list', methods=['POST'])
def add_new_friend(name):
    for friend in friends:
        if friend['name'] == name:
            request_data = request.get_json()
            new_friend_list = {
                'name': request_data['name'],
                'sex': request_data['sex'],
                'city': request_data['city']
            }
            friend['friend_list'].append(new_friend_list)
            return jsonify(friend)
    return jsonify({'error message': name + ' is not in your friend list'})
# GET /friend/<string:name>/friend_list
@app.route('/friend/<string:name>/friend_list')
def get_friend_from_friend_list(name):
    for friend in friends:
        if friend['name'] == name:
            return jsonify({'friend_list': friend['friend_list']})
    return jsonify({'error message': name + ' is not in your friend list'})

# run localhost at port 1950
app.run(port=1950)
