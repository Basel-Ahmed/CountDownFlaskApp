from flask import Flask
from flask import render_template
from datetime import datetime

app = Flask(__name__)
@app.route("/")
def countdown():

    launchTime = datetime(2022, 10, 31)
    currentTime = datetime.now()
    diff = launchTime - currentTime
    numberOfMilliseconds = int(diff.total_seconds() )
    numberOfDays = diff.days

    print("Deadline for Training plan is : ")
    
    return render_template(
        "countdown.html",
        daytime=numberOfDays,
        secstime=numberOfMilliseconds
    )