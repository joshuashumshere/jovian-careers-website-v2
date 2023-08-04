from flask import Flask, render_template

app = Flask(__name__)  # create an object of the class


@app.route("/")  #path of the url after the url
def hello_world():
  return render_template('home_css_bootstrap.html')
  #render_template('home.html') # this was with original CSS that was manually input


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
