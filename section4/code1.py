import time

start_time = time.perf_counter()

nums = range(1000000)
squares = []
for num in nums:
	squares.append(num*num)
for square in squares[:15]:
	print(square)

print("This search took: ", time.perf_counter() - start_time, "seconds")

print(dir(squares))
