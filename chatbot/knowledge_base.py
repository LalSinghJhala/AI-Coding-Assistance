# very tiny knowledge base for theory answers
answers = {
    "binary search": (
        "Binary Search is an efficient algorithm to find an element in a sorted array. "
        "It works by repeatedly dividing the search interval in half until the element is found. "
        "Time complexity: O(log n)."
    ),
    "merge sort": (
        "Merge Sort is a divide-and-conquer sorting algorithm. "
        "It divides the array into halves, sorts them recursively, and merges the results."
    ),
    "quick sort": (
        "Quick Sort is a fast divide-and-conquer sorting algorithm. "
        "It picks a pivot, partitions the array, and sorts each side recursively."
    ),
    "big o": (
        "Big-O describes how runtime scales with input size, e.g., O(1), O(log n), O(n), O(n log n), O(n^2)."
    ),
    "recursion": (
        "Recursion is when a function calls itself with a smaller subproblem until a base case is reached."
    ),
    "stack vs heap": (
        "Stack: automatic, fast, used for function calls and local variables. "
        "Heap: dynamic allocations, flexible but slower."
    ),
}

def get_answer(topic: str) -> str:
    topic = topic.lower()
    return answers.get(topic, f"Sorry, I don’t know about {topic} yet.")
