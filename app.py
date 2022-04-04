from distutils.command import upload
from tkinter.messagebox import NO
import pyrebase 

config = {
    "apiKey": "AIzaSyC9HSzgVaBQ4nxgRTDxR5K59QpHRLo77-s",
    "authDomain": "test-55cca.firebaseapp.com",
    "databaseURL": "",
    "projectId": "test-55cca",
    "storageBucket": "test-55cca.appspot.com",
    "messagingSenderId": "163206894466",
    "appId": "1:163206894466:web:dbe1254b13ff389d15b59b",
    "measurementId": "G-7XPPFFTJS4"
}

firebase = pyrebase.initialize_app(config)  

storage = firebase.storage()

from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def basic():
    if request.method == 'POST':       
        upload = request.files['upload']
        storage.child("images/").put(upload)
        return redirect(url_for('uploads'))
    return render_template('index.html')

@app.route('/uploads')
def uploads():
    if True:
        links = storage.child('images/new.jpg').get_url(None)
        return render_template('upload.html', l=links)

if __name__ == '__main__':
    app.run(debug=True)


