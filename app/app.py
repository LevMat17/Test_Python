from tasks import *

@app.route("/task", methods=["POST"])
def add_task():
    request_data = request.get_json()
    task = Task.add_task(request_data["name"], request_data["priority"],
                    request_data["description"])
    response = make_response(jsonify(Task= task.json()), 201)
    return response

@app.route("/task", methods=["GET"])
def get_all_tasks():

    print(request.args.get("sortby"))
    if request.args.get("sortby"):
        if request.args.get("sortby") == "priority" or request.args.get("sortby") == "creation_date" or request.args.get("sortby") == "last_update":
            tasks = Task.get_task_by_value(request.args.get("sortby"))
            response = make_response(jsonify(Task=tasks), 200)
        else :
            response = make_response("no key with value : " + request.args.get("sortby"), 400)
    else:
        tasks = Task.get_all_tasks()
        response = make_response(jsonify(Task=tasks), 200)

    return response

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
    request_update = request.get_json()
    try:
        new_name=None
        new_priority=None
        new_description=None

        if "name" in request_update:
            new_name = request_update['name']
        if "priority" in request_update:
            new_priority = request_update['priority']
        if "description" in request_update:
            new_description = request_update['description']

        task = Task.update_task(id, new_name, new_priority, new_description)
        response = make_response(jsonify(Task=task), 200)
    except ValueError as e:
        response = make_response(jsonify(error=str(e)), 404)

    return response


if __name__ == "__main__":
    db.create_all()
    app.run(port=5000, debug=True, host="0.0.0.0")
