# very tiny knowledge base for theory answers
answers = {
    "binary search": (
        "Binary Search finds a target in a *sorted* array by repeatedly halving the search space. "
        "Time complexity: O(log n)."
    ),
    "big o": "Big-O describes how runtime scales with input size, e.g., O(1), O(log n), O(n), O(n log n), O(n^2).",
    "recursion": "Recursion is when a function calls itself with a smaller subproblem until a base case is reached.",
    "stack vs heap": "Stack: automatic, fast, for function frames. Heap: dynamic allocations, flexible but slower."
}

def get_answer(query: str) -> str:
    q = query.lower()
    for key, value in answers.items():
        if key in q:
            return value
    return "I don't know that yet. Try: binary search, big o, recursion, stack vs heap."
