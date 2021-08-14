from flask import Flask, request, jsonify,render_template,flash
from distance import main,Address
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Record.db'
app.config['SECRET_KEY'] = "random string"

db=SQLAlchemy(app)
class Record(db.Model):
	AadhaarNo=db.Column(db.String(100),primary_key=True)
	Hospital=db.Column(db.String(200),nullable=False)
	Slot=db.Column(db.String(20),nullable=False)

def __init__(self,AadhaarNo, Hospital,Slot):
   self.AadhaarNo = AadhaarNo
   self.Hospital = Hospital
   self.Slot = Slot

@app.route("/",methods=['POST', 'GET'])
def index():
    return render_template('index.html',Record=Record.query.all());

@app.route('/RegisterUser')
def Register():
  return render_template('RegisterUser.html')

@app.route("/slots",methods = ['POST', 'GET'])
def index2():
    AadhaarNo=request.form['AadhaarNo']
    status=main(AadhaarNo)
    return render_template('slots.html',name=status)

    #return render_template('slots.html',name="Incorrect Aadhar Number")
@app.route("/slots",methods = ['POST', 'GET'])
def new():
    if request.method == 'POST':
       Record = Record(request.form['AadhaarNo'],status, request.form['slot'])
       db.session.add(Record)
       db.session.commit()
       flash('Record was successfully added')
       return redirect(url_for('index'))


if __name__ == '__main__':
   db.create_all()
   app.run(threaded=True,port=int(os.getenv('PORT')))
