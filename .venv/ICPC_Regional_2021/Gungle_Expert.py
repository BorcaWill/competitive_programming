def main():
    W = list(input().strip())
    n = len(W)
    i = 0
    while i < n:
        if isVowel(W[i]):
            if i == 0:
                W[i] = 'G'
            elif W[i-1] not in 'GL':
                if (i < n-1 and isVowel(W[i+1])):
                    W[i] = 'G'
                else:
                    W[i-1] = 'G' 
        i += 1
    W = ''.join(W)
    print(W)
def isVowel(c: str)->bool:
    return c in 'AEIOU'

if __name__ == "__main__":
    main()