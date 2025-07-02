from flask import Flask
from flask import request


#mock db
mock_users = {
    1: {"username": "alice", "email": "alice@example.com"},
    2: {"username": "bob", "email": "bob@example.com"},
    3: {"username": "charlie", "email": "charlie@example.com"},
    4: {"username": "diana", "email": "diana@example.com"},
}

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()  # get JSON body
    return {"you_sent": data}, 200



if __name__ == '__main__':
    app.run(debug=True)

