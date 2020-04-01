import random
mini = input('最小的數字: ')
maxi = input('最大的數字: ')
ma = int(maxi)
mi = int(mini)
r = random.randint(mi, ma)
i = 0
while True:
	n = input('請猜猜看數字是多少: ')
	n = int(n)
	if n == r:
		print('猜對了啦哈哈')
		break
	else:
		i = i + 1		
		if n > r:
			print('小一點啦幹!!')
		else:
			print('大一點啦幹!!')
		print('猜錯第', i, '次==')

