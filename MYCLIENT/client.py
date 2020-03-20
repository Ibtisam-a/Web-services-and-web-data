import http.client
import json
from urllib.parse import urlencode

loop = True
token = ""

while loop:
    print("Rating Professors Application")
    print(" Enter the command you wish to do ")
    print("Register")
    print("Login")
    print("List")
    print("Rating list")
    print("View")
    print("Rate")
    print("Logout")
    connection = http.client.HTTPConnection("127.0.0.1:8000")
    command = input("cmd> ")
    global username

    if command == "Register":
        username = input("Enter the Username: ")
        email = input("Enter The Email: ")
        password = input("Enter the Passwod: ")
        formatted_string = '/app/register?username='+username+'&email='+email+'&password='+password
        print('formatted string', formatted_string)
        connection.request('GET', formatted_string)
        response = connection.getresponse()
        print(response.read().decode())


    elif command == "Login":
        username = input("username: ")
        password = input("password: ")
        formatted_string = '/app/login?username='+username+'&password='+password
        connection.request('GET', formatted_string)
        response = connection.getresponse()
        print(response.read().decode())


    elif command == "List":
        formatted_string = '/app/list?username='+username
        print("formated string --- ", formatted_string)
        connection.request('GET', formatted_string)
        response = connection.getresponse()
        print(response.read().decode())


    elif command == "Rating list":
        formatted_string = '/app/ratinglist?username='+ username
        connection.request('GET',  formatted_string)
        response = connection.getresponse()
        print(response.read().decode())


    elif command == "View":
        pofessor = input("pofessor: ")
        course = input("course: ")
        encoded = urlencode({'username':username, 'pofessor':pofessor, 'course':course})
        formatted = '/app/singlerating?'+encoded
        connection.request('GET',  formatted)
        response = connection.getresponse()
        print(response.read().decode())


    elif command == "Rate":
        pofessor = input("pofessor: ")
        course = input("course: ")
        rating = input("rating: ")
        encoded = urlencode({'username':username, 'pofessor':pofessor, 'course':course, 'rating':rating})
        formatted = '/app/rate?'+encoded
        connection.request('GET',  formatted)
        response = connection.getresponse()
        print(response.read().decode())


    elif command == "Logout":
        formatted_string = f'/{username}/logout'
        connection.request('GET', formatted_string)
        response = connection.getresponse()
        loop = False
        print(response.read().decode())

    else:
        print("command not found")

    connection.close()
