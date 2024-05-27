import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template, redirect, flash, send_file
from sklearn.preprocessing import MinMaxScaler
from werkzeug.utils import secure_filename
import pickle

import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template, redirect, flash, send_file
from sklearn.preprocessing import MinMaxScaler
from werkzeug.utils import secure_filename
import pickle
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

app = Flask(__name__) #Initialize the flask App


heart = pickle.load(open('heartd.pkl','rb'))
@app.route('/')

@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/chart')
def chart():
	return render_template('chart.html')

#@app.route('/future')
#def future():
#	return render_template('future.html')    

@app.route('/login')
def login():
	return render_template('login.html')
@app.route('/upload')
def upload():
    return render_template('upload.html')  
@app.route('/preview',methods=["POST"])
def preview():
    if request.method == 'POST':
        dataset = request.files['datasetfile']
        df = pd.read_csv(dataset,encoding = 'unicode_escape')
        df.set_index('Id', inplace=True)
        return render_template("preview.html",df_view = df)	


#@app.route('/home')
#def home():
 #   return render_template('home.html')

@app.route('/prediction', methods = ['GET', 'POST'])
def prediction():
    return render_template('prediction.html')


#@app.route('/upload')
#def upload_file():
#   return render_template('BatchPredict.html')



@app.route('/predict',methods=['POST'])
def predict():
	int_feature = [x for x in request.form.values()]
	 
	final_features = [np.array(int_feature)]
	 
	result=heart.predict(final_features)
	if result == 1:
			result = "Positive"
	else:
		result = 'Negative'
	
	return render_template('prediction.html', prediction_text= result)
@app.route('/performance')
def performance():
	return render_template('performance.html')   
    
if __name__ == "__main__":
    app.run()
