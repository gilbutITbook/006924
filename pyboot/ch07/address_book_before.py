class AddressBook:

    # 주소록에 등록된 사람 목록
    person_list = []

    def add(self, person):
        # 주소록에 신규로 등록
        pass

    def show_all(self):
        # 등록된 사람들을 목록으로 표시
        pass

    def search(self, keyword):
        # 검색 조건에 일치하는 사람을 표시
        pass

class Person:
    import datetime

    firstname = '' # 이름
    lastname = '' # 성
    tel = '' # 전화번호
    mail_address = '' # 메일 주소
    birthday = datetime.datetime(2000, 1, 1) # 생년월일
