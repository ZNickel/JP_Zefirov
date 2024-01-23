from django.shortcuts import render


def main(request):
    return render(request, 'main_page.html')


def demand(request):
    return render(request, 'demand_page.html')


def geography(request):
    return render(request, 'geography_page.html')


def skills(request):
    return render(request, 'skills_page.html')


def latest(request):
    return render(request, 'latest_page.html')
