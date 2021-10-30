password = 'a123456'
test = 3
while test != 0:
    pwd = input('請輸入密碼：')
    if pwd != password:
        test = test - 1
        print('密碼錯誤，還有', test, '次機會')
    else:
        print('登入成功')
        break