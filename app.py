from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db=SQLAlchemy(app)

class Todo(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(500),nullable=False) 
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno}-{self.title}"
#  to create todo.db use ""flask shell"" on cmd then db.create_all()



@app.route("/")
def hello():
    allTodo=Todo.query.all()

    return render_template("index.html",allTodo=allTodo)

@app.route("/login")


def hllo():
    return "hello world"
if __name__=="__main__":
    app.run(debug=True,port=8000)
