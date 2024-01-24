from datetime import datetime

import json
import requests

from main_app.models import Vacancy
from main_app.scripts.cbr_exchange_rate import get_rate_from_api


def parse_salary(item, dt):
    salary_node = item.get('salary', {})
    if not salary_node:
        return None

    salary_from = salary_node.get('from')
    salary_to = salary_node.get('to')

    if not salary_to and salary_from:
        salary = float(salary_from)
    if salary_to and not salary_from:
        salary = float(salary_to)
    if salary_to and salary_from:
        salary = (float(salary_to) + float(salary_from)) / 2
    else:
        salary = None

    currency = salary_node.get('currency')
    if currency == 'RUB':
        return salary
    elif salary:
        return salary / get_rate_from_api(dt.month, dt.year, currency)
    return None


def get_response() -> str:
    agent_ = {"User-Agent": "HH-User-Agent"}
    api_request = "https://api.hh.ru/vacancies?search_field=name&text=инженерANDпрограммист"
    response = requests.get(api_request, headers=agent_)
    return response.text if response.status_code == 200 else str(response.status_code)


def parse_json(json_str) -> list:
    v = json.loads(json_str)
    items = v.get('items', [])
    vacancies = []
    for item in items:
        snippet = item.get('snippet', {})
        employer = item.get('employer', {})
        area = item.get('area', {})
        dt = datetime.strptime(item.get('published_at'), '%Y-%m-%dT%H:%M:%S%z')
        vacancies.append(
            Vacancy(
                name=item.get('name'),
                description=None,
                key_skills=snippet.get('requirement') if snippet else None,
                company=employer.get('name') if employer else None,
                salary=parse_salary(item, dt),
                area_name=area.get('name') if area else None,
                publication_date=dt
            )
        )
    return vacancies


def load_latest_vacancies():
    Vacancy.objects.bulk_create(parse_json(get_response()))
    pass

