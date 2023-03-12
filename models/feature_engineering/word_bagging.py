from sklearn.feature_extraction.text import CountVectorizer
import csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import re
from sklearn.metrics import accuracy_score


    
y = []
all_messages  = []

with open('./../../data/SMSSpamCollection.csv', 'r') as f:
    reader = csv.reader(f)
    
    for row in reader:
         append_X = row[0][4:].lower() 
         all_messages.append( append_X)
         append_y = 1 if "spa" in row[0][0:4] else 0
         y.append(append_y)

vectorizer = CountVectorizer()
print(type(all_messages), 'ALL MESSAGE TYPE')

X  = vectorizer.fit_transform(all_messages)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# print(type(X_test), 'typerdo')
print(X_test, 'xtest')

# print(X_test.toarray().flatten(), 'erm?')

model = LogisticRegression()
model.fit(X_train, y_train)
# print(X_test, 'xtest')

# X_tester = vectorizer.transform( X_test.toarray().flatten())
predictions = model.predict(X_test)

print(predictions, 'predictions')
accuracy = accuracy_score(y_test, predictions)

print(f"Accuracy: {accuracy}")