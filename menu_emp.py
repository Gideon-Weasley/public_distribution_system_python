import mysql.connector as mycon
import pickle
import sys
import table_db
def inp():
    x=int(input('enter serial no.  '))
    y=input('enter name  ')
    val=(x,y)
    sql='insert into prod (Sno, Name) values(%s,%s)'
    cur.execute(sql,val)
    con.commit()
    for i in cur:
        print(i)
def billing():
    rno=int(input('Enter ration number'))
    stat='select status from consumer where Rationno={}'.format(rno)
    cur.execute(stat)
    rec=cur.fetchone()
    c=rec[0]
    print('enter the product names one after another (press enter after each name) enter "e" to end')
    t=0
    while True :
        i=input()
        if i.upper()=='E':
            break
        else:
            query="SELECT* FROM PRODUCT WHERE P_NAME='{}'".format(i)
            cur.execute(query)
            r=cur.fetchone()
            if r[2]==0:
                print('no stock left')
                sys.exit()
            else:
                QUERY="UPDATE PRODUCT SET STOCK_LEFT=STOCK_LEFT-SUPPLY_PERMONTH WHERE P_NAME='{}'".format(i)
                cur.execute(QUERY)
                con.commit()
            if c=='APL':
                print(r[0],r[1],'%10s' % r[3])
                t+=r[3]
            if c=='BPL':
                print(r[0],r[1],'%10s' % r[4])
                t+=r[4]
    print('total amount           :',t)
    cur.execute('select name from consumer where Rationno={}'.format(rno))
    name=cur.fetchone()
    total=str(t)
    #hist=(rno,':',s)
    histf=open('history.txt','w')
    histf.write('{}      {}'.format(name[0],total))
con=mycon.connect(host='localhost',user='root',passwd='1729@Abhi',db='ration')
cur=con.cursor(buffered=True)
print('------------------------------USER : EMPLOYEE---------------------------')
print()
while True:
    try:
        print('1.Display Consumer table\n2.Display Product Table\n3.Billing\n4.Exit')
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
        elif ch==2:
            print('-'*69)
            print('Sno. ','|Product name','|Stock left','|Price(APL)','|Price(BPL)','|supply per month','|',sep='')
            print('-'*69)
            cur.execute("SELECT * FROM PRODUCT")
            for i in cur:
                print('%3s' % i[0],'  |','%-12s' % i[1],'|','%-10s' % i[2],'|','%-10s' % i[3],'|','%-10s' % i[4],'|    ','%-12s' % i[5],'|',sep='')
            print('-'*69)    
        elif ch==3 :
            billing()
        elif ch==4:
            break
        else:
            print('Invalid choice')
    except Exception as i:
        print('Error !!!',end=':')
        print(i)
