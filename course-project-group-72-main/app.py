# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# # Database configuration
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://username:password@localhost/database_name'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # Initialize SQLAlchemy
# db = SQLAlchemy(app)

# @app.route('/')
# def about():
#     return 'index.html'


# # Define User model
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#     password = db.Column(db.String(100), nullable=False)
#     # Add any other fields as required

# # Define UploadedImage model
# class UploadedImage(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     filename = db.Column(db.String(100), nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     user = db.relationship('User', backref=db.backref('images', lazy=True))
#     # Add any other fields as required

# if __name__ == '__main__':
#     # Create tables if they do not exist
#     db.create_all()
#     app.run(debug=True)
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app = Flask(__name__, static_url_path='/custom_static')
# app.static_folder = 'static'

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:rithu2005@localhost/database_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

@app.route('/')
def about():
    return render_template("index.html")

@app.route('/multImage')
def mult_image():
    return render_template('multImag.html')

@app.route('/video')
def video():
    return render_template('video.html')


# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    # Add any other fields as required

# Define UploadedImage model
class UploadedImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('images', lazy=True))
    # Add any other fields as required

if __name__ == '__main__':
    # Create tables if they do not exist within application context
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)
