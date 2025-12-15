contacts =[]
while True:
    print("1,Add  a new acontact")
    print("2,Show a new contact")
    print("3,Search  a new contact ")
    print("4.Exit")
    
    choice = input("Enter your choice: ")
    if  choice == "1":
        name =input("Enter name: ")
        phone =input("Enter a phone:")
        new_contact = (name, phone)
        contacts.append(new_contact)
       

    elif choice =="2" :
         for contact in contacts:
             print(contact)
        
    elif choice == "3":
        search = input("Enter name to search: ")
        found = False

        for contact in contacts:
            if contact[0] == search:
                print("Found:", contact)
                found = True

        if not found:
            print("Not found")
       
    elif choice =="4" :
        break
    else:
        print("invalid choice,  ")
           
           


   
  




































