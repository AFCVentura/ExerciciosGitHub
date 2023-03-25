# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

from os import replace


print("S I G N - U P")
user=input("User: ")
password=input("Password: ")

user_up=user.upper()
password_up=password.upper()
while password_up==user_up:
    print("You can't use your user as your password")
    print("Enter a valid password")
    password=input("Password: ")
    password_up=password.upper()
    print()
    
len_password=len(password)
hidden_password=password.replace(password,"*"*len_password)
print()
print()


print(f"User: {user}")
print(f"Password: {hidden_password}")