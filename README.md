# Rossman Predictions

This repository is for the Sales Prediction API given the Rossman dataset. 
Here are the relevant files in this repository:
<ul>
  <li> Processing and Model Development - Main notebook used to process the data and train a model</li>
  <li> App.py - Contains the API</li>
  <li> pred_model2.joblib - Contains the pickled trained model; referenced in App.py</li>
  <li> preprocess.py - Contains the preprocessing functions that each new POST request undergoes; referenced in App.py</li>
  <li> Store.csv - Contains data of the 1,115 Rossman Stores; referenced in App.py</li>
  <li> Procfile, setup.sh, requirements.txt - Files needed to deploy the API on Heroku</li>
</ul>


To develop this API, <b>X steps</b> were performed. These are explained in detail in the Preprocess and Model Development notebook.
<ol>
  <li> Data cleaning - null values, encoding, data type formatting</li>
  <li> Feature Engineering and Reduction - Generated 4 new features and performed PCA to determine the relevant features</li>
  <li> Model Selection - Tested on 5 models with adjusted R square and RMSE as the main metrics</li>
  <li> Pickle and Export - Exported the selected trained model (Catboost) and preprocessing functions</li>
  <li> API Development - A simple API was developed to have an initial landing page and a /predict link that takes in a JSON post request and outputs the predicted Sale</li>
  <li> Deployment - The API was deployed to Heroku with the following link https://mynt-hbalcera.herokuapp.com/predict; testing was done using Postman</li>
</ol>


For any inquiries, kindly reach out to heidemlbalcera@gmail.com or https://www.linkedin.com/in/heidemae-balcera-sci/
This project is part of an application to Mynt.
