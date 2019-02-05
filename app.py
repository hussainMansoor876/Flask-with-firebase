from flask import Flask, request, jsonify
import pyrebase

app = Flask(__name__)

config = {
    "apiKey": "AIzaSyBNKp2zih1SxmBk3t1ED-CydhpSWY7hnlA",
    "authDomain": "teacher-interview.firebaseapp.com",
    "databaseURL": "https://teacher-interview.firebaseio.com",
    "projectId": "teacher-interview",
    "storageBucket": "teacher-interview.appspot.com",
    "messagingSenderId": "574831678717"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return '''
            <form method="post">
            <h2>User</h2>
            <input type="text" name="user">
            <h2>Email</h2>        
            <input type="email" name="email">        
            <input type="submit" value="Submit">
            </form>
        '''
    else:
        data = {'user': request.form['user'],'email': request.form['email']}
        db.child('Users').push(data)
        return '''
            <form method="post">
            <h2>User</h2>
            <input type="text" name="user">
            <h2>Email</h2>        
            <input type="email" name="email">        
            <input type="submit" value="Submit">
            </form>
        '''


app.run(debug=True)
