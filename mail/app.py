

from flask import Flask, render_template, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# SMTP Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "akkayyagariashok@gmail.com"  # Change to your email
EMAIL_PASSWORD = "ytoc ckrw uzyi zmhe"   # Use an App Password

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send-email", methods=["POST"])
def send_email():
    try:
        data = request.json
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]

        msg = MIMEMultipart()
        msg["From"] = SMTP_EMAIL
        msg["To"] = "your-receiving-email@gmail.com"  # Your email to receive messages
        msg["Subject"] = f"New Message from {name}" if subject == "No Subject" else subject

        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        server.sendmail(SMTP_EMAIL, "your-receiving-email@gmail.com", msg.as_string())
        server.quit()

        return jsonify({"status": "success", "message": "✅ Your message has been sent!"})

    except Exception as e:
        return jsonify({"status": "error", "message": f"❌ Error sending email: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
