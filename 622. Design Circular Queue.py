class MyCircularQueue:

	def __init__(self, k: int):
		self.maxSize = k
		self.queue = [0] * k
		self.front = 0
		self.rear = -1

	def enQueue(self, value: int) -> bool:
		if self.isFull():
			return False
		self.queue[self.rear] = value
		self.rear = (self.rear + 1) % self.maxSize
		return True

	def deQueue(self) -> bool:
		if self.isEmpty():
			return False
		self.front = (self.front + 1) % self.maxSize
		return True

	def Front(self) -> int:
		if self.isEmpty():
			return -1
		return self.queue[self.front]

	def Rear(self) -> int:
		if self.isEmpty():
			return -1
		return self.queue[self.rear - 1]

	def isEmpty(self) -> bool:
		return self.rear - self.front == -1

	def isFull(self) -> bool:
		size = self.rear - self.front + 1
		if self.rear < self.front and self.rear > -1:
			size += self.maxSize
		return size == self.maxSize 


q = MyCircularQueue(3)

print(q.enQueue(1))
print(q.enQueue(2))
print(q.enQueue(3))
print(q.enQueue(4))
print(q.Rear())
print(q.isFull())
print(q.deQueue())
print(q.enQueue(4))
print(q.Rear())