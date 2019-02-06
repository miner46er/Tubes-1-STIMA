import algoritma_greedy as greed

data_input = open("input.txt", "r")
data_output = open("output.txt", "w+")

l_quartet = data_input.readlines()

for lst in l_quartet:
	quartet = lst.split(' ')
	quartet[-1] = quartet[-1].strip()
	
	hasil = greed.solve24_greedy(quartet)
	data_output.write(hasil)
	data_output.write("\n")
	

data_input.close()
data_output.close()