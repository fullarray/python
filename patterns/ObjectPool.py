class ReusablePool:
	def __init__(self, size):
		self._reusables = [Reusable() for _ in range(size)]
	
	def acquire(self):
		return self._reusables.pop()
	
	def release(self):
		self._reusables.append(reusable)

class Reusable:
	pass

def main():
	reusable_pool = ReusablePool(20)
	reusable = reusable_pool.acquire()
	reusable_pool.release(reusable)
	
if __name__ == "__main__":
	main()