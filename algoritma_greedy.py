operators = ['+', '-', '*', '/']

def opScoreCalc(c):
    '''
    Menentukan score suatu operator
    '''
    if (c == '+'):
        return 5
    elif (c == '-'):
        return 4
    elif (c == '*'):
        return 3
    elif (c == '/'):
        return 2

def solve24_greedy(inputList):
    '''
    Menerima masukan berupa list berisi 4 bilangan.\n
    Mengeluarkan jawaban greedy dari game 24.
    '''
    # Preprocessing
    # mengubah list of string menjadi list of int untuk diurutkan
    lstInt = [int(item) for item in inputList]
    # mengurutkan list angka menjadi mengecil
    lstInt.sort(reverse = True)
    # mengembalikan list menjadi list of string untuk diproses lebih lanjut
    listNum = [str(item) for item in lstInt]
    
    # inisialisasi
    answer = listNum.pop(0)
    opScore = 0
    
    # iterasi setiap angka
    for num in listNum:
        tempTotalScore = -99999
        
        # iterasi tiap operator
        for op in operators:
            try:
                # menghitung score dari ekspresi sejauh ini
                tempScore = opScore + opScoreCalc(op) - abs(24 - eval(answer + op + num))
                
                # menyimpan hasil score terbaik
                if tempScore > tempTotalScore:
                    tempOp = op + num
                    tempOpScore = opScore + opScoreCalc(op)
                    tempTotalScore = tempScore
            
            # mencegah ZeroDivisionError
            except ZeroDivisionError:
                pass
        
        # menambahkan hasil iterasi greedy ke dalam jawaban
        answer += tempOp
        opScore = tempOpScore
    
    return answer
