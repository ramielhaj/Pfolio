from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/")
def write_to_csv(data):
    with open('database.csv', newline="", mode="a+") as f:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csvwriter = csv.writer(f, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow([email,subject,message])
    return csvwriter

@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return render_template("thankyou.html")

    else:
        return "something went wrong"
@app.route("/<string:username>")
def hello_worldie(username):
    return render_template(username)



#@app.route("/favicon.ico")
#def img():
 #   return render_template("favicon.ico")