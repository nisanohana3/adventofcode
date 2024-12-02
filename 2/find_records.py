from typing import List


def parse_reports(file_path: str) -> List[List[int]]:
    """
    Parses the input file and returns a list of reports.
    Each report is represented as a list of integers.

    Args:
        file_path (str): Path to the file containing the reports.

    Returns:
        List[List[int]]: A list of reports, where each report is a list of integers.
    """
    reports = []
    with open(file_path, "r") as file:
        for line in file:
            report = list(map(int, line.strip().split()))
            reports.append(report)
    return reports


def is_report_safe(report: List[int]) -> bool:
    """
    Determines if a report is safe based on the rules:
    1. Levels are either all increasing or all decreasing.
    2. Any two adjacent levels differ by at least 1 and at most 3.

    Args:
        report (List[int]): A list of integers representing the levels in a report.

    Returns:
        bool: True if the report is safe, False otherwise.
    """
    if len(report) < 2:
        return True  # A single level or empty report is considered safe by default.

    differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    # Check if differences are consistent (all positive or all negative) and within the range 1 to 3
    is_increasing = all(1 <= diff <= 3 for diff in differences)
    is_decreasing = all(-3 <= diff <= -1 for diff in differences)

    return is_increasing or is_decreasing


def is_report_safe_with_dampener(report: List[int]) -> bool:
    """
    Determines if a report is safe, considering the Problem Dampener.
    The Dampener allows removing one level to make the report safe.

    Args:
        report (List[int]): A list of integers representing the levels in a report.

    Returns:
        bool: True if the report is safe or can be made safe by removing one level, False otherwise.
    """
    if is_report_safe(report):
        return True

    for i in range(len(report)):
        # Create a new report with one level removed
        modified_report = report[:i] + report[i + 1 :]
        if is_report_safe(modified_report):
            return True

    return False


def count_safe_reports(file_path: str) -> int:
    """
    Counts the number of safe reports in a file.

    Args:
        file_path (str): Path to the file containing the reports.

    Returns:
        int: The count of safe reports.
    """
    reports = parse_reports(file_path)
    return sum(is_report_safe(report) for report in reports)


def count_safe_reports_with_dampener(file_path: str) -> int:
    """
    Counts the number of safe reports in a file, considering the Problem Dampener.

    Args:
        file_path (str): Path to the file containing the reports.

    Returns:
        int: The count of safe reports, considering the Problem Dampener.
    """
    reports = parse_reports(file_path)
    return sum(is_report_safe_with_dampener(report) for report in reports)


def main():
    """
    Main function to read the input file, count the number of safe reports, and print the result.
    """
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        # Count the safe reports
        safe_count = count_safe_reports(file_path)
        print(f"Number of safe reports: {safe_count}")

        safe_count_with_dampener = count_safe_reports_with_dampener(file_path)
        print(f"Number of safe reports (with Dampener): {safe_count_with_dampener}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except ValueError:
        print("Error: File contains invalid data.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
