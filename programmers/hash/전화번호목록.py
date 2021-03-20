def solution(phone_book):
    answer = True
    len_book=len(phone_book)
    phone_book.sort()
    
    for i in range(len_book-1):
        print('1:',phone_book[i],'2:',phone_book[i+1])
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer=False
    return answer
