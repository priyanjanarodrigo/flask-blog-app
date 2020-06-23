from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
'''
    # Generate a secret easily (IDLE can be used)
    import secrets
    secrets.token_hex(16) 
'''
app.config['SECRET_KEY'] = '30e8a8f03e6df34c9f76837290d89e1b'

posts = [
    {
        'author': 'Priyanjana Rodrigo',
        'title': 'Blog Post 1',
        'content': 'First person content',
        'date_posted': 'April 20,2020'
    },
    {
        'author': 'JK Rowlling',
        'title': 'Blog Post 2',
        'content': 'Second person content',
        'date_posted': 'April 21,2020'
    }
]


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', posts=posts)


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'priyanjanarodrigo@gmail.com' and form.password.data == 'password':
            flash(f'You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')

    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)

# https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog/snippets