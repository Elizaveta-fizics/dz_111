import json


def load_candidates_from_json(path):
    with open(path, encoding='utf-8') as file:
        return json.load(file)


def get_candidate(candidate_id):
    candidates = load_candidates_from_json("candidates.json")
    for candidate in candidates:
        if candidate_id == candidate["id"]:
            return candidate


def get_candidates_by_name(candidate_name):
    candidates = load_candidates_from_json("candidates.json")
    count_candidate = 0
    candidate_list = []
    for candidate in candidates:
        if candidate_name.lower() in candidate["name"].lower():
            count_candidate += 1
            candidate_list.append(candidate)
    candidate_new = {
        "Список кандидатов": candidate_list,
        "Количество кандидатов": count_candidate
        }
    return candidate_new


def get_candidates_by_skill(skill_name):
    candidates = load_candidates_from_json("candidates.json")
    list_candidate = []
    for candidate in candidates:
        list_candidate = candidate["skills"].split(", ")
        if skill_name in list_candidate:
            return list_candidate
