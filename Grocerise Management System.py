
#Edward Ding Hong Wai
#TP065396
 
# MAINMENU PAGE
def mainmenu():                                                                                             #Define a function (mainmenu)
    print("Select type of command for the system to proceed\n")                                             #Display text (Select type of command for the system to proceed)
    print("\t1.Admin Page\n")                                                                               #Display text (Admin Page)
    print("\t2.New Customer Page\n")                                                                        #Display text (New Customer Page)
    print("\t3.Registered Customer Page\n")                                                                 #Display text (Registered Customer Page)
    print("\t4.Exit Page\n")                                                                                #Display text (Exit Page)
    MenuValid = False                                                                                       #Booleans used to represent true or false value (MenuVailid is False then try....)
    
    try:                                                                                                    #Try let you test the a block of code for error  
        user = int(input("Enter the number command of your choice:"))                                       #Take the input (Enter the number command of your choice:)
        MenuValid = True                                                                                    #Booleans used to represent true or false value (MenuValid is True then continue to....)
    except:                                                                                                 #Except block handle the error without red code 
        if ValueError:                                                                                      #if allows for conditional execution of a statement (if ValueError)
            print("Invalid Input!")                                                                         #Display text (Invalid Input)
            mainmenu()
    if MenuValid:                                                                                           #if allows for conditional execution of a statement (if Menuvalid)
        if (user<1) or (user>4):                                                                            #if allows for conditional execution of a statement (if less then 1 or more then 4)
            print("Invalid Input!")                                                                         #Display text (Invalid Input)
            mainmenu()
        elif (user == 1):                                                                                   #elif used in condition statement (elif user equality to 1)
            AdminLogin()                                                                                    #Direct to AdminLogin
        elif (user == 2):                                                                                   #elif used in condition statement (elif user equality to 2)
            NewCustomerPage()                                                                               #Direct to NewCustomerPage
        elif (user == 3):                                                                                   #elif used in condition statement (elif user equality to 3)
            CustomerLogin()                                                                                 #Direct to CustomerLogin
        elif (user == 4):                                                                                   #elif used in condition statement (elif user equality to 4) 
            print("Thank you for visiting Fresh Food Groceries Store\n")                                    #Display text (Thank you for visiting Fresh Food Groceries Store)
            print("See You Again!\n")                                                                       #Display text (See You Again!)
            end()                                                                                           #Direct to end         

def end():                                                                                                  #Define a function (end)
    return "End Program"                                                                                    #Return statement that you can use inside a function or method to send the function's result back to the caller (End Program)




 
# ADMIN LOGIN
def AdminLogin():                                                                                           #Define a function (AdminLogin)
    print("Please Login")                                                                                   #Display text (Admin Login)
    AdminLogintxt = open("AdminLogin.txt","r")                                                              #AdminLogin.txt is a text file and open with read mode 
    AdminLogintxt = (AdminLogintxt.readlines())                                                             #Read AdminLogin.txt line by lines in text file
    AdminU = "-"                                                                                            #AdminU equals to dash
    AdminUsername = input("Enter your username: \n (Click enter to back to Main Menu Page.)\n")             #Take the input (Enter your username and click enter to back to main menu page) 
    if AdminUsername == '':                                                                                 #if allows for conditional execution of a statement (if AdminUsername equality to blank)
        mainmenu()                                                                                          #Direct to mainmenu
    else:                                                                                                   #else used in condition statement (else (xxxx) then it will continue to (xxxx))
        for text in AdminLogintxt:                                                                          #AdminLogin is a list that contains the username and password of admin
            if text.startswith(AdminUsername):                                                              #if allows for conditional execution of a statement (if text start with AdminUsername)
                AdminU,AdminP = text.split("#")                                                             #Splits a string into a list by using (#)
                AdminU = AdminU.strip()                                                                     #Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters
                AdminP = AdminP.strip()                                                                     #Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters                                                                                                                                  
                AdminPassword = input("Enter your password:")                                               #Take the input (Enter your password:)
                if AdminPassword != AdminP:                                                                 #if allows for conditional execution of a statement (if AdminPassword is not AdminP)
                    print("Incorrect password. Please try again")                                           #Display text (Incorrect password. Please try again)
                    AdminLogin()                                                                            #Direct to AdminLogin
                else:                                                                                       #else used in condition statement (else (xxxx) then it will direct to (xxxx))
                    print("Login Successful")                                                               #Display text (Login successful)
                    AdminMenu()                                                                             #Direcy to AdminMenu 
        if AdminU == "-":                                                                                   #if allows for conditional execution of a statement (if AdminU equality to dash)
            print("Username not found.")                                                                    #Display text (Username not found)
            AdminLogin()                                                                                    #Direct to AdminLogin

def AdminMenu():                                                                                            #Define a function (AdminMenu)
    print("Welcome to Groceries Management Page\n")                                                         #Display text (Welcome to Groceries Management Page)
    print("Select the features below\n")                                                                    #Display text (Select the features below)
    print("\t1.Upload Groceries Information\n")                                                             #Display text (1.Upload Groceries Information)
    print("\t2.View All Groceries\n")                                                                       #Display text (2.View All Groceries)
    print("\t3.Modify Or Update Groceries Information\n")                                                   #Display text (3.Modify Or Update Groceries Information)
    print("\t4.Delete Groceries Information\n")                                                             #Display text (4.Delete Groceries Information)
    print("\t5.Search Groceries Details\n")                                                                 #Display text (5.Search Groceries Details)
    print("\t6.View All Orders\n")                                                                          #Display text (6.View All Orders)
    print("\t7.Search Order for Specific Customer\n")                                                       #Display text (7.Search Order for Specific Customer)
    print("\t8.Exit\n")                                                                                     #Display text (8.Exit)
    MenuValid = False                                                                                       #Booleans used to represent true or false value ( MenuVailid is False then try....)
    try:                                                                                                    #Try let you test the a block of code for error
        user = int(input("Enter the number command of your choice:"))                                       #Take the input (Enter the number command of your choice:)
        MenuValid = True                                                                                    #Booleans used to represent true or false value ( MenuValid is True then continue to....)
    except:                                                                                                 #Except block handle the error without red code
        print("Invalid Input!")                                                                             #Display text (Invalid Input!)
        AdminMenu()                                                                                         #Direct to AdminMenu
    if MenuValid:                                                                                           #if allows for conditional execution of a statement (if Menuvalid)
        if (user<1) or (user>9):                                                                            #if allows for conditional execution of a statement (if user less then 4 or user more then 9)
            print("Invalid Input!")                                                                         #Display text (Invalid Input!)
            AdminMenu()                                                                                     #Direct to AdminMenu
        elif (user == 1):                                                                                   #elif used in condition statement (elif user equality to 1) 
            UploadGroceriesInformation()                                                                    #Direct to UploadGroceriesInformation
        elif (user == 2):                                                                                   #elif used in condition statement (elif user equality to 2)
            AdminViewAllGroceries()                                                                         #Direct to AdminViewAllGroceries
        elif (user == 3):                                                                                   #elif used in condition statement (elif user equality to 3)
            ModifyOrUpdateGroceriesInformation()                                                            #Direct to ModifyOrUpdateGroceriesInformation
        elif (user == 4):                                                                                   #elif used in condition statement (elif user equality to 4)
            DeleteGroceriesDetails()                                                                        #Direct to DeleteGroceriesDetails
        elif (user == 5):                                                                                   #elif used in condition statement (elif user equality to 5)
            SearchGroceriesDetails()                                                                        #Direct to SearchGroceriesDetails
        elif (user == 6):                                                                                   #elif used in condition statement (elif user equality to 6)
            ViewAllOrders()                                                                                 #Direct to ViewAllOrders
        elif (user == 7):                                                                                   #elif used in condition statement (elif user equality to 7)
            SearchOrderForSpecificCustomer()                                                                #Direct to SearchOrderForSpecificCustomer
        elif (user == 8):                                                                                   #elif used in condition statement (elif user equality to 8)
            print("Thank you for visiting Fresh Food Groceries Store\n")                                    #Display text (Thank you for visiting Fresh Food Groceries Store)
            print("See You Again!\n")                                                                       #Display text (See You Again!)
            end()                                                                                           #Direct to end





