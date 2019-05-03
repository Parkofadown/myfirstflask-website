from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)
# Basic Routing
@app.route('/')#127.0.0.1:5000
def index():
    return render_template('bootstrap template.html')
#html files inside templates
#images go into static
#@app.route('/puppy_latin/<name>')#127.0.0.1:5000/information
#def puppylatin(name):

    #pupname = ''
    #if name[-1] == 'y':
    #    pupname = name[:-1] + 'iful'
    #else:
        #pupname = name + 'y'
    #return "<h1> Your puppy latin name is: {}".format(pupname)

# Dynamic Routing
#@app.route('/puppy/<name>')
#def puppy(name):
#    return "<h1> This is a page for {} </h1>".format(name)

if __name__ == '__main__':
    app.run(debug=True)
