

def calc_iso_probability():
    answer = []
    for n in range(1, 91):
        if n <= 73:
            answer.append(0.006)
        else:
            answer.append(min(0.006+(n-73)*0.06, 1))
    return answer


def calc_probability():
    answer = []
    un_answer = []
    for i, prob in enumerate(calc_iso_probability()):
        if i == 0:
            answer.append(prob)
            un_answer.append(1-prob)
        else:
            answer.append(un_answer[-1]*prob)
            un_answer.append(un_answer[-1]*(1-prob))
    return answer


def expect():
    probability = calc_probability()
    ans = 0
    for i, prob in enumerate(probability):
        ans += (i+1)*prob
    return ans


def mode():
    probability = calc_probability()
    max_value = max(probability)
    max_index = probability.index(max_value)
    return max_index


print(calc_iso_probability())
print(len(calc_iso_probability()))
print(calc_probability())
print(len(calc_probability()))
print(sum(calc_probability()))
print("期待値", expect())
print("最頻値", mode())
