from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    current_page = 'home'
    return render_template('home.html', current_page=current_page)

@app.route('/experience')
def experience():
    current_page = 'experience'
    return render_template('experience.html', current_page=current_page)

@app.route('/skills')
def skills():
    current_page = 'skills'
    return render_template('skills.html', current_page=current_page)

@app.route('/languages')
def languages():
    current_page='languages'
    return render_template('languages.html', current_page=current_page)

@app.route('/about')
def about():
    current_page = 'about'
    return render_template('about.html', current_page=current_page)

@app.route('/contact')
def contact():
    current_page = 'contact'
    return render_template('contact.html', current_page=current_page)

@app.route('/classic_cv')
def classic_cv():
    current_page = 'classic_cv'
    return render_template('classic_cv.html', current_page=current_page)


if __name__=='__main__':
    app.run(debug=True)