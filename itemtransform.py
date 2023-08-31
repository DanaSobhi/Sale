import items 

class removeItem(): #class of removing item or quantity 
    def __init__(self, codei):
        self.codei = codei #get the item code 
        if not any(x['code'] == self.codei for x in items.marketItems): #check first if the item in the list 
            print("item not found") #priot not found if its not in the list 
            
        for x in items.marketItems: #loop the items 
            if x['code'] == self.codei: #check if the code matchs the item code in the list 
                print(x) #print the item content 
                numb = input("Enter the quantity of the item you want to remove\n") #get the quantity number
                if numb.isnumeric(): #check if the quantity is a number 
                    if int(numb) > int(x['quantity']): # if the quantity asked for is more than item quantity
                        answer = input("There's less quantity than this do you want to process?\n") #let the user decide to remove 
                        if answer == 'yes': # if yes 
                            choose =input("choose 1 to remove item\n choose 2 to remove quantity\n") 
                            if choose == '1':
                                items.itemsremoved.append(x) #extra list if we want to check removed itemss
                                items.marketItems.remove(x) #remove item from warehouse
                                print("Item removed and sent to removed items.") 
                            elif choose == '2': #incase  the user choose 2 
                                x['quantity'] = 0 #only quantity will be removed
                            print("Quantity has been set to 0 \n")
                        else:
                            break
                    else:
                        choose =input("choose 1 to remove item\n choose 2 to remove quantity\n") #else the quantity is less than item quantity
                        if choose == '1': #choosing 1 to remove item
                            items.itemsremoved.append(x) #append the item to removed list 
                            items.marketItems.remove(x) #remove the item from warehouse list
                            print("Item removed and sent to removed items.\n")
                        elif choose == '2':
                            k = int(x['quantity']) - int(numb) #incase only removing the quantity just subtitle requested number from quantity
                            x['quantity'] = k #return the quantity requested, doing this the quantity will be replaced already
                            print("Quantity has been set to ", k, " \n") # and print it 



class addtoStore(): # number 5 choose to list in the store 
    def __init__(self,codes):
        self.codes = codes #get the code 
    def readFoulder(self): #function to read the file 
        listofitems = [] #list of items we need to add to the store
        fname = "DistributeItems_"+self.codes+".txt" #the file name will be generated from the code
        flines = open(fname, "r") #open the file for reading
        lines = flines.readline() #read first line from the file 
        while lines: #while reading the line 
            goods = lines.split(";") #split using ;  we will have 6 sections first is the code and last is the quantity
            if not any(x['code'] == goods[0] for x in items.marketItems): #if the codes didn't match in the list then print
                print("item with code "+ goods[0]+" "+goods[1]+ " with quantity " + ''.join(goods[5].split('\n')) +" not found \n") #item name with code and asked quantity
            for x in items.marketItems: #and now check all items in the market 
                if x['code'] == goods[0]: #if the code matched 
                    if int(x['quantity']) < int(goods[5]): #if the quantity less than the quantity asked for
                        print("you requested for "  + x['code'] +" "+ x['name']+ " the quantity " + ''.join(goods[5].split('\n')))
                        listofitems.append(x) #add the item as it is since you will add all the item quantity
                        items.marketItems.remove(x) #and remove the item from the warehouse list
                    elif int(x['quantity']) > int(goods[5]): #else if the quantity greater than the quantity asked for
                        x['quantity'] = goods[5] #add only the one we need 
                        listofitems.append(x) #append it to shop list 
                        items.marketItems.remove(x) #and remove it from the warehouse list
            
            lines = flines.readline() #read the next line from the file
        return listofitems #and return the list of items we added 
      
            
    def additemstostore(self): #the function we will use to add the list of items to the shop item
        for i in items.systemmarket: #check the shop if from the shop list
            if i['code'] == self.codes:  #check the code
                i['items'] = self.readFoulder() #set the items of the shop into the list we genarate
                print("Done transforming the items into the shop \n")
        for i in items.systemmarket:
            print ("Shop details : \n", i) # extra step, print the  shops details afterwards.


class reportforItems(): #report for the items of the warehouse step 6
    def __init__(self):
        counterI =0 #counter of the items in the warehouse
        totalCost = 0 #total cost of the warehouse 
        totalSale = 0 #total sales of the warehouse
        profits = [] #profits we could make by selling all the items in the warehouse
        itemsNum =0 #item brand and their quantity
        for x in items.marketItems:
            counterI +=1 #count the items 
            itemsNum += int(x['quantity'])
            totalCost += ((float(x['cost'])) * int(x['quantity']))  #count the total cost of the items in the warehouse
            totalSale += ((float(x['sales'])) * int(x['quantity'])) #count the total sales of the warehouse
            
            profits.append(((float(x['sales'])) * int(x['quantity'])) - (((float(x['cost'])) * int(x['quantity']))))#count the profit for each brand
        totalprofit = 0
        for t in profits:
            totalprofit += float(t) #sum all the profits. 

        print ("The total profit is " , totalprofit ,"\nthe total cost is ", totalCost , "\nthe total sales is " , totalSale , "\n" )
        print("The total number of items brand is ",counterI,"\nWhile total numeber of items with their quantity is",itemsNum,"\n")


        
        



