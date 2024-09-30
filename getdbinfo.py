import sqlite3
conn = sqlite3.connect('genjson/temp.db')
#conn = sqlite3.connect('C:/Users/gugu/Downloads/x-ui (2).db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
# 获取查询结果 
columns = cursor.fetchall()

# 打印列名称
print(columns)
cursor.close()
conn.close()