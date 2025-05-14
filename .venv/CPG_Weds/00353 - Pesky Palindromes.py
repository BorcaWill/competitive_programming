import sys

def main():
    input = sys.stdin.read
    data = input().strip().split("\n")
    for s in data:
        n = len(s)
        ans = 0
        pali_set = set()
        for i in range(n):
            for j in range(i, n):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    if s[i:j + 1] not in pali_set:
                        pali_set.add(s[i:j + 1])
                        ans += 1
        print(f"The string '{s}' contains {ans} palindromes.")

if __name__ == "__main__":
    main()