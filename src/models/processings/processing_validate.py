from src.models.utils.ascii import BColors


class PydanticResponseError:
    @staticmethod
    def print_error(e):
        print(BColors.WARNING + "\n__________<ReportValidate>__________" + BColors.ENDC)
        print(BColors.BOLD + "Ошибка валидации, тип:" + BColors.ENDC,
              BColors.FAIL + repr(e.errors()[0]['type']),
              ":", repr(e.errors()[0]['msg']) + BColors.ENDC)
        print(BColors.BOLD + "Проблемный ключ:" + BColors.ENDC, repr(e.errors()[0]['loc']))
        print(BColors.BOLD + "Входящее значение:" + BColors.ENDC, repr(e.errors()[0]['input']))
        print(BColors.BOLD + "Полный текст ошибки:" + BColors.ENDC, repr(e.errors()))
        print(BColors.WARNING + "__________</ReportValidate>__________" + BColors.ENDC)


class ResponseErrorRU:
    blank = ['Значение не должно быть пустым.']
    not_valid = ['Значение недопустимо.']
    not_valid_email = ['Значение адреса электронной почты недопустимо.']
    long_email = ['Значение слишком длинное. Должно быть равно 320 символам или меньше.']
    long_name = ['Значение слишком длинное. Должно быть равно 60 символам или меньше.']
    expected = ['Это поле не ожидалось.']
    choice_invalid = ['Выбранный вариант недопустим.']

class ResponseErrorEN:
    blank = ['This value should not be blank.']
    not_valid = ['This value is not valid.']
    not_valid_email = ['This value is not a valid email address.']
    long_email = ['This value is too long. It should have 320 characters or less.']
    long_name = ['This value is too long. It should have 60 characters or less.']
    expected = ['This field was not expected.']
    choice_invalid = ['The selected choice is invalid.']