from flask import Flask
from modules import evals, profiles, members

app = Flask(__name__)

app.register_blueprint( members.bp )
app.register_blueprint( evals.bp,     url_prefix = '/evals' )
app.register_blueprint( profiles.bp , url_prefix = '/profiles')

if __name__ == '__main__':
    app.run( host = '0.0.0.0', port = 3000 )
