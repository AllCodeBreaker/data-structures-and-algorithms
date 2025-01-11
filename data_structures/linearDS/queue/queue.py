class Queue:

	def __init__(self):
		self._queue = []
	
	def enqueue(self, ele):
		self._queue.append(ele)
	def dequeue(self):
		return self._queue.pop(0)
	def isEmpty(self):
		return len(self._queue) == 0
	def display(self):
		for val in self._queue:
			print(val, end=" ")

if __name__ == "__main__":
	queue = Queue()
	print("Queue is created")
	queue.enqueue(7)
	queue.enqueue(67)
	queue.enqueue(23)
	print("Added 7 67 23 into the Queue")
	queue.display()
	print(f"{queue.dequeue()} removed from Queue")
	queue.display()

