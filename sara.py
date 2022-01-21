class restaurant:
    class teacher:
        def _init_(self,email,password,food_items):
            self.te_email=email
            self.te_pass=password
            self.food_items=food_items

        def start(self):
            print("\nSelect one option from the following :")
            print("1.Add new food items \n2.Edit food items \n3.Show food items \n4.Remove food item \n5.Exit\n")
            admin_input=input()
            if admin_input=="1":
                self.add_new_food_item()
            elif admin_input=="2":
                self.edit_food_items()
            elif admin_input=="3":
                self.show_food_items()
            elif admin_input=="4":
                self.remove_food_item()
            elif admin_input=="5":
                exit()
            else:
                print("Please choose correct option")
                self.start()

        def add_new_food_item(self):
            l=[]
            name = input("Type name of the item : \n")
            l.append(name)
            quantity=input("Type quantity of the item\n")
            l.append(quantity)
            price=input("Type price of item\n")
            l.append(price)
            discount=input("Type discount for item\n")
            l.append(discount)
            stock=int(input("Type stock of item\n"))
            l.append(stock)
            self.food_items.append(l)
            print("Item added successfully")
            self.start()    
        
        def edit_food_items(self):
            print("\Choose an item to edit")
            for i in range(len(self.food_items)):
                print(str(i+1),end=". ")
                print(self.food_items[i])
            l=int(input())-1
            print("Selected food item is : ")
            print(self.food_items[l])
            print("Select from the below to edit an item:")
            print("1.Edit name \n2.Edit quantity \n3.Edit price \n4.Edit discount \n5.Edit stock \n6.Go back")
            xx=input()
            if xx=="1":
                self.food_items[l][0]=input("Type name to change: ")
                print("Name successfully changed")
            elif xx=="2":
                self.food_items[l][1]=input("Type quantity to change: ")
                print("Quantity successfully changed")
            elif xx=="3":
                self.food_items[l][2]=input("Type price to change: ")
                print("Price successfully changed")
            elif xx=="4":
                self.food_items[l][3]=input("Type discount to change: ")
                print("Discount successfully changed")
            elif xx=="5":
                self.food_items[l][4]=input("Type stock to change: ")
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
            for i in range(len(self.food_items)):
                print(str(i+1),end=". ")
                print(self.food_items[i])
            l=list(map(int,input().split()))
            print("\nSelected items are: \n")
            x=[]
            for i in range(len(l)):
                print(str(l[i]),end=". ")
                print(self.food_items[l[i]-1])
            print("Type Yes to Confirm and delete the above mentioned items")
            print("Type No to Cancel and go back")
            y=input()
            if y=="Yes":
                for i in l:
                    del self.food_items[i-1]
                print("Food items selected are successfully deleted")
            elif y=="No":
                self.start()
            print()
            self.start()


        def show_food_items(self):
            print("Available food items are: ")
            for i in range(len(self.food_items)):
                print(str(i+1)+". "+self.food_items[i][0]+" ("+self.food_items[i][1]+") "+" ["+self.food_items[i][2]+"] "+
                "Discount: "+self.food_items[i][3]+" Items in stock :"+str(self.food_items[i][4]))
            print()
            
            self.start()

            
            




    class student:
        
        def _init_(self,email,password,full_name,phone,address,food_items,prev_orders):
            self.email = email
            self.password = password
            self.full_name = full_name
            self.phone = phone
            self.address = address
            self.student_data = []
            self.food_items = food_items
            self.prev_orders = prev_orders
        
        def create(self):
            self.student_data.append(self.email)
            self.student_data.append(self.password)
            self.student_data.append(self.full_name)
            self.student_data.append(self.phone)
            self.student_data.append(self.address)
            self.interface()

        def interface(self):
            print("\nChoose any one option from the following :")
            print("1.Place new order \n2.Order History \n3.Update Profile \n4.Exit")
            m=input()
            if m=="1":
                self.order()
            elif m=="2":
                self.history()
            elif m=="3":
                self.profile()
            elif m=="4":
                exit()
            else:
                print("Please choose correct option")
                self.interface()

        def order(self):
            print("\nSelect items from the below list")
            print("Example: For selecting 1st and 2nd items type 1 2")
            for i in range(len(self.food_items)):
                print(str(i+1)+". "+self.food_items[i][0]+" ("+self.food_items[i][1]+") "+" ["+self.food_items[i][2]+"]")
            l=list(map(int,input().split()))
            print("\nSelected items are: \n")
            x=[]
            for i in range(len(l)):
                print(str(l[i])+". "+self.food_items[l[i]-1][0]+" ("+self.food_items[l[i]-1][1]+") "+" ["+self.food_items[l[i]-1][2]+"]")
                x.append(str(l[i])+". "+self.food_items[l[i]-1][0]+" ("+self.food_items[l[i]-1][1]+") "+" ["+self.food_items[l[i]-1][2]+"]")
            print()
            m=0
            for i in range(len(l)):
                if self.food_items[l[i]-1][4]==0:
                        m=1
                        print(self.food_items[l[i]-1][0]+" is out of stock\n")

                        
            if m==1:
                print("Type Change to select other items or Cancel to go back\n")
                zz=input()
                if zz=="Change":
                    self.order()
                elif zz=="Cancel":
                    self.interface()
            print("\nType Yes to confirm your order and No to go back")
            print("Type Change to change your order\n")
            m=input()
            if m=="Yes":
                print("\nOrder confirmed\n")
                self.prev_orders.append(x)
                for i in range(len(l)):
                    self.food_items[l[i]-1][4]-=1
                self.interface()
            elif m=="No":
                self.interface()
            elif m=="Change":
                self.order()

        def history(self):
            print("These are the previous orders:\n")
            if len(self.prev_orders)==0:
                print("No orders placed, to view order history please order an item.\n")
                self.interface()
            else:
                for i in self.prev_orders:
                    print(i)
                self.interface()

        def profile(self):
            print("\nChoose the below options to change data")
            print("1.Email \n2.Password \n3.Full Name \n4.Phone \n5.Address \n6.Change another data \n7.Exit\n" )
            mm=input()
            if mm=="1":
                print("Enter new Email to update: ")
                self.student_data[0]=input()
                print("Email updated successfully")
                self.profile()
            elif mm=="2":
                print("Enter new Password to update: ")
                self.student_data[1]=input()
                print("Password updated successfully")
                self.profile()
            elif mm=="3":
                print("Enter new Full Name to update: ")
                self.student_data[2]=input()
                print("Full Name updated successfully")
                self.profile()
            elif mm=="4":
                print("Enter new Phone to update: ")
                self.student_data[3]=input()
                print("Phone update successfully")
                self.profile()
            elif mm=="5":
                print("Enter new Address to update: ")
                self.student_data[4]=input()
                print("Address update successfully")
                self.profile()
            elif mm=="6":
                self.profile()
            elif mm=="7":
                self.interface()
            else:
                print("Choose correct option")
                self.profile()

            
 

    
        
 
    

    
food_items=[["Tandoori Chicken","4 pieces","INR 240","10% OFF",2],
    ["Vegan Burger","1 piece","INR 320","10% OFF",2],
    ["Truffle Cake","500 gm","INR 900","10% OFF",2]]
while True:
    print("Welcome to Sara Food Delivery App")
    print("\nChoose one option from the following :")
    print("1.teacher login \n2.student Login \n3.Exit\n")
    student_input=input()
    if student_input=="1":
        te_email=input("Enter teacher email: ")
        te_pass= input("Enter teacher password: ")
        print()
        if te_email=="teacher-saradeepika@gmail.com" and te_pass=="sara123":
            t=restaurant.teacher(te_email,te_pass,food_items)
            t.start()
        else:
            print("Enter correct admin details\n")

    elif student_input=="2": 
        full_name=input("Type full name: ")
        phone=input("Type phone number: ")
        email=input("Type email address: ")
        address=input("Type address: ")
        password=input("Type password: ")
        create_student=restaurant.student(email,password,full_name,phone,address,food_items,[])
        create_student.create()
    elif student_input=="3":
        exit()

    else:
        print("Choose correct option from the following")
