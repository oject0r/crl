import os
import os.path
import time
import glob
import random
import pygame.mixer
import pygame
import colorama
import pickle



money_value = 21999
room = "InRoom"
room_select1=0
room_select2=0
multiply_select1="0"
have_food=0
have_water=0
have_lapsha=0
have_phone=0
have_pc=0
have_coffeemaker=0
used_bebra = False
skipLoadingAndAntiCheat = 756738409086713906
stats = [
    money_value,
    room,
    room_select1,
    have_food,
    have_water,
    have_lapsha,
    have_phone,
    have_pc,
    have_coffeemaker,
    skipLoadingAndAntiCheat,
    ]
firstTimeAtWork = True
def DevMode(secretline):
    if secretline == "NDEKFCDL":
        room = "InPhone_Terminal"
    else:
        print('Invalid DevMode Code! Game gonna crash.')
        input()
        quit()
def s(sleepTimeInSec):
    time.sleep(sleepTimeInSec)
# money_value, room, room_select1, have_food, have_water, have_lapsha, have_phone, have_pc, have_coffeemaker, skipLoadingAndAntiCheat,

def save():
    stats = [
    money_value,
    room,
    have_food,
    have_water,
    have_lapsha,
    have_phone,
    have_pc,
    have_coffeemaker,
    skipLoadingAndAntiCheat,
    ]
    with open('./savefiles/moneyvalue.txt', 'w') as f:
        f.write(str(money_value))
    with open('./savefiles/room.txt', 'w') as f:
        f.write(str(room))
    with open('./savefiles/have_food.txt', 'w') as f:
        f.write(str(have_food))
    with open('./savefiles/have_water.txt', 'w') as f:
        f.write(str(have_water))
    with open('./savefiles/have_doshirak.txt', 'w') as f:
        f.write(str(have_lapsha))
    with open('./savefiles/have_phone.txt', 'w') as f:
        f.write(str(have_phone))
pygame.mixer.init()
def Loading():
    print('Добро пожаловать в игру под названием...')
    time.sleep(5)
    print('КИБЕР РЕАЛЬНОСТЬ (Текстовая Версия)')
    time.sleep(5)
    input()
    print('Чтобы начать игру, нажмите Enter...')
    input()
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Но для начала нам нужно выполнить загрузку...')
    time.sleep(2)
    print('Загрузка начата!')
    os.system('cls' if os.name == 'nt' else 'clear')
    print('1%')
    time.sleep(random.randint(1,4))
    os.system('cls' if os.name == 'nt' else 'clear')
    print('17%')
    time.sleep(random.randint(6,9))
    os.system('cls' if os.name == 'nt' else 'clear')
    print('31%')
    time.sleep(random.randint(6,9))
    os.system('cls' if os.name == 'nt' else 'clear')
    print('82%')
    time.sleep(random.randint(6,9))
    os.system('cls' if os.name == 'nt' else 'clear')
    print('100%')
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Проверяем обновления с серверов.')
    time.sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Проверяем обновления с серверов..')
    time.sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Проверяем обновления с серверов...')
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(0.1)
    print('Проверяем обновления с серверов.')
    time.sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Проверяем обновления с серверов..')
    time.sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Проверяем обновления с серверов...')
    time.sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Обновлений не найдено! Можно играть...')
    input()


def InGameDevStart_OldForHistoryJustNothingDontTouchThisShitAhaahhahah():
    print('"Добро пожаловать!" Было написано на этой табличке. На самом деле я не знаю где я. Я заснул дома, у себя на кровати, а сейчас в какой-то комнате...')
    print('Я увидел дверь и выбежал оттуда, но тут...')
    print('Моя комната! Представляете? Я так и не понял что произошло.')
    print('Я ещё никому не рассказывал об этом деле.')
    print()
