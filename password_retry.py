password = 'a123456'
x = int(3)
while x > 0:
	a = input('請輸入密碼: ')
	if a == password:
		print('登入成功')
		break
	else :
		x = x - 1
		if x > 0:
			print('密碼錯誤! 還有', x, '次機會')
		else:
			print('密碼錯誤! 請稍後再嘗試')