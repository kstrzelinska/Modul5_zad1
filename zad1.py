#pip install faker
from faker import Faker

# Create a Faker instance for generating random data
fake = Faker('pl_PL')

class BaseContact:
    def __init__(self, name, last_name, phone_personal, email):
        self.name = name
        self.last_name = last_name
        self.phone_personal = phone_personal
        self.email = email

    def contact(self):
        print(f'Wybieram numer {self.phone_personal} i dzwonię do {self.name} {self.last_name}')
    
    @property
    def label_length(self):  
        return len(self.name) + len(self.last_name) + 1  

class BusinessContact(BaseContact):
    def __init__(self, occupation, company_name, phone_business, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.occupation = occupation
        self.company_name = company_name
        self.phone_business = phone_business

    def contact(self):
        print(f'Wybieram numer {self.phone_business} i dzwonię do {self.name} {self.last_name}')

# Function to generate a random person using Faker
def create_random_person(contact_type):
    name = fake.first_name()
    last_name = fake.last_name()
    phone_personal = fake.phone_number()
    email = fake.email()
    if contact_type == "BaseContact":
        return BaseContact(name=name, last_name=last_name, phone_personal=phone_personal, email=email)
    elif contact_type == "BusinessContact":
        occupation = fake.job()
        company_name = fake.company()
        phone_business = fake.phone_number()
        return BusinessContact(name=name, last_name=last_name, phone_personal=phone_personal, email=email, occupation=occupation, company_name=company_name, phone_business=phone_business)

def create_contacts(contact_type, num_contacts):
    people_list = [create_random_person(contact_type) for _ in range(num_contacts)]
    for person in people_list:
        person.contact()
        #print(f'{person.name} {person.last_name}, Długość etykiety: {person.label_length}')        

# Getting input from the user
contact_type = input("Podaj rodzaj wizytówki odpowiednią nazwę: BaseContact lub BusinessContact: ")
i = int(input("Podaj ilość osób: "))

# Creating and displaying the contacts
create_contacts(contact_type, i)