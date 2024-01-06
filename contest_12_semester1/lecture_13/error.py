

try:
    i = int(input())
    print(1/i)
except ValueError as e:
    print('ERROR', e)
except ZeroDivisionError as e:
    print('ERROR2', e)
except Exception as e:
    print('ERROR3', e)
finally:
    print('Всегда будет срабатывать, не важно есть ошибка или нет')
