from flask import Flask, jsonify, request
import pickle

app = Flask(__name__)

@app.route("/", methods=[ "GET"])
def index():
    return "<h1>Welcome to my App!!!!</h1>", 200

@app.route('/predict', methods=["GET"])
def predict():
    level = request.args.get("level", "")
    lang = request.args.get("lang", "")
    tweets = request.args.get("tweets", "")
    phd = request.args.get("phd", "")
    print("level:", level, lang, tweets, phd)
    prediciton = predict_interviews_well([level, lang, tweets, phd])

    if prediciton is not None:
        result = {"prediction": prediciton}
        return jsonify(result), 200
    else:
        return "Error making predcition", 400

def predict_interviews_well(instance):
    infile = open("tree.p", "rb")
    header, interview_tree = pickle.load(infile)
    print("header:", header)
    print("interview:", interview_tree)
    infile.close()
    try:
        return tdidt_classifier(interview_tree, header, instance)
    except:
        return None

    return predicition

def tdidt_classifier(tree, header, instance):
    infor_type = tree[0]
    if infor_type == "Attribute":
        attribute = tree[1]
        attribute_index = header.index(attribute)
        test_value = instance[attribute_index]
        for i in range(2, len(tree)):
            value_list = tree[i]
            if value_list[1] == test_value:
                return tdidt_classifier(value_list[2], header, instance)
    else:
        leaf_label = tree[1]
        return leaf_label

if __name__ == '__main__':
    app.run(debug= True)