import sys

PlayerPosition = 1
Monsters = {"Octopus": 100}
Guns = {"gun1": 30, "gun2": 100}
PlayerInventory = []
OctopusLife = 1;
ChekToChek = [0,0,0,0,0,0]
Letters = []
CurrentRoomSubjects4 = ["Осколки от пробирок", "Бочка с жижей", "Бочка с топливом", "Ключ"]
CurrentRoomSubjects5 = ["Ускоритель G6", "Подушка", "Боевая винтовка", "Столик"]
CurrentRoomSubjects1 = ["Письмо из комнаты №1", "Космический пистолет"]
CurrentRoomSubjects2 = ["Вендикатор"]
CurrentRoomSubjects3 = ["Пин-код"]

PinCod = "777999 - код от корабля"
LetterStart = "Кажется это конец... последние минуты жизни я проведу на инопланетном корабле. Зря я самонадеянно \n"\
              "попытался помародерствовать на корабле этого ксеноса. \n"\
              "Последней надеждой был корабль, находяшийся в комнате №6. Но у меня нет к нему доступа. \n"\
              "Если кто-то читает сейчас эту записку, знай, что тебе потребуются: пин-код от корабля, \n"\
              "ключ зажигания, топливо, а также вендикатор и ускоритель G6. Остерегайся, этот корабль \n"\
              "полон опасностей. По моим наблюдениям в комнате N2 находится форма жизни ранее еще не известная нам. \n"\
              "ОНО ОПАСНО! Оружие... Тебе нужно оружие ............"
def main ():
    if PlayerPosition == 2:
        Active2()
    elif PlayerPosition == 6:
        Active6()
    else:
        Active()
def Active():
    print("")
    print("------------------------------------------")
    print("Выберите действие: \n"
          "1. Пойти в другую комнату \n"
          "2. Осмотреться \n"
          "3. Взять предмет \n"
          "4. Посмотреть инвентарь \n"
          "5. Прочитать все записки")
    print("------------------------------------------")
    print("")
    UserChoice = 0
    try:
        UserChoice = int(input())
    except:
        ErrorVvod()
        main()
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
        case 1488:
            GodModForTest()
        case _:
            ErrorVvod()
            main()

def GodModForTest():
    PlayerInventory.append("Вендикатор")
    PlayerInventory.append("Ключ")
    PlayerInventory.append("Ускоритель G6")
    PlayerInventory.append("Бочка с топливом")
    main()

def Active2():
    print("")
    print("------------------------------------------")
    print("Выберите действие: \n"
          "1. Пойти в другую комнату \n"
          "2. Осмотреться \n"
          "3. Взять предмет \n"
          "4. Посмотреть инвентарь \n"
          "5. Прочитать все записки \n"
          "6. Убить существо")
    print("------------------------------------------")
    print("")
    UserChoice = 0
    try:
        UserChoice = int(input())
    except:
        ErrorVvod()
        main()
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
        case _:
            ErrorVvod()
            main()

def Active6():
    print("")
    print("------------------------------------------")
    print("Выберите действие: \n"
          "1. Пойти в другую комнату \n"
          "2. Осмотреться \n"
          "3. Взять предмет \n"
          "4. Посмотреть инвентарь \n"
          "5. Прочитать все записки \n"
          "6. Попытаться улететь на корабле \n"
          "7. Открыть люк корабля")
    print("------------------------------------------")
    print("")
    UserChoice = 0
    try:
        UserChoice = int(input())
    except:
        ErrorVvod()
        main()
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
            Cosmodjet()
        case 7:
            print("Нарушена гермитезация корабля. Вас засосало в космос")
            print("В мертвы")
            print("Игра окончена")
        case _:
            ErrorVvod()
            main()

def Cosmodjet():
    print("Вы пытаетесь запустить космический корабль")
    print("Введите пин-код от корабля - ")
    UserChoice = 0
    try:
        UserChoice = int(input())
    except:
        ErrorVvod()
        main()
    if UserChoice == 777999:
        print("Вы ввели пин-код правильно!")
        if "Ускоритель G6" in PlayerInventory and "Бочка с топливом" in PlayerInventory and "Вендикатор" in PlayerInventory and "Ключ" in PlayerInventory:
            print("У вас есть все нужные детали. Корабль починен!")
            print("Вы смогли выбраться!")
            print("ИГРА ОКОНЧЕНА")
            sys.exit()
        else:
            print("Вы не собрали все нужные детали")
            main()
    else:
        print("Пин-код неверный!")
        main()
