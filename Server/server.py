from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request
from flask import jsonify

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///links.db"
db = SQLAlchemy(app)


class Links(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    link = db.Column(db.String(200), default="")
    likes = db.Column(db.Integer, default=0)
    dislikes = db.Column(db.Integer, default = 0)
    about = db.Column(db.Text, default = "")
    isActive = db.Column(db.Boolean, default=True)
   
    
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/api", methods=["GET"])
def get_links():
    links = db.session.query(Links).all()
    links_dict = [link.__dict__ for link in links]
    for link_dict in links_dict:
        link_dict.pop('_sa_instance_state')
    return jsonify(links_dict)


@app.route("/api/<int:id>", methods=["GET"])
def get_link(id):
    link = db.session.get(Links, id)
    if link is None:
        return jsonify({'error': 'Link not found'}), 404
    else:
        link_dict = link.__dict__
        link_dict.pop('_sa_instance_state')
        return jsonify(link_dict)


@app.route('/api', methods=['POST'])
def create_user():
    data = request.get_json()
    if 'about' not in data or 'link' not in data:
        return jsonify({'message': 'Link is required required'}), 400
    else:
        link = Links(link=data['link'], about=data['about'])
        db.session.add(link)
        db.session.commit()
        link_dict = link.__dict__
        link_dict.pop('_sa_instance_state')
        return jsonify(link_dict), 201


@app.route('/api', methods=['PUT'])
def update_user():
    data = request.get_json()
    if 'id' not in data:
        return jsonify({'message': 'Link is required'}), 400
    else:
        link = db.session.get(Links, int(data['id']))
        if link is None:
            return jsonify({'error': 'Link not found'}), 404
        else:
            if 'id' not in data:
                return jsonify({'message': 'Link is required'}), 400
            else:
                if 'link' in data:
                    link.link = data['link']
                if 'likes' in data:
                    link.likes = data['likes']
                if 'dislikes' in data:
                    link.dislikes = data['dislikes']
                if 'about' in data:
                    link.about = data['about']
                if 'isActive' in data:
                    link.isActive = data['isActive']
                db.session.commit()
                link_dict = link.__dict__
                link_dict.pop('_sa_instance_state')
                return jsonify(link_dict), 200


@app.route('/api/<int:id>', methods=['DELETE'])
def delete_user(id):
    link = db.session.get(Links, id)
    if link is None:
        return jsonify({'message': 'Link not found'}), 404
    else:
        db.session.delete(link)
        db.session.commit()
        return '', 204


if __name__ == "__main__":
    app.run(debug=False)