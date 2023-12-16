# импортируем библиотеки
import pandas as pd
import numpy as np
#загружаем данные их файла MS Excel
# проще всего положить файл в папку, где находится скрипт
# если листов больше чем один, надо указать его название в переменной sheet_name
sales=pd.read_excel('005DataSetMc.xlsx')
#проверяем результат, выводим первые пять строчек кода
sales.head()

# преобразуем таблицу таким образом, чтобы столбцы были наименования ассортимента, строки клиенты, а на пересечении
# на какую сумму они купили данных товаров
# фактически для построение данной матрицы нужны столбцы имя клиента или чек, название позции, сумма или количество купленных товаров
UID_sales=sales.pivot_table(values='Сумма', columns=['Ассортимент'], index='Имя', aggfunc=np.sum)
#Вместо NaN (значение отсутствует) проставим в ДатаФрейм 0-ки:
UID_sales[np.isnan(UID_sales)] = 0
# все значения больше 0 заменим 1, чтобы больше проявить правила. Делать не обязательно, но это повышает точность
UID_sales[UID_sales>0]=1
# пять первых строк новой таблицы
UID_sales.head()

#Создадим вначале список транзакций в формате [[1,4,5], [3,5,3], ....] - то есть каждый элемент списка -
#список того, что купил клиент:

#Создадим функцию для создания списка транзакций:
def transaction_list(df):
    list_external=[]
    for i in range(df.shape[0]):
        list_internal=[]
        data=df.iloc[i]
        index=data[data>0]
        for element in index.index:
            list_internal.append(element)
        list_external.append(list_internal)
    return list_external
# используем функцию, чтобы преобразовать массив в список транзакций

#
# Внимание! ниже мы берем только 1000 записей, так как в бесплатной версии
# notebooks не зватает памяти на обработку всех записей
#
transactions=transaction_list(UID_sales[:50])
# в данном случае не обращаем внимание на предупреждение
# как выглядит наш список
# Безусловно, к нему можно было придти и не строя бинарную матрицу
# но с бинарной матрицей можно выполнять другие операции, например, искать теже кластера
# это список товаров, которые содержаться в чеке или их покупает клиент
print(transactions[0])

# загрузим пакеты, необходимые для выполнения анализа
from pymining import itemmining, assocrules, perftesting

relim_input = itemmining.get_relim_input(transactions)
item_sets = itemmining.relim(relim_input, min_support = 1)
rules = assocrules.mine_assoc_rules(item_sets, min_support = , min_confidence = 0.3)
print(rules)

# сгенерируем ассоциативные правила с уровнем доверия 0.1 Стоит учитывать, что данный уровень поддержки крайне
# низкий и используется только для примера
# write_rules(rules, 'association_rules_group.csv')
def write_rules2(rul):
    retMass = []
    for el in rul:
        basic = ''
        for iterator in iter(el[0]):
            basic = basic + iterator + '-'
        conclution = ''
        for iterator in iter(el[1]):
            conclution=conclution+iterator+'-'
            retMass.append([basic, conclution, str(el[2]), str(el[3])])
    return retMass
rul1 = write_rules2(rules)
df_rules = pd.DataFrame(rul1, columns=['Посыл', 'Следствие', 'Поддержка', 'Достоверность'])

#имя файла AssocRules002.xlsx

writer = pd.ExcelWriter('AssocRules002.xlsx')
df_rules.to_excel(writer,'AR')
print(df_rules)
writer.save()
writer.close()