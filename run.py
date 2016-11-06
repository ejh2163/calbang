import os
from project import app

if __name__ == "__main__":
    app.run()
    #app.run(host = os.getenv('IP', '0.0.0.0'), port = int(os.getenv('PORT', 8080)))
    
    # lsof -i
    # kill apacheprocessid
    # export APP_SETTINGS='config.DevConfig'
    # export DATABASE_URL='mysql://jlee7737:@localhost/calbang'
    # sudo service mysql start
    # python run.py
    
    # heroku config
    # heroku config:set DATABASE_URL='db url goes here'
    # heroku run python migrate.py db migrate
    # heroku run python migrate.py db upgrade
    
    # git add .
    # git commit -am "msg goes here"
    # git push
    # git push heroku master