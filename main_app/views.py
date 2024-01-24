from django.shortcuts import render

from main_app.models import Vacancy, TableData, Theme
from main_app.scripts.hhru_api_handler import load_latest_vacancies


def main(request):
    return render(request, 'main_page.html')


def demand(request):
    themes = Theme.objects.filter(category__name='demand')
    return render(request, 'demand_page.html')


def geography(request):
    themes = Theme.objects.filter(category__name='geography')
    return render(request, 'geography_page.html')


def skills(request):
    themes = Theme.objects.filter(category__name='skills')
    return render(request, 'skills_page.html')


def latest(request):
    load_latest_vacancies()
    vac_list = Vacancy.objects.all().order_by('-id')[:10]
    return render(request, 'latest_page.html', context={"vac_list": vac_list})
