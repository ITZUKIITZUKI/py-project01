# s = [56, 90, 88, 65, 90, 100, 209, 72, 145]
# print(s)
# s.append(199)#末尾添加
# print(s)
# s.insert(1, 100)#指定插入
# print(s)
# s.remove(88)#指定删除
# print(s)
# s.pop(4)#选择删除
# print(s)
# s.sort()#排序
# print(s)
# s.reverse()#反转
# print(s)
# s.clear()
# print(s)

# num_list =[]
# for s in range(10):
#     num = int(input("请输入1个数字:"))
#     num_list.append(num)
# print("数字列表",num_list)
# num_list.sort()
# print("排序后的数字列表",num_list)
# print("最小值",num_list[0])
# print("最大值",num_list[-1])
# print("平均值",sum(num_list)/len(num_list))

# num_list1 = [19,23,54,64,875,20,109,232,123,54]
# num_list2 = [55,80,72,35,60,123,54,29,91]
# # num_list3 = [*num_list1,*num_list2]
# num_list3 = num_list1 + num_list2
# num_list3.sort()
# print(num_list3)
# new_list = []
# for num in num_list3:
#     if num not in new_list:#判断是否在此列表中
#         new_list.append(num)
# new_list.sort()
# print(new_list)

# num_list2 = [i**2 for i in range(1,21)]#快速生成列表
# print(num_list2)


# num_list = [12,32,45,77,80,92,33,57,97,98,110,111,122]
# #new_list = [i**2 for i in num_list]#提取所有数并平方
# #[表达式 for 元素 in 可迭代对象 if 条件]
# new_list = [i**2 for i in num_list if i%2==0]#偶数
# print(new_list)

# num_list1 = ['M','A','C','E','F','G','H','L','N']
# num_list2 = ['X','Z','T','F','L','H']
# num_list3 = num_list1 + num_list2
# new_list = []
# for num in num_list3:
#         if num not in new_list:
#                 new_list.append(num)
# num_list3.sort()
# print(num_list3)

# str_list = []
# for i in range(10):
#         s = input(f"请输入第{i+1}个字符串:")
#         new_s = s[::-1].upper()
#         str_list.append(new_s)
# print(str_list)
#

# a=10
# b=20
# a,b=b,a#元组的组包解包
# print(a)
# print(b)

#&交集 #|交集 #-差集

# shopping_cart = {}
# print("-------欢迎使用购物车管理系统-------")
# menu = """
# ########## 购物车系统 ##########
# #         1.添加购物车         #
# #         2.修改购物车         #
# #         3.删除购物车         #
# #         4.查询购物车         #
# #         5.退出购物车         #
# ##############################
# """
# print(menu)
# while True:
#     choic = input("请选择要执行的操作(1-5):")
#     match choic:
#         case "1":#添加购物车
#             goods_name = input("请输入商品名称:")
#             goods_price = float(input("请输入商品价格:"))
#             goods_num = int(input("请输入商品数量:"))
#             if goods_name in shopping_cart:
#                 print("物品重复,请重新选择")
#             else:
#                 shopping_cart[goods_name] = {"price":goods_price,"num":goods_num}
#                 print("商品添加完毕!")
#         case "2":
#             goods_name = input("请输入要修改的商品名称:")
#             if goods_name not in shopping_cart:
#                 print("商品不存在!")
#                 continue
#             goods_price = float(input("请输入商品最新的价格:"))
#             goods_num = int(input("请输入商品最新的数量:"))
#             shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
#             print("商品添加完毕!")
#         case "3":
#             goods_name = input("请输入要删除的商品名称:")
#             if goods_name not in shopping_cart:
#                 print("商品不存在!")
#             else:
#                 del shopping_cart[goods_name]
#                 print("商品删除完毕!")
#         case "4":
#             for goods_name in shopping_cart.keys():
#                 goods_info = shopping_cart[goods_name]
#                 print(f"商品名称:{goods_name},商品价格:{goods_info["price"]},商品数量:{goods_info["num"]}")
#         case "5":
#             break
#         case _:
#             print("非法操作,不支持!!")



