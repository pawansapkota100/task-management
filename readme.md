to view only the tasks they have created.
get request
http://127.0.0.1:8000/tasks/

to retreve the tasks they have created.
get request
http://127.0.0.1:8000/tasks/1/

to create the task:
post req
http://127.0.0.1:8000/tasks/

action to mae the task complete
post req
http://127.0.0.1:8000/tasks/9/complete/

to update the task
patch req
http://127.0.0.1:8000/tasks/7/

to delete the task
delete req
http://127.0.0.1:8000/tasks/8/

filter the tasks by priority and status
http://127.0.0.1:8000/tasks/?status=I&&priority=H

to search the task by name
http://127.0.0.1:8000/tasks/?search=testing task
