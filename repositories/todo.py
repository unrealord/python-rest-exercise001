import uuid


class TodoRepository(object):

    todos_db = dict()


    #
    # Create a new resource
    #
    def create_todo(self, todo_payload):
        todo_id = str(uuid.uuid4())
        self.todos_db[todo_id] = todo_payload
        todo_payload['id'] = todo_id
        return todo_payload