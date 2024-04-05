def validIP (ip):
    ip = ip.split('.')
    if len(ip) != 4:
        return False
    if not all(i.isnumeric() for i in ip):
        return False
    ip = [int(i) for i in ip]
    if max(ip) > 255 or min(ip) < 0:
        return False
    return True

def main():
    tess = int(input())
    addresses = [input() for _ in range(tess)]

    for address in addresses:
        if validIP(address):
            print('YES')
        else:
            print('NO')

main()

    