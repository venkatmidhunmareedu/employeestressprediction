from flask import Flask , render_template , redirect , url_for
app  = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/predict" , methods=['POST'])
def predict():
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)



# for static file create folder called static and make all the file in it and then 
# 1. {{ url_for("static" , filename="main.css") }} add this in the html file 