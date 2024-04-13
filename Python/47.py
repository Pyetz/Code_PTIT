def process_file(filename):
    result = []
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if not word.isdigit():
                    result.append(word)
    
    result.sort()
    return result

filename = 'DATA.in'
output = process_file(filename)
print(' '.join(output))