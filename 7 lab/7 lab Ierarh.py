import pandas as pd
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# Создаем DataFrame с предоставленными данными
data = {
    'Region': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'Days': [11, 18, 20, 14, 15, 17, 15, 12, 11, 17, 12, 19, 19, 14, 15, 11, 14, 12, 10, 17, 15],
    'Visits': [4, 2, 2, 4, 4, 2, 4, 6, 4, 2, 2, 2, 2, 4, 2, 6, 4, 6, 4, 2, 4],
    'ExtrCharges': [202, 160, 137, 270, 212, 190, 212, 312, 216, 221, 195, 153, 160, 270, 192, 344, 271, 312, 301, 174, 212],
    'Tips': [204, 139, 117, 208, 173, 153, 173, 198, 187, 193, 231, 133, 133, 208, 133, 263, 183, 198, 198, 136, 173],
    'USD': [23624, 11144, 10614, 24190, 16490, 13354, 16094, 31945, 27797, 15471, 21887, 10364, 11895, 20720, 13973, 16830, 29663, 36425, 16949, 11326, 16934]
}

df = pd.DataFrame(data)

# Выбираем только интересующие нас параметры для кластеризации
features_income_tips = df[['USD', 'Tips']]
features_all = df.drop(['Region'], axis=1)

# Масштабируем данные
scaler = StandardScaler()
scaled_features_income_tips = scaler.fit_transform(features_income_tips)
scaled_features_all = scaler.fit_transform(features_all)

# Иерархическая кластеризация по среднему доходу и размеру чаевых
linkage_matrix_income_tips = linkage(scaled_features_income_tips, method='ward', metric='euclidean')
plt.figure(figsize=(12, 8))
dendrogram(linkage_matrix_income_tips, labels=df.index, leaf_rotation=90, leaf_font_size=10)
plt.title('Иерархическая кластеризация по среднему доходу и размеру чаевых')
plt.show()

# Иерархическая кластеризация по всем параметрам
linkage_matrix_all = linkage(scaled_features_all, method='ward', metric='euclidean')
plt.figure(figsize=(12, 8))
dendrogram(linkage_matrix_all, labels=df.index, leaf_rotation=90, leaf_font_size=10)
plt.title('Иерархическая кластеризация по всем параметрам')
plt.show()
