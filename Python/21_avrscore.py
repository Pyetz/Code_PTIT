def average_score(scores):
    min_score = min(scores)
    max_score = max(scores)
    while min_score in scores:
        scores.remove(min_score)
    while max_score in scores:
        scores.remove(max_score)
    return round(sum(scores) / len(scores), 2)

def main():
    total_score = int(input())
    scores = input().split()
    scores = [float(scores[i]) for i in range(total_score)]
    print(average_score(scores))

main()