from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
import config  # ← Yeh config.py file alag banani hai
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# 🔌 Mail config
app.config.from_object(config)
mail = Mail(app)

# 📦 Projects list
projects = [
    {
        'title': 'PDF to Google Sheets Automation',
        'desc': 'This project extracts table data from a PDF and sends it to Google Sheets using Python.',
        'link': 'https://github.com/CodeWithRehan10/pdf-to-sheets-automation'
    },
    {
        'title': 'Portfolio Website (You’re Looking At It!)',
        'desc': 'This is a personal portfolio built using Flask and hosted on Replit.',
        'link': '#'
    }
]

# 🏠 Homepage
@app.route("/")
def home():
    return render_template("index.html", projects=projects)

# 📬 Contact form
@app.route("/contact", methods=["POST"])
def contact():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    try:
        msg = Message(
            subject=f"New Contact from {name}",
            sender=config.MAIL_USERNAME,               # ✅ Gmail sender
            recipients=[config.MAIL_USERNAME],         # ✅ Gmail recipient
            body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        )
        mail.send(msg)
        flash("✅ Message sent successfully!")
    except Exception as e:
        print(e)
        flash("❌ Message failed. Please try again.")

    return redirect("/#contact")


# ✅ Hosting fix: PORT env variable for Railway/Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
