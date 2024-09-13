from datetime import datetime
import mysql.connector
con = mysql.connector.connect(host =  "localhost" , user = "harshitvyas" , passwd = "12345678" , database = "billing")
cursor = con.cursor()
now = datetime.now()
class administrator():
    
    def groceries(self):
        admin = input("""


                                       1 vagetables:
                                       2 fruits
                                       3 dairyproducts
                                       4 grocers("for all things expect above)

                                    enter the thing you want to add
        
        """)

        match admin:
            case "vegetables":
                
                item = input("enter the vegetable to add")
                id  = input("enter the id ")
                cost = input("enter the cost of vegetable")
                gst = input("enter  the gst ")
                insert = "insert into vegetable(id , item , cost  ,gst) values(%s , %s , %s , %s)"
                add_vegetable = [id , item  ,cost , gst]
                cursor.execute(insert , add_vegetable)

            case "fruits":
                item = input("enter the fruit to add")
                id  = input("enter the id ")
                cost = input("enter the cost of fruit")
                gst = input("enter  the gst ")
                insert = "insert into fruits(id , item , cost  ,gst) values(%s , %s , %s , %s)"
                add_fruit = [id , item  ,cost , gst]
                cursor.execute(insert , add_fruit)

            case "dairyproducts":
                item = input("enter the dairyproducts to add")
                id  = input("enter the id ")
                cost = input("enter the cost of dairyproducts")
                gst = input("enter  the gst ")
                insert = "insert into dairyproducts(id , item , cost  ,gst) values(%s , %s , %s , %s)"
                add_dairyproducts = [id , item  ,cost , gst]
                cursor.execute(insert , add_dairyproducts)


            case "grocers":
                item = input("enter the grocers to add")
                id  = input("enter the id ")
                cost = input("enter the cost of grocers")
                gst = input("enter  the gst ")
                insert = "insert into grocers(id , item , cost  ,gst) values(%s , %s , %s , %s)"
                add_grocers = [id , item  ,cost , gst]
                cursor.execute(insert , add_grocers)

    def clothes(self):
      
                item = input("enter the clothes to add")
                id  = input("enter the id ")
                cost = input("enter the cost of clothes")
                gst = input("enter  the gst ")
                insert = "insert into clothes(id , item , cost  ,gst) values(%s , %s , %s , %s)"
                add_clothes = [id , item  ,cost , gst]
                cursor.execute(insert , add_clothes)
                con.commit()

    def cosmetic(self):
       
                item = input("enter the cosmetic to add")
                id  = input("enter the id ")
                cost - input(f"enter the cost of {item}")
                gst = input("enter  the gst ")
                insert = "insert into cosmetics(id , item , cost  ,gst) values(%s , %s , %s , %s)"
                add_cosmetic = [id , item  ,cost , gst]
                cursor.execute(insert , add_cosmetic)
                con.commit()


    def electric_appliance(self):
       
                item = input("enter the elctric appliance to add")
                id  = input("enter the id ")
                cost - input("enter the cost of electric applian")
                gst = input("enter  the gst ")
                insert = "insert electric_appliance(id , item , cost  ,gst) values(%s , %s , %s , %s)"
                add_electric = [id , item  ,cost , gst]
                cursor.execute(insert , add_electric)


    def food(self):
        
                item = input("enter the foods to add")
                id  = input("enter the id ")
                cost - input("enter the cost of food ")
                gst = input("enter  the gst ")
                insert = "insert into foods(id , item , cost  ,gst) values(%s , %s , %s , %s)"
                add_food = [id , item  ,cost , gst]
                cursor.execute(insert , add_food)


    def toys(self):
                item = input("enter the toy to add")
                id  = input("enter the id ")
                cost - input("enter the cost of toy")
                gst = input("enter  the gst ")
                insert = "insert into toy(id , item , cost  ,gst) values(%s , %s , %s , %s)"
                add_toy = [id , item  ,cost , gst]
                cursor.execute(insert , add_toy)



    def decor(self):
        
                item = input("enter the decor item to add")
                id  = input("enter the id ")
                cost - input("enter the cost of decor  item")
                gst = input("enter  the gst ")
                insert = "insert into decor(id , item , cost  ,gst) values(%s , %s , %s , %s)"
                add_decor = [id , item  ,cost , gst]
                cursor.execute(insert , add_decor)


admin = administrator()


