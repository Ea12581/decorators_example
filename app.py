from flask import Flask, request, jsonify
import decorators
from decorators import log_call, timer, delay

#mock db
mock_users = {
    1: {"username": "alice", "email": "alice@example.com"},
    2: {"username": "bob", "email": "bob@example.com"},
    3: {"username": "charlie", "email": "charlie@example.com"},
    4: {"username": "diana", "email": "diana@example.com"},
}

app = Flask(__name__)


@app.route('/')
@log_call
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/users', methods=['GET', 'POST'])
@log_call
@timer
@delay(rate=1)
def users():
    if request.method == 'GET':
        user_id = int(request.args.get('user_id'))
        if not user_id:
            return jsonify({'error': 'No user id provided'}), 400

        try:
            user_id = int(user_id)
        except ValueError:
            return jsonify({'error': 'Invalid user id'}), 400

        if user_id in mock_users:
            return jsonify(mock_users[user_id]), 200
        else:
            return jsonify({"error":"user not found"}), 404
    elif request.method == 'POST':
        data = request.get_json()
        if not data or "username" not in data or "email" not in data:
            return jsonify({"error": "username and email are required"}), 400
        new_user = {"username": data["username"], "email": data["email"]}
        new_id = max(mock_users.keys()) + 1
        users[new_id] = new_user
        return jsonify({"id" : new_id, "username" : data["username"], "email": data["email"]}), 201





@app.route('/echo', methods=['POST'])
@log_call
@timer
@delay(rate=1)
def echo():
    data = request.get_json()  # get JSON body
    return {"you_sent": data}, 200



if __name__ == '__main__':
    app.run(debug=True)

