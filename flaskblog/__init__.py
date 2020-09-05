from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)
bcrypt = Bcrypt(app)



app.config['SECRET_KEY']='myownsecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER']= 'smtp.googlemail.com'
app.config['MAIL_PORT']= 587
app.config['MAIL_USE_TLS']= True
#Your E-mail creditial 
app.config['MAIL_USERNAME']= "Your E-mail Address Goes here"
app.config['MAIL_PASSWORD']= "Your Password Goes Here"
mail = Mail(app)
from flaskblog import routs