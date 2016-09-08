import feedparser

from flask import Flask, render_template
from flask import request

app = Flask(__name__)



RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640'}

# taking query from user using the GET request and extracting that query value 
# to call the particular rss feed
# search for key value pair after ? in the URL of GET request
# HERE key is publication and value will be rss feed
# url:  localhost:5000/?publication=bbc
@app.route("/")
def get_news():
    query = request.args.get("publication")
    if not query or query.lower() not in RSS_FEEDS:
        publication = "bbc"
    else:
        publication = query.lower()

    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template("home.html",articles=feed['entries'])

if __name__ == "__main__":
    app.run(port=5000, debug=True)


