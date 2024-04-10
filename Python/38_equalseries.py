def find_min_step(series):
    min_step = 0
    chose_num = series[0]
    for i in range(len(series)):
        sum_step = 0
        for num in series:
            if num != series[i]:
                sum_step += abs(num - series[i])
        if sum_step < min_step or min_step == 0:
            min_step = sum_step
            chose_num = series[i]
    return min_step, chose_num


def input_series(tess):
    series = list(map(int, input().split()))
    for _ in range(tess, len(series)):
        series.pop()
    return series

def main():
    tess = int(input())
    series = input_series(tess)
    
    min_step, chose_num = find_min_step(series)
    print(min_step, chose_num)
    

main()