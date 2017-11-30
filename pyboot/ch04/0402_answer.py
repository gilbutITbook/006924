def game369(v):
    if v % 3 == 0:
        return '바보'
    elif "3" in str(v):
        return '바보'
    return v

# 동작 확인
result = game369(3)
print(result)
result = game369(32)
print(result)
result = game369(110)
print(result)
