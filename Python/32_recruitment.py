class Candidate:
    static_id = 0
    def __init__(self, name, theory, practice):
        Candidate.static_id += 1
        self.id = 'TS' + str(Candidate.static_id).zfill(2)
        self.name = name
        if float(theory) > 10:
            theory = theory.strip('0')
            if theory == '1':
                theory = '10'
            else:            
                theory = theory[0] + "." + theory[1:]
        if float(practice) > 10:
            practice = practice.strip('0')
            if practice == '1':
                practice = '10'
            else:
                practice = practice[0] + "." + practice[1:]
        self.avr_score = (float(theory) + float(practice)) / 2
    
    def classify(self):
        if self.avr_score < 5:
            return "TRUOT"
        elif self.avr_score < 8:
            return "CAN NHAC"
        elif self.avr_score <= 9.5:
            return "DAT"
        else:
            return "XUAT SAC"
        
def rank_candidates(candidates):
    return sorted(candidates, key = lambda x: x.avr_score, reverse = True)
        
def input_candidates(tess):
    candidates = []
    for _ in range(tess):
        name = input()
        theory = input()
        practice = input()
        candidates.append(Candidate(name, theory, practice))
    return candidates

def main():
    tess = int(input())
    candidates = input_candidates(tess)
    candidates = rank_candidates(candidates)

    for candidate in candidates:
        print(candidate.id, candidate.name, format(candidate.avr_score, '.2f'), candidate.classify())

main()