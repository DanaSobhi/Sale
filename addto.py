from dataclasses import is_dataclass
import additems
import itemtransform
import os
#code by Dana Ghnimat 1200031 

def menu_display(): #just displaying the menu
    print(" ======================== Menu ===================== \n")
    print("1- Add product items to the warehouse \n ")
    print("2- Add a new supermarket to the management system; \n ")
    print("3- List of items in the warehouse based on expiry date;\n ")
    print("4- Clear an item from the warehouse; \n ")  
    print("5- Distribute products from the warehouse to a supermarket;\n ")
    print("6- Generate a report about the sales status of the warehouse; \n ")
    print("7- Exit the program")

def restore():
    try:
        fopen = open("warehouse_items.txt",'r')
        lines = fopen.readline()
        while lines:
            goods = lines.split(";") #split using ; 
            additems.addItem(goods[0],goods[1],goods[2],goods[3],goods[4],goods[5]) #send it to the class where it will add it to the item list
            lines = fopen.readline() # read next line 
    finally:
        fopen.close()


def main(): #the main that have all other functions called

    looping = True
    while looping: #while looping is true
        menu_display() #display the menu 
        optionchoose = int(input(" choose your option from the list ")) #read the user option
        if optionchoose == 1: #if user selected 1 
            print("Chosen option 1, Adding an Item to warehouse list \n")
            icode = input(" Enter your product code: ") #get the item code
            iname = input(" Enter your product name: ") #get the product name
            idate = input(" Enter your product Expire date: ") #get the expire date
            icost = input(" Enter your product cost: ") #get the cost
            isale = input(" Enter your product price of selling: ") #get the price
            iquantity = input(" Enter your product quantity: ")#get the quantity of the item
            additems.addItem(icode,iname,idate,icost,isale,iquantity) #send it to the class where it will add it to the item list
            additems.saveintoFile() #then add the item to the file
        elif optionchoose == 2: #if user selected 2 
            print("Chosen option 2, Adding an supermarket to supermarket list \n")
            sname = input(" Enter supermarket name: ") #get the name of the supermarket
            scode = input(" Enter supermarket code: ") #get the code of the supermarket
            saddress = input(" Enter supermarket address: ") #get the address of the supermarket
            additems.addSuperMarket(scode,sname,saddress) #the date will be generated automatically when you add the supermarket
        elif optionchoose == 3: #if user selected 3
            print("Chosen option 3, List the item depend on expiry date: \n")
            idate = input(" Enter expiry date: ") #get the expiry date
            additems.showItems(idate) #the item will be printed when you send the date to the class
        
        elif optionchoose == 4: #if user selected 4
            print("Chosen option 4, Delete an item or quantity from the items list\n")
            icode = input(" Enter your product code: ") #get the product code 
            itemtransform.removeItem(icode) #then send the code to the class for other operations such as deleting the item or quantity
        
        if optionchoose == 5: #if user selected 5
            print("Chosen option 5, Distribute products from the warehouse to a supermarket\n")
            scode = input(" Enter your supermarket code: ") #get the supermarket code , you must have already entered manually the item you wanted to be included in the shop
            itemtransform.addtoStore(scode).additemstostore() #send the code to the class then generate the function 
        
        elif optionchoose == 6: # if user selected 6
            print(" Generate a report from the warehouse and supermarket")
            itemtransform.reportforItems() #generate the report from the warehouse 

        elif optionchoose == 7: #if user selected 7
            print("You are about to exit the program  do you want to save last edits into warehouse ?\n")
            choose = input(" Some item might get deleted , input yes to save and exit... no to exit the program ... \n")
            if choose == "yes":
                additems.saveintoFile() #save what we had lastly in the were house 
                print("Thank you for using our system.\n")
                looping = False #and stop the loop. 
            elif choose == "no":
                print("Thank you for using our system.\n")
                looping = False #and stop the loop. 


print("\tWelcome to the Supermarket Management System ! \n")
oldfile = "warehouse_items.txt"
if os.path.isfile(oldfile): #extra step if we want old data from warehouse items 
    print("!! !! There's an  item data file would you like to restore it ? !! !!  \n")
    choose = input("Please enter yes or no to restore \n") 
    if choose == "yes":
        restore()

main() #just to call the main function 
