import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import statsmodels.formula.api as smf
from statsmodels.stats.multicomp import MultiComparison
import seaborn as sns
import matplotlib.pyplot as plt

# Загрузить данные из файла shops.csv
data = pd.read_csv("../../../Downloads/shops.csv")

# Провести дисперсионный анализ
model = ols('price ~ store + origin', data=data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

# Вывести результаты
print(anova_table)

# Провести дисперсионный анализ с учетом взаимодействия факторов
model_interaction = smf.ols('price ~ store * origin', data=data).fit()
anova_table_interaction = sm.stats.anova_lm(model_interaction, typ=2)

# Вывести результаты
print(anova_table_interaction)


# Создать объект MultiComparison для проведения множественных сравнений
mc = MultiComparison(data['price'], data['product'])

# Провести анализ
result = mc.tukeyhsd()

# Вывести результаты
print(result.summary())

# Построение boxplot для цен в зависимости от продукта
data_frame = pd.read_csv("../../../Downloads/shops.csv")
df = pd.DataFrame(data)
plt.figure(figsize=(12, 8))
sns.boxplot(x='product', y='price', hue='origin', data=df, showfliers=False)
plt.xlabel('Продукт')
plt.ylabel('Цена')
plt.title('Воздействие фактора Продукт на цену в разрезе страны')
plt.legend(title='Страна', loc='upper right')
plt.show()

