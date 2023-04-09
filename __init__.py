from flask import Flask, jsonify
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)



@app.route("/<string:name>/<string:email>/<string:phone>/<string:message>")
def func(name, email, phone, message):
    result = {
        "name": name,
        "email": email,
        "phone": phone,
        "message": message
    }
    app.config["MAIL_SERVER"] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASSWORD')
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    mail = Mail(app)
    msg = Message(
        subject="Query from Website",
        sender=os.getenv('EMAIL_USERNAME'),
        recipients=["test email"]
    )
    msg.body = f"Name: {name}\nEmail: {email}\nPhone Number: {phone}\nMessage: {message}\n"
    mail.send(msg)
    return jsonify(result)




app.run(debug=True)