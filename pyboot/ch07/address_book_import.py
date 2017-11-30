class AddressBook:

    person_list = []

    def add(self, person):
        self.person_list.append(person)

    def show_all(self):
        for person in self.person_list:
            print(person.lastname + " " + person.firstname)

    def search(self,keyword):
        for person in self.person_list:
            if keyword in person.firstname or keyword in person.lastname:
                print(person.lastname + " " + person.firstname)

    def import_data(self,file):
        import csv
        import datetime

        with open(file, 'r',encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)  # 헤더가 있으면 건너뛰기

            for row in reader:
                # row에 데이터가 한 줄씩 할당됩니다.
                p = Person()
                p.lastname = row[0]
                p.firstname = row[1]
                p.mail_address = row[2]
                # 날짜 문자열로부터 날짜 타입 데이터를 만든다.
                p.birthday = datetime.datetime.strptime(row[3], "%Y/%m/%d")
                p.tel = row[4]

                self.person_list.append(p)

class Person:
    import datetime

    firstname = ''  # 이름
    lastname = ''  # 성
    tel = ''  # 전화번호
    mail_address = ''  # 메일 주소
    birthday = datetime.datetime(2000, 1, 1)  # 생년월일

ab = AddressBook()
ab.import_data('sample100.csv')

print('주소록에 등록된 사람 수->' + str(len(ab.person_list)) + '명')

ab.search('철수')
