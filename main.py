from flask import Flask, request
from caesar import rotate_string
app = Flask(__name__)
app.config['DEBUG'] = True
form="""
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form input ='/' method = 'post'>
        <input name ="rot" type = "text" default value = 0>
        <textarea name = "text">{0}</textarea>
        <button type = "submit">Submit</button>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")
@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = str(request.form['text'])
    encrypt = rotate_string(text, rot)
    return form.format(encrypt)
app.run()
