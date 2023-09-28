passwoed = 'a123456'
i = 3
while  i > 0:
	password_input = input('請輸入密碼: ')
	if passwoed == password_input :
		print('登入成功')
		break;

	else :
		i = i -1 
		if i != 0 :
			print('密碼錯誤! 還有', i , '次機會')
		else :	
			print('密碼錯誤! 還有', i , '次機會')
			print('失敗')
			break;

