import algoritma_greedy as greed
import sys

data_input = open(sys.argv[1], "r")
data_output = open(sys.argv[2], "w+")

l_quartet = data_input.readlines()

for lst in l_quartet:
	quartet = lst.split(' ')
	quartet[-1] = quartet[-1].strip()
	
	hasil = greed.solve24_greedy(quartet)
	data_output.write(hasil)
	data_output.write("\n")
	

data_input.close()
data_output.close()