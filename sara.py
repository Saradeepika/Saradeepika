import sys


class Teacher:
    # name quantity price discount stock 
    def _init_(self,email,password,food_data):
        self.te_email=email
        self.te_pass=password
        self.food_data=food_data
        self.start()

    def start(self):
        print("\nSelect one option from the following :")
        print("1.Add new food items \n2.Edit food items \n3.Show food items \n4.Remove food item \n5.Exit\n")
        m=input()
        if m=="1":
            self.add_new_food_item()
        elif m=="2":
            self.edit_food_items()
        elif m=="3":
            self.show_food_items()
        elif m=="4":
            self.remove_food_item()
        elif m=="5":
            sys.exit()
        else:
            print("Please choose correct option")
            self.start()

    def add_new_food_item(self):
        x=[]
        name = input("Enter the name of the food item : \n")
        x.append(name)
        quantity=input("Enter the quantity of the food item...ex : 500 gm, 2 pieces, 1 piece\n")
        x.append(quantity)
        price=input("Enter the price of the food item...ex : INR 200, INR 20\n")
        x.append(price)
        discount=input("Enter the discount for the food item...ex : 10% OFF, 20% OFF\n")
        x.append(discount)
        stock=int(input("Enter the stock of the food item...ex : 5, 2\n"))
        x.append(stock)
        self.food_data.append(x)
        print("Food item added successfully")
        self.start()    
    
    def edit_food_items(self):
        # name quantity price discount stock 
        print("\nSelect a food item to edit")
        for i in range(len(self.food_data)):
            print(str(i+1),end=". ")
            print(self.food_data[i])
        l=int(input())
        print("Selected food item is : ")
        print(self.food_data[l])
        print("Select from the below to edit the selected food item:")
        print("1.Edit name \n2.Edit quantity \n3.Edit price \n4.Edit discount \n5.Edit stock \n6.Go back")
        xx=input()
        if xx=="1":
            self.food_data[l][0]=input("Enter name to change: ")
            print("Name successfully changed")
        elif xx=="2":
            self.food_data[l][1]=input("Enter quantity to change: ")
            print("Quantity successfully changed")
        elif xx=="3":
            self.food_data[l][2]=input("Enter price to change: ")
            print("Price successfully changed")
        elif xx=="4":
            self.food_data[l][3]=input("Enter discount to change: ")
            print("Discount successfully changed")
        elif xx=="5":
            self.food_data[l][4]=input("Enter stock to change: ")
            print("Stock successfully changed")
        elif xx==6:
            self.start()
        else:
            print("Please choose correct option")
            self.edit_food_items()            



        self.start()


    def remove_food_item(self):
        print("\nSelect a food item to remove")
        print("Example: For selecting 1st and 2nd items type 1 2")
        for i in range(len(self.food_data)):
            print(str(i+1)+". "+self.food_data[i])
        l=list(map(int,input().split()))
        print("\nSelected items are: \n")
        x=[]
        for i in range(len(l)):
            print(str(l[i])+". "+self.food_data[l[i]])
        print("Type Yes to Confirm and delete the above mentioned items")
        print("Type No to Cancel and go back")
        y=input()
        if y=="Yes":
            for i in l:
                del self.food_data[i]
            print("Food items selected are successfully deleted")
        elif y=="No":
            self.start()
        print()
        self.start()


    def show_food_items(self):
        print("Available food items are: ")
        for i in range(len(self.food_data)):
            print(str(i+1)+". "+self.food_data[i][0]+" ("+self.food_data[i][1]+") "+" ["+self.food_data[i][2]+"] "+
            "Discount: "+self.food_data[i][3]+" Items in stock :"+str(self.food_data[i][4]))
        print()
        
        self.start()

        
        




