# ux
This contains a simple flask app and UX template for Administration use.

# Get it to run

### Clone the project
The project is here... you found it... Clone it locally

### Virtual environment
There are several ways to create and activate a virtual environment.  One is to run
```
virtualenv env -p python3
```
and then activate by running
```
source env/bin/activate
```
### Install Flask (and other things if needed)
Run pip
```
pip install -r reqirements.txt
```
### Run the app
To run the app, run the following
```
python -m flask --app app run --port 8000 --debug
```