def KillOctupus():
    global  OctopusLife
    if ChekToChek[1] == 1:
        print("------------------------------------------")
        print("Вы пытаетесь убить существо. Количество здоровья существа - 100. Что-же кажется вам потребуется мощное оружие!")
        if OctopusLife == 0:
            print("Существо уже метртво")
            main()
        else:
            if "Космический пистолет" in PlayerInventory and "Боевая винтовка" in PlayerInventory:
                print("Урон вашего лучшего оружия - %s" % Guns["gun2"])
                OctopusLife = 0
                print("Существо уничтожено!")
                main()
            elif "Космический пистолет" not in PlayerInventory and "Боевая винтовка" not in PlayerInventory:
                print("У вас нет оружия")
                print("Существо жестоко расправилось с вами. Вы мертвы!")
                print("ИГРА ЗАКОНЧЕНА!")
            elif "Боевая винтовка" in PlayerInventory:
                print("Урон вашего оружия - %s" % Guns["gun2"])
                OctopusLife = 0
                print("Существо уничтожено!")
                main()
            elif "Космический пистолет" in PlayerInventory:
                print("Урон вашего оружия - %s" % Guns["gun1"])
                print("Урона вашего оружия не хватило!")
                print("Существо жестоко расправилось с вами. Вы мертвы!")
    else:
        print("Сначала необходимо осмотреться!")
        main()
def ReadLetters():
    print("------------------------------------------")
    print("Текст ваших записок:")
    if "Письмо из комнаты №1" in PlayerInventory and "Пин-код" in PlayerInventory:
        print(LetterStart)
        print(PinCod)
        main()
    elif "Письмо из комнаты №1" in PlayerInventory:
        print(LetterStart)
        main()
    elif "Пин-код" in PlayerInventory:
        print(PinCod)
        main()
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
def ErrorVvod():
    print("------------------------------------------")
    print("Похоже вы ввели данные неправильно!")
    print("------------------------------------------")

