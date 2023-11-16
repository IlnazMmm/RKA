from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn import datasets
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
from sklearn.tree import export_graphviz
from io import StringIO

from IPython.display import Image
import pydotplus
import pandas as pd

# Предоставленные данные
import csv

# Specify the path to your CSV file
file_path = "Credit.csv"

# Create an empty list to store the parsed data
parsed_data = []

# Open the CSV file and read its contents
with open(file_path, 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file, delimiter=';')  # Assuming tabs separate values in your file

    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Convert each value in the row to an integer and append to the parsed_data list
        parsed_row = [int(value) for value in row]
        parsed_data.append(parsed_row)


#
# Имена столбцов
columns = ['кредит', 'з_плата', 'возраст', 'кр_карта']

# Создание DataFrame
df = pd.DataFrame(parsed_data, columns=columns)

# Разделение данных на признаки (X) и целевую переменную (y)
X = df[['з_плата', 'возраст', 'кр_карта']]
y = df['кредит']

# Разделение данных на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Создание и обучение модели дерева решений
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Предсказание на тестовом наборе данных
y_pred = model.predict(X_test)

# Оценка точности
accuracy = accuracy_score(y_test, y_pred)
# dot_data = StringIO()
# feature_names = ['з_плата', 'возраст', 'кр_карта']  # Замените своими именами признаков
# class_names = ['отказ', 'одобрение']  # Замените своими именами классов
# export_graphviz(model, out_file=dot_data, feature_names=feature_names, class_names=class_names,
#                 filled=True, rounded=True, special_characters=True)
# graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
# Image(graph.create_png())
plt.figure(figsize=(20, 10))
plot_tree(model, filled=True, feature_names=X.columns, class_names=['0', '1'], rounded=True, fontsize=10)
plt.show()
print(f'Accuracy: {accuracy}')

# Матрица ошибок
conf_matrix = confusion_matrix(y_test, y_pred)
print(f'Confusion Matrix:\n{conf_matrix}')

# Отчет о классификации
class_report = classification_report(y_test, y_pred)
print(f'Classification Report:\n{class_report}')
