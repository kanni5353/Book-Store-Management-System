import mysql.connector as x
y=x.connect(host='localhost',user='root',password='5353')
mycursor=y.cursor()
mycursor.execute("create database if not exists store")
mycursor.execute("use store")
mycursor.execute("create table if not exists signup(username varchar(20),password varchar(20))")
mycursor.execute("create table if not exists Available_Books(Bookid varchar(10) primary key,BookName varchar(30),Genre varchar(20),Quantity int(3),Author varchar(20),Publication varchar(30),Price int(7))")
mycursor.execute("create table if not exists Sales(CustomerName varchar(20),PhoneNumber char(10) unique key,Bookid varchar(10),BookName varchar(30),Quantity int(100),Price int(7),foreign key (Bookid) references Available_Books(Bookid))")

while True:
    print(
        """1:Signup
2:Login
3:Exit"""
    )
    ch = int(input("SIGNUP/LOGIN/EXIT(1,2,3):"))
    #Signup
    if ch==1:
        username=input("Enter Username: ")
        password=input("Enter password: ")
        mycursor.execute('insert into signup values("{}","{}")'.format(username,password))
        y.commit()
    
    #Login
    elif ch==2:
        username=input("Enter Username: ")
        mycursor.execute('select * from signup where username="{}"'.format(username))
        user = mycursor.fetchall()
        if user is not None:
            print("VALID USERNAME!!!!!!")
            pw = input("PASSWORD:")
            mycursor.execute("select password from signup where password='{}' and username='{}'".format(pw,username))
            a = mycursor.fetchall()
            if len(a)>=1:
                print(
                    """+++++++++++++++++++++++
+++LOGIN SUCCESSFULL+++
+++++++++++++++++++++++"""
                )
                print(
                    """======================================================================
++++++++++++++++++++++++++    KANNI'S.BOOK STORE     +++++++++++++++++++++++++
=========================================================================="""
                )
                while True:
                    print(
                        """1.Sell
2.Stock
3.Total Sales
4.Exit""")
                    ch=int(input("Enter your choice (in number):"))
                    
                    # Sell
                    if ch==1:
                        custname=input("Enter Customer Name: ")
                        phn=int(input("Enter Phone number:"))
                        while True:
                            bid=input("Enter Bok ID: ")
                            bname=input("Enter Bookname: ")
                            quantity=int(input("Enter the quantity"))
                            price=int(input("Enter the Price: "))
                            mycursor.execute("select quantity from available_books where bookid='{}'".format(bid))
                            if quantity<=mycursor.fetchall()[0][0]:
                                mycursor.execute("update available_books set quantity=quantity-{}".format(quantity))
                                mycursor.execute("insert into sales values('{}','{}','{}','{}',{},{})".format(ustname,phn,bid,bname,quantity,price))
                            repeat=input("Want to sell another book:(Y/N)")
                            if repeat.lower() in('n','no'):
                                print("Purchase record stored succesfully")
                                continue
                    
                    #STOCK
                    elif ch==2:
                        while True:
                            print(
                                """1.View
2.Modify
3.Back Menu""")
                            ch=int(input("Enter number of your choice: "))
                            #VIEW
                            if ch==1:
                                mycursor.execute("select bookid,bookname,genre,author,publication,quantity,price from available_books order by genre")
                                ret_lists=mycursor.fetchall()
                                if len(ret_lists)>=1:
                                    for i in ret_lists:
                                        print(i)
                                else:
                                    print("Nothing to show here yet")
                                continue
                            
                            
                            #MODIFY
                            elif ch==2:
                                while True:
                                    update=input("""1.Add
2.Subtract
3.back""")
                                    #ADD
                                    if update==1:
                                        bid=input("Enter BookID: ")
                                        quantity=int(input("Enter the Quantity: "))
                                        mycursor.execute("update available_books set quantity=quantity+{}".format(quantity))
                                        print("STOCK ADDED SUCCESFULLY")
                                        y.commit()
                                        break
                                    #SUBTRACT
                                    elif update==2:
                                        bid=input("Enter BookID: ")
                                        quantity=int(input("Enter the Quantity: "))
                                        if quantity<=mycursor.fetchall()[0][0]:
                                            mycursor.execute("update available_books set quantity=quantity-{}".format(quantity))
                                        print("STOCK subtracted SUCCESFULLY")
                                        y.commit()
                                        break
                                    #BACK
                                    elif update==3:
                                        break
                                    #REPEAT INCASE OF INVALID INPUT
                                    else:
                                        continue
                                    
                            # BACK MENU
                            elif ch==3:
                                break
                            #REPEAT INCASE OF INVALID INPUT
                            else:
                                continue
                        
                    #VIEW TOTAL SALES
                    elif ch==3:
                        mycursor.execute("select * from sales")
                        ret_lists=mycursor.fetchall()
                        if len(ret_lists)>=1:
                            for i in ret_lists:
                                print(i)
                        else:
                            print("Nothing to show here yet")
                        continue
                    #Exit to login
                    elif ch==4:
                        break
                    else:
                        continue
            #ELSE FOR INVALID PASSWORD
            else:
                print("Login Unsuccessful")
                continue
        #ELSE FOR INVALID USERNAME
        else:
            print("Invalid Username")
            continue
    #EXIT IN LOGIN
    elif ch==3:
        break
    #REPEAT INCASE OF INVALID INPUT
    else:
        continue
    
    
    
                            
                            
                                
                            
                            
                        