#UPLOAD GROCERIES DETAILS
def UploadGroceriesInformation():                                                                           #Define a function (UploadGroceriesInformation)
    UploadValid = False                                                                                     #Booleans used to represent true or false value (UploadValid is False then try....)
    Categories = input("Enter the name of categories:  \n (Click enter to back to Admin Menu Page.)\n")     #Take the input (Enter the name of categories:Click enter to back to Admin Menu Page.)
    if Categories == '':                                                                                    #if allows for conditional execution of a statement (if category equality to blank)
        AdminMenu()                                                                                         #Direct to AdminMenu
    elif Categories == ("Vegetable"):                                                                       #elif used in condition statement (elif categories equality to Vegetable)
        Vegetable = "Gro_Vegetable.txt"                                                                     #Gro_Vegetable.txt is a text file
        txt = open(Vegetable, "r")                                                                           
        txt = txt.readlines()                                                                               #read txt line by lines in text file
        UploadValid = True                                                                                  #Booleans used to represent true or false value (UploadValid is True then continue to....)
    elif Categories == ("Fruits"):                                                                          #elif used in condition statement (elif categories equality to Fruits)
        Fruits = "Gro_Fruits.txt"                                                                           #Gro_Vegetable.txt is a text file
        txt = open(Fruits, "r")                                                                              
        txt = txt.readlines()                                                                               #read txt line by line in text file
        UploadValid = True                                                                                  #Booleans used to represent true or false value (UploadValid is True then continue to....)
    elif Categories == ("Ingredient"):                                                                      #elif used in condition statement (elif categories equality to Ingredient)
        Ingredient = "Gro_Ingredient.txt"                                                                   #Gro_Ingredient.txt is a text file
        txt = open(Ingredient, "r")                                                                         
        txt = txt.readlines()                                                                               #read txt line by line sin text file
        UploadValid = True                                                                                  #Booleans used to represent true or false value (UploadValid is True then continue to....)
    else:                                                                                                   #else used in condition statement (else (xxxx) then it will continue to (xxxx))
        print("Invalid Input!")                                                                             #Display text (Invalid Input!)
        UploadGroceriesInformation()                                                                        #Direct to UploadGroceriesInformation
    GroceryExist = False                                                                                    #Booleans used to represent true or false value (GroceryExist is False then try....)
    if UploadValid:                                                                                         #if allows for conditional execution of a statement (if UploadValid)
        GroceriesN = input("Enter the name of grocery:")                                                    #Take the input (Enter the name of grocery:)
        for grocery in txt:                                                                                 #For loop is used for iterating over a sequence (for grocery in text file)
            if grocery.startswith(GroceriesN):                                                              #if allows for conditional execution of a statement (if grocery start with GroceriesN)
                print("This grocery has been uploaded.")                                                    #Display text (This grocery has been uploaded.)
                GroceryExist = True                                                                         #Booleans used to represent true or false value (GroceryExist is True then continue to....)
                break                                                                                       #Break is for a loop control statement
        if GroceryExist:                                                                                    #if allows for conditional execution of a statement (if GroceryExits)
            UploadGroceriesInformation()                                                                    #Direct to UploadGroceriesInformation
        else:                                                                                               #else used in condition statement (else (xxxx) then it will continue to (xxxx))
            GroceriesED = input("Enter the expiry date of grocery(dd/mm/yyyy):")                            #Take the input (Enter the expiry date of grocery(dd/mm/yyyy):)
            GroceriesP = input("Enter price of grocery:RM")                                                 #Take the input (Enter price of grocery:RM)
            GroceriesS = input("Enter specification of grocery:")                                           #Take the input (Enter specification of grocery:)
            print("Name:",GroceriesN)                                                                       #Display text (Name:,GroceriesN)
            print("Expiry date:",GroceriesED)                                                               #Display text (Expiry date:,GroceriesED)
            print("Price: RM",GroceriesP)                                                                   #Display text (Price: RM,GroceriesP)
            print("Type of specification:",GroceriesS)                                                      #Display text (Type of specification:,GroceriesS)
            print("Uploaded Successful")                                                                    #Display text (Uploaded Successfu)
 
            if Categories == ("Vegetable"):                                                                 #if allows for conditional execution of a statement (if Categories equality to Vegetable)
                UploadGroceriesInformationtxt = open(Vegetable,"a")                                         #Open Vegetable text file and add append for additionally adding info 
            elif Categories == ("Fruits"):                                                                  #elif used in condition statement (elif categories equality to Fruits)
                UploadGroceriesInformationtxt = open(Fruits,"a")                                            #Open Fruits text file and add append for additionally adding info
            elif Categories == ("Ingredient"):                                                              #elif used in condition statement (elif categories equality to Ingredient)
                UploadGroceriesInformationtxt = open(Ingredient,"a")                                        #Open Ingredient text file and add append for additionally adding info
            UploadGroceriesInformationtxt.write("\n")                                                       #(\n) added to move to new line
            UploadGroceriesInformationtxt.write(GroceriesN)
            UploadGroceriesInformationtxt.write("#")                                                        #(#) added to split the text
            UploadGroceriesInformationtxt.write(GroceriesED)
            UploadGroceriesInformationtxt.write("#RM")                                                      #(#) added to split the text
            UploadGroceriesInformationtxt.write(GroceriesP)
            UploadGroceriesInformationtxt.write("#")                                                        #(#) added to split the text
            UploadGroceriesInformationtxt.write(GroceriesS)
            UploadGroceriesInformationtxt.close()                                                           #Close the text file
            uploaded = True                                                                                 #Booleans used to represent true or false value (uploaded is True then continue to....)
            validAns = False                                                                                #Booleans used to represent true or false value (validAns is False then try....)
            while not validAns:
                UserAns = input("Enter '1' to back to Admin Menu Page.")                                    #Take the input (Enter '1' to back to Admin Menu Page.)
                if UserAns == "1":                                                                          #if allows for conditional execution of a statement (if UserAns equality to 1)
                    AdminMenu()                                                                             #Direct to AdminMenu
                    break                                                                                   #Break is for a loop control statement
                else:                                                                                       #else used in condition statement (else (xxxx) then it will continue to (xxxx))
                    print("Invalid Input.")                                                                 #Display text (Invalid Input.)





#VIEW UPLOADED GROCERIES
def AdminViewAllGroceries():                                                                                #Define a function (AdminViewAllGroceries)
    ViewAllGroceriestxt = open("Gro_Fruits.txt","r")                                                        #Gro_Fruits.txt is a text file and open with read mode
    ViewAllGroceriestxt = (ViewAllGroceriestxt.readlines())                                                 #Read Gro_Fruits.txt line by lines in text file
    for text in ViewAllGroceriestxt:                                                                        #For loop is used for iterating over a sequence (for text in ViewAllGroceriestxt)
        print(text)                                                                                         #Display text (text)
    ViewAllGroceriestxt = open("Gro_Ingredient.txt","r")                                                    #Gro_Ingredient.txt is a text file and open with read mode
    ViewAllGroceriestxt = (ViewAllGroceriestxt.readlines())                                                 #Read Gro_Ingredient.txt line by lines in text file
    for text in ViewAllGroceriestxt:                                                                        #For loop is used for iterating over a sequence (for text in ViewAllGroceriestxt)
        print(text)                                                                                         #Display text (text)
    ViewAllGroceriestxt = open("Gro_Vegetable.txt","r")                                                     #Gro_vegetable.txt is a text file and open with read mode
    ViewAllGroceriestxt = (ViewAllGroceriestxt.readlines())                                                 #Read Gro_Vegetable.txt line by lines in text file
    for text in ViewAllGroceriestxt:                                                                        #For loop is used for iterating over a sequence (for text in ViewAllGroceriestxt)
        print(text)                                                                                         #Display text (text)

    validAns = False                                                                                        #Booleans used to represent true or false value ( validAns is False then try.... )
    while not validAns:                                                                                     #While not loop repeatedly executes the body of the loop until the condition for loop termination is met (while not validAns)
        UserAns = input("Enter '1' to back to Admin Menu Page.")                                            #Take the input (Enter '1' to back to Admin Menu Page.)
        if UserAns == "1":                                                                                  #if allows for conditional execution of a statement (UserAns equality to 1)
            AdminMenu()                                                                                     #Direct to AdminMenu
            break                                                                                           #Break is for a loop control statement
        else:                                                                                               #else used in condition statement (else (xxxx) then it will continue to (xxxx))
            print("Invalid Input!")                                                                         #Display text (Invalid Input!)





