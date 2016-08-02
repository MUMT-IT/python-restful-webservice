from __future__ import print_function
import os
import psycopg2
from flask import Flask, jsonify, url_for, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Shell

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://likit:Intrinity0@localhost/mumtdb'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

conn = psycopg2.connect("dbname='mumtdb' user='likit'")

def make_shell_context():
    return dict(app=app, db=db)

manager.add_command("shell", Shell(make_context=make_shell_context))

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

@app.route('/uploads', methods=['POST'])
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

if __name__=='__main__':
    app.run(host='128.199.227.62', debug=True)
