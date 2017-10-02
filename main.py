from flask import Flask, request, redirect, render_template
import cgi
import os



app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/")
def index():
    #return input
    return render_template('input.html')



#@app.route('/signup')
@app.route("/signup", methods=['POST','GET'])
def hello():
    username = request.args.get('username')
    password = request.args.get('password')
   
    verify = request.args.get('verify')
    email = request.args.get('email')

    #return render_template('input.html', username=username)
    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''
    
    if username.isalnum() == False:
        username_error = "Must have no spaces or special characters"

    if username == "" or  len(username) < 3 or len(username) > 20:
        username_error = 'Username needs to be between 3-20 characters'
        username=''

    if password.isalnum() == False:
        password_error = "Must have no spaces or special characters"
    

    if password == "" or  len(password) < 3 or len(password) > 20:
        password_error = 'Password needs to be between 3-20 characters'
        password=''   

    

    if password != verify:
        verify_error = 'Passwords must match'
        verify=''

    

    
    optional = ''
    if email == '':
        email = optional
    else:
            
        if len(email) < 3 or len(email) > 20:
            email_error = 'Invalid email'
            email=''


    
        
    
    if email.isalnum():
        email_error = "(ex. name@gmail.com)"             



    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username)
    
    else:
        
        return render_template('input.html',
        username=username,
        email=email,
        username_error=username_error,
        password_error=password_error, 
        verify_error=verify_error,
        email_error=email_error)
       

        

    
        
 

app.run()

