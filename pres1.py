import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
transform={
    "perceived_inflation": "Воспринимаемая инфляция",
    "real_inflation": "ИПЦ",
    "expected_inflation": "Ожидаемая инфляция",
}
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 10000)
data = pd.read_csv("inflation_rates.csv", encoding="cp1251", sep=",")
data["rate"] = data["rate"].map(lambda x: str(x).replace(",", "."))
data['rate'] = pd.to_numeric(data['rate'], errors='coerce')
data["time"] = data["month"] + " " + data["year"].astype(str)
data["Метрика"]=data["type"].map(lambda x: transform[x])
print(data.head())
hse_palette = ["#F9B932", "#249FD8", "#A5183E"]
sns.set_theme(style="ticks")
# Draw a nested barplot by species and sex
g = sns.lineplot(data=data, x="time", y="rate", hue="Метрика", palette=hse_palette, sort=False)
g.set_xticks(range(len(data) // 3)) # <--- set the ticks first
g.set_xticklabels(list(data["year"])[:len(data) // 3])
for ind, label in enumerate(g.get_xticklabels()):
    if ind % 12 == 0:  # every 10th label is kept
        label.set_visible(True)
    else:
        label.set_visible(False)
plt.xlabel("Год")
plt.ylabel("Инфляция, %")
plt.title("Различия между метриками инфляции")
#g.legend.set_title("")
plt.savefig('inflation_types_by_stats.png')

