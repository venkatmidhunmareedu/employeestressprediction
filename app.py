from flask import Flask , render_template , redirect , url_for , request
app  = Flask(__name__)
from predict import mul

@app.route("/",methods=['GET'])
def home():
    return render_template('home.html')

@app.route("/predict" , methods=['POST'])
def predict():
    age = int(request.form.get('age'))
    avghrs = int(request.form.get('avghours'))
    result = mul(age , avghrs)
    return render_template('home.html', age=age,avghrs=avghrs , result= result)

if __name__ == '__main__':
    app.run(debug=True)



# for static file create folder called static and make all the file in it and then 
# 1. {{ url_for("static" , filename="main.css") }} add this in the html file 