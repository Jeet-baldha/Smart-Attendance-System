
from flask import Flask, render_template, request, jsonify
import face_recognition
import numpy as np
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
import pyrebase

Config = {
    "apiKey": "AIzaSyAUizon1JMbxAXzxgxEAEN_xlKylf0whVk",
    "authDomain": "smart-attendance-system-92033.firebaseapp.com",
    "databaseURL": "https://smart-attendance-system-92033-default-rtdb.firebaseio.com",
    "projectId": "smart-attendance-system-92033",
    "storageBucket": "smart-attendance-system-92033.appspot.com",
    "messagingSenderId": "627834716240",
    "appId": "1:627834716240:web:82c05b787cb7d10bf41155",
    "measurementId": "G-HJ5MC3B5C7"
    };



# firebase = pyrebase.initialize_app(Config)
# database = firebase.database()


# Reference to the root of your database

# Data to be inserted in JSON format


# Insert the data using push()
headers = {'Content-Type': 'application/json'}

cred = credentials.Certificate('smart-attendance-system-92033-firebase-adminsdk-twwbf-6901576c31.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smart-attendance-system-92033-default-rtdb.firebaseio.com/'
})

# root_ref = db.reference()


app = Flask(__name__)

@app.route('/reg')
def reg():  
    return render_template('registration-form.html')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    try:
        data ={
            "name": request.form.get('username'),
            "email": request.form.get('email'),
            "password": request.form.get('password'),
            "address": request.form.get('address')

        }
        database.push(data);
        return render_template('dashboard.html')
    except:
        return jsonify({"error":"get error"}),400
    # if request.content_type == 'application/json':
    #     data = request.get_json()
    #     new_ref = root_ref.child('users').push(data)
    # else:
    #     return jsonify({'error': 'Invalid content type'}), 400



# Define known individuals and their face encodings
known_individuals = [
    {"name": "Jeet", "image_path": "1.jpg"},
    {"name": "Viraj", "image_path": "viraj.jpeg"},
    {"name": "Henil", "image_path": "henil.jpeg"},
]

# Load known face encodings and names
known_face_encodings = []
known_face_names = []

for individual in known_individuals:
    image = face_recognition.load_image_file(individual["image_path"])
    encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(encoding)
    known_face_names.append(individual["name"])

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/recognize', methods=['POST'])
def recognize_face():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})

    uploaded_image = request.files['image']
    uploaded_image_data = face_recognition.load_image_file(uploaded_image)
    uploaded_face_encodings = face_recognition.face_encodings(uploaded_image_data)

    if not uploaded_face_encodings:
        return jsonify({'message': 'No faces found in the uploaded image', 'recognized_names': []})

    recognized_names = []

    for uploaded_encoding in uploaded_face_encodings:
        face_distances = face_recognition.face_distance(known_face_encodings, uploaded_encoding)
        min_distance_index = np.argmin(face_distances)

        if face_distances[min_distance_index] < 0.6:
            recognized_names.append(known_face_names[min_distance_index])

    if recognized_names:
        return jsonify({'message': 'Faces recognized', 'recognized_names': recognized_names})
    else:
        return jsonify({'message': 'No known faces recognized', 'recognized_names': []})

if __name__ == '__main__':
    app.run()
    app.debug = True
