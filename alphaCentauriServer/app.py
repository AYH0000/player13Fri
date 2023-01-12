# from flask import Flask, request, jsonify # Flask


# app = Flask(__name__)

# @app.route('/')
# def users():

#     obj =  '1234'
# 	# with Json
#     return jsonify({"param": obj})

# @app.route('/test')
# def users():

#     obj =  '1234'
# 	# with Json
#     return jsonify({"param": obj})


# if __name__ == "__main__":
#     app.run(debug = True)

from flask import Flask # Flask

app = Flask(__name__)

@app.route('/flaskSV')
def flaskSV():
	# users 데이터를 Json 형식으로 반환한다
    return {"members": [{ "id" : 1, "name" : "yerin" },
                        { "id" : 2, "name" : "dalkong" }]}

#     obj =  '1234'
# 	# with Json
#     return jsonify({"param": obj})

if __name__ == "__main__":
    app.run(debug = True)