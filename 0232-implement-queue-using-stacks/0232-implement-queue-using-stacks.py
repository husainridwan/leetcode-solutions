# class MyQueue:

#     def __init__(self):
#         self.s1 = []
#         self.s2 = []

#     def push(self, x: int) -> None:
#         return s1.append(x)

#     def pop(self) -> int:
#         self.peek()
#         return self.s2.pop()

#     def peek(self) -> int:
#         if not s2:
#             while s1:
#                 return self.s2.append(s1.pop())
#         return s2[-1]
#     def empty(self) -> bool:
#         return not self.s1 and not self.s2

class MyQueue:
    """
    Each method is O(1) time complexity, while the "left"
    property is amortized O(1) time complexity, since
    each append-pop operation is done once for each
    element added to the queue.
    """

    def __init__(self):
        self.right = []
        self._left = []

    @property
    def left(self):
        if not self._left:
            while self.right:
                self._left.append(self.right.pop())
        return self._left

    def push(self, x: int) -> None:
        self.right.append(x)

    def pop(self) -> int:
        return self.left.pop()

    def peek(self) -> int:
        return self.left[-1]

    def empty(self) -> bool:
        return not self.left
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
