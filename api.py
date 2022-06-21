from tasks import *

@app.route("/task", methods=["POST"])
def add_task():
    request_data = request.get_json()
    task = Task.add_task(request_data["name"], request_data["priority"],
                    request_data["description"])
    # response = Response(str(jsonify({'Task', task})), 201, mimetype='application/json')
    # return response
    response = make_response(jsonify(Task= task.json()), 201)
    return response

@app.route("/tasks", methods=["GET"])
def get_all_tasks():

    priority = int(request.args.get('priority'))
    # temporality = request.args.get('temporality')

    if priority:
        tasks = Task.get_task_by_priority(priority)
    else :
        tasks = Task.get_all_tasks()

    return make_response(jsonify(Task=tasks), 200)

@app.route("/task/<int:id>", methods=["GET"])
def get_task(id):
    try:
        task = Task.get_task_by_id(id)
        response = make_response(jsonify(Task=task), 200)
    except ValueError as e:
        response = make_response(jsonify(error=str(e)), 404)

    return response

@app.route("/task/<int:id>", methods=["DELETE"])
def delete_task(id):
    Task.delete_task(id)
    response = Response("Task Deleted", status=200, mimetype='application/json')
    return response

@app.route("/task/<int:id>", methods=["PUT"])
def update_task(id):
    request_data = request.get_json()
    try:
        task = Task.update_task(id, request_data['name'], request_data['priority'], request_data['description'])
        response = make_response(jsonify(Task=task), 200)
    except ValueError as e:
        response = make_response(jsonify(error=str(e)), 404)

    return response


if __name__ == "__main__":
    app.run(port=5000, debug=True)
