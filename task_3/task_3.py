import csv
import requests

from faker import Faker
from flask import Flask, request, Response
from http import HTTPStatus
from currency_symbols import CurrencySymbols
from pprint import pprint

from task_3.utils import format_records

app = Flask(__name__)


@app.route("/students")
def generate_students():
    amount = request.args.get('amount', '50')
    if not amount.isdigit():
        return 'Enter valid digit amount'

    amount = int(amount)

    if not 1 < amount < 1000:
        return 'ERROR: Available amount of students is from 1 to 1000'

    student_info = Faker('UK')

    student_data = []
    for i in range(amount):
        # Students must be aged between 16 and 60 (well, if you find one, who older than 60 - message me)
        student_list = [student_info.first_name(), student_info.last_name(), student_info.email(),
                        student_info.password(), student_info.date_of_birth(None, 16, 60).isoformat()]
        student_data.append(student_list)
    with open('students.csv', 'w') as f:
        data = csv.writer(f)
        data.writerow(student_data)

    return format_records(student_data)  #


@app.route("/bitcoin")
def get_bitcoin_value():
    currency = request.args.get('currency', 'USD')
    multiplier = request.args.get('count', 1.0)
    if not multiplier.isdigit():
        multiplier = 1

    multiplier = float(multiplier)

    url = 'https://bitpay.com/api/rates'
    result = requests.get(url, {})
    if result.status_code != HTTPStatus.OK:
        return Response('ERROR: Courses is not available now. Try again later', status=result.status_code)

    result = result.json()
    for i in result:
        if currency == i["code"]:
            return f'{multiplier} {CurrencySymbols.get_symbol("BTC")} is worth {i["rate"] * multiplier} ' \
                   f'{CurrencySymbols.get_symbol(currency)} '


app.run(port=5002, debug=True)
