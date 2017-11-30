def compare_string(a, b):
    if len(a) > len(b):
        return a
    return b

# 동작 확인
result = compare_string('AAA', 'BBBBB')
print(result)
