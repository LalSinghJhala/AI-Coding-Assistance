from knowledge_base import get_answer

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

def handle(query: str) -> str:
    q = query.strip()
    qlow = q.lower()

    if qlow.startswith("explain "):
        # usage: explain binary search
        topic = q[8:].strip()
        return get_answer(topic)

    if qlow.startswith("run bs"):
        # demo run: binary search on a fixed list
        arr = [1, 2, 3, 7, 7, 9]
        target = 7
        idx = binary_search_py(arr, target)
        return f"binary_search({arr}, {target}) -> index {idx}"

    if qlow in {"help", "commands"}:
        return (
            "commands:\n"
            "  • explain <topic>    e.g., explain binary search\n"
            "  • run bs             demo binary search on a sample array\n"
            "  • quit               exit"
        )

    return "type 'help' to see commands."

if __name__ == "__main__":
    print("AI Coding Assistant (Step 1) — type 'help' for commands")
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
