from flask import Flask, render_template, request, redirect, url_for
import time

app = Flask(__name__, template_folder="./")
todo_list =[]
@app.route("/")
def home():
    return render_template("todo.html",todos=todo_list)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['item']
    if len(task) > 0:
        id = int(time.time()*1000)
        todo_list.append({'id': id, 'task': task})
        print(todo_list)

    return redirect(url_for('home'))
@app.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    #id = int(id)
    for i in range(len(todo_list)):
        if todo_list[i]['id'] == id:
            todo_list.pop(i)
            break
    return redirect(url_for('home'))
