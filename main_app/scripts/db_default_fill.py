from main_app.models import Theme, Category
from main_app.scripts.data_analyze import skill_top, count_by_year, avg_salary_year, ratio_by_city

category_theme_names = {
    'Востребованность': [
        'Динамика уровня зарплат по годам',  #
        'Динамика количества вакансий по годам',  #
        'Динамика уровня зарплат по годам для выбранной профессии',  #
        'Динамика количества вакансий по годам для выбранной профессии',  #
    ],
    'География': [
        'Уровень зарплат по городам',
        'Доля вакансий по городам',  #
        'Уровень зарплат по городам для выбранной профессии',
        'Доля вакансий по городам для выбранной профессии',  #
    ],
    'Навыки': [
        'ТОП-20 навыков по годам',  #
        'ТОП-20 навыков по годам для выбранной профессии',  #
    ],
}


def fill():
    for key, values in category_theme_names.items():
        category = Category.objects.create(name=key)
        for v in values:
            Theme.objects.create(name=v, category=category)


fill()
