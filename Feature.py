from flask import Flask
import numpy as np
import pandas as pd
app=Flask(__name__)

@app.reoute('/')
def basic():
    return 'Basic URL Created'

if __name__=='__main__':
    app.run(debug=True)