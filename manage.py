import os
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db

env = os.environ.get('env', "default")
print("env", env)
app = create_app(env)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run(default_command='runserver')
