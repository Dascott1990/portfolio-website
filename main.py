from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')  # Make sure you have the about.html file

# Other routes for your sections (skills, services, etc.)
@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
