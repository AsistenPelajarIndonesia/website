from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

questions = [
    {"id": 1, "text": "You enjoy vibrant social events with lots of people.", "dimension": "EI"},
    {"id": 2, "text": "You often spend time exploring unrealistic yet intriguing ideas.", "dimension": "SN"},
    {"id": 3, "text": "Your travel plans are more likely to look like a rough list of ideas than a detailed itinerary.", "dimension": "JP"},
    {"id": 4, "text": "You are more inclined to follow your head than your heart.", "dimension": "TF"},
    {"id": 5, "text": "You often find it difficult to introduce yourself to other people.", "dimension": "EI"},
    {"id": 6, "text": "You get carried away by fantasies and ideas.", "dimension": "SN"},
    {"id": 7, "text": "You prefer to have a to-do list for each day.", "dimension": "JP"},
    {"id": 8, "text": "You consider yourself more practical than creative.", "dimension": "TF"},
]

@app.route('/')
def index():
    return render_template_string(open('/Users/aqila/BIA/website/index.html').read(), questions=questions)

@app.route('/submit', methods=['POST'])
def submit_answers():
    data = request.json
    answers = data.get('answers')

    if not answers or len(answers) != len(questions):
        return jsonify({"error": "Invalid answers"}), 400

    # Process answers to determine personality type
    personality_type = determine_personality_type(answers)
    return jsonify({"personality_type": personality_type})

def determine_personality_type(answers):
    scores = {
        "E": 0, "I": 0,
        "S": 0, "N": 0,
        "T": 0, "F": 0,
        "J": 0, "P": 0
    }

    for answer, question in zip(answers, questions):
        dimension = question["dimension"]
        if dimension == "EI":
            if answer in ["E", "e"]:
                scores["E"] += 1
            elif answer in ["I", "i"]:
                scores["I"] += 1
        elif dimension == "SN":
            if answer in ["S", "s"]:
                scores["S"] += 1
            elif answer in ["N", "n"]:
                scores["N"] += 1
        elif dimension == "TF":
            if answer in ["T", "t"]:
                scores["T"] += 1
            elif answer in ["F", "f"]:
                scores["F"] += 1
        elif dimension == "JP":
            if answer in ["J", "j"]:
                scores["J"] += 1
            elif answer in ["P", "p"]:
                scores["P"] += 1

    personality_type = ""
    personality_type += "E" if scores["E"] > scores["I"] else "I"
    personality_type += "S" if scores["S"] > scores["N"] else "N"
    personality_type += "T" if scores["T"] > scores["F"] else "F"
    personality_type += "J" if scores["J"] > scores["P"] else "P"

    return personality_type

if __name__ == '__main__':
    app.run(debug=True)
