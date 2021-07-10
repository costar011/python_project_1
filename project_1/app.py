from db import Person
from util import Util
from program import Program

jyr = Person()  # Person 이라는 설계가 됨
jyr.data_setter("정예림", 19, "여성")
print(jyr)

DB_PEOPLE = []
DB_PEOPLE.append(jyr)


def startApp():
    print("💙💙💙💙💙💙💙💙💙💙💙💙💙💙💙💙💙")
    print("1. View People")
    print("2. Add People")
    print("3. Delete People")
    print("4. Exit Program")
    print("💙💙💙💙💙💙💙💙💙💙💙💙💙💙💙💙💙")

    an = Util.custom_input()

    if an is False:
        print("[SYSTEM] 잘못된 입력 입니다.")
        startApp()
    else:
        if an == 1:
            Program.view_people(DB_PEOPLE)
            startApp()
        elif an == 2:
            result = Program.create_people(DB_PEOPLE)

            if result is True:
                print("[SYSTEM] 새로운 사람이 추가되었습니다.")
                startApp()
            else:
                print("[SYSTEM] 사람 추가 실패했습니다. 다시 시도해주세요.")
                startApp()

        elif an == 3:
            result = Program.delete_people(DB_PEOPLE)

            if result is True:
                print("[SYSTEM] 사람이 삭제 되었습니다.")
                startApp()
            else:
                print("[SYSTEM] 사람 삭제 실패했습니다. 다시 시도해주세요.")
                startApp()

        elif an == 4:
            print("프로그램 종료")

        else:
            print("[SYSTEM] 잘못된 입력 입니다.")
            startApp()


startApp()