def input_student_name(prompt):
    while True:
        student_name = input(prompt).strip()
        if student_name:
            return student_name
        print("学生姓名不能为空，请重新输入!")


def input_score(prompt):
    while True:
        try:
            score = float(input(prompt))
        except ValueError:
            print("成绩必须是数字，请重新输入!")
            continue
        if 0 <= score <= 100:
            return score
        print("成绩必须在0到100之间，请重新输入!")


def print_student(student_name, student_info):
    print(
        f"学生名称:{student_name},"
        f"语文成绩:{student_info['语文成绩']},"
        f"数学成绩:{student_info['数学成绩']},"
        f"英语成绩:{student_info['英语成绩']}"
    )


print("    欢迎使用教务管理系统  ")
menu = """
******** 教务系统 ********
*     1.添加学生信息      *
*     2.修改学生信息      *
*     3.删除学生信息      *
*     4.查询学生信息      *
*     5.列出所有学生      *
*     6.统计班级成绩      *
*     7.退出系统         *
*************************
"""
print(menu)
student_new = {}
while True:
    choice = input("请选择一个操作输入数字:").strip()
    match choice:
        case "1":
            student_name = input_student_name("请输入学生姓名:")
            if student_name in student_new:
                print("学生重复,请重新输入!")
                continue
            student_chinese = input_score("请输入学生语文成绩:")
            student_math = input_score("请输入学生数学成绩:")
            student_english = input_score("请输入学生英语成绩:")
            student_new[student_name] = {
                "语文成绩": student_chinese,
                "数学成绩": student_math,
                "英语成绩": student_english
            }
            print("添加完毕!")
        case "2":
            student_name = input_student_name("请输入要修改的学生姓名:")
            if student_name not in student_new:
                print("学生信息不存在,请重新输入!")
                continue
            student_chinese = input_score("请输入修改后的学生语文成绩:")
            student_math = input_score("请输入修改后的学生数学成绩:")
            student_english = input_score("请输入修改后的学生英语成绩:")
            student_new[student_name] = {
                "语文成绩": student_chinese,
                "数学成绩": student_math,
                "英语成绩": student_english
            }
            print("修改完毕!")
        case "3":
            student_name = input_student_name("请输入要删除的学生姓名:")
            if student_name not in student_new:
                print("学生不存在!")
            else:
                del student_new[student_name]
                print("删除完毕!")
        case "4":
            student_name = input_student_name("请输入学生姓名:")
            if student_name not in student_new:
                print("学生不存在!")
            else:
                print_student(student_name, student_new[student_name])
        case "5":
            if not student_new:
                print("暂无学生信息!")
            else:
                for student_name, student_info in student_new.items():
                    print_student(student_name, student_info)
        case "6":
            if not student_new:
                print("暂无学生信息，请先添加学生!")
            else:
                for subject in ["语文成绩", "数学成绩", "英语成绩"]:
                    max_names = []
                    min_names = []
                    max_score = min_score = None
                    total_score = 0
                    for student_name, student_info in student_new.items():
                        score = student_info[subject]
                        total_score += score
                        if max_score is None or score > max_score:
                            max_score = score
                            max_names = [student_name]
                        elif score == max_score:
                            max_names.append(student_name)
                        if min_score is None or score < min_score:
                            min_score = score
                            min_names = [student_name]
                        elif score == min_score:
                            min_names.append(student_name)
                    average_score = total_score / len(student_new)
                    print(f"\n{subject}统计:")
                    print(f"最高分:{max_score:.1f}，姓名:{'、'.join(max_names)}")
                    print(f"最低分:{min_score:.1f}，姓名:{'、'.join(min_names)}")
                    print(f"平均分:{average_score:.2f}")
        case "7":
            print("退出系统")
            break
        case _:
            print("非法输入!")