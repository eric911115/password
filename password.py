password = 'a123456'
x = 1
i = 3
while x < 4:
	password = input('請輸入密碼:')

	if password == 'a123456':
		print('登入成功')
		break
	else:
		i = i - 1
		print('密碼錯誤!還有', i, '次機會')
	x=x+1