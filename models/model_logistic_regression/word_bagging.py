from sklearn.feature_extraction.text import CountVectorizer
import csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    mean_squared_error,
    mean_squared_error,
    r2_score,
)
import math


y = []
all_messages = []

with open("./../../data/SMSSpamCollection.csv", "r") as f:
    reader = csv.reader(f)

    for row in reader:
        append_X = row[0][4:].lower()
        all_messages.append(append_X)
        append_y = 1 if "spa" in row[0][0:4] else 0
        y.append(append_y)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(all_messages)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = LogisticRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
print("Accuracy", round(accuracy, 4))
mse = mean_squared_error(y_test, predictions)
print("MSE", round(mse, 4))
rmse = math.sqrt(mse)
print("RMSE:", round(rmse, 4))
r2 = r2_score(y_test, predictions)
print("R-squared:", round(r2, 4))


def cross_validation(X, y):
    vectorizer_for_cross_validation = CountVectorizer()
    X = vectorizer_for_cross_validation.fit_transform(all_messages)
    model_for_cross_validation = LogisticRegression()
    folds = 5

    for index in range(folds):
        X_train_fold, X_val_fold, y_train_fold, y_val_fold = train_test_split(
            X, y, test_size=0.2, random_state=index
        )
        model_for_cross_validation.fit(X_train_fold, y_train_fold)
        y_prediction = model_for_cross_validation.predict(X_val_fold)
        accuracy_for_this_split = accuracy_score(y_val_fold, y_prediction)
        print("Fold", index, "accuracy score:", round(accuracy_for_this_split, 4))


cross_validation(all_messages, y)
