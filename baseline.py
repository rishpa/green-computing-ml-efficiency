
import os
import time
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import matthews_corrcoef
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

from codecarbon import EmissionsTracker

DATA_FOLDER = "data"

results = [ ]

for file in os.listdir(DATA_FOLDER) :

       if file.endswith(".csv") :

             print(f"\nProcessing: {file}")

             path = os.path.join(DATA_FOLDER, file)
             
             df = pd.read_csv(path)

             df = df.dropna( )

             X = df.iloc[:, :-1]
             y = df.iloc[:, -1]

             for col in X.columns:
                     if X[col].dtype == "object":
                              le = LabelEncoder( )
                              X[col] = le.fit_transform(X[col].astype(str))

             if y.dtype == "object":
                   le = LabelEncoder( )
                   y = le.fit_transform(y.astype(str))

             mcc_scores = [ ]

             tracker = EmissionsTracker( )
             tracker.start( )

             start_time = time.time( )

             for i in range(100) :
                      
                      X_train, X_test, y_train, y_test = train_test_split(
                                X,
                                 y,
                                 test_size=0.2,
                                 random_state=i
                      )

                  
                      model = RandomForestClassifier(
                                  n_estimators=100,
                                  random_state=42
                      )


                      model.fit(X_train, y_train)
 
                      y_pred = model.predict(X_test)

                      mcc = matthews_corrcoef(y_test, y_pred)

                      mcc_scores.append(mcc)

             end_time = time.time( )
   
             emissions = tracker.stop( )

             avg_mcc = np.mean(mcc_scores)
             runtime = end_time - start_time

             results.append( {
                          "Dataset" : file,
                           "Model" : "RandomForest",
                           "Average_MCC" : avg_mcc,
                           "Runtime_seconds" : runtime,
                           "CO2_kg" : emissions
                 } )

results_df = pd.DataFrame(results)

results_df.to_csv("baseline_results.csv", index=False)

print("\nDone!")
print(results_df)
