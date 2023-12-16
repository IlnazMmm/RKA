import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Список транзакций
transactions = [
    ['shrimp', 'almonds', 'avocado', 'vegetables mix', 'green grapes', 'whole weat flour', 'yams', 'cottage cheese', 'energy drink', 'tomato juice', 'low fat yogurt', 'green tea', 'honey', 'salad', 'mineral water', 'salmon', 'antioxydant juice', 'frozen smoothie', 'spinach', 'olive oil'],
    ['burgers', 'meatballs', 'eggs'],
]

# Преобразование транзакций в формат one-hot encoded
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

print(df)

# Генерация частых наборов элементов с использованием Apriori
frequent_itemsets = apriori(df, min_support=0.001, use_colnames=True)

print(frequent_itemsets)

# Генерация ассоциативных правил
rules = association_rules(frequent_itemsets[:1000], metric="confidence", min_threshold=0.05)
#
# # Вывод ассоциативных правил
print(rules)
