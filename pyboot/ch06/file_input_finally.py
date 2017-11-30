file = None
try:
	file = open('file_not_found_exception','r')
except FileNotFoundError as ioe:
	print('파일을 찾을 수 없습니다.')
finally:
	file.close()
