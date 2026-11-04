# #creating class
# class Student:
#     name = "Sarang"
#
# #creating object (instance)
#
# s1 = Student()
# print(s1.name)
#
# s2 = Student()
# print(s2.name)
#
# class Car:
#     color = "blue"
#     brand = "Toyota"
#
# car1 = Car()
#
# print(car1.color)
# print(car1.brand)
#
#
# # init function or the constructor
# #def __init__():
#
# class Student2:
#
#         def __init__(self, fullname):
#             self.name = fullname
#             print("adding new student in database")
# s1 = Student2("Sarang")
# print(s1.name)

#we can name the self object with any name not only self
#
# class Student3:
#     college_name = "ABC College" #class attribute
#     name = "anonymous"
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         # print("this is constructor")
#     def hello(self):
#         print("Welcome student", self.name)
#     def get_marks(self):
#         return self.marks
#
#
# s3 = Student3("Sarang",59)
# # print(s3.name, s3.marks)
# s3.hello()
# print(s3.get_marks())
# # s4 = Student3("Sheikh",60)
# # print(s4.name, s4.marks)
# #
# # print(Student3.college_name) #we can call class attribute directly
# # print(Student3.name) #preference will be given to object attribute
# class Student():
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def get_Avg(self):
#         total = 0
#         for val in self.marks:
#             total += val
#         print("Average", total/3)
# s1 = Student("Ali", [58,99,45])dfaf
# s1.get_Avg()

class Account():
    def __init__(self, blnc, acc_no):
        self.balance = blnc
        self.account_num = acc_no
    def debit(self, amount):
        self.balance -= amount
        print("Your Account is Debited = ", amount)
        print("Your current balance is = ", self.get_Blnc())
    def credit(self, amount):
        self.balance += amount
        self.get_Blnc
        print("Your Account is Creditedd = ", amount)
        print("Your current balance is = ", self.get_Blnc())
    def get_Blnc(self):
        return self.balance

user01 = Account(20000, 45204)
user01.debit(15000)
user01.credit(10000)
print("Current Balance = ",user01.get_Blnc())
