from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {
    "id": 0,
    "name": "Charles",
    "job_title": "SRE",
    "communicate_information": {
        "email": "charles@gmail.com",
        "mobile": "09XX-XXX-XXX"
        }
    }
]

@app.route('/user')
def get_user():
    return jsonify(users)

@app.route('/user', methods=['POST'])
def create_user():
    request_data = request.get_json()
    new_user = {
        "id": request_data['id'],
        "name": request_data['name'],
        "job_title": request_data['job_title'],
        "communicate_information": {
            "email": request_data['communicate_information']['email'],
            "mobile": request_data['communicate_information']['mobile']
        }
    }
    users.append(new_user)
    return jsonify(users)

@app.route('/user', methods=['PUT'])
def update_user():
    request_data = request.get_json()

    update_user = {
        "id": request_data['id'],
        "name": request_data['name'],
        "job_title": request_data['job_title'],
        "communicate_information": {
            "email": request_data['communicate_information']['email'],
            "mobile": request_data['communicate_information']['mobile']
        }
    }
    
    users[request_data['id']] = update_user
    return jsonify(users)

@app.route('/user', methods=['DELETE'])
def delete_user():
    request_data = request.get_json()
    del_user = {
        "id": request_data['id'],
        "name": request_data['name'],
        "job_title": request_data['job_title'],
        "communicate_information": {
            "email": request_data['communicate_information']['email'],
            "mobile": request_data['communicate_information']['mobile']
        }
    }
    users.remove(del_user)
    return jsonify(users)  

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)