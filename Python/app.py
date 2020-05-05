import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import psycopg2
from flask import Flask, render_template, jsonify


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
    cursor.execute("SELECT * FROM emissions_infrastructure LIMIT 100;")
    print(cursor)

    view_all=[]

    result = cursor.fetchall()

    for row in result:
        view_all.append(row)

    conn.close()

    return render_template("template.html", list=view_all)

    #return jsonify(view_all)

if __name__ == '__main__':
    app.run(debug=True)
