import mysql.connector as msql
import os
db=msql.connect(host='localhost',user='root',passwd='1729@Abhi',database='Ration')
if db.is_connected()==False:
    sys.exit()
mycurs=db.cursor(buffered=True)
print()
def show_table():
    print('-'*69)
    print('Sno. ','|Product name','|Stock left','|Price(APL)','|Price(BPL)','|supply per month','|',sep='')
    print('-'*69)
    mycurs.execute("SELECT * FROM PRODUCT")
    for i in mycurs:
        print('%3s' % i[0],'  |','%-12s' % i[1],'|','%-10s' % i[2],'|','%-10s' % i[3],'|','%-10s' % i[4],'|    ','%-12s' % i[5],'|',sep='')
    print('-'*69)    
def stock():
    print('\n1.Check the stock \n2.Increase/decrease the stock of a product\n3.Cancel')
    ch=int(input('enter the choice '))
    if ch==1:
        print('-'*35)
        mycurs.execute("SELECT P_NO,P_NAME,STOCK_LEFT FROM PRODUCT")
        print('%3s' % 'P_NO',' |','%-12s' % 'P_NAME','|','%-10s' % 'STOCK_LEFT','|')
        print('-'*35)
        for i in mycurs:
            print('%3s' % i[0],'  |','%-12s' % i[1],'|','%-10s' % i[2],'|')
        print('-'*35)
    elif ch==2:
        p=input('enter the p_name for which stock is to be changed').capitalize()
        mycurs.execute('select * from product')
        for i in mycurs:
            if p==i[1]:
                tru=True
                continue
        if tru:
            s=int(input('enter new stock'))
            query="UPDATE PRODUCT SET STOCK_LEFT={} WHERE P_NAME='{}'".format(s,p)
            mycurs.execute(query)
            db.commit()
        else:
            print('\nItem not in table')
            print()
    elif ch==3:
        return 0
    else:
        print('\nInvalid choice')
        
def price():
    print('current prices')
    mycurs.execute("SELECT P_NO,P_NAME,PRICE_APL,PRICE_BPL FROM PRODUCT")
    myrecords=mycurs.fetchall()
    for i in myrecords:
        print(i)
    ch=int(input('enter your choice 1)change price for APL category 2)change price for BPL category'))    
    if ch==1:
        p=input('enter the product name for which price is to be changed')
        n=float(input('enter  new price'))
        query="UPDATE PRODUCT SET PRICE_APL={} WHERE P_NAME='{}'".format(n,p)
        mycurs.execute(query)
        db.commit()
    else:
        p=input('enter the product name for which price is to be changed')
        n=float(input('enter  new price'))
        query="UPDATE PRODUCT SET PRICE_BPL=%s WHERE P_NAME='%s'"%(n,p)
        mycurs.execute(query)
        db.commit()
def add_product():
    print('CURRENT TABLE')
    print('-'*69)
    print('Sno.','|Product name','|Stock left','|Price(APL)','|Price(BPL)','|supply per month','|',sep='')
    print('-'*69)
    mycurs.execute("SELECT * FROM PRODUCT")
    for i in mycurs:
        print('%3s' % i[0],'  |','%-12s' % i[1],'|','%-10s' % i[2],'|','%-10s' % i[3],'|','%-10s' % i[4],'|    ','%-12s' % i[5],'|',sep='')
    print('-'*69)     
    n=int(input('enter serial number of product: '))
    p=input('enter product name: ').capitalize()
    s=int(input('enter stock available(in Kg / L)'))
    pa=float(input('enter price for APL category (in per Kg / per L)'))
    pb=float(input('enter enter price for BPL category (in per Kg / per L)'))
    m=int(input('enter supply per month (in Kg / L)'))
    query="INSERT INTO PRODUCT VALUES({},'{}',{},{},{},{})".format(n,p,s,pa,pb,m)
    mycurs.execute(query)
    db.commit()
def billing():
    rno=int(input('Enter ration number'))
    stat='select status from consumer where Rationno={}'.format(rno)
    mycurs.execute(stat)
    rec=mycurs.fetchone()
    c=rec[0]
    print('enter the product names one after another (press enter after each name) enter "e" to end')
    t=0
    while True :
        i=input()
        if i.upper()=='E':
            break
        else:
            query="SELECT* FROM PRODUCT WHERE P_NAME='{}'".format(i)
            mycurs.execute(query)
            r=mycurs.fetchone()
            if r[2]==0:
                print('no stock left')
                sys.exit()
            else:
                QUERY="UPDATE PRODUCT SET STOCK_LEFT=STOCK_LEFT-SUPPLY_PERMONTH WHERE P_NAME='{}'".format(i)
                mycurs.execute(QUERY)
                db.commit()
            if c=='APL':
                print(r[0],r[1],'%10s' % r[3])
                t+=r[3]
            if c=='BPL':
                print(r[0],r[1],'%10s' % r[4])
                t+=r[4]
    print('total amount           :',t)
    mycurs.execute('select name from consumer where Rationno={}'.format(rno))
    name=mycurs.fetchone()
    total=str(t)
    #hist=(rno,':',s)
    histf=open('history.txt','w')
    histf.write('{}      {}'.format(name[0],total))                
                
while True:
    print('\n1.view product table \n2.check/add/minus the stock \n3.change the price of any item \n4.Add new product\n5.Billing\n6.Exit to main menu')
    c=int(input('enter your choice'))
    if c==1:
        show_table()
    elif c==2:
        stock()
    elif c==3:
        price()
    elif c==4:
        add_product()
    elif c==5:
        billing()
    elif c==6:
        exec(open('menu_admin.py').read())
        db='12345'
    else:
        print('invalid choice')
mycurs.close()        
    
    
