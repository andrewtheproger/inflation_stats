import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 10000)
data = pd.read_csv("time_inflation.csv", encoding="cp1251", sep=",")
data["Значение"] = data["Значение"].map(lambda x: str(x).replace(",", "."))
data['Значение'] = pd.to_numeric(data['Значение'], errors='coerce') 
data["Значение"] = data["Значение"].map(lambda x: (x-1)*100)
hse_palette = ["#F9B932", "#249FD8", "#A5183E"]
sns.set_theme(style="ticks")
# Draw a nested barplot by species and sex
g = sns.lineplot(data=data, x="Месяц", y="Значение", hue="Тип", palette=hse_palette, sort=False)
for ind, label in enumerate(g.get_xticklabels()):
    if ind % 2 == 0:  # every 10th label is kept
        label.set_visible(True)
    else:
        label.set_visible(False)
plt.xlabel("Месяц")
plt.ylabel("Инфляция, %")
plt.title("Различия между месячной и накопленной инфляцией")
#g.legend.set_title("")
plt.savefig('inflation_type_by_time.png')

