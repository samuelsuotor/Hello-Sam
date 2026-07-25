from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello Sam!</h1>

    <form action="/welcome">
        <input type="text" name="name" placeholder="Enter your name">
        <button>Submit</button>
    </form>
    """

@app.route("/welcome")
def welcome():
    name = request.args.get("name", "Guest")
    return f"<h1>Welcome, {name}!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)