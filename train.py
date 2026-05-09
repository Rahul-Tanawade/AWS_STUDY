from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib
import os
<<<<<<< HEAD
save_model_path = '/home/sagemaker-user/study_projects/iris-fargate-job/models/'
=======
save_model_path  = r"C:\Users\rtanawad\Desktop\work\AI_ML_ENG\AWS\Iris_fargate_cron\\"

>>>>>>> f524110 (commiting train.py, main.py, requirements.txt and train.py)
os.makedirs(save_model_path, exist_ok=True)

iris=load_iris()
X,y=iris.data, iris.target
model=RandomForestClassifier()
model.fit(X,y)
joblib.dump(model, os.path.join(save_model_path, 'iris_rf.pkl'))
<<<<<<< HEAD
print("model saved at ",os.path.join(save_model_path, 'iris_rf.pkl'))
=======
print("model saved at ",os.path.join(save_model_path, 'iris_rf.pkl'))
>>>>>>> f524110 (commiting train.py, main.py, requirements.txt and train.py)
