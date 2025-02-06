import mysql.connector as sql
def add():
       while True:
              print("Choose category of the item you want to add:")
              print("1. Grains")
              print("2. Milk and dairy products")
              print("3. Dry foods")
              print("4. Others")
              print("5. View bill")
              print("6. Go back")
              a=int(input("Enter choice:"))
              print()
              if a==1:
                     print('\t\t\t',"GRAINS")
                     s="SELECT *FROM GRAINS"
                     cur.execute(s)
                     data=cur.fetchall()
                     print("ITEM_NO","NAME","QTY","PRICE",sep='\t\t')
                     for r in data:
                            for i in r:
                                   if len(str(i))<=7:
                                          print(i,end='\t\t')
                                   else:
                                          print(i,end='\t')
                            print()
                     b=input("Enter item number of the item you want to purchase:")
                     cur.execute("SELECT *FROM GRAINS WHERE ITEM_NO=%s"%b)
                     f=int(input("Enter quantity needed:"))
                     d=cur.fetchone()
                     s="INSERT INTO {} VALUES('{}','{}',{},{})".format(n,d[0],d[1],f,f*d[-1])
                     cur.execute(s)
                     mycon.commit()
                     cur.execute("UPDATE GRAINS SET QTY=QTY-{} WHERE ITEM_NO={}".format(f,b))
                     mycon.commit()
                     print("Added!")
                     print()
              elif a==2:
                     print('\t\tMILK AND DAIRY PRODUCTS')
                     s="SELECT *FROM MILK_AND_DAIRY_PRODUCTS"
                     cur.execute(s)
                     data=cur.fetchall()
                     print("ITEM_NO","NAME","QTY","PRICE",sep='\t\t')
                     for r in data:
                            for i in r:
                                   if len(str(i))<=7:
                                          print(i,end='\t\t')
                                   else:
                                          print(i,end='\t')
                            print()
                     b=input("Enter item number of the item you want to purchase:")
                     cur.execute("SELECT *FROM MILK_AND_DAIRY_PRODUCTS WHERE ITEM_NO=%s"%b)
                     f=int(input("Enter quantity needed:"))
                     d=cur.fetchone()
                     s="INSERT INTO {} VALUES('{}','{}',{},{})".format(n,d[0],d[1],f,f*d[-1])
                     cur.execute(s)
                     mycon.commit()
                     cur.execute("UPDATE MILK_AND_DAIRY_PRODUCTS SET QTY=QTY-{} WHERE ITEM_NO={}".format(f,b))
                     mycon.commit()
                     print("Added!")
                     print()
              elif a==3:
                     print('\t\t\tDRY FOODS')
                     s="SELECT *FROM DRY_FOODS"
                     cur.execute(s)
                     data=cur.fetchall()
                     print("ITEM_NO","NAME","QTY","PRICE",sep='\t\t')
                     for r in data:
                            for i in r:
                                   if len(str(i))<=7:
                                          print(i,end='\t\t')
                                   else:
                                          print(i,end='\t')
                            print()
                     b=input("Enter item number of the item you want to purchase:")
                     cur.execute("SELECT *FROM DRY_FOODS WHERE ITEM_NO=%s"%b)
                     f=int(input("Enter quantity needed:"))
                     d=cur.fetchone()
                     s="INSERT INTO {} VALUES('{}','{}',{},{})".format(n,d[0],d[1],f,f*d[-1])
                     cur.execute(s)
                     mycon.commit()
                     cur.execute("UPDATE DRY_FOODS SET QTY=QTY-{} WHERE ITEM_NO={}".format(f,b))
                     mycon.commit()
                     print("Added!")
                     print()
              elif a==4:
                     print('\t\t\tOTHERS')
                     s="SELECT *FROM OTHERS"
                     cur.execute(s)
                     data=cur.fetchall()
                     print("ITEM_NO","NAME","QTY","PRICE",sep='\t\t')
                     for r in data:
                            for i in r:
                                   if len(str(i))<=7:
                                          print(i,end='\t\t')
                                   else:
                                          print(i,end='\t')
                            print()
                     b=input("Enter item number of the item you want to purchase:")
                     cur.execute("SELECT *FROM OTHERS WHERE ITEM_NO=%s"%b)
                     f=int(input("Enter quantity needed:"))
                     d=cur.fetchone()
                     s="INSERT INTO {} VALUES('{}','{}',{},{})".format(n,d[0],d[1],f,f*d[-1])
                     cur.execute(s)
                     mycon.commit()
                     cur.execute("UPDATE OTHERS SET QTY=QTY-{} WHERE ITEM_NO={}".format(f,b))
                     mycon.commit()
                     print("Added!")
                     print()
              elif a==5:
                     print('\t\t\tYOUR BILL')
                     cur.execute("SELECT *FROM %s"%n)
                     data=cur.fetchall()
                     print("ITEM_NO","NAME","QTY","PRICE",sep='\t\t')
                     for r in data:
                            for i in r:
                                   if len(str(i))<=7:
                                          print(i,end='\t\t')
                                   else:
                                          print(i,end='\t')
                            print()
                     print()
              elif a==6:
                     break
              else:
                     print("Invalid. try again")
