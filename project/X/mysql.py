import  cymysql

con=cymysql.connect(host='localhost',passwd='root',db='yx',user='root')
cur=con.cursor()

cur.execute('call ')

res=cur.fetchall()