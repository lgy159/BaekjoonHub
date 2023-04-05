def cal(today, month, before):
    t_year, t_month, t_day = map(int, today.split('.'))
    b_year, b_month, b_day = map(int, before.split('.'))

    t = t_year * 12 * 28 + t_month * 28 + t_day
    b = b_year * 12 * 28 + b_month * 28 + b_day + month * 28
    
    return 1 if t >= b else 0
    
    
def solution(today, terms, privacies):
    answer = []
    term = {}
    for data in terms:
        term[data[0]] = int(data[2:])
    
    for idx, data in enumerate(privacies):
        if cal(today, term[data[11]], data[:10]):
            answer.append(idx + 1)
    
    answer.sort()
    return answer