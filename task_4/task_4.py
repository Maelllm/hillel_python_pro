from flask import Flask

from utils import format_records
from database_handler import execute_query
from webargs import fields
from webargs.flaskparser import use_kwargs

app = Flask(__name__)


@app.route("/order_price")
@use_kwargs(
    {
        "country": fields.Str(
            missing="%"
        )
    },
    location="query"
)
def order_price(country):
    if country == "":
        country = "%"
    query = "SELECT BillingCountry, SUM(UnitPrice * Quantity) as Full_Price " \
            "FROM invoice_items INNER JOIN invoices i on i.InvoiceId = invoice_items.InvoiceId " \
            f"WHERE BillingCountry LIKE \"{country}\" " \
            "GROUP BY BillingCountry;"
    records = execute_query(query)

    return format_records(records)


@app.route("/get_all_info_about_track")
@use_kwargs(
    {
        "trackid": fields.Str(
            missing='"%"'
        )
    },
    location="query"
)
def get_all_info_about_track(trackid):
    if trackid == "":
        trackid = '"%"'
    query = "SELECT * FROM tracks LEFT JOIN playlist_track pt on tracks.TrackId = pt.TrackId " \
            "LEFT JOIN albums a on a.AlbumId = tracks.AlbumId " \
            "LEFT JOIN artists a2 on a.ArtistId = a2.ArtistId " \
            "LEFT JOIN genres g on tracks.GenreId = g.GenreId " \
            "LEFt JOIN media_types mt on tracks.MediaTypeId = mt.MediaTypeId " \
            "LEFT JOIN playlists p on pt.PlaylistId = p.PlaylistId " \
            "LEFT JOIN (SELECT * FROM invoice_items AS P " \
            "LEFT JOIN (SELECT * FROM invoices as I " \
            "LEFT JOIN (SELECT * FROM customers AS C " \
            "LEFT JOIN employees e on e.EmployeeId = C.SupportRepId) " \
            "k on k.CustomerId = I.CustomerId) u on u.InvoiceId = P.InvoiceId) " \
            "T on tracks.TrackID = T.TrackId " \
            f"WHERE T.TrackId LIKE {trackid};"

    records = execute_query(query)

    return format_records(records)


@app.route("/time_all_tracks")
def time_all_tracks():
    query = "SELECT Title as Album, ROUND(CAST(SUM(Milliseconds) AS FLOAT)/3600000, 2) || ' hours' " \
            "as Duration " \
            "FROM albums LEFT JOIN tracks t on albums.AlbumId = t.AlbumId GROUP BY Title;"
    records = execute_query(query)
    return format_records(records)


app.run(port=5002, debug=True)
