num = int(input("Enter your number: "))

def check_palindrome(num):
	t = num
	rev = 0
	while(num>0):
		dec = num%0
		rev = 10*rev + dec
		num = num//10
	if rev == t:
		return True
	return False

next_num = num + 1
check_next_num = check_palindrome(next_num)
while check_next_num == False:
	next_num = next_num + 1
	check_next_num = check_palindrome(next_num)

print(next_num)