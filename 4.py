class NegativeValueException(Exception):
    pass

def check_name(name):
    if len(name)>10:
        raise NegativeValueException('Длина более 10 символов')
    else:
        print('Успешеая регистрация')

if __name__ == '__main__':
    name='123456788889203'
    check_name(name)