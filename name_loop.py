##Jennifer Gotschalk 2020 / Movie Fundraiser

name = ""
count = 0
max_tickets = 150

while name != "xxx" and count < max_tickets:
    print("You have {} seats " "left".format(max_tickets - count))

    name = input("Name: ")
    count += 1
    print()


    age = input("Age: ")
    low_num = 12
    high_num = 130
    def int_check(question, low_num, high_num):
        error = "Please enter a whole number between {} " \
                "and {}".format(low_num, high_num)
        age = int_check("Age: ", 12, 130)
    
        valid = False
        while not valid:
            try:
                response = int(input(question))
                return response
                if low_num < response < high_num:
                    return response
                else:
                    print(error)

            except ValueError:
                print(error)



    
if count == max_tickets:
    print("You have sold all the avaible tickets.")
else:
    print("You have sold {} tickets. \n There are places still avaiable.") 
