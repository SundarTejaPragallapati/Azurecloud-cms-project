"""
This script runs the FlaskWebProject application using a development server.
"""

from os import environ
from FlaskWebProject import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    with app.app_context():
        from FlaskWebProject import db
        from FlaskWebProject.models import User
        db.create_all()
        if not User.query.filter_by(username='admin').first():
            u = User(username='admin')
            u.set_password('pass')
            db.session.add(u)
            db.session.commit()
    app.run(HOST, PORT)
