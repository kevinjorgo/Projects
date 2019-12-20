def num_coins(num, cntr):
	coins = [25,10,5,1]
	

	for i in range(0, len(coins)):
		sum = num - coins[i]

		if (sum%coins[i] != 0) and (sum%coins[i] != sum) and (sum>=0):
			cntr+=1
		elif sum%coins[i] == 0:
		 	num_coins(sum, cntr)

	print(cntr+1)

def main():	
	counter = 0

	num_coins(31,counter)

if __name__ == '__main__':
	main()