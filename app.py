from dns.rdatatype import NULL
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key="secretkey"

def mongopostdata(user):
    app.config["MONGO_URI"]="mongodb+srv://aastha18:thunderbird@cluster0.a0epe.mongodb.net/formfill?retryWrites=true&w=majority"
    mongo=PyMongo(app)
    id = mongo.db.firstform.save(user)
    if id!=NULL:
        return 1
    else:
        return 0
    

@app.route('/', methods=["POST"])
def req_data():
    request_body =request.get_json()

    user={
        "name":request_body['name'],
        "email":request_body['email'],
        "phone":request_body['phone'],
        "gender":request_body['gender'],
        "location":request_body['location']
    }

    value=mongopostdata(user)
    if value==1:
        status_return= "Data saved Successfully"
    else:
        status_return= "Error in saving the data"
    return jsonify(status_return)


if __name__ =="__main__":
    app.run()