from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from project import app, db
import datetime

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)



if __name__ == '__main__':
    manager.run()

    