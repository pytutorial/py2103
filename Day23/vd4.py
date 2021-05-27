from flask import Flask, request

app = Flask(__name__)

taskList = [
    {'id': 1, 'name': 'Task 1', 'estimated_time': '2h'},
    {'id': 2, 'name': 'Task 2', 'estimated_time': '3h'},
    {'id': 3, 'name': 'Task 3', 'estimated_time': '4h'},
]

@app.route('/')
def index():
    html  = '<ul>'
    for task in taskList:
        taskId = task['id']
        taskName = task['name']
        html += f'<li><a href="/view-task-detail?id={taskId}"> {taskName} </a></li>'
    html + '</ul>'
    return html  

#127.0.0.1:5000/view-task-detail?id=1
@app.route('/view-task-detail')
def viewTask():
    taskId = int(request.args.get('id', -1))
    print('taskId=', taskId)
    task = taskList[taskId-1]
    return f'''
        <div>
            <p>Task: {task["name"]}</p>
            <p>Thời lượng dự kiến hoàn thành : {task["estimated_time"]}</p>
        </div>
    '''

app.run(debug=True)