from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_jwt_extended import JWTManager

app = Flask(__name__)
# secret key replaced by JWT_SECRET_KEY for Flask-JWT-Extended
# app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
app.config['JWT_SECRET_KEY'] = "i-should-be-secret-and-stored-in-env-variables"
# jwt secret key should be kept secret and ideally stored in environment variables
# this is for demonstration purposes only
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
db = SQLAlchemy(metadata=metadata)

migrate = Migrate(app, db)
db.init_app(app)

bcrypt = Bcrypt(app)
# initialize JWT manager for handling JWT authentication
jwt = JWTManager(app)

api = Api(app)
