def solution(phone_book):
    c = phone_book[0]
    for j in range(1, len(phone_book)):
        if len(c) < len(phone_book(j)):
            c = phone_book[j]
            for i in range(len(phone_book)):
                if c == phone_book[i]:
                    continue
                if c == phone_book[i][:len(c)]:
                    return False
    
    return True




print(solution(['119', '97674223', '1195524421']))
print(solution(['123','456','789']))
print(solution(['12','123','1235','567','88']))