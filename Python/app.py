import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import psycopg2
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
conn_string = "host='localhost' dbname='ETL_Project_DB' user='postgres' password='postgres'"

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/api/v1.0/emissions_infrastructure")
def view():
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM emissions_infrastructure LIMIT 10;")
    print(cursor)

    view_all=[]

    result = cursor.fetchall()

    for row in result:
        view_all.append(row)

    conn.close()

    return jsonify(view_all)


if __name__ == '__main__':
    app.run(debug=True)


# <table>
# {%- for row in items|batch(3, '&nbsp;') %}
#  <tr>
#  {%- for column in row %}
#    <td>{{ column }}</td>
#  {%- endfor %}
#  </tr>
# {%- endfor %}
# </table>