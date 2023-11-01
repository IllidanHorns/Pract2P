import sys
import json
import csv
import os

Nickname = ""
Finish = ""
PlayerPosition = 1
Monsters = {"Octopus": 100}
Guns = {"gun1": 30, "gun2": 100}
PlayerInventory = []
OctopusLife = 1;
ChekToChek = [0,0,0,0,0,0]
Letters = []
CurrentRoomSubjects4 = ["Oskolki ot probirok", "Bochka s vodoi", "Bochka s toplivom", "Kluch"]
CurrentRoomSubjects5 = ["Uskoritel G6", "Podushka", "Boevaiy vintovka", "Stolik"]
CurrentRoomSubjects1 = ["Pismo iz komnati №1", "Kosmicheskiy pistolet"]
CurrentRoomSubjects2 = ["Vendikator"]
CurrentRoomSubjects3 = ["Pin-code"]

PinCod = "777999 - код от корабля"
LetterStart = "Кажется это конец... последние минуты жизни я проведу на инопланетном корабле. Зря я самонадеянно \n"\
              "попытался помародерствовать на корабле этого ксеноса. \n"\
              "Последней надеждой был корабль, находяшийся в комнате №6. Но у меня нет к нему доступа. \n"\
              "Если кто-то читает сейчас эту записку, знай, что тебе потребуются: Pin-code от корабля, \n"\
              "kluch зажигания, топливо, а также Vendikator и uskoritel G6. Остерегайся, этот корабль \n"\
              "полон опасностей. По моим наблюдениям в комнате N2 находится форма жизни ранее еще не известная нам. \n"\
              "ОНО ОПАСНО! Оружие... Тебе нужно оружие ............"

def start():
    global  Nickname
    print("Хотите начать с последнего сохранения или начать новую игру (Сохранение или Новая игра)?")
    a = input()
    if a == "Сохранение":
        openjsoninf()
        print(f"Здравствуйте, {Nickname}")
    elif a == "Новая игра":
        Nickname = input("Введите свой никнейм на английском - ")
    else:
        print("Вы ввели данные неправильно!")
        start()
        return

def main ():
    if PlayerPosition == 2:
        Active2()
        return
    elif PlayerPosition == 6:
        Active6()
        return
    else:
        Active()
        return None

