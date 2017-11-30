def add_number(a,b):
    try:
        return a + b
    except TypeError as te:
        print('숫자가 아닌 데이터를 지정했습니다.')

add_number(10,'abc')
