from flask import Flask, request, render_template, redirect, url_for

from forms import TodoForm
from todosSQL import todos

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

@app.route("/todos/", methods=["GET", "POST"])
def todos_list():
    form = TodoForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            values=[] 
            for v in form.data.values():
                values.append(v)
            todos.create(values)
        return redirect(url_for("todos_list"))

    return render_template("todos.html", form=form, todos=todos.all(), error=error)


@app.route("/todos/<int:todo_id>/", methods=["GET", "POST"])
def todo_details(todo_id):
    todo = todos.get(todo_id)
    form = TodoForm(data=todo)
    if request.method == "POST":
        if form.validate_on_submit():
            todos.update(todo_id, form.data)
        return redirect(url_for("todos_list"))
    return render_template("todo.html", form=form, todo_id=todo_id)


if __name__ == "__main__":
    app.run(debug=True)