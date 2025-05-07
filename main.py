import questionary
import subprocess
import random
def priem():
    # Ввод порта
    port_select = questionary.confirm("Вы хотите ввести порт сами или его сгенерирует программа за вас?").ask()
    if port_select == True:
        try:
            port = int(questionary.text("Введите порт:").ask())
            if port > 65535:
                print("Порт превышает максимальное число, введите другой")
                port = int(questionary.text("Введите порт:").ask())
        except ValueError:
            print("Введите число, а не текст")
            port = int(questionary.text("Введите порт:").ask())
            if port > 65535:
                print("Порт превышает максимальное число, введите другой")
                port = int(questionary.text("Введите порт:").ask())
    else:
        port = random.randint(1025, 65535)
    
    header = 1024
    try:
        buffer = int(questionary.text("Введите кол-во байтов, которое будет передаваться за один раз").ask())
    except ValueError:
        print("Введите число, а не текст")
        buffer = int(questionary.text("Введите кол-во байтов, которое будет передаваться за один раз").ask())
    
    if port_select != True:
        print('Сервер находится на порту', port)
    
    print("Сервер работает только в локальной сети! Для передачи данных по интернету воспользуйтесь программами типа Radmin Vpn(НЕ РЕКЛАМА!)")
    subprocess.call(['python', 'core.py', 'server', '--buff', str(buffer), '--header', str(header), '--port', str(port)])

def otpravka():
    ip = questionary.text("Введите IPv4 адрес").ask()
    try:
        port = int(questionary.text("Введите порт:").ask())
    except ValueError:
        print("Введите число, а не текст")
        port = int(questionary.text("Введите порт:").ask())
    path = questionary.text("Введите путь до файла, который хотите передать").ask()
    if path[0] == path[-0] == '"':
        path = path[1:-1]
    subprocess.call(['python', 'core.py', 'client', '--ip', ip, '--port', str(port), '--path', str(path), '--header', '1024'])



# Выбор действия
select = questionary.select(
    "Что вы хотите сделать?",
    choices=["Принять файл", "Отправить файл"]
).ask()


if select == "Принять файл":
    priem()
elif select == "Отправить файл":
    otpravka()