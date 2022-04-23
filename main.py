from utils import *
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    candidates = load_candidates_from_json('candidates.json')
    return render_template('list.html', candidates=candidates)


@app.route("/candidate/<int:uid>/")
def inform(uid):
    candidate = get_candidate(uid)
    return render_template('card.html', candidate=candidate)


@app.route("/search/<name>/")
def search(name):
    candidates = get_candidates_by_name(name)
    return render_template('search.html', candidates=candidates, candidate_len=candidates["Количество кандидатов"])


@app.route("/skill/<skill_name>")
def get_skill(skill_name):
    candidates = load_candidates_from_json('candidates.json')
    list_candidate_skills = get_candidates_by_skill(skill_name)
    len_list_candidate_skills = len(list_candidate_skills)
    return render_template("skill.html", candidates=candidates, list_candidate_skills=list_candidate_skills, len_list_candidate_skills=len_list_candidate_skills)


if __name__ == '__main__':
    app.run(debug=True)

