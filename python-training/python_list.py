all_contacts={}

class Contact:
    def __init__(self,address,number):
        self.address=address
        self.number=number

    def __str__(self):
        return f"{self.number} ,{self.address}"


class Person:
    def __init__(self,name,emp_id,email,contact_details):
        self.name=name
        self.emp_id=emp_id
        self.email=email   
        for contact in contact_details: 
         if isinstance(contact,Contact):
            if type(contact_details)!=list:
                raise Exception("there is object type error")
            else:
                self.contact_details=contact_details
         else:
            raise Exception("Object not from actual class")

    
    def print_contact_details(self):
       for contact in self.contact_details:
           print(contact)
   


class Employee(Person):
    def __init__(self,name,id,email,contact_details,salary,designation):
        super().__init__(name,id,email,contact_details)
        self.salary=salary
        self.designation=designation



# Function to Check if the contact already exists
isContact=False

def create_contact(address,number,name):
    global isContact
    for key in all_contacts.keys():
        if key==number:
            isContact=True
            break
    if isContact==True:
        print("Error:Contact already exists")
        
    else:
        global contact_obj
        contact_obj=Contact(address,number)
        all_contacts[number]=contact_obj
       
    return contact_obj


def getDetails(name,People):
    for person in People:
        if person.name==name:
            print(f"Person details are = name:{person.name}, emap_id:{person.emp_id}, email:{person.email}")


c1=create_contact("coorg",987647882,"varsha")
c2=create_contact("coorg",887647882,"varsha")
c3=create_contact("banglore",6687647882,"vamshi")
# print(all_contacts)

p1=Person("varsha",12,"varsha@gmail.com",[c1,c2])
p2=Person("vamshi",12,"varsha@gmail.com",[c3])

People=[p1,p2]

# p1.print_contact_details()

getDetails("varsha",People)
