from flask import Flask, request

from utils import format_records
from database_handler import execute_query

app = Flask(__name__)


@app.route("/stats_by_city")
def stats_by_city():
    genre = request.args.get("genre")
    if (genre,) not in execute_query("SELECT Name FROM genres"):
        return "Enter valid genre"

    query = "SELECT BillingCity as City, Name as Genre " \
            "FROM invoices LEFT JOIN invoice_items ii on invoices.InvoiceId = ii.InvoiceId " \
            "LEFT JOIN (SELECT * FROM genres LEFT JOIN tracks g on genres.GenreId = g.GenreId) t " \
            "on t.TrackId = ii.TrackId " \
            f"WHERE Genre = \'{genre}\' " \
            "GROUP BY BillingCity, Name " \
            "ORDER BY SUM(Milliseconds) DESC " \
            "LIMIT 1;"

    records = execute_query(query)

    return format_records(records)


app.run(port=5003, debug=True)
