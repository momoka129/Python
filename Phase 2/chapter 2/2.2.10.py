from pymysql import Connection

# construct connection to mysql
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123321"
)

print(conn.get_server_info())
print(conn.host_info)
print(conn.get_host_info())
print(conn.get_proto_info())

# cursor object
cursor = conn.cursor()

# use school
conn.select_db("school")

# execute non-query sql
# cursor.execute("create table test_pymysql(id int);")
# cursor.execute("create table test_pymysql_2(id int)")  # can without ';'

# execute query sql
cursor.execute("select * from student")

results:tuple = cursor.fetchall()
# print(results)
for row in results:
    print(row)

# close connection
conn.close()