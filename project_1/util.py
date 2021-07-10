class Util:

    def custom_input():
        answer = input(">>>")

        # answer의 길이가 1보다 크다면?
        if len(answer) > 1:
            return False
        elif len(answer) == 0:
            return False
        else:
            ascii_value = ord(answer)

            if ascii_value >= 47 and ascii_value <= 57:
                return int(answer)
            else:
                return False
