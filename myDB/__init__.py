# import mysql.connector
from psycopg2 import connect, extras

'''
For cloud

host="b5grqlbaqnhiu3xs5zqs-mysql.services.clever-cloud.com"
user="umirqrxz6pdfjjpo"
passwd="4Lj01OwXEH0e5t7ZKIFU"
port="3306"
database="b5grqlbaqnhiu3xs5zqs"

For local
host="localhost"
user="root"
passwd=""
database="bus_reservation"
'''

# mydb = mysql.connector.connect(
#     host="b5grqlbaqnhiu3xs5zqs-mysql.services.clever-cloud.com",
#     user="umirqrxz6pdfjjpo",
#     passwd="4Lj01OwXEH0e5t7ZKIFU",
#     database="b5grqlbaqnhiu3xs5zqs"
# )

database = "rwmprcfu"
user = "rwmprcfu"
password = "PMATMochoBaVnxc9UvDabt-dk8KDcEIQ"
host = "arjuna.db.elephantsql.com"

mydb = connect(database=database, user=user, password=password, host=host)
mycursor = mydb.cursor()
