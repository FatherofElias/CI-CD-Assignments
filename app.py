from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://example_sum_postgres_2moj_user:lcOZ8DlDUF3Mu2ZnQLm3Xcq9AGnqlJFk@dpg-ctpfkrrqf0us73ebldcg-a.ohio-postgres.render.com/example_sum_postgres_2moj'
db = SQLAlchemy(app)


class SumResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    a = db.Column(db.Integer, nullable=False)
    b = db.Column(db.Integer, nullable=False)
    result = db.Column(db.Integer, nullable=False)


@app.route('/sum', methods=['POST'])
def add_sum():
    data = request.get_json()
    a = data['a']
    b = data['b']
    result = a + b
    sum_result = SumResult(a=a, b=b, result=result)
    db.session.add(sum_result)
    db.session.commit()
    return jsonify({"a": a, "b": b, "result": result}), 201


@app.route('/sum', methods=['GET'])
def get_all_sums():
    sums = SumResult.query.all()
    result_list = [{"a": sum_result.a, "b": sum_result.b, "result": sum_result.result} for sum_result in sums]
    return jsonify(result_list), 200


@app.route('/sum/result/<int:result_value>', methods=['GET'])
def get_sums_by_result(result_value):
    sums = SumResult.query.filter_by(result=result_value).all()
    if not sums:
        return jsonify({"error": "No sums found with the specified result"}), 404

    result_list = [{"a": sum_result.a, "b": sum_result.b, "result": sum_result.result} for sum_result in sums]
    return jsonify(result_list), 200


if __name__ == '__main__':
    app.run(debug=True)
