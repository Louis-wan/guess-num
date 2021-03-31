import random
start = input('請start ')
end =  input ('請end num')
start = int (start)
end = int (end)
r = random.randint(start,end)
count = 0 

while True: 
	count = count + 1
	num = input('請猜數字 ')
	num = int(num)
	if num == r :
		print('猜對囉')
		print('這次你猜的第', count, '次')
		break
	elif num > r :
		print('數字猜太大囉')
	elif num < r :
		print('數字猜太小囉')
	print('這次你猜的第', count, '次')