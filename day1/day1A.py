import sys

def main(input: str):
    with open(input) as f:
        res = 0
        for line in f:
            nums = list(filter(lambda x: x.isdigit(), line))
            first, second = nums[0], nums[-1]
            res += int(first + second)

    return res



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Provide a file to be opened")

    else:
        filename = sys.argv[1]
        print(main(filename))
