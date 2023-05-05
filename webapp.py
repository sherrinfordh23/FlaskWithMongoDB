from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
from connection import client
from bson import ObjectId


app = Flask(__name__)
db = client.taskmaster
tasks_collection = db.tasks



@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        task_content = request.form['content']
        
        new_task = {
            "content": task_content,
            "date_created": datetime.now()
        }
        
        try:
            tasks_collection.insert_one(new_task)
            return redirect('/')
        except:
            return 'There was an issue adding your task'
    
    else:
        tasks = []
        cursor = tasks_collection.find()
        for item in cursor:
            tasks.append(item)
        return render_template('index.html', tasks=tasks)


@app.route('/delete/<string:id>')
def delete(id):
    task_to_delete = {"_id": ObjectId(id)}
    try:
        tasks_collection.delete_one(task_to_delete)
        return redirect('/')
    except:
        return 'There was an issue deleting your task'

@app.route('/update/<string:id>', methods=['GET', 'POST'])
def update(id):
    task_to_update = {"_id": ObjectId(id)}
    if request.method == 'POST':
        task_content = request.form['content']
        change_content = {"$set": {"content": task_content}}
        try:
            tasks_collection.update_one(task_to_update, change_content)
            return redirect('/')
        except:
            return 'There was an issue updating your task'
    else:
        task = tasks_collection.find_one(task_to_update)
        return render_template('update.html', task=task)




if __name__ == "__main__":
    app.run(debug=True)