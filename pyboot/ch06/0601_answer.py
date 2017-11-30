def test(idx):
    try:
        abc = ['a','b','c']
        print(abc[idx])
    except IndexError as ie:
        print('인덱스가 범위 밖입니다.')

test(10)