def save_csv():
    if os.path.isfile("output.csv") == False:
        zxc = open("output.csv", "w+")
        zxc.close()
    data = [
        {"name" : Nickname, "inventory" : PlayerInventory, "letters" : Letters, "monsterkill": OctopusLife, "ending" : Finish}
    ]
    fieldnames = ["name", "inventory", "letters", "monsterkill", "ending"]
    if fieldnames[0] in open("output.csv").read():
        with open("output.csv", "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=";")
            writer.writerows(data)
        exit()
    else:
        with open("output.csv", "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=";")
            writer.writeheader()
            writer.writerows(data)
        exit()



def save_json():
    last_user_data = {
        "name": Nickname,
        "inventory": PlayerInventory,
        "letters" : Letters,
        "last_position": PlayerPosition,
        "view": ChekToChek,
        "monsterkill": OctopusLife
    }
    with open("output.json", "w", encoding="utf-8") as file:
        json.dump(last_user_data, file,indent=4)
    return

def openjsoninf():
    global PlayerInventory, PlayerPosition, ChekToChek, OctopusLife, Letters, Nickname
    with open("output.json", "r") as file:
        data = json.load(file)
    Nickname = data["name"]
    PlayerInventory = data["inventory"]
    Letters = data["letters"]
    PlayerPosition = data["last_position"]
    ChekToChek = data["view"]
    OctopusLife = data["monsterkill"]
    return

def ErrorVvod():
    print("------------------------------------------")
    print("Похоже вы ввели данные неправильно!")
    print("------------------------------------------")
def Active():
    print("")
    print("------------------------------------------")
    print("Выберите действие: \n"
          "1. Пойти в другую комнату \n"
          "2. Осмотреться \n"
          "3. Взять предмет \n"
          "4. Посмотреть инвентарь \n"
          "5. Прочитать все записки \n"
          "6. Сохраниться")
    print("------------------------------------------")
    print("")
    UserChoice = 0
    try:
        UserChoice = int(input())
    except:
        ErrorVvod()
        main()
        return
    match UserChoice:
        case 1:
            RoomChoice()
            return
        case 2:
            Survey()
            return
        case 3:
            Take()
            return
        case 4:
            ChekInventory()
            return
        case 5:
            ReadLetters()
        case 1488:
            GodModForTest()
        case 6:
            save_json()
            sys.exit(0)
        case _:
            ErrorVvod()
            main()
            return
def GodModForTest():
    PlayerInventory.append("Vendikator")
    PlayerInventory.append("Kluch")
    PlayerInventory.append("Uskoritel G6")
    PlayerInventory.append("Bochka s toplivom")
    main()
    return
def Active2():
    print("")
    print("------------------------------------------")
    print("Выберите действие: \n"
          "1. Пойти в другую комнату \n"
          "2. Осмотреться \n"
          "3. Взять предмет \n"
          "4. Посмотреть инвентарь \n"
          "5. Прочитать все записки \n"
          "6. Убить существо \n"
          "7. Сохраниться")
    print("------------------------------------------")
    print("")
    UserChoice = 0
    try:
        UserChoice = int(input())
    except:
        ErrorVvod()
        main()
        return
    match UserChoice:
        case 1:
            RoomChoice()
        case 2:
            Survey()
        case 3:
            Take()
        case 4:
            ChekInventory()
        case 5:
            ReadLetters()
        case 6:
            KillOctupus()
        case 7:
            save_json()
            sys.exit(0)
        case _:
            ErrorVvod()
            main()
            return
def Active6():
    global Finish
    print("")
    print("------------------------------------------")
    print("Выберите действие: \n"
          "1. Пойти в другую комнату \n"
          "2. Осмотреться \n"
          "3. Взять предмет \n"
          "4. Посмотреть инвентарь \n"
          "5. Прочитать все записки \n"
          "6. Попытаться улететь на корабле \n"
          "7. Открыть люк корабля \n"
          "8. Сохранитья")
    print("------------------------------------------")
    print("")
    UserChoice = 0
    try:
        UserChoice = int(input())
    except:
        ErrorVvod()
        main()
        return 
    match UserChoice:
        case 1:
            RoomChoice()
            return
        case 2:
            Survey()
            return
        case 3:
            Take()
            return
        case 4:
            ChekInventory()
            return
        case 5:
            ReadLetters()
            return
        case 6:
            Cosmodjet()
            return
        case 7:
            print("Нарушена гермитезация корабля. Вас засосало в космос")
            print("В мертвы")
            print("Игра окончена")
            Finish = "Death"
            save_csv()
        case 8:
            save_json()
            sys.exit(0)
        case _:
            ErrorVvod()
            main()
            return
def Cosmodjet():
    global Finish
    print("Вы пытаетесь запустить космический корабль")
    print("Введите Pin-code от корабля - ")
    UserChoice = 0
    try:
        UserChoice = int(input())
    except:
        ErrorVvod()
        main()
        return
    if UserChoice == 777999:
        print("Вы ввели Pin-code правильно!")
        if ("Uskoritel G6" in PlayerInventory) and ("Bochka s toplivom" in PlayerInventory) and ("Vendikator" in PlayerInventory) and ("Kluch" in PlayerInventory):
            print("У вас есть все нужные детали. Корабль починен!")
            print("Вы смогли выбраться!")
            print("ИГРА ОКОНЧЕНА")
            Finish = "Win"
            save_csv()
        else:
            print("Вы не собрали все нужные детали")
            main()
            return
    else:
        print("Pin-code неверный!")
        main()
        return
def KillOctupus():
    global  OctopusLife
    global  Finish
    if ChekToChek[1] == 1:
        print("------------------------------------------")
        print("Вы пытаетесь убить существо. Количество здоровья существа - 100. Что-же кажется вам потребуется мощное оружие!")
        if OctopusLife == 0:
            print("Существо уже метртво")
            main()
            return
        else:
            if "Kosmicheskiy pistolet" in PlayerInventory and "Boevaiy vintovka" in PlayerInventory:
                print("Урон вашего лучшего оружия - %s" % Guns["gun2"])
                OctopusLife = 0
                print("Существо уничтожено!")
                main()
                return
            elif "Kosmicheskiy pistolet" not in PlayerInventory and "Boevaiy vintovka" not in PlayerInventory:
                print("У вас нет оружия")
                print("Существо жестоко расправилось с вами. Вы мертвы!")
                print("ИГРА ЗАКОНЧЕНА!")
                Finish = "Death"
                save_csv()
            elif "Boevaiy vintovka" in PlayerInventory:
                print("Урон вашего оружия - %s" % Guns["gun2"])
                OctopusLife = 0
                print("Существо уничтожено!")
                main()
                return
            elif "Kosmicheskiy pistolet" in PlayerInventory:
                print("Урон вашего оружия - %s" % Guns["gun1"])
                print("Урона вашего оружия не хватило!")
                print("Существо жестоко расправилось с вами. Вы мертвы!")
                print("ИГРА ОКОНЧЕНА!")
                Finish = "Death"
                save_csv()
    else:
        print("Сначала необходимо осмотреться!")
        main()
        return
def ReadLetters():
    print("------------------------------------------")
    print("Текст ваших записок:")
    if "Pismo iz komnati №1" in PlayerInventory and "Pin-code" in PlayerInventory:
        print(LetterStart)
        print(PinCod)
        main()
        return
    elif "Pismo iz komnati №1" in PlayerInventory:
        print(LetterStart)
        main()
        return
    elif "Pin-code" in PlayerInventory:
        print(PinCod)
        main()
        return
    else:
        print("У вас нет никаких писем")
        main()
def ChekInventory():
    global  PlayerInventory
    print("------------------------------------------")
    print("В вашем инвентаре - ")
    print(*PlayerInventory, sep = ", ")
    print("------------------------------------------")
    main()
    return
def Survey():
    match PlayerPosition:
        case 1:
            print("------------------------------------------")
            print("Комната круглой формы. Вокруг ничего кроме металла и 5 дверей. Но, стоп! Кажется \n"
                  "за одной металлических пластин стены вы видите странный предмет и, кажется, записку. \n"
                  "Странным предметом оказался kosmicheskiy pistolet. Но кто же оставил записку?")
            print("------------------------------------------")
            ChekToChek[0] = 1
            main()
            return
        case 2:
            print("------------------------------------------")
            print("О боже! Огромное создание, напоминающее осьминога находится прямо в центре комнаты. \n"
                  "Огромные щупальца, не видно глаз. Не понятно опасно ли ЭТО? В одном щупальце это \n"
                  "существо держит Vendikator (деталь, необходимая для починки корабля)")
            print("------------------------------------------")
            ChekToChek[1] = 1
            main()
            return
        case 3:
            print("------------------------------------------")
            print("Что? В углу комнаты вы видете инопланетный труп. Судя по форме это учёный. \n "
                  "Из его кармана торчит листок. Похоже вы нашли Pin-code.")
            print("------------------------------------------")
            ChekToChek[2] = 1
            main()
            return
        case 4:
            print("------------------------------------------")
            print("Комната похожа на лабораторию. Рядом с одной из стен стоит стол, полный всяких вещей. \n"
                  "В центре комнаты - стоит небольшая bochka s toplivom. Недалеко от стола вы замечаете \n"
                  "oskolki ot probirok и банку с неизвестной жидкостью. В углу комнаты валяется kluch.")
            print("------------------------------------------")
            ChekToChek[3] = 1
            main()
            return
        case 5:
            print("------------------------------------------")
            print("Комната напоминает место для отдыха. Маленький stolik, кровать причудливой формы, под кроватью \n"
                  "лежит странная вещь, напоминающая деталь от чего-то и boevaiy vintovka.")
            print("------------------------------------------")
            ChekToChek[4] = 1
            main()
            return
        case 6:
            print("------------------------------------------")
            print("В комнате вы видете небольшой коспический корабль. С виду он выглядит рабочим.")
            print("------------------------------------------")
            ChekToChek[5] = 1
            main()
            return
def Take():
    match PlayerPosition:
        case 1:
            if ChekToChek[0] == 1:
                global CurrentRoomSubjects1
                print("------------------------------------------")
                print("Вы можете взять: \n "
                      f"1. {CurrentRoomSubjects1[0]} \n"
                      f"2. {CurrentRoomSubjects1[1]} \n ")
                print("------------------------------------------")
                UserChoice = 0
                try:
                    UserChoice = int(input("Выберите что хотите взять"))
                except:
                    ErrorVvod()
                    Take()
                    return None
                if UserChoice == 1:
                    PlayerInventory.append(CurrentRoomSubjects1[0])
                    CurrentRoomSubjects1[0] = "Kusok jeleznoy plastini"
                    main()
                    return
                elif UserChoice == 2:
                    PlayerInventory.append(CurrentRoomSubjects1[1])
                    CurrentRoomSubjects1[1] = "Kusok jeleznoy plastini"
                    main()
                    return
                else:
                    ErrorVvod()
                    Take()
                    return
            else:
                print("Сначала нужно осмотреться, прежде брать что-то!")
                main()
                return
        case 2:
            if ChekToChek[1] == 1:
                global CurrentRoomSubjects2
                if OctopusLife == 0:
                    print("------------------------------------------")
                    print("Вы можете взять: \n "
                        f"1. {CurrentRoomSubjects2[0]}")
                    print("------------------------------------------")
                    UserChoice = 0
                    try:
                        UserChoice = int(input("Выберите что хотите взять "))
                        if UserChoice == 1:
                            PlayerInventory.append(CurrentRoomSubjects2[0])
                            CurrentRoomSubjects2[0] = "Kusok tela sushestva"
                            main()
                            return
                        else:
                            ErrorVvod()
                            Take()
                            return
                    except:
                        ErrorVvod()
                        Take()
                        return
                else:
                    print("Сначала убейте существо")
                    main()
                    return
            else:
                print("Сначала нужно осмотреться, прежде брать что-то!")
                main()
                return
        case 3:
            if ChekToChek[2] == 1:
                global CurrentRoomSubjects3
                print("------------------------------------------")
                print("Вы можете взять: \n "
                      f"1. {CurrentRoomSubjects3[0]}")
                print("------------------------------------------")
                UserChoice = 0
                try:
                    UserChoice = int(input("Выберите что хотите взять"))
                except:
                    ErrorVvod()
                    Take()
                    return
                if UserChoice == 1:
                    PlayerInventory.append(CurrentRoomSubjects3[0])
                    CurrentRoomSubjects3[0] = "Kusok ot odejdi ksenosa"
                    main()
                    return
                else:
                    ErrorVvod()
                    Take()
                    return
            else:
                print("Сначала нужно осмотреться, прежде брать что-то!")
                main()
                return
        case 5:
            if ChekToChek[4] == 1:
                global CurrentRoomSubjects5
                print("------------------------------------------")
                print("Вы можете взять: \n "
                      f"1. {CurrentRoomSubjects5[0]} \n"
                      f"2. {CurrentRoomSubjects5[1]} \n"
                      f"3. {CurrentRoomSubjects5[2]} \n"
                      f"4. {CurrentRoomSubjects5[3]} \n")
                print("------------------------------------------")
                UserChoice = 0
                try:
                    UserChoice = int(input("Выберите что хотите взять"))
                except:
                    print("Похоже вы ввели данные неправильно!")
                    Take()
                    return
                if UserChoice == 1:
                    PlayerInventory.append(CurrentRoomSubjects5[0])
                    CurrentRoomSubjects5[0] = "Pul' s pola"
                    main()
                    return
                if UserChoice == 2:
                    PlayerInventory.append(CurrentRoomSubjects5[1])
                    CurrentRoomSubjects5[1] = "Kusok metalicheskoy plastini"
                    main()
                    return
                if UserChoice == 3:
                    PlayerInventory.append(CurrentRoomSubjects5[2])
                    CurrentRoomSubjects5[2] = "Pul' s pola"
                    main()
                    return
                if UserChoice == 4:
                    PlayerInventory.append(CurrentRoomSubjects5[3])
                    CurrentRoomSubjects5[3] = "Kusok metalicheskoy plastini"
                    main()
                    return
                else:
                    ErrorVvod()
                    Take()
                    return
            else:
                print("Сначала нужно осмотреться, прежде брать что-то!")
                main()
                return
        case 4:
            if ChekToChek[3] == 1:
                global CurrentRoomSubjects4
                print("------------------------------------------")
                print("Вы можете взять: \n "
                      f"1. {CurrentRoomSubjects4[0]} \n"
                      f"2. {CurrentRoomSubjects4[1]} \n"
                      f"3. {CurrentRoomSubjects4[2]} \n"
                      f"4. {CurrentRoomSubjects4[3]} \n")
                print("------------------------------------------")
                UserChoice = 0
                try:
                    UserChoice = int(input("Выберите что хотите взять"))
                except:
                    print("Похоже вы ввели данные неправильно!")
                    Take()
                    return
                if UserChoice == 1:
                    PlayerInventory.append(CurrentRoomSubjects4[0])
                    CurrentRoomSubjects4[0] = "Oskolok ot probirki"
                    main()
                    return
                if UserChoice == 2:
                    PlayerInventory.append(CurrentRoomSubjects4[1])
                    CurrentRoomSubjects4[1] = "Neponiatniy predmet na stole"
                    main()
                    return
                if UserChoice == 3:
                    PlayerInventory.append(CurrentRoomSubjects4[2])
                    CurrentRoomSubjects4[2] = "Pul' s pola"
                    main()
                    return
                if UserChoice == 4:
                    PlayerInventory.append(CurrentRoomSubjects4[3])
                    CurrentRoomSubjects4[3] = "Kusok metalicheskoy plastini"
                    main()
                    return
                else:
                    ErrorVvod()
                    Take()
                    return
            else:
                print("Сначала нужно осмотреться, прежде брать что-то!")
                main()
                return
        case 6:
                print("------------------------------------------")
                print("Здесь нечего брать")
                print("------------------------------------------")
                main()
                return


def RoomChoice():
    UserChoice = 0
    match PlayerPosition:
        case 1:
            print("В какую из пяти комнат пойдёте?")
            try:
                UserChoice = int(input())
            except:
                ErrorVvod()
                main()
                return
            match (UserChoice):
                case 1:
                    print("Вы и так находитесь в комнате №1")
                    main()
                    return
                case 2:
                    Rooms(2)
                case 3:
                    Rooms(3)
                case 4:
                    Rooms(4)
                case 5:
                    Rooms(5)
                case 6:
                    Rooms(6)
                case _:
                    ErrorVvod()
                    RoomChoice()
                    return
        case 2:
            Rooms(1)
        case 3:
            Rooms(1)
        case 4:
            Rooms(1)
        case 5:
            Rooms(1)
        case 6:
            Rooms(1)
def Rooms(roomnumber):
    global PlayerPosition
    global Inventory

    match roomnumber:
        case 1:
            print("------------------------------------------")
            print("Вы оказались в Комнате №1")
            print("------------------------------------------")
            PlayerPosition = 1
            main()
            return
        case 2:
            print("------------------------------------------")
            print("Вы оказались в Комнате №2")
            print("------------------------------------------")
            PlayerPosition = 2
            main()
            return
        case 3:
            print("------------------------------------------")
            print("Вы оказались в Комнате №3")
            print("------------------------------------------")
            PlayerPosition = 3
            main()
            return
        case 4:
            print("------------------------------------------")
            print("Вы оказались в Комнате №4")
            print("------------------------------------------")
            PlayerPosition = 4
            main()
            return
        case 5:
            print("------------------------------------------")
            print("Вы оказались в Комнате №5")
            print("------------------------------------------")
            PlayerPosition = 5
            main()
            return
        case 6:
            print("------------------------------------------")
            print("Вы оказались в Комнате №6")
            print("------------------------------------------")
            PlayerPosition = 6
            main()
            return
        case _:
            ErrorVvod()
            main()
            return


start()
print("Итак... Вы оказались на коробле инопланетян. Вы стоите в большой круглой комнате (назовём её Комната №1). \n Вокруг вас "
      "вы не видете ничего кроме 5 дверей и металла, но стоит осмотреться получше. \n Кажется это ваш шанс выбраться от сюда. Вперёд!")
main()