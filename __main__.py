def chkuser():
    global p,access1,access2
    print('1.Administrator\n2.Employee')
    p=int(input('Enter user choice :'))
    if p==1:
        pa=input('Enter password :')
        if pa==a[0]:
            access1='accessed'
            print('ACCESSED')
        else:
            access1='denied'
            print('DENIED :incorrect password')
            print()
            chkuser()
    elif p==2:
        pb=input('Enter password :')
        if pb==a[1]:
            access2='accessed'
            print('ACCESSED')
        else:
            access2='denied'
            print('DENIED :incorrect password')
            print()
            chkuser()
    else:
        print('\nWrong choice')
         
try:
    with open('pass.csv','r') as f:
        a=f.read().splitlines()
    chkuser()
    if p==1 and access1=='accessed':
        import table_db
        import menu_admin
    elif p==2 and access2=='accessed':
        import table_db
        import menu_emp
    else:
        print('########END OF PROGRAM###########')
except Exception as err:
    print(err)

