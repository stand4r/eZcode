from flask import Flask, render_template, request, jsonify, redirect, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin

app = Flask(__name__, static_folder="static/")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///links.db"
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
db = SQLAlchemy(app)

ips = {}

class Links(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(200), default="", unique=True)
    likes = db.Column(db.Integer, default=0)
    about = db.Column(db.Text, default="")
    name = db.Column(db.Text, default="")
    image = db.Column(db.Text, default="")
    tags = db.Column(db.Text, default="")

    def to_dict(self):
        link_dict = {
            "id": self.id,
            "link": self.link,
            "likes": self.likes,
            "about": self.about,
            "name": self.name,
            "image": self.image,
            "tags": self.tags.split(';')
        }
        return link_dict


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route("/api", methods=["GET"])
@cross_origin()
def get_links():
    linee = db.session.query(Links).all()
    links_dict = [link.to_dict() for link in linee]
    return jsonify(links_dict)


@app.route("/api/<int:id>", methods=["GET"])
@cross_origin()
def get_link(id):
    link = db.session.query(Links).get(id)
    if link is None:
        return jsonify({'error': 'Link not found'}), 404
    link_dict = link.to_dict()
    return jsonify(link_dict)


@app.route('/api', methods=['POST'])
@cross_origin()
def create_link():
    data = request.get_json()
    if not data or not all(key in data for key in ['name', 'link', 'desc', 'image', 'tags']):
        return jsonify({'error': 'Invalid request data'}), 400

    link = Links(
        name=data['name'],
        link=data['link'],
        about=data['desc'],
        likes=0,
        image=data['image'],
        tags=';'.join(data['tags'])
    )
    db.session.add(link)
    db.session.commit()
    link_dict = link.to_dict()
    return jsonify(link_dict), 201

@app.route("/api/tags/")
@cross_origin()
def get_by_tags_all():
    linee = db.session.query(Links).all()
    links_dict = [link.to_dict() for link in linee]
    return jsonify(links_dict)


@app.route("/api/tags/<string:tags>")
@cross_origin()
def get_by_tags(tags):
    if not tags:
        linee = db.session.query(Links).all()
        links_dict = [link.to_dict() for link in linee]
        return jsonify(links_dict)
    tarray = [f'%{i}%' for i in tags.split(';')]
    search_res = db.session.query(Links)
    for i in tarray:
        search_res = search_res.where(Links.tags.like(i))
    search_res = search_res.all()
    endp_res = []
    for i in search_res:
        if any([k in i.tags.split(';') for k in tags.split(';')]):
            link_dict = i.__dict__
            link_dict.pop('_sa_instance_state')
            endp_res.append(link_dict)
    return jsonify(endp_res), 200

@app.route("/api/like/<int:id>")
@cross_origin()
def set_like(id):
    link = db.session.query(Links).get(id)
    if link is None:
        return jsonify({'error': 'Link not found'}), 404
    link.likes += 1
    db.session.commit()
    return '', 201


@app.route('/api/<int:id>', methods=['DELETE'])
@cross_origin()
def delete_link(id):
    link = db.session.query(Links).get(id)
    if link is None:
        return jsonify({'error': 'Link not found'}), 404
    db.session.delete(link)
    db.session.commit()
    return '', 204

@app.route('/admin')
def admin():
    links = Links.query.all()
    return render_template('admin.html', links=links)

@app.route('/add', methods=['POST'])
def add_link():
    link = Links(
        name=request.form['name'],
        link=request.form['link'],
        about=request.form['desc'],
        likes=0,
        image=request.form['image'],
        tags=request.form['tags']
    )
    db.session.add(link)
    db.session.commit()
    link_dict = link.to_dict()
    return redirect('/admin')

@app.route('/delete/<int:id>')
def delete_link_admin(id):
    link = Links.query.get(id)
    db.session.delete(link)
    db.session.commit()
    return redirect('/admin')


if __name__ == "__main__":
    app.run(debug=True)