def edit():
       print("1. Remove a particular item")
       print("2. Edit the quantity of an item")
       p=int(input("Enter your choice:"))
       if p==1:
              rno=input("Enter item number to be deleted:")
              cur.execute("DELETE FROM {} WHERE ITEM_NO={}".format(n,rno))
              mycon.commit()
              print("Item removed!")
              print()
       elif p==2:
              rno=input("Enter item number to be edited:")
              qty=int(input("Enter the new quantity:"))
              cur.execute("SELECT ROUND(PRICE/QTY) FROM {} WHERE ITEM_NO={}".format(n,rno))
              d=cur.fetchone()
              for i in d:
                  m=i
              cur.execute("UPDATE {} SET QTY={},PRICE={} WHERE ITEM_NO={}".format(n,qty,qty*m,rno))
              mycon.commit()
              print("Item updated!")
              print()
def view():
       print('\t\t\tYOUR BILL')
       cur.execute("SELECT *FROM %s"%n)
       data=cur.fetchall()
       print("ITEM_NO","NAME","QTY","PRICE",sep='\t\t')
       for r in data:
              for i in r:
                     if len(str(i))<=7:
                            print(i,end='\t\t')
                     else:
                            print(i,end='\t')
              print()
       print("\t\t\t\t\t\tTOTAL:",end='')
       cur.execute("SELECT SUM(PRICE) FROM %s"%n)
       data=cur.fetchone()
       for r in data:
              print(r)
       print()
def clear():
       cur.execute("DELETE FROM %s"%n)
       mycon.commit()
       print("List Cleared.")
       print()
#main
mycon=sql.connect(host='localhost',user='root',passwd='',database='project2022')
cur=mycon.cursor()
print("\t\t\t\tWELCOME TO FRESHMART!")
print("\t\t\tYour daily stop for grocery shopping!")
print("Now you can add whatever you need to your cart in a few simple steps and then proceed to finalize your bill!")
print()
cname=input("Enter customer name:")
cdate=input("Enter today's date in ddmm format:")
n=''
l=cname.split()
for i in l:
       n+=i
n=n+cdate
print()
cur.execute("CREATE TABLE IF NOT EXISTS %s(ITEM_NO CHAR(5),ITEM_NAME CHAR(50),QTY INT,PRICE INT)"%n)
while True:
       print("Main menu")
       print('1. Add items')
       print('2. Edit list')
       print('3. View list')
       print('4. Clear list')
       print('5. View final bill and exit')
       c=int(input("Enter choice:"))
       if c==1:
              add()
       elif c==2:
              edit()
       elif c==3:
              view()
       elif c==4:
              clear()
       elif c==5:
              view()
              print("Total amount of purchase: ₹",end='')
              cur.execute("SELECT SUM(PRICE) FROM %s"%n)
              data=cur.fetchone()
              for r in data:
                     print(r)
              break
              mycon.close()
       else:
              print("Invalid. try again")
