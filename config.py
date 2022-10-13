from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://rey:rey@localhost:8090/flask-react'
db = SQLAlchemy(app)