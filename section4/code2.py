import time

start_time = time.perf_counter()


class Squares:
    def __init__(self, max_num = 0):
        self.max = max_num
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max:
            pass

        result = self.n*self.n
        self.n += 1
        return result

count = 0
squares = Squares(2)
# while count<15:
# 	print(next(squares))
# 	count+=1

print(dir(squares))

print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))

print("This search took: ", time.perf_counter() - start_time, "seconds")

# print(type(squares))
# print(dir(squares))