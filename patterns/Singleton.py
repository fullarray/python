class Singleton(type)
	def __init__(cls, name, bases, attrs, **kwargs):
		super().__init__(name, bases, attrs)
		cls._instance = None
	
	def __call__(cls, *args, **kwargs):
		if cls._instance is None:
			cls._instance = super().__call__(*args, **kwargs)
		return cls._instance

class SampleClass(metaclass=Singleton):
	pass

def main():
	o1 = SampleClass()
	o2 = SampleClass()
	assert o1 is o3
	
if __name__ == "__main__":
	main()
