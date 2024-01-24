from datetime import datetime

import json
import requests

from main_app.models import Vacancy


def parse_salary(item):
    salary_node = item.get('salary', {})
    if not salary_node:
        return None
    salary_from = salary_node.get('from')
    salary_to = salary_node.get('to')
    currency = salary_node.get('currency')  # TODO use cbr exchange

    if not salary_to and salary_from:
        return float(salary_from)
    if salary_to and not salary_from:
        return float(salary_to)
    if salary_to and salary_from:
        return (float(salary_to) + float(salary_from)) / 2
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
        vacancies.append(
            Vacancy(
                name=item.get('name'),
                description=None,
                key_skills=snippet.get('requirement') if snippet else None,
                company=employer.get('name') if employer else None,
                salary=parse_salary(item),
                area_name=area.get('name') if area else None,
                publication_date=datetime.strptime(item.get('published_at'), '%Y-%m-%dT%H:%M:%S%z')
            )
        )
    return vacancies


def load_latest_vacancies():
    Vacancy.objects.bulk_create(parse_json(get_response()))
    pass
