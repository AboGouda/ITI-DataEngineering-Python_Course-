def location():
    for i, c in enumerate("port said"):
     if c == 'i':
        print(i)

###########################################
n = 4
def MARIO (n):
    for i in range(n + 1):
        print(" " *(n-i),"*"*i)
###########################################

def multiblication(x):
    for i in range(1, x + 1):
        for j in range(1, i + 1):
            print(f"{i} * {j} = {i * j}")
##########################################
def vowels(x):
    return sum(1 for i in x if i in "aeiou")

###########################################
def sort_numbers():
    L = [int(input("Enter number: ")) for _ in range(5)]
    print(sorted(L), sorted(L, reverse=True))
#########################################
# def validition(attempts=5):
#     for i in range(attempts):
#         name = input("Your name: ").strip()
        
#         if name.isalpha() and not name.isdigit():
#             email = input("Your Email: ").strip()
            
#             if (
#                 "@" in email and "." in email and
#                 email.find("@") > 0 and
#                 email.find(".") < len(email) - 1 and
#                 email.find("@") < email.find(".") - 1
#             ):
#                 print(f"Your name is: {name} | Your Email is: {email}")
#                 return name, email
#             else:
#                 print("Incorrect email")
#         else:
#             print("Incorrect name")
    
#     print("End of tries")
#     return 
# #########################################################
# def mario_list():
#     L = [" ", " ", " ", " ", " "]
#     for i in range(len(L)):
#         L.pop(0)
#         L.append("*")
#         print(L)
# ##########################################

# def valid_email(email):
#     try: 
#         return (
#         email.count("@") == 1 and
#         "." not in email.split("@")[0] and
#         "." in email.split("@")[1] and
#         "@." not in email
#     )
#     except ValueError:
#         print("Error:Invalid Email")

# def extract_domain(email):
#     try:
#         return email.split("@")[1]
#     except ValueError:
#         print("Erorr:Invalid domain")

# for attempt in range(5):
#     email = input("Enter your email: ")
#     if valid_email(email):
#         print("Valid email! Domain is:", extract_domain(email))
#         break
#     else:
#         print("Invalid email, Please try again.")

# else:
#     raise ValueError("Sekt elslama nta.")
# ####################################
# def log_in():
#     users = [
#         {"name": "ahmed", "pass": "1234"},
#         {"name": "noha", "pass": "5678"}
#     ]

#     username = input("your username: ")

#     for i in users:
#         if i["name"] == username:
#             input_pass = input("Enter Password: ")
#             if i["pass"] == input_pass:
#                 print("Correct Password")
#             else:
#                 print("Incorrect Password")
#             break
#     else:
#         print("The name is not valid")
#          ##################################

         