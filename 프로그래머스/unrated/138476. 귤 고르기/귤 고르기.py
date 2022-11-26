def solution(k, tangerine):
    d = {}
    for data in tangerine:
        if not data in d:
            d[data] = 1
        else:
            d[data] += 1
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    cnt = 0
    result = []
    for idx, data in enumerate(d):
        if cnt + data[1] <= k:
            result.append(data[0])
            cnt += data[1]
        else:
            if cnt == k:
                break
            result.append(data[0])
            break


    answer = 0
    return len(result)