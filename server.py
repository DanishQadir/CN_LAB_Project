import socket


quiz_questions = [
    "1. What does 'phishing' refer to in the context of cybersecurity?\n a) A fishing technique used by hackers to catch fish\n b) Sending emails pretending to be from reputable sources to trick individuals into revealing personal information, such as passwords and credit card numbers\n c) Fishing for compliments on social media\n",
    "2. What is a strong password?\n a) Password123\n b) A password that is easy to remember\n c) A password that is at least 8 characters long and includes a combination of letters, numbers, and special characters\n",
    "3. What is malware?\n a) A type of fish\n b) Software designed to harm your computer or steal information\n c) Malicious software that helps protect your computer\n",
    "4. What is two-factor authentication (2FA)?\n a) Using two different passwords to log in to your accounts\n b) A security process in which the user provides two different authentication factors to verify themselves\n",
    "5. What is the purpose of antivirus software?\n a) To speed up your computer\n b) To protect your computer from viruses, malware, and other threats\n c) To delete important files\n"
]


correct_answers = ["b", "c", "b", "b", "b"]

cybersecurity_rules = """
1. All faculty members must ensure the security and confidentiality of university data.
2. Faculty members should use strong passwords and avoid sharing them with others.
3. Faculty members are responsible for reporting any cybersecurity incidents promptly.
4. Unauthorized access to university systems or networks is strictly prohibited.
5. Faculty members should participate in cybersecurity training and awareness programs regularly.
"""


def conduct_quiz(client_socket):
    score = 0
    for idx, question in enumerate(quiz_questions):
        client_socket.send(question.encode())
        answer = client_socket.recv(1024).decode().strip().lower()
        if answer == correct_answers[idx]:
            score += 1
        if idx == len(quiz_questions) - 1:
            client_socket.send(f"Your final score: {score}/5".encode())
        else:
            client_socket.send("Next question.".encode())


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_socket.bind(('localhost', 9999))


server_socket.listen(5)

print("Server is listening...")

while True:
  
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address} established.")

    user_type = client_socket.recv(1024).decode()
    username = client_socket.recv(1024).decode()
    password = client_socket.recv(1024).decode()

   
    authenticated = False
    if user_type == "student":
        if username == "student" and password == "studentpass":
            authenticated = True
    elif user_type == "staff":
        if username == "staff" and password == "staffpass":
            authenticated = True
    elif user_type == "faculty":
        if username == "faculty" and password == "facultypass":
            authenticated = True

    if authenticated:
        client_socket.send("Login successful!".encode())
    else:
        client_socket.send("Login failed. Invalid username or password.".encode())
        client_socket.close()
        continue

    
    if user_type == "student":
        option = client_socket.recv(1024).decode()
        if option == "1":
              def read_education_material():
                try:
                 with open("cybersecurity_education_material.txt", "r") as file:
                   education_material = file.read()
                 return education_material
                except FileNotFoundError:
                 return "Error: File not found"
                except Exception as e:
                 return f"Error: {str(e)}"
 

        if option == "2":
            conduct_quiz(client_socket)
          
        if option == "3":
            
            solution = client_socket.recv(1024).decode()
            try:
                with open(f"{username}_solution.txt", "w") as file:
                    file.write(solution)
                client_socket.send("Solution received and saved successfully.".encode())
            except Exception as e:
                print(f"Error occurred while saving solution: {e}")
                client_socket.send("Error occurred while saving solution.".encode())

    elif user_type == "staff" :
        option = client_socket.recv(1024).decode()
        if option == "1":
        
            material = client_socket.recv(1024).decode()
            material_filename = f"{username}_material.txt"
            try:
                with open(material_filename, "w") as file:
                    file.write(material)
                client_socket.send(f"Material saved as {material_filename}".encode())
            except Exception as e:
                print(f"Error occurred while saving material: {e}")
                client_socket.send("Error occurred while saving material.".encode())
        elif option == "2":
         
            assignment = client_socket.recv(1024).decode()
            assignment_filename = f"{username}_assignment.txt"
            try:
                with open(assignment_filename, "w") as file:
                    file.write(assignment)
                client_socket.send(f"Assignment saved as {assignment_filename}".encode())
            except Exception as e:
                print(f"Error occurred while saving assignment: {e}")
                client_socket.send("Error occurred while saving assignment.".encode())
    elif user_type == "faculty":
        option = client_socket.recv(1024).decode()
        if option == "1":
         
            client_socket.send(cybersecurity_rules.encode())

    # Close the connection
    client_socket.close()
