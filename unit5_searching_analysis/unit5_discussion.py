"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""
# Used to time how long it takes a function to run.
import time


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """

    # Iterates through each item in the list and provides the idx for that item.
    for idx in range(len(lst)):
        # Uses the index to compare the item to the target.
        if lst[idx] == target:
            # Returns the index if the target is found.
            return idx

    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """

    # Initialize left and right limits.
    left = 0
    right = len(lst)-1

    # Searches as long as 1 item remains.
    while left <= right:
        # Gets the mid-point.
        mid = (left + right)//2

        mid_point = lst[mid]

        # Checks mid_point against target.
        if mid_point == target:

            # Returns index if found.
            return mid

        # If not found we check to see which half it might be on and remove the other.

        # Checks if mid_point is less than the target.
        if mid_point < target:

            # Removes the left half of the list by moving up the left limit.
            left = mid+1

        else:
            # mid_point is higher, so we remove the right side by lowering the right limit.
            right = mid-1

    # Target not found.
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.")
    # Small sorted data set
    small_lst = [i for i in range(100)]

    # Target to search for
    target = 87

    # Used to time the binary_search function.
    bs_start = time.perf_counter()

    # Does binary search.
    bs_result = binary_search(small_lst, target)

    # Used to time the binary_search function.
    bs_end = time.perf_counter()

    # Used to time the linear_search function.
    ls_start = time.perf_counter()

    # Does linear search.
    ls_result = linear_search(small_lst, target)

    # Used to time the linear_search function.
    ls_end = time.perf_counter()

    print(f"Result from the Binary Search was {bs_result} and took {bs_end - bs_start:.10f} seconds.\n")

    print(f"Result from the Linear Search was {ls_result} and took {ls_end - ls_start:.10f} seconds.\n")





    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")

    # Large sorted data set
    large_lst = [i for i in range(100000)]

    # Target to search for
    target2 = 87293

    # Used to time the binary_search function.
    bs_start = time.perf_counter()

    # Does binary search.
    bs_result = binary_search(large_lst, target2)

    # Used to time the binary_search function.
    bs_end = time.perf_counter()

    # Used to time the linear_search function.
    ls_start = time.perf_counter()

    # Does linear search.
    ls_result = linear_search(large_lst, target2)

    # Used to time the linear_search function.
    ls_end = time.perf_counter()

    print(f"Result from the Binary Search was {bs_result} and took {bs_end - bs_start:.10f} seconds.\n")

    print(f"Result from the Linear Search was {ls_result} and took {ls_end - ls_start:.10f} seconds.\n")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===\n")

    print("\n=== EMPTY LIST TEST ===\n")


    # Large sorted data set
    empty_lst = []

    # Target to search for
    target = 5

    # Used to time the binary_search function.
    bs_start = time.perf_counter()

    # Does binary search.
    bs_result = binary_search(empty_lst, target)

    # Used to time the binary_search function.
    bs_end = time.perf_counter()

    # Used to time the linear_search function.
    ls_start = time.perf_counter()

    # Does linear search.
    ls_result = linear_search(empty_lst, target)

    # Used to time the linear_search function.
    ls_end = time.perf_counter()

    print(f"Result from the Binary Search on an empty list was {bs_result} and took {bs_end - bs_start:.10f} seconds.\n")

    print(f"Result from the Linear Search on an empty list was {ls_result} and took {ls_end - ls_start:.10f} seconds.\n")


    print("\n=== SINGLE-ELEMENT LIST TEST ===\n")


    # Large sorted data set
    single_item_lst = [5]

    # Target to search for
    target = 5

    # Used to time the binary_search function.
    bs_start = time.perf_counter()

    # Does binary search.
    bs_result = binary_search(single_item_lst, target)

    # Used to time the binary_search function.
    bs_end = time.perf_counter()

    # Used to time the linear_search function.
    ls_start = time.perf_counter()

    # Does linear search.
    ls_result = linear_search(single_item_lst, target)

    # Used to time the linear_search function.
    ls_end = time.perf_counter()

    print(f"Result from the Binary Search on a single-element list was {bs_result} and took {bs_end - bs_start:.10f} seconds.\n")

    print(f"Result from the Linear Search on a single-element list was {ls_result} and took {ls_end - ls_start:.10f} seconds.\n")    


    print("\n=== VALUE NOT PRESENT TEST ===\n")


    # Large sorted data set
    item_lst = [5]

    # Target to search for
    target = 1

    # Used to time the binary_search function.
    bs_start = time.perf_counter()

    # Does binary search.
    bs_result = binary_search(item_lst, target)

    # Used to time the binary_search function.
    bs_end = time.perf_counter()

    # Used to time the linear_search function.
    ls_start = time.perf_counter()

    # Does linear search.
    ls_result = linear_search(item_lst, target)

    # Used to time the linear_search function.
    ls_end = time.perf_counter()

    print(f"Result from the Binary Search for a not present item was {bs_result} and took {bs_end - bs_start:.10f} seconds.\n")

    print(f"Result from the Linear Search for a not present item was {ls_result} and took {ls_end - ls_start:.10f} seconds.\n")  

    
    print("\n=== VALUE AT FIRST POSITION TEST ===\n")

    # Uses list used to demonstrate the small data set searches.

    # Target to search for
    target = 0

    # Used to time the binary_search function.
    bs_start = time.perf_counter()

    # Does binary search.
    bs_result = binary_search(small_lst, target)

    # Used to time the binary_search function.
    bs_end = time.perf_counter()

    # Used to time the linear_search function.
    ls_start = time.perf_counter()

    # Does linear search.
    ls_result = linear_search(small_lst, target)

    # Used to time the linear_search function.
    ls_end = time.perf_counter()

    print(f"Result from the Binary Search for item at first position was {bs_result} and took {bs_end - bs_start:.10f} seconds.\n")

    print(f"Result from the Linear Search for item at first position was {ls_result} and took {ls_end - ls_start:.10f} seconds.\n") 

    
    print("\n=== VALUE AT LAST POSITION TEST ===\n")

    # Uses list used to demonstrate the small data set searches.

    # Target to search for
    target = 99

    # Used to time the binary_search function.
    bs_start = time.perf_counter()

    # Does binary search.
    bs_result = binary_search(small_lst, target)

    # Used to time the binary_search function.
    bs_end = time.perf_counter()

    # Used to time the linear_search function.
    ls_start = time.perf_counter()

    # Does linear search.
    ls_result = linear_search(small_lst, target)

    # Used to time the linear_search function.
    ls_end = time.perf_counter()

    print(f"Result from the Binary Search for item at last position was {bs_result} and took {bs_end - bs_start:.10f} seconds.\n")

    print(f"Result from the Linear Search for item at last position was {ls_result} and took {ls_end - ls_start:.10f} seconds.\n") 


if __name__ == "__main__":
    main()
