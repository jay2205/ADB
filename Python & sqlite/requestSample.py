from bottle import get, post, request,run,template # or route

@get('/hello')
@get('/hello/<name>')
def hello(name='World'):
    return template('hello', name=name)

@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''
def check_login(username,password):
    if username == 'jayanth' and password == 'hello':
        return True

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"


run(host='localhost', port=8080, debug=True)
