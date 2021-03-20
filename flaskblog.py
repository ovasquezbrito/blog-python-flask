from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '02eb7faa696d439d1c225f0d79700779'

posts = [
    {
        'author': 'Oduber Vásquez',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Marzo 04, 2021'
    },
    {
        'author': 'Karelyan guerra',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Marzo 05, 2021'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.is_submitted():
        flash(f'Cuenta creada para {form.username.data}!', 'success')
        return redirect(url_for('home'))
    
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.is_submitted():
        if form.email.data == 'admin@gmail.com' and form.password.data == 'password':
            flash('¡Has iniciado sesión!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Inicio de sesión fallido, compruebe el nombre de usuario y la contraseña', 'danger') 


    return render_template('login.html', title='Login', form=form)

if (__name__) == '__main__':
    app.run(debug=True)