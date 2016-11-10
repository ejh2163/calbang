import os
from project import app

if __name__ == "__main__":
    #app.run()
    app.run(host = os.getenv('IP', '0.0.0.0'), port = int(os.getenv('PORT', 8080)))
    
    # lsof -i
    # kill apacheprocessid
    # sudo service mysql start
    # export APP_SETTINGS='config.DevConfig'
    # export DATABASE_URL='mysql://jlee7737:@localhost/calbang'
    # export SECRET_KEY='\x95\xdc?\xba\xfdO\xde\xb6"\xcdm\x1el3T<\xf0\xd5\x86\xf6\xa4\xfa\x1b\xfb'
    # export APP_MAIL_USERNAME='calbang.noreply@gmail.com'
    # export APP_MAIL_PASSWORD='L'
    # python run.py
    
    # heroku addons
    # heroku addons:destroy add-on-name-goes-here
    # heroku addons:create cleardb:ignite --fork=mysql://jlee7737:@localhost/calbang
    # heroku config:set DATABASE_URL='db url goes here'
    # heroku run python migrate.py db migrate
    # heroku run python migrate.py db upgrade
    
    # heroku logs
    # heroku config
    
    # git add .
    # git commit -am "msg goes here"
    # git push
    # git push heroku master