# A view function is a Python function registered with a route to handle incoming requests and produce responses. The function can return text, HTML, JSON, a redirect or another supported response type.

from flask import Flask,jsonify

app= Flask(__name__)

@app.route("/")
def home():
    return "Hello World !!"


# |--------> A Simple View Function

@app.route("/hello")
def hello():
    return "Hello from Flask"

# |--------> Returning HTML
@app.route("/welcome")
def welcome():
    return """
    <!DOCTYPE html>
    <html>
    <head><title>Welcome</title></head>
    <body>
        <h1>Welcome to Flask</h1>
        <p>This is an HTML response.</p>
    </body>
    </html>
    """

# |--------> Returning JSON
@app.route("/api/status")
def status():
    return jsonify({
        "application": "Flask",
        "status": "running"
    })

# |--------> View Functions Can Call Other Functions
def calculate_total(price, quantity):
    return price * quantity

@app.route("/total")
def total():
    amount = calculate_total(100, 3)
    return f"Total amount: {amount}"
# |-------->
# |-------->


if __name__ == "__main__":
    app.run(debug=True)




