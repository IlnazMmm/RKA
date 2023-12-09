import pandas as pd
from sklearn.cluster import KMeans
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

# Выполняем кластеризацию для среднего дохода и размера чаевых
kmeans_income_tips = KMeans(n_clusters=3, random_state=42)
df['Cluster_Income_Tips'] = kmeans_income_tips.fit_predict(features_income_tips)

# Выполняем кластеризацию для всех параметров
kmeans_all = KMeans(n_clusters=3, random_state=42)
df['Cluster_All'] = kmeans_all.fit_predict(features_all)

# Визуализация результатов по среднему доходу и размеру чаевых
plt.scatter(df['USD'], df['Tips'], c=df['Cluster_Income_Tips'], cmap='rainbow', label='Данные')
plt.scatter(kmeans_income_tips.cluster_centers_[:, 0], kmeans_income_tips.cluster_centers_[:, 1], c='black', marker='X', s=200, label='Центроиды')
plt.title('Кластеры по среднему доходу и размеру чаевых')
plt.xlabel('Средний месячный доход туриста (USD)')
plt.ylabel('Объем чаевых за одно проживание (Tips)')
plt.legend()
plt.show()

# Визуализация результатов по всем параметрам
df['Region'] = df['Region'].astype('category')  # Кластеризация с учетом региона
plt.scatter(df['Visits'], df['USD'], c=df['Cluster_All'], cmap='rainbow', label='Данные')
plt.scatter(kmeans_all.cluster_centers_[:, 1], kmeans_all.cluster_centers_[:, 4], c='black', marker='X', s=200, label='Центроиды')
plt.title('Кластеры по всем параметрам')
plt.xlabel('Количество посещаемых в год стран (Visits)')
plt.ylabel('Средний месячный доход туриста (USD)')
plt.legend()
plt.show()