#UPDATE/MODIFY GROCERIES INFO
def ModifyOrUpdateGroceriesInformation():                                                                   #Define a function (ModifyOrUpdateGroceriesInforamtion)
    SearchValid = False                                                                                     #Booleans used to represent true or false value (SearchValid is False then try....)
    Categories = input("Enter the name of categories: \n (Click enter to back to Admin Menu Page.)\n")      #Take the input (Enter the name of categories: Click enter to back to Admin Menu Page.)
    if Categories == '':                                                                                    #if allows for conditional execution of a statement (if categories equality to blank)
        AdminMenu()                                                                                         #Direct to AdminMenu
    elif Categories == ("Vegetable"):                                                                       #elif used in condition statement (elif categories equality to Vegetable)
        Vegetable = open("Gro_Vegetable.txt","r")                                                           #Gro_Vegetable.txt is a text file and open with read mode
        GroceriesDetail = Vegetable.readlines()                                                             #Read Gro_Vegetable.txt line by lines in text file
        Vegetable2 = open("Gro_Vegetable.txt","r")                                                          #Gro_Vegetable.txt is a text file and open with read mode
        GroceriesDetail2 = Vegetable2.read()                                                                #Read Gro_Vegetable.txt line by lines in text file
        SearchValid = True                                                                                  #Booleans used to represent true or false value (SearchValid is True then continue to....)
        
    elif Categories == ("Fruits"):                                                                          #elif used in condition statement (elif categories equality to Fruits)
        Fruits = open("Gro_Fruits.txt","r")                                                                 #Gro_Fruits.txt is a text file and open with read mode
        GroceriesDetail = Fruits.readlines()                                                                #Read Gro_Fruits.txt line by lines in text file
        Fruits2 = open("Gro_Fruits.txt","r")                                                                #Gro_Fruits.txt is a text file and open with read mode
        GroceriesDetail2 = Fruits2.read()                                                                   #Read Gro_Fruits.txt line by lines in text file
        SearchValid = True                                                                                  #Booleans used to represent true or false value (SearchValid is True then continue to....)
        
    elif Categories == ("Ingredient"):                                                                      #elif used in condition statement (elif categories equality to Ingredient)
        Ingredient = open("Gro_Ingredient.txt","r")                                                         #Gro_Ingredient.txt is a text file and open with read mode
        GroceriesDetail = Ingredient.readlines()                                                            #Read Gro_Igredient.txt line by lines in text file
        Ingredient2 = open("Gro_Ingredient.txt","r")                                                        #Gro_Vegetable.txt is a text file and open with read mode
        GroceriesDetail2 = Ingredient2.read()                                                               #Read Gro_Igredient.txt line by lines in text file
        SearchValid = True                                                                                  #Booleans used to represent true or false value (SearchValid is True then continue to....)
        
    else:
        print("Invalid Input!")                                                                             #Display text (Invalid Input!)
        ModifyOrUpdateGroceriesInformation()                                                                #Direct to ModifyOrUpdateGroceriesInformation
        SearchValid = False                                                                                 #Booleans used to represent true or false value (SearchValid is False then try....)

    if SearchValid == True:                                                                                 #Booleans used to represent true or false value (SearchValid is True then continue to....)
        ori = "-"                                                                                           #ori equiality to dash
        update = False                                                                                      #Booleans used to represent true or false value (update is False then try....)
        while not update:                                                                                   #While not loop repeatedly executes the body of the loop until the condition for loop termination is met (while not update)
            GroceriesN = input("Enter the name of grocery that requires to modify:")                        #Take the input (Enter the name of grocery that requires to modify:)
            for information in GroceriesDetail:                                                             #For loop is used for iterating over a sequence (for information in GroceriesDetail)
                if information.startswith(GroceriesN):                                                      #if allows for conditional execution of a statement (if information start with GroceriesN)
                    name, other = information.split("#", 1)                                                 #Splits a string into a list by using (#)
                    if GroceriesN == name.strip():                                                          #if allows for conditional execution of a statement (if CroceriesN equality to name.strip)
                        ori = information                                                                   
            if ori != "-":                                                                                  #if allows for conditional execution of a statement (if ori is not dash)
                print("Enter the new grocery information")                                                  #Display text (Enter the new grocery information)
                New_GroceriesED = input("Enter the new expiry date of grocery(dd/mm/yyyy):")                #Take the input (Enter the new expiry date of grocery(dd/mm/yyyy))
                New_GroceriesP = input("Enter the new price of grocery (RM):")                              #Take the input (Enter the new price of grocery (RM):)
                New_GroceriesS = input("Enter the new specification of grocery:")                           #Take the input (Enter the new specification of grocery:)
                new = GroceriesN+" # " +New_GroceriesED+" # RM" +New_GroceriesP +" # " + New_GroceriesS +"\n" 
                EditInformation = GroceriesDetail2.replace(ori, new)

                if Categories == ("Vegetable"):                                                             #if allows for conditional execution of a statement (if Categories equality to Vegetable)
                    Vegetable_write = open("Gro_Vegetable.txt","w")                                         #Gro_Vegetable.txt is a text file and open with write mode
                    Vegetable_write.write(EditInformation)                                                  #write information that are edited 
                    Vegetable_write.close()                                                                 #Close the text file
                    
                elif Categories == ("Fruits"):                                                              #elif used in condition statement (elif categories equality to Fruits)
                    Fruits_write = open("Gro_Fruits.txt","w")                                               #Gro_Fruits.txt is a text file and open with write mode
                    Fruits_write.write(EditInformation)                                                     #write information that are edited 
                    Fruits_write.close()                                                                    #Close the text file
                    
                elif Categories == ("Ingredient"):                                                          #elif used in condition statement (elif categories equality to Ingredient)
                    Ingredient_write = open("Gro_Ingredient.txt","w")                                       #Gro_Ingredient.txt is a text file and open with write mode
                    Ingredient_write.write(EditInformation)                                                 #write information that are edited 
                    Ingredient_write.close()                                                                #Close the text file

                update = True                                                                               #Booleans used to represent true or false value ( update is True then continue to.... )
                print("Grocery Successfully updated.")                                                      #Display text (Grocery Successfully updated.)
                
                validAns = False                                                                            #Booleans used to represent true or false value ( validAns is False then try.... )
                while not validAns:                                                                         #While not loop repeatedly executes the body of the loop until the condition for loop termination is met (while not validAns)
                    UserAns = input("Enter '1' to back to Admin Menu Page.")                                #Take the input (Enter '1' to back to Admin Menu Page.)
                    if UserAns == "1":                                                                      #if allows for conditional execution of a statement (if UserAns equality to 1)
                        AdminMenu()                                                                         #Direct to AdminMenu
                        break                                                                               #Break is for a loop control statement
                    else:                                                                                   #else used in condition statement (else (xxxx) then it will continue to (xxxx))
                        print("Invalid Input!")                                                             #Display text (Invalid Input!)
            else:                                                                                           #else used in condition statement (else (xxxx) then it will continue to (xxxx))
                ModifyOrUpdateGroceriesInformation()                                                        #Direct to ModifyOrUpdateGroceriesInformation





#DELETE GROCERIES INFO
def DeleteGroceriesDetails():                                                                               #Define a function (DeleteGroceriesDetails)
    Categories = input("Enter the name of categories:  \n (Click enter to back to Admin Menu Page.)\n")     #Take the input (Enter the name of categories: Click enter to back to Admin Menu Page.)
    if Categories == "":                                                                                    #if allows for conditional execution of a statement (if Categories equality to blank)
        AdminMenu()                                                                                         #Direct to AdminMenu
        CategoryTrue = False                                                                                #Booleans used to represent true or false value ( CategoryTrue is False then try.... )
     
    elif Categories == ("Vegetable"):                                                                       #elif used in condition statement (elif categories equality to Vegetable)
        Vegetable = open("Gro_Vegetable.txt","r")                                                           #Gro_Vegetable.txt is a text file and open with read mode
        GroceriesDetail = Vegetable.readlines()                                                             #Read Gro_Vegetable.txt line by lines in text file
        CategoryTrue = True                                                                                 #Booleans used to represent true or false value (CategoryTrue is True then continue to....)
        
    elif Categories == ("Fruits"):                                                                          #elif used in condition statement (elif categories equality to Fruits)
        Fruits = open("Gro_Fruits.txt","r")                                                                 #Gro_Fruits.txt is a text file and open with read mode
        GroceriesDetail = Fruits.readlines()                                                                #Read Gro_Fruits.txt line by lines in text file
        CategoryTrue = True                                                                                 #Booleans used to represent true or false value (CategoryTrue is True then continue to....)

        
    elif Categories == ("Ingredient"):                                                                      #elif used in condition statement (elif categories equality to Ingredient)
        Ingredient = open("Gro_Ingredient.txt","r")                                                         #Gro_Ingredient.txt is a text file and open with read mode
        GroceriesDetail = Ingredient.readlines()                                                            #Read Gro_Ingredient.txt line by lines in text file
        CategoryTrue = True                                                                                 #Booleans used to represent true or false value (CategoryTrue is True then continue to....)

    else:                                                                                                   #else used in condition statement (else (xxxx) then it will continue to (xxxx))
        print("Invalid Input!")                                                                             #Display text (Invalid Input!)
        DeleteGroceriesDetails()                                                                            #Direct to DeleteGroceriesDetails
        CategoryTrue = False                                                                                #Booleans used to represent true or false value (CategoryTrue is False then try....)


    WantToDelete = "nothing"
    delete = False                                                                                          #Booleans used to represent true or false value (delete is False then try....)
    if CategoryTrue:                                                                                        #if allows for conditional execution of a statement (if CategoryTrue)
        GroceriesN = input("Enter the name of grocery that requires to delete:")                            #Take the input (Enter the name of grocery that requires to delete.)
        for information in GroceriesDetail:                                                                 #For loop is used for iterating over a sequence (for information in GroceriesDetail)

            if information.startswith(GroceriesN):                                                          #if allows for conditional execution of a statement (if information satrt with GroceriesN)
                name, others = information.split("#", 1)                                                    #Splits a string into a list by using (#)
                if name.strip() == GroceriesN:                                                              #if allows for conditional execution of a statement (if name.strip equality to GroceriesN)
                    WantToDelete = input                                                                    

        if WantToDelete != "nothing":                                                                       #if allows for conditional execution of a statement (if WantToDelete is not nothing)
            validAns = False                                                                                #Booleans used to represent true or false value (validAns is False then try....)
            if Categories == ("Vegetable"):                                                                 #if allows for conditional execution of a statement (if Category equality to Vegetable)
                Vegetable_write = open("Gro_Vegetable.txt","w")                                             #Gro_Vegetable.txt is a text file and open with write mode
                Vegetable_write.write("")                                                                   #Write blank
                Vegetable_write.close()                                                                     #Close the text file
                    
            elif Categories == ("Fruits"):                                                                  #elif used in condition statement (elif categories equality to Fruits)
                Fruits_write = open("Gro_Fruits.txt","w")                                                   #Gro_Vegetable.txt is a text file and open with write mode
                Fruits_write.write("")                                                                      #Write blank
                Fruits_write.close()                                                                        #Close the text file
                    
            elif Categories == ("Ingredient"):                                                              #elif used in condition statement (elif categories equality to Ingredient)
                Ingredient_write = open("Gro_Ingredient.txt","w")                                           #Gro_Vegetable.txt is a text file and open with write mode
                Ingredient_write.write("")                                                                  #Write blank
                Ingredient_write.close()                                                                    #Close the text file
            GroceriesDetail.remove(WantToDelete)                                                            #Remove WantToDelete
            for grocery in GroceriesDetail:                                                                 #For loop is used for iterating over a sequence (for grocery in GroceriesDetail)
                print(grocery)                                                                              #Display text (grocery)
                if Categories == ("Vegetable"):                                                             #if allows for conditional execution of a statement (if Categories equality to Vegetable)
                    Vegetable_write = open("Gro_Vegetable.txt","a")                                         #Gro_Vegetable.txt is a text file and open with append mode
                    Vegetable_write.write(grocery)                                                          #Write grocery 
                    Vegetable_write.close()                                                                 #Close the text file
                    
                elif Categories == ("Fruits"):                                                              #elif used in condition statement (elif categories equality to Fruits)
                    Fruits_write = open("Gro_Fruits.txt","a")                                               #Gro_Fruits.txt is a text file and open with append mode
                    Fruits_write.write(grocery)                                                             #Write grocery
                    Fruits_write.close()                                                                    #Close the text file
                    
                elif Categories == ("Ingredient"):                                                          #elif used in condition statement (elif categories equality to Ingredient)
                    Ingredient_write = open("Gro_Ingredient.txt","a")                                       #Gro_Ingredient.txt is a text file and open with append mode
                    Ingredient_write.write(grocery)                                                         #Write grocery
                    Ingredient_write.close()                                                                #Close the text file

            print("Grocery Successfully deleted.")                                                          #Display text (Grocery Successfully deleted.)
                    
        else:                                                                                               #else used in condition statement (else (xxxx) then it will continue to (xxxx))
            print("Grocery not found.")                                                                     #Display text (Grocery not found.)
            DeleteGroceriesDetails()                                                                        #Direct to DeleteGroceriesDetails
            validAns = True                                                                                 #Booleans used to represent true or false value ( validAns is True then continue to.... )
            
        while not validAns:                                                                                 #While not loop repeatedly executes the body of the loop until the condition for loop termination is met (while not validAns)
            UserAns = input("Enter '1' to back to Admin Menu Page.")                                        #Take the input (Enter '1' to back to Admin Menu Page.)
            if UserAns == "1":                                                                              #if allows for conditional execution of a statement (if UserAns equality to 1)
                AdminMenu()                                                                                 #Direct to AdminMenu
                break                                                                                       #Break is for a loop control statement
            else:                                                                                           #else used in condition statement (else (xxxx) then it will continue to (xxxx))
                print("Invalid Input!")                                                                     #Display text (Invalid Input!)





