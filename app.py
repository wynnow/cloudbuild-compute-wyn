from flask import Flask 
app = Flask(__name__)   #app instance
 

#root of application 
@app.route("/")       #app as a decorator to create each router or URL provided by application 
def hello(): 
    return "Hello, Welcome to WYN cloud build test"

 
if __name__ == "__main__": 
    app.run() 
