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

def solve24_greedy(lst):
    '''
    Menerima masukan berupa list berisi 4 bilangan.\n
    Mengeluarkan jawaban greedy dari game 24.
    '''
    # Preprocessing
    # mengurutkan list angka menjadi mengecil
    lst.sort(reverse = True)
    
    # inisialisasi
    answer = lst.pop(0)
    opScore = 0
    
    for num in lst:
        tempTotalScore = -99999
        
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
        
        answer += tempOp
        opScore = tempOpScore
    
    return answer
