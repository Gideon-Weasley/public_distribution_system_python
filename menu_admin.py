import mysql.connector as mycon
import sys
def inp():
    x=int(input('enter serial no.  '))
    y=input('enter name  ')
    sql='insert into prod (Sno, Name) values(%s,%s)'
    cur.execute(sql,(x,y))
    for i in cur:
        print(i)
    con.commit()
def add():
    add_entry='insert into consumer values(%s,%s,%s,%s,%s)'
    rno=int(input('Enter ration number'))
    name=input('Enter name')
    phoneno=input('Enter Phone number (0123456789)')
    status=input('Enter status in society (APL/BPL)')
    gend=input('Enter gender (Male/Female)')
    values=(rno,name,phoneno,status,gend)
    cur.execute(add_entry,values)
    con.commit()
def delete():
    delete_entry='delete from consumer where Rationno = %s'
    rationno=int(input('Enter the ration number of entry to delete'))
    value=(rationno,)
    if input('Are you sure? (Y/N)').upper()=='Y':
        cur.execute(delete_entry,value)
        con.commit()
    else:
        print('Aborting.....')
        print()
from table_db import dbpass
con=mycon.connect(host='localhost',user='root',passwd=dbpass,db='ration')
cur=con.cursor(buffered=True)
print('----------------------USER : ADMINISTRATOR-----------------------')
print()
while True:
    try:
        print('1.Display Consumer table\n2.View or edit Product table\n3.Add entry to consumer table\n4.Delete Entry from Consumer table\n5.Exit')
        ch=int(input('Enter choice'))
        if ch==1:
            print('-'*65)
            print('%-5s' % 'Ration no.','|','%-19s' % 'Name','|','%-10s' % 'Phone no.','|','status','|','Gender','|')
            print('-'*65)
            cur.execute('select * from consumer')
            for x in cur:
                print('%-10s' % x[0],'|','%-19s' % x[1], '|',x[2],'|','%-6s' % x[3],'|','%-6s' % x[4],'|',end='')
                print()
            print('-'*65)
        if ch==2:
            import prod_view_edit.py
        if ch==3:
            add()
        if ch==4:
            delete()
        if ch==5:
            sys.exit()
    except Exception as i:
        print('got an Error ma dude',end=':')
        print(i)
cur.close()
