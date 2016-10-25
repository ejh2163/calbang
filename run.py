import os
from project import app

if __name__ == "__main__":
    #app.run()
    app.run(host = os.getenv('IP', '0.0.0.0'), port = int(os.getenv('PORT', 8080)))