password = 'a123456'
i = 3
while i > 0:
	password = input('請輸入密碼:')
	if password == 'a123456':
		print('登入成功')
		break
	else:
		i = i - 1
		print('密碼錯誤!')
		if i > 0:
			print('還有', i, '次機會')
		else:
			print('你已經沒機會了!')