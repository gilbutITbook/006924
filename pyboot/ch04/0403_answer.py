import random
def make_random_array(size):
    result = []
    for v in range(size):
        result.append(random.randint(0, 100))
    return result

# 동작 확인
result = make_random_array(10)
print(result)
result = make_random_array(25)
print(result)
