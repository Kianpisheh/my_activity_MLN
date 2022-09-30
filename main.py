from flask import Flask


from pracmln import MLN
from pracmln import Database
from pracmln import MLNQuery, MLNLearn
from pracmln.utils.project import PRACMLNConfig


def train_mln(mln, db, config1):
    # inference
    learner = MLNLearn(mln=mln, db=db, config=config1, verbose=True)
    learner.run()


def update_activity(activity):
    pass


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/activity")
def get_activities():
    mln = MLN(mlnfile="./activity.mln")
    db = Database.load(mln, "./activity.db")
    config1 = PRACMLNConfig("./learn.conf")

    # convert mln into proper activity format


@app.route("/activity/update")
def update_activity():
    pass


app = Flask(__name__)
