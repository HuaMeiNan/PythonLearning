mingpian_lisr = []


def xinzengmingpian():
    name = input("请输入名片名字")
    phone = input("请输入电话")
    email = input("请输入邮箱")
    mingpian_dic = {'name': name, 'phone': phone, 'email': email}
    mingpian_lisr.append(mingpian_dic)
    print('成功添加名片')


def 显示全部():
    if len(mingpian_lisr) == 0:
        print('没有任何名片')
        return

    for 表头 in ['名字', '电话', '邮箱']:
        print(表头, end='\t\t\t')
    print('')
    print('-' * 50)

    for mingpian_dic in mingpian_lisr:
        print('%s\t\t\t%s\t\t\t%s' % (mingpian_dic['name'], mingpian_dic['phone'], mingpian_dic['email']))


def 查询名片():
    chaxunmingpian = input('请输入要查询的名片')



    for chaxun in mingpian_lisr:
        if chaxun['name'] == chaxunmingpian :
            print('%s\t\t%s\t\t%s' %(chaxun['name'],chaxun['phone'],chaxun['email']))

            caozuo = input('请选择要执行的操作 【1修改】 【2删除】【3返回菜单】')

            if caozuo == '1':

                chaxun['name'] = xiugaimingzi('请输入新名字',chaxun['name'])
                chaxun['phone']=xiugaimingzi('请输入新手机',chaxun['phone'])
                chaxun['email']=xiugaimingzi('请输入新邮箱',chaxun['email'])
                print('恭喜修改成功')

                return

            if caozuo == '2':
                mingpian_lisr.remove(chaxun)
                print('删除成功')

                return




    else:
        print('没有找到名片')


def xiugaimingzi(xinmingzi,jiumingzi):
    p=input(xinmingzi)

    if len(p) > 0 :
        return p

    else:
        return jiumingzi




