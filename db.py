import pymysql
# Connect to the database 
conn = pymysql.connect (
      host='localhost',
      database='',
      user='root',
      password='',
      charset='utf8mb4',
      cursorclass=pymysql.cursors.DictCursor
 )
# Create a cursor object
cursor = conn.cursor()
# Create table
sql_query = """CREATE TABLE `eze_coverage` (
  `system_id` int DEFAULT NULL,
  `splitter_name` varchar(255) DEFAULT NULL,
  `province_id` int DEFAULT NULL,
  `province_name` varchar(255) DEFAULT NULL,
  `district_id` int DEFAULT NULL,
  `district_name` varchar(255) DEFAULT NULL,
  `modified_on` varchar(255) DEFAULT NULL,
  `available_port` int DEFAULT NULL
)"""
# Execute the sqlQuery
cursor.execute(sql_query)