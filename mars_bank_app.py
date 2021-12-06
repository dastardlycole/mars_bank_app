import random
import time
users = {}
transaction_records = {}   
with open("users.txt","r") as file:
    doc = file.read()
    users = eval(doc)       

with open("transactions.txt","r") as file:
    doc = file.read()
    transaction_records = eval(doc)       
def transactions(amount,trans_type,transaction):
    new_dict = {}
    new_dict["amount"] = amount
    new_dict["trans_type"] = trans_type
    new_dict["transaction"] = transaction
    return new_dict
def mars_bank_app():
    for i in range(10):
        print("-"*20)
        print("Welcome to Mars Bank")
        print("-"*20)
        time.sleep(1)
        account_bool = input("Do you have an account with us?(Enter yes or no)\r\n> ").lower()
        time.sleep(1)
        if account_bool == 'no':
            print("Let's sign you up")
            time.sleep(1)
            name = input('Enter your name:\r\n> ').title()
            if all(x.isalpha() or x.isspace() for x in name) and not name.isspace():
                spec_str = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
                special_char = list(spec_str)
                isValid = False
                while not isValid:
                    time.sleep(1)
                    password = input("Enter your password. Password must contain:\r\nat least an integer,\r\na capital letter,\r\na small letter,\r\na special character\r\nand must be more than 8 characters\r\n> ")   
                    time.sleep(1)
                    if len(password) < 8:
                        print("Password length should not be less than 8")
                    elif not any(char.isdigit() for char in password):
                        print("Password should contain at least a number")
                    elif not any(char.islower() for char in password):
                        print("Password should contain at least a lowercase letter")
                    elif not any(char.isupper() for char in password):
                        print("Password should contain at least an uppercase letter")
                    elif not any(char in special_char for char in password):
                        print("Password should contain a special character")
                    else:
                        isValid = True
                trans_pin = input('Create a numerical trans pin:\r\n> ')            
                if trans_pin.isdigit():
                    print("Creating your account. Please wait...")
                    time.sleep(3)
                    account_num_check = 22
                    while account_num_check == 22:
                        account_num = random.randrange(3000000000,3999999999) 
                        if account_num in users.keys():
                            pass 
                        else:
                            account_num_check = 23
                    balance = 0
                    details = {}
                    details['name'] = name
                    details['password'] = password
                    details['trans_pin'] = trans_pin
                    details['balance'] = balance
                    users[account_num] = details
                    transaction_records[account_num] = []
                    print(f"Dear {name}, Please remember the following details... ")
                    time.sleep(1)
                    print(f"Your account number is: {account_num}")
                    time.sleep(1)
                    print(f"Your password is: {password}")
                    time.sleep(1)
                    print(f"Your trans pin is: {trans_pin}")
                    time.sleep(1)
                else:
                    print("Trans pin must be a number")                 
            else:
                print("Name must be letters") 
         
            if i < 9:       
                end_num = 100
            else:
                end_num = 1 
                print("goodbye")
            while end_num == 100:      
                end_session = input("Do you want to end this session:\r\n> ").lower()
                if end_session == 'yes':
                    print("goodbye")
                    end_num= 1
                    return
                elif end_session == 'no':
                    end_num = 1
                else:
                    print("Invalid")                               
        elif account_bool == 'yes':
            print("Let's log you in")
            time.sleep(1)
            login_acct_num = input("Enter your account number:\r\n> ")
            time.sleep(1)
            if login_acct_num.isdigit():
                login_acct_num = int(login_acct_num)
                if login_acct_num in users.keys():
                    login_password = input("Enter your password:\r\n> ")   
                    time.sleep(1)
                    if login_password == users[login_acct_num]['password']:
                        print(f"Login successful. Welcome back {users[login_acct_num]['name']}!")
                        time.sleep(1)
                        actions = input(("Enter 'd' to deposit, 'w' to withdraw, 't' to transfer money, 'c' to check balance, 'e' to edit your details:\r\n> ")).lower()
                        time.sleep(1)
                        if actions == 'd':
                            deposit = input("Enter how much in naira do you want to deposit:\r\n> ")
                            time.sleep(1)
                            if deposit.isdigit():
                                deposit = int(deposit)
                                if deposit > 0:
                                    login_trans_pin = input("Enter your trans pin to confirm:\r\n> ")
                                    time.sleep(1)
                                    if login_trans_pin == users[login_acct_num]['trans_pin']:
                                        users[login_acct_num]['balance'] += deposit
                                        print(f'{deposit} naira succesfully deposited into your account')
                                        transaction_records[login_acct_num].append(transactions(deposit,'Credit','Deposit'))
                                    else:
                                        print("Incorrect pin")                              
                                else:
                                    print("Cannot deposit 0 naira")        
                            else:
                                print("Deposit must be a number")  
                        elif actions == 'w':
                            withdrawal = input("Enter the amount you want to withdraw\r\n> ")        
                            time.sleep(1)
                            if withdrawal.isdigit():
                                withdrawal = int(withdrawal)
                                if withdrawal <= users[login_acct_num]['balance']:
                                    if withdrawal > 0:
                                        login_trans_pin = input("Enter your trans pin to confirm:\r\n> ")
                                        time.sleep(1)
                                        if login_trans_pin == users[login_acct_num]['trans_pin']:
                                            users[login_acct_num]['balance'] -= withdrawal
                                            print(f"{withdrawal} naira successfully withdrawn")
                                            transaction_records[login_acct_num].append(transactions(withdrawal,'Debit','Withdrawal'))
                                        else:
                                            print("Incorrect pin")  
                                    else:
                                        print("Cannot withdraw 0 naira")          
                                else:
                                    print("Insufficient Funds")        
                            else:
                                print("Withdrawal ust be a number")  
                        elif actions == 't':
                            transfer_amount = input("Enter the amount you want to transfer:\r\n> ")
                            if transfer_amount.isdigit():
                                transfer_amount = int(transfer_amount)
                                transfer_to = input("Enter the account number of the recipient:\r\n> ")
                                if transfer_to.isdigit():
                                    transfer_to = int(transfer_to)
                                    if transfer_amount <= users[login_acct_num]['balance']:
                                        if transfer_amount > 0:
                                            if transfer_to in users:
                                                login_trans_pin = input(f"Enter your trans pin to confirm the transfer of {transfer_amount} naira to {users[transfer_to]['name']}:\r\n> ")
                                                if login_trans_pin == users[login_acct_num]['trans_pin']:
                                                    users[transfer_to]['balance'] += transfer_amount
                                                    transaction_records[transfer_to].append(transactions(transfer_amount,'Credit','Transfer'))
                                                    users[login_acct_num]['balance'] -= transfer_amount
                                                    transaction_records[login_acct_num].append(transactions(transfer_amount,'Debit','Transfer'))
                                                    print(f"{transfer_amount} naira successfully transferred to {users[transfer_to]['name']}")
                                                else:
                                                    print("Incorrect pin")    
                                            else:
                                                print("Account number does not exist")       
                                        else:
                                            print("Cannot transfer 0 naira")        
                                    else:
                                        print('Insufficient funds')         
                                else:
                                    print("Account number must be a number")
                            else:
                                print('Transfer must be a number')                
                        elif actions == 'c':
                            login_trans_pin = input("Enter your trans pin to confirm:\r\n> ")
                            time.sleep(1)
                            if login_trans_pin == users[login_acct_num]['trans_pin']:
                                print(f"Your account balance is : {users[login_acct_num]['balance']} naira")
                            else:
                                print("Incorrect pin")   
                        elif actions == 'e':
                            login_trans_pin = input("Enter your trans pin to edit details:\r\n> ")
                            time.sleep(1)
                            if login_trans_pin == users[login_acct_num]['trans_pin']:
                                what_to_edit = input("What do you want to edit? 'n' for name, 'p' for password, 't' for trans pin, 'a' for all\r\n> ")
                                if what_to_edit == 'n':
                                    name = input('Enter your name:\r\n> ').title()   
                                    if all(x.isalpha() or x.isspace() for x in name) and not name.isspace():
                                        users[login_acct_num]['name'] = name  
                                        time.sleep(1)
                                        print(f"Name successfully changed to {users[login_acct_num]['name']}")                                   
                                    else:
                                        print("Name change failed: Name must be letters")        
                                elif what_to_edit =='p':    
                                    isValid = False
                                    while not isValid:
                                        time.sleep(1)
                                        password = input("Enter your password. Password must contain:\r\nat least an integer,\r\na capital letter,\r\na small letter,\r\na special character\r\nand must be more than 8 characters\r\n> ")   
                                        time.sleep(1)
                                        if len(password) < 8:
                                            print("Password length should not be less than 8")
                                        elif not any(char.isdigit() for char in password):
                                            print("Password should contain at least a number")
                                        elif not any(char.islower() for char in password):
                                            print("Password should contain at least a lowercase letter")
                                        elif not any(char.isupper() for char in password):
                                            print("Password should contain at least an uppercase letter")
                                        elif not any(char in special_char for char in password):
                                            print("Password should contain a special character")
                                        else:
                                            isValid = True
                                        users[login_acct_num]['password'] = password    
                                    print(f"Password successfully changed to {users[login_acct_num]['password']}")
                                elif what_to_edit == 't':
                                    trans_pin = input('Create a numerical trans pin:\r\n> ')       
                                    if trans_pin.isdigit():        
                                        users[login_acct_num]['trans_pin'] = trans_pin 
                                        time.sleep(1)
                                        print(f"Trans pin successfully changed to {users[login_acct_num]['trans_pin']}")                          
                                    else:
                                        print("Trans pin change failed: Trans pin must be a number") 
                                elif what_to_edit == 'a':
                                    name = input('Enter your name:\r\n> ').title()   
                                    if all(x.isalpha() or x.isspace() for x in name) and not name.isspace():
                                        users[login_acct_num]['name'] = name  
                                        time.sleep(1)
                                        print(f"Name successfully changed to {users[login_acct_num]['name']}")                                   
                                    else:
                                        print("Name change failed: Name must be letters")
                                    isValid = False
                                    while not isValid:
                                        time.sleep(1)
                                        password = input("Enter your password. Password must contain:\r\nat least an integer,\r\na capital letter,\r\na small letter,\r\na special character\r\nand must be more than 8 characters\r\n> ")   
                                        time.sleep(1)
                                        if len(password) < 8:
                                            print("Password length should not be less than 8")
                                        elif not any(char.isdigit() for char in password):
                                            print("Password should contain at least a number")
                                        elif not any(char.islower() for char in password):
                                            print("Password should contain at least a lowercase letter")
                                        elif not any(char.isupper() for char in password):
                                            print("Password should contain at least an uppercase letter")
                                        elif not any(char in special_char for char in password):
                                            print("Password should contain a special character")
                                        else:
                                            isValid = True
                                        users[login_acct_num]['password'] = password    
                                    print(f"Password successfully changed to {users[login_acct_num]['password']}")
                                    trans_pin = input('Create a numerical trans pin:\r\n> ')       
                                    if trans_pin.isdigit():        
                                        users[login_acct_num]['trans_pin'] = trans_pin 
                                        time.sleep(1)
                                        print(f"Trans pin successfully changed to {users[login_acct_num]['trans_pin']}")                          
                                    else:
                                        print("Trans pin change failed: Trans pin must be a number")        
                                else:
                                    print("Invalid input")                                               
                            else: 
                                print("Incorrect pin")    
                        else:
                            print("Invalid input")   
                    else: 
                        print("Incorrect password")    
                else:
                    print("Invalid account number")    
            else:
                print("Account number must be a number") 
            if i < 9:       
                end_num = 100
            else:
                end_num = 1 
                print("goodbye")
            while end_num == 100:      
                end_session = input("Do you want to end this session:\r\n> ").lower()
                if end_session == 'yes':
                    time.sleep(1)
                    print("goodbye")
                    end_num= 1
                    return
                elif end_session == 'no':
                    end_num = 1
                else:
                    print("Invalid")               
        else:
            print("Invalid input")     
            if i < 9:       
                end_num = 100
            else:
                end_num = 1 
                print("goodbye")
            while end_num == 100:      
                end_session = input("Do you want to end this session:\r\n> ").lower()
                if end_session == 'yes':
                    print("goodbye")
                    end_num= 1
                    return
                elif end_session == 'no':
                    end_num = 1
                else:
                    print("Invalid")           
               
mars_bank_app()
with open("users.txt","w") as file:
    file.write(f"{users}")
with open("transactions.txt","w") as file:
    file.write(f"{transaction_records}")