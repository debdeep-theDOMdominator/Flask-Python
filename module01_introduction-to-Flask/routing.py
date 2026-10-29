# use it in cmd --> python routing.py

from flask import Flask

app= Flask(__name__)

@app.route("/")
def home():
    return "Hello World !!" 
# Routing examples -- 
@app.route("/about")
def about():
    return "This is About us page ~" 

@app.route("/contact")
def contact():
    return "contact me page ." 

if __name__ == "__main__":
    app.run(debug=True)

