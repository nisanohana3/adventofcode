import re
from typing import List


def extract_file(file_path: str) -> str:
    """
    Reads the memory string from a file.

    Args:
        file_path (str): Path to the file containing the corrupted memory.

    Returns:
        str: The corrupted memory string.
    """
    with open(file_path, "r") as file:
        memory = file.read()

    return memory


def parse_mul_instructions_part_1(memory: str) -> List[int]:
    """
    Parses the memory string to find all valid mul(X,Y) instructions
    and computes their results.

    Args:
        memory (str): The corrupted memory string containing instructions.

    Returns:
        List[int]: A list of results from valid mul(X,Y) instructions.
    """
    # Regular expression to match valid mul(X,Y) instructions
    pattern = r"mul\((\d+),(\d+)\)"

    # Find all matches in the memory string
    matches = re.findall(pattern, memory)

    # Compute results of the valid instructions
    results = [int(x) * int(y) for x, y in matches]

    return sum(results)


def calculate_enabled_multiplications_part_2(memory: str) -> int:
    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"

    instructions = re.findall(pattern, memory)

    # Initially, mul instructions are enabled
    mul_enabled = True
    total_sum = 0

    for instruction in instructions:
        if instruction == "do()":
            # Enable future mul instructions
            mul_enabled = True
        elif instruction == "don't()":
            # Disable future mul instructions
            mul_enabled = False
        elif instruction.startswith("mul(") and mul_enabled:
            # Process the mul(X,Y) instruction if enabled
            # Extract the two numbers using regex
            match = re.match(r"mul\((\d+),(\d+)\)", instruction)
            if match:
                x, y = map(int, match.groups())
                total_sum += x * y

    return total_sum


def main():
    """
    Main function to handle input and compute the sum of valid mul(X,Y) results.
    """
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        memory = extract_file(file_path)

        part_1_total_sum = parse_mul_instructions_part_1(memory)
        print(f"The sum of all valid multiplications is: {part_1_total_sum}")

        part_2_total_sum = calculate_enabled_multiplications_part_2(memory)
        print(f"The sum of all valid multiplications is: {part_2_total_sum}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
