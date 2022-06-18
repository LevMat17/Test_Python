from tasks import *

@app.route("/task", methods=["POST"])
def add_task():
    request_data = request.get_json()
    Task.add_task(request_data["name"], request_data["priority"],
                    request_data["description"])
    response = Response("Task added", 201, mimetype='application/json')
    return response

@app.route("/tasks", methods=["GET"])
def get_all_tasks():

    priority = int(request.args.get('priority'))
    # temporality = request.args.get('temporality')
    print (priority)
    if priority:
        tasks = Task.get_task_by_priority(priority)
    else :
        tasks = Task.get_all_tasks()

    return jsonify({'Task': tasks})

@app.route("/task/<int:id>", methods=["GET"])
def get_task(id):
    return_value = Task.get_task(id)
    return jsonify(return_value)

@app.route("/task/<int:id>", methods=["DELETE"])
def delete_task(id):
    Task.delete_task(id)
    response = Response("Task Deleted", status=200, mimetype='application/json')
    return response

@app.route("/task/<int:id>", methods=["PUT"])
def update_task(id):
    request_data = request.get_json()
    Task.update_task(id, request_data['name'], request_data['priority'], request_data['description'])
    response = Response("Task Updated", status=200, mimetype='application/json')
    return response


@app.route("/swagger")
def swag():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "My API"
    return jsonify(swag)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
