#importing a template from flask module of render_template
from flask import Flask,request, render_template

app=Flask(__name__)


@app.route('/')

def welcome():
  return render_template('get.html')

# Define a route for the root URL ("/") that handles GET requests.
# handles GET requests and retrieves a "uname" parameter from the query string.

@app.route('/login',methods=['GET'])
def login():
    # Get the "uname" parameter from the query string.
    uname=request.args.get('uname')
    password=request.args.get('pass')
    if uname=='Baiju' and password=='Fet':
        return 'Welcome %s' %uname
    else:
        return "Wrong Credentials"
    
if __name__=='__main__':
    app.run(debug=True)
