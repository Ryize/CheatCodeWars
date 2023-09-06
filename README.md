# cheatCodeWars

Позволяет автоматически решать задания на CodeWars по заранее созданому конфигу.

## Прежде всего:

> Установите Python (если он не установлен)<br>
> [Скачать Python3](https://www.python.org/downloads/)

Клонируйте репозиторий и перейдите в установленную папку:
```
git clone https://github.com/Ryize/cheatCodeWars.git
cd cheatCodeWars
```

Установите requirements:
```
pip3 install -r requirements.txt
```

Добавьте конфиг в формате:
```
https://www.codewars.com/kata/50654ddff44f800200000004/train/python
def multiply(a, b):
    return a * b
[!NEXT!]
```
Где:
1 строка - ссылка на кату;
Далее верный код;
После кода - [!NEXT!].
Пустые строки не требуется. 
Пример конфига:
```
https://www.codewars.com/kata/50654ddff44f800200000004/train/python
def multiply(a, b):
    return a * b
[!NEXT!]
https://www.codewars.com/kata/583203e6eb35d7980400002a/train/python
def count_smileys(arr):
    result = []
    for i in arr:
        if len(i) == 2 and i[0] in list(';:') and i[-1] in list(')D'):
            result.append(i)
        elif len(i) > 2 and i[0] in list(';:') and i[1] in list("-~") and i[-1] in list(")D"):
            result.append(i)
    return len(result)
[!NEXT!]
https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python
def high(x):
    score_letter = {value: key+1 for key, value in enumerate(__import__('string').ascii_lowercase)}
    return max(x.split(), key=lambda word: sum([score_letter[i] for i in word]))
```

> Технологии, использованные в проекте: Python3, PyAutoGui
