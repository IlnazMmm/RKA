from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import random

# Dataset
data = [
    ("P,P,A,A,A,P", "NB"),
    ("N,N,A,A,A,N", "NB"),
    ("A,A,A,A,A,A", "NB"),
    ("P,P,P,P,P,P", "NB"),
    ("N,N,P,P,P,N", "NB"),
    ("A,A,P,P,P,A", "NB"),
    ("P,P,A,P,P,P", "NB"),
    ("P,P,P,A,A,P", "NB"),
    ("P,P,A,P,A,P", "NB"),
    ("P,P,A,A,P,P", "NB"),
    ("P,P,P,P,A,P", "NB"),
    ("P,P,P,A,P,P", "NB"),
    ("N,N,A,P,P,N", "NB"),
    ("N,N,P,A,A,N", "NB"),
    ("N,N,A,P,A,N", "NB"),
    ("N,N,A,P,A,N", "NB"),
    ("N,N,A,A,P,N", "NB"),
    ("N,N,P,P,A,N", "NB"),
    ("N,N,P,A,P,N", "NB"),
    ("A,A,A,P,P,A", "NB"),
    ("A,A,P,A,A,A", "NB"),
    ("A,A,A,P,A,A", "NB"),
    ("A,A,A,A,P,A", "NB"),
    ("A,A,P,P,A,A", "NB"),
    ("A,A,P,A,P,A", "NB"),
    ("P,N,A,A,A,P", "NB"),
    ("N,P,A,A,A,N", "NB"),
    ("P,N,A,A,A,N", "NB"),
    ("P,N,P,P,P,P", "NB"),
    ("N,P,P,P,P,N", "NB"),
    ("P,N,P,P,P,N", "NB"),
    ("N,N,A,P,P,P", "NB"),
    ("P,N,P,A,A,P", "NB"),
    ("N,P,A,P,A,P", "NB"),
    ("N,P,A,A,P,N", "NB"),
    ("A,N,N,N,N,A", "B"),
    ("P,N,N,N,N,N", "B"),
    ("N,P,N,N,N,N", "B"),
    ("A,P,N,A,N,N", "B"),
    ("N,N,N,N,N,N", "B"),
    ("N,N,N,A,N,A", "B"),
    ("N,N,N,N,N,P", "B"),
    ("N,N,N,N,N,A", "B"),
    ("N,N,N,A,N,P", "B"),
    ("N,N,N,A,N,N", "B"),
    ("N,N,A,N,N,N", "B"),
    ("P,N,N,N,N,N", "B"),
    ("A,N,N,N,N,N", "B"),
    ("N,N,N,N,N,N", "B"),
    ("P,N,N,N,A,A", "B")
]
print(len(data))
# Convert the dataset into feature and label list
X = [list(map(lambda x: 1 if x == 'P' else (0 if x == 'A' else -1), entry[0].split(','))) for entry in data]
y = [entry[1] for entry in data]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and fit the k-NN classifier
k = 7  # number of neighbors
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)
# print(X_test)
# Make predictions on the test set\

y_pred = knn.predict(X_test)
# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy}")

def randomize_data(data_string):
    data_list = data_string.split(",")
    random.shuffle(data_list)
    return ",".join(data_list)

# Пример использования
print(X_test[1][1])
data_string = "P,N,N,N,A,A"
# x: 1 if x == 'P' else (0 if x == 'A' else -1
test = []
randomized_data_strings = []
for i in range(1, 10):
    randomized_data_string = randomize_data(data_string)
    randomized_data_strings.append(randomized_data_string)

test = [[1 if entry == 'P' else (0 if entry == 'A' else -1) for entry in randomized_data.split(',')] for randomized_data in randomized_data_strings]
y_pred = knn.predict(test)
print(y_pred)