#SEARCH GROCERIES DETAIL
def SearchGroceriesDetails():                                                                               #Define a function (SearchGroceriesDetails)
    FruitsGD = open("Gro_Fruits.txt","r")                                                                   #Gro_Fruits.txt is a text file and open with read mode
    FruitsGD = (FruitsGD.readlines())                                                                       #Read Gro_Fruits.txt line by lines in text file
    IngredientGD = open("Gro_Ingredient.txt","r")                                                           #Gro_Ingredient.txt is a text file and open with read mode
    IngredientGD = (IngredientGD.readlines())                                                               #Read Gro_Ingredient.txt line by lines in text file
    VegetableGD = open("Gro_Vegetable.txt","r")                                                             #Gro_Vegetable.txt is a text file and open with read mode
    VegetableGD = (VegetableGD.readlines())                                                                 #Read Gro_Vegetable.txt line by lines in text file
    
    EGCategory = input("Enter grocery category: \n (Click enter to back to Admin Menu Page.)\n")            #Take the input (Enter grocery category: Click enter to back to Admin Menu Page.)
    if EGCategory == "":                                                                                    #if allows for conditional execution of a statement (If EGCategory equality to blank)
        AdminMenu()                                                                                         #Direct to AdminMenu
        CategoryTrue = False                                                                                #Booleans used to represent true or false value (CategoryTrue is False then try....)
    elif EGCategory == ("Fruits"):                                                                          #elif used in condition statement (elif EGCategory equality to FruitsGD)
        ViewGroceriesDetailstxt = FruitsGD
        CategoryTrue = True                                                                                 #Booleans used to represent true or false value (CategoryTrue is True then continue to....)
    elif EGCategory == ("Ingredient"):                                                                      #elif used in condition statement (elif EGCategory equality to IngredientGD)
        ViewGroceriesDetailstxt = IngredientGD
        CategoryTrue = True                                                                                 #Booleans used to represent true or false value (CategoryTrue is True then continue to....)
    elif EGCategory == ("Vegetable"):                                                                       #elif used in condition statement (elif EGCategory equality to VegetableGD)
        ViewGroceriesDetailstxt = VegetableGD
        CategoryTrue = True                                                                                 #Booleans used to represent true or false value (CategoryTrue is True then continue to....)
    else:                                                                                                   #else used in condition statement (else (xxxx) then it will continue to (xxxx))
        print("Invalid Input!")                                                                             #Display text (Invalid Input!)
        SearchGroceriesDetails()                                                                            #Direct to SeachGroceriesDetails
        CategoryTrue = False                                                                                #Booleans used to represent true or false value (CategoryTrue is False then try....)
    
    search = False                                                                                          #Booleans used to represent true or false value (search is False then try....)
    if CategoryTrue:                                                                                        #if allows for conditional execution of a statement (if CategoryTrue)
        EGName = input("Enter grocery name:")                                                               #Take the input (Enter grocery name:)
            
        for information in ViewGroceriesDetailstxt:                                                         #For loop is used for iterating over a sequence (for information in ViewGroceriesDetailstxt)
            if information.startswith(EGName):                                                              #if allows for conditional execution of a statement (if information start with EGName)
                name, other = information.split("#",1)                                                      #Splits a string into a list by using (#)
                if name.strip() == EGName:                                                                  #if allows for conditional execution of a statement (if name.strip equality to EGName)
                    Name,ExpiryDate,Price,Typeofspecification = information.split("#")                      #Splits a string into a list by using (#)
                    print("Name:",Name)                                                                     #Display text (Name:,Name)
                    print("Expiry Date:",ExpiryDate)                                                        #Display text (Expiry Date:,ExpiryDate)
                    print("Price:",Price)                                                                   #Display text (Price:,Price)
                    print("Type of specification:",Typeofspecification)                                     #Display text (Type of specification:,Typeofspecification)
                    search = True                                                                           #Booleans used to represent true or false value ( search is True then continue to.... )
                    validAns = False                                                                        #Booleans used to represent true or false value ( validAns is False then try.... )
                    while not validAns:                                                                     #While not loop repeatedly executes the body of the loop until the condition for loop termination is met (while not validAns)
                        UserAns = input("Enter '1' to back to Admin Menu Page.")                            #Take the input (Enter '1' to back to Admin Menu Page.)
                        if UserAns == "1":                                                                  #if allows for conditional execution of a statement (if UserAns equality to 1)
                            AdminMenu()                                                                     #Direct to AdminMenu
                            break                                                                           #Break is for a loop control statement
                        else:                                                                               #else used in condition statement (else (xxxx) then it will continue to (xxxx))
                            print("Invalid Input!")                                                         #Display text (Invalid Input!)
                
        if not search:                                                                                      #if not is a logical operator that evaluates to True and False (if not search)
            print("Information not found.")                                                                 #Display text (Information not found.)
            SearchGroceriesDetails()                                                                        #Direct to SearchGroceriesDetails
            




#VIEW CUSTOMER ORDERS
def ViewAllOrders():                                                                                        #Define a function (ViewAllOrders)
    ViewOrdertxt = open("ViewOrder.txt","r")                                                                #ViewOrder.txt is a text file and open with read mode
    ViewOrdertxt = (ViewOrdertxt.readlines())                                                               #Read ViewOrder.txt line by lines in text file
    for CVOrder in ViewOrdertxt:                                                                            #For loop is used for iterating over a sequence (for CVOrder in ViewOrdertxt)
        try:                                                                                                #Try let you test the a block of code for error
            CustomerName,GroceryName,Price,Quantity = CVOrder.split("#")                                    #Splits a string into a list by using (#)
            SplitValid = True                                                                               #Booleans used to represent true or false value ( SplitValid is True then continue to.... )
        except:                                                                                             #Except block handle the error without red code
            pass                                                                                            #Pass statement is used as a placeholder for future code
        if SplitValid:                                                                                      #if allows for conditional execution of a statement (if SplitValid)
            CustomerName = CustomerName.strip()                                                             #Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters
            GroceryName = GroceryName.strip()                                                               #Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters
            Price = Price.strip()                                                                           #Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters
            Quantity = Quantity.strip()                                                                     #Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters
            print("Customer Name:",CustomerName)                                                            #Display text (Customer Name:,CustomerName)
            print("Grocery Name:",GroceryName)                                                              #Display text (Grocery Name:,GroceryName)
            print("Price:",Price)                                                                           #Display text (Price:,Price)
            print("Quantity:",Quantity)                                                                     #Display text (Quantity:,Quantity)

    validAns = False                                                                                        #Booleans used to represent true or false value ( validAns is False then try.... )
    while not validAns:                                                                                     #While not loop repeatedly executes the body of the loop until the condition for loop termination is met (while not validAns)
        UserAns = input("Enter '1' to back to Admin Menu Page.")                                            #Take the input (Enter '1' to back to Admin Menu Page.)
        if UserAns == "1":                                                                                  #if allows for conditional execution of a statement (if UserAns equality to 1)
            AdminMenu()                                                                                     #Direct to AdminMenu
            break                                                                                           #Break is for a loop control statement
        else:                                                                                               #else used in condition statement (else (xxxx) then it will continue to (xxxx))
            print("Invalid Input!")                                                                         #Display text (Invalid Input!)
    


        

