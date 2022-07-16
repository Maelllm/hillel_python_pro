import pandas
import random

from flask import Flask

app = Flask(__name__)


@app.route("/passwords")
def generate_password():
    symbol_list = [i for i in range(40, 64) if 40 <= i < 48 or 58 <= i < 64]
    numbers_list = range(48, 58)
    letter_list_upper = range(65, 91)
    letter_list_lower = range(97, 123)
    full_list = [i for i in range(40, 123) if 48 <= i < 58 or 65 <= i < 123]  # We will use it for repeatable values
    random_list = []
    k = 0
    max_element = random.randrange(6, 16) # For aiming required length of password
    while k < max_element:
        random_list.append(random.choice(full_list))  # Adding repeatable elements
        k += 1

    # Adding required elements
    for i in [random.choice(symbol_list), random.choice(numbers_list), random.choice(letter_list_upper),
              random.choice(letter_list_lower)]:
        random_list.append(i)

    random.shuffle(random_list) # This will change position of our elements for more randomness
    password_list = [chr(i) for i in random_list] # Transform into required symbols

    password = ''.join(password_list)

    return password


@app.route("/filedata")
def calculate_average():
    data = pandas.read_csv('hw.csv', index_col='Index')
    data_dict = dict(data.mean().round(2))  # Return as dict for displaying column names

    return f"<p>Average values are {data_dict}</p>"


app.run(port=5001, debug=True)