class student:
    
    def _init_(self,email,password,full_name,phone,address,food_data,prev_orders):
        self.email = email
        self.password = password
        self.full_name = full_name
        self.phone = phone
        self.address = address
        self.user_data = []
        self.food_data = food_data
        self.prev_orders = prev_orders
    
    def create(self):
        self.student_data.append(self.email)
        self.student_data.append(self.password)
        self.student_data.append(self.full_name)
        self.student_data.append(self.phone)
        self.student_data.append(self.address)
        self.application()

    def application(self):
        print("\nChoose any one option from the following :")
        print("1.Place new order \n2.Order History \n3.Update Profile \n4.Exit")
        m=input()
        if m=="1":
            self.place_order()
        elif m=="2":
            self.order_history()
        elif m=="3":
            self.update_profile()
        elif m=="4":
            sys.exit()
        else:
            print("Please choose correct option")
            self.application()

    def place_order(self):
        print("\nSelect items from the below list")
        print("Example: For selecting 1st and 2nd items type 1 2")
        for i in range(len(self.food_data)):
            print(str(i+1)+". "+self.food_data[i][0]+" ("+self.food_data[i][1]+") "+" ["+self.food_data[i][2]+"]")
        l=list(map(int,input().split()))
        print("\nSelected items are: \n")
        x=[]
        for i in range(len(l)):
            print(str(l[i])+". "+self.food_data[l[i]-1][0]+" ("+self.food_data[l[i]-1][1]+") "+" ["+self.food_data[l[i]-1][2]+"]")
            x.append(str(l[i])+". "+self.food_data[l[i]-1][0]+" ("+self.food_data[l[i]-1][1]+") "+" ["+self.food_data[l[i]-1][2]+"]")
        print()
        m=0
        for i in range(len(l)):
            if self.food_data[l[i]-1][4]==0:
                    m=1
                    print(self.food_data[l[i]-1][0]+" is out of stock\n")

                    
        if m==1:
            print("Type Change to select other items or Cancel to go back\n")
            zz=input()
            if zz=="Change":
                self.place_order()
            elif zz=="Cancel":
                self.application()
        print("\nType Yes to confirm your order and No to go back")
        print("Type Change to change your order\n")
        m=input()
        if m=="Yes":
            print("\nOrder confirmed\n")
            self.prev_orders.append(x)
            for i in range(len(l)):
                self.food_data[l[i]-1][4]-=1
            self.application()
        elif m=="No":
            self.application()
        elif m=="Change":
            self.place_order()

    def order_history(self):
        print("These are the previous orders:\n")
        if len(self.prev_orders)==0:
            print("No orders placed, to view order history please order an item.\n")
            self.application()
        else:
            for i in self.prev_orders:
                print(i)
            self.application()

    def update_profile(self):
        #email password full name phone address
        print("\nChoose the below options to change data")
        print("1.Email \n2.Password \n3.Full Name \n4.Phone \n5.Address \n6.Change another data \n7.Exit\n" )
        mm=input()
        if mm=="1":
            print("Enter new Email to update: ")
            self.student_data[0]=input()
            print("Email updated successfully")
            self.update_profile()
        elif mm=="2":
            print("Enter new Password to update: ")
            self.student_data[1]=input()
            print("Password updated successfully")
            self.update_profile()
        elif mm=="3":
            print("Enter new Full Name to update: ")
            self.student_data[2]=input()
            print("Full Name updated successfully")
            self.update_profile()
        elif mm=="4":
            print("Enter new Phone to update: ")
            self.student_data[3]=input()
            print("Phone update successfully")
            self.update_profile()
        elif mm=="5":
            print("Enter new Address to update: ")
            self.student_data[4]=input()
            print("Address update successfully")
            self.update_profile()
        elif mm=="6":
            self.update_profile()
        elif mm=="7":
            self.application()
        else:
            print("Please choose correct option")
            self.update_profile()

        
 

def take_input(food_data,prev_orders):
    
        student_input=input()
        if student_input=="1": #teacher login
            te_email=input("Enter teacher email: ")
            te_pass= input("Enter teacher password: ")
            print()
            if te_email=="teacher-saradeepika@gmail.com" and te_pass=="sara123":
                teacher_login=teacher(ad_email,ad_pass,food_data)
                teacher_login()
            else:
                print("Please enter correct email and password")
                choose()
    
        elif student_input=="2": #new student
            full_name=input("Enter your full name: ")
            phone=input("Enter your phone number: ")
            email=input("Enter your email address: ")
            address=input("Enter your address: ")
            password=input("Enter your password: ")
            create_student=student(email,password,full_name,phone,address,food_data,prev_orders)
            create_student.create()
        elif student_input=="3":
            sys.exit()

        else:
            print("Please choose correct option")
            choose()
 
    

def choose():
    print("\nChoose any one option from the following :")
    print("1.teacher login \n2.student Login \n3.Exit\n")
    take_input((("Tandoori Chicken","4 pieces","INR 240","10% OFF",2),
    ("Vegan Burger","1 piece","INR 320","10% OFF",2),
    ("Truffle Cake","500 gm","INR 900","10% OFF",2)),[])


print("Welcome to Food Ordering App")
choose()
