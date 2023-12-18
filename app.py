from flask import Flask,render_template, request, redirect, url_for        
from flask_sqlalchemy import SQLAlchemy   
from datetime import datetime
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)
 
# Define the Post model
class Post(db.Model):   
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(225), nullable=False)
    content = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow)

# Create the database tables
with app.app_context():
    db.create_all()
    
@app.route("/")
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)
    

@app.route('/post/<int:id>')
def post_detail(id):

    pass

@app.route('/admin')
def admin():
    pass

@app.route('/admin/add', methods=['POST'])
def add_post():
    pass

@app.route('/admin/delete/<int:id>')
def delete_post(id):
    pass

if __name__ == '__main__':
    app.run(debug=True)

 
 