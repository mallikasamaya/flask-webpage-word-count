# flask-webpage-word-count
Word count of a web page returned by user submitted URL using flask and redis

A Flask App counting the words in a web page returned by user-submitted URL.

# Dependencies :

- Flask==1.0.2
- Flask-SQLAlchemy==2.3.2
- SQLAlchemy==1.2.15
- redis==3.0.1
- requests==2.2.1
- rq==0.13.0

## Setup :
Assume that you have created virtual environment in your computer and have python3 installed.
### Install the dependencies:
`sudo pip install requirements.txt`

### Run redis worker:
Go to project directory and run the following command in your console, on your virtual environment.
 
 `python worker.py`

--> Make sure that you are running this worker.py in the background. 
 
### Create Database:
Open your terminal window and create the database in mysql server.

### Run application server:
Open another terminal window and run the following command.

`python app.py`

Now, open your web browser and visit the below URL for server.

`http://localhost:80`
