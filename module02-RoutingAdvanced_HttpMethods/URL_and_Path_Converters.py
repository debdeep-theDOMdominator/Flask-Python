from flask import Flask
from uuid import UUID

app= Flask(__name__)

@app.route("/")
def home():
    return "Hello World !!"

# |--------> INT converter
@app.route("/product/<int:product_id>")
def product(product_id):
    return f"Product ID: {product_id}"

# |--------> Float converter
@app.route("/price/<float:amount>")
def price(amount):
    return f"Price: {amount}"

# |--------> Path Converter
@app.route("/files/<path:filename>")
def file_info(filename):
    return f"Requested path: {filename}"

# |--------> UUID Converter
@app.route("/records/<uuid:record_id>")
def record(record_id):
    return f"Record ID: {record_id}"

# |--------> 
# |-------->  

if __name__ == "__main__":
    app.run(debug=True)

