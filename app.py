from flask import Flask, render_template, request

app = Flask(__name__, static_folder="public", static_url_path="")


@app.route("/")
def home():
    sender_name = request.args.get("from", "").strip()
    if not sender_name:
        sender_name = "Your Name"
    return render_template("index.html", sender_name=sender_name)


if __name__ == "__main__":
    app.run(debug=True)
