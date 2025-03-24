import mysql.connector as my

def connect_to_database():
    return my.connect(host="localhost", user="root", passwd="s", auth_plugin="mysql_native_password", database="f1_racing")

def menu():
    try:
        con = connect_to_database()
        print("*" * 200)
        print("Formula 1 Racing Management".center(200))
        print("*" * 200)
        c = input("Press y to continue: ")
        
        if c == 'y':
            name = input("Enter your Name: ")
            print("Welcome", name, "to the world of F1 racing")
            print("Let's get started")
            
            while True:
                print("*" * 150)
                print("1. Show Race Details")
                if name.lower() == "admin":
                    print("2. Update Race Details")
                print("3. Show participating teams")
                print("4. Show types of seat")
                print("5. Show food menu")
                print("6. Search food item by name")
                if name.lower() == "admin":
                    print("7. Update price of food item")
                    print("8. Add food item detail")
                    print("9. Delete food item from menu")
                print("10. Show type of seat chosen by viewer and its price")
                print("11. If food item ordered then its bill")
                print("12. Check out our season membership for year 2023")
                print("13. Add new participating team")
                print("14. Message from F1 Team")
                print("15. Exit")
                
                opt = int(input("Enter your choice: "))
                
                if opt == 1:
                    show_race_details(con)
                elif opt == 2 and name.lower() == "admin":
                    update_race(con)
                elif opt == 3:
                    participating_teams(con)
                elif opt == 4:
                    seat_type(con)
                elif opt == 5:
                    food_menu(con)
                elif opt == 6:
                    search_food(con)
                elif opt == 7 and name.lower() == "admin":
                    update_food(con)
                elif opt == 8 and name.lower() == "admin":
                    add_food(con)
                elif opt == 9 and name.lower() == "admin":
                    delete_food(con)
                elif opt == 10:
                    seat_reservation()
                elif opt == 11:
                    food_bill()
                elif opt == 12:
                    membership()
                elif opt == 13:
                    add_team(con)
                elif opt == 14:
                    message()
                elif opt == 15:
                    print("Exiting the program...")
                    break
                else:
                    print("---------INVALID OPTION OR UNAUTHORIZED ACCESS----------")
        else:
            print("Exiting the program...")
    
    except my.Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        if 'con' in locals():
            con.close()

def show_race_details(con):
    try:
        c1 = con.cursor()
        c1.execute("SELECT * FROM race_details")
        res = c1.fetchall()
        for i in res:
            print(i)
    except my.Error as e:
        print(f"Error fetching race details: {e}")

def update_race(con):
    try:
        c1 = con.cursor()
        while True:
            a = input("What do you want to update in race details? (Date/Destination/Both): ")
            if a.lower() == "date":
                dst = input("Enter destination of race whose date is to be updated: ")
                dt = input("Enter new date of race: ")
                query = "UPDATE race_details SET Date='{0}' WHERE Destination='{1}'".format(dt, dst)
                c1.execute(query)
                con.commit()
                print("Date of race updated...")
    except my.Error as e:
        print(f"Error updating race details: {e}")

def participating_teams(con):
    try:
        c1 = con.cursor()
        c1.execute("SELECT * FROM participating_teams")
        res = c1.fetchall()
        for i in res:
            print(i)
    except my.Error as e:
        print(f"Error fetching participating teams: {e}")
def Seat_type():
    import mysql.connector as my
    con=my.connect(host="localhost",user="root",passwd="star",auth_plugin="mysql_native_password",database="f1_racing")
    c1=con.cursor()
    c1.execute("Select * from types_of_seat")
    res=c1.fetchall()
    for i in res:
        print(i)
    con.close()



def food_menu():
    import mysql.connector as my
    con=my.connect(host="localhost",user="root",passwd="star",auth_plugin="mysql_native_password",database="f1_racing")
    c1=con.cursor()
    c1.execute("Select * from food")
    res=c1.fetchall()
    for i in res:
        print(i)
    con.close()

