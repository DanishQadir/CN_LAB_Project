import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client_socket.connect(('localhost', 9999))


def get_user_type():
    print("Select user type:")
    print("1. Student")
    print("2. Staff")
    print("3. Faculty")
    choice = input("Enter choice (1/2/3): ")
    if choice == "1":
        return "student"
    elif choice == "2":
        return "staff"
    elif choice == "3":
        return "faculty"
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        return get_user_type()


def get_student_choice():
    print("Select an option:")
    print("1. Cybersecurity Awareness Education")
    print("2. Conduct Quiz")
    print("3. Assessments")
    option = input("Enter choice (1/2/3): ")
    return option


def conduct_quiz():
    score = 0
    for _ in range(5):
        question = client_socket.recv(1024).decode()
        print(question)
        answer = input("Enter your answer (a/b/c): ").strip().lower()
        client_socket.send(answer.encode())
        response = client_socket.recv(1024).decode()
        print(response)
        if "correct" in response:
            score += 1
    print(f"Your final score: {score}/5")
    def receive_education_material():
      material = client_socket.recv(1024).decode()
      print(material)

def receive_education_material():
    education_material = client_socket.recv(1024).decode()
    print(education_material)
def receive_assessment():
    assessment = client_socket.recv(1024).decode()
    print("Assessment from faculty:")
    print(assessment)


def upload_solution(username):
    solution = input("Enter your solution: ")
    client_socket.send(solution.encode())


def upload_material():
    print("Enter the material to upload:")
    material = input()
    client_socket.send(material.encode())
    response = client_socket.recv(1024).decode()
    print(response)


def upload_assignment():
    print("Enter the assignment to upload:")
    assignment = input()
    client_socket.send(assignment.encode())
    response = client_socket.recv(1024).decode()
    print(response)

def read_cybersecurity_rules():
    print("Cybersecurity Rules and Regulations:")
    rules = client_socket.recv(1024).decode()
    print(rules)
user_type = get_user_type()
username = input("Enter username: ")
password = input("Enter password: ")


client_socket.send(user_type.encode())
client_socket.send(username.encode())
client_socket.send(password.encode())


response = client_socket.recv(1024).decode()
print(response)


if user_type == "student" and response == "Login successful!":
    student_choice = get_student_choice()
    client_socket.send(student_choice.encode())
    if student_choice == "1": 
        receive_education_material()

    if student_choice == "2":  
        conduct_quiz()
    if student_choice == "3":
       
        print("Please enter your solution:")
        solution = input()
        
        client_socket.send(solution.encode())
        
        confirmation = client_socket.recv(1024).decode()
        print(confirmation)
if user_type == "staff" and response == "Login successful!":
       print("Select an option:")
       print("1. Upload Material")
       print("2. Upload Assignment")
       option = input("Enter choice (1/2): ")
       client_socket.send(option.encode())
       if option == "1":
        upload_material()
       elif option == "2":
         upload_assignment()
if user_type == "faculty" and response == "Login successful!":
    print("Select an option:")
    print("1. Read Cybersecurity Rules and Regulations")
    option = input("Enter choice (1): ")
    client_socket.send(option.encode())
    if option == "1":
        read_cybersecurity_rules()


client_socket.close()