def CheatFind():
    print(stats)
    print('Здравствуйте! Перед игрой нам необходимо сканировать ваш компьютер на читы. (В читы также входят такие программы как: Cheat Engine версии 7.3 и более, другие утилиты.)')
    print('Ваш процессор и оперативную память (2-3 ГБ) может немного "бомбить" когда начнётся проверка. (БУДЬТЕ АККУРАТНЫ НА СЛАБЫХ ПК!!!)')
    input()
    print('Проверка начата!')
    myList = []
    for i in range(9211):
        myList.append(random.randint(0, 10000000000))
    max_el=myList[0]
    max_el_num=0
    for a in range(len(myList)):
        if myList[a]>max_el:
            max_el=myList[a]
            max_el_num=a
    os.chdir("C:\Program Files\Cheat Engine 7.3")
    for file in glob.glob("lua53-64.dll"):
        print('У вас найдены читы! Просьба: удалите их. Иначе игра не запустится.')
        input()
        quit()

print('sdfsdfsdf')
room = "InRoom"
while True: 
    if room == "InRoom":
     pygame.mixer.music.load('HomeMelody.mp3')
     pygame.mixer.music.play(5000)
     print(stats)
     os.system('cls' if os.name == 'nt' else 'clear')
     print(str('Я у себя дома. Ничего необычного. В правом углу стоит стул, на котором, весит одежда'))
     print('Можно выйти, а можно пойти на кухню. Куда мне пойти? 1 - Выйти, 2 - Пойти на кухню. 3 - Воспользоваться телефоном (Нужен смартфон), 4 - Сохраниться, 5 - Загрузить сохранение.')
     room_select1 = int(input('Ваш выбор: '))
     if room_select1 == 1:
         room = "Outside"
     if room_select1 == 2:
         room = "Kitchen"
     if room_select1 == 756738409086713906:
         money_value = money_value + 500000
         print(money_value)
         input()
     if room_select1 == 3:
         room="InPhone"
     if room_select1 == 4:
         save()
         stats = [
            money_value,
            room,
            room_select1,
            have_food,
            have_water,
            have_lapsha,
            have_phone,
            have_pc,
            have_coffeemaker,
            skipLoadingAndAntiCheat,
         ]
     if room_select1 == 5:
         with open('./savefiles/moneyvalue.txt') as f:
            money_value = str(f.read())
         with open('./savefiles/room.txt') as f:
             room = str(f.read())
         with open('./savefiles/have_phone.txt') as f:
             have_phone = str(f.read())
         with open('./savefiles/have_water.txt') as f:
             have_water = str(f.read())
         with open('./savefiles/have_food.txt') as f:
             have_food = str(f.read())
         with open('./savefiles/have_doshirak.txt') as f:
             have_lapsha = str(f.read())
         money_value = int(money_value)
         have_phone = int(have_phone)
         have_water = int(have_water)
         have_food = int(have_food)
         have_lapsha = int(have_lapsha)
    if room == "Outside":
        os.system('cls' if os.name == 'nt' else 'clear')
        pygame.mixer.music.load('OutsideMelody.mp3')
        pygame.mixer.music.play(5000)
        print('Вы вышли на улицу. Куда вам пойти?')
        print(str("1 - Сходить в магазин, 2 - Пойти домой, 3 - Сходить погулять (БУДЕТ В 1.1), 4 - Использовать телефон..."))
        room_select2 = int(input('Ваш выбор: '))
    if room_select2 == 1:
        room = "Store"
    if room_select2 == 2:
        room = "InRoom"
    if room_select2 == 9223372036854775807:
        room = "Stroll"
    if room_select2==4:
        room= "InPhone"

    if room == "Stroll":
        print('Вы пошли на прогулку.')
        print('Вы увидели парк развлечений. Пойдёте, ли вы туда?')
        print('1 - Да, 2 - Нет')
        select1 = int(input('Ваш выбор: '))
        if select1 == 1:
            room = "AtPark"
    if room == "AtPark":
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Вы пришли в Парк Развлечений. Что будете делать?')
        print('1 - Скатиться с горки (10 раз - 50 рублей), 2 - Пойти на батут (5 Минут - 50 рублей), 3 - Пойти в верёвочный парк (1 Трасса - 50 рублей), 4 - Уйти отсюда.')
        select2 = int(input('Ваш выбор: '))
        if select2 == 1:
            time.sleep(10)
            print('Вы скатились с горки 10 раз.')
            print('К вам подошёл билетёр. Он спросил вас, не хотите, ли вы работать у нас?')
            print('За сколько рублей вы готовы работать у них? (Зарплата раз в минуту, первая плата без ожидания и задержки)')
            how_much_got_money_select = int(input('Выбор зарплаты (До 160к в минуту): '))
            if how_much_got_money_select > 160000:
                print('Вы выбрали слишком большую плату!')
                print('Ваша зарплата будет 160к в минуту.')
                how_much_got_money_select = 160000
            print('Вы сказали, что готовы работать у них за ', how_much_got_money_select, ' рублей в минуту')
            print('Они согласились за такую плату.')
            how_much_got_on_work = how_much_got_money_select - 20000
            print('Но 20000 рублей снимается как комиссия.')
            room = "AtWork"
    if room == "AtWork":
        if firstTimeAtWork == True:
            money_value = money_value + how_much_got_on_work
            print('Вы получили первую плату в размере: ', how_much_got_money_select, 'Но с комиссией 20 тысяч рублей. Ваша итоговая зарплата: ', how_much_got_on_work, 'Ваш баланс: ', money_value)
            firstTimeAtWork = False
        print('Вы пришли на работу. Напишите сколько вы будете работать (в минутах). Но вы будете ждать это время без игры. 0 - Для выхода обратно')
        work_time = int(input('Введите время работы (в минутах): '))
        if work_time != 0:
            how_much_i_got = work_time * 140000
            work_time = work_time * 60
            money_value = money_value + how_much_i_got
            print('Ваш баланс к окончанию работы составит: ', money_value)
            time.sleep(work_time)
            print('Ваш баланс: ', money_value, ' рублей')
            room = "Outside"
        else:
            room="Outside"

    if room=="InPhone":
        pygame.mixer.music.load('InPhoneMelody.mp3')
        pygame.mixer.music.play(5000)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Вы зашли в телефон...')
        time.sleep(3)
        print('Он попривествовал вас своей заставкой SamSuka (R)')
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Загрузка...')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Ваш телефон загрузился...')
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('У вас установлено 3 приложения. В какое зайти?')
        print('1. Гугл (1.1), 2. Терминал, 3. Телефон.')
        select3 = int(input('Ваш выбор: '))
        if select3 == 1:
            print('Жди 1.1 >:(')
            input()
            print('Ваш телефон выключился и вы решили включить его заново...')
            room = "InPhone"
        if select3 == 2:
            room = "InPhone_Terminal"
        if select3 == 3:
            print('Вы решили кому-то позвонить...')
            print('Упс! У вас нет сим-карты чтобы позвонить кому-либо. В дальнейших планах, я добавлю возможность покупать сим-карту')
            input()
            room = "Outside"
    if room=="InPhone_Terminal":
        pygame.mixer.music.load('HackerTerminalMelody.mp3')
        pygame.mixer.music.play(5000)
        print('Добро пожаловать в хакерский терминал... введите переменную app и команду Quit ( app.Quit() ), чтобы выйти...')
        command_cmd = input('Введите команду: ')
        if command_cmd == "music:surprise_genocide":
            pygame.mixer.music.load('surprise_genocide.mp3')
            pygame.mixer.music.play()
            print('Sans Fucked You...')
            input()
            quit()
        if command_cmd == "bebra.use()":
            if used_bebra == False:
                print('Вы настоящий любитель бебр! Вы нашли 500 рублей!')
                money_value = money_value + 500
                used_bebra = True
                print('Ваш баланс: ', money_value)
                input()
            else:
                print('В очередной раз вы понюхали смачной бебры...')
                input()
        if command_cmd == 'execute("hack.exe", +, args:"funcInTerminalArg?bankhack=true&nd=true&secretcode=KFC")':
            print('\033[32mWelcome.')
            print('For start hack we need to check Args you used in CMD')
            s(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Arg detected: bankhack=true')
            how_many_money_to_hack = int(input('Enter the number (1000$ = 0.1 second): '))
            s(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Arg detected: nd=true')
            print("Narpal's Anti-FCB (v89.6stable (11 October 2021 year)): Turned On")
            s(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            how_many_time_to_hack = how_many_money_to_hack / 10000
            print('Hack use will be get: ', how_many_time_to_hack, 'You will get: ', how_many_money_to_hack)
            bnkhckex = int(input("1 - Ok, 2 - Cancel: "))
            if bnkhckex == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Hack started!')
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Hacking...')
                s(how_many_time_to_hack)
                money_value = money_value + how_many_money_to_hack
                print('Хак окончен. Ваш нынешний баланс: ', money_value)
                input()
            if bnkhckex == 2:
                print('Why ;(')
        if command_cmd == 'hack':
            print('\033[32mWelcome.')
            print('Looks like you started programm without args! Args will be set automaticly.')
            print('What do you want to choose?')
            print('1 - Money')
            user_select_hackexe = int(input('Hacks: '))

        

        if command_cmd == "app.Quit()":
            room = "InPhone"
        

    if room == "Kitchen":
        print('Вы пошли на кухню...')
        time.sleep(3)
        print('Но вы вспомнили, то что у вас нету кухни.')
        input()
        room="InRoom"
    if room == "Store":
         os.system('cls' if os.name == 'nt' else 'clear')
         pygame.mixer.music.load('MagazineMelody.mp3')
         pygame.mixer.music.play(5000)
         print('Вы пришли в магазин. У вас: ', money_value, " рублей.")
         print('Что купите?')
         print('"ПРОДУКТОВЫЙ МАГАЗИН": П1 - Купить еды (109 рублей), П2 - Купить воды (39 рублей), П3 - Купить Доширак/Роллтон (30/15 рублей)')
         print('"МАГАЗИН ТЕХНИКИ": Т1 - Купить смартфон (20599 рублей), T2 - Собрать ПК (169999 рублей) (БУДЕТ ДОБАВЛЕНО В 1.1 ВЕРСИИ), T3 - Купить Кофемашину (T31 - 27999/T32 - 130000) (БУДЕТ ДОБАВЛЕНО В 1.1 ВЕРСИИ)')
         print('1 - Выйти на улицу.')
         multiply_select1 = input('Ваш выбор: ')

         if multiply_select1 == "П1":
             if money_value < 109:
                 print('У вас не хватает денег!')
                 input()
                 room = "Store"
             else:
                 money_value = money_value - 109
                 print('Вы купили 1 порцию еды! Ваш нынешний баланс: ', money_value, ' рублей!')
                 have_food = have_food + 1
                 print('Сейчас у вас порций еды: ', have_food)
                 input()
         if multiply_select1 == "П2":
             if money_value < 39:
                 print('У вас не хватает денег!')
                 input()
                 room = "Store"
             else:
                 money_value = money_value - 39
                 print('Вы купили бутылку воды! Ваш нынешний баланс: ', money_value, ' рублей!')
                 have_water = have_water + 1
                 print('Сейчас у вас ', have_water, ' бутылок воды')
                 input()
        
         if multiply_select1 == "П3":
             if money_value < 109:
                 print('У вас не хватает денег!')
                 input()
                 room = "Store"
             else:
                 money_value = money_value - 109
                 print('Вы купили 1 порцию доширака! Ваш нынешний баланс: ', money_value, ' рублей!')
                 have_lapsha = have_lapsha + 1
                 print('Сейчас у вас порций еды: ', have_lapsha)
                 input()
         if multiply_select1 == "Т1":
             if have_phone == 0:
                if money_value < 20599:
                    print('У вас не хватает денег!')
                    input()
                    room = "Store"
                else:
                    money_value = money_value - 20599
                    print('Вы купили Смартфон! Ваш нынешний баланс: ', money_value, ' рублей!')
                    have_phone = have_phone + 1
                    print('Сейчас у вас есть смартфон. Для того чтобы его включить, выйдите на улицу и выберите вариант 4.')
                    input()
             else:
                print('У вас уже есть смартфон!')
                input()
            
         if multiply_select1 == "1":
             room = "Outside"

