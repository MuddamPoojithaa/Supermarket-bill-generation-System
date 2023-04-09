from datetime import datetime

name=input("enter your name:")
lists='''
rice     Rs 20/kg
sugar    Rs 30/kg
salt     Rs 20/kg
oil      Rs 80/liter
panner   Rs 110/kg
maggi    Rs 50/kg
boost    Rs 90/each
colgate  Rs 85/each 
'''
print(lists)

price=0
pricelist=[]
totalprice=0
Finalfinshprice=0
ilist=[]
qlist=[]
plist=[]

items={'rice':20,'sugar':30,'salt':20,'oil':80,'panner':110,'maggi':50,'boost':90,'colgate':85}
option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)): 
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your items:")
        quantity=int(input("enter your quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))  
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you entered item is not available:")
    else:
        print("you entered wrong number:")
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","POOJITHA SUPERMARKETt",25*"=")
            print(28*" ","HYDERABAD")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*"",'items',8*"-",'quantity',3*" ",'price')
            print()
            for i in range(len(pricelist)):
                print(i , 8*' ',8*' ',list[i] ,3*' ',qlist[i] , plist[i])
            print(75*"_")
            print(50*" ",'Totalamount:','Rs',totalprice) 
            print("gst amount",50*" ",'Rs',gst) 
            print(75*"-")
            print(50*" ",'finalalamount:','Rs',finalamount)    
            print(75*"-")
            print(50*" ","Thanks for visting")
            print(75*"-")





                


