import os
import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from collections import Counter
from rq import Queue
from rq.job import Job
from worker import connect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a56c789269362ffade24f8555561'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

q = Queue(connection=connect)

from models import *
db.create_all()

def count_and_save_words(url):
    errors = []
    try:
        r = requests.get(url,verify=False);
    except:
        errors.append(
            "Unable to get URL. Please make sure it's valid and try again."
        )
        return {"error": errors}

    words = len(r.text.split());
    scode = r.status_code
    # save the results
    try:
        result = Result(
            url=url,
            result_words=words,
            status_code=scode
        )
        db.session.add(result)
        db.session.commit()
        return result.id
    except:
	errors.append("Unable to add item to database.")
        return {"error": errors}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":	
        job = q.enqueue_call(
            func="app.count_and_save_words", args=(request.form['url'],),
        )
	print(job.get_id())
	return render_template('index.html',jobid=job.get_id())
    return render_template('index.html')

@app.route("/results/<job_key>", methods=['GET'])
def get_results(job_key):

    job = Job.fetch(job_key, connection=connect)
    if job.is_finished:
    	obj = Result.query.filter_by(id=job.result).first()
    	print(obj)
    	return str(obj.result_words)
    else:
        return "Hey! Come back after sometime"


if __name__ == '__main__':
    app.run(port=80, debug=True)
