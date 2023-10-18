#buy choc and cake
# one choc is Rs 200
# one cake is 150
#get budget from user.


print("MENU")
print("----")
print(" 1.choco ")
print(" 2.cake ")
tot_bill=0
choco_bill=0
cake_bill=0
no_bill=0
tot_bill=choco_bill + cake_bill + no_bill
for i in range(2):
        ans=input("Enter your choice:" )
        if ans=="1": 
          num_choco=int(input("enter the number of choco:")) 
          choco_bill=num_choco * 200
          print("ChocoBill:",choco_bill)
        elif ans=="2":
          num_cake= int(input("enter the number of cake:"))
          cake_bill=num_cake * 150
          print("CakeBill :",cake_bill)
    
        else:
           no_bill=0
           print("Not Valid Choice Try again") 
tot_bill=choco_bill + cake_bill + no_bill           
print("Total bill :",tot_bill)          