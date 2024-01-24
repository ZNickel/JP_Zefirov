import json


def parse_dict_to_json(d: dict, name: str, col_a, col_b):
    res = {
        "name": name,
        "columns": [
            {
                "name": col_a,
                "values": list(d.keys()),
            },
            {
                "name": col_b,
                "values": list(d.values()),
            }
        ]
    }
    with open(f"{name}.json", 'w', encoding='utf-8') as json_file:
        json.dump(res, json_file, indent=2, ensure_ascii=False)
