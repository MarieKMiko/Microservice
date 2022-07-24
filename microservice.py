
from crypt import methods
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Grading Criteria</h1><p>This site provides our grading services.</p>"

@app.route("/grade", methods = ['GET'])
def grade():
    args = request.args
    student_answers = args.getlist('student_answers')
    #correct answer index number corresponds to answer number - 1 
    correct_answers_math = [
    'E', 'J', 'C', 'J', 'B', 'K', 'B', 'F', 'E', 'F', 'C', 'F', 'C', 'H', 'C', 
    'G', 'A', 'H', 'A', 'H', 'E', 'J', 'D', 'G', 'B', 'F', 'C', 'F', 'E', 'J', 
    'C', 'K', 'B', 'K', 'C', 'G', 'D', 'J', 'C', 'J', 'A', 'K', 'B', 'K', 'A', 
    'F', 'E', 'F', 'A', 'G', 'D', 'J', 'D', 'G', 'D', 'F', 'E', 'G', 'D', 'G' 
    ]
    #calculate score based on correct answer numbers
    #project ACT score compared to calculated score
    test_type = args.get("test_type")
    #answers is a list of answers
    corr = 0
    inc = 0
    scaled = 0
    i = 0

    #compare correct list to answers list
    while i<60:
        if student_answers[i] == correct_answers_math[i]:
            corr +=1
        else:
            inc +=1
        i +=1
    per = corr/60 * 100

    #corr to scaled coversion:
    #index of convert corresponds to number correct- 0-60
    convert = [
            1, 4, 6, 8, 10,
            11, 11, 12, 13, 13,
            14, 14, 14, 15, 15,
            15, 16, 16, 16, 16,
            16, 17, 17, 17, 18,
            18, 18, 19, 19, 20,
            20, 21, 22, 22, 23,
            23, 24, 24, 24, 25,
            25, 26, 26, 26, 27,
            27, 27, 28, 28, 28,
            29, 30, 30, 31, 32,
            32, 33, 34, 35, 35, 36
            ]

    scaled = convert[corr]
    
    results = {
                "test_type": test_type,
                "percent_correct": per,
                "correct_answer_count": corr,
                "incorrect_answer_count": inc,
                "scaled_projection": scaled
            }
    return jsonify(results)
    
    

app.run()



