import json

from django.shortcuts import render

from main_app.models import Vacancy, Theme, TableFile, ChartFile
from main_app.scripts.hhru_api_handler import load_latest_vacancies


def main(request):
    return render(request, 'main_page.html')


def demand(request):
    themes = Theme.objects.filter(category__name='Востребованность')
    data = build_tables(themes)
    return render(request, 'demand_page.html', context={"data": data})


def geography(request):
    themes = Theme.objects.filter(category__name='География')
    data = build_tables(themes)
    return render(request, 'geography_page.html', context={"data": data})


def skills(request):
    themes = Theme.objects.filter(category__name='Навыки')

    charts = []

    for theme in themes:
        for chart in ChartFile.objects.filter(theme__name=theme.name):
            charts.append(chart)

    tables = []
    for theme in themes:
        for raw_t in list(TableFile.objects.filter(theme=theme)):
            json_data = json.load(raw_t.file)
            col0 = json_data["columns"][0]
            col1 = json_data["columns"][1]
            rows = []
            for i in range(len(col0['values'])):
                rows.append(f"<tr><td>{col0['values'][i]}</td><td>{round(col1['values'][i], 2)}</td></tr>")
            table = f"""
            <table>
                <thead>
                <tr><th>{col0['name']}</th><th>{col1['name']}</th></tr>
                </thead>
                <tbody>{'\n'.join(rows)}</tbody>
            </table>
            """
            tables.append(table)

    return render(request, 'skills_page.html', context={"tables": tables, "charts": charts})


def latest(request):
    load_latest_vacancies()
    vac_list = Vacancy.objects.all().order_by('-id')[:10]
    return render(request, 'latest_page.html', context={"vac_list": vac_list})


def build_tables(themes: list) -> list:
    data = []
    for theme in themes:
        tf = list(TableFile.objects.filter(theme=theme))[0]
        json_data = json.load(tf.file)
        col0 = json_data["columns"][0]
        col1 = json_data["columns"][1]
        rows = []
        for i in range(len(col0['values'])):
            rows.append(f"<tr><td>{col0['values'][i]}</td><td>{round(col1['values'][i], 2)}</td></tr>")
        table = f"""
        <table>
            <thead>
            <tr><th>{col0['name']}</th><th>{col1['name']}</th></tr>
            </thead>
            <tbody>{'\n'.join(rows)}</tbody>
        </table>
        """
        data.append([theme, table])
    return data


def build_skill_table() -> list:
    pass
