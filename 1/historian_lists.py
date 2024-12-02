import sys
from typing import List
from collections import Counter


def read_file_into_lists(file_path: str) -> tuple[List[int], List[int]]:
    """
    Reads a file with two columns of numbers and loads them into two separate lists.

    Args:
        file_path (str): The path to the file.

    Returns:
        (List[int], List[int]): Two lists containing the numbers from the file's columns.
    """
    left_list = []
    right_list = []
    with open(file_path, "r") as file:
        for line in file:
            numbers = line.strip().split()
            if len(numbers) == 2:
                left_list.append(int(numbers[0]))
                right_list.append(int(numbers[1]))
    return left_list, right_list


def calculate_total_distance(left_list: List[int], right_list: List[int]) -> int:
    """
    Calculate the total distance between two lists.
    Each pair is formed by the smallest remaining numbers from both lists.

    Args:
        left_list (List[int]): The first list of integers.
        right_list (List[int]): The second list of integers.

    Returns:
        int: The total distance between the two lists.
    """
    # Sort both lists
    left_list.sort()
    right_list.sort()

    # Calculate the total distance
    return sum(
        abs(left_list_element - right_list_element)
        for left_list_element, right_list_element in zip(left_list, right_list)
    )


def calculate_similarity_score(left_list: List[int], right_list: List[int]) -> int:
    """
    Calculate the similarity score between two lists.
    The score is the sum of each number in the left list multiplied by its frequency in the right list.

    Args:
        left_list (List[int]): The first list of integers.
        right_list (List[int]): The second list of integers.

    Returns:
        int: The similarity score.
    """
    # Count occurrences of each number in the right list
    right_counts = Counter(right_list)

    # Calculate the similarity score
    similarity_score = sum(num * right_counts[num] for num in left_list)

    return similarity_score


def main():
    """
    Main function to read the input file, calculate the total distance, and print the result.
    """
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        # Read the file into two lists
        left_list, right_list = read_file_into_lists(file_path)

        # Calculate the total distance
        total_distance = calculate_total_distance(left_list, right_list)

        similarity_score = calculate_similarity_score(left_list, right_list)

        # Print the result
        print(f"Total distance: {total_distance}")
        print(f"Similarity score: {similarity_score}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except ValueError:
        print("Error: File contains invalid data.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
