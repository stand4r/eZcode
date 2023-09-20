from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///links.db"
db = SQLAlchemy(app)

class Links(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    likes = db.Column(db.Integer, default=0)
    dislikes = db.Column(db.Integer, default = 0)
    about = db.Column(db.Text, default = "")
    isActive = db.Column(db.Boolean, default=True)
    
@app.route("/")
@app.route("/index")
def index():
    return "Hello world"


if __name__ == "__main__":
    app.run()