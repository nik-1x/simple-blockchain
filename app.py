from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

from blockchain import *

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    blocks_results = check_intergrity()

    if request.method == "POST":
        _from = request.form['inFrom']
        _to = request.form['inTo']
        _amount = request.form['inAmount']

        write_block(_from, _amount, _to)

    return render_template("index.html", blockchain_results=blocks_results)


@app.route('/getblock', methods=["GET", "POST"])
def getblock_data():
    blockid = request.args.get('block_id')
    if os.path.isfile(os.curdir + "/blocks/" + str(blockid)):
        return jsonify(getblock(blockid))
    else:
        return jsonify({
            "error": "unknown block id"
        })


@app.route('/xcalc', methods=["GET", "POST"])
def getmath():
    uid = request.args.get('uid')
    return jsonify({
        "uid": uid,
        "balance": calculate(uid)
    })


if __name__ == '__main__':
    app.run(debug=True)
