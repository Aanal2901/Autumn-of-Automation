d = int(input("Enter the decimal digit: "))
#d = 1
def check_prime(n):
	if n>1:
		for i in range(2,n):
			if n%i==0:
				return False
		return True
	return False

f = open("Text file for Q1", "w+")


for i in range(10**(d-1), 10**d):
	if check_prime(i):
		prime1 = i
		t = i+2
		if (check_prime(t) and t<10**d):
			#print(str(i)+" "+str(t))
			f.write(str(i)+" "+str(t)+ "\n")

f.close()
