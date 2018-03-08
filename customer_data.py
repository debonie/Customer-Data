import yaml

def choose():
    while True:
        choices = input("Please choose a number: 1. first name 2. last name 3. email >>> ")
        if choices == '1':
            rename = input("Please enter your correct first name? >>> ").lower().strip()
            customer_data['FirstName'] = rename
            with open('customers.yaml', 'w+') as config_file:
                yaml.safe_dump(doc, config_file, default_flow_style=False)
            break
        elif choices == '2':
            renamelast = input("Please enter your correct last name? >>> ").lower().strip()
            customer_data['LastName'] = renamelast
            with open('customers.yaml', 'w+') as config_file:
                yaml.safe_dump(doc, config_file, default_flow_style=False)
            break
        elif choices == '3':
            reemail = input("Please enter your correct email? >>> ").lower().strip()
            customer_data['Email'] = reemail
            with open('customers.yaml', 'w+') as config_file:
                yaml.safe_dump(doc, config_file, default_flow_style=False)
            break
        else:
            print("Please enter a vaild number.")

def change():
    while True:
        update = input("Before you go, is there anything that you need to update?(yes or no) >>> ").lower().strip()
        if update == 'yes':
            choose() 
            break   
        elif update == 'no':
            print("Ok, great!")
            break
        else:
            print("Please enter a valid answer.")    
    
print("Welcome to Dee's Place!")
while True:
    with open('customers.yaml', 'r') as f:
        doc = yaml.load(f)
    customer_data = None
    last_customer_key = 0
    for x in doc:
        key = int(x.lstrip('CustomerInfo'))
        if key > last_customer_key:
            last_customer_key = key
    new_key = last_customer_key + 1
    
    returning_customer = input("Are you a returning customer? (yes or no) >>> ").lower().strip()
    if returning_customer == 'yes':
        name = input("What's your first name so I can look up your loyalty points? >>> ").lower().strip()
        
        for x in doc:
            if doc[x]['FirstName'].lower().strip() == name.lower().strip():
                customer_data = doc[x]       
        
        if customer_data:
            print(f"You have {customer_data['Points']} points.")
            customer_data['Points'] = int(customer_data['Points']) + 50
            
            with open('customers.yaml', 'w+') as config_file:
                yaml.safe_dump(doc, config_file, default_flow_style=False)
            print(f"You now have {customer_data['Points']}.")
            change()
            print("Thank you for stopping by. I hope to see again soon.")
            break
        else:
            print("It seems that we can't find you in our system.")
            signup = input("Would you like to sign up? (yes or no) >>> ").lower().strip()
            if signup == 'yes':
                print("Ok great! Let's get you set up.")
                first_name = input("What is your first name? >>> ").lower().strip()
                last_name = input("What is your last name? >>> ").lower().strip()
                customer_email = input("What is your email? >>> ").lower().strip()
                x.lstrip('CustomerInfo')
                doc['CustomerInfo' + str(new_key)] = {
                    'FirstName': first_name,
                    'LastName': last_name,
                    'Email': customer_email,
                    'Points': '1000' 
                }
                with open('customers.yaml', 'w+') as config_file:
                    yaml.safe_dump(doc, config_file, default_flow_style=False)
                break
            elif signup == 'no':
                print("Thanks for stopping by. Have a great day!")
                break
            else:
                print("Please enter a valid answer.")
                
    elif returning_customer == 'no':
        customer_loyalty = input("Would you like to sign up for our Customer Loyalty Program? (yes or no) >>> ").lower().strip()
        if customer_loyalty == 'yes':
            print("Ok great! Let's get you set up.")
            first_name = input("What is your first name? >>> ").lower().strip()
            last_name = input("What is your last name? >>> ").lower().strip()
            customer_email = input("What is your email? >>> ").lower().strip()
            doc['CustomerInfo' + str(new_key)] = {
                'FirstName': first_name,
                'LastName': last_name,
                'Email': customer_email,
                'Points': '1000'
            }
            with open('customers.yaml', 'w+') as config_file:
                yaml.safe_dump(doc, config_file, default_flow_style=False)
            print("Thank you for signing up with us! We love having you as a customer.")
            print("Please enjoy 1000 loyalty points to start with.")
            print("Thank you for stopping by. We hope to see you soon.")
            break

        elif customer_loyalty == 'no':
            print("Thank you for your time.")
            break