from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

# Define the Post model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow)

# Create the database tables
with app.app_context():
    db.create_all()

# Define routes
@app.route('/')
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)

@app.route('/post/<int:id>')
def post_detail(id):
    post = Post.query.get(id)
    return render_template('post_detail.html', post=post)

@app.route('/admin')
def admin():
    posts = Post.query.all()
    return render_template('admin.html', posts=posts)

@app.route('/admin/add', methods=['POST'])
def add_post():
    title = request.form['title']
    content = request.form['content']

    new_post = Post(title=title, content=content)
    db.session.add(new_post)
    db.session.commit()

    return redirect(url_for('admin'))

@app.route('/admin/delete/<int:id>')
def delete_post(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)
