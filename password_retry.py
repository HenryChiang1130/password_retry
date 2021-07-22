password = 'a123456'
x = int(3)
while True:
	a = input('請輸入密碼: ')
	if a == password:
		print('登入成功')
		break
	elif a != password and x > 1:
		x = x - 1
		print('密碼錯誤! 還有', x, '次機會')
	else:
		print('密碼錯誤! 請稍後再試')
		break