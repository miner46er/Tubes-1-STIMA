import time
#import GUI
import algoritma_greedy

# -----------------MAIN PROGRAM------------------
# menerima masukan pengguna
userInput = input("Masukan 4 bilangan bulat 1-13: (e.g. 1 2 3 4)\n").split(' ')

if len(userInput) == 4: #input 4 bilangan
    # memulai penghitung waktu
    start = time.perf_counter()
    # mencari jawaban dari masukan
    answer = algoritma_greedy.solve24_greedy(userInput)
    # menghentikan penghitung waktu
    end = time.perf_counter()
    
    # menampilkan waktu algoritma dan jawaban
    print("Waktu yang dibutuhkan algoritma greedy: " + str((end-start)) + "s.\n")
    print(answer)

else: #input bukan 4 bilangan
    print("Masukan bukan 4 bilangan!")
