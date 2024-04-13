class Candidate:
    static_id = 0
    def __init__(self, name, theory, practice):
        Candidate.static_id += 1
        self.id = 'TS0' + str(Candidate.static_id)
        self.name = name
        while theory > 10:
            theory /= 10
        while practice > 10:
            practice /= 10
        self.theory = theory
        self.practice = practice

    def avr_score(self):
        return (self.theory + self.practice) / 2
    
    def classify(self):
        if self.avr_score() < 5:
            return "TRUOT"
        elif self.avr_score() < 8:
            return "CAN NHAC"
        elif self.avr_score() <= 9.5:
            return "DAT"
        else:
            return "XUAT SAC"
        
def rank_candidates(candidates):
    return sorted(candidates, key = lambda x: x.avr_score(), reverse = True)
        
def input_candidates(tess):
    candidates = []
    for _ in range(tess):
        name = input()
        theory = float(input())
        practice = float(input())
        candidates.append(Candidate(name, theory, practice))
    return candidates

def main():
    tess = int(input())
    candidates = input_candidates(tess)
    candidates = rank_candidates(candidates)

    for candidate in candidates:
        print(candidate.id, candidate.name, format(candidate.avr_score(), '.2f'), candidate.classify())

main()   