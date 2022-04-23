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
    list_skills = []
    list_candidate_skills = []
    for candidate in candidates:
        list_skills = candidate["skills"].split(", ")
        list_skills_new = [x.lower() for x in list_skills]
        if skill_name.lower() in list_skills_new:
            list_candidate_skills.append(candidate)
    return list_candidate_skills

