print ('Welcome to SCA  Cloud School Application')
print ('Hello, My name is Oluwatimileyin Akinpelu. Here is my simple code written in Python:')
def addition():
    a = 10
    b = 30
    print(a + b)

addition()


def addition():
    a = int(input("Enter a number. "))
    b = int(input("Please enter another number. "))
    print(a + b)


addition()

# *args and **kwargs
def application(fname, lname, Homeaddress, email, *args, **kwargs):
    print("{} {} lives at {}. Her email is {}.".format(fname, lname, Homeaddress, email))


application("Oluwatimileyin", "Akinpelu", "Akute, Ogun state", "oluwatimileyinakinpelu49@gmail.com.",)
print ('Thanks for taking out out time to review this code.')
print('I am eager to receive an acceptance mail.')