
# coding: utf-8
class makedata:
    def __init__(self):
        print("Success a Instance!")

    def users(self):
        alpha_list = []
        res = []
        for i in range(48,48+10):
            alpha_list.append(chr(i))
        for i in range(97,97+26):
            alpha_list.append(chr(i))
        for i in range(65,65+26):
            alpha_list.append(chr(i))
        
        count = 0
        for count in range(100):
            numbers = range(61)
            alphas = [(n) for n in numbers]
    
            res = random.sample(alphas,6)
    
            print(alpha_list[res[0]]+alpha_list[res[1]]+alpha_list[res[2]]+alpha_list[res[3]]+alpha_list[res[4]]+alpha_list[res[5]])
    
            print(char)
            count = count + 1
    
    def context(self):
        

