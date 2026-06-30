tasks = ["Buy groceries", "Clean room", "Study Python"]

print(tasks)
print(tasks[0])
print(tasks[1])
print(len(tasks))

tasks.append("Walk the dog")
print(tasks)
count = 0
while count < 3:
    print("Loop number:", count)
    count = count + 1

print("Loop finished")
user_choice = "add"

if user_choice == "add":
    print("You chose to add a task.")
elif user_choice == "view":
    print("You chose to view tasks.")
elif user_choice == "quit":
    print("Goodbye!")
else:
    print("I don't understand that choice.")

name = input("What's your name? ")
print("Hello, " + name + "!")