#SEARCH CUSTOMER ORDER
def SearchOrderForSpecificCustomer():                                                                       #Define a function (SearhOrderForSpecificCustomer)
    SOFSCustomertxt = open("ViewOrder.txt","r")                                                             #ViewOrder.txt is a text file and open with read mode
    SOFSCustomertxt = (SOFSCustomertxt.readlines())                                                         #Read SOFSCCustomertxt line by lines in text file
    SOFSC = False                                                                                           #Booleans used to represent true or false value ( SOFSC is False then try.... )
    Username = input("Enter the username of customer order that you requires: \n (Click enter to back to Admin Menu Page.)\n") #Take the input (Enter the username of customer order that you requires: Click enter to back to Admin Menu Page.)
    if Username == '':                                                                                      #if allows for conditional execution of a statement (if Username equality to blank)
        AdminMenu()                                                                                         #Direct to AdminMenu
    for SOFSCustomer in SOFSCustomertxt:                                                                    #For loop is used for iterating over a sequence (for SOFSCustomer in SOFSCustomertxt)
        if SOFSCustomer.startswith(Username):                                                               #if allows for conditional execution of a statement (if SOFSCustomer start with Username)
            CustomerName,GroceryName,Price,Quantity = SOFSCustomer.split("#")                               #Splits a string into a list by using (#)
            CustomerName = CustomerName.strip()                                                             #Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters
            GroceryName = GroceryName.strip()                                                               #Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters
            Price = Price.strip()                                                                           #Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters
            Quantity = Quantity.strip()                                                                     #Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters
            print("Customer Name:",CustomerName)                                                            #Display text (Customer Name:,CustomerName)
            print("Grocery Name:",GroceryName)                                                              #Display text (Grocery Name:,GroceryName)
            print("Price:",Price)                                                                           #Display text (Price:,Price)
            print("Quantity:",Quantity)                                                                     #Display text (Quantity:,Quantity)
            SOFSC = True                                                                                    #Booleans used to represent true or false value ( SOFSC is True then continue to.... )
            validAns = False                                                                                #Booleans used to represent true or false value ( validAns is False then try.... )
            while not validAns:                                                                             #While not loop repeatedly executes the body of the loop until the condition for loop termination is met (while not validAns)
                UserAns = input("Enter '1' to back to Admin Menu Page.")                                    #Take the input (Enter '1' to back to Admin Menu Page.)
                if UserAns == "1":                                                                          #if allows for conditional execution of a statement (if UserAns equality to 1)
                    AdminMenu()                                                                             #Direct to AdminMenu
                    break                                                                                   #Break is for a loop control statement
                else:                                                                                       #else used in condition statement (else (xxxx) then it will continue to (xxxx))
                    print("Invalid Input!")                                                                 #Display text (Invalid Input!)
        else:                                                                                               #else used in condition statement (else (xxxx) then it will continue to (xxxx))
            SOFSC = False                                                                                   #Booleans used to represent true or false value ( SOFSC is False then try.... )
    if not SOFSC:                                                                                           #if not is a logical operator that evaluates to True and False (if not SOFSC)
            print("Customer order doesn't exist")                                                           #Display text (Customer order doesn't exist)
            SearchOrderForSpecificCustomer()                                                                #Direct to SearchOrderForSpecificCustomer




   
# NEW CUSTOMER PAGE
def NewCustomerPage():                                                                                      #Define a function (NewCustomerPage)
    print("Welcome to the New Customer Page\n")                                                             #Display text (Welcome to the New Customer Page)
    print("Select the features below\n")                                                                    #Display text (Select the features below)
    print("\t1.View Groceries Details\n")                                                                   #Display text (1.View Groceries Details)
    print("\t2.Registration\n")                                                                             #Display text (2.Registration)
    print("\t3.Exit\n")                                                                                     #Display text (3.Exit)
    NewValid = False                                                                                        #Booleans used to represent true or false value ( NewValid is False then try.... )
    while not NewValid:                                                                                     #While not loop repeatedly executes the body of the loop until the condition for loop termination is met (while not NewValid)
        user = input("Enter the number command of your choice:\n (Click enter to back to Admin Menu Page.)\n") #Take the input (Enter the number command of your choice: Click enter to back to Admin Menu Page.)
        if user == '':                                                                                      #if allows for conditional execution of a statement (if user equality to blank)
            mainmenu()                                                                                      #Direct to mainmenu
            break                                                                                           #Break is for a loop control statement
        else:                                                                                               #else used in condition statement (else (xxxx) then it will continue to (xxxx))
            try:                                                                                            #Try let you test the a block of code for error
                user = int(user)
                if (user<1) or (user>3):                                                                    #if allows for conditional execution of a statement (if user less then 1 or more then 3)
                    print("Invalid Input!")                                                                 #Display text (Invalid Input!)
                else:                                                                                       #else used in condition statement (else (xxxx) then it will continue to (xxxx))
                    NewValid = True                                                                         #Booleans used to represent true or false value ( Newvalid is True then continue to.... )
                    break                                                                                   #Break is for a loop control statement
            except:                                                                                         #Except block handle the error without red code
                if ValueError:                                                                              #if allows for conditional execution of a statement (if ValueError)
                    print("Invalid Input!")                                                                 #Display text (Invalid Input!)
    if NewValid:                                                                                            #if allows for conditional execution of a statement (if NewValid)
        if (user == 1):                                                                                     #if allows for conditional execution of a statement (if user equality to 1)
            ViewGroceriesDetails()                                                                          #Direct to ViewGroceriesDetails
        elif (user == 2):                                                                                   #elif used in condition statement (elif user equality to 2)
            NewCustomerRegistration()                                                                       #Direct to NewCustomerRegistration
        elif (user == 3):                                                                                   #elif used in condition statement (elif user equality to 3)
            print("Thank you for visiting Fresh Food Groceries Store\n")                                    #Display text (Thank you for visiting Fresh Food Groceries Store)
            print("See You Again!\n")                                                                       #Display text (See You Again!)
            end()                                                                                           #Direct to end

                    




#VIEW GROCERIES DETAIL
def ViewGroceriesDetails():                                                                                 #Define a function (ViewGroceriesDetails)
    ViewGroceriesDetailstxt = open("Gro_Fruits.txt","r")                                                    #Gro_Fruits.txt is a text file and open with read mode
    ViewGroceriesDetailstxt = (ViewGroceriesDetailstxt.readlines())                                         #Read Gro_Fruits.txt line by lines in text file
    for text in ViewGroceriesDetailstxt:                                                                    #For loop is used for iterating over a sequence (for text in ViewGroceriesDetailstxt)
        print(text)                                                                                         #Display text (text)
    ViewGroceriesDetailstxt = open("Gro_Ingredient.txt","r")                                                #Gro_Ingredient.txt is a text file and open with read mode
    ViewGroceriesDetailstxt = (ViewGroceriesDetailstxt.readlines())                                         #Read Gro_Ingredient.txt line by lines in text file
    for text in ViewGroceriesDetailstxt:                                                                    #For loop is used for iterating over a sequence (for text in ViewGroceriesDetailstxt)
        print(text)                                                                                         #Display text (text)
    ViewGroceriesDetailstxt = open("Gro_Vegetable.txt","r")                                                 #Gro_Vegetable.txt is a text file and open with read mode
    ViewGroceriesDetailstxt = (ViewGroceriesDetailstxt.readlines())                                         #Read Gro_Vegetable.txt line by lines in text file
    for text in ViewGroceriesDetailstxt:                                                                    #For loop is used for iterating over a sequence (for text in ViewGroceriesDetailstxt)
        print(text)                                                                                         #Display text (text)
    validAns = False                                                                                        #Booleans used to represent true or false value (validAns is False then try....)
    while not validAns:                                                                                     #While not loop repeatedly executes the body of the loop until the condition for loop termination is met (while not validAns)
        UserAns = input("Enter '1' to back to New Customer Menu Page.")                                     #Take the input (Enter '1' to back to New Customer Menu Page.)
        if UserAns == "1":                                                                                  #if allows for conditional execution of a statement (if UserAns equality to 1)
            NewCustomerPage()                                                                               #Direct to NewCustomerPage
            break                                                                                           #Break is for a loop control statement
        else:                                                                                               #else used in condition statement (else (xxxx) then it will continue to (xxxx))
            print("Invalid Input!")                                                                         #Display text (Invalid Input!)