def search_food():
    import mysql.connector as my
    con=my.connect(host="localhost",user="root",passwd="star",auth_plugin="mysql_native_password",database="f1_racing")
    c1=con.cursor()
    while True:
        nm=input("Enter food name to search:")
        query="Select * from food where item_name='{}'".format(nm)
        c1.execute(query)
        res=c1.fetchone()
        print(res)
        b=input("Do you want to search more food items?(yes/no):")
        if b=="no":
            break

def update_food():
    import mysql.connector as my
    con=my.connect(host="localhost",user="root",passwd="star",auth_plugin="mysql_native_password",database="f1_racing")
    c1=con.cursor()
    while True:
        nm=input("Enter food item whose price is to be updated:")
        p=int(input("Enter new price:"))
        query="Update food set price={0} where item_name='{1}'".format(p,nm)
        c1.execute(query)
        con.commit()
        print("Price of food item updated...")
        b=input("Do you want to update more food items?(yes/no):")
        if b=="no":
            break


def add_food():
    import mysql.connector as my
    con=my.connect(host="localhost",user="root",passwd="star",auth_plugin="mysql_native_password",database="f1_racing")
    c1=con.cursor()
    L=[]
    S_no=int(input("Enter serial no.:"))
    L.append(S_no)
    item_name=input("Enter name of food item:")
    L.append(item_name)
    price=int(input("Enter price of food item:"))
    L.append(price)
    f=(L)
    sql="insert into food(S_no,item_name,price)values(%s,%s,%s)"
    c1.execute(sql,f)
    con.commit()
    print("Record inserted in food")


def delete_food():
    import mysql.connector as my
    con=my.connect(host="localhost",user="root",passwd="star",auth_plugin="mysql_native_password",database="f1_racing")
    c1=con.cursor()
    while True:
        nm=input("Enter food name which is to be deleted from menu:")
        query="Delete from food where item_name='{}'".format(nm)
        c1.execute(query)
        con.commit()
        print("Food item deleted from menu...")
        b=input("Do you want to delete more food items?(yes/no):")
        if b=="no":
            break



def seat_reservation():
    print("FOLLOWING SEAT TYPES ARE AVAILABLE FOR YOU")
    print("1. General Admission Rs 500 per person")
    print("2. Grandstand Rs 1500 per person")
    print("3. Upper Stands Rs 2500 per person")
    print("4. VIP Box Rs 3500 per person")
    x=int(input("ENTER YOUR CHOICE OF SEAT PLEASE:"))
    n=int(input("ENTER NUMBER OF TICKETS PLEASE:"))
    if(x==1):
        print("You have chosen GENERAL ADMISSION")
        s=500*n
        print("your TOTAL TICKET PRICE is = ",s)
    elif (x==2):
        print("You have chosen GRANDSTAND")
        s=1500*n
        print("your TOTAL TICKET PRICE is = ",s)
    elif (x==3):
        print("You have chosen UPPER STANDS")
        s=2500*n
        print("your TOTAL TICKET PRICE is = ",s)
    elif (x==4):
        print("You have chosen VIP Box")
        s=3500*n
        print("your TOTAL TICKET PRICE is = ",s)
    else:
        print("--------INVALID OPTION-------")
        print("Please choose from option 1,2,3,4")



def food_bill():
    import mysql.connector as my
    con=my.connect(host="localhost",user="root",passwd="star",auth_plugin="mysql_native_password",database="f1_racing")
    c1=con.cursor()
    c1.execute("Select * from food")
    res=c1.fetchall()
    for i in res:
        print(i)
    con.close()
    c=int(input("Order your item number:"))
    d=int(input("Enter quantity:"))
    if(c==1):
        s=25*d
        print("TOTAL FOOD BILL is = ",s)
    elif(c==2):
        s=30*d
        print("TOTAL FOOD BILL is = ",s)
    elif(c==3):
        s=30*d
        print("TOTAL FOOD BILL is = ",s)
    elif(c==4):
        s=40*d
        print("TOTAL FOOD BILL is = ",s)
    elif(c==5):
        s=45*d
        print("TOTAL FOOD BILL is = ",s)
    elif(c==6):
        s=45*d
        print("TOTAL FOOD BILL is = ",s)
    elif(c==7):
        s=40*d
        print("TOTAL FOOD BILL is = ",s)
    elif(c==8):
        s=30*d
        print("TOTAL FOOD BILL is = ",s)
    else:
        print("----------INVALID OPTION---------")
        print("Please choose from mentioned options...")




