import subprocess
from knowledge_base import get_answer


# -------- existing algorithms -------- #
def binary_search_py(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


def binary_search_cpp(target: int) -> str:
    exe_path = "./cpp_algos/binary_search.exe"  # adjust for Linux/Mac if needed
    try:
        result = subprocess.check_output([exe_path, str(target)], text=True).strip()
        return result
    except Exception as e:
        return f"[error running C++ binary_search] {e}"


def fibonacci_py(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_py(n-1) + fibonacci_py(n-2)


def merge_sort_py(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_py(arr[:mid])
    right = merge_sort_py(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# -------- memory (new for step 5) -------- #
last_command = None
last_topic = None


def handle(query: str) -> str:
    global last_command, last_topic

    q = query.strip()
    qlow = q.lower()

    # ---- memory-based commands ----
    if qlow == "repeat":
        if last_command:
            return handle(last_command)
        return "Nothing to repeat yet."

    if qlow == "why":
        if last_topic:
            return f"Why {last_topic}? Because it helps solve problems efficiently. (expand with examples later!)"
        return "No topic to explain why yet."

    if qlow == "details":
        if last_topic:
            return f"Here are more details about {last_topic}: {get_answer(last_topic)}"
        return "No topic to expand yet."

    # ---- normal commands ----
    if qlow.startswith("explain "):
        topic = q[8:].strip()
        last_topic = topic
        last_command = q
        return get_answer(topic)

    if qlow.startswith("run bs py"):
        last_command = q
        arr = [1, 2, 3, 7, 7, 9]
        target = 7
        idx = binary_search_py(arr, target)
        return f"[Python] binary_search({arr}, {target}) -> index {idx}"

    if qlow.startswith("run bs cpp"):
        last_command = q
        target = 7
        idx = binary_search_cpp(target)
        return f"[C++] binary_search(target={target}) -> index {idx}"

    if qlow.startswith("run fib py"):
        last_command = q
        n = 6
        result = fibonacci_py(n)
        return f"[Python] fibonacci({n}) -> {result}"

    if qlow.startswith("run merge py"):
        last_command = q
        arr = [5, 2, 9, 1, 6]
        sorted_arr = merge_sort_py(arr)
        return f"[Python] merge_sort({arr}) -> {sorted_arr}"

    if qlow in {"help", "commands"}:
        return (
            "commands:\n"
            "  • explain <topic>\n"
            "  • run bs py / run bs cpp\n"
            "  • run fib py\n"
            "  • run merge py\n"
            "  • repeat      (repeat last command)\n"
            "  • why         (why about last topic)\n"
            "  • details     (more info on last topic)\n"
            "  • quit"
        )

    return "type 'help' to see commands."


if __name__ == "__main__":
    print("AI Coding Assistant (Step 5: Memory) — type 'help' for commands")
    while True:
        try:
            q = input("you> ")
        except (EOFError, KeyboardInterrupt):
            print("\nbye!")
            break

        if q.strip().lower() in {"quit", "exit"}:
            print("bye!")
            break

        print("bot>", handle(q))
