
from flask import Flask,url_for,render_template,request

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/Log_input/')
def Log_input():
    return render_template('Log_input.html')

with app.test_request_context('/hello',method='GET'):
    assert request.path=='/hello'
    assert request.method=='GET'
#
# with app.test_request_context():
#     print url_for('index')
#     print url_for('static',filename='')





if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0')
