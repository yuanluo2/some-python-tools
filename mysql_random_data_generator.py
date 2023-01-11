import pymysql
import faker
import random
import time

# database information
host     = 'localhost'
port     = 3306
user     = 'root'
password = '193168'
database = 'emp'

# connect to database
conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database)
cursor = conn.cursor()

# sql and data list
sql = 'INSERT INTO t_emp (name, path, salary, age) VALUES (%s, %s, %s, %s)'
data_list = []

# generate random data
fk = faker.Faker(locale="zh-CN")

for i in range(0, 100000):
    data = (
        fk.name(),
        fk.file_path(),
        random.randint(7000, 14000),
        random.randint(16, 70)
    )
    data_list.append(data)

# execute and commit
time_start = time.perf_counter()
res = cursor.executemany(sql, data_list)
conn.commit()
time_end = time.perf_counter()

# result
print('result:', res)
print(f"Time cost: {time_end - time_start:0.4f} seconds")

# free resources
cursor.close()
conn.close()
