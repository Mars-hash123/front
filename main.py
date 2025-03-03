
import time
import sys

def auto_type(text, speed):
    time.sleep(2)  # Задержка перед началом печатания (2 секунды)
    for char in text:
        sys.stdout.write(char)  # Печатает символ
        sys.stdout.flush()       # Сразу выводит
        time.sleep(speed)        # Задержка между символами

if __name__ == "__main__":
    # Текст, который будет печататься
    text = "Привет, это пример автопечатания текста!"
    
    # Скорость печатания (меньше - быстрее)
    speed = 0.1  # Задержка в секундах

    auto_type(text, speed)
