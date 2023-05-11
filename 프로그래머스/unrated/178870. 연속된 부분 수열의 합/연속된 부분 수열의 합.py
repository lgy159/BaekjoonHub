def solution(sequence, k):
    answer = []
    left, right = 0, 0
    now = sequence[0]
    while len(sequence) > right and sequence[right] <= k:
        if now > k:
            now -= sequence[left]
            left += 1
        elif now < k:
            right += 1
            if right == len(sequence):
                now -= sequence[left]
                left += 1
                continue
            now += sequence[right]
        else:
            answer.append((right - left, left, right))
            right += 1
            if right == len(sequence):
                now -= sequence[left]
                left += 1
                continue
            now += sequence[right]
        #print(now, left, right)
    
    answer.sort()
    #print(answer)
    answer = [answer[0][1], answer[0][2]]
    return answer