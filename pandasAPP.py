from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods = ['GET'])
def a():
    import pandas as pd
    film = pd.read_csv('https://raw.githubusercontent.com/wtitze/3E/main/2010.csv',sep=";")
    film
    return render_template('index.html', film = film)



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)