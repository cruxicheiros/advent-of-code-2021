import sys
import functools

def load_input_to_instruction_tuples(filename):
    result = []

    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()
            result.append((line[0], int(line[-1])))

    return result

def instruction_to_vector(instruction_tuple):
    if instruction_tuple[0] == "f":
        vector = (instruction_tuple[1], 0)
    elif instruction_tuple[0] == "u":
        vector = (0, 0 - instruction_tuple[1])
    elif instruction_tuple[0] == "d":
        vector = (0, instruction_tuple[1])
    else:
        raise Exception("Bad instruction", instruction_tuple[0])

    return vector

def vectorize(instructions):
    return map(instruction_to_vector, instructions)

def sum_tuple(a, b):
    return (a[0] + b[0], a[1] + b[1])

def get_position(vectors):
    return functools.reduce(sum_tuple, vectors)

def mult_tuple(position):
    return position[0] * position[1]

def move_with_aim(instruction_tuple, position_tuple):
    aim, x, y = position_tuple

    if instruction_tuple[0] == "f":
        y += aim * instruction_tuple[1]
        x += instruction_tuple[1]
    elif instruction_tuple[0] == "u":
        aim -= instruction_tuple[1]
    elif instruction_tuple[0] == "d":
        aim += instruction_tuple[1]
    else:
        raise Exception("Bad instruction", instruction_tuple[0])

    return aim, x, y

def get_position_part2(instructions):
    position = (0, 0, 0)

    for instruction in instructions:
        position = move_with_aim(instruction, position)

    return position

def part_1(instructions):
    return mult_tuple(get_position(vectorize(instructions)))

def part_2(instructions):
    return mult_tuple(get_position_part2(instructions)[1:3])

def main():
    instructions = load_input_to_instruction_tuples(sys.argv[1])
    print("part 1:", part_1(instructions))
    print("part 2:", part_2(instructions))

if __name__ == "__main__":
    main()