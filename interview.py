# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#         #method using self
#     def method1(self):
#         # self.first_name = "Jane"
#         # self.last_name = "Doe"
#         self.middle_name = "roy"
#         print(self.first_name, self.last_name)
#         print(self.middle_name)
#         print("normal method")
#
#     #method without self
#     @staticmethod
#     def method2():
#         print("static method")
#
# p1 = Person("John", "Smith")
# # p1.method1()
# # p1.method2()
# Person.method2()
# p2 = Person("John", "Smith")
# p2.method1()
# # Person.method1()
#
#
# def extendList(val, lst=[]):
#     lst = []
#     lst.append(val)
#     return lst
# 
# list1 = extendList(10)
# print(list1)
# list2 = extendList(20, [])
# print(list2)
# list3 = extendList(30)
# print(list3)
