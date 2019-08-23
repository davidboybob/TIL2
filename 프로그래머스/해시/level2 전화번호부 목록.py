def solution(phone_book):
    
    for j in phone_book:
        c = j
        for i in range(len(phone_book)): 
            
            if len(c) <= len(phone_book[i]):
                if c == phone_book[i]:
                    continue
                if c == phone_book[i][:len(c)]:
                    return False
                
        else:        
            answer = True
        
        return answer




print(solution(['119', '97674223', '1195524421']))
print(solution(['123','456','789']))
print(solution(['12','123','1235','567','88']))