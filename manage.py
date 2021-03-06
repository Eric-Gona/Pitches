from flask import appcontext_popped
from flask_script import Manager, Server
from flask_migrate import Migrate
from app.models import User
from app.templates import create_app
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(appcontext_popped)

app = create_app('production')

manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('db',Migrate)
manager.add_command('run',Server(use_debugger=True))


@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User)

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == "__main__":
    manager.run()