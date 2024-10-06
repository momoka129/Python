from pymysql import Connection

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123321",
    autocommit=True     # automatically commit
)

cursor = conn.cursor()

conn.select_db("school")

# cursor.execute( "insert into student values(10,'GU',30,'male') ")
cursor.execute( "insert into student values(11,'Ferry',17,'female') ")

# # data modify need to commit
# conn.commit()

conn.close()