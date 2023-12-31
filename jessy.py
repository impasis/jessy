from datetime import date
import asyncio
import g4f
import random
import sys

_providers = [
    g4f.Provider.You,
]


async def run_provider(provider: g4f.Provider.BaseProvider, message):
    try:
        response = await g4f.ChatCompletion.create_async(
            model=g4f.models.default,
            messages=[{"role": "user", "content": message}],
            provider=provider,
        )
        print(response)
    except Exception as e:
        print(f"{provider.__name__}:", e)


async def run_all(message):
    calls = [
        run_provider(provider, message) for provider in _providers
    ]
    await asyncio.gather(*calls)


def summer():
    now = date.today()
    summer_start = date(now.year, 6, 1)
    if now > summer_start:
        summer_start = date(now.year + 1, 6, 1)
    days = (summer_start - now).days

    print(f"До начала лета осталось {days} дней.")


def new_year():
    now = date.today()
    new = date(now.year + 1, 1, 1)
    days = (new - now).days

    print(f"До Нового года осталось {days} дней.")


def calc(__expr):
    all_ = "1234567890-+*()/%"

    for el in __expr:
        if el not in all_:
            return "Наш калькулятор не поддерживает такие операции"

    try:
        return eval(__expr)
    except:
        return "Error"


def RPS():
    try:
        print("Если вы хотите выйти, то напиши !exit")
        n = int(input("До скольких побед играем? "))
        counter = 0
        rps = ["камень", "ножницы", "бумага"]
        bot_wins = 0
        player_wins = 0

        while counter < n:
            choice = input().lower()
            bot_choice = random.choice(rps)

            if choice in rps:
                if choice == "ножницы" and bot_choice == "камень":
                    bot_wins += 1
                    print("Победила Джесси!")
                    print(f"Счет - {player_wins} : {bot_wins}")

                elif choice == "ножницы" and bot_choice == "бумага":
                    player_wins += 1
                    print(f"Победил(а) {name}!")
                    print(f"Счет - {player_wins} : {bot_wins}")

                elif choice == "камень" and bot_choice == "бумага":
                    bot_wins += 1
                    print("Победила Джесси!")
                    print(f"Счет - {player_wins} : {bot_wins}")

                elif choice == "камень" and bot_choice == "ножницы":
                    player_wins += 1
                    print(f"Победил(а) {name}!")
                    print(f"Счет - {player_wins} : {bot_wins}")

                elif choice == "бумага" and bot_choice == "ножницы":
                    bot_wins += 1
                    print("Победила Джесси!")
                    print(f"Счет - {player_wins} : {bot_wins}")

                elif choice == "бумага" and bot_choice == "камень":
                    player_wins += 1
                    print(f"Победил(а) {name}!")
                    print(f"Счет - {player_wins} : {bot_wins}")

                else:
                    print("Ничья!")
                    print(f"Счет - {player_wins} : {bot_wins}")

                counter += 1

            else:
                print("Error")

        if player_wins < bot_wins:
            print("Джесси одолела тебя!")
            print(f"Счет - {player_wins} : {bot_wins}")
        elif player_wins > bot_wins:
            print("Ты все-таки победил Джесси!")
            print(f"Счет - {player_wins} : {bot_wins}")
        else:
            print("Ничья!")
            print(f"Счет - {player_wins} : {bot_wins}")

    except ValueError:
        print("Error")


name = input('Привет! Меня зовут Джесси, а как зовут тебя? ')
print("приятно познокомиться,", name)
print('''мой создатель запрограммировал меня на следующие функции:
1. Калькулятор: \"!calc\"
2. Поговори со мной: \"!dialog\" и ваши фразы, вводить по одной фразе! можно его прервать фразой \"пока\"
3. Рандомный элемент из введенного списка: \"!random\"
4. Рандомное чило от n до m: \"!randint\" вывожу любое число от S до I, которые вы введёте
5. Завершение программы: \"!exit\"
6. Камень ножницы бумага: \"!RPS\"
7. Сколько дней до Нового Года: \"!new_year"
9. Сколько дней до Лета: \"!summer"
''')

while True:
    cmd = input("$ ")

    if cmd == "!calc":
        expr = input()
        print(calc(expr))

    elif cmd == "!dialog":
        while True:
            mes = input()
            if mes == "пока":
                break
            asyncio.run(run_all(mes))

    elif cmd == "!random":
        lst = input().split()
        print(random.choice(lst))

    elif cmd == "!randint":
        try:
            s, i = map(int, input().split())
            print(random.randint(s, i))
        except ValueError:
            print("Error")

    elif cmd == "!exit":
        sys.exit()

    elif cmd == "!RPS":
        RPS()

    elif cmd == "!summer":
        summer()

    elif cmd == "!new_year":
        new_year()
