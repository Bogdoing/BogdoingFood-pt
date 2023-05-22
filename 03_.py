from flask import Flask, render_template, redirect
from loginform import LoginForm

import DATA

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'


@app.route('/')
def index():
    return render_template('index.html', title='Авторизация')


@app.route('/fastfood', methods=['GET', 'POST'])
def fastFood():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('fastFood.html', title='Фаст фуд', form=form)



@app.route('/login2', methods=['GET', 'POST'])
def login2():
    form = LoginForm()
    if form.validate_on_submit():
        return render_template('ak.html', title='User')
        #return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/login3', methods=['GET', 'POST'])
def login3():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login_2.html', title='Авторизация2', form=form)


# response_object = {'status': 'success'}
#     if request.method == 'POST':
#         post_data = request.get_json()
#         BOOKS.append({
#             'title': post_data.get('title'),
#         })
#         response_object['message'] = 'Book added!'

@app.route('/success')
def success():
    return 'success'


if __name__ == '__main__':
    app.run(port=8081, host='127.0.0.1')
