cart=["Mango","Guva","Banana","Orange"]
quantity=[50,30,40,60]
price=[30,40,50,60]
com=input("enter a person:")
if com=='owner':
#Owner
    print("1.Mango")
    print("2.Banana")
    print("3.Watermelon")
    print("4.Guva")
    cart=[]
    while True:
        print("1.add")
        print("2.remove")
        print("3.display")
        print("4.exit")
        ch=int(input("enter your choice:"))
        if ch==1:
            fruit=input("enter your fruit:")
            if fruit in cart:
                print(fruit,"already found")
            else:
                cart.append(fruit)
                print(fruit,"added")
        elif ch==2:
            if fruit in cart:
                cart.remove(fruit)
                print(fruit,"has been removed")
            else:
                print(fruit,"already removed")
        elif ch==3:
            for i in cart:
                print(i,end=' ')
            print()
        elif ch==4:
            print("Exit")
            break
        else:
            print("invalid option")
elif com=='customer':
    print("*"*20)
    print()
    #Customer
    while True:
        fruit=input("enter a fruit:")
        if fruit in cart:
            idx=cart.index(fruit)
            qunt=float(input("enter required quantity of fruit:"))
            if qunt<=quantity[idx]:
                cost=qunt*price[idx]
                print("pleasepay:",cost)
                quantity=quantity[idx]-qunt
            else:
                print("not enough quantity")
        else:
            print(fruit,"not available")
        ch=input("if shop was close(yes/no):")
        if ch=='yes':
            for i in zip(fruit,quantity):
                print(i[0],'-',i[1],'kgs')
                break
else:
    print("out of stock")
            
