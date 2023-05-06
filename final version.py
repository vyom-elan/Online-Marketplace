print ("                               Welcome to Online Marketplace")     #Online Marketplace can be switched with any other name
lipro=[]
lipri=[]
liqty=[]
st2={}
st3={}
st4={}
st1={}
st1=input("Enter your name: ")
costt=0
def qty(price):
    q=int(input("How many of this item do you want"))
    liqty.append(q)
    for i in range(0,q):
        li7.append(pprice)
def checkout(li7):
    if len(li7) <5:
        cost = sum(li7)
    if len(li7) >=5:
        cost = sum(li7)-(sum(li7)*0.1)
    print("                                 Online Marketplace")
    print("              Address: #34, Bikasipura,Konankunte cross, Bengaluru-78")
    print("                     Phone: 1800-254-4321 (toll free)")
    print("                     email: contact@onlinemarketplace.com")
    print("                                        INVOICE  ")
    ln=len(lipri)
    for i in range(0,ln):
        print(' Item name: ',lipro[i])
        print(' Price: ',lipri[i])
        print(' Quantity: ', liqty[i])
    print(' Tax: 5%')
    costt=cost + (cost*1/20)
    

    print(" The total amount to be paid is: ",costt)
    print("Thanks for shopping with us! Have a great day!")
