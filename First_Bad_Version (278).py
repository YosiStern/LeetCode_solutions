import math


class CheckVersion():
    _first_bad_ = 0  # [4, 1, 1, 0, 666]

    def update_first_bad(self, bad):
        self._first_bad_ = bad

    def is_bad_version(self, n):
        return True if n < self._first_bad_ else False


def first_bad_version(n: int) -> int:
    # Initialize variables to represent the range of versions we are currently searching.
    low, high = 1, n

    # Binary search loop to find the first bad version.
    while low < high:
        # Calculate the mid-point of the current range.
        i = math.ceil((high - low) / 2)

        # Check if the version at the mid-point is bad or not by calling the API isBadVersion.
        bad = is_bad_version(low + i)

        # If the version at the mid-point is bad, the first bad version lies in the left half of the range.
        if bad:
            # Update the 'high' boundary to narrow down the search range to the left half.
            high = high - i
        else:
            # If the version at the mid-point is not bad, the first bad version lies in the right half of the range.
            # Update the 'low' boundary to narrow down the search range to the right half.
            low = low + i + 1

    # At the end of the loop, 'low' and 'high' will be equal, and the search range will be narrowed down to a single
    # version.

    # Check if the version at 'high' is not bad. If it's not bad, it means the first bad version is the next version,
    # so return 'high + 1'.
    if not is_bad_version(high):
        return high + 1
    # If the version at 'high' is bad, it means the first bad version is at 'high', so return 'high'.
    return high


# Test cases
def test_first_bad_version():
    # Test case 1
    n1 = 5
    bad = 4
    result1 = first_bad_version(n1)
    assert result1 == bad, f"Expected {bad}, but got {result1}"

    # Test case 2
    n2 = 1
    bad = 1
    result2 = first_bad_version(n2)
    # assert result2 == bad, f"Expected {bad}, but got {result2}"

    # Test case 3 (Edge case: Only one version, which is bad)
    n3 = 1
    bad = 1
    result3 = first_bad_version(n3)
    assert result3 == bad, f"Expected {bad}, but got {result3}"

    # Test case 4 (Edge case: Only one version, which is not bad)
    n4 = 1
    bad4 = 0
    result4 = first_bad_version(n4)
    assert result4 == bad4, f"Expected {bad4}, but got {result4}"

    # Test case 5 (Large number of versions)
    n5 = 1000
    bad5 = 666
    result5 = first_bad_version(n5)
    assert result5 == bad5, f"Expected {bad5}, but got {result5}"

    # Add more test cases if needed

    print("All test cases passed!")


# Call the test function to run the test cases
if __name__ == '__main__':
    test_first_bad_version()