def membership():
    print("WANT TO SEE WHOLE SEASON THAT TOO FROM VIP BOX?")
    print("THEN TRY OUR NEW SEASON MEMBERSHIP")
    print()
    print("AVAILABLE MEMBERSHIPS FOR THE SEASON")
    print("1. SILVER MEMBERSHIP(WATCH WHOLE RACE FROM NEAREST TO THE TRACK) FOR Rs 10000")
    print("2. GOLD MEMBERSHIP(CHANCE TO INTERACT WITH THE CREW) FOR Rs 15000")
    print("3. PLATINUM MEMBERSHIP(ENJOY ALL THE RACES FROM VIP BOX) FOR Rs 20000")
    a=int(input("ENTER YOUR CHOICE OF MEMBERSHIP:"))
    if(a==1):
        print("you have chosen SILVER MEMBERSHIP")
    elif(a==2):
        print("you have chosen GOLD MEMBERSHIP")
    elif(a==3):
        print("you have chosen PLATINUM MEMBERSHIP")
    else:
        print("----------INVALID OPTION-----------")
        print("Please choose from option 1,2,3")


def add_team():
    import mysql.connector as my
    con=my.connect(host="localhost",user="root",passwd="star",auth_plugin="mysql_native_password",database="f1_racing")
    c1=con.cursor()
    L=[]
    Name=input("ENTER NAME OF TEAM:")
    L.append(Name)
    Name_of_racer=input("ENTER NAME OF RACER:")
    L.append(Name_of_racer)
    Crew_Number=int(input("ENTER CREW NUMBER"))
    L.append(Crew_Number)
    Team_Chief=input("ENTER NAME OF CHIEF")
    L.append(Team_Chief)
    t=(L)
    sql="insert into participating_teams(Name,Name_of_racer,Crew_Number,Team_Chief)values(%s,%s,%s,%s)"
    c1.execute(sql,t)
    con.commit()
    print("Record of NEW TEAM inserted")



def message():
    m='''                IT HAS BEEN A LONG TIME IN THE JOURNEY OF F1 AND A LOT OF PEOPLE HAVE CONNECTED WITH US
                IN THIS LONG PERIOD OF TIME IN THESE MANY YEARS WE HAVE TRIED OUR BEST TO MAKE PEOPLE
                HAPPY AND ALL OF YOU HAVE SHOWN A GREAT RESPECT AND GRATITUDE TO US IN THIS JOURNEY
                WHEN PEOPLE FROM ALL OVER THE WORLD COMES TO CHEER FOR THEIR TEAMS, IT IS A JOY FOR US.
                IT FEELS LIKE WE REALLY HAVE DONE A GREAT JOB, IT IS NOT JUST ABOUT THE RACE IT IS ABOUT
                THE SPIRIT THE ENTHUSIASM AND LOVE. IT IS MORE THAN RACE. IT IS EXCITING TO SEE THE BOND
                ALL PEOPLE SHARE FOR THAT RACE TRACK AND THE CROWD WHICH HELPS TO BOOST THE SPIRIT OF THE
                RACE. WE ARE REALLY GRATEFUL THAT TODAY YOU PEOPLE ARE A PART OF US AND WE HOPE THAT WITH
                MANY MORE YEARS TO COME OUR BOND WILL BE MORE STRONG
                                                                        A WARM MESSAGE FROM F1 TEAM...'''
    print(m)


menu()
