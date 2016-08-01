from __future__ import print_function
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

conn = psycopg2.connect("dbname='mumtdb' user='likit' host='localhost'")

@app.route('/api/hardware/0.1/<int:item_id>')
@app.route('/api/hardware/0.1/')
def list(item_id=None):
    cur = conn.cursor()
    if not item_id:
        cur.execute("""SELECT * FROM item_code;""")
    else:
        cur.execute("""SELECT * FROM item_code WHERE item_id = %d;""" % item_id)
    rows = cur.fetchall()
    data = []
    for r in rows:
        keys = ['item_id', 'display_code', 'group_class_id', 'type_id', 'description_id']
        item = dict(zip(keys, r))
        data.append(item)
    if rows:
        return jsonify(data)
    else:
        return 'Items not found'

if __name__=='__main__':
    app.run(debug=True)