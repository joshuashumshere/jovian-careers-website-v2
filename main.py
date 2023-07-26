from flask import Flask

app = Flask(__name__) # create an object of the class 

@app.route("/") #path of the url after the url

def hello_world():
  return "Hello, World!"

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
