from flask import Flask, render_template, request, session, redirect, url_for
import webscrape
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_genres")
def get_genre():
    url = request.args.get("url")
    genres = webscrape.get_genres(url)
    if genres != None:
        return render_template("display_genres.html", genres=genres)
    else:
        message = "Not a valid URL, please try again"
        return render_template("index.html",message=message)

if __name__ == "__main__":
    if not os.environ.get('HEROKU_POSTGRESQL_VIOLET_URL'):
        app.run(debug=True)