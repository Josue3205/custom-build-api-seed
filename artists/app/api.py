import os
from flask import Flask, url_for, jsonify, request
from flask import make_response
from flask.ext.sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, '../data.sqlite')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/firstdb'

db = SQLAlchemy(app)


class ValidationError(ValueError):
    pass


class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.Integer)
    score = db.Column(db.Integer)
    domain = db.Column(db.String(64))
    reddit_id = db.Column(db.String(64))
    title = db.Column(db.String(500))
    author = db.Column(db.String(64))
    ups = db.Column(db.Integer)
    downs = db.Column(db.Integer)
    comment_count = db.Column(db.Integer)
    permalink = db.Column(db.String(500))
    thumbnail = db.Column(db.String(500))
    subreddit_id = db.Column(db.String(64))
    edited = db.Column(db.String(64))
    is_self = db.Column(db.String(64))
    name = db.Column(db.String(64))
    url = db.Column(db.String(500))

    def get_url(self):
        return url_for('get_artist', id=self.id, _external=True)

    def export_data(self):
        return {
            'self_url': self.get_url(),
            'created': self.created,
            'score': self.score,
            'domain': self.domain,
            'reddit_id': self.reddit_id,
            'title': self.title,
            'author': self.author,
            'ups': self.ups,
            'downs': self.downs,
            'comment_count': self.comment_count,
            'permalink': self.permalink,
            'thumbnail': self.thumbnail,
            'subreddit_id': self.subreddit_id,
            'edited': self.edited,
            'is_self': self.is_self,
            'name': self.name,
            'url': self.url
        }

    def import_data(self, data):
        try:
            self.created = data['created']
            self.score = data['score']
            self.domain = data['domain']
            self.reddit_id = data['reddit_id']
            self.title = data['title']
            self.author = data['author']
            self.ups = data['ups']
            self.downs = data['downs']
            self.comment_count = data['comment_count']
            self.permalink = data['permalink']
            self.thumbnail = data['thumbnail']
            self.subreddit_id = data['subreddit_id']
            self.edited = data['edited']
            self.is_self = data['is_self']
            self.name = data['name']
            self.url = data['url']
        except KeyError as e:
            raise ValidationError('Invalid artist: missing ' + e.args[0])
        return self


@app.route('/artists/', methods=['GET'])
def get_artists():
    return jsonify({'artists': [artist.get_url() for artist in
                                  Artist.query.all()]})

@app.route('/artists/<int:id>', methods=['GET'])
def get_artist(id):
    return jsonify(Artist.query.get_or_404(id).export_data())

@app.route('/artists/', methods=['POST'])
def new_artist():
    artist = Artist()
    artist.import_data(request.json)
    db.session.add(artist)
    db.session.commit()
    return jsonify({}), 201, {'Location': artist.get_url()}

@app.route('/artists/<int:id>', methods=['PUT'])
def edit_artist(id):
    artist = Artists.query.get_or_404(id)
    artist.import_data(request.json)
    db.session.add(artist)
    db.session.commit()
    return jsonify({})


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)