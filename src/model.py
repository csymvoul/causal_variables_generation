from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_auc_score
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

class Model():
    def __init__(self, data: pd.DataFrame) -> None:
        self.model = LogisticRegression(max_iter=3000)
        self.data = data
        self.columns = data.columns
        self.dataset = pd.DataFrame.to_numpy(data)
        self.X = None
        self.y = None
        self.X_test = None
        self.y_test = None
        self.X_train = None
        self.y_train = None
        self.estimator = None
        self.predictions = None
        self.accuracy = None
        self.precision = None
        self.recall = None
        self.f1 = None
        self.confusion_matrix = None
        self.roc_auc = None

    def split_data(self) -> None:
        print("Splitting data...")
        self.X = self.data.drop(columns=["class"])
        self.y = self.data["class"]
        self.X, self.X_test, self.y, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)

    def preprocess_data(self) -> None:
        print("Preprocessing data...")
        self.dataset = MinMaxScaler().fit_transform(self.dataset)
        # Update data DataFrame with new values
        self.data = pd.DataFrame(self.dataset, columns=self.columns)


    def fit(self) -> None:
        print("Fitting model...")
        self.estimator = self.model.fit(self.X, self.y)

    def predict(self) -> None:
        print("Predicting...")
        self.predictions = self.estimator.predict(self.X_test)
    
    def get_predictions(self) -> np.ndarray:
        return self.predictions
    
    def get_X_train(self) -> pd.DataFrame:
        return self.X_train
    
    def get_y_train(self) -> pd.DataFrame:
        return self.y_train
    
    def get_X_test(self) -> pd.DataFrame:
        return self.X_test

    def get_y_test(self) -> pd.DataFrame:
        return self.y_test
    
    def calculate_accuracy(self) -> None:
        self.accuracy = accuracy_score(self.y_test, self.predictions)
    
    def get_accuracy(self) -> float:
        return self.accuracy
    
    def calculate_precision(self) -> None:
        self.precision = precision_score(self.y_test, self.predictions)

    def get_precision(self) -> float | np.ndarray:
        return self.precision

    def calculate_recall(self) -> None:
        self.recall = recall_score(self.y_test, self.predictions)
    
    def get_recall(self) -> float | np.ndarray:
        return self.recall
    
    def calculate_f1(self) -> None:
        self.f1 = f1_score(self.y_test, self.predictions)

    def get_f1(self) -> float | np.ndarray:
        return self.f1

    def calculate_confusion_matrix(self) -> None:
        self.confusion_matrix = confusion_matrix(self.y_test, self.predictions)

    def get_confusion_matrix(self) -> np.ndarray:
        return self.confusion_matrix

    def calculate_roc_auc(self) -> None:
        self.roc_auc = roc_auc_score(self.y_test, self.predictions)
    
    def get_roc_auc(self) -> float:
        return self.roc_auc