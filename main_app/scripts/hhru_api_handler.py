from datetime import datetime

import requests
import pandas as pd

from main_app.models import Vacancy


def parse_salary(item):
    salary_from = item.get('salary', {}).get('from')
    salary_to = item.get('salary', {}).get('to')
    currency = item.get('salary', {}).get('currency')  # TODO use cbr exchange
    if not salary_to and salary_from:
        return float(salary_from)
    if salary_to and not salary_from:
        return float(salary_to)
    if salary_to and salary_from:
        return (float(salary_to) + float(salary_from)) / 2
    return None


def get_response() -> str:
    api_request = "https://api.hh.ru/vacancies?search_field=name&text=инженерANDпрограммист"
    response = requests.get(api_request, headers={"User-Agent": "HH-User-Agent"})
    print(response.status_code, response.headers, response.history)
    return response.json() if response.status_code != 200 else response.status_code


def parse_json(json: str) -> list:
    items = json.get('items', [])
    vacancies = []
    for item in items:
        vacancies.append(
            Vacancy(
                name=item.get('name'),
                description=None,
                skills=item.get('snippet', {}).get('requirement'),
                company=item.get('employer', {}).get('name'),
                salary=parse_salary(item),
                area_name=item.get('area', {}).get('name'),
                published_at=datetime.strptime(item.get('published_at'), '%Y-%m-%dT%H:%M:%S%z')
            )
        )
    return vacancies


def get_latest_vacancies() -> list:
    return parse_json(get_response())

# def get_vacancies() -> list:
#     json = get_response()