# NEW CUSTOMER REGISTRATION
def NewCustomerRegistration():                                                                              #Define a function (NewCustomerRegistration)
    NewCustomerUsernameExist = True                                                                         #Booleans used to represent true or false value (NewCustomerusernamExist is True then continue to....)
    while NewCustomerUsernameExist:                                                                         #While loop is a control flow statement which allows code to be executed repeatedly (while NewCustomerUsernameExist)
        exist = False                                                                                       #Booleans used to represent true or false value (exist is False then try....)
        NewCustomerUsername = input("Enter your username: \n (Click enter to back to New Customer Menu Page.)\n") #Take the input (Enter your username: Click enter to back to Admin Menu Page.)
        if NewCustomerUsername == "":                                                                       #if allows for conditional execution of a statement (if NewCustomerUsername equality to blank)
            NewCustomerPage()                                                                               #Direct to NewCustomerPage
            NewCustomerUsernameExist = False                                                                #Booleans used to represent true or false value (NewCustomerUsernmaExist is False then try....)
            break                                                                                           #Break is for a loop control statement
        CustomerLogin_txt = open("CustomerLogin.txt", "r")                                                  #CustomerLogin.txt is a text file and open with read mode
        CustomerLogin_txt = CustomerLogin_txt.readlines()                                                   #Read CustomerLogin.txt line by lines in text file
        for text in CustomerLogin_txt:                                                                      #For loop is used for iterating over a sequence (for test in CustomerLogin_txt)

            if text.startswith(NewCustomerUsername):                                                        #if allows for conditional execution of a statement (if text start with NewCustomerUsername)
                NCUsername,NCPassword = text.split("#")                                                     #Splits a string into a list by using (#)
                NCUsername = NCUsername.strip()                                                             #Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters
                NCPassword = NCPassword.strip()                                                             #Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters
                if NewCustomerUsername == NCUsername:                                                       #if allows for conditional execution of a statement (if NewCustomerUsername equality to NCUsername)
                    print("Username already exist")                                                         #Display text (Username already exist)
                    exist = True                                                                            #Booleans used to represent true or false value (exist is True then continue to....)
        if not exist:                                                                                       #if not is a logical operator that evaluates to True and False (if not exist)
            NewCustomerUsernameExist = False                                                                #Booleans used to represent true or false value (NewCustomerUsernameExist is False then try....)
            break                                                                                           #Break is for a loop control statement
    if NewCustomerUsername != "":                                                                           #if allows for conditional execution of a statement (if NewCustomerUsername is not blank)
        NewCustomerName = input("Enter your name:")                                                         #Take the input (Enter your name:)
        
        NewCustomerAddress = input("Enter your Address:")                                                   #Take the input (Enter your address:)

        NewCustomerEmailIDExist = True                                                                      #Booleans used to represent true or false value (NewCustomerEmailIDExist is True then continue to....)
        exist = False                                                                                       #Booleans used to represent true or false value (exist is False then try....)
        while NewCustomerEmailIDExist:                                                                      #While loop is a control flow statement which allows code to be executed repeatedly (while NewCustomerEmailIDExist)
            NewCustomerEmailID = input("Enter your Email ID:")                                              #Take the input (Enter your Email ID:)
            RegisteredCustomer_txt = open("PersonalInformation.txt","r")                                    #PersonalInformation.txt is a text file and open with read mode
            RegisteredCustomer_txt = PersonalInformation_txt.readlines()                                    #Read PersonalInformatiom.txt line by lines in text file
            for text in RegisteredCustomer_txt:                                                             #For loop is used for iterating over a sequence (for text in RegisteredCustomer_txt)
                if NewCustomerEmailID in text:                                                              #if allows for conditional execution of a statement (if NewCustomerEmailID is in text)
                    NewCustomerN,NewCustomerA,NewcustomerEID,NewCustomerCN,NewCustomerDOB,NewCustomerG = text.split("#") #Splits a string into a list by using (#)
                    NewCustomerEID = NewcustomerEID.strip()                                                 #Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters
                    if NewCustomerEmailID == NewCustomerEID:                                                #if allows for conditional execution of a statement (if NewCustomerEmailID is equality to NewCustomerEID)
                        print("Email ID already exist")                                                     #Display text (Email ID already exist)
                        exist = True                                                                        #Booleans used to represent true or false value (exist is True then continue to....)
            if not exist:                                                                                   #if not is a logical operator that evaluates to True and False (if not exist)
                NewCustomerEmailIDExist = False                                                             #Booleans used to represent true or false value (NewCustomerEmailIDExist is False then try....)
                break                                                                                       #Break is for a loop control statement
                
        NewCustomerContactNumberExist = True                                                                #Booleans used to represent true or false value (NewCustomerContactNumberExist is True then continue to....)
        exist = False                                                                                       #Booleans used to represent true or false value (exist is False then try....)
        while NewCustomerContactNumberExist:                                                                #While loop is a control flow statement which allows code to be executed repeatedly (while NewCustomerContactNumberExist)
            NewCustomerContactNumber = input("Enter your Contact Number:")                                  #Take the input (Enter your Contact Number:)
            RegisteredCustomer_txt = open("PersonalInformation.txt","r")                                    #PersonalInformation.txt is a text file and open with read mode
            RegisteredCustomer_txt = PersonalInformation_txt.readlines()                                    #Read PersonalInformation.txt line by lines in text file
            for text in RegisteredCustomer_txt:                                                             #For loop is used for iterating over a sequence (for text in RegisteredCustomer_txt)
                if NewCustomerContactNumber in text:                                                        #if allows for conditional execution of a statement (if NewCustomerContactNumber is in text)
                    NewCustomerN,NewCustomerA,NewcustomerEID,NewCustomerCN,NewCustomerDOB,NewCustomerG = text.split("#") #Splits a string into a list by using (#)
                    NewCustomerCN = NewCustomerCN.strip()                                                   #Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters
                    if NewCustomerContactNumber == NewCustomerCN:                                           #if allows for conditional execution of a statement (if NewCustomerContactNumber equality to NewCustomerCN)
                        print("Contact Number already exist")                                               #Display text (Contact Number already exist)
                        exist = True                                                                        #Booleans used to represent true or false value (exist is True then continue to....)
            if not exist:                                                                                   #if not is a logical operator that evaluates to True and False (if not exist)
                NewCustomerContactNumberExist = False                                                       #Booleans used to represent true or false value (NewCustomerContactNumberExist is False then try....)
                break                                                                                       #Break is for a loop control statement

        NewCustomerDateOfBirth = input("Enter your Date Of Birth:")                                         #Take the input (Enter your Date Of Birth:)
        
        NewCustomerGender = input("Enter your Gender:")                                                     #Take the input (Enter your Gender:)
        
        PasswordIncorrect = True                                                                            #Booleans used to represent true or false value (PasswordIncorrect is True then continue to....)
        while PasswordIncorrect:                                                                            #While loop is a control flow statement which allows code to be executed repeatedly (while PasswordIncorrect)
            PasswordNotStrong = True                                                                        #Booleans used to represent true or false value (PasswordNotStrong is True then continue to....)
            while PasswordNotStrong:                                                                        #While loop is a control flow statement which allows code to be executed repeatedly (while PasswordNotStrong)
                NewCustomerPassword = input("Enter your password:")                                         #Take the input (Enter your password:)
                if len(NewCustomerPassword)<8:                                                              #if allows for conditional execution of a statement (if length of NewCustomerPassword is not more then 8 word)
                    print("Password not strong enough. Please enter the password more than 8 words.")       #Display text (Password not strong enough. Please enter the password more than 8 words)
                else:                                                                                       #else used in condition statement (else (xxxx) then it will continue to (xxxx))
                    PasswordNotStrong = False                                                               #Booleans used to represent true or false value (PasswordNotStrong is False then try....)
            NewCustomerConfirmPassword = input("Confirm password:")                                         #Take the input (Confirm password:)
            if NewCustomerConfirmPassword != NewCustomerPassword:                                           #if allows for conditional execution of a statement (if NewCustomerConfirmPassword is not NewCustomerPassword)
                print("Incorrect password. Please try again")                                               #Display text (Incorrect password. Please try again)
            else:                                                                                           #else used in condition statement (else (xxxx) then it will continue to (xxxx))
                PasswordIncorrect = False                                                                   #Booleans used to represent true or false value (PasswordNotStrong is False then try....)
        print("Account Created Successfully. You can now access to Registered Customer Page.")              #Display text (Account Created Successfully. You can now access to Registered Customer Page.)
        
        
        CustomerLogin_txt = open("CustomerLogin.txt", "a")                                                  #CustomerLogin.txt is a text file and open with append mode
        CustomerLogin_txt.write(NewCustomerUsername)                                    
        CustomerLogin_txt.write("#")                                                                        #(#) added to split the text
        CustomerLogin_txt.write(NewCustomerPassword)
        CustomerLogin_txt.write("\n")                                                                       #(\n) added to move to new line
        CustomerLogin_txt.close()                                                                           #Close the text file

        RegisteredCustomer_txt = open("PersonalInformation.txt","a")                                        #PersonalInformation.txt is a text file and open with append mode
        RegisteredCustomer_txt.write(NewCustomerUsername.strip())                                           #Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters
        RegisteredCustomer_txt.write("#")                                                                   #(#) added to split the text                     
        RegisteredCustomer_txt.write(NewCustomerName.strip())                                               #Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters
        RegisteredCustomer_txt.write("#")                                                                   #(#) added to split the text
        RegisteredCustomer_txt.write(NewCustomerAddress)
        RegisteredCustomer_txt.write("#")                                                                   #(#) added to split the text
        RegisteredCustomer_txt.write(NewCustomerEmailID)
        RegisteredCustomer_txt.write("#")                                                                   #(#) added to split the text
        RegisteredCustomer_txt.write(NewCustomerContactNumber)
        RegisteredCustomer_txt.write("#")                                                                   #(#) added to split the text
        RegisteredCustomer_txt.write(NewCustomerDateOfBirth)
        RegisteredCustomer_txt.write("#")                                                                   #(#) added to split the text
        RegisteredCustomer_txt.write(NewCustomerGender)
        RegisteredCustomer_txt.write("\n")                                                                  #(\n) added to move to new line
        RegisteredCustomer_txt.close()                                                                      #Close the text file
        
        CustomerLogin()                                                                                     #Direct to CustomerLogin




    
# REGISTERED CUSTOMER PAGE
def RegisteredCustomerPage(username):                                                                       #Define a function (RegisteredCustomerPage)
    print("Welcome to the Register Customer Page\n")                                                        #Display text (Welcome to the Register Customer Page)
    print("Select the features below\n")                                                                    #Display text (Select the features below)
    print("\t1.View All Groceries Details\n")                                                               #Display text (1.View All Groceries Details)
    print("\t2.Place Order and Payment\n")                                                                  #Display text (2.Place Order and Payment)
    print("\t3.View Order\n")                                                                               #Display text (3.View Order)
    print("\t4.View personal Information\n")                                                                #Display text (4.View personal Information)
    print("\t5.Exit\n")                                                                                     #Display text (5.Exit)

    RegisteredValid = False                                                                                 #Booleans used to represent true or false value ( Registeredvalid is False then try.... )
    while not RegisteredValid:                                                                          #While not loop repeatedly executes the body of the loop until the condition for loop termination is met (while not RegisteredValid)
        try:                                                                                                #Try let you test the a block of code for error
            user = int(input("Enter the number command of your choice:"))                                   #Take the input (Enter the number command of your choice:)
            if (user<1) or (user>5):                                                                        #if allows for conditional execution of a statement (if user more then 1 or user less then 5)
                print("Invalid Input!")                                                                     #Display text (Invalid Input!)
            else:                                                                                           #else used in condition statement (else (xxxx) then it will continue to (xxxx))
                RegisteredValid = True                                                                      #Booleans used to represent true or false value ( Registeredvalid is True then continue to.... )
                break                                                                                       #Break is for a loop control statement
        except:                                                                                             #Except block handle the error without red code
            if ValueError:                                                                                  #if allows for conditional execution of a statement (if ValueError)
                print("Invalid Input!")                                                                     #Display text (Invalid Input!)
                    
    if (user == 1):                                                                                         #if allows for conditional execution of a statement (if UserAns equality to 1)
        ViewAllGroceries(username)                                                                          #Direct to ViewAllGroceries Username
    elif (user == 2):                                                                                       #elif used in condition statement (elif user equality to 2)
        PlaceOrder(username)                                                                                #Direct to PlaceOrder Username
    elif (user == 3):                                                                                       #elif used in condition statement (elif user equality to 3)
        ViewOrder(username)                                                                                 #Direct to ViewOrder Username
    elif (user == 4):                                                                                       #elif used in condition statement (elif user equality to 4)
        ViewPersonalInformation(username)                                                                   #Direct to ViewPersonalInformation Username
    elif (user == 5):                                                                                       #elif used in condition statement (elif user equality to 5)
        print("Thank you for visiting Fresh Food Groceries Store\n")                                        #Display text (Thank you for visiting Fresh Food Groceries Store)
        print("See You Again!\n")                                                                           #Display text (See You Again!)
        end()