class buyer():
    def products(self):
        customer = input(  """  


                        Welcome to our shop what you want to buy


                                  1    grocery
                                  2    decor
                                  3    clothes
                                  4    cosmetic
                                  5    electric appliance
                                  6    toys
                                  7    food

                              write category you want to buy
        """ ) 

        match customer:
            case "grocery":
                customer_inp = input("""   
                                           enter one thing you wany buy 

                                       1 vagetables:
                                       2 fruits
                                       3 dairyproducts
                                       4 grocers("for all things expect above)

                
                """)

                match customer_inp:
                    case "vegetables":
                        flag = "yes"
                        while(flag == "yes"):
                         cursor.execute("select * from  vegetable")
                         date = now.date()
                         sold_item = []
                         lst_vegetable = []
                         lst_vegetable = cursor.fetchall() 
                         print("id\t\t\titem\t\t\t        cost\t\t\t gst")
                         for i in lst_vegetable:
                             print(i[0],"\t\t\t",i[1],"\t\t\t",i[2],"\t\t\t",i[3])
                         cust_input = int(input("select the item you want to buy write it's id "))
                         for e in lst_vegetable:
                             if(e[0] == cust_input):
                                 sold_item.append(e[0])  
                                 sold_item.append(e[1])  
                                 sold_item.append(e[2])  
                                 sold_item.append(e[3])  
                         
                                      
                         insert = "insert into sales(id , item , cost , gst , date)values(%s , %s , %s , %s  ,%s)"
                         data = [sold_item[0] , sold_item[1] , sold_item[2] , sold_item[3], date]
                         cursor.execute(insert , data)
                         con.commit()
                         del sold_item
                         del lst_vegetable  
                         del data
                         flag = input("you yo want buy more yes or no")

                    case "fruits":
                        flag = "yes"
                        while(flag == "yes"):
                         cursor.execute("select * from  fruits")
                         date = now.date()
                         sold_item = []
                         lst_fruits = []
                         lst_fruits = cursor.fetchall() 
                         print("id\t\t\titem\t\t\t        cost\t\t\t gst")
                         for i in lst_fruits:
                             print(i[0],"\t\t\t",i[1],"\t\t\t",i[2],"\t\t\t",i[3])
                         cust_input = int(input("select the item you want to buy write it's id "))
                         for e in lst_fruits:
                             if(e[0] == cust_input):
                                 sold_item.append(e[0])  
                                 sold_item.append(e[1])  
                                 sold_item.append(e[2])  
                                 sold_item.append(e[3])  
                         
                                      
                         insert = "insert into sales(id , item , cost , gst , date)values(%s , %s , %s , %s  ,%s)"
                         data = [sold_item[0] , sold_item[1] , sold_item[2] , sold_item[3], date]
                         cursor.execute(insert , data)
                         con.commit()
                         del sold_item
                         del lst_fruits
                         del data
                         flag = input("you yo want buy more yes or no")

                    case "dairyproducts":
                        flag = "yes"
                        while(flag == "yes"):
                         cursor.execute("select * from  dairyproduct")
                         date = now.date()
                         sold_item = []
                         lst_dairy = []
                         lst_dairy = cursor.fetchall() 
                         print("id\t\t\titem\t\t\t        cost\t\t\t gst")
                         for i in lst_dairy:
                             print(i[0],"\t\t\t",i[1],"\t\t\t",i[2],"\t\t\t",i[3])
                         cust_input = int(input("select the item you want to buy write it's id "))
                         for e in lst_dairy:
                             if(e[0] == cust_input):
                                 sold_item.append(e[0])  
                                 sold_item.append(e[1])  
                                 sold_item.append(e[2])  
                                 sold_item.append(e[3])  
                         
                                      
                         insert = "insert into sales(id , item , cost , gst , date)values(%s , %s , %s , %s  ,%s)"
                         data = [sold_item[0] , sold_item[1] , sold_item[2] , sold_item[3], date]
                         cursor.execute(insert , data)
                         con.commit()
                         del sold_item
                         del lst_dairy
                         del data
                         flag = input("you yo want buy more yes or no")

                    case "grocers":
                        flag = "yes"
                        while(flag == "yes"):
                         cursor.execute("select * from  grocers")
                         date = now.date()
                         sold_item = []
                         lst_grocers = []
                         lst_grocers = cursor.fetchall() 
                         print("id\t\t\titem\t\t\t        cost\t\t\t gst")
                         for i in lst_grocers:
                             print(i[0],"\t\t\t",i[1],"\t\t\t",i[2],"\t\t\t",i[3])
                         cust_input = int(input("select the item you want to buy write it's id "))
                         for e in lst_grocers:
                             if(e[0] == cust_input):
                                 sold_item.append(e[0])  
                                 sold_item.append(e[1])  
                                 sold_item.append(e[2])  
                                 sold_item.append(e[3])  
                         
                                      
                         insert = "insert into sales(id , item , cost , gst , date)values(%s , %s , %s , %s  ,%s)"
                         data = [sold_item[0] , sold_item[1] , sold_item[2] , sold_item[3], date]
                         cursor.execute(insert , data)
                         con.commit()
                         del sold_item
                         del lst_grocers
                         del data
                         flag = input("you yo want buy more yes or no")


                

                                   



            case "decor":
                        flag = "yes"
                        while(flag == "yes"):
                         cursor.execute("select * from  decor")
                         date = now.date()
                         sold_item = []
                         lst_decor = []
                         lst_decor = cursor.fetchall() 
                         print("id\t\t\titem\t\t\t        cost\t\t\t gst")
                         for i in lst_decor:
                             print(i[0],"\t\t\t",i[1],"\t\t\t",i[2],"\t\t\t",i[3])
                         cust_input = int(input("select the item you want to buy write it's id "))
                         for e in lst_decor:
                             if(e[0] == cust_input):
                                 sold_item.append(e[0])  
                                 sold_item.append(e[1])  
                                 sold_item.append(e[2])  
                                 sold_item.append(e[3])  
                         
                                      
                         insert = "insert into sales(id , item , cost , gst , date)values(%s , %s , %s , %s  ,%s)"
                         data = [sold_item[0] , sold_item[1] , sold_item[2] , sold_item[3], date]
                         cursor.execute(insert , data)
                         con.commit()
                         del sold_item
                         del lst_decor
                         del data
                         flag = input("you yo want buy more yes or no")

            case "clothes":
                        flag = "yes"
                        while(flag == "yes"):
                         cursor.execute("select * from  clothes")
                         date = now.date()
                         sold_item = []
                         lst_clothes = []
                         lst_clothes = cursor.fetchall() 
                         print("id\t\t\titem\t\t\t        cost\t\t\t gst")
                         for i in lst_fruits:
                             print(i[0],"\t\t\t",i[1],"\t\t\t",i[2],"\t\t\t",i[3])
                         cust_input = int(input("select the item you want to buy write it's id "))
                         for e in lst_clothes:
                             if(e[0] == cust_input):
                                 sold_item.append(e[0])  
                                 sold_item.append(e[1])  
                                 sold_item.append(e[2])  
                                 sold_item.append(e[3])  
                         
                                      
                         insert = "insert into sales(id , item , cost , gst , date)values(%s , %s , %s , %s  ,%s)"
                         data = [sold_item[0] , sold_item[1] , sold_item[2] , sold_item[3], date]
                         cursor.execute(insert , data)
                         con.commit()
                         del sold_item
                         del lst_clothes
                         del data
                         flag = input("you yo want buy more yes or no")

            case "cosmetic":
                        flag = "yes"
                        while(flag == "yes"):
                         cursor.execute("select * from  cosmetics")
                         date = now.date()
                         sold_item = []
                         lst_cosmetics = []
                         lst_cosmetics = cursor.fetchall() 
                         print("id\t\t\titem\t\t\t        cost\t\t\t gst")
                         for i in lst_cosmetics:
                             print(i[0],"\t\t\t",i[1],"\t\t\t",i[2],"\t\t\t",i[3])
                         cust_input = int(input("select the item you want to buy write it's id "))
                         for e in lst_fruits:
                             if(e[0] == cust_input):
                                 sold_item.append(e[0])  
                                 sold_item.append(e[1])  
                                 sold_item.append(e[2])  
                                 sold_item.append(e[3])  
                         
                                      
                         insert = "insert into sales(id , item , cost , gst , date)values(%s , %s , %s , %s  ,%s)"
                         data = [sold_item[0] , sold_item[1] , sold_item[2] , sold_item[3], date]
                         cursor.execute(insert , data)
                         con.commit()
                         del sold_item
                         del lst_cosmetics
                         del data
                         flag = input("you yo want buy more yes or no")
               

            case "electric appliance":
                        flag = "yes"
                        while(flag == "yes"):
                         cursor.execute("select * from  electric_appliance")
                         date = now.date()
                         sold_item = []
                         lst_electric_appliance = []
                         lst_ekectric_appliance = cursor.fetchall() 
                         print("id\t\t\titem\t\t\t        cost\t\t\t gst")
                         for i in lst_electric_appliance:
                             print(i[0],"\t\t\t",i[1],"\t\t\t",i[2],"\t\t\t",i[3])
                         cust_input = int(input("select the item you want to buy write it's id "))
                         for e in lst_electric_appliance:
                             if(e[0] == cust_input):
                                 sold_item.append(e[0])  
                                 sold_item.append(e[1])  
                                 sold_item.append(e[2])  
                                 sold_item.append(e[3])  
                         
                                      
                         insert = "insert into sales(id , item , cost , gst , date)values(%s , %s , %s , %s  ,%s)"
                         data = [sold_item[0] , sold_item[1] , sold_item[2] , sold_item[3], date]
                         cursor.execute(insert , data)
                         con.commit()
                         del sold_item
                         del lst_electric_appliance
                         del data
                         flag = input("you yo want buy more yes or no")
                

            case "toys":
                        flag = "yes"
                        while(flag == "yes"):
                         cursor.execute("select * from  toy")
                         date = now.date()
                         sold_item = []
                         lst_toys = []
                         lst_toys = cursor.fetchall() 
                         print("id\t\t\titem\t\t\t        cost\t\t\t gst")
                         for i in lst_toys:
                             print(i[0],"\t\t\t",i[1],"\t\t\t",i[2],"\t\t\t",i[3])
                         cust_input = int(input("select the item you want to buy write it's id "))
                         for e in lst_toys:
                             if(e[0] == cust_input):
                                 sold_item.append(e[0])  
                                 sold_item.append(e[1])  
                                 sold_item.append(e[2])  
                                 sold_item.append(e[3])  
                         
                                      
                         insert = "insert into sales(id , item , cost , gst , date)values(%s , %s , %s , %s  ,%s)"
                         data = [sold_item[0] , sold_item[1] , sold_item[2] , sold_item[3], date]
                         cursor.execute(insert , data)
                         con.commit()
                         del sold_item
                         del lst_toys
                         del data
                         flag = input("you yo want buy more yes or no")

            case "food":
                
                        flag = "yes"
                        while(flag == "yes"):
                         cursor.execute("select * from  food")
                         date = now.date()
                         sold_item = []
                         lst_food = []
                         lst_food = cursor.fetchall() 
                         print("id\t\t\titem\t\t\t        cost\t\t\t gst")
                         for i in lst_food:
                             print(i[0],"\t\t\t",i[1],"\t\t\t",i[2],"\t\t\t",i[3])
                         cust_input = int(input("select the item you want to buy write it's id "))
                         for e in lst_fruits:
                             if(e[0] == cust_input):
                                 sold_item.append(e[0])  
                                 sold_item.append(e[1])  
                                 sold_item.append(e[2])  
                                 sold_item.append(e[3])  
                         
                                      
                         insert = "insert into sales(id , item , cost , gst , date)values(%s , %s , %s , %s  ,%s)"
                         data = [sold_item[0] , sold_item[1] , sold_item[2] , sold_item[3], date]
                         cursor.execute(insert , data)
                         con.commit()
                         del sold_item
                         del lst_food
                         del data
                         flag = input("you yo want buy more yes or no")




buy = buyer()
user_input = input("""


                         1   administrator

                         2   buyer

                         3   exit     
                


                 """)


match user_input:
    case "1":
     #email = input("enter email ")
     #password = input("password")
     #if(email == "harshit11@gmail" and password == "123456"):

        u_input = input("""     enter 
                                   
                                   
                                   add   for add    """)
     
        match u_input:
            case "add":
    

                user_input = input(""" 
                                          enter    1   for        groceries
                                          enter    2   for        clothes
                                          enter    3   for        cosmetics
                                          enter    4   for        electric appliance
                                          enter    5   for        food
                                          enter    6   for        toys
                                          enter    7   for        decor


                """)

                match user_input:

                    case "1":
                        admin.groceries()

                    case "2":
                           admin.clothes()

                    case "3":
                        admin.cosmetic()
                    
                    case "4":
                        admin.electric_appliance()

                    case "5":
                        admin.food()

                    case "6":
                        admin.toys()

                    case "7":
                        admin.decor()



        #this indentation for add and other admin section
     #else:
       # print("wrong email and password")   

    case "2":

        buy.products()

    case "3":
        exit



