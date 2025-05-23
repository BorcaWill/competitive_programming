import sys
dict_of_quirksome_squares = dict()
def main():
    input = sys.stdin.read
    data = input().strip().split("\n")
    square_numbers = list()
    data = list(map(int, data))
    for i in range(10**(max(data)//2)):
        square_numbers.append(i**2)
    for l in data:
        if l in dict_of_quirksome_squares:
            for i in dict_of_quirksome_squares[l]:
                print(f"{i:0{l}d}")
        else:
            for i in square_numbers:
                if i>=10**l:
                    break
                first_half = i // (10**(l//2))
                second_half = i % (10**(l//2))
                if (first_half + second_half)**2 == i:
                    if l not in dict_of_quirksome_squares:
                        dict_of_quirksome_squares[l] = list()
                    dict_of_quirksome_squares[l].append(i)
                    print(f"{i:0{l}d}")

if __name__ == "__main__":
    main()