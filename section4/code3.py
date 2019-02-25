import time

start_time = time.perf_counter()

def squares(max_num=0):
	i = 0
	while i<max_num:
		result = i*i
		yield result
		i+=1

squares = squares(5)

num = 0
# while num<15:
# 	print(next(squares))
# 	num += 1

print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))


print("This search took: ", time.perf_counter() - start_time, "seconds")

print(type(squares))
print(dir(squares))
