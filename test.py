from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {
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
    find = [request_data for request_data in users if request_data['name'] == users['name'] ]
    # update_user = {
    #     "name": request_data['name'],
    #     "job_title": request_data['job_title'],
    #     "communicate_information": {
    #         "email": request_data['communicate_information']['email'],
    #         "mobile": request_data['communicate_information']['mobile']
    #     }
    # }

    if len(find) == 0:
        return {'message': 'user is not exist'}
    user = find[0]
    user['name'] = request_data['name']
    user['job_title'] = request_data['job_title']
    user['communicate_information']['email'] = request_data['communicate_information']['email']
    user['communicate_information']['mobile'] = request_data['communicate_information']['mobile']

    return jsonify(users)

@app.route('/user', methods=['DELETE'])
def delete_user():
    request_data = request.get_json()
    del_user = {
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
    app.run('0.0.0.0', port=5001, debug=True)