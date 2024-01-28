import pymysql

class dbCon:
  def db_connect():
    try:
      conn = None
      conn = pymysql.connect (
        host='localhost',
        database='',
        user='root',
        password='',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
      )
    except Exception as e:
      print(f"Error connecting to the database: {str(e)}")
    return conn
