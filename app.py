from flask import Flask , render_template , redirect , url_for , request , make_response
app  = Flask(__name__)
from model import model

@app.route("/",methods=['GET'])
def home():
    return render_template('home.html' , result=None)

@app.route("/predict" , methods=['POST','GET'])
def predict():
    data = request.form.to_dict()
    result = model(data)
    return render_template('home.html', data=data , result=result)

if __name__ == '__main__':
    app.run(debug=True)



# for static file create folder called static and make all the file in it and then 
# 1. {{ url_for("static" , filename="main.css") }} add this in the html file 