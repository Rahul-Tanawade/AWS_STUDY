import joblib
from sklearn.datasets import load_iris
import os
save_model_path =r"C:\Users\rtanawad\Desktop\work\AI_ML_ENG\AWS\Iris_fargate_cron\\"
model_saved_as=os.path.join(save_model_path, 'iris_rf.pkl')

model_l=joblib.load(model_saved_as)

iris=load_iris()
X=iris.data[:5]
predictions=model_l.predict(X)
print("model predictions are ",predictions)