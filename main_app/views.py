from django.shortcuts import render

from main_app.models import Vacancy
from main_app.scripts.hhru_api_handler import load_latest_vacancies


def main(request):
    return render(request, 'main_page.html')


def demand(request):
    return render(request, 'demand_page.html')


def geography(request):
    return render(request, 'geography_page.html')


def skills(request):
    return render(request, 'skills_page.html')


def latest(request):
    load_latest_vacancies()
    vac_list = Vacancy.objects.all().order_by('-id')[:10]
    return render(request, 'latest_page.html', context={"vac_list": vac_list})
