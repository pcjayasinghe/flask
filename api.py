import dbCon as db
from flask import Flask, request, jsonify, Response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return Response(('Hello World!'), status=200)

@app.route('/coverage', methods=['GET'])
def coverage():
  conn = db.dbCon.db_connect()
  cursor = conn.cursor()
  cursor.execute("SELECT province_name, GROUP_CONCAT(district_name) as districts FROM eze_coverage GROUP BY province_name")
  rows = cursor.fetchall()
  conn.close()
#  return jsonify(rows)

# Reorder keys
  reordered_data = []
  for row in rows:
      reordered_item = {"province_name": row["province_name"], "districts": row["districts"]}
      reordered_data.append(reordered_item)
  return jsonify(reordered_data)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')