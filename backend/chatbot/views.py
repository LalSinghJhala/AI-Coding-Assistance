from rest_framework.views import APIView
from rest_framework.response import Response

knowledge_base = {
    "binary search": "Binary search is O(log n). It works by repeatedly dividing the search space in half.",
    "big o": "Big O notation describes the time complexity of algorithms.",
    "recursion": "Recursion is when a function calls itself.",
    "stack vs heap": "Stack stores function calls, heap stores dynamically allocated memory."
}

class ChatbotView(APIView):
    def post(self, request):
        query = request.data.get("query", "").lower()

        if query.startswith("explain"):
            topic = query.replace("explain", "").strip()
            answer = knowledge_base.get(topic, "Sorry, I don't know that yet.")
            return Response({"answer": answer})

        elif query == "help":
            return Response({"answer": "Commands: explain <topic>, run bs, help, quit"})

        else:
            return Response({"answer": "Unknown command"})
