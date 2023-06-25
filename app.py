from flask import Flask , render_template , redirect , url_for , request , make_response , flash
app  = Flask(__name__)
from model import model
app=Flask(__name__)
app.secret_key = 'your_secret_key'

result = []

@app.route("/",methods=['GET'])
def home():
    global result
    return render_template('home.html' , result=result)

@app.route("/predict" , methods=['POST'])
def predict():
    global result
    data = request.form.to_dict()
    method = data.pop('method' , None)
    result = model(data,method)
    print(method)
    print(data)
    print(result)
    flash("Predicted Successfully")
    return redirect("/")

@app.route("/reset" , methods=['POST','GET'])
def reset():
    global result
    result = []
    flash("Reset Complete!")
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)



# for static file create folder called static and make all the file in it and then 
# 1. {{ url_for("static" , filename="main.css") }} add this in the html file 