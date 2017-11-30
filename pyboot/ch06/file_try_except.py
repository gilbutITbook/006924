try:
    file = open('python.txt', 'r')
except FileNotFoundError as fne:
    print('파일을 찾을 수 없습니다. 확인해주세요.')
