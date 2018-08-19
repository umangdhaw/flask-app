from flask import Flask, request, jsonify
import redis
import json
from datetime import *

app = Flask(__name__)
db = redis.Redis("localhost")

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/hello/<username>", methods=['GET'])
def wish_user(username):
  dob = db.get(username)
  if dob is None:
    return jsonify(message = "User not found"), 404
  else:
    dob = datetime.strptime(dob, "%Y-%m-%d").date()
    dobYear, dobMonth, dobDay = dob.year, dob.month, dob.day
    today = date.today()
    nextBirthday = date(today.year, dobMonth, dobDay)
    if (today == nextBirthday):
      return jsonify(message = "Hello %s, Happy birthday!" % username)
    elif today < nextBirthday:
      # birthday is upcoming
      return jsonify(message = "Hello %s, Your birthday is in %s days" %(username, (nextBirthday - today).days))
    else:
      # birthday has already passed in this calendar year, so get # of days from next calendar year
      nextBirthday = date(today.year + 1, dobMonth, dobDay)
      return jsonify(message = "Hello %s, Your birthday is in %s days" %(username, (nextBirthday - today).days))

@app.route("/hello/<username>", methods=['PUT'])
def create_or_update_user(username):
  content = request.get_json()
  if 'dateOfBirth' in content:
    dob = content['dateOfBirth']
    try:
      # check if DOB is in correct format
      formatted_dob = datetime.strptime(dob,"%Y-%m-%d").date()
      if formatted_dob > date.today():
        return "dateOfBirth cannot be in the future. Please try again.", 400
    except Exception:
      return "dateOfBirth format incorrect. Please use the YYYY-MM-DD ISO format", 400
    db.set(username, dob)
    return 'No Content', 201
  else:
    return "dateOfBirth key missing in PUT request", 400

if __name__ == '__main__':
  app.run()
