from collections import Counter

import numpy as np
import pandas as pd
from pandas import DataFrame

key_words_1 = 'engineer|инженер'
key_words_2 = 'soft|program|develop|разработчик|по|програм'
path = '../../v2.csv'


# path = '../../v2.csv'


# Безопасное извлечение года
# ==============================
def safe_convert_to_year(value):
    try:
        return pd.to_datetime(value).year
    except (ValueError, TypeError):
        return None


# Безопасный поиск средней ЗП
def calculate_average_salary(row):
    try:
        salary_from = float(row['salary_from'])
    except ValueError:
        salary_from = -1

    try:
        salary_to = float(row['salary_to'])
    except ValueError:
        salary_to = -1

    if salary_from != -1 and salary_to != -1:
        return (salary_from + salary_to) / 2.0
    if salary_from != -1 and salary_to == -1:
        return salary_from
    if salary_to != -1 and salary_from == -1:
        return salary_to
    else:
        return np.nan


# Кол-во по годам
# ==============================
def count_by_year(filtration: bool) -> dict:
    df = pd.read_csv(path, usecols=['name', 'published_at'])
    if filtration:
        df = df[df['name'].str.contains(key_words_1, case=False) & df['name'].str.contains(key_words_2, case=False)]
    return df['published_at'].apply(safe_convert_to_year).value_counts().to_dict()


# Топ-20 навыков по годам
def skill_top(filtration: bool):
    df = pd.read_csv(path, usecols=['name', 'key_skills', 'published_at'])
    df = df[df['key_skills'].notna()]
    if filtration:
        df = df[df['name'].str.contains(key_words_1, case=False) & df['name'].str.contains(key_words_2, case=False)]

    skills_df = df['key_skills'].str.split('\n', expand=True)
    skills_df['year'] = df['published_at'].apply(safe_convert_to_year)
    melted_df = pd.melt(skills_df, id_vars=['year'], value_name='skill').dropna()
    top_skills_by_year = melted_df.groupby(['year', 'skill']).size().reset_index(name='count')
    top = top_skills_by_year.sort_values(['year', 'count'], ascending=[True, False]).groupby('year').head(20)

    print(top)
    res_dicts = []

    years = top['year'].unique().tolist()
    for value in years:
        print(type(value))

    result_dict = {}
    # for r in top:
    #     print(r)
    # print(group)
    # result_dict[year] = list(group['skill'])

    # print(result_dict)


# Частота вакансий для города
# ==============================
def ratio_by_city(filtration: bool):
    df = pd.read_csv(path, usecols=['name', 'area_name'])
    if filtration:
        df = df[df['name'].str.contains(key_words_1, case=False) & df['name'].str.contains(key_words_2, case=False)]
    total = len(df)
    threshold = len(df) * 0.01
    d = df['area_name'].value_counts().to_dict()
    d = {key: round(value / total, 4) for key, value in d.items() if len(df[df['area_name'] == key]) > threshold}
    return dict(list(sorted(d.items(), key=lambda item: (-item[1], item[0]))))


# Динамика уровня зарплат по годам
def avg_salary_year(filtration: bool) -> dict:
    df = pd.read_csv(path, usecols=['name', 'area_name', 'salary_from', 'salary_to'])
    df['salary'] = df.apply(calculate_average_salary, axis=1)
    if filtration:
        df = df[df['name'].str.contains(key_words_1, case=False) & df['name'].str.contains(key_words_2, case=False)]
    return df.dropna(subset=['salary']).groupby('year')['salary'].mean().to_dict()


print(skill_top(True))
