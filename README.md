# Rossman Predictions

This repository is for the Sales Prediction API given the Rossman dataset. The dataset was processed and a model was trained in the Processing and Model Development notebook. 

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
  <li> 
