from flask import Flask, render_template, url_for, flash, redirect, session, Blueprint
from sklearn.externals import joblib
from flask import request
import numpy as np
import os

from flask_session import Session
app = Flask(__name__, template_folder='template',static_folder='static')

dir_path = os.path.dirname(os.path.realpath(__file__))

#@app.route('/Files/<path:filename>')
#def download(filename):
 #   return send_from_directory(directory='Files', filename=filename)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


#@app.route("/Home")
#def home():
 #   return render_template("home.html")


@app.route("/Standard_Report")
def Standard_Report():
    return render_template("Standard_Report.html")



@app.route("/Custom_Report")
def Custom_Report():
    return render_template("Custom_Report.html")


@app.route("/ReportigInfo")
def ReportigInfo():
    # if form.validate_on_submit():
    return render_template("ReportigInfo.html")


@app.route("/Contact")
def heart():
    return render_template("Contact.html")


if __name__ == "__main__":
    app.run(debug=True,port=5001)