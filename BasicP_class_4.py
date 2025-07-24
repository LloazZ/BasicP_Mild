# def my_sum(num1,num2):
#     return num1 + num2

# sum_riw_vava = my_sum(14, 47)
# print(sum_riw_vava)


# def ginkaw(spoon,rice):
#     if spoon == True and rice == True:
#         return "มีทั้งช้อน ทั้งข้าว กินข้าวได้"
#     elif spoon == True and rice == False:
#         return "มีช้อน ไม่มีข้าว กินไม่ได้"
#     elif spoon == False and rice == True:
#         return "ไม่มีช้อน แต่มีข้าว กินไม่ได้"
#     else:
#         return "ไม่มีอะไรสักอย่างไม่ต้องกิน"
    
# print(ginkaw(False,True))

# def calculator(num1, num2, cmd):
#     print("Calculator: ", num1, cmd, num2)
#     if cmd == "sum":
#         return num1 + num2
#     elif cmd == "minus":
#         return num1 - num2
# print(calculator(5, 5, "minus"))

# def pnt_n_times(times):
#     for t in range(1, times +1):
#         print(t, "Hello")

# pnt_n_times(4)

# box = ["pen", 30, True, "ruler"]
# print(box[0])
# print(box[1])
# print(box[3])
# box[0] = "book"
# print(box[0])
# print(box)
# box.append("space")
# print("append", box)
# box.pop(2)
# print("pop ", box)

# box = ["pen", 30, True, "ruler"]
# for i in range(5):
#     print(i, "Starter Pack")
# print("----------")
# for i in [0, 1, 2, 3, 4]:
#     print(i, "Starter Pack")
# print("----------")
# for i in box:
#     print(i, "Starter Pack")

# box_fruit = ["apple", "banana", "watermelon"]
# for fruit in box_fruit:
#     if fruit == "apple":
#         print("apple aroi")
#     else:
#         print("mai jer")

# box_fruit = ["apple", "orange", "watermelon", "banana", "coconut"]
# def find_fruit(fruit):
#     for i in box_fruit:
#         if i == fruit:
#             print("orange aroi")
#         else:
#             print("orange mai aroi")
    
# find_fruit("orange")

# student = {"name_student": "Thanasorn Dusadeeroj",
#             "age": 19 ,
#             "ID": 1234567}

# print(student)

# student = {"name_student": "Mild",
#            "age": 18 ,
#            "ID": 1234567890}

# if student["age"] >= 18:
#     print("ผ่าน")
# else:
#     print("ไม่ผ่าน")

# students = [{"name": "Thanasorn Dusadeeroj", "age": 19, "ID": 67130500014},
#             {"name": "satit", "age": 19, "ID": 6713050047}]

# for i in students:
#     print(i["name"])
#     if (i["age"]) >= 18:
#         print("เกิน")
#     else:
#         print("ไม่เกิน")
        
