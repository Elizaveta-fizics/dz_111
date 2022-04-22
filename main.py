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
    candidates_skill = get_candidates_by_skill(skill_name)
    return render_template("skill.html", candidates=candidates, candidates_len=len(candidates_skill), skill_name=skill_name, candidates_skill=candidates_skill)


if __name__ == '__main__':
    app.run(debug=True)
