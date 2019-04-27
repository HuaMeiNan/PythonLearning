import 系统功能


while True:

    print("*"*50)
    print("欢迎使用【名片管理系统】")
    print("")
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print("")
    print("0.退出系统")

    shuzi=input("请输入操作功能:")

    if shuzi == '1':
        系统功能.xinzengmingpian()


    elif shuzi == '2':
        系统功能.显示全部()

    elif shuzi == '3':
        系统功能.查询名片()

    elif shuzi == '0':
        print("成功退出系统")
        break



    print("*"* 50)

