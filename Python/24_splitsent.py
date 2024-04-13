txt = ''
while True:
    try:
      line = input()
    except EOFError:
        break
    txt += line + '\n'

result = []
current_string = ''
for char in txt:
    if char == '.' or char == '?' or char == '!':
        result.append(current_string.strip().capitalize())
        current_string = ''
    else:
        current_string += char

for sentence in result:
    print(sentence)