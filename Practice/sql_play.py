import mysql.connector as mysql
mycon = mysql.connect(host='localhost', user='root', passwd='imroot', database='g7')
if mycon.is_connected():
    print("Suck it\n")
cursor = mycon.cursor()
cursor.execute('select * from cricket')
data = cursor.fetchall()
for i in data: print(i)
print('\n\n')
#cursor.execute('drop table cricket')
#cursor.execute('create table Cricket_Events (Sequence int primary key, Name varchar(40) not null, Type varchar(5) not null check (type in ("Men", "Women")) default "Men", Format varchar(4) not null check (format in ("Test", "ODI", "T20")) default "T20", Teams int, Year varchar(2) default "+0")')
'''for i in range(len(data)):
    cursor.execute('insert into wwe_ppv values({}, "{}", "{}")'.format(i+1, data[i][0], data[i][1]))'''
'''cursor.execute('desc cricket_events')
data = cursor.fetchall()
for i in data: print(i)
print('\n\n')'''
'''cursor.execute('select * from wwe_ppv')
data = cursor.fetchall()
for i in data: print(i)'''
mycon.commit()
mycon.close()
