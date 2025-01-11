
class Stack:
	def __init__(self):
		self._stack = []

	def push(self, ele):
		self._stack.append(ele)

	def pop(self):
		if len(self._stack) == 0:
			raise StackUnderFlow("Stack Underflow")
		else:
			return self._stack.pop()

	def isEmpty(self):
		return len(self._stack) == 0
	def display(self):
		print(self._stack)


if __name__ == "__main__":
	stack = Stack()
	print("Stack Created")
	stack.push(4)
	stack.push(7)
	stack.push(8)
	print("Added 4 7 8 into the stack")
	stack.display()
	print(f"{stack.pop()} popped from the stack")
	stack.display()