li7=[]
n=0
while n<=5:
    print ('''We have a wide range of products
1. Mobile Phones"
2. Smartphone Accessories
3. Office Essentials
4. Car parts
5. Fashion and Accessories
6. Checkout
 Flat 10% discount on orders including more than 5 items''')
    n = int(input("Enter your choice:"))
    if n==1:
        print('''Your Mobile Destination
1. Android Phones
2. iPhones
3. Budget Phones''')
        pc = int(input("Enter your choice:"))
        if pc==1:
            print ('''Having been in the industry for a long time, we have a great collection for you!
We have a wide range of Android Phones! 
1. Google Pixel 3 XL
2. OnePlus 7T Pro McLaren
3. Redmi Note 5 Pro
4.Huawei P20 Pro - QuadCamera
5.Redmi Note 8 Pro
''')
            ic = int(input("Please choose the phone you want: "))
            if ic ==1:
                pname="Pixel 3 XL"
                pprice=77000
                print(pname)
                print(pprice)
                print('''Camera: 12MP,ROM: 128 GB ,Snapdragon 845''')
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
            if ic ==2:
                pname="OnePlus7T Pro McLaren"
                pprice=53000
                print(pname)
                print(pprice)
                print("Camera: 24MP + 12MPROM: 128 GB,Snapdragon 855+")
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
            if ic ==3:
                pname="Redmi Note 5 Pro"
                pprice=16000
                print(pname)
                print(pprice)
                print("Camera: 12MP + 4MP","ROM: 64 GB","Snapdragon 636")
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
            if ic ==4:
                pname="Huawei P20 Pro"
                pprice=710000
                print(pname)
                print(pprice)
                print("Camera: 12MP + 12 MP + 8MP + 8MP,ROM: 32 GB,Kirin 970")
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
            if ic ==5:
                pname="Redmi Note 8 Pro"
                pprice=15000
                print(pname)
                print(pprice)
                print("Camera: 48MP AI dual camera,ROM: 128 GB,Spandragon 710")
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
        if pc==2:
            print('''1. iPhone XR
2. iPhone 11
3. iPhone 11 Pro
4. iPhone 11 Pro Max''')
            ic = int(input("Please input your choice: "))
            if ic ==1:
                pname="iPhone XR"
                pprice=43000
                print(pname)
                print(pprice)
                print('''Camera: 12MP,ROM: 32 GB,Apple A10 Fusion''')
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
            if ic ==2:
                pname="iPhone 11"
                pprice=68000
                print(pname)
                print(pprice)
                print("Camera: 12MP,ROM: 64 GB,Apple A11 Bionic")
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
            if ic ==3:
                pname="iPhone 11 Pro"
                pprice=85000
                print(pname)
                print(pprice)
                print("Camera: 12MP,ROM: 32 GB,Apple A12 Bionic")
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
            if ic ==4:
                pname="iPhone 11 Pro Max"
                pprice=110000
                print(pname)
                print(pprice)
                print("Camera: 12MP + 12MP,ROM: 256 GB,Apple A12 Bionic")
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
        if pc==3:
            print('''BUDGET PHONES"
We have a wide raange of Budget picks just for you! 
1. Realme C1
2. Redmi 6
3. Honor 7S
4. Oppo A3s''')
            ic = int(input("Please input your choice: "))
            if ic ==1:
                pname="Realme C1"
                pprice=7500
                print(pname)
                print(pprice)
                print("Camera: 12MP")
                print("ROM: 64 GB")
                print("4320 mAh")
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
            if ic ==2:
                pname="Redmi 6"
                pprice=8000
                print(pname)
                print(pprice)
                print("Camera: 12MP")
                print("ROM: 32 GB")
                print("5000 mAh")
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
            if ic ==3:
                pname="Honor 7S"
                pprice=6000
                print(pname)
                print(pprice)
                print("Camera: 12MP")
                print("ROM: 32 GB")
                print("Apple A10 Fusion")
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
            if ic ==4:
                pname="Oppo A3s"
                pprice=9000
                print(pname)
                print(pprice)
                print("Camera: 8MP")
                print("ROM: 32 GB")
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
    if n==2:
        print ("1. Earphones / Headphones")
        ac = int(input("Enter your choice"))
        if ac==1:
            print ("1. JBL Over-Ear")
            print ("2. BOSE Noise Cancelling Headphones")
            print ("3. audiotechnica CRL100 In - Ear")
            print ("4. JABRA Bluetooth Speaker")
            print ("5. NU Republic wireless headphone")
            print ("6. APPLE AIRPODS")
            print ("7. Samsung BUDS")
            ec = int(input("Please input your choice: "))
            if ec ==1:
                pname="JBL Over-Ear"
                pprice=6500
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
            if ec ==2:
                pname="BOSE Noise Cancelling Headphones"
                pprice=30000
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
            if ec ==3:
                pname="Audiotechnica CRL100 In-Ear"
                pprice=740
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
            if ec ==4:
                pname="JABRA Bluetooth Speaker"
                pprice=8000
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
            if ec ==5:
                pname="NU Republic wireless"
                pprice=1000
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
            if ec ==6:
                pname="Apple Airpods"
                pprice=10000
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
            if ec ==7:
                pname="Galaxy Buds"
                pprice=9000
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
                
    if n==3:
        print ("1. Monitors")
        print ("2. MacBooks")
        print ("3. Printers")
        oc = int(input("Enter your choice:"))
        if oc==1:
            print ("We have a wide raange of monitors just for you! ")
            print ("1. iMac 5K")
            print ("2. Dell 22 inch")
            print ("3. LG 23.8 inch")
            print ("4. BenQ LED 21 Inch")
            mc = int(input("Please input your choice: "))
            if mc ==1:
                pname="iMac 5K"
                pprice=250000
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
            if mc ==2:
                pname="Dell 22 inches"
                pprice=6500
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
            if mc ==3:
                pname="LG 23.8 inches"
                pprice=15000
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
            if mc ==4:
                pname="BenQ 21 inches"
                pprice=8500
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
        if oc==2:
            print ("1. MacBook Air")
            print ("2. macBook Pro with touchbar")
            lc = int(input("Enter your choice:"))
            if lc ==1:
                pname="MacBook Air"
                pprice=68000
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
            if lc ==2:
                pname="MacBook Pro"
                pprice=180000
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
                
        if oc==3:
            print ("1. HP WiFi Printer")
            print ("2. HP Sprockett")
            pc=int(input("Enter your choice:"))
            if pc ==1:
                pname="HP WiFi"
                pprice=11000
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
            if pc ==2:
                pname="HP Sprockett"
                pprice=5500
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
    if n==4:
        print("we have a wide range of car parts for your favourite engine 1.3L MJD")
        print('''1.Turbocharger
2.Transmission
3.Idling belt
4.Power steering belt
5.Crankshaft
6.Engine head''')
        cp=int(input("enter your choice"))              
        if cp==1:
            pname="Turbocharger"
            pprice=26000
            qty(pprice)
            lipri.append(pprice)
            lipro.append(pname)
        if cp==2:
            pname="Transmission"
            pprice=80000
            qty(pprice)
            lipri.append(pprice)
            lipro.append(pname)
        if cp==3:
            pname="Idling belt"
            pprice=2800
            qty(pprice)
            lipri.append(pprice)
            lipro.append(pname)
        if cp==4:
            pname="Power Steering belt"
            pprice=3500
            qty(pprice)
            lipri.append(pprice)
            lipro.append(pname)
        if cp==5:
            pname="Crankshaft"
            pprice=12000
            qty(pprice)
            lipri.append(pprice)
            lipro.append(pname)
        if cp==6:
            pname="Engine head"
            pprice=30000
            qty(pprice)
            lipri.append(pprice)
            lipro.append(pname)

    if n==5:
        print('''Choose your section:
1.Clothes
2.Shoes
3.Belts''')
        cs=int(input("Enter your choice: "))
        if cs==1:
            print('''We have a wide variety of chothing options for you!
1.Casual T-Shirt
2.Formal Shirt
3.Jeans
4.Socks''')
            lc=int(input("Enter your choice: "))
            if lc==1:
                pname="T-shirt"
                pprice=500
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
            if lc==2:
                pname="Formal Shirt"
                pprice=900
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
            if lc==3:
                pname="Jeans"
                pprice=800
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
            if lc==4:
                pname="Socks"
                pprice=200
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
        if cs==2:
            print('''We have a lot of different shoes to fit all your styles!
1.Nike Flyknit Trainer
2.Adidas Ultraboost 2019
3.Yeezy 350v2
4.Air Jordan 1''')
            lc=int(input("Enter your choice: "))
            if lc==1:
                pname="Flyknit Trainer"
                pprice=5000
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
            if lc==2:
                pname="Ultraboost"
                pprice=18000
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
            if lc==3:
                pname="Yeezy 350v2"
                pprice=19000
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
            if lc==4:
                pname="Jordan 1"
                pprice=9000
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname)
        if cs==3:
            print('''We have exquisite belts for you!
1.School belt
2.Standard Leather belt
3.Gucci belt
4.Louis Vuitton belt''')
            lc=int(input("Enter your choice: "))
            if lc==1:
                pname="School belt"
                pprice=800
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname) 
            if lc==2:
                pname="Leather belt"
                pprice=1000
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname) 
            if lc==3:
                pname="Gucci belt"
                pprice=30000
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname) 
            if lc==4:
                pname="LV belt"
                pprice=32000
                qty(pprice)
                lipri.append(pprice)
                lipro.append(pname) 
    if n==6:
        checkout(li7)
        break  

myfile=open("xyzshop.txt","a")
myfile.write('Customer Name='+st1+'\n')
z=len(lipri)
myfile.write('Product name'+'                  '+'Product price'+'                       '+'Qty'+'                        '+'\n')
for i in range(0,z):
    st4=str(liqty[i])
    st2=str(lipri[i])
    st3=str(lipro[i])
    myfile.write(st3+'                  '+st2+'                       '+st4+'                        '+'\n')
myfile.close()



import mysql.connector as sql
mycon=sql.connect(host="localhost",user="root",passwd="",database="test")               #linking it with MySQL database
try:
        cursor=mycon.cursor()
        for i in range(0,len(lipro)):
            inp = (liqty[i],lipro[i])
            sqlquery="update 99rpm set Quantity= Quantity- %s where ProductName= %s;"
            cursor.execute(sqlquery,inp)
            print(cursor.statement)
except:
    if (mycon.is_connected()== False):
        print('Connection to mysql database unsuccessful')

mycon.commit()
mycon.close()


