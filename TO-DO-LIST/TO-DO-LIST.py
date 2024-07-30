list = []
num =0
def display():
    for i in list:
        print(i)

def insert():
    global num
    print ("How many task you want to enter")
    answer = int(input())
    for answer in range(answer):
        line = input('>')
        num+=1
        list.append(f"{num}. {line} ")


while True:
        
    print(""" What do you want to do 
        create    - for creating a to do list
        update    - for updating your to do list
        display   - for track/display the to do list
        """)
    answer = input()

    #Creating list..
    if answer.lower() == 'create':
        insert()
        print("List is successfully created")


    #updation of list...
    elif answer.lower() == 'update':
        print("This is the list ")
        display()
        print("What do you want to do insertion/deletion ??")
        if input().lower().startswith('i'):
            insert()
            
        else:
            print("inter the list no to delete")
            index =int(input())
            list.pop(index-1)
        print("List is successfully updated")
        

    elif answer.lower() == 'display':
        display()

    else:
        print("Please enter the right input")

    print("Do you want to continue....")
    if not input().lower().startswith('y'):
        break
    
print("Bye BYe .....")