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

data = {"Name" : "Vira","Age":21,"Id":1}

firebase = pyrebase.initialize_app(Config)
database = firebase.database()
database.push(data)