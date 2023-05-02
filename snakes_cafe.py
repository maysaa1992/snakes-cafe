# refactore it & keep it DRY
Appetizers = ["Wings",'Cookies'," Spring Rolls"]
Entrees = ["Salmon","Steak","Meat Tornado","A Literal Garden"]
Desserts = ["Ice Cream","Cake","Pie"]
Drinks = ["Coffee","Tea","Unicorn Tears"]


def intro():
    print('''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
''')

def user_insertion():
    user_input=input(">")  
    return user_input        

def main():
    user_input = user_insertion()
    obj ={}
    
    while(user_input.lower() != "quit"):
              
        # if user_input.lower() == "quit":
        #     end_application()        
            if user_input in Appetizers:
                if user_input in obj :
                 obj[user_input] +=1
                else :
                    obj[user_input]=1 
                print(obj[user_input],user_input," has been added to your meal")
                
               
            else:
             if user_input in Entrees:
                 if user_input in obj :
                  obj[user_input] =obj[user_input]+1
                 else :
                    obj[user_input]=1 
                 print(obj[user_input],user_input," has been added to your meal")
                
             else:
              if user_input in Desserts:
                 if user_input in obj :
                  obj[user_input] +=1
                 else :
                    obj[user_input]=1 
                 print(obj[user_input],user_input," has been added to your meal")
                 
              else:
               if user_input in Drinks:
                 if user_input in obj :
                  obj[user_input] += 1
                 else :
                    obj[user_input]=1 
                 print(obj[user_input],user_input," has been added to your meal")    
        
               
               
                
            user_input = user_insertion()    
    end_application()


def end_application():
    print("thanks for using snakes cafe application !")          

#invoke the function 

intro()  
main()