# REGISTERED CUSTOMER LOGIN
def CustomerLogin():                                                                                        #Define a function (CustomerLogin)
    print("\nWelcome to Registered Customer Login Page.")                                                   #Display text (Welcome to Registered Customer Login Page.)
    CustomerLogintxt = open("CustomerLogin.txt","r")                                                        #CustomerLogin.txt is a text file and open with read mode
    CustomerLogintxt = (CustomerLogintxt.readlines())                                                       #Read CustomerLogin.txt line by lines in text file
    CustomerU = "-"                                                                                         #CustomerU equals to dash
    CustomerUsername = input("Enter your username: \n (Click enter to back to Main Menu Page.)\n")          #Take the input (Enter your username: Click enter to back to Main Menu Page)
    if CustomerUsername == '':                                                                              #if allows for conditional execution of a statement (if CostumerUsername equality to blank)
        mainmenu()                                                                                          #Direct to mainmenu
        CustomerU = ''                                                                                      #CustomerU equality to blank
    else:                                                                                                   #else used in condition statement (else (xxxx) then it will continue to (xxxx))
        for text in CustomerLogintxt:                                                                       #For loop is used for iterating over a sequence (for text in CustomerLogintxt)
            if text.startswith(CustomerUsername):                                                           #if allows for conditional execution of a statement (if text start with CustomerUsername)
                CustomerU,CustomerP = text.split("#")                                                       #Splits a string into a list by using (#)  
                CustomerU = CustomerU.strip()                                                               #Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters
                CustomerP = CustomerP.strip()                                                               #Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters
                CustomerPassword = input("Enter your password:")                                            #Take the input (Enter your password:)
                if CustomerPassword != CustomerP:                                                           #if allows for conditional execution of a statement (if CustomerPassword is not CustomerP)
                    print("Incorrect password. Please try again")                                           #Display text (Incorrect password. Please try again)
                    CustomerLogin()                                                                         #Direct to CustomerLogin
                    break                                                                                   #Break is for a loop control statement
                else:                                                                                       #else used in condition statement (else (xxxx) then it will continue to (xxxx))
                    print("Login Successful")                                                               #Display text (Login Successful)
                    RegisteredCustomerPage(CustomerUsername)
                    break                                                                                   #Break is for a loop control statement
                    
    if CustomerU == "-":                                                                                    #if allows for conditional execution of a statement (if CustomerU is equality to dash)
        print("Username not found.")                                                                        #Display text (Username not found.)
        CustomerLogin()                                                                                     #Direct to CustomerLogin





#VIEW GROCERIES DETAIL
def ViewAllGroceries(username):                                                                             #Define a function (ViewAllGroceries)
    ViewAllGroceriestxt = open("Gro_Fruits.txt","r")                                                        #Gro_Fruits.txt is a text file and open with read mode
    ViewAllGroceriestxt = (ViewAllGroceriestxt.readlines())                                                 #Read Gro_Fruits.txt line by lines in text file
    for text in ViewAllGroceriestxt:                                                                        #For loop is used for iterating over a sequence (for information in GroceriesDetail)
        print(text)                                                                                         #Display text (text)
    ViewAllGroceriestxt = open("Gro_Ingredient.txt","r")                                                    #Gro_Ingredient.txt is a text file and open with read mode
    ViewAllGroceriestxt = (ViewAllGroceriestxt.readlines())                                                 #Read Gro_Ingredient.txt line by lines in text file
    for text in ViewAllGroceriestxt:                                                                        #For loop is used for iterating over a sequence (for text in ViewAllGroceriestxt)
        print(text)                                                                                         #Display text (text)
    ViewAllGroceriestxt = open("Gro_Vegetable.txt","r")                                                     #Gro_Vegetable.txt is a text file and open with read mode
    ViewAllGroceriestxt = (ViewAllGroceriestxt.readlines())                                                 #Read Gro_Vegetable.txt line by lines in text file
    for text in ViewAllGroceriestxt:                                                                        #For loop is used for iterating over a sequence (for text in ViewAllGroceriestxt)
        print(text)                                                                                         #Display text (text)
    validAns = False                                                                                        #Booleans used to represent true or false value ( validAns is False then try.... )
    while not validAns:                                                                                     #While not loop repeatedly executes the body of the loop until the condition for loop termination is met (while not validAns)
        UserAns = input("Enter '1' to back to Registered Customer Menu Page.")                              #Take the input (Enter '1' to back to New Customer Menu Page.)
        if UserAns == "1":                                                                                  #if allows for conditional execution of a statement (if UserAns equality to 1)
            RegisteredCustomerPage(username)                                                                #Direct to RegisteredCustomerPage
            break                                                                                           #Break is for a loop control statement
        else:                                                                                               #else used in condition statement (else (xxxx) then it will continue to (xxxx))
            print("Invalid Input!")                                                                         #Display text (Invalid Input!)



        

