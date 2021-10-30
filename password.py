password = 'a123456'
test = 3
while test != 0:
    test = test - 1
    pwd = input('請輸入密碼：')
    if pwd != password:    
        print('密碼錯誤')
        if test > 0:
            print('還有', test, '次機會')
        else:
            print('沒機會嘗試了！')
    else:
        print('登入成功！')
        break