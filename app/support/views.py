import psycopg2
from flask import url_for, jsonify
from . import support
from .. import db

conn = psycopg2.connect("dbname='mumtdb' user='likit'")

@support.route('/hardware/api/0.1/<int:item_id>')
@support.route('/hardware/api/hardware/0.1/')
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

@support.route('/uploads', methods=['POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER'],
                                    file.filename)
            file.save(filename)
            # print('File %s uploaded..' % request.files['name'])
            print(request.values.get('name'))
            return jsonify({"success": True})
