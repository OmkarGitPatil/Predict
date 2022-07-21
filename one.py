from flask import Flask

app=Flask(__name__)

@app.reoute('/')
def basic():
    return 'Basic URL Created'

@app.route('/predict',methods=['GET','POST'])
def predict():
    return 'This is predict function'

if __name__=='__main__':
    app.run(debug=True)