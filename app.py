from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", css_url=url_for('static', filename='style.css'))

@app.route('/terms-of-service')
def terms_of_service():
    return render_template('terms_of_service.html', css_url=url_for('static', filename='style.css'))

@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy_policy.html', css_url=url_for('static', filename='style.css'))

if __name__ == "__main__":
    app.run(debug=True)
