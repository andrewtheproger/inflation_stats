import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 10000)
data = pd.read_csv("db_cb_questionnaire.csv", encoding="cp1251", sep=",")
#data = data[pd.to_numeric(data['p9_4'], errors='coerce').notnull()]
#data["p9_4"] = data["p9_4"].astype(float)
data = data[data.k87!= "ЗАТРУДНЯЮСЬ ОТВЕТИТЬ"]
data = data[data.k87!= "НЕТ ОТВЕТА"]
data = data[data.k87!= "Не изменились"]
data = data[data.k87!= "Росли медленнее, чем раньше"]
data = data[data.k87!= "ОТКАЗ ОТ ОТВЕТА"]
data = data[data.k87!= "Снижались"]
data = data[(data["m22"]=="Да") | (data["m22"]=="Нет")]
dct = {
    "Да": 1,
    "Нет": 0
}
data["m22"] = data["m22"].map(lambda x: dct[x] * 100)
data["m22"] = data["m22"].astype(float)
print(data["k87"].value_counts())
sns.set_theme(style="dark")

# Draw a nested barplot by species and sex
g = sns.barplot(data=data, y='m22', x='k87', errorbar=None)
plt.xlabel("Оценка роста цен за прошлые 12 месяцев")
plt.ylabel("Процент людей, решивших купить валюту")
plt.title("Высокая инфляция снижает доверие к рублю")
#g.legend.set_title("")
plt.savefig('output.png')