def Survey():
    match PlayerPosition:
        case 1:
            print("------------------------------------------")
            print("Комната круглой формы. Вокруг ничего кроме металла и 5 дверей. Но, стоп! Кажется \n"
                  "за одной металлических пластин стены вы видите странный предмет и, кажется, записку. \n"
                  "Странным предметом оказался коспический пистолет. Но кто же оставил записку?")
            print("------------------------------------------")
            ChekToChek[0] = 1
            main()
        case 2:
            print("------------------------------------------")
            print("О боже! Огромное создание, напоминающее осьминога находится прямо в центре комнаты. \n"
                  "Огромные щупальца, не видно глаз. Не понятно опасно ли ЭТО? В одном щупальце это \n"
                  "существо держит вендикатор (деталь, необходимая для починки корабля)")
            print("------------------------------------------")
            ChekToChek[1] = 1
            main()
        case 3:
            print("------------------------------------------")
            print("Что? В углу комнаты вы видете инопланетный труп. Судя по форме это учёный. \n "
                  "Из его кармана торчит листок. Похоже вы нашли пин-код.")
            print("------------------------------------------")
            ChekToChek[2] = 1
            main()
        case 4:
            print("------------------------------------------")
            print("Комната похожа на лабораторию. Рядом с одной из стен стоит стол, полный всяких вещей. \n"
                  "В центре комнаты - стоит небольшая бочка с топливом. Недалеко от стола вы замечаете \n"
                  "осколки от пробирок и банку с неизвестной жидкостью. В углу комнаты валяется ключ.")
            print("------------------------------------------")
            ChekToChek[3] = 1
            main()
        case 5:
            print("------------------------------------------")
            print("Комната напоминает место для отдыха. Маленький столик, кровать причудливой формы, под кроватью \n"
                  "лежит странная вещь, напоминающая деталь от чего-то и боевая винтовка.")
            print("------------------------------------------")
            ChekToChek[4] = 1
            main()
        case 6:
            print("------------------------------------------")
            print("В комнате вы видете небольшой коспический корабль. С виду он выглядит рабочим.")
            print("------------------------------------------")
            ChekToChek[5] = 1
            main()
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
                if UserChoice == 1:
                    PlayerInventory.append(CurrentRoomSubjects1[0])
                    CurrentRoomSubjects1[0] = "Кусок железной пластины"
                    main()
                elif UserChoice == 2:
                    PlayerInventory.append(CurrentRoomSubjects1[1])
                    CurrentRoomSubjects1[1] = "Кусок железной пластины"
                    main()
                else:
                    ErrorVvod()
                    Take()
            else:
                print("Сначала нужно осмотреться, прежде брать что-то!")
                main()
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
                            CurrentRoomSubjects2[0] = "Кусок тела существа"
                            main()
                    except:
                        ErrorVvod()
                        Take()
                else:
                    print("Сначала убейте существо")
                    main()
            else:
                print("Сначала нужно осмотреться, прежде брать что-то!")
                main()
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
                if UserChoice == 1:
                    PlayerInventory.append(CurrentRoomSubjects3[0])
                    CurrentRoomSubjects3[0] = "Кусок от одежды ксеноса"
                    main()
                else:
                    ErrorVvod()
                    Take()
            else:
                print("Сначала нужно осмотреться, прежде брать что-то!")
                main()
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
                if UserChoice == 1:
                    PlayerInventory.append(CurrentRoomSubjects5[0])
                    CurrentRoomSubjects5[0] = "Пыль с пола"
                    main()
                if UserChoice == 2:
                    PlayerInventory.append(CurrentRoomSubjects5[1])
                    CurrentRoomSubjects5[1] = "Кусок металлической пластины"
                    main()
                if UserChoice == 3:
                    PlayerInventory.append(CurrentRoomSubjects5[2])
                    CurrentRoomSubjects5[2] = "Пыль с пола"
                    main()
                if UserChoice == 4:
                    PlayerInventory.append(CurrentRoomSubjects5[3])
                    CurrentRoomSubjects5[3] = "Кусок металлической пластины"
                    main()
                else:
                    ErrorVvod()
                    Take()
            else:
                print("Сначала нужно осмотреться, прежде брать что-то!")
                main()
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
                if UserChoice == 1:
                    PlayerInventory.append(CurrentRoomSubjects4[0])
                    CurrentRoomSubjects4[0] = "Осколок от пробирки"
                    main()
                if UserChoice == 2:
                    PlayerInventory.append(CurrentRoomSubjects4[1])
                    CurrentRoomSubjects4[1] = "Непонятный предмет на столе"
                    main()
                if UserChoice == 3:
                    PlayerInventory.append(CurrentRoomSubjects4[2])
                    CurrentRoomSubjects4[2] = "Пыль с пола"
                    main()
                if UserChoice == 4:
                    PlayerInventory.append(CurrentRoomSubjects4[3])
                    CurrentRoomSubjects4[3] = "Кусок металлической пластины"
                    main()
                else:
                    ErrorVvod()
                    Take()
            else:
                print("Сначала нужно осмотреться, прежде брать что-то!")
                main()
        case 6:
            if ChekToChek[5] == 1:
                print("------------------------------------------")
                print("Здесь нечего брать")
                print("------------------------------------------")
                main()
            else:
                print("------------------------------------------")
                print("Сначала нужно осмотреться!")
                print("------------------------------------------")
                main()



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
            match (UserChoice):
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
                    RoomChoice()
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
        case 2:
            print("------------------------------------------")
            print("Вы оказались в Комнате №2")
            print("------------------------------------------")
            PlayerPosition = 2
            main()
        case 3:
            print("------------------------------------------")
            print("Вы оказались в Комнате №3")
            print("------------------------------------------")
            PlayerPosition = 3
            main()
        case 4:
            print("------------------------------------------")
            print("Вы оказались в Комнате №4")
            print("------------------------------------------")
            PlayerPosition = 4
            main()
        case 5:
            print("------------------------------------------")
            print("Вы оказались в Комнате №5")
            print("------------------------------------------")
            PlayerPosition = 5
            main()
        case 6:
            print("------------------------------------------")
            print("Вы оказались в Комнате №6")
            print("------------------------------------------")
            PlayerPosition = 6
            main()
        case _:
            ErrorVvod()
            main()

print("Итак... Вы оказались на коробле инопланетян. Вы стоите в большой круглой комнате (назовём её Комната №1). \n Вокруг вас "
      "вы не видете ничего кроме 5 дверей и металла, но стоит осмотреться получше. \n Кажется это ваш шанс выбраться от сюда. Вперёд!")
main()