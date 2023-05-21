import platform
import pyautogui
import time
import random
import webbrowser

COEFFICIENT_X = 0.1
COEFFICIENT_Y = 1.49

_BASE_DIR = 'img_for_search'
ATTEMPT = f'{_BASE_DIR}/attempt.png'
FOR_CURSOR = f'{_BASE_DIR}/for_cursor.png'

TRANSLITE = {
    'Q': 'Й', 'W': 'Ц', 'E': 'У', 'R': 'К', 'T': 'Е',
    'U': 'Г', 'I': 'Ш', 'O': 'Щ', 'P': 'З', 'Y': 'Н',
    '{': 'Х', '}': 'Ъ', 'A': 'Ф', 'S': 'Ы', 'D': 'В',
    'G': 'П', 'H': 'Р', 'J': 'О', 'K': 'Л', 'F': 'А',
    'L': 'Д', ':': 'Ж', '"': 'Э', 'Z': 'Я', 'X': 'Ч',
    'V': 'М', 'B': 'И', 'N': 'Т', 'M': 'Ь', 'C': 'С',
    '<': 'Б', '>': 'Ю', 'q': 'й', 'w': 'ц',
    'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'e': 'у',
    'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х', ']': 'ъ',
    's': 'ы', 'd': 'в', 'f': 'а', 'g': 'п', 'a': 'ф',
    'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д', ';': 'ж',
    'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', "'": 'э',
    'b': 'и', 'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю',
}


def open_codewars_url(url):
    webbrowser.open_new_tab(url)
    time.sleep(5)
    pyautogui.moveTo([200, 550], duration=random.randint(1, 3))
    pyautogui.click()
    pyautogui.scroll(-1000)


open_codewars_url('https://www.codewars.com/kata/50654ddff44f800200000004/train/python')
while True:
    start = pyautogui.locateCenterOnScreen(ATTEMPT, grayscale=False)
    if not start:
        continue
    ATTEMPT_X = start.x
    ATTEMPT_Y = start.y
    if platform.system() == 'Darwin':
        ATTEMPT_X //= 2
        ATTEMPT_Y //= 2
    break

SCREEN_SIZE_X, SCREEN_SIZE_Y = pyautogui.size()


def send_for_execution():
    """
    Отправляет код на проверку.

    Ищет и нажимает на кнопку ATTEMPT.

    :return: None
    """
    pyautogui.moveTo([ATTEMPT_X, ATTEMPT_Y], duration=random.randint(1, 3))
    pyautogui.click()
    pyautogui.moveTo(
        [
            ATTEMPT_X - ATTEMPT_X * COEFFICIENT_X, ATTEMPT_Y // COEFFICIENT_Y
        ],
        duration=random.randint(1, 2))
    pyautogui.click()
    pyautogui.moveTo([
        random.randint(29, SCREEN_SIZE_X - 15),
        random.randint(39, SCREEN_SIZE_Y - 15)
    ],
        duration=random.randint(1, 3))


def _change_language():
    if platform.system() == 'Darwin':
        pyautogui.hotkey('command', 'space')
    else:
        pyautogui.hotkey('alt', 'shift')


def _dial_code(code):
    code = list(code)
    LANGUAGE = 0  # 0 - en, 1 - ru

    for k, i in enumerate(code):
        if i == '\n':
            pyautogui.hotkey('option', 'enter')
            continue
        if i in TRANSLITE.values():
            if LANGUAGE != 1:
                LANGUAGE = 1
                _change_language()
            i = list(TRANSLITE.keys())[list(TRANSLITE.values()).index(i)]
        else:
            if LANGUAGE != 0:
                LANGUAGE = 0
                _change_language()
        pyautogui.typewrite(i, interval=0.18 + random.randint(-5, 5) / 100)


def dial_code():
    with open('config.txt', 'r', encoding='utf-8') as file:
        text = file.read().split('[!NEXT!]')
        number = 0
        print(f'Конфиг на {len(text)} кат\n')
        time_all = 0
        for kata in text:
            kata_start_time = time.time()
            url = kata.split('\n')[0]
            code = '\n'.join(kata.split('\n')[1:])
            if not url:
                url = kata.split('\n')[1]
                code = '\n'.join(kata.split('\n')[2:])
            preparation_to_write(url)
            _smart_code_writer(code)
            kata_end_time = time.time()
            number += 1
            sleep_time = int((kata_end_time - kata_start_time) * 2)
            time_all += int(kata_end_time - kata_start_time)
            print()
            print(
                f'Завершена {number} ката ({url}) за {int(kata_end_time - kata_start_time)} секунд.\nЗасыпаю на: {sleep_time} секунд')
            time.sleep(sleep_time)
    print(f'Конфиг успешно пройден! Потрачено времени: {time_all}')


def _smart_code_writer(code):
    time_start_sleep = time.time()
    time_start_attempt = time.time()
    for code_str in code.split('\n'):
        _dial_code(code_str + '\n')
        if time.time() - time_start_sleep > random.randint(25, 30):
            time.sleep(5 + random.randint(-2, 15))
            time_start_sleep = time.time()
        if time.time() - time_start_attempt > random.randint(50, 60):
            send_for_execution()
            pyautogui.hotkey('option', 'enter')
            time_start_attempt = time.time()
    send_for_execution()
    send_for_execution()


def preparation_to_write(url):
    open_codewars_url(url)
    send_for_execution()
    clear_code_field()


def clear_code_field():
    if platform.system() == 'Darwin':
        pyautogui.hotkey('command', 'a')
    else:
        pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('backspace')


if __name__ == '__main__':
    pyautogui.FAILSAFE = False
    dial_code()
