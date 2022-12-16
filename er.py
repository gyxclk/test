def ShowMenu():
    print ("——"*30)
    print ("    学生通信录管理系统    ")
    print ("1.添加学生")
    print ("2.删除学生")
    print ("3.修改学生")
    print ("4.查询学生")
    print ("5.获取所有学生通讯信息")
    print ("6.退出系统")
    print ("——"*30)


def getselect():
    selectNum = int(input("请输入选择的序号："))
    return selectNum


dict = {
    "杨海云":{"性别":"女","电话":"18863226522"},
    "高玉玺":{"性别":"女","电话":"17852529575"}
}



def addstuinfo():
    while True:
        name = input("请输入要添加的姓名:")
        sex = input("请输入要添加的性别：")
        telphone = input("请输入要添加的手机号码：")
        if len(telphone) != 11:
            print("输入的电话号码位数不正确，请重新输入")
            telphone = input("请输入要添加的手机号码：")
            studentlist = []
        studentlist.append(dict)
        x = input("输入p结束添加学生，输入其他任意字符将继续：")
        if x == "p":
            break
    dict[name] = {"性别": sex, "电话": telphone}
    print(dict)


def delstuinfo():
    name = input("你请输入要删除的姓名：")
    del dict[name]
    print (dict)

def modifystuinfo():
    name = input("请输入要修改的姓名：：")
    sex = input("请输入修改后的性别：")
    telphone = input("请输入修改后手机号码：")
    dict[name] ={"性别":sex,"电话":telphone}
    print(dict)

def seckstuinfo():
    name = input("请输入查询的姓名：")
    print(dict[name])

def showstuinfo():
    name = input("按enter键展示所有学生通信信息：")
    for i in dict.items():#dict.item遍历字典中所有元素
        print (i)

def exitSystem():
    print("***QAQ  谢谢使用本系统  QAQ***")



while True:
    ShowMenu()
    num = getselect()
    if num == 1:
        addstuinfo()
    elif num == 2:
        delstuinfo()
    elif num == 3:
        modifystuinfo()
    elif num == 4:
        seckstuinfo()
    elif num == 5:
        showstuinfo()
    elif num == 6:
        exitSystem()
        break
    else:
        print ("你的输入有误，请重新输入---------")


