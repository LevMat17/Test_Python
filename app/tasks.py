import datetime

from settings import *
import json


class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)#datetime.now().strftime("%H:%M:%S"))
    last_update = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)#datetime.now().strftime("%H:%M:%S"))
    priority = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(80), nullable=False)

    def json(self):
        return {'id': self.id, 'name': self.name, 'priority' : self.priority, 'description' : self.description,
                'creation_date': self.creation_date, 'last_update': self.last_update}

    def add_task(_name, _priority, _description):
        new_task = Task(name=_name, priority=_priority, description=_description)
        db.session.add(new_task)
        db.session.commit()
        return new_task

    def get_value(value):
        return task.get(value)

    def get_priority():
        return task.get("priority")

    def get_all_tasks():
        return [Task.json(task) for task in Task.query.all()]

    def get_task_by_id(_id):
        task = Task.query.filter_by(id=_id).first()

        if not task:
            raise ValueError("No task id : " + str(_id))

        return [Task.json(task)]

    def get_task_by_value(value):
        tasks = [Task.json(task) for task in Task.query.order_by(value).all()]
        return tasks

    def update_task(_id, _name, _priority, _description):
        task_to_update = Task.query.filter_by(id=_id).first()
        if not task_to_update:
            raise ValueError("No task id : " + str(_id))

        modif=False

        if _name :
            task_to_update.name = _name
            modif = True

        if _priority :
            task_to_update.priority = _priority
            modif = True

        if _description :
            task_to_update.description = _description
            modif = True

        if modif :
            task_to_update.last_update = datetime.datetime.now()

        db.session.commit()

        return task_to_update.json()

    def delete_task(_id):
        Task.query.filter_by(id=_id).delete()
        db.session.commit()