#PLACE ORDER AND PAYMENT
def PlaceOrder(username):                                                                                   #Define a function (PlaceOrder)
    Categories = input("Enter the name of categories: \n (Click enter to back to Registered Customer Menu Page.)\n") #Take the input (Enter the name of categories: Click enter to back to Registered Customer Menu Page.)
    if Categories == "":                                                                                    #if allows for conditional execution of a statement (if Categories equality to blank)
        RegisteredCustomerPage(username)                                                            
    
    elif Categories == ("Vegetable"):                                                                       #elif used in condition statement (elif Categories equality to Vegetable)
        Vegetable = open("Gro_Vegetable.txt","r")                                                           #Gro_Vegetable.txt is a text file and open with read mode
        GroceriesDetail = Vegetable.readlines()                                                             #Read Vegetable line by lines in text file
        CategoryTrue = True                                                                                 #Booleans used to represent true or false value ( CategoryTrue is True then continue to.... )
            
    elif Categories == ("Fruits"):                                                                          #elif used in condition statement (elif Categories equality to Fruits)
        Fruits = open("Gro_Fruits.txt","r")                                                                 #Gro_Fruits.txt is a text file and open with read mode
        GroceriesDetail = Fruits.readlines()                                                                #Read Fruits line by lines in text file
        CategoryTrue = True                                                                                 #Booleans used to represent true or false value ( CategoryTrue is True then continue to.... )
        
    elif Categories == ("Ingredient"):                                                                      #elif used in condition statement (elif Categories equality to Ingredient)
        Ingredient = open("Gro_Ingredient.txt","r")                                                         #Gro_Ingredient.txt is a text file and open with read mode
        GroceriesDetail = Ingredient.readlines()                                                            #Read Ingredient line by lines in text file
        CategoryTrue = True                                                                                 #Booleans used to represent true or false value ( CategoryTrue is True then continue to.... )

    else:                                                                                                   #else used in condition statement (else (xxxx) then it will continue to (xxxx))
        print("Invalid Input!")                                                                             #Display text (Invalid Input!)
        PlaceOrder(username)
        CategoryTrue = False                                                                                #Booleans used to represent true or false value ( CategoryTrue is False then try.... )
        
    search = False                                                                                          #Booleans used to represent true or false value ( search is False then try.... )
    if CategoryTrue:                                                                                        #if allows for conditional execution of a statement (if CategoryTrue equality to False)
        
        EGName = input("Enter grocery name: \n (Click enter to back to Registered Customer Menu Page.)\n")  #Take the input (Enter the name of categories: Click enter to back to Registered Customer Menu Page.)
        if EGName == "":                                                                                    #if allows for conditional execution of a statement (if EGName equality to blank)
            RegisteredCustomerPage(username)
        else:                                                                                               #else used in condition statement (else (xxxx) then it will continue to (xxxx))

            for information in GroceriesDetail:                                                             #For loop is used for iterating over a sequence (for information in GroceriesDetail)
                if information.startswith(EGName):                                                          #if allows for conditional execution of a statement (if information start with EGName)
                    name, other = information.split("#",1)                                                  #Splits a string into a list by using (#)
                    if name.strip() == EGName:                                                              #if allows for conditional execution of a statement (if name.strip is equality with EGName)
                        Name,ExpiryDate,Price,Typeofspecification = information.split("#")                  #Splits a string into a list by using (#)
                        search = True                                                                       #Booleans used to represent true or false value ( search is True then continue to.... )
                        break                                                                               #Break is for a loop control statement
                    
            if not search:                                                                                  #if not is a logical operator that evaluates to True and False (if not search)
                print("Grocery not found.")                                                                 #Display text (Grocery not found.)
                PlaceOrder(username)
                
            else:                                                                                           #else used in condition statement (else (xxxx) then it will continue to (xxxx))
                quantity = input("Please enter the quantity: ")                                             #Take the input (Please enter the quantity:)                                            
                price = str(Price).strip(" RM ")                                                            #string by price.strip 
                total = float(price) * int( quantity)                                                       #float by price times integer of quantity
                total = str(total)                                                                          #string total amount
                try:                                                                                        #Try let you test the a block of code for error
                    num, decimal = total.split(".")                                                         #Splits a string into a list by using (.)
                except:                                                                                     #Except block handle the error without red code
                    pass                                                                                    #Pass statement is used as a placeholder for future code
                if len(decimal) < 2:                                                                        #if allows for conditional execution of a statement (if length of decimal is under 2)
                    decimal = decimal + "0"
                total = num + "." + decimal [:2]
                print("The total payment is RM",total)                                                      #Display text (The total payment is RM,total)
                payment = False                                                                             #Booleans used to represent true or false value ( payment is False then try.... )
                while not payment:                                                                          #While not loop repeatedly executes the body of the loop until the condition for loop termination is met (while not payment)
                    PaymentMethod = input("Please enter '1' if you want to pay with cash. Enter '2' to pay with card: ") #Take the input (Please enter '1' if you want to pay with cash. Enter '2' to pay with card:)
           
                    if PaymentMethod == "1":                                                                #if allows for conditional execution of a statement (if PaymentMethod equality to 1)
                        payment = 0
                        while payment != total:                                                             #While loop is a control flow statement which allows code to be executed repeatedly (while PaymentMethod is equality to 1)
                            payment = input("Enter how much you want to pay: RM")                           #Take the input (Enter how much you want to pay: RM)
                            if payment != total:                                                            #if allows for conditional execution of a statement (if payment equality is not total)
                                print("Payment Unsuccessful. Please pay the exact total price.")            #Display text (Payment Unsuccessful. Please pay the exact total price.)
                            else:                                                                           #else used in condition statement (else (xxxx) then it will continue to (xxxx))
                                break                                                                       #Break is for a loop control statement
                        print("Payment Successful. Amount Paid: RM", total)                                 #Display text (Payment Successful. Amount Paid: RM, total)
                        payment = True                                                                      #Booleans used to represent true or false value ( payment is True then continue to.... )
                        break                                                                               #Break is for a loop control statement
                    elif PaymentMethod == "2":                                                              #elif used in condition statement (elif PaymentMethod equality to 2)
                        print("Payment Successful. Amount Paid: RM", total)                                 #Display text (Payment Successful. Amount Paid: RM, total)
                        payment = True                                                                      #Booleans used to represent true or false value ( payment is True then continue to.... )
                        break                                                                               #Break is for a loop control statement
                    else:                                                                                   #else used in condition statement (else (xxxx) then it will continue to (xxxx))
                        print("Invalid Input!")                                                             #Display text (Invalid Input!)
                    
                ViewOrdertxt = open("ViewOrder.txt","a")                                                    #ViewOrder.txt is a text file and open with append mode
                ViewOrdertxt.write(username)
                ViewOrdertxt.write(" # ")                                                                   #Splits a string into a list by using (#)
                ViewOrdertxt.write( EGName)
                ViewOrdertxt.write(" # RM")                                                                 #Splits a string into a list by using (#)
                ViewOrdertxt.write(str(total))
                ViewOrdertxt.write(" # ")                                                                   #Splits a string into a list by using (#)
                ViewOrdertxt.write(quantity)
                ViewOrdertxt.write("\n")                                                                    #(\n) added to move to new line
                ViewOrdertxt.close()                                                                        #Close the text file
                validAns = False                                                                            #Booleans used to represent true or false value ( validAns is False then try.... )
                while not validAns:                                                                         #While not loop repeatedly executes the body of the loop until the condition for loop termination is met (while not validAns)
                    UserAns = input("Enter '1' to back to Registered Customer Menu Page.")                  #Take the input (Enter '1' to back to Registered Customer Menu Page.)
                    if UserAns == "1":                                                                      #if allows for conditional execution of a statement (if UserAns equality to 1)

                        RegisteredCustomerPage(username)
                        break                                                                               #Break is for a loop control statement
                    else:                                                                                   #else used in condition statement (else (xxxx) then it will continue to (xxxx))
                        print("Invalid Input!")                                                             #Display text (Invalid Input!)




            
#VIEW ORDER
def ViewOrder(Username):                                                                                    #Define a function (ViewOrder)
    ViewOrdertxt = open("ViewOrder.txt","r")                                                                #ViewOrder.txt is a text file and open with read mode
    ViewOrdertxt = (ViewOrdertxt.readlines())                                                               #Read Vieworder.txt line by lines in text file
    View = False                                                                                            #Booleans used to represent true or false value ( View is False then try.... )
    for CVOrder in ViewOrdertxt:                                                                            #For loop is used for iterating over a sequence (for CVOrder in ViewOrdertxt)
        if CVOrder.startswith(Username):                                                                    #if allows for conditional execution of a statement (if CVOrder start with Username)
            CustomerName,GroceryName,Price,Quantity = CVOrder.split("#")                                    #Splits a string into a list by using (#)
            CustomerName = CustomerName.strip()                                                             #Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters
            GroceryName = GroceryName.strip()                                                               #Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters
            Price = Price.strip()                                                                           #Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters
            Quantity = Quantity.strip()                                                                     #Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters
            print("Customer Name:",CustomerName)                                                            #Display text (Customer Name:,CustomerName)
            print("Grocery Name:",GroceryName)                                                              #Display text (Grocery Name:,GroceryName)
            print("Price:",Price)                                                                           #Display text (Price:,Price)
            print("Quantity:",Quantity)                                                                     #Display text (Quantity:,Quantity)
            View = True                                                                                     #Booleans used to represent true or false value ( View is True then continue to.... )
            break                                                                                           #Break is for a loop control statement
        else:                                                                                               #else used in condition statement (else (xxxx) then it will continue to (xxxx))
            View = False                                                                                    #Booleans used to represent true or false value ( View is False then try.... )
    if not View:                                                                                            #if not is a logical operator that evaluates to True and False (if not view)
        print("No Order Purchased")                                                                         #Display text (No Order Purchased)
    validAns = False                                                                                        #Booleans used to represent true or false value ( validAns is False then try.... )
    while not validAns:                                                                                     #While not loop repeatedly executes the body of the loop until the condition for loop termination is met (while not validAns)
        UserAns = input("Enter '1' to back to Registered Customer Menu Page.")                              #Take the input (Enter '1' to back to Registered Customer Menu Page.)
        if UserAns == "1":                                                                                  #if allows for conditional execution of a statement (if UserAns equality to 1)
            RegisteredCustomerPage(Username)
            break                                                                                           #Break is for a loop control statement
        else:                                                                                               #else used in condition statement (else (xxxx) then it will continue to (xxxx))
            print("Invalid Input!")                                                                         #Display text (Invalid Input!)





#VIEW PERSONAL INFORMATION
def ViewPersonalInformation(Username):                                                                      #Define a function (ViewPersonalInformation)
    PersonalInformationtxt = open("PersonalInformation.txt","r")                                            #PersonalInforamtion.txt is a text file and open with read mode
    PersonalInformationtxt = (PersonalInformationtxt.readlines())                                           #Read PersonalInformation.txt line by lines in text file
    Information = False                                                                                     #Booleans used to represent true or false value ( Information is False then try.... )
    for VPInformation in PersonalInformationtxt:                                                            #For loop is used for iterating over a sequence (for VPInformation in PersonalInformationtxt)
        if VPInformation.startswith(Username):                                                              #if allows for conditional execution of a statement (if VPInformation start with Username)
            txtUsername,Name,Address,EmailID,ContactNumber,DateOfBirth,Gender = VPInformation.split("#")    #Close the text file
            if Username.strip() == txtUsername.strip():                                                     #Removes any leading (spaces at the beginning) and trailing (spaces at the end) characters
                print("Name:",Name)                                                                         #Display text (Name:,Name)
                print("Address:",Address)                                                                   #Display text (Address:,Address)
                print("Email ID:",EmailID)                                                                  #Display text (Email ID:,EmailID)
                print("Contact Number:",ContactNumber)                                                      #Display text (Contact Number:,ContactNumber)
                print("Date Of Birth:",DateOfBirth)                                                         #Display text (Date Of Birth:,DateOfBirth)
                print("Gender:",Gender)                                                                     #Display text (Gender:,Gender)
                Information = True                                                                          #Booleans used to represent true or false value ( Information is True then continue to.... )
                break                                                                                       #Break is for a loop control statement

    validAns = False                                                                                        #Booleans used to represent true or false value ( validAns is False then try.... )
    while not validAns:                                                                                     #While not loop repeatedly executes the body of the loop until the condition for loop termination is met (while not validAns)
        UserAns = input("Enter '1' to back to Registered Customer Menu Page.")                              #Take the input (Enter '1' to back to Registered Customer Menu Page.)
        if UserAns == "1":                                                                                  #if allows for conditional execution of a statement (if UserAns equality to 1)
            RegisteredCustomerPage(Username)
            break                                                                                           #Break is for a loop control statement
        else:                                                                                               #else used in condition statement (else (xxxx) then it will continue to (xxxx))
            print("Invalid Input!")                                                                         #Display text (Invalid Input!)

while True:                                                                                                 #While True is a way of running a loop that will continue to run until you explicitly break out of it using break or return
    print("Greetings!")                                                                                     #Display text (Greetings!)
    print("Welcome to Fresh Food Groceries Management System")                                              #Display text (Welcome to Fresh Food Groceries Management System)
    mainmenu()                                                                                              #Direct to mainmenu
    if end() == "End Program":                                                                              #if allows for conditional execution of a statement (if ednf equality to End Program)
        break                                                                                               #Break is for a loop control statement
