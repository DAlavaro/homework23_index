import json
import os

from constants import BASE_DIR
from flask import Flask, request, jsonify, render_template
from utils import dict_of_utils, log_generator

app = Flask(__name__)


# получить параметры query и file_name из request.args, при ошибке вернуть ошибку 400
# проверить, что файла file_name существует в папке DATA_DIR, при ошибке вернуть ошибку 400
# с помощью функционального программирования (функций filter, map), итераторов/генераторов сконструировать запрос
# вернуть пользователю сформированный результат


@app.get('/')
def index():
    return render_template("index.html")




@app.post("/perform_query")
def perform_query():
    file_name = request.form.get('file_name')
    cmd1 = request.form.get('cmd1')
    value1 = request.form.get('value1')
    cmd2 = request.form.get('cmd2')
    value2 = request.form.get('value2')

    if None in (file_name, cmd1, value1, cmd2, value2):
        return 'Не все поля заполнены', 400

    if not os.path.exists(BASE_DIR + '/data/' + file_name):
        return 'Файл не найден', 400

    default_generator = log_generator()

    first_func = dict_of_utils.get(cmd1)
    second_func = dict_of_utils.get(cmd2)

    first_res = first_func(value1, default_generator)
    second_res = second_func(value2, first_res)

    return render_template("block.html", items=second_res)


if __name__ == '__main__':
    app.run()
