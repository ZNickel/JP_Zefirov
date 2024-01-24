import matplotlib.pyplot as plt
import numpy as np


def draw_chart_xy(data: dict, title):
    t = list(reversed(list(data.keys())))
    v = list(reversed(list(data.values())))

    plt.figure(figsize=(6, 6))
    plt.barh(t, v, align='center')
    plt.title(f'ТОП-20 ({title})', loc='center', pad=20)
    plt.xticks(rotation=60)
    # plt.ylabel('', labelpad=10)
    # plt.xlabel('Года')
    plt.subplots_adjust(left=.15)
    plt.savefig(f'ТОП-20 по выбранной вакансии ({title}).png', dpi=150)

# for key in data.keys():
#     draw_chart_xy(data[key], key)
