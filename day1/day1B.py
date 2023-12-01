import sys

values = {
    "o": [("one", "1")],
    "t": [("two", "2"), ("three", "3")],
    "f": [("four", "4"), ("five", "5")],
    "s": [("six", "6"), ("seven", "7")],
    "e": [("eight", "8")],
    "n": [("nine", "9")],

}


def main(input):
    with open(input) as f:
        sum = 0
        for line in f:
            i = 0
            res = []
            while i < len(line):
                char = line[i]
                if char.isdigit():
                    res.append(char)
                elif char in values:
                    nums = values[char]
                    for num in nums:
                        if num[0] == line[i:i+len(num[0])]:
                            res.append(num[1])
                i += 1
            
            first, second = res[0], res[-1]
            sum += int(first+second)


    return sum


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Provide a file to be opened")

    else:
        filename = sys.argv[1]
        print(main(filename))

