import sys

def load_input_to_list(filename):
    result = []

    with open(filename) as input_file:
        for line in input_file:
            result.append(int(line))

    return result

def find_result_pt1(depths):
    result = 0

    for i in range(1, len(depths)):
        if depths[i] > depths[i-1]:
            result += 1
            
    return result

def sum3(a,b,c):
    return a + b + c

def find_result_pt2(depths):
    result = 0
    prev = sum3(*depths[0:3])
    
    for i in range(1, len(depths)):
        if (i + 3) > len(depths):
            break  # a sum is not possible, so get out of the loop
        
        sum = sum3(*depths[i:i+3])

        if sum > prev:
            result += 1

        prev = sum

    return result

def main():
    print("Processing file", sys.argv[1])

    input_list = load_input_to_list(sys.argv[1])

    print("Part 1 result:", find_result_pt1(input_list))
    print("Part 2 result:", find_result_pt2(input_list))

if __name__ == "__main__":
    main()