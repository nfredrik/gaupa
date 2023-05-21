import os

from flask import Flask
import git
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello POE!'


@app.route('/update_server', methods=['POST'])
def webhook():
    os.chdir('/home/nfredrik')
    repo = git.Repo('https://github.com/nfredrik/gaupa')
    origin = repo.remotes.origin
    origin.pull()
    return 'Updated PythonAnywhere successfully', 200


if __name__ == '__main__':
    app.run()
