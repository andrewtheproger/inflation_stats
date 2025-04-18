import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 10000)
data = pd.read_csv("deflator.csv", encoding="cp1251", sep=",")
data["Значение"] = data["Значение"].map(lambda x: str(x).replace(",", "."))
data['Значение'] = pd.to_numeric(data['Значение'], errors='coerce') 
data["Значение"] = data["Значение"].map(lambda x: x-100)
data = data[data["Год"] > 2010]
hse_palette = ["#F9B932", "#249FD8", "#A5183E"]
sns.set_theme(style="ticks")
# Draw a nested barplot by species and sex
g = sns.lineplot(data=data, x="Год", y="Значение", hue="Метрика", palette=hse_palette, sort=False)

plt.xlabel("Год")
plt.ylabel("Инфляция, %")
plt.title("Различия между метриками инфляции")
#g.legend.set_title("")
plt.savefig('inflation_type_by_metric.png')

