# class Person:
#     def __init__(self, name, age, gender):
#         # Initializing the attributes
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def introduce(self):
#         # Method to introduce the person
#         print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")

# # Create an instance of the Person class
# person1 = Person("Alice", 30, "Female")

# # Call the introduce method
# person1.introduce()

#files

# file=open('me.txt','w')
# file.write('AM GOING TO DO IT IN JESUS NAME')
# file.close


# file=open('me.txt','r')
# content=file.read()
# print(content)
# file.close


#flat file

# file=open('GF.csv','w')
# file.write('GOD IS GOING TO HELP US GET THROUGH ALL THIS')
# file.close


# import csv

# with open('GF.csv','r') as file:
#     reader=csv.reader(file)
#     for row in reader:
#         print(row)
# reader.readlines()      
# 
#   


# file=open('GF7.txt', 'x')
# file.close()

# file=open('GF.csv','w')
# file.writelines(['PRAISE THE LIVING GOD AND ALWAYS BELIEVE IN HIM\n','HE IS ALWAYS TRUE WITH ME THOUGH OUT MY LIFE\n'])
# file.close()

# file=open('GF7.txt','r')
# content=file.read()
# print(content)
# file.close()


#deletin a file
# import os

# file='GF.CSV'

# if os.path.exists(file):
#     os.remove(file)
#     print(f'{file} has been deleted successfully')
# else:
#     print(f'{file} does  not exist')    




#try...except

# import pdb


# pdb.set_trace()
# try:
#     number=int(input('Enter number to divide by 10: '))
#     result= number/10
#     print(f'answer is :{result}')
# except ValueError:
#     print('please enter a valid number')
# except ZeroDivisionError:
#     print('you cant divide by zero')        


# import unittest

# def add(a,b):
#     return a+b

# class TestAdd(unittest.TestCase):
#     def test_add(self):
#         result=add(10,20)
#         self.assertEqual(result,30)


# if __name__ == '__main__':
#     unittest.main()



#file assignment



def create ():
    try:
        with open("GF.txt","w") as file:
            file.write("GOD DID IT ALL THE WAY\n")
            file.write("HE HAS ALWAYS BEEN BY MY SIDE THROUGH OUT")
            print("file 'GF.txt' has been created successfully\n")
    except Exception as e:
        print(f"error occured while creatin the file{e}")


#reading file


def read():
    try:
        with open("GF.txt",'r') as file:
            content= file.read()
            print("\nReading'GF.txt'")
            print(content)

    except FileNotFoundError:
        print("erro:'GF.txt' not found")
    except PermissionError:
        print("erro, permossion denied to access 'GF.tx'")
    except Exception as e:
        print(f"an error occured during file reading{e}")  

#appending a file     


def append():
    try:
        with open("GF.txt","a") as file:
            file.write("GOD ADDED MORE OPPORTUNITIES IN MYLIFE LIKE THIS LINE\n")
            file.write("THANKS BE TO GOD ALWAYS\n")

            print("Data appended to 'GF.txt' successfully")

    except Exception as e:
        print(f"an error occured while appending data :{e}")  




def main():
    try:
        create()
        read()
        append()
        read()

    except  Exception as e:
        print(f"unexpected  errro occured:{e} ")


    finally:
        print("script execution completed successfullly")


if __name__ == "__main__":
    main()                              

