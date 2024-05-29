from flask import Flask
from werkzeug.urls import url_quote_plus as url_quote

app = Flask(__name__)

@app.route('/')
def training():
    # Construct your message here
    message = """
    <html>
        <head>
            <title>Training Page</title>
        </head>
        <body>
            <h1>Training 22</h1>
            <p>Hi, my name is Miguel</p>
        </body>
    </html>
    """
    return message

if __name__ == '__main__':
    app.run(debug=True)
