# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")
define n = Character('Неко-помощник', color="c8ffc8")
define r = Character('Полу-демон', color="c8ffc8")
define ohr = Character('Охранник', color="c8ffc8")
define rebiata = Character('Ребята', color="c8ffc8")
define starik = Character('Какой-то мужик', color="c8ffc8") 
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    play music "Relax.mp3"

    scene black



    "{alpha=.5}{cps=25}Я взглянул в окно и увидел бригаду рабочих, кажется они строили дом. Я дал каждому из них свой номер.{/alpha}"
    "{alpha=.5}{cps=25}Они работали как часы: №1 таскал цемент с песком, №2 таскал воду, затем №3 из полученных ингредиентов создавал бетон, который после передавался №4 для укладывания кирпича.{/alpha}"
    "{alpha=.5}{cps=25}Каждого рабочего можно было сравнить с шестеренкой в этом механизме.{/alpha}"
    "{alpha=.5}{cps=25}Я же был словно маленький винтик выпавший из собственной конструкции...{/alpha}"
    stop music fadeout 1

    play sound "bells.mp3"

    scene sch
    with Dissolve(2.5)
    play music "School.mp3"
    "{cps=25}ДА БЛИН! В этот раз звонок какой-то громкий."
    "{cps=25}Похоже, я стал слишком чувтсвительным к окружающему."
    play sound "Punch.mp3"
    with vpunch
    define andr = Character("Андрей", color = "ffdab9")
    define a = Character("Сергей", color = "ffffff")
    define pet = Character("Петя", color = "ffffe0")
    andr"{cps=25}Эй, Сергей, у тебя не найдется ручки?"
    menu:
        "Найдется.":
            jump choice1_yes
        "Не найдется.":
            jump choice1_no
    label choice1_yes:
        $ menu_flag = True
    a"{cps=25}Да, держи."
    andr"{cps=25}Спасибо."
    jump choice1_done
    label choice1_no:
        $ menu_flag = False
    a"{cps=25}Нет, сорян."
    andr"{cps=25}Жалко..."
    jump choice1_done
    label choice1_done:
    a"{cps=25}Кстати, я тут классную игру нашел, может сыграем вечерком?"
    andr"{cps=25}Нет, у меня встреча с девчонками будет."
    a"{cps=25}Ладно тогда."
    "{alpha=.5}{cps=25}Кого-бы еще пригласить...{w=1.0} Может Петя захочет?{/alpha}"
    a"{cps=25}Петя!{w=.3} Не хочешь сегодня в PG: Online сыграть?"
    pet"{cps=25}Я даже не покупал ее!"
    a"{cps=25}Так давай купи и поиграем, на нее скидка сейчас."
    pet"{cps=25}Не,{w=.5} точно не сегодня,{w=0.5} ладно,{w=0.5} мне пора."
    "{cps=25}Да чтоб тебя!{w} СО МНОЙ СЫГРАЕТ КТО-НИБУДЬ, НЕТ?!"
    "{cps=25}ПОЧЕМУ  ВСЕГДА ТАК?!"
    "{cps=25}Ладно, пора домой."
    play music "veter.mp3"
    show street4
    with Fade(2.0, 0.0, 0.8, color= '#000000')
    pause
    play music "Computer.mp3"
    show laptop1
    with Fade(2.0, 0.0, 0.8, color= '#000000')
    pause
    "{cps=25}Эх, во что бы погамать?"
    "{cps=25}...{/alpha}"
    "{cps=15}\"Герои-Рыцари и Маги\"!"
    scene background3
    with pixellate
    play music "Gotika.mp3"
    jump previugame
label choise1:
hide screen restart
$game1vibor+=1
hide screen kristina_karta1
hide screen fiona_karta1
hide screen alena_karta1
hide screen gg_karta1
show ggkarta1:
    xalign 0.3
    yalign 0.6
show alenakarta1:
    xalign 0.1
    yalign 0.6
show fionakarta1:
    xalign 0.3
    yalign 0.2
show kristinakarta2:
    xalign 0.1
    yalign 0.2
if game1vibor==1:
    if sluchain1 == 1:
        $attack+=1;
        show sword1:
            xalign 0.1
            yalign 0.04
        pause 2
        hide kristinakarta2
        jump choise0
    else:
        hide fionakarta1
        hide alenakarta1
        hide ggkarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Перейти к защите":
                jump armor_one
else:
    if game1vibor==2:
        if sluchain2 == 1:
            $attack+=1;
            show sword2:
                xalign 0.15
                yalign 0.04
            pause 2
            hide kristinakarta2
            jump choise0
        else:
            hide screen fiona_karta1
            hide screen alena_karta1
            hide screen gg_karta1
            window show
            "Увы вы ошиблись."
            menu:
                "Перейти к защите":
                    jump armor_one


label choise2:
hide screen restart
$game1vibor+=1
hide screen kristina_karta1
hide screen fiona_karta1
hide screen alena_karta1
hide screen gg_karta1
show ggkarta1:
    xalign 0.3
    yalign 0.6
show alenakarta1:
    xalign 0.1
    yalign 0.6
show fionakarta2:
    xalign 0.3
    yalign 0.2
show kristinakarta1:
    xalign 0.1
    yalign 0.2
if game1vibor==1:
    if sluchain1 == 2:
        $attack+=1;
        show sword1:
            xalign 0.1
            yalign 0.04
        pause 2
        hide fionakarta2
        jump choise0
    else:
        hide kristinakarta1
        hide alenakarta1
        hide ggkarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Перейти к защите":
                jump armor_one
else:
    if game1vibor==2:
        if sluchain2 == 2:
            $attack+=1;
            show sword2:
                xalign 0.15
                yalign 0.04
            pause 2
            hide fionakarta2
            jump choise0
        else:
            hide kristinakarta1
            hide alenakarta1
            hide ggkarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Перейти к защите":
                    jump armor_one

label choise3:
hide screen restart
$game1vibor+=1
hide screen kristina_karta1
hide screen fiona_karta1
hide screen alena_karta1
hide screen gg_karta1
show ggkarta1:
    xalign 0.3
    yalign 0.6
show alenakarta2:
    xalign 0.1
    yalign 0.6
show fionakarta1:
    xalign 0.3
    yalign 0.2
show kristinakarta1:
    xalign 0.1
    yalign 0.2
if game1vibor==1:
    if sluchain1 == 3:
        $attack+=1;
        show sword1:
            xalign 0.1
            yalign 0.04
        pause 2
        hide alenakarta2
        jump choise0
    else:
        hide kristinakarta1
        hide fionakarta1
        hide ggkarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Перейти к защите":
                jump armor_one
else:
    if game1vibor==2:
        if sluchain2 == 3:
            $attack+=1;
            show sword2:
                xalign 0.15
                yalign 0.04
            pause 2
            hide alenakarta2
            jump choise0
        else:
            hide kristinakarta1
            hide fionakarta1
            hide ggkarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Перейти к защите":
                    jump armor_one
label choise4:
hide screen restart
$game1vibor+=1
hide screen kristina_karta1
hide screen fiona_karta1
hide screen alena_karta1
hide screen gg_karta1
show ggkarta2:
    xalign 0.3
    yalign 0.6
show alenakarta1:
    xalign 0.1
    yalign 0.6
show fionakarta1:
    xalign 0.3
    yalign 0.2
show kristinakarta1:
    xalign 0.1
    yalign 0.2
if game1vibor==1:
    if sluchain1 == 4:
        $attack+=1;
        show sword1:
            xalign 0.1
            yalign 0.04
        pause 2
        hide ggkarta2
        jump choise0
    else:
        hide kristinakarta1
        hide fionakarta1
        hide alenakarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Перейти к защите":
                jump armor_one
else:
    if game1vibor==2:
        if sluchain2 == 4:
            $attack+=1;
            show sword2:
                xalign 0.15
                yalign 0.04
            pause 2
            hide ggkarta2
            jump choise0
        else:
            hide kristinakarta1
            hide fionakarta1
            hide alenakarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Перейти к защите":
                    jump armor_one
# Игра начинается здесь:
label previugame:
    menu:
        "Прочитать правила":
            jump pravila
        "Начать игру":
            jump game
    label pravila:
    scene pravila1
    "Приветсвую в мини-игре!"
    "Для победы над противником вам нужно набрать достаточное количество атаки и защиты."
    "Очки атаки вы зарабатываете,поочерёдно угадывая синие карты, которые открылись после начала игры."
    "Очки защиты вы зарабатываете,поочерёдно угадывая красные карты, которые открылись после начала игры."
    menu:
        "Начать игру":
            jump game
    label game:
    "В этот раз для победы вам нужно заработать 2 очка атаки и 2 очка защиты."
    hide screen kristina_karta1
    hide screen fiona_karta1
    hide screen alena_karta1
    hide screen gg_karta1
    window hide
    scene background4
    $armor = 0
    $attack = 0
    $game1vibor2=0
    $game1vibor=0
    $sluchain1 = 0
    $sluchain2 = 0
    $sluchain3 = 0
    $sluchain4 = 0
    screen restart:
        imagebutton xalign 0.5 yalign 0.2:
            idle ("restart.png")
            action Jump("previugame")
    show kristinakarta1:
        xalign 0.1
        yalign 0.2
    show fionakarta1:
        xalign 0.3
        yalign 0.2
    show alenakarta1:
        xalign 0.1
        yalign 0.6
    show ggkarta1:
        xalign 0.3
        yalign 0.6
    show viacheslavkarta1:
        xalign 0.65
        yalign 0.2
    show tamarakarta1:
        xalign 0.85
        yalign 0.2
    show gopnikkarta1:
        xalign 0.65
        yalign 0.6
    show starikkarta1:
        xalign 0.85
        yalign 0.6
    $sluchain1 = renpy.random.randint(1,4)
    $sluchain1v2 = renpy.random.randint(1,4)
####Разворот первых двух карт
    pause 2
    if sluchain1 == 1:#Первая синяя карта
        hide kristinakarta1
        show kristinakarta2:
            xalign 0.1
            yalign 0.2
    if sluchain1v2 == 1:#Первая красная карта
        hide viacheslavkarta1
        show viacheslavkarta2:
            xalign 0.65
            yalign 0.2
    if sluchain1 == 2:
        hide fionakarta1
        show fionakarta2:
            xalign 0.3
            yalign 0.2
    if sluchain1v2 == 2:
        hide tamarakarta1
        show tamarakarta2:
            xalign 0.85
            yalign 0.2
    if sluchain1 == 3:
        hide alenakarta1
        show alenakarta2:
            xalign 0.1
            yalign 0.6
    if sluchain1v2 == 3:
        hide gopnikkarta1
        show gopnikkarta2:
            xalign 0.65
            yalign 0.6
    if sluchain1 == 4:
        hide ggkarta1
        show ggkarta2:
            xalign 0.3
            yalign 0.6
    if sluchain1v2 == 4:
        hide starikkarta1
        show starikkarta2:
            xalign 0.85
            yalign 0.6
#####Разворот обратно этих же карт
    pause 2
    if sluchain1 == 1:
        hide kristinakarta2
        show kristinakarta1:
            xalign 0.1
            yalign 0.2
    if sluchain1v2 == 1:
        hide viacheslavkarta2
        show viacheslavkarta1:
            xalign 0.65
            yalign 0.2
    if sluchain1 == 2:
        hide fionakarta2
        show fionakarta1:
            xalign 0.3
            yalign 0.2
    if sluchain1v2 == 2:
        hide tamarakarta2
        show tamarakarta1:
            xalign 0.85
            yalign 0.2
    if sluchain1 == 3:
        hide alenakarta2
        show alenakarta1:
            xalign 0.1
            yalign 0.6
    if sluchain1v2 == 3:
        hide gopnikkarta2
        show gopnikkarta1:
            xalign 0.65
            yalign 0.6
    if sluchain1 == 4:
        hide ggkarta2
        show ggkarta1:
            xalign 0.3
            yalign 0.6
    if sluchain1v2 == 4:
        hide starikkarta2
        show starikkarta1:
            xalign 0.85
            yalign 0.6

    pause 2
#######Razvorot sleduyushih dvuh kart

    $sluchain2 = renpy.random.randint(1,4)
    $sluchain2v2 = renpy.random.randint(1,4)
    if sluchain2 == 1:#Первая синяя карта
        hide kristinakarta1
        show kristinakarta2:
            xalign 0.1
            yalign 0.2
    if sluchain2v2 == 1:#Первая красная карта
        hide viacheslavkarta1
        show viacheslavkarta2:
            xalign 0.65
            yalign 0.2
    if sluchain2 == 2:
        hide fionakarta1
        show fionakarta2:
            xalign 0.3
            yalign 0.2
    if sluchain2v2 == 2:
        hide tamarakarta1
        show tamarakarta2:
            xalign 0.85
            yalign 0.2
    if sluchain2 == 3:
        hide alenakarta1
        show alenakarta2:
            xalign 0.1
            yalign 0.6
    if sluchain2v2 == 3:
        hide gopnikkarta1
        show gopnikkarta2:
            xalign 0.65
            yalign 0.6
    if sluchain2 == 4:
        hide ggkarta1
        show ggkarta2:
            xalign 0.3
            yalign 0.6
    if sluchain2v2 == 4:
        hide starikkarta1
        show starikkarta2:
            xalign 0.85
            yalign 0.6
#####Разворот обратно этих же карт
    pause 2
    if sluchain2 == 1:
        hide kristinakarta2
        show kristinakarta1:
            xalign 0.1
            yalign 0.2
    if sluchain2v2 == 1:
        hide viacheslavkarta2
        show viacheslavkarta1:
            xalign 0.65
            yalign 0.2
    if sluchain2 == 2:
        hide fionakarta2
        show fionakarta1:
            xalign 0.3
            yalign 0.2
    if sluchain2v2 == 2:
        hide tamarakarta2
        show tamarakarta1:
            xalign 0.85
            yalign 0.2
    if sluchain2 == 3:
        hide alenakarta2
        show alenakarta1:
            xalign 0.1
            yalign 0.6
    if sluchain2v2 == 3:
        hide gopnikkarta2
        show gopnikkarta1:
            xalign 0.65
            yalign 0.6
    if sluchain2 == 4:
        hide ggkarta2
        show ggkarta1:
            xalign 0.3
            yalign 0.6
    if sluchain2v2 == 4:
        hide starikkarta2
        show starikkarta1:
            xalign 0.85
            yalign 0.6

    pause 2
################################
    hide kristinakarta1
    hide fionakarta1
    hide alenakarta1
    hide ggkarta1
    hide viacheslavkarta1
    hide tamarakarta1
    hide gopnikkarta1
    hide starikkarta1


    label choise0:
    hide screen kristina_karta1
    hide screen fiona_karta1
    hide screen alena_karta1
    hide screen gg_karta1
    if game1vibor==2:
        window show
        "Вы заработали максимальную атаку."
        menu:
            "Перейти к защите":
                jump armor_one
    screen kristina_karta1:
        imagebutton xalign 0.1 yalign 0.2:
            idle ("karta2.png")
            hover ("karta3.png")
            action Jump("choise1")
    show screen kristina_karta1
    screen fiona_karta1:
        imagebutton xalign 0.3 yalign 0.2:
            idle ("karta2.png")
            hover ("karta3.png")
            action Jump("choise2")
    show screen fiona_karta1
    screen alena_karta1:
        imagebutton xalign 0.1 yalign 0.6:
            idle ("karta2.png")
            hover ("karta3.png")
            action Jump("choise3")
    show screen alena_karta1
    screen gg_karta1:
        imagebutton xalign 0.3 yalign 0.6:
            idle ("karta2.png")
            hover ("karta3.png")
            action Jump("choise4")
    show screen gg_karta1
    call screen restart

label armor_one:
    hide screen kristina_karta1
    hide screen fiona_karta1
    hide screen alena_karta1
    hide screen gg_karta1
    window hide
    if game1vibor2==2:
        window show
        "Вы заработали максимальную защиту."
        menu:
            "Начать битву":
                jump fight_one
    screen viacheslav_karta1:
        imagebutton xalign 0.65 yalign 0.2:
            idle ("karta4.png")
            hover ("karta5.png")
            action Jump("choise5")
    show screen viacheslav_karta1
    screen tamara_karta1:
        imagebutton xalign 0.85 yalign 0.2:
            idle ("karta4.png")
            hover ("karta5.png")
            action Jump("choise6")
    show screen tamara_karta1
    screen gopnik_karta1:
        imagebutton xalign 0.65 yalign 0.6:
            idle ("karta4.png")
            hover ("karta5.png")
            action Jump("choise7")
    show screen gopnik_karta1
    screen starik_karta1:
        imagebutton xalign 0.85 yalign 0.6:
            idle ("karta4.png")
            hover ("karta5.png")
            action Jump("choise8")
    show screen starik_karta1
    call screen restart

label choise5:
hide screen restart
$game1vibor2+=1
hide screen starik_karta1
hide screen gopnik_karta1
hide screen tamara_karta1
hide screen viacheslav_karta1
show starikkarta1:
    xalign 0.85
    yalign 0.2
show gopnikkarta1:
    xalign 0.65
    yalign 0.6
show tamarakarta1:
    xalign 0.85
    yalign 0.6
show viacheslavkarta2:
    xalign 0.65
    yalign 0.2
if game1vibor2==1:
    if sluchain1v2 == 1:
        $armor+=1;
        show shield1:
            xalign 0.6
            yalign 0.04
        pause 2
        hide viacheslavkarta2
        jump armor_one
    else:
        hide starikkarta1
        hide gopnikkarta1
        hide tamarakarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Начать битву":
                jump fight_one
else:
    if game1vibor2==2:
        if sluchain2v2 == 1:
            $armor+=1;
            show shield2:
                xalign 0.65
                yalign 0.04
            pause 2
            hide viacheslavkarta2
            jump armor_one
        else:
            hide starikkarta1
            hide gopnikkarta1
            hide tamarakarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Начать битву":
                    jump fight_one
label choise6:
hide screen restart
$game1vibor2+=1
hide screen starik_karta1
hide screen gopnik_karta1
hide screen tamara_karta1
hide screen viacheslav_karta1
show starikkarta1:
    xalign 0.85
    yalign 0.2
show gopnikkarta1:
    xalign 0.65
    yalign 0.6
show viacheslavkarta1:
    xalign 0.65
    yalign 0.2
show tamarakarta2:
    xalign 0.85
    yalign 0.2
if game1vibor2==1:
    if sluchain1v2 == 2:
        $armor+=1;
        show shield1:
            xalign 0.6
            yalign 0.04
        pause 2
        hide tamarakarta2
        jump armor_one
    else:
        hide starikkarta1
        hide gopnikkarta1
        hide viacheslavkarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Начать битву":
                jump fight_one
else:
    if game1vibor2==2:
        if sluchain2v2 == 2:
            $armor+=1;
            show shield2:
                xalign 0.65
                yalign 0.04
            pause 2
            hide tamarakarta2
            jump armor_one
        else:
            hide starikkarta1
            hide gopnikkarta1
            hide viacheslavkarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Начать битву":
                    jump fight_one
label choise7:
hide screen restart
$game1vibor2+=1
hide screen starik_karta1
hide screen gopnik_karta1
hide screen tamara_karta1
hide screen viacheslav_karta1
show starikkarta1:
    xalign 0.85
    yalign 0.2
show viacheslavkarta1:
    xalign 0.65
    yalign 0.2
show tamarakarta1:
    xalign 0.85
    yalign 0.2
show gopnikkarta2:
    xalign 0.65
    yalign 0.6
if game1vibor2==1:
    if sluchain1v2 == 3:
        $armor+=1;
        show shield1:
            xalign 0.6
            yalign 0.04
        pause 2
        hide gopnikkarta2
        jump armor_one
    else:
        hide starikkarta1
        hide tamarakarta1
        hide viacheslavkarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Начать битву":
                jump fight_one
else:
    if game1vibor2==2:
        if sluchain2v2 == 3:
            $armor+=1;
            show shield2:
                xalign 0.65
                yalign 0.04
            pause 2
            hide gopnikkarta2
            jump armor_one
        else:
            hide starikkarta1
            hide tamarakarta1
            hide viacheslavkarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Начать битву":
                    jump fight_one
label choise8:
hide screen restart
$game1vibor2+=1
hide screen starik_karta1
show starikkarta2:
    xalign 0.85
    yalign 0.2
show viacheslavkarta1:
    xalign 0.65
    yalign 0.2
show tamarakarta1:
    xalign 0.85
    yalign 0.2
show gopnikkarta1:
    xalign 0.65
    yalign 0.6
if game1vibor2==1:
    if sluchain1v2 == 4:
        $armor+=1;
        show shield1:
            xalign 0.6
            yalign 0.04
        pause 2
        hide starikkarta2
        jump armor_one
    else:
        hide gopnikkarta1
        hide tamarakarta1
        hide viacheslavkarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Начать битву":
                jump fight_one
else:
    if game1vibor2==2:
        if sluchain2v2 == 4:
            $armor+=1;
            show shield2:
                xalign 0.65
                yalign 0.04
            pause 2
            hide starikkarta2
            jump armor_one
        else:
            hide gopnikkarta1
            hide tamarakarta1
            hide viacheslavkarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Начать битву":
                    jump fight_one

label fight_one:
    hide screen viacheslav_karta1
    hide screen tamara_karta1
    hide screen gopnik_karta1
    hide screen starik_karta1
    if attack==2 and armor==2:
        scene win
        "Атаки и защиты хватило чтобы победить!"
    else:
        scene lose
        if attack<2 and armor<2:
            "Наша защита была разгромлена, наши атаки не достигли противника."
        else:
            if attack<2:
                "Наши атаки не достигли противника."
            if armor<2:
                "Наша защита была разгромлена."
        menu:
            "Начать заново":
                jump previugame
    label label_two:
scene black
play music "Relax.mp3"
with Fade(2.0, 0.0, 0.8, color= '#000000')
"{alpha=.5}{cps=25}Обессиленный я упал в кровать.{/alpha}"
"{alpha=.5}{cps=25}.{/alpha}"
"{alpha=.5}{cps=25}..{/alpha}"
"{alpha=.5}{cps=25}...{/alpha}"
"{alpha=.5}{cps=25}Может показаться, что я всю жизнь играю без команды.{/alpha}"
"{alpha=.5}{cps=25}Однако, когда-то мне удавалось находить соплеменников в игровом мире.{/alpha}"
stop music fadeout 1
define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
play music "csounds.mp3"
scene club
with flashbulb
define v = Character('Вячеслав', color="#FF0000")
show viachesl3
v"{cps=25}Так, ты хочешь вступить в нашу команду!?"
a"{cps=25}Нууу...да."
v"{cps=25}Хорошо. Проверим твои наваыки в действии."
a"{cps=25}Отлично!"
v"{cps=25}Главное у нас это бодрый настрой и командный дух!"
a"{cps=25}Я СПРАВЛЮСЬ!1"
hide viaches13
with Dissolve(.5)
scene black
with Fade(2.0, 0.0, 0.8, color= '#000000')
play music "Relax.mp3"
"{alpha=.5}{cps=25}Мы играли во многих турнирах. Иногда даже получалось выигрывать.{/alpha}"
"{alpha=.5}{cps=25}В те моменты я чувствовал себя по-настоящему счастливым.{/alpha}"
"{alpha=.5}{cps=25}Но в один момент всё изменилось.{/alpha}"
scene club
with flashbulb
play music "csounds.mp3"
show viachesl3
with Dissolve(.5)
a"{cps=25}Что? Ты уходишь из команды?"
v"{cps=25}Да."
a"{cps=25}Но почему?"
v"{cps=25}Знаешь, Саня, я уже слишком постарел для игры. Многие игроки уважают меня лишь за былые заслуги."
v"{cps=25}Да и сам я понимаю, что играю все хуже и хуже."
v"{cps=25}Знаешь, я как старая бабушка, которая старается быть привлекательной. Может она для своих лет и ничё так, но в её сторону уже никто не смотрит."
a"{cps=25}Да что ты несешь, это же неправда.{w=.5} Ты первое звено в нашей команде, без тебя мы словно..."
v"{cps=25}ХВАТИТ  НЫТЬ!"
a"{cps=25}..."
v"{cps=25}Запомни-ка вот что: если у тебя есть чувство стремления к победе, то ты всегда будешь побеждать."
"{cps=25}Он положил мне руку на плечо."
v"{cps=25}Ты очень хорошо играешь Сергей, я знаю, что у тебя есть потенциал."
v"{cps=25}Если что, пиши мне."
hide viachesl3
with Dissolve(.5)
play sound "Uhod.mp3"
"{alpha=.5}{cps=25}Он отдал мне честь и вышел из клуба.{/alpha}"
scene black
play music "Relax.mp3"
with Fade(2.0, 0.0, 0.8, color= '#000000')
"{alpha=.5}{cps=25}Вообще, после ухода Вячеслава мне было не очень приятно играть с остальными, ведь для меня он был настоящим капитаном: отважным, решительным, относительно спокойным.{/alpha}"
"{alpha=.5}{cps=25}У моих тиммейтов не было этих качеств.{/alpha}"
"{alpha=.5}{cps=25}Возможно, тогда мне стоило больше общаться с командой для нашего киберспортивного будущего.{/alpha}"
"{alpha=.5}{cps=25}Однако, случилось событие, которое поставило точку в наших отношениях.{/alpha}"
scene club
play music "csounds.mp3"
a"{cps=25}{cps=25}Эй,{w=.5} почему вы давали им столько шансов для победы?"
define e = Character('Егор', color="#ff6347")
define i = Character('Ильдус', color="#00ffff")
e"{cps=25}А ты разве не знаешь?"
a"{cps=25}Чего?"
i"{cps=25}Матч подставной."
i"{cps=25}Мы ставим на свой проигрышь и зарабатывем  на этом."
a"{cps=25}Подставные матчи?{w=.5} ВЫ СОВСЕМ РЕХНУЛИСЬ?!"
a"{cps=25}ДА ПОШЛИ ВЫ ВСЕ НА@#*"
play sound "Hodba.mp3"
"{alpha=.5}{cps=25}Без раздумий я немедленно покинул клуб.{/alpha}"
play music "Relax.mp3"
scene black
with Fade(2.0, 0.0, 0.8, color= '#000000')
"{alpha=.5}{cps=25}Я понял, что мы уже не были той командой, которая была с Вячеславом.{/alpha}"
"{alpha=.5}{cps=25}Стимул команды перевернулся с ног  на голову. Раньше мы были готовы побеждать всех и каждого, а теперь готовы променять свою победу на деньги.{/alpha}"
"{alpha=.5}{cps=25}Я не был согласен с таким порядком. После этого я потерял в себе уверенность в отношении игры в команде.{/alpha}"
"{alpha=.5}{cps=25}...{/alpha}"
"{alpha=.5}{cps=25}Или я не прав?{/alpha}"
scene laptop2
with Fade(0.2, 0.0, 0.8, color= '#fff')
play music "Utro.mp3"
"{alpha=.5}{cps=25}Я проснулся из-за ярких лучей солнца, направленных в мое окно.{/alpha}"
a"{cps=25}Нет! только не  ослепительное пламя!"
"{cps=25}Пора в школу, но для начала надо поесть."
define circleirisout = ImageDissolve("circle.png",1.0,8)
play sound "Shag pol.mp3"
scene kit
with circleirisout
play music "Kitchen.mp3"
"{alpha=.5}{cps=25}Я зашёл на кухню.{/alpha}"
"{cps=25}..."
"{cps=25}Странно, обычно мама всегда делает мне завтрак. Похоже её нет дома."
"{alpha=.5}{cps=25}Мы заботимся друг о друге: она зарабатывает деньги, а я помогаю ей по дому.{/alpha}"
"{alpha=.5}{cps=25}Мы живём вдвоём, после того, как отец погиб в автокатастрофе.{/alpha}"
"{cps=25}Придётся остаться без завтрака. Поем в школе."
define circleirisin = ImageDissolve("circle.png",1.0,8,reverse=True)
scene schooltrip
with circleirisin
play music "Street.mp3"
"{alpha=.5}{cps=25}Дорога до школы занимала около 10 минут. В это время я мог насладиться прекрасным видом улицы.{/alpha}"
"{alpha=.5}{cps=25}Но решил этого не делать.{/alpha}"
scene way1
with fade
play sound "Shagi.mp3"
"{alpha=.5}{cps=25}По дороге я думал о разных вещах: например о том, что я буду есть.{/alpha}"
"{cps=25}Думаю надо перекусить..."
scene schooltrip
with fade
play sound "Punch.mp3"
with hpunch
"{alpha=.5}{cps=25}Я столкнулся с какой-то женщиной.{/alpha}"
show tamara
with Dissolve(.5)
define t = Character('Тамара', color="#FF00FF")
t"{cps=25}Смотри под ноги!"
t"{cps=25}Ох уже эти школьники!"
a"{cps=25}Прошу прощения."
hide tamara
with Dissolve(.5)
"{alpha=.5}{cps=25}С первого взгляда я понял - с ней лучше не связываться.{/alpha}"
"{alpha=.5}{cps=25}Надеюсь, судьба не столкнет нас снова."
"{alpha=.5}{cps=25}Я пошел дальше.{/alpha}"
scene sch
with irisout
play music "School.mp3"
"{alpha=.5}{cps=25}За день ничего не произошло, впрочем как и всегда. Разве что я вновь встретил ту странную женщину.{/alpha}"
play  music "Cafe.mp3"
scene stol
with fade
"{cps=25}Откуда она здесь?"
play sound "Shag pol.mp3"
"{alpha=.5}{cps=25}Я быстро доел свой обед и поспешно направился к выходу.{/alpha}"
play music "Street.mp3"
scene schooltrip
with fade
pause
play music "Kitchen.mp3"
scene kit
with fade
pause
"{cps=25}Странно... мамы до сих пор нет."
play sound "Phone.mp3"
"{cps=25}Позвоню-ка я ей на работу."
"{cps=25}А то как-то не по себе."
pause
play sound "Otvet.mp3"
"{cps=25}..."
"{cps=25}..."
"{cps=25}..."
"{cps=25}..."
"{cps=25}..."
pause
define s = Character('Работник', color="#FF4500")
s"{cps=25}Привет, Сергей!"
a"{cps=25}Здравствуйте! Сегодня мама была на работе?"
s"{cps=25}Да, я как раз хотел тебе позвонить, тут такая ситуация: твоя мама неудачно упала с лестницы и {w=0.5}повредила позвоночник.{w=0.5} Сейчас она находится в больнице."
a"{cps=25}Господи..."
s"{cps=25}Сочувстую, парень."
a"{cps=25}Я сейчас к ней приеду.{w=0.5} Скажите адрес."
s"{cps=25}Хорошо, подожди, сейчас продиктую..."
play music "Relax.mp3"
scene black
with Fade(2.0, 0.0, 0.8, color= '#000000')
"{alpha=.5}{cps=25}Когда я приехал меня не впустили в палату. Травма оказалась слишком серьёзной.{/alpha}"
"{alpha=.5}{cps=25}Врач сказал, что если не провести операцию в ближайшие 2 месяца, то мама не сможет больше ходить.{/alpha}"
"{alpha=.5}{cps=25}Мне стало ещё хуже, когда узнал, что цена операции - 250000 рублей.{/alpha}"
"{alpha=.5}{cps=25}Естественно, у нас таких денег не было, и просить было не у кого.{/alpha}"
play sound "Udar.mp3"
play sound "Plach.mp3"
a"{cps=25}Что же делать?"
a"{cps=25}ЧТО ДЕЛАТЬ?!"
"{alpha=.5}{cps=25}Проведя ночь в больнице мне удалось увидеть мать, однако она спала.{/alpha}"
"{alpha=.5}{cps=25}Позже я сказал врачу, что смогу достать деньги. Хотя я был без понятия как это сделать.{/alpha}"
pause
scene laptop2
with fade
play music "Utro.mp3"
"{alpha=.5}{cps=25}По дороге домой мне пришла отличная идея.{/alpha}"
a"{cps=25}Ограбление банка!"
"{alpha=.5}{cps=25}Я чуть было не открыл вкладку \"Ограбление банков для начинающих\", как наткнулся на регистрацию на турнир по игре в которую я играю.{/alpha}"
a"{cps=25}Ёлки - иголки! Он проводится в моём городе."
a"{cps=25}Так, а что по призовым за победу?"
"{cps=25}500000 рублей за первое место - какая удача! Надежда ещё есть!"
"{alpha=.5}{cps=25}Я  быстро оформил заявку на участие.{/alpha}"
a"{cps=25}Ну всё!"
a"{cps=25}."
a"{cps=25}.."
a"{cps=25}..."
a"{cps=25}У меня же нет команды."
play music "Relax.mp3"
scene black
with Fade(2.0, 0.0, 0.8, color= '#000000')
"{alpha=.5}{cps=25}По началу я позвал Вячеслава, но тот отказался от предложения.{/alpha}"
"{alpha=.5}{cps=25}Весь следующий день я потратил гуляя на форумах и занимаясь поиском игроков.{/alpha}"
"{alpha=.5}{cps=25}Требования: желание победить в турнире, наличие компьютера. Мне этого было достаточно.{/alpha}"
"{alpha=.5}{cps=25}Хоть требования были минимальными, игроки нашлись не сразу.{/alpha}"
"{alpha=.5}{cps=25}И все-таки команда была собрана.{/alpha}"
"{alpha=.5}{cps=25}Пора вместе сыграть.{/alpha}"
scene laptop2
with Fade(2.0, 0.0, 0.8, color= '#000000')
play music "Computer.mp3"
pause
"{cps=25}..."
"{cps=25}..."
"{cps=25}..."
play sound "Udar.mp3"
a"{cps=25}ДА КАК ТАК?!"
pause
define circlewipe =  ImageDissolve("Circle2.png",1.0,8)
scene laptop1
with circlewipe
play music "Computer.mp3"
a"{cps=25}Да кто так играет?!"
play sound "Loud.mp3"
a"{cps=25}ААААААААААААААА!!!"
a"{cps=25}Это было ужасно."
scene black
with Fade(2.0, 0.0, 0.8, color= '#000000')
play music "Relax.mp3"
play sound "Phone.mp3"
"{alpha=.5}{cps=25}Я решил узнать в чем проблема нашей игры и снова позвонил Вячеславу.{/alpha}"
a"{cps=25}...почему же мы проигрываем?"
v"{cps=25}А вы вживую-то виделись?"
a"{cps=25}Эм, нет."
v"{cps=25}А по голосовому чату общались?"
a"{cps=25}Ни разу."
v"{cps=25}Тогда всё понятно. Конечно вы так не победите."
v"{cps=25}Ты должен узнать их, а они тебя. Они вроде в твоём городе живут. Встреться с ними."
v"{cps=25}У каждого человека свои тараканы в голове, а ты должен увидеть их и направить на правильный путь."
v"{cps=25}Так сказать стать тараканьим королём!"
a"{cps=25}Ну, я попробую."
"{alpha=.5}{cps=25}После ещё одной игры я предложил им встретится в кафе на следующий день после обеда.{/alpha}"
"{alpha=.5}{cps=25}Пора и вздремнуть.{/alpha}"
"{alpha=.5}{cps=25}...{/alpha}"
play music "Utro.mp3"
scene laptop2
with Fade(2.0, 0.0, 0.8, color= '#000000')
"{alpha=.5}{cps=25}Погода была пасмурной, однако обещали потепление."
"{cps=25}Как же одеться?"
menu:
    "Потеплее.":
        jump choice2_yes
    "Похолоднее :).":
        jump choice2_no
label choice2_yes:
    $ menu_flag = True
play music "Street.mp3"
scene schooltrip
with fade
play music "Street.mp3"
"{alpha=.5}{cps=25}Когда я вышел, то не пожалел о том, что оделся потеплее.{/alpha}"
"{cps=25}Если погода наладится, то просто затолкаю куртку в рюкзак.{/alpha}"
"{alpha=.5}{cps=25}Воздух ещё не успел прогреться.{/alpha}"
jump choice2_done
label choice2_no:
    $ menu_flag = False
play music "Street.mp3"
scene schooltrip
with fade
"{alpha=.5}{cps=25}Когда я вышел, то пожалел о том, что не оделся потеплее.{/alpha}"
"{cps=25}Надеюсь, станет действительно теплее.{/alpha}"
"{alpha=.5}{cps=25}Воздух ещё не успел прогреться.{/alpha}"
jump choice2_done
label choice2_done:
play music "School.mp3"
scene sch
with fade
pause
play music "Cafe.mp3"
scene stol
with fade
pause
play music "Street.mp3"
scene street3
with circlewipe
"{alpha=.5}{cps=25}Как и было советовано, я предложил устроить встречу после школы.{/alpha}"
"{alpha=.5}{cps=25}Я прибыл в кафе первым.{/alpha}"
play music "Cafe.mp3"
scene cafe
with fade
"{alpha=.5}{cps=25}\"Домовёнок\" был единственным кафе в моём районе.{/alpha}"
"{alpha=.5}{cps=25}Это место привлекало много людей, они приходили сюда поесть в хорошей обстановке.{/alpha}"
"{alpha=.5}{cps=25}Как всегда родной уют и приятный сервис.{/alpha}"
"{alpha=.5}{cps=25}На стене висел плакат со странной надписью \"Cibo Per i romani\".{/alpha}"
"{cps=25}Наверное, что-то свяанное с итальяской кухней."
"{cps=25}Как же я её ненавижу.{w=0.5} Как люди могут это есть?"
"{alpha=.5}{cps=25}Почти все столики были заняты.{/alpha}"
"{alpha=.5}{cps=25}Официант как раз наводил порядок на столе после предыдущих посетителей, мне посчастливилось занять его.{/alpha}"
scene black
with fade
"{alpha=.5}{cps=25}...{/alpha}"
play music "Cafe.mp3"
scene cafe
with fade
"{alpha=.5}{cps=25}В дальней части кафе я увидел пару любопытных глаз.{/alpha}"
"{alpha=.5}{cps=25}Эта была девушка, ее взгляд был словно лучем Солнца. Он прожигал меня насквозь.{/alpha}"
"{cps=25}Хм...форма моей школы."
init:
    define k = Character('Кристина', color="#FF1493")
    define l = Character('Алёна', color="#000080")
    define f = Character('Фиона', color="#FF8C00")
    define kicon = Character('Кристина', color="#FF1493",image="kristinaicon")
    image side kristinaicon = "kristinaicon.png"
    define licon = Character('Алёна', color="#000080",image="alionaicon")
    image side alionaicon = "alionaicon.png"
    define ficon = Character('Фиона', color="#FF8C00",image="fionaicon")
    image side fionaicon = "fionaicon.png"
image kristina1:
    "kristina1.png"
    pause 7.5
    "kristina1morg.png"
    pause 0.1
    repeat
image kristina2:
    "kristina2.png"
    pause 7.5
    "kristina2morg.png"
    pause 0.1
    repeat
image kristina3:
    "kristina3.png"
    pause 7.5
    "kristina3morg.png"
    pause 0.1
    repeat
image kristina4:
    "kristina4.png"
    pause 7.5
    "kristina4morg.png"
    pause 0.1
    repeat
image kristina5:
    "kristina5.png"
    pause 7.5
    "kristina5morg.png"
    pause 0.1
    repeat
image kristina6:
    "kristina6.png"
    pause 7.5
    "kristina6morg.png"
    pause 0.1
    repeat
image kristina7:
    "kristina7.png"
    pause 7.5
    "kristina7morg.png"
    pause 0.1
    repeat
image kristinakupalnik3:
    "kristinakupalnik3.png"
    pause 7.5
    "kristina7morg.png"
    pause 0.1
    repeat
image alyona1:
    "alyona1.png"
    pause 9.0
    "alyona1morg.png"
    pause 0.1
    repeat
image alyona2:
    "alyona2.png"
    pause 9.0
    "alyona2morg.png"
    pause 0.1
    repeat
image alyona3:
    "alyona3.png"
    pause 9.0
    "alyona3morg.png"
    pause 0.1
    repeat
image alyona4:
    "alyona4.png"
    pause 9.0
    "alyona4morg.png"
    pause 0.1
    repeat
image alyona5:
    "alyona5.png"
    pause 9.0
    "alyona5morg.png"
    pause 0.1
    repeat
image alyona6:
    "alyona6.png"
    pause 9.0
    "alyona6morg.png"
    pause 0.1
    repeat
image alenainbikini:
    "alenainbikini.png"
    pause 9.0
    "alenainbikinimorg.png"
    pause 0.1
    repeat
image fiona1:
    "fiona1.png"
    pause 6.0
    "fiona1morg.png"
    pause 0.1
    repeat
image fiona2:
    "fiona2.png"
    pause 6.0
    "fiona2morg.png"
    pause 0.1
    repeat
image fiona3:
    "fiona3.png"
    pause 6.0
    "fiona3morg.png"
    pause 0.1
    repeat
image fiona5:
    "fiona5.png"
    pause 6.0
    "fiona5morg.png"
    pause 0.1
    repeat
image fiona6:
    "fiona6.png"
    pause 6.0
    "fiona6morg.png"
    pause 0.1
    repeat
image fiona8:
    "fiona8.png"
    pause 6.0
    "fiona8morg.png"
    pause 0.1
    repeat
image fiona9:
    "fiona9.png"
    pause 6.0
    "fiona9morg.png"
    pause 0.1
    repeat
image fiona10:
    "fiona10.png"
    pause 6.0
    "fiona10morg.png"
    pause 0.1
    repeat
image fiona11:
    "fiona11.png"
    pause 6.0
    "fiona11morg.png"
    pause 0.1
    repeat
image fiona12:
    "fiona12.png"
    pause 6.0
    "fiona12morg.png"
    pause 0.1
    repeat
image fiona13:
    "fiona13.png"
    pause 6.0
    "fiona13morg.png"
    pause 0.1
    repeat
image fiona14:
    "fiona14.png"
    pause 6.0
    "fiona14morg.png"
    pause 0.1
    repeat
image fiona15:
    "fiona15.png"
    pause 6.0
    "fiona15morg.png"
    pause 0.1
    repeat
image fionainbikini:
    "fionainbikini.png"
    pause 6.0
    "fionainbikinimorg.png"
    pause 0.1
    repeat
image fionashuy:
    "fionashuy.png"
    pause 6.0
    "fionashuymorg.png"
    pause 0.1
    repeat
image gopnik1:
    "gopnik1.png"
    pause 12.0
    "gopnik1morg.png"
    pause 0.1
    repeat
image tamara:
    "tamara.png"
    pause 11.0
    "tamaramorg.png"
    pause 0.1
    repeat
image tamara5:
    "tamara5.png"
    pause 11.0
    "tamara5morg.png"
    pause 0.1
    repeat
image tamara6:
    "tamara6.png"
    pause 10.0
    "tamara6morg.png"
    pause 0.1
    repeat
image tamara6:
    "tamara6.png"
    pause 10.0
    "tamara6morg.png"
    pause 0.1
    repeat
image viachesl1:
    "viachesl1.png"
    pause 10.0
    "viachesl1morg.png"
    pause 0.1
    repeat

show fiona1
with Dissolve(.5)
"{alpha=.5}{cps=25}Школьница припархала к моему столу словно бабочка, которая нашла цветок в пустыне.{/alpha}"
"{alpha=.5}{cps=25}Она не выглядела как человек, интересующийся играми,{w=0.5} девушка выглядела жизнерадостоной и активной - полная противоположность меня.{/alpha}"
f"{cps=25}Приветики! Это тут собрание задротов?"
a"{cps=25}Ты по адресу! Я кто-то вроде основателя этой команды."
hide fiona1
show fiona2
f"{cps=25}Как классно, что мой капитан это мой одноклассник!"
"{alpha=.5}{cps=25}Эта была Фиона - моя сокурсница и теперь игрок моей новой команды.{/alpha}"
a"{cps=25}Ты серьёзно играешь в MOBA игры?"
f"{cps=25}Да. Я тащусь от них!"
a"{cps=25}Я даже не знал об этом, хотя мы учимся в одном классе."
hide fiona2
show fiona1
f"{cps=25}Так ты меня никогда не спрашивал."
hide fiona1
with Dissolve(.5)
"{alpha=.5}{cps=25}Пока мы вели беседу, к нашему столу подходила ещё одна девушка в школьной форме.{/alpha}"
"{cps=25}Совпадение?  Не думаю."
play sound "Hodba2.mp3"
"{alpha=.5}{cps=25}Робко, шаг за шагом, она подошла к нам и остановилась.{/alpha}"
show kristina1
with Dissolve(.5)
pause
"{alpha=.5}{cps=25}...{/alpha}"
"{alpha=.5}{cps=25}Неловкое молчание длилось около десяти секунд.{/alpha}"
"{alpha=.5}{cps=25}Я решил проявить инициативу.{/alpha}"
a"{cps=25}Ты кто?"
hide kristina1
show kristina2
k"{cps=25}Я...я Кристина."
a"{cps=25}Ты так же по адресу."
a"{cps=25}Я никогда не видел тебя в нашей школе."
hide kristina2
show fiona1
with Dissolve(.5)
f"{cps=25}Это Кристина, мы с ней знакомы. Она на год старше нас, и ,кстати, ходит в кружок плавания, а ещё любит тортики."
hide fiona1
show kristina2
with Dissolve(.5)
k"{cps=25}Эй! Мы виделись с тобой один раз. Откуда такая информация обо мне?"
hide kristina2
show fiona5
with Dissolve(.5)
f"{cps=25}Из надежных источников."
hide fiona5
with Dissolve(.5)
"{alpha=.5}{cps=25}Кристина с опаской поглядела на Фиону.{/alpha}"
a"{cps=25}А меня зовут Сергей. Я капитан нашей команды."
show kristina1
with Dissolve(.5)
k"{cps=25}Очень приятно, Сергей."
hide kristina1
with Dissolve(.5)
"{alpha=.5}{cps=25}Не успел я задать ей пару вопросов, как появился последний член нашей команды.{/alpha}"
"{alpha=.5}{cps=25}Тоже девушка, но, о боже,{w=0.5} она не в школьной форме.{/alpha}"
show alyona1
with Dissolve(.5)
l"{cps=25}Судя по вашей беседе это вы играли со мной."
a"{cps=25}А как тебя зовут?"
hide alyona1
show alyona2
l"{cps=25}Меня зовут Алёна,я люблю...сидеть дома за компом и...на этом наверное всё."
"{alpha=.5}{cps=25}В этом я с ней похож.{/alpha}"
hide alyona2
show fiona1
with Dissolve(.5)
f"{cps=25}Рада с тобой познакомиться, Алёна."
hide fiona1
with Dissolve(.5)
"{alpha=.5}{cps=25}Кристина, видимо, постесняясь, так ничего и не сказала.{/alpha}"
"{cps=25}Итак, все участники в сборе."
"{cps=25}Пришло время сказать речь, которая вдохновит нас на победы."
a"{cps=25}Перейдём к теме по которой мы сегодня собрались."
a"{cps=25}Как вы знаете мы собираемся победить в крупном турнире по PG: Online."
a"{cps=25}Однако с нашим уровнем игры это почти невозможно."
a"{cps=25}Поэтому нам нужно улучшить командную работу."
show alyona1
with Dissolve(.5)
l"{cps=25}И какие у тебя идеи?"
a"{cps=25}Пока их нет."
hide alyona1
show alyona3
l"{cps=25}Прекрасно. Ты нас позвал не имея плана..."
hide alyona3
show fiona2
with Dissolve(.5)
f"{cps=25}Думаю нужно время, чтобы получше друг друга узнать."
hide fiona2
show alyona1
with Dissolve(.5)
a"{cps=25}Да, особенно Серёже, потому что мы девушки и нам проще общаться, а он парень."
hide alyona1
with Dissolve(.5)
"{cps=25}И откуда логика такая?"
play sound "Zamok.mp3"
"{alpha=.5}{cps=25}Фиона потянулась к своему портфелю и вытащила оттуда книгу, на обложке которой красовалась, видимо, ее любимая киберспортивная команда и сказала:{/alpha}"
show fiona1
with Dissolve(.5)
f"{cps=25}В этой книге я прочитала одну действенную методику для сплочения команды."
f"{cps=25}Там указано, что для большей эффективности нужно тренироваться группами по два человека."
f"{cps=25}Как только мы узнаем друг друга получше, мы сможем тренироваться полным составом."
hide fiona1
with Dissolve(.5)
a"{cps=25}Это отличная идея, давайте проголосуем."
show alyona1#-----------------------------------ЗАМЕНИТЬ(АЛЁНА С---------------------------------------------------------------
with Dissolve(.5)
l"{cps=25}А какой смысл голосовать? У нас разве есть альтернатива?"
hide alyona1
show kristina1
with Dissolve(.5)
k"{cps=25}Давайте сойдёмся на этом."
hide kristina1
with Dissolve(.5)
play sound "Uhod.mp3"
"{alpha=.5}{cps=25}Наше собрание подошло к концу, я поспешно удалился.{/alpha}"
play music "Relax.mp3"
scene black
with Fade(2.0, 0.0, 0.8, color= '#000000')
"{cps=25}Сегодняшняя встреча ровным счётом ничего не изменила."
"{cps=25}Можно сказать, что я до сих пор их незнаю."
"{cps=25}Мне не хочется такого же финала как с прошлой комадой."
"{cps=25}А если встетиться с каждой из них по отдельности, то тогда возможно получится установить контакт."
"{alpha=.5}{cps=25}Перед сном я решил создать беседу в мессенджере и договориться о том, на какие пары мы завтра разобъемся.{/alpha}"
"{cps=25}Итак, с кем мне провести время для начала?"
$ score1 = 1
$ score2 = 1
$ score3 = 1
$tamara0 = 0
menu:
    "С Фионой":
        $ score1 = score1 +2
        $tamara0 = tamara0 + 1
        jump Fiona1

    "C Кристиной":
        $ score2 = score2 +2
        $ tamara0 = tamara0 + 1
        jump Kristina1

    "С Алёной":
        $ score3 = score3 +2
        jump Alyona1
label Fiona1:
    "{alpha=.5}{cps=25}Я написал с кем хотел бы быть в группе, споров не возникло.{/alpha}"
    "{alpha=.5}{cps=25}После чего я перешёл в спящий режим.{/alpha}"
    "{cps=25}..."
    play music "Utro.mp3"
    scene laptop2
    with Fade(2.0, 0.0, 0.8, color= '#000000')
    "{cps=25}Решено, сегодня подойду к Фионе."
    play music "Street.mp3"
    scene schooltrip
    with fade
    play music "Koridor1.mp3"
    scene koridor
    with fade
    "{alpha=.5}{cps=25}По моему мнению Фиона нравилась абсолютно всем с кем встречалась.{/alpha}"
    "{alpha=.5}{cps=25}Не сказать, что она мне нравилась, но и отвращение она у меня не вызывала.{/alpha}"
    "{alpha=.5}{cps=25}Вот и сегодня она с беззаботностью носилась туда-сюда привлекая всеобщее внимание.{/alpha}"
    play music "Dynamic.mp3"
    show fiona3 at right
    with Dissolve(.5)
    f"{cps=25}АААА! Она меня сожрёт!"
    define y = Character('Ученик', color="#808080")
    y"{cps=25}Кто?"
    f"{cps=25}Химичка, я не написала ей тест."
    show fiona3 at left
    with move
    f"{cps=25}СПААСИИИИТЕЕЕ!"
    "{alpha=.5}{cps=25}С закрытыми глазами она неслась сначала по кругу, а потом в мою сторону.{/alpha}"
    "{cps=25}Нужно уворачиваться."
    hide fiona3
    menu:
        "Влево":
            jump vibor1
        "Вправо":
            jump vibor2
    label vibor1:
    play sound "Punch.mp3"
    with vpunch
    stop music
    play music "Koridor1.mp3"
    "{alpha=.5}{cps=25}К сожалению она летела слишком быстро.{/alpha}"
    jump vibor1d
    label vibor2:
    play sound "Punch.mp3"
    with vpunch
    stop music
    play music "Koridor1.mp3"
    "{alpha=.5}{cps=25}К сожалению она летела слишком быстро.{/alpha}"
    jump vibor1d
    label vibor1d:
    a"{cps=25}Эй! Надо смотреть куда бежишь!"
    show fiona5
    with Dissolve(.5)
    f"{cps=25}А тебе надо было смотреть на того, кто не смотрит куда бежит."
    "{alpha=.5}{cps=25}Как я понял, нелогичные вещи в разговоре для неё тоже обычное дело.{/alpha}"
    a"{cps=25}Бред не неси."
    hide fiona5
    show fiona4
    f"{cps=25}Уфф..."
    hide fiona4
    with Dissolve(.5)
    "{cps=25}Она развернулась и куда-то утопала."
    "{cps=25}Похоже пока разговору не суждено сбыться."
    play music "School.mp3"
    scene sch
    with fade
    "{cps=25}Блин, я же не позавтракал."
    "{cps=25}Нужно пойти в столовую."
    play music "Cafe.mp3"
    scene stol
    with fade
    "{alpha=.5}{cps=25}Мне повезло, я успеваю взять последнюю котлетку с пюрешкой.{/alpha}"
    "{cps=25}Почти..."
    "{cps=25}Нет!"
    scene kotleta
    with flashbulb
    play sound "Choir.mp3"
    f"{cps=25}Да!"
    scene stol
    with fade
    play music "1234.mp3"
    show fiona6
    a"{cps=25}Это была моя котлетка!"
    hide fiona6
    show fiona7
    f"{cps=25}Эй, мы же в столовой, как говорится: кто успел тот и съел."
    "{cps=25}Нет, я этого так не оставлю."
    hide fiona7
    with Dissolve(.5)
    "{alpha=.5}{cps=25}Я зверски отобрал котлету и съел её.{/alpha}"
    a"{cps=25}Это за то, что сбила меня."
    show fiona5
    with Dissolve(.5)
    f"{cps=25}Ты хочешь войны?"
    a"{cps=25}Время для битвы..."
    hide fiona5
    with Dissolve(.5)
    "{alpha=.5}{cps=25}Фиона выставила кулаки и готова была защищаться.{/alpha}"
    a"{cps=25}...кибербитвы."
    show fiona2
    with Dissolve(.5)
    f"{cps=25}Кибербитвы?"
    a"{cps=25}Да."
    hide fiona2
    show fiona5
    f"{cps=25}Тогда ты уже проиграл."
    a"{cps=25}Мы это ещё посмотрим."
    hide fiona5
    with Dissolve(.5)
    play music "Street.mp3"
    scene schooltrip
    with fade
    play music"Computer.mp3"
    scene laptop1
    with fade
    "{cps=25}Пора показать кто здесь сильнейший."

    label start2:
    scene background3
    with pixellate
    show neko1
    with moveinbottom
    n "Приветствую в мини-игре, ня!"
    n "Пора приступать!"
    hide neko1

    label game1n2:
    $attack2rndm = 0
    $round = 1
    $preimus1 = 50
    $attack1=2
    $attack2=5
    $mobattack1=0
    $mobattack2=0
    $mobs = 0
    $preimus2=50
    $preimus3=0
    $time=0
    $attackcheck=0
    jump choise_done3v2
    label choise_done1v2:
    show neko1v2
    with moveinbottom
    n "Новый раунд"
    hide neko1v2
    with moveoutleft
    if mobs == 2:
        show mob1:
            xalign 0.7
            yalign 0.2
        show mob2:
            xalign 0.85
            yalign 0.2
    if preimus1 > 99:
        jump text1
    if preimus2 > 99:
        jump text2
    $round += 1
    $preimus3 = attack1 + mobattack1 + mobattack2 - attack2

    if preimus1 > 75:
        $attack1 += 1;

        e "атака персонажей команды 1 повышена на  1"
    if preimus2 > 75:
        $attack2 +=1;

    if preimus3 > 0:
        $preimus1 = preimus1 + preimus3
        $preimus2 = preimus2 - preimus3
        e "Преимущество первой команды возросло на [preimus3]"
    else:
        $preimus1 = preimus1 + preimus3
        $preimus2 = preimus2 - preimus3
        $preimus3 = 0 - preimus3
        e "Преимущество второй команды возросло на [preimus3]"
    if preimus1 > 99:
        jump text2v2
    if preimus2 > 99:
        jump text1v2
    $time=0
    show neko1
    with moveinbottom
    n "Ход команды 1"
    hide neko1
#///////////////////////////////////Вывод на экран значение атаки каждого героя, а так же окна следующего хода
    label choise_done3v2:
    screen screen_attack_onev2():
        frame:
            xalign 0.53
            yalign 0.19
            vbox:
                text"[attack1]"


    screen screen_attack_twov2():
        frame:
            xalign 0.53
            yalign 0.63
            vbox:
                text"[attack2]"


    screen round_onev2:
        frame:
            xalign 0.9
            yalign 0.93
            vbox:
                if round == 2:
                    $preimus1 = 100;
                text"Раунд [round]":
                    size 30
                textbutton("Закончить ход"):
                        idle_background Frame("knopka1", 12, 12)
                        hover_background Frame("knopka2", 12, 12)
                        xpadding 20
                        ypadding 10
                        xmargin 5
                        ymargin 5
                        text_idle_color "#c0c0c0"
                        text_hover_color "#ffffff"

                        action Jump("choise_dvav2")

                        #SetVariable("round",round + 1)
    screen random_damage_one:
        frame:
            xalign 0.5
            yalign 0.92
            vbox:
                textbutton("Неожиданный{p=0}удар"):
                    action Jump("choise_rndmudarv2")
                    hovered Notify("Ваша атака повышается на 0-2")
    screen preimuschestvo_onev2:
        zorder 2
        frame:

            xalign 0.15
            yalign 0.4
            vbox:
                text"Преимущество [preimus1]%"

    screen preimuschestvo_twov2:
        zorder 2
        frame:
            xalign 0.15
            yalign 0.5
            vbox:
                text"Преимущество [preimus2]%"
#///////////////////Вывод на экран героев
    show fionakarta2:
        xalign 0.5
        yalign 0.2
    show ggkarta:
        xalign 0.5
        yalign 0.75
    show screen screen_attack_onev2
    show screen screen_attack_twov2
    if time < 1:
        show screen random_damage_one
    #show screen screen_attack_four
    #show screen screen_attack_five
    #show screen screen_attack_six
    #show screen screen_attack_seven
    #show screen screen_attack_eight
    show screen preimuschestvo_onev2
    show screen preimuschestvo_twov2
    call screen round_onev2
#//////////////////////////////////////////////////////////////////////
    label choise_rndmudarv2:
    hide screen random_damage_one
    $attack2rndm = renpy.random.randint(0,2)
    $attack2 = attack2 + attack2rndm
    $time=1
    jump choise_done3v2
#///////////////////////////////////////////////////////////////////////
    label choise_dvav2:
    show neko1
    with moveinbottom
    n "Ход команды 2"
    hide neko1
    with moveoutbottom
    hide screen screen_attack_onev2
    hide screen screen_attack_twov2
    if attackcheck==1:
        $attackcheck=0
        $attack2+=1
    show fionakarta2:
        xalign 0.5
        yalign 0.5
    if mobs == 0:
        r "Призыв!"
        $mobs = 2
        $mobattack1 = 1
        $mobattack2 = 1
    else:

        r"Ядовитые пары!"
        $attack2-=1
        $attackcheck=1
    hide fionakarta2
    jump choise_done1v2
#//////////////////////////////////////////////////////////////////////
    label text1v2:
    show neko1
    with moveinbottom
    n"Победа, победа вместо обеда!"
    ficon"{cps=25}Ты же понимаешь что я тебе поддавалась?"
    a"{cps=25}Еще раунд?"
    ficon"{cps=25}А ты читаешь мои мысли."
    hide screen screen_attack_onev2
    hide screen screen_attack_twov2
    hide screen preimuschestvo_onev2
    hide screen preimuschestvo_twov2
    hide screen random_damage_one
    hide neko1
    jump label_three
#////////////////////////////////////////////////////////////////////////////
    label text2v2:
    show neko1
    with moveinbottom
    n "О нет! Ты проиграл"
    hide neko1
    with moveoutbottom
    a"{cps=25}Ты же понимаешь, что я тебе поддавался..."
    ficon"{cps=25}Хаха, ну тогда еще один раунд?"
    a"{cps=25}Читаешь мои мысли."
    hide screen screen_attack_onev2
    hide screen screen_attack_twov2
    hide screen preimuschestvo_onev2
    hide screen preimuschestvo_twov2
    hide screen random_damage_one
    jump label_three

    label label_three:
    scene black
    "{alpha=.5}{cps=25}Мы играли до четырёх часов ночи.{/alpha}"
    "{alpha=.5}{cps=25}В эти моменты я понимал чего мне не хватало.{/alpha}"
    "{alpha=.5}{cps=25}Обмениваться эмоциями во время игры,{w=0.5} вместе радоваться победам и поражениям. {w=0.5}Эти чувства незабываемы.{/alpha}"
    show laptop1
    with Fade(2.0, 0.0, 0.8, color= '#000000')
    a"{cps=25}Я что-то устал, может закончим?"
    ficon"{cps=25}Ну блииин, ты так хочешь спать? Может ещё одну игру?"
    a"{cps=25}Нет, надо идти спать, всё-таки завтра в школу."
    ficon"{cps=25}Точно, я уже забыла о школе хи-хи."
    ficon"{cps=25}Слушай, а давай как-нибудь сыграем ещё."
    a"{cps=25}Ну можно будет."
    ficon"{cps=25}Поклянись! Прикоснись к монитору и поклянись мне в этом."
    "{alpha=.5}{cps=25}Что за бред ?!{/alpha}"
    a"{cps=25}Это для тебя так серьёзно? Ну ладно, тогда ты тоже поклянись!"
    ficon"{cps=25}Клянусь!"
    a"{cps=25}Обещаю."
    a"{cps=25}И как же завтра вставать? Мы всю ночь играли."
    ficon"{cps=25}Думаю, как обычно."
    a"{cps=25}Действительно..."
    scene black
    scene laptop2
    with Fade(0.2, 0.0, 0.8, color= '#fff')
    play music "Utro.mp3"
    a"{cps=25}Аааххх..."
    "{alpha=.5}{cps=25}Упав с постели, я заставил себя встать.{/alpha}"
    a"{cps=25}Как же тяжело."
    "{alpha=.5}{cps=25}С трудом открывая глаза я решил взбодриться и заварить крепкий кофе, но он не сильно мне помог.{/alpha}"
    "{alpha=.5}{cps=25}Одевшись и собрав свои вещи, я направился в своё училище.{/alpha}"
    "{alpha=.5}{cps=25}Думаю мы с Фионой будем как сонные мухи.{/alpha}"
    play music "1234.mp3"
    scene sch
    with fade
    "{cps=25}Крейсер мне в бухту!"
    show fiona3 at right
    f"{cps=25}Физра, Физра, подкачаемся ребята!"
    hide fiona3
    show fiona2
    with Dissolve(.5)
    f"{cps=25}О, привет, классно вчера поиграли."
    a"{cps=25}Как ты стоишь на ногах?"
    f"{cps=25}Сила юности бурлит во мне, я едина с юностью!"
    "{alpha=.5}{cps=25}К сожалению силой юности я не обладал. Поэтому решил немного вздремнуть.{/alpha}"
    hide fiona2
    "{alpha=.5}{cps=25}Я уж было пошёл за свою парту и...{/alpha}"
    play sound "Punch.mp3"
    with vpunch
    stop music
    "{alpha=.5}{cps=25}Я обернулся и увидел лежащую на полу Фиону.{/alpha}"
    a"{cps=25}Эй, ты чего?"
    f"{cps=25}Да, я просто уже две недели так не сплю."
    "{alpha=.5}{cps=25}Я аккуратно приподнял её на ноги.{/alpha}"
    show fiona8 with Dissolve(.5)
    f"{cps=25}I need healing"
    "{alpha=.5}{cps=25}Похоже придётся сводить её к врачу.{/alpha}"
    "{alpha=.5}{cps=25}Я взял Фиону на плечо и пошёл в мед кабинет.{/alpha}"
    play sound "Hodba2.mp3"
    scene koridor
    with fade
    scene medkabinet
    with fade
    a"{cps=25}Здравствуйте! У меня тут больной."
    play sound "Choir.mp3" #Стоит ли добавлять этот звук?
    show tamara2 with Dissolve(.5)
    if (tamara0==1):
        t"{cps=25}Я врач. Что случилось?"
        "{alpha=.5}{cps=25}Это же та женщина, с которой я столкнулся пару дней назад.{/alpha}"
        a"{cps=25}Обморок."
        t"{cps=25}Бедная девочка. Это ты её угробил?"
        a"{cps=25}Но как я это мог сделать?"
        hide tamara2
        show tamarasboku2
        t"{cps=25}Вы, школяры, способ найдёте."
        hide tamarasboku2 with Dissolve(.5)
    else:
        "{alpha=.5}{cps=25}Резко из-за угла, словно ниндзя, выпрыгнула Тамара.{/alpha}"
        "{alpha=.5}{cps=25}Её взгляд вселял в меня страх.{/alpha}"
        t"{cps=25}Не прошло и двух дней, как ты угандошил ещё девушку."
    scene koridor
    with fade
    play sound "Punch.mp3"
    with vpunch
    "{alpha=.5}{cps=25}Врач забрала у меня Фиону и выпнула меня из кабинета.{/alpha}"
    if (tamara0==1):
        "{cps=25}..."
        "{alpha=.5}{cps=25}Однако уже через 5 минут я получил её обратно.{/alpha}"
    else:
        "{cps=25}Недавно я узнал о личности этого врача."
        "{alpha=.5}{cps=25}Это Тамара, женщина 30 лет, не замужем, но что интересно, она давний игрок в PG Online, даже когда-то игравший на про сцене.{/alpha}"
        "{alpha=.5}{cps=25}Обо многом я хотел бы её спросить, но делать это, в связи наших плохих отношений, не буду.{/alpha}"
        "{alpha=.5}{cps=25}Через 5 минут я дверь отворилась.{/alpha}"
    show tamara2 with Dissolve(.5)
    t"{cps=25}Ей нужно отоспаться, так что просто проводи её домой."
    a"{cps=25}Будет сделано!"
    "{alpha=.5}{cps=25}Другой ответ я не смог бы ей сказать.{/alpha}"
    play music "veter.mp3"
    show street4
    with Fade(2.0, 0.0, 0.8, color= '#000000')
    pause
    "{alpha=.5}{cps=25}Мы шли медленно, поэтому я замерзал.{/alpha}"
    "{alpha=.5}{cps=25}Фиона молчала, что было для неё нестандартно.{/alpha}"
    "{alpha=.5}{cps=25}Так молча мы дошли до её дома.{/alpha}"
    ficon"{cps=25}Ну дальше я сама."
    a"{cps=25}Окей."
    ficon"{cps=25}Спасибо за ночь.{w=1} Никто раньше не катал со мной до 4 утра, когда нужно вставать в 7 утра."
    ficon"{cps=25}Сергей, считай, что за сегодняшний день ты заработал от меня одно очко уважения."
    a"{cps=25}Я сделал всё, что должен был."
    "{alpha=.5}{cps=25}С положительными эмоциями я направился домой.{/alpha}"
    play music "Relax.mp3"
    scene black
    with Fade(2.0, 0.0, 0.8, color= '#000000')
    "{cps=25}Итак, с кем мне ещё провести время?"
    if score2 == 1 and score3 == 1:
        menu:
            "C Кристиной":
                $ score2 = score2 +2
                $tamara0 = tamara0 + 1
                jump Kristina1
            "С Алёной":
                $ score3 = score3 +2
                $tamara0 = tamara0 + 1
                jump Alyona1
    else:
        jump All_done

label Kristina1:
#    "[score2]"
    "{cps=25}Решено, сегодня подойду к Кристине."
    play music "Street.mp3"
    scene schooltrip
    with fade
    scene sch
    with fade
    play music "School.mp3"
    "{alpha=.5}{cps=25}Так как Кристина училась в другом классе, нужно было спуститься на этаж ниже.{/alpha}"
    "{alpha=.5}{cps=25}Я зашёл в её класс, однако её уже не было.{/alpha}"
    "{alpha=.5}{cps=25}Спросив девочек которые убирались в кабинете, я узнал, что она в бассейне.{/alpha}"
    play sound "Hodba2.mp3"
    scene koridor
    with Dissolve(.5)
    "{alpha=.5}{cps=25}Кристина была немного замкнутой и довольно стеснительной девушкой, эти черты характера шли во вред нашей команде.{/alpha}"
    "{cps=25}Если я скажу ей об этом, то она может обидеться на меня."
    "{cps=25}Надо будет как - то помочь Кристине стать более открытой."
    stop music fadeout 1
    scene pool
    with Dissolve(.5)
    "{alpha=.5}{cps=25}В этом просторном помещении было темновато.{/alpha}"
    "{cps=25}Я играл в хоррор с похожим бассейном."
    "{cps=25}Там за мной гонялась какая-то девочка, которая пыталась меня зарезать."
    "{cps=25}А вот и Кристина, она практически сразу меня заметила.{w=1} Надеюсь она не утопит меня."
    scene kristinainpool
    with fade
    play music "swimming.mp3"
    "{alpha=.5}{cps=25}Кристина изнурённо плавала в бассейне.{/alpha}"
    "{alpha=.5}{cps=25}Скорее всего она готовится к соревнованиям.{/alpha}"
    "{alpha=.5}{cps=25}Однако мне всё - таки кажется, что она переусердствует.{/alpha}"
    "{alpha=.5}{cps=25}Я решил подойти ближе, но в этот момент она сделала глубокий толчок под воду.{/alpha}"
    stop music fadeout 1
    scene black
    a"{cps=25}"
    a"{cps=25}."
    a"{cps=25}.."
    a"{cps=25}..."
    scene pool
    with fade
    play music "trevoga.mp3"
    "{cps=25}Ну и где она?"
    "{alpha=.5}{cps=25}Неужели лучшая пловчиха в нашей школе решила утонуть.{/alpha}"
    scene black
    "{alpha=.5}{cps=25}Я резко прыгнул в воду и попытался найти её.{/alpha}"
    a"{cps=25}Вот она!"
    "{alpha=.5}{cps=25}Говорить вслух под водой было плохой идеей.{/alpha}"
    "{alpha=.5}{cps=25}Хоть было и тяжело, но я вытащил её.{/alpha}"
    scene kristinabezsoznania1
    with circleirisin
    "{alpha=.5}{cps=25}Что делать дальше?{/alpha}"
    menu:#хз добавлять ли арты
        "Массаж сердца":
            jump vibor3
        "Исскуственное дыхание":
            jump vibor4
    label vibor3:
    scene black
    "{cps=25}К сожалению многого в спасении людей я не знал. Поэтому просто нашёл сердце и делал нажатия руками."
    "{cps=25}."
    "{cps=25}.."
    "{cps=25}..."
    show kristinabezsoznania1
    with fade
    "{cps=25}Не помогает, нужно что-то ещё."
    menu:
            "Исскуственное дыхание":
                jump vibor4v2
    label vibor4v2:
    scene black
    "{cps=25}Я набрал в себя воздух и попытался сделать искусственное дыхание."
    jump vibor3and4_done

    label vibor4:
    scene black
    "{cps=25}Я набрал в себя воздух и попытался сделать искусственное дыхание."
    show kristinabezsoznania1
    with fade
    "{cps=25}Не помогает, нужно что-то ещё."
    menu:
        "Массаж сердца":
            jump vibor3v2
    label vibor3v2:
    scene black
    "{cps=25}К сожалению многого в спасении людей я не знал. Поэтому просто нашёл сердце и делал нажатия руками."
    "{cps=25}."
    "{cps=25}.."
    "{cps=25}..."
    jump vibor3and4_done

    label vibor3and4_done:
    stop music fadeout 1
    scene kristinabezsoznania1
    with fade
    "{alpha=.5}{cps=25}Отчаянно повторяя эти действия, я не заметил, как прошла уже минута.{/alpha}"
    "{alpha=.5}{cps=25}Безрезультатные попытки чуть не заставили опустить руки, но на мое лицо полилась вода.{/alpha}"
    "{alpha=.5}{cps=25}Это была вода Кристины,{w=1} а точнее вода из её рта.{/alpha}"
    scene kristinabezsoznania3
    a"{cps=25}Очнулась!"
    k"{cps=25}Кх..Кх"
    "{alpha=.5}{cps=25}Похоже ей трудно говорить.{/alpha}"
    k"{cps=25}Я в порядке."
    a"{cps=25}Тебя нужно отвезти к врачу."
    "{alpha=.5}{cps=25}Я поднял её и повел в мед кабинет.{/alpha}"
    play sound "Hodba2.mp3"
    scene koridor
    with fade
    scene medkabinet
    with fade
    show tamara2 with Dissolve(.5)
    if (tamara0==1):
        t"{cps=25}Я врач. Что случилось?"
        "{alpha=.5}{cps=25}Это же та женщина, с которой я столкнулся пару дней назад.{/alpha}"
        a"{cps=25}Она тонула."
        t"{cps=25}Могу поспорить что это из-за тебя."
        "{alpha=.5}{cps=25}После этих бредней я резко захлопнул дверь.{/alpha}"
    else:
        "{alpha=.5}{cps=25}Резко из-за угла, словно ниндзя, выпрыгнула Тамара.{/alpha}"
        "{alpha=.5}{cps=25}Её взгляд вселял в меня страх.{/alpha}"
        t"{cps=25}Не прошло и двух дней, как ты угандошил ещё девушку."
        t"{cps=25}А может ты к ней приставал...Изварщенец!"
        "{alpha=.5}{cps=25}После этих бредней я резко захлопнул дверь.{/alpha}"

    hide tamara2 with Dissolve(.5)
    scene koridor
    with fade
    if (tamara0==2):
        "{cps=25}Недавно я узнал о личности этого врача."
        "{alpha=.5}{cps=25}Это Тамара, женщина 30 лет, не замужем, но что интересно, она давний игрок в 'Герои-Рыцари и Маги', даже когда-то игравший на про сцене.{/alpha}"
        "{alpha=.5}{cps=25}Обо многом я хотел бы её спросить, но делать это, в связи наших плохих отношений, не буду.{/alpha}"

    "{alpha=.5}{cps=25}Через 5 минут дверь отворилась.{/alpha}"
    show tamara2
    t"{cps=25}Чего стоишь без дела?!"
    t"{cps=25}Отведи её бысто домой, пусть завтра в школу не приходит,а ты потом её проведай."
    a"{cps=25}Хорошо."
    play music "veter.mp3"
    show street4
    with Fade(2.0, 0.0, 0.8, color= '#000000')
    pause
    "{alpha=.5}{cps=25}Дом Кристины находился недалеко.{/alpha}"
    "{alpha=.5}{cps=25}Когда мы вышли из школы, она тихо сказала.{/alpha}"
    kicon"{cps=25}Спасиб.."
    a"{cps=25}Не надо лишних слов! Я сделал то, что должен был."
    "{alpha=.5}{cps=25}Чувство героизма переполняло меня.{/alpha}"
    a"{cps=25}Эй, а зачем ты так напрягалась в бассейне?"
    kicon"{cps=25}Я не напрягалась, а скорее торопилась."
    kicon"{cps=25}Мы же вроде как собираемся выиграть турнир, а у меня ещё много дел помимо этого."
    kicon"{cps=25}Например, соревнования по плаванию."
    kicon"{cps=25}Поэтому я старалась всё делать в спешке и вечером тренировать свою игру."
    a"{cps=25}..."
    "{alpha=.5}{cps=25}Я не знал, что ответить.{/alpha}"
    stop music fadeout 1
    scene black
    "{alpha=.5}{cps=25}...{/alpha}"
    scene kristinahome2
    with fade
    "{alpha=.5}{cps=25}Через какое-то время мы пришли к её дому.{/alpha}"
    show kristina4 with Dissolve(.5)
    k"{cps=25}У меня к тебе вопрос."
    k"{cps=25}Ты так стараешься победить в турнире.Зачем тебе это? На что ты потратишь призовые?"
    menu:
        "Мне нужны деньги на лечение матери.":
            $score2 = score2 + 2
            jump choise3N1
        "Я пока не знаю.":
            jump choise3N2
    label choise3N1:
    a"{cps=25}Мне нужны деньги на лечение матери."
    hide kristina4
    show kristina2
    k"{cps=25}Что же с ней случилось?"
    a"{cps=25}Я точно не знаю. Отказ нижних конечностей."
    k"{cps=25}Тебе, наверное, тяжело."
    a"{cps=25}Я в норме, просто мама единственный близкий мне человек, поэтому я сделаю всё для неё."
    k"{cps=25}Сочувствую."
    a"{cps=25}Всё в порядке."
    jump choise3_done
    label choise3N2:
    a"{cps=25}Мне нужны деньги на лечение матери."
    hide kristina4
    show kristina2
    k"{cps=25}Я вот тоже."
    hide kristina2
    show kristina3
    k"{cps=25}Может буду покупать каждый день тортики."
    "{alpha=.5}{cps=25}Я улыбнулся.{/alpha}"
    a"{cps=25}То что я не знаю на что потрачу деньги не значит, что у меня нет воли к победе."
    hide kristina3
    show kristina1
    k"{cps=25}Понимаю, тогда я буду стараться как никогда для победы!"
    a"{cps=25}Ты уже сделала очень много. Не перенапрягайся."
    k"{cps=25}Хорошо, я обещаю."
    jump choise3_done
    label choise3_done:
    a"{cps=25}Кстати, как я вижу тебе уже немного лучше, может сходим поиграем?"
    k"{cps=25}О чем ты говоришь, мы играем целыми днями."
    a"{cps=25}Я не о наших компьютерах, я имею в виду игровой клуб."
    "{cps=25}Возможно, я так смогу её раскрыть."
    a"{cps=25}В обстановке компьютерного клуба ты сможешь больше посвятить себя обществу геймеров."
    a"{cps=25}Я хочу, чтобы ты смогла лучше понимать игру."
    k"{cps=25}Давай попробуем, я напишу тебе, а пока мне надо переодеться."
    a"{cps=25}Хорошо."
    hide kristina1 with Dissolve(.5)
    "{alpha=.5}{cps=25}Кристина поднялась на второй этаж и помахала мне рукой.{/alpha}"
    play music "Street.mp3"
    scene schooltrip
    with fade
    pause
    play music "Kitchen.mp3"
    scene kit
    with fade
    pause
    scene laptop2
    with fade
    stop music fadeout 1
    pause
    scene black
    with fade
    "{alpha=.5}{cps=25}...{/alpha}"
    scene laptop2
    with fade
    pause
    "{alpha=.5}{cps=25}Через некоторое время она мне написала.{/alpha}"
    "{cps=25}Пойду встречу её."
    play music "Street.mp3"
    scene schooltrip
    with fade
    pause
    scene kristinahome2
    with fade
    show kristina5
    "{alpha=.5}{cps=25}Она увидела меня и радостно улыбнулась.{/alpha}"
    "{alpha=.5}{cps=25}Сейчас Кристина выглядит даже слишком радостной.{/alpha}"
    a"{cps=25}Ну что, пойдём?"
    k"{cps=25}Ну пошли."
    hide kristina5
    play music "csounds.mp3"
    scene club
    with flashbulb
    "{alpha=.5}{cps=25}В наше время компьютерные клубы очень популярны среди молодёжи, да и среди некоторых взрослых.{/alpha}"
    "{alpha=.5}{cps=25}Некоторые просиживают в них почти весь день.{/alpha}"
    "{alpha=.5}{cps=25}Все весело играли в свои игры и развлекались на всю катушку.{/alpha}"
    "{alpha=.5}{cps=25}Мы стояли у стойки и ждали своей очереди.{/alpha}"
    "{alpha=.5}{cps=25}После оплаты я показал Крестине, где стоят наши компьютеры, и сел рядом с ней.{/alpha}"
    show kristina5
    k"{cps=25}Ну-у что мы будем делать?"
    a"{cps=25}Заходи в \"Герои-Рыцари и Маги\".Я прелагаю сыграть в другие режимы, например, в 3 на 3."
    hide kristina5
    "{alpha=.5}{cps=25}Осмотрев часть компьютерного клуба, я заметил ребят, которые играют в ту же игру, что и мы.{/alpha}"
    a"{cps=25}Ребят, не хотите сыграть несколько каток?"
    "{alpha=.5}{cps=25}Парни кивнули, и видимо главный из них поздоровался со мной.{/alpha}"
    show denis1
    define noname = Character('????', color="#ffffff")
    noname"{cps=25}Давайте я зайду за вас, а мои друзья будут играть против нас."
    a"{cps=25}Давай, конечно."
    "{alpha=.5}{cps=25}Парень присоединился к нашему отряду.{/alpha}"
    define d = Character('Денис', color="#ffffff")
    d"{cps=25}Меня, кстати, зовут Денис."
    a"{cps=25}Я Сергей, а вон там моя подруга Кристина."
    hide denis1
    "{alpha=.5}{cps=25}Кристина неловко помахала рукой.{/alpha}"
    "{alpha=.5}{cps=25}Партия началась, и мы приступили к сражению.{/alpha}"
    scene black
    with fade
    "{alpha=.5}{cps=25}...{/alpha}"
    scene club
    with fade
    d"{cps=25}Воу, это был хороший момент. Сергей, ты круто играешь."
    a"{cps=25}Спасибо, но ничего особенного, этот приём использует почти половина игроков."
    kicon"{cps=25}Что? И ты мне об этой фишке не сказал."
    "{alpha=.5}{cps=25}Я стал замечать, что Кристина советуется с некоторыми игроками о своей стратегии.{/alpha}"
    a"{cps=25}Похоже, ты вжилась в этот коллектив."
    kicon"{cps=25}Да-а?А я сама и не заметила."
    scene black
    with fade
    "{alpha=.5}{cps=25}Мы играли почти весь вечер, и наше время почти подошло к концу."
    scene club
    with fade
    a"{cps=25}Фуух, я даже не заметил, как быстро прошло время."
    show kristina5:
        xalign 0.3
        yalign 1.0
    k"{cps=25}Я думаю мне пора домой."
    show denis1:
        xalign 0.6
        yalign 1.0
    d"{cps=25}Давайте ещё продлим на час?"
    a"{cps=25}Спасибо за предложение, но я как-то устал."
    a"{cps=25}Надеюсь, мы ещё встретимся."
    "{alpha=.5}{cps=25}Денис кивнул мне и продолжил играть."
    hide kristina5
    hide denis1
    stop music fadeout 1
    scene black
    with fade
    "{alpha=.5}{cps=25}Я проводил Кристину до дома."
    scene kristinahome2
    with fade
    show kristina5
    k"{cps=25}Это был интересный опыт, спаcибо тебе."
    a"{cps=25}Пока."
    hide krisina5
    "{alpha=.5}{cps=25}С чувством выполненного долга я направился домой."
    "{alpha=.5}{cps=25}Скорее всего, именно излишнее старание было причиной её плохой игры."
    "{cps=25}Похоже, сегодня мне удалось её хотя бы чуточку раскрыть и промотивировать."
    play music "Relax.mp3"
    scene black
    with Fade(2.0, 0.0, 0.8, color= '#000000')
    "{cps=25}Итак, с кем мне ещё провести время?"
    if score1 == 1 and score3 == 1:
        menu:
            "С Фионой":
                $ score1 = score1 + 2
                $tamara0 = tamara0 + 1
                jump Fiona1
            "С Алёной":
                $ score3 = score3 + 2
                $tamara0 = tamara0 + 1
                jump Alyona1
    else:
        jump All_done

label Alyona1:
stop music fadeout 1
"{alpha=.5}{cps=25}Встретиться с Алёной было проблематично, так как она не училась в школе."
"{cps=25}Сегодня вечером нужно будет ей написать о встрече."
scene schooltrip
with fade
scene sch
with fade
scene schooltrip
with fade
play music "trevoga.mp3"
"{alpha=.5}{cps=25}Сегодня безоблачно."
"{alpha=.5}{cps=25}Я шёл по привычному маршруту, как вдруг из-за угла в мою сторону выбежала Алёна."
show alyona6 with Dissolve(.5)
l"{cps=25}А! Это ты!"
starik"{cps=25}СТОЯТЬ!"
starik"{cps=25}Эй ты, отдай её нам."
l"{cps=25}Бежим!"
"{alpha=.5}{cps=25}Алёна схватила меня за руку, и мы рванули со всех ног."
hide alyona2 with Dissolve(.5)
scene street3 with fade
"{alpha=.5}{cps=25}Мы пробежали мимо площади."
scene kristinahome2 with fade
"{alpha=.5}{cps=25}Скрылись в улицах."
scene black
"{alpha=.5}{cps=25}И прибежали к моему дому."
"{alpha=.5}{cps=25}Я остановился."
a"{cps=25}Стой! Мы оторвались."
l"{cps=25}Точно?"
a"{cps=25}Да."
scene alenaseed with Dissolve(.5)
####################################################################################################Тут остановить музыку
stop music fadeout 1
"{alpha=.5}{cps=25}Алёна упала на колени.Я тоже очень устал."
"{cps=25}Так кто это был?"
l"{cps=25}Это очень плохие люди. Они пытаются разрушить мои планы по победе в турнире , а также запугать меня и забрать моё имущество, включая компьютер."
a"{cps=25}Не лучше ли написать заявление в полицию?"
l"{cps=25}Нет, мне очень страшно, можно денёк пожить у тебя?"
"{cps=25}?"
a"{cps=25}Что? А почему ты не пойдёшь к Кристине или Фионе?"
l"{cps=25}Дурак, я же не знаю, где они живут."
"{alpha=.5}{cps=25}Думаю случай важный, так что я решил согласиться."
a"{cps=25}И что ты предлагаешь? Сидеть у меня и просто ждать?"
l"{cps=25}Конечно нет, я просто пережду у тебя ночь и пойду в полицию."
a"{cps=25}Хорошо.{w=1.0}.наверное."
a"{cps=25}Тогда добро пожаловать!"
scene kit with Dissolve(.5)
"{alpha=.5}{cps=25}Когда мы вошли в дом, ко мне начали приходить дурные мысли о том, что мы с Алёной останемся вдвоём на ночь одни."
"{alpha=.5}{cps=25}Однако всего пару слов смогли меня переубедить."
l"{cps=25}Где комп?"
a"{cps=25}В моей комнате, я покажу."
scene black
"{alpha=.5}{cps=25}Я посадил её за своё рабочее кресло и пошел готовить еду. Ну как еду, бутерброды с чаем."
a"{cps=25}Bellissimo."
"{alpha=.5}{cps=25}Я принёс своё фирменное блюдо и сел на кровать."
play music "Computer.mp3"
scene alenazakompom
"{alpha=.5}{cps=25}Прошло где-то 2 часа."
"{alpha=.5}{cps=25}Я следил за игрой Алёны, как всегда она нападала необдуманно и агрессивно, однако часто такая тактика венчалась успехом из-за элемента неожиданности."
l"{cps=25}Ну что, как тебе моя игра?"
a"{cps=25}Неплохо, но есть ошибки."
l"{cps=25}Что? Да ты хуже меня игрешь, как ты смеешь видеть у меня ошибки."
a"{cps=25}Но ты проиграла прошлую игру."
l"{cps=25}Да это союзники плохие и вообще, вообще... Ой всё!"
"{alpha=.5}{cps=25}Исчерпав аргументы Алёна отвернулась."
"{alpha=.5}{cps=25}Между тем она проиграла ещё одну игру."
l"{cps=25}Ну это, что там за ошибки у меня?"
scene black
"{alpha=.5}{cps=25}Я рассказал ей о правильном позиционировании в битве, таймингах и многом другом."
a"{cps=25}...Вот здесь 3 секунды ждёшь, а потом в атаку."
scene alenazakompom
l"{cps=25}Понятно, а ты умнее, чем я ожидала."
a"{cps=25}Я польщён."
l"{cps=25}Слушай Сергей, нужно тебе сказать кое-что важное."
a"{cps=25}И что же?"
l"{cps=25}В общем, те бандиты, которые гнались сегодня за нами, это.."
l"{cps=25}Это мои родители."
"{cps=25}??"
a"{cps=25}Какие к чёрту родители бегают с дубинкой по городу за своим ребёнком?!"
l"{cps=25}Они с чего-то подумали, что меня кто - то запугал и украл."
a"{cps=25}И этот кто-то - я."
l"{cps=25}Похоже на то."
a"{cps=25}А почему ты убегала?"
l"{cps=25}У нас произошёл конфликт. Они считают, что компьютер мешает мне жить, и что я должна его выбросить и найти работу."
"{alpha=.5}{cps=25}Я заметил это, но похоже Алёна на пару лет меня старше."
a"{cps=25}Жёстко, хотя наверное это не повод убегать."
l"{cps=25}Но что же мне делать? Ведь я могу заработать на турнире неплохую сумму денег."
menu:
    "Я пойду к твоим родителям.":
        jump Alena1vb1
    "Ты пойдёшь к своим родителям":
        jump Alena1vb2
label Alena1vb1:
a"{cps=25}Я пойду к твоим родителям и всё объясню."
l"{cps=25}Но они же думают, что ты меня украл."
a"{cps=25}Делов то, представлюсь твоим капитаном, и они всё поймут."
l"{cps=25}Ну, это в лучшем случае."
l"{cps=25}Я буду следить за тобой. Для подстраховки."
a"{cps=25}Хорошо."
scene laptop2
play music "Utro.mp3"
"{alpha=.5}{cps=25}Я проснулся первым."
"{alpha=.5}{cps=25}Нужно было разбудить Алёну."
a"{cps=25}Подъём!"
l"{cps=25}Ещё 5 минут."
"{alpha=.5}{cps=25}Алёна спряталась под одеялом."
a"{cps=25}Вставай, мне ещё в школу потом."
scene black
"{alpha=.5}{cps=25}Я стянул с Алёны одеяло, однако не учёл, что она была в одних трусах."
l"{cps=25}Извращуга!"
"{alpha=.5}{cps=25}Я отвернулся и пошёл на первый этаж."
scene schooltrip with fade
"{alpha=.5}{cps=25}Как и было решено, мы пошли к родителям Алёны."
scene alenahomev1 with fade
stop music fadeout 1
"{alpha=.5}{cps=25}Я постучался в дверь, а Алёна спряталась за дерево."
play sound "Udar.mp3"
a"{cps=25}Здравствуйте, я пришёл поговорить."
show starik at right with Dissolve(.5)
starik"{cps=25}А? Это тот самый парнишка. А ну говори, где наша дочь."
a"{cps=25}Я скажу, если вы меня выслушаете."
starik"{cps=25}Что же ты хочешь сказать?"
a"{cps=25}Что вашу дочь я не крал, а она сама сбежала."
a"{cps=25}Из - за того что вы не считете доход в киберспорте нормальным заработком."
starik"{cps=25}Да как вообще можно получать деньги играя?"
a"{cps=25}Я могу всё доказать."
"{alpha=.5}{cps=25}Я показал ему официальную страницу турнира и призовой фонд."
starik"{cps=25}Этого недостаточно."
a"{cps=25}Тогда почему бы вам не прийти самим на турнир."
starik"{cps=25}Это хороший вариант, только сначала верни мою дочь."
a"{cps=25}Только если вы дадите ей тренироваться с нами."
"{alpha=.5}{cps=25}Жестом головы он показал своё согласие, тогда я позвал Алёну, прячущуюся за деревом."
starik"{cps=25}Ладно, посмотрим, что у вас за турнир. Извини за грубость, доченька."
show alyona4
l"{cps=25}И ты меня извини."
starik"{cps=25}Пошли к матери."
l"{cps=25}Угу."
l"{cps=25}Спасибо, Серёжа, что помог и приютил этой ночью."
starik"{cps=25}Что? Ты спала у него дома?!"
"{alpha=.5}{cps=25}Он гневно посмотрел на меня."
a"{cps=25}До свидания!"
scene black
"{alpha=.5}{cps=25}Я развернулся и быстрым шагом, который можно было считать бегом ушёл оттуда."
"{alpha=.5}{cps=25}С позитивными мыслями я вернулся домой."
"{alpha=.5}{cps=25}Но позже, правда, вспомнил, что мне нужно было пойти в школу."
a"{cps=25}Аааааа."
play music "Relax.mp3"
"{cps=25}Итак, с кем мне ещё провести время?"
if score1 == 1 and score2 == 1:
    menu:
        "С Фионой":
            $ score1 = score1 +2
            jump Fiona1
        "С Кристиной":
            $ score2 = score2 +2
            jump Kristina1
else:
    jump All_done

label Alena1vb2:
a"{cps=25}Ты должна сама решить все проблемы на корню."
a"{cps=25}А я для поддержки буду следить за тобой."
l"{cps=25}Не знаю, смогу ли я."
a"{cps=25}Ты должна."
l"{cps=25}Постараюсь."
scene laptop2
play music "Utro.mp3"
"{alpha=.5}{cps=25}Я проснулся первым."
"{alpha=.5}{cps=25}Нужно было разбудить Алёну."
a"{cps=25}Подъём!"
l"{cps=25}Ещё 5 минут."
"{alpha=.5}{cps=25}Алёна спряталась под одеялом."
a"{cps=25}Вставай, мне ещё в школу потом."
scene black
"{alpha=.5}{cps=25}Я стянул с Алёны одеяло, однако не учёл, что она была в одних трусах."
l"{cps=25}Извращуга!"
"{alpha=.5}{cps=25}Я отвернулся и пошёл на первый этаж."
scene schooltrip with fade
"{alpha=.5}{cps=25}Как и было решено, мы пошли к родителям Алёны."
scene alenahomev1 with fade
stop music fadeout 1
"{alpha=.5}{cps=25}Алёна постучала в дверь, а я спрятался за деревом."
"{alpha=.5}{cps=25}Из двери вышел её отец и началаь беседа.К сожалению я ничего не слышал."
"{cps=25}."
"{cps=25}.."
"{cps=25}..."
"{cps=25}Похоже у них не клеится разговор и придётся вмешаться."
a"{cps=25}Извините, можно вмешаться в вашу беседу."
show starik at right
show alyona4
starik"{cps=25}А? Это тот самый парнишка."
starik"{cps=25}Дочь мне всё рассказала. О том, что можно зарабатывать на играх и подобную чушь."
a"{cps=25}Почему чушь? Всё серьёзно. Взять хотя бы турнир в котором мы участвуем."
"{alpha=.5}{cps=25}Я показал ему официальную страницу турнира и призовой фонд."
starik"{cps=25}Этого недостаточно."
a"{cps=25}Тогда почему бы вам не прийти самим на турнир."
starik"{cps=25}Хм.. ладно, я признаю свою ошибку, если вам вручат деньги."
a"{cps=25}Отлично, тогда вы дадите Алёне тренироваться с командой!"
starik"{cps=25}Хорошо."
"{alpha=.5}{cps=25}Отец огляделся вокруг и зашёл в дом."
hide starik
l"{cps=25}Спасибо Сергей, я пойду тогда тоже."
a"{cps=25}Мы выиграем турнир ради тебя."
scene black
"{alpha=.5}{cps=25}С позитивными мыслями я вернулся домой."
"{alpha=.5}{cps=25}Но позже, правда, вспомнил, что мне нужно было пойти в школу."
a"{cps=25}Аааааа..."
play music "Relax.mp3"
"{cps=25}Итак, с кем мне ещё провести время?"
if score1 == 1 and score2 == 1:
    menu:
        "С Фионой":
            $ score1 = score1 +2
            jump Fiona1
        "С Кристиной":
            $ score2 = score2 +2
            jump Kristina1
else:
    jump All_done

label All_done:
"{cps=25}Похоже ни с кем, ибо время поджимает."
"{alpha=.5}{cps=25}Итак, сегодня квалификации на турнир."
"{alpha=.5}{cps=25}Я потратил много сил на нашу подготовку."
scene black
"{alpha=.5}{cps=25}Моя новая команда."
show fiona2:
    xalign 0.2
    yalign 1.0
"{alpha=.5}{cps=25}Фиона."
show kristina2
"{alpha=.5}{cps=25}Кристина."
show alyona1:
        xalign 0.8
        yalign 1.0
"{alpha=.5}{cps=25}Алёна."
"{alpha=.5}{cps=25}Мы очень сблизились за последние дни."
"{alpha=.5}{cps=25}Думаю так и должно быть в настоящем коллективе."
hide fiona2
hide kristina2
hide alyona1
play music "Computer.mp3"
scene laptop1
with Fade(2.0, 0.0, 0.8, color= '#000000')
pause
a"{cps=25}Ну что начинаем?"
kicon"{cps=25}Начнём!"
ficon"{cps=25}Да прибудет с нами удача!"
licon"{cps=25}Да."
jump previugame2
label choise1n2:
hide screen restartn2
$game1vibor+=1
hide screen kristina_karta1n2
hide screen fiona_karta1n2
hide screen alena_karta1n2
hide screen gg_karta1n2
show ggkarta1:
    xalign 0.3
    yalign 0.6
show alenakarta1:
    xalign 0.1
    yalign 0.6
show fionakarta1:
    xalign 0.3
    yalign 0.2
show kristinakarta2:
    xalign 0.1
    yalign 0.2
if game1vibor==1:
    if sluchain1 == 1:
        $attack+=1;
        show sword1:
            xalign 0.1
            yalign 0.04
        pause 2
        hide kristinakarta2
        jump choise0n2
    else:
        hide fionakarta1
        hide alenakarta1
        hide ggkarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Перейти к защите":
                jump armor_two
else:
    if game1vibor==2:
        if sluchain2 == 1:
            $attack+=1;
            show sword2:
                xalign 0.15
                yalign 0.04
            pause 2
            hide kristinakarta2
            jump choise0n2
        else:
            hide fionakarta1
            hide alenakarta1
            hide ggkarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Перейти к защите":
                    jump armor_two
    else:
        if game1vibor==3:
            if sluchain3 == 1:
                $attack+=1;
                show sword3:
                    xalign 0.2
                    yalign 0.04
                pause 2
                hide kristinakarta2
                jump choise0n2
            else:
                hide fionakarta1
                hide alenakarta1
                hide ggkarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Перейти к защите":
                        jump armor_two


label choise2n2:
hide screen restartn2
$game1vibor+=1
hide screen kristina_karta1n2
hide screen fiona_karta1n2
hide screen alena_karta1n2
hide screen gg_karta1n2
show ggkarta1:
    xalign 0.3
    yalign 0.6
show alenakarta1:
    xalign 0.1
    yalign 0.6
show fionakarta2:
    xalign 0.3
    yalign 0.2
show kristinakarta1:
    xalign 0.1
    yalign 0.2
if game1vibor==1:
    if sluchain1 == 2:
        $attack+=1;
        show sword1:
            xalign 0.1
            yalign 0.04
        pause 2
        hide fionakarta2
        jump choise0n2
    else:
        hide kristinakarta1
        hide alenakarta1
        hide ggkarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Перейти к защите":
                jump armor_two
else:
    if game1vibor==2:
        if sluchain2 == 2:
            $attack+=1;
            show sword2:
                xalign 0.15
                yalign 0.04
            pause 2
            hide fionakarta2
            jump choise0n2
        else:
            hide kristinakarta1
            hide alenakarta1
            hide ggkarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Перейти к защите":
                    jump armor_two
    else:
        if game1vibor==3:
            if sluchain3 == 2:
                $attack+=1;
                show sword3:
                    xalign 0.2
                    yalign 0.04
                pause 2
                hide fionakarta2
                jump choise0n2
            else:
                hide kristinakarta1
                hide alenakarta1
                hide ggkarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Перейти к защите":
                        jump armor_two


label choise3n2:
hide screen restartn2
$game1vibor+=1
hide screen kristina_karta1n2
hide screen fiona_karta1n2
hide screen alena_karta1n2
hide screen gg_karta1n2
show ggkarta1:
    xalign 0.3
    yalign 0.6
show alenakarta2:
    xalign 0.1
    yalign 0.6
show fionakarta1:
    xalign 0.3
    yalign 0.2
show kristinakarta1:
    xalign 0.1
    yalign 0.2
if game1vibor==1:
    if sluchain1 == 3:
        $attack+=1;
        show sword1:
            xalign 0.1
            yalign 0.04
        pause 2
        hide alenakarta2
        jump choise0n2
    else:
        hide kristinakarta1
        hide fionakarta1
        hide ggkarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Перейти к защите":
                jump armor_two
else:
    if game1vibor==2:
        if sluchain2 == 3:
            $attack+=1;
            show sword2:
                xalign 0.15
                yalign 0.04
            pause 2
            hide alenakarta2
            jump choise0n2
        else:
            hide kristinakarta1
            hide fionakarta1
            hide ggkarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Перейти к защите":
                    jump armor_two
    else:
        if game1vibor==3:
            if sluchain3 == 3:
                $attack+=1;
                show sword3:
                    xalign 0.2
                    yalign 0.04
                pause 2
                hide alenakarta2
                jump choise0n2
            else:
                hide kristinakarta1
                hide fionakarta1
                hide ggkarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Перейти к защите":
                        jump armor_two
label choise4n2:
hide screen restartn2
$game1vibor+=1
hide screen kristina_karta1n2
hide screen fiona_karta1n2
hide screen alena_karta1n2
hide screen gg_karta1n2
show ggkarta2:
    xalign 0.3
    yalign 0.6
show alenakarta1:
    xalign 0.1
    yalign 0.6
show fionakarta1:
    xalign 0.3
    yalign 0.2
show kristinakarta1:
    xalign 0.1
    yalign 0.2
if game1vibor==1:
    if sluchain1 == 4:
        $attack+=1;
        show sword1:
            xalign 0.1
            yalign 0.04
        pause 2
        hide ggkarta2
        jump choise0n2
    else:
        hide kristinakarta1
        hide fionakarta1
        hide alenakarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Перейти к защите":
                jump armor_two
else:
    if game1vibor==2:
        if sluchain2 == 4:
            $attack+=1;
            show sword2:
                xalign 0.15
                yalign 0.04
            pause 2
            hide ggkarta2
            jump choise0n2
        else:
            hide kristinakarta1
            hide fionakarta1
            hide alenakarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Перейти к защите":
                    jump armor_two
    else:
        if game1vibor==3:
            if sluchain3 == 4:
                $attack+=1;
                show sword3:
                    xalign 0.2
                    yalign 0.04
                pause 2
                hide alenakarta2
                jump choise0n2
            else:
                hide kristinakarta1
                hide fionakarta1
                hide ggkarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Перейти к защите":
                        jump armor_two

label previugame2:
    menu:
        "Прочитать правила":
            jump pravila2
        "Начать игру":
            jump game2
    label pravila2:
    scene pravila1
    "Приветсвую в мини-игре!"
    "Для победы над противником вам нужно набрать достаточное количество атаки и защиты."
    "Очки атаки вы зарабатываете,поочерёдно угадывая синие карты, которые открылись после начала игры."
    "Очки защиты вы зарабатываете,поочерёдно угадывая красные карты, которые открылись после начала игры."
    menu:
        "Начать игру":
            jump game2
    label game2:
    "У противника сильная атака, поэтому вам нужно больше фокусироваться на защите."
    hide screen kristina_karta1n2
    hide screen fiona_karta1n2
    hide screen alena_karta1n2
    hide screen gg_karta1n2
    window hide
    scene background4
    $armor = 0
    $attack = 0
    $game1vibor2=0
    $game1vibor=0
    $sluchain1 = 0
    $sluchain2 = 0
    $sluchain3 = 0
    $sluchain4 = 0
    screen restartn2:
        imagebutton xalign 0.5 yalign 0.2:
            idle ("restart.png")
            action Jump("previugame2")
    show kristinakarta1:
        xalign 0.1
        yalign 0.2
    show fionakarta1:
        xalign 0.3
        yalign 0.2
    show alenakarta1:
        xalign 0.1
        yalign 0.6
    show ggkarta1:
        xalign 0.3
        yalign 0.6
    show viacheslavkarta1:
        xalign 0.65
        yalign 0.2
    show tamarakarta1:
        xalign 0.85
        yalign 0.2
    show gopnikkarta1:
        xalign 0.65
        yalign 0.6
    show starikkarta1:
        xalign 0.85
        yalign 0.6
    $sluchain1 = renpy.random.randint(1,4)
    $sluchain1v2 = renpy.random.randint(1,4)
####Разворот первых двух карт
    pause 2
    if sluchain1 == 1:#Первая синяя карта
        hide kristinakarta1
        show kristinakarta2:
            xalign 0.1
            yalign 0.2
    if sluchain1v2 == 1:#Первая красная карта
        hide viacheslavkarta1
        show viacheslavkarta2:
            xalign 0.65
            yalign 0.2
    if sluchain1 == 2:
        hide fionakarta1
        show fionakarta2:
            xalign 0.3
            yalign 0.2
    if sluchain1v2 == 2:
        hide tamarakarta1
        show tamarakarta2:
            xalign 0.85
            yalign 0.2
    if sluchain1 == 3:
        hide alenakarta1
        show alenakarta2:
            xalign 0.1
            yalign 0.6
    if sluchain1v2 == 3:
        hide gopnikkarta1
        show gopnikkarta2:
            xalign 0.65
            yalign 0.6
    if sluchain1 == 4:
        hide ggkarta1
        show ggkarta2:
            xalign 0.3
            yalign 0.6
    if sluchain1v2 == 4:
        hide starikkarta1
        show starikkarta2:
            xalign 0.85
            yalign 0.6
#####Разворот обратно этих же карт
    pause 2
    if sluchain1 == 1:
        hide kristinakarta2
        show kristinakarta1:
            xalign 0.1
            yalign 0.2
    if sluchain1v2 == 1:
        hide viacheslavkarta2
        show viacheslavkarta1:
            xalign 0.65
            yalign 0.2
    if sluchain1 == 2:
        hide fionakarta2
        show fionakarta1:
            xalign 0.3
            yalign 0.2
    if sluchain1v2 == 2:
        hide tamarakarta2
        show tamarakarta1:
            xalign 0.85
            yalign 0.2
    if sluchain1 == 3:
        hide alenakarta2
        show alenakarta1:
            xalign 0.1
            yalign 0.6
    if sluchain1v2 == 3:
        hide gopnikkarta2
        show gopnikkarta1:
            xalign 0.65
            yalign 0.6
    if sluchain1 == 4:
        hide ggkarta2
        show ggkarta1:
            xalign 0.3
            yalign 0.6
    if sluchain1v2 == 4:
        hide starikkarta2
        show starikkarta1:
            xalign 0.85
            yalign 0.6

    pause 2
#######Razvorot sleduyushih dvuh kart

    $sluchain2 = renpy.random.randint(1,4)
    $sluchain2v2 = renpy.random.randint(1,4)
    if sluchain2 == 1:#Первая синяя карта
        hide kristinakarta1
        show kristinakarta2:
            xalign 0.1
            yalign 0.2
    if sluchain2v2 == 1:#Первая красная карта
        hide viacheslavkarta1
        show viacheslavkarta2:
            xalign 0.65
            yalign 0.2
    if sluchain2 == 2:
        hide fionakarta1
        show fionakarta2:
            xalign 0.3
            yalign 0.2
    if sluchain2v2 == 2:
        hide tamarakarta1
        show tamarakarta2:
            xalign 0.85
            yalign 0.2
    if sluchain2 == 3:
        hide alenakarta1
        show alenakarta2:
            xalign 0.1
            yalign 0.6
    if sluchain2v2 == 3:
        hide gopnikkarta1
        show gopnikkarta2:
            xalign 0.65
            yalign 0.6
    if sluchain2 == 4:
        hide ggkarta1
        show ggkarta2:
            xalign 0.3
            yalign 0.6
    if sluchain2v2 == 4:
        hide starikkarta1
        show starikkarta2:
            xalign 0.85
            yalign 0.6
#####Разворот обратно этих же карт
    pause 2
    if sluchain2 == 1:
        hide kristinakarta2
        show kristinakarta1:
            xalign 0.1
            yalign 0.2
    if sluchain2v2 == 1:
        hide viacheslavkarta2
        show viacheslavkarta1:
            xalign 0.65
            yalign 0.2
    if sluchain2 == 2:
        hide fionakarta2
        show fionakarta1:
            xalign 0.3
            yalign 0.2
    if sluchain2v2 == 2:
        hide tamarakarta2
        show tamarakarta1:
            xalign 0.85
            yalign 0.2
    if sluchain2 == 3:
        hide alenakarta2
        show alenakarta1:
            xalign 0.1
            yalign 0.6
    if sluchain2v2 == 3:
        hide gopnikkarta2
        show gopnikkarta1:
            xalign 0.65
            yalign 0.6
    if sluchain2 == 4:
        hide ggkarta2
        show ggkarta1:
            xalign 0.3
            yalign 0.6
    if sluchain2v2 == 4:
        hide starikkarta2
        show starikkarta1:
            xalign 0.85
            yalign 0.6

    pause 2
################################
    $sluchain3 = renpy.random.randint(1,4)
    $sluchain3v2 = renpy.random.randint(1,4)
    if sluchain3 == 1:
        hide kristinakarta1
        show kristinakarta2:
            xalign 0.1
            yalign 0.2
    if sluchain3v2 == 1:
        hide viacheslavkarta1
        show viacheslavkarta2:
            xalign 0.65
            yalign 0.2
    if sluchain3 == 2:
        hide fionakarta1
        show fionakarta2:
            xalign 0.3
            yalign 0.2
    if sluchain3v2 == 2:
        hide tamarakarta1
        show tamarakarta2:
            xalign 0.85
            yalign 0.2
    if sluchain3 == 3:
        hide alenakarta1
        show alenakarta2:
            xalign 0.1
            yalign 0.6
    if sluchain3v2 == 3:
        hide gopnikkarta1
        show gopnikkarta2:
            xalign 0.65
            yalign 0.6
    if sluchain3 == 4:
        hide ggkarta1
        show ggkarta2:
            xalign 0.3
            yalign 0.6
    if sluchain3v2 == 4:
        hide starikkarta1
        show starikkarta2:
            xalign 0.85
            yalign 0.6
    pause 2
########################
    if sluchain3 == 1:
        hide kristinakarta2
        show kristinakarta1:
            xalign 0.1
            yalign 0.2
    if sluchain3v2 == 1:
        hide viacheslavkarta2
        show viacheslavkarta1:
            xalign 0.65
            yalign 0.2
    if sluchain3 == 2:
        hide fionakarta2
        show fionakarta1:
            xalign 0.3
            yalign 0.2
    if sluchain3v2 == 2:
        hide tamarakarta2
        show tamarakarta1:
            xalign 0.85
            yalign 0.2
    if sluchain3 == 3:
        hide alenakarta2
        show alenakarta1:
            xalign 0.1
            yalign 0.6
    if sluchain3v2 == 3:
        hide gopnikkarta2
        show gopnikkarta1:
            xalign 0.65
            yalign 0.6
    if sluchain3 == 4:
        hide ggkarta2
        show ggkarta1:
            xalign 0.3
            yalign 0.6
    if sluchain3v2 == 4:
        hide starikkarta2
        show starikkarta1:
            xalign 0.85
            yalign 0.6
    pause 2
#################
    hide kristinakarta1
    hide fionakarta1
    hide alenakarta1
    hide ggkarta1
    hide viacheslavkarta1
    hide tamarakarta1
    hide gopnikkarta1
    hide starikkarta1


    label choise0n2:
    hide screen kristina_karta1n2
    hide screen fiona_karta1n2
    hide screen alena_karta1n2
    hide screen gg_karta1n2
    if game1vibor==3:
        window show
        "Вы заработали максимальную атаку."
        menu:
            "Перейти к защите":
                jump armor_two
    screen kristina_karta1n2:
        imagebutton xalign 0.1 yalign 0.2:
            idle ("karta2.png")
            hover ("karta3.png")
            action Jump("choise1n2")
    show screen kristina_karta1n2
    screen fiona_karta1n2:
        imagebutton xalign 0.3 yalign 0.2:
            idle ("karta2.png")
            hover ("karta3.png")
            action Jump("choise2n2")
    show screen fiona_karta1n2
    screen alena_karta1n2:
        imagebutton xalign 0.1 yalign 0.6:
            idle ("karta2.png")
            hover ("karta3.png")
            action Jump("choise3n2")
    show screen alena_karta1n2
    screen gg_karta1n2:
        imagebutton xalign 0.3 yalign 0.6:
            idle ("karta2.png")
            hover ("karta3.png")
            action Jump("choise4n2")
    show screen gg_karta1n2
    call screen restartn2

label armor_two:
    hide screen viacheslav_karta1n2
    hide screen tamara_karta1n2
    hide screen gopnik_karta1n2
    hide screen starik_karta1n2
    window hide
    if game1vibor2==3:
        window show
        "Вы заработали максимальную защиту."
        menu:
            "Начать битву":
                jump fight_two
    screen viacheslav_karta1n2:
        imagebutton xalign 0.65 yalign 0.2:
            idle ("karta4.png")
            hover ("karta5.png")
            action Jump("choise5n2")
    show screen viacheslav_karta1n2
    screen tamara_karta1n2:
        imagebutton xalign 0.85 yalign 0.2:
            idle ("karta4.png")
            hover ("karta5.png")
            action Jump("choise6n2")
    show screen tamara_karta1n2
    screen gopnik_karta1n2:
        imagebutton xalign 0.65 yalign 0.6:
            idle ("karta4.png")
            hover ("karta5.png")
            action Jump("choise7n2")
    show screen gopnik_karta1n2
    screen starik_karta1n2:
        imagebutton xalign 0.85 yalign 0.6:
            idle ("karta4.png")
            hover ("karta5.png")
            action Jump("choise8n2")
    show screen starik_karta1n2
    call screen restartn2

label choise5n2:
hide screen restartn2
$game1vibor2+=1
hide screen starik_karta1n2
hide screen gopnik_karta1n2
hide screen tamara_karta1n2
hide screen viacheslav_karta1n2
show starikkarta1:
    xalign 0.85
    yalign 0.2
show gopnikkarta1:
    xalign 0.65
    yalign 0.6
show tamarakarta1:
    xalign 0.85
    yalign 0.6
show viacheslavkarta2:
    xalign 0.65
    yalign 0.2
if game1vibor2==1:
    if sluchain1v2 == 1:
        $armor+=1;
        show shield1:
            xalign 0.6
            yalign 0.04
        pause 2
        hide viacheslavkarta2
        jump armor_two
    else:
        hide starikkarta1
        hide gopnikkarta1
        hide tamarakarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Начать битву":
                jump fight_two
else:
    if game1vibor2==2:
        if sluchain2v2 == 1:
            $armor+=1;
            show shield2:
                xalign 0.65
                yalign 0.04
            pause 2
            hide viacheslavkarta2
            jump armor_two
        else:
            hide starikkarta1
            hide gopnikkarta1
            hide tamarakarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Начать битву":
                    jump fight_two
    else:
        if game1vibor2==3:
            if sluchain3v2 == 1:
                $armor+=1;
                show shield3:
                    xalign 0.7
                    yalign 0.04
                pause 2
                hide viacheslavkarta2
                jump armor_two
            else:
                hide starikkarta1
                hide gopnikkarta1
                hide tamarakarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Начать битву":
                        jump fight_two
label choise6n2:
hide screen restartn2
$game1vibor2+=1
hide screen starik_karta1n2
hide screen gopnik_karta1n2
hide screen tamara_karta1n2
hide screen viacheslav_karta1n2
show starikkarta1:
    xalign 0.85
    yalign 0.2
show gopnikkarta1:
    xalign 0.65
    yalign 0.6
show viacheslavkarta1:
    xalign 0.65
    yalign 0.2
show tamarakarta2:
    xalign 0.85
    yalign 0.2
if game1vibor2==1:
    if sluchain1v2 == 2:
        $armor+=1;
        show shield1:
            xalign 0.6
            yalign 0.04
        pause 2
        hide tamarakarta2
        jump armor_two
    else:
        hide starikkarta1
        hide gopnikkarta1
        hide viacheslavkarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Начать битву":
                jump fight_two
else:
    if game1vibor2==2:
        if sluchain2v2 == 2:
            $armor+=1;
            show shield2:
                xalign 0.65
                yalign 0.04
            pause 2
            hide tamarakarta2
            jump armor_two
        else:
            hide starikkarta1
            hide gopnikkarta1
            hide viacheslavkarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Начать битву":
                    jump fight_two
    else:
        if game1vibor2==3:
            if sluchain3v2 == 2:
                $armor+=1;
                show shield3:
                    xalign 0.7
                    yalign 0.04
                pause 2
                hide tamarakarta2
                jump armor_two
            else:
                hide starikkarta1
                hide gopnikkarta1
                hide viacheslavkarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Начать битву":
                        jump fight_two
label choise7n2:
hide screen restartn2
$game1vibor2+=1
hide screen starik_karta1n2
hide screen gopnik_karta1n2
hide screen tamara_karta1n2
hide screen viacheslav_karta1n2
show starikkarta1:
    xalign 0.85
    yalign 0.2
show viacheslavkarta1:
    xalign 0.65
    yalign 0.2
show tamarakarta1:
    xalign 0.85
    yalign 0.2
show gopnikkarta2:
    xalign 0.65
    yalign 0.6
if game1vibor2==1:
    if sluchain1v2 == 3:
        $armor+=1;
        show shield1:
            xalign 0.6
            yalign 0.04
        pause 2
        hide gopnikkarta2
        jump armor_two
    else:
        hide starikkarta1
        hide tamarakarta1
        hide viacheslavkarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Начать битву":
                jump fight_two
else:
    if game1vibor2==2:
        if sluchain2v2 == 3:
            $armor+=1;
            show shield2:
                xalign 0.65
                yalign 0.04
            pause 2
            hide gopnikkarta2
            jump armor_two
        else:
            hide starikkarta1
            hide tamarakarta1
            hide viacheslavkarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Начать битву":
                    jump fight_two
    else:
        if game1vibor2==3:
            if sluchain3v2 == 3:
                $armor+=1;
                show shield3:
                    xalign 0.7
                    yalign 0.04
                pause 2
                hide gopnikkarta2
                jump armor_two
            else:
                hide starikkarta1
                hide tamarakarta1
                hide viacheslavkarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Начать битву":
                        jump fight_two
label choise8n2:
hide screen restartn2
$game1vibor2+=1
hide screen starik_karta1n2
hide screen gopnik_karta1n2
hide screen tamara_karta1n2
hide screen viacheslav_karta1n2
show starikkarta2:
    xalign 0.85
    yalign 0.2
show viacheslavkarta1:
    xalign 0.65
    yalign 0.2
show tamarakarta1:
    xalign 0.85
    yalign 0.2
show gopnikkarta1:
    xalign 0.65
    yalign 0.6
if game1vibor2==1:
    if sluchain1v2 == 4:
        $armor+=1;
        show shield1:
            xalign 0.6
            yalign 0.04
        pause 2
        hide starikkarta2
        jump armor_two
    else:
        hide gopnikkarta1
        hide tamarakarta1
        hide viacheslavkarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Начать битву":
                jump fight_two
else:
    if game1vibor2==2:
        if sluchain2v2 == 4:
            $armor+=1;
            show shield2:
                xalign 0.65
                yalign 0.04
            pause 2
            hide starikkarta2
            jump armor_two
        else:
            hide gopnikkarta1
            hide tamarakarta1
            hide viacheslavkarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Начать битву":
                    jump fight_two
    else:
        if game1vibor2==3:
            if sluchain3v2 == 4:
                $armor+=1;
                show shield3:
                    xalign 0.7
                    yalign 0.04
                pause 2
                hide starikkarta2
                jump armor_two
            else:
                hide gopnikkarta1
                hide tamarakarta1
                hide viacheslavkarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Начать битву":
                        jump fight_two
label fight_two:
    hide screen viacheslav_karta1n2
    hide screen tamara_karta1n2
    hide screen gopnik_karta1n2
    hide screen starik_karta1n2
    if attack>0 and armor>2:
        scene win
        "Атаки и защиты хватило чтобы победить!"
    else:
        scene lose
        if attack<1 and armor<3:
            "Наша защита была разгромлена, наши атаки не достигли противника."
        else:
            if attack<1:
                "Наши атаки не достигли противника."
            if armor<3:
                "Наша защита была разгромлена."
        menu:
            "Начать заново":
                jump previugame2
label label_four:
play music "Computer.mp3"
scene laptop1
with Fade(2.0, 0.0, 0.8, color= '#000000')
pause
"{alpha=.5}{cps=25}Это оказалось проще,чем я ожидал."
"{alpha=.5}{cps=25}У нас было намного меньше ошибок, чем пару дней назад."
a"{cps=25}Победа!"
licon"{cps=25}Не удивительно."
ficon"{cps=25}Мы зажарили их, как шашлычок."
kicon"{cps=25}Всё благодаря нашему капитану."
licon"{cps=25}Да, ты молодец."
ficon"{cps=25}Угу."
a"{cps=25}Мы все постарались."
kicon"{cps=25}Предлагаю это отпраздновать."
a"{cps=25}Каким образом?"
ficon"{cps=25}У нас дискотека в эту субботу."
ficon"{cps=25}Приглашаю всех."
"{alpha=.5}{cps=25}Конечно, я не умел танцевать, но отказывать не хотелось."
a"{cps=25}Я согласен."
licon"{cps=25}Наверное, я тоже."
kicon"{cps=25}Тогда я принесу тортик."
stop music fadeout 1
scene black
"{alpha=.5}{cps=25}До начала турнира оставалось три дня."
scene disco
with fade
"{alpha=.5}{cps=25}А я веселился на дискотеке."
play music "Disco.mp3"
"{alpha=.5}{cps=25}Мы стояли в кругу и исполняли непонятные движения."
"{alpha=.5}{cps=25}Похоже, не один я плохо танцевал."
show fiona9
f"{cps=25}Да тут никто не шарит."
a"{cps=25}?"
hide fiona9
"{alpha=.5}{cps=25}Фиона вышла в центр и начала танцевать нижний брейк."
"{alpha=.5}{cps=25}Я тоже вошёл в кураж и колбасился под каждый трек."
scene black
with fade
scene disco
with fade
"{cps=25}Да. Давно я так не веселился."
a"{cps=25}Какой там следующий трек?"
stop music fadeout 1
define di = Character('Диджей', color="#c8ffc8")
di"{cps=25}А теперь немного расслабимся в медленном танце, парни приглашают девчонок."
a"{cps=25}Ну вот."
"{alpha=.5}{cps=25}Я прошёл в дальний угол и начал наблюдать за происходящим."
"{alpha=.5}{cps=25}На удивление ни Фиону, ни Кристину, ни Алёну не пригласили."
"{alpha=.5}{cps=25}Хотя бы я должен это сделать."
menu:
    "Пригласить Фиону":
        $score1 += 2
        jump Fiona2
    "Пригласить Кристину":
        $score2 += 2
        jump Kristina2
    "Пригласить Алёну":
        $score3 += 2
        jump Alyona2
label Fiona2:
show fiona9
a"{cps=25}Не хочешь потанцевать?"
f"{cps=25}Ладненько."
hide fiona9
play music "Relax.mp3"
scene fionadance
"{alpha=.5}{cps=25}Я положил руки к ней на талию."
"{alpha=.5}{cps=25}Мы медленно начали кружится."
f"{cps=25}Классно же, что мы прошли отборочные."
f"{cps=25}Кстати... А на что ты собираешься потратить приз?"
a"{cps=25}Я находился в безвыходной ситуации, не попади я в неё команда не была бы создана."
a"{cps=25}Моя мать сильно больна, если я не соберу деньги на её операцию, то она не сможет ходить."
f"{cps=25}Это..грустно.."
"{alpha=.5}{cps=25}Глаза Фионы были наполнены жалостью."
a"{cps=25}Но не волнуйся. Когда мы победим в турнире, всё станет намного лучше."
f"{cps=25}Я постараюсь ради тебя и твоей мамы."
"{alpha=.5}{cps=25}Внезапно во мне появилось желание прижать её к себе."
"{alpha=.5}{cps=25}Я помотрел ей в лицо, там светилась привычная детская улыбка с долей смущения."
"{alpha=.5}{cps=25}Мы могли бы и дальше так танцевать, как вдруг какой-то незнакомец прервал наш танец."
stop music fadeout 1
scene disco
with circleirisin
show gopnik1
define gop = Character('Незнакомец', color="#c8ffc8")
gop"{cps=25}Эй, парнишка, иди потанцуй в другом месте."
hide gopnik1
"{alpha=.5}{cps=25}Он встал между мной и Фионой, резко притянув её к себе."
a"{cps=25}А у девушки поинтересоваться не хочешь?"
gop"{cps=25}Чё ты там ляпнул?!Я же сказал тебе иди гуляй."
show gopnik1
"{alpha=.5}{cps=25}Он повернулся в мою сторону."
"{alpha=.5}{cps=25}Глядя на растерянный вид Фионы, я понял, что нужно действовать."
play music "trevoga.mp3"
menu:
    "Ударить":
        jump Fiona2_1
    "Уйти с дискотеки вместе с Фионой.":
        jump Fiona2_2
label Fiona2_1:
"{alpha=.5}{cps=25}Он был где-то в полтора раза выше меня и скорее всего имел опыт в драках."
scene black
hide gopnik1
play sound "vzmah.mp3"
"{alpha=.5}{cps=25}Я попытался ударить его в лицо, но промахнулся и попал в плечо."
scene disco
with fade
show gopnik1
"{alpha=.5}{cps=25}Незнакомец немного пошатнулся, но быстро встал в равновесие."
"{alpha=.5}{cps=25}Его взгляд сфокусировался на мне."
"{alpha=.5}{cps=25}Я встал в боевую стойку."
gop"{cps=25}Ну давай!"
hide gopnik1
"{alpha=.5}{cps=25}Мы бросились навстречу друг к другу."
scene black
with fade
play sound "Punch.mp3"
scene white
with fade
scene disco
with fade
"{alpha=.5}{cps=25}Я оклимался.{w=.5} Похоже удар, прилетевший в щёку, заставил меня свалиться на пол."
"{alpha=.5}{cps=25}Однако мой кулак тоже попал в цель."
"{alpha=.5}{cps=25}Бунтарь прижимал свой нос от боли."
scene white
with fade
play music "Relax.mp3"
"{alpha=.5}{cps=25}И тут меня осенило."
"{alpha=.5}{cps=25}Жизнь готовила меня к этому дню."
"{alpha=.5}{cps=25}Файтинги.{w=.5} Я прошел множество игр в данном жанре, так что опыт драк у меня уже был."
"{alpha=.5}{cps=25}Разница в нашем росте не играла никакого значения.{w=.5} Нужно было лишь умело уворачиваться и находить момент для атаки."
scene disco
with fade
"{alpha=.5}{cps=25}Я встал на ноги и побежал в его сторону."
label Fiona2_1_1:
"{cps=25}Пару таких ударов мне не выдержать."
"{alpha=.5}{cps=25}Он согнул правую руку и готовился атаковать. Мне необходимо увернуться."
"{alpha=.5}{cps=25}Я..."
menu:
    "Резко остановлюсь.":
        jump Fiona2_1_2_1
    "Попытаюсь увернуться влево.":
        jump Fiona2_1_2_2
    "Попытаюсь увернуться вправо.":
        jump Fiona2_1_2_3
label Fiona2_1_2_1:
"{alpha=.5}{cps=25}Я резко остановился и надеялся, что он меня не достанет."
scene black
with fade
play sound "Punch.mp3"
scene white
with fade
scene disco
with fade
"{alpha=.5}{cps=25}Но я ошибся. Его руки были длиннее, чем я ожидал."
"{alpha=.5}{cps=25}От удара я снова упал."
jump Fiona2_1_1
label Fiona2_1_2_3:
"{alpha=.5}{cps=25}Я вытянулся вправо."
scene black
with fade
play sound "Punch.mp3"
scene white
with fade
scene disco
with fade
"{alpha=.5}{cps=25}Но я ошибся. Его руки были длиннее, чем я ожидал."
"{alpha=.5}{cps=25}От удара я снова упал."
jump Fiona2_1_1
label Fiona2_1_2_2:
"{alpha=.5}{cps=25}Я вытянулся влево."
scene black
with fade
play sound "vzmah.mp3"
scene white
with fade
scene disco
with fade
"{alpha=.5}{cps=25}Похоже мне удалось увернуться. Теперь прекрасный момент для контратаки."
play sound "Punch.mp3"
"{alpha=.5}{cps=25}Я целился своим коленом ему в живот, но попал чуть ниже.."
"{alpha=.5}{cps=25}Он упал и застонал от боли."
play sound "gong.mp3"
scene ko
"{alpha=.5}{cps=25}Похоже мне удалось сделать критический удар."
"{cps=25}Самое время сматываться."
"{alpha=.5}{cps=25}Я схватил Фиону за руку и выбежал из помещения."
scene black
stop music fadeout 1
scene street4
with fade
play music "Relax.mp3"
show fiona10
f"{cps=25}"
f"{cps=25}Зачем ты это сделал?"
a"{cps=25}Он сам напросился."
f"{cps=25}Нужно было просто свалить, и тогда не было бы проблем."
a"{cps=25}Не знаю. Я просто не выдержал."
"{alpha=.5}{cps=25}Фиона скрючила злостную гримасу и... обняла меня."
hide fiona10
f"{cps=25}Но всё-таки.. спасибо, что за меня заступился."
f"{cps=25}Я сильно испугалась этого парня."
"{alpha=.5}{cps=25}Мы простояли так несколько секунд."
"{alpha=.5}{cps=25}..."
show fiona10
f"{cps=25}Сергей.."
a"{cps=25}Да?"
f"{cps=25}Тебе нравятся.. "
f"{cps=25}..парни?"
a"{cps=25}Эм, нет."
show fiona9
"{alpha=.5}{cps=25}Фиона улыбнулась."
show fionashuy
f"{cps=25}А мне вот нравится один..."
"{alpha=.5}{cps=25}Я хотел было ответить, как..."
show alyona2 at right
show kristina6 at left
l"{cps=25}Вот вы где!"
k"{cps=25}Мы вас обыскались."
l"{cps=25}Что ты там устроил?"
a"{cps=25}Я просто защищался."
l"{cps=25}Идиот, просто не надо было лезть."
k"{cps=25}Ты не поранился?"
a"{cps=25}Всё хорошо, завтра пройдёт."
k"{cps=25}Я надеюсь."
"{alpha=.5}{cps=25}Я совсем забыл про Кристину и Алёну, а они очень волновались за меня."
show fiona9
f"{cps=25}Похоже того парня выгнали."
a"{cps=25}Пора возвращатся."
hide kristina6
hide fiona10
hide alyona2
scene black
with fade
scene disco
with fade
stop music fadeout 1
"{cps=25}Я слишком устал танцевать."
a"{cps=25}Я пошёл домой."
show kristina6 at right
k"{cps=25}До встречи."
show fiona9
f"{cps=25}Досвидули."
show alyona2 at left
l"{cps=25}Пока."
jump All_done2
label Fiona2_2:
"{alpha=.5}{cps=25}Я взял Фиону за руку."
a"{cps=25}Бежим!"
"{alpha=.5}{cps=25}Мы попытались скрыться в толпе, в тот же момент незнакомец схватил её за блузку, но его рука ускользнула, и нам удалось добраться до выхода."
scene black
with fade
scene street4
with fade
play music "Relax.mp3"
show fiona11
"{alpha=.5}{cps=25}Я осмотрелся."
a"{cps=25}Похоже, мы оторвались."
f"{cps=25}Я сильно испугалась этого парня."
a"{cps=25}Я тоже.."
"{alpha=.5}{cps=25}Пока стояло неловкое молчание, я заметил, что её блузка порвана."
f"{cps=25}Эм, можешь отпустить мою руку."
"{cps=25}Точно,  я всё это время не отпускал её руку."
a"{cps=25}Конечно, прости."
a"{cps=25}У тебя порвалась блузка, держи мою куртку."
hide fiona11
show fiona12
f"{cps=25}Фиона - Благодарю."
a"{cps=25}Может прогуляемся?"
f"{cps=25}Можно."
hide fiona12
scene street3v2
with fade
"{cps=25}Стояла приятная тишина,яркий луннный свет освещал дорогу."
"{cps=25}Мы гуляли по тихим городским улицам."
"{cps=25}Я повернулся в сторону Фионы. Легкий ветерок ласкал её волосы."
"{cps=25}Фиона выглядела смущенной. Она будто пыталась что-то сказать."
show fiona12
f"{cps=25}Серёжа.."
a"{cps=25}Да?"
f"{cps=25}Тебе нравятся.. "
a"{cps=25}Эм, нет."
show fiona13
"{alpha=.5}{cps=25}Фиона улыбнулась."
f"{cps=25}Это хорошо."
a"{cps=25}Я думаю да."
f"{cps=25}Серёжа, я очень волнуюсь о турнире."
a"{cps=25}Не волнуйся, всё будет хорошо."
f"{cps=25}Я тебе верю."
"{alpha=.5}{cps=25}..."
show alyona2 at right
show kristina6 at left
l"{cps=25}Вот вы где!"
k"{cps=25}Мы вас обыскались."
l"{cps=25}Что ты там устроил?"
a"{cps=25}Я просто защищался."
l"{cps=25}Идиот, просто не надо было лезть."
k"{cps=25}Ты не поранился?"
a"{cps=25}Всё хорошо, завтра пройдёт."
k"{cps=25}Я надеюсь."
"{alpha=.5}{cps=25}Я совсем забыл про Кристину и Алёну, а они очень волновались за меня."
f"{cps=25}Ладно, я наверное пойду домой."
hide fiona13
a"{cps=25}Я тоже очень устал."
k"{cps=25}Обязательно продизенфицируй раны."
hide alyona2
hide kristina6
jump All_done2

label Kristina2:
show kristina6
a"{cps=25}Не хочешь потанцевать?"
k"{cps=25}Оу. Я? Давай!"
hide kristina6
play music "Relax.mp3"
scene kristinadance
with fade
"{alpha=.5}{cps=25}Я положил руки к ней на талию."
"{alpha=.5}{cps=25}Мы медленно начали кружится."
k"{cps=25}Я очень рада, что встретила тебя, Алёну и Фиону."
k"{cps=25}Думаю у вас всё получится."
a"{cps=25}У нас?"
k"{cps=25}Да, я всё хотела тебе сказать."
k"{cps=25}Ну..в общем я ухожу из команды."
stop music fadeout 1
scene disco
"{alpha=.5}{cps=25}Я резко остановился."
a"{cps=25}Что!?"
k"{cps=25}Прости."
"{alpha=.5}{cps=25}Кристина отпустила меня и начала убегать."
a"{cps=25}Стой!"
"{alpha=.5}{cps=25}Я погнался за ней."
scene street3v2
with fade
a"{cps=25}Стой!"
scene black
with fade
"{alpha=.5}{cps=25}Я гнался за ней около минуты, но моя дыхалка была намного хуже, и она оторвалась."
a"{cps=25}Чёрт!"
"{cps=25}Почему так произошло?"
"{alpha=.5}{cps=25}Я вернулся на дискотеку."
scene disco
show alyona4:
    xalign 0.3
    yalign 1.0
show fiona10:
    xalign 0.7
    yalign 1.0
f"{cps=25}Что? Она просто ушла?"
a"{cps=25}Да."
l"{cps=25}.."
"{alpha=.5}{cps=25}Алёна выглядела очень подавленной. Похоже ей трудно что-то сказать."
f"{cps=25}И что ты собираешься делать?"
"{cps=25}А что я могу."
a"{cps=25}Я.."
menu:
    "Пойду к ней домой":
        jump Krisina2_1
    "Свяжусь с ней в игре":
        jump Krisina2_2
label Krisina2_1:
a"{cps=25}Я пойду к ней домой."
f"{cps=25}Отличная идея. Чтоб завтра всё нам рассказал."
a"{cps=25}А почему я иду один?"
f"{cps=25}Ты капитан команды."
a"{cps=25}Но.."
a"{cps=25}Ай ладно."
"{alpha=.5}{cps=25}Я вышел на улицу и направился в сторону дома Кристины."
scene street3v2
with fade
scene kristinahome1
with fade
"{cps=25}Хм, всё-таки время позднее. Не разбужу ли я здешних жителей?"
"{alpha=.5}{cps=25}Я постучал как можно тише."
play sound "udar.mp3"
"{cps=25}Да, глупая идея, но у меня есть идея ещё глупее."
"{cps=25}Так как Кристина только пришла, она не спит, а значит я могу проникнуть в её комнату."
"{alpha=.5}{cps=25}Окно на втором этаже было открыто."
a"{cps=25}Приступаем к операции 'Проникновение'."
"{alpha=.5}{cps=25}В голове появились воспоминания из стэлс игр."
"{cps=25}Идти нужно в полуприсяде."
"{alpha=.5}{cps=25}Я пробрался к дереву, стоявшему рядом с окном."
scene window1
"{alpha=.5}{cps=25}Взобрался на него."
"{cps=25}Проблема. Между веткой и окном несколько метров."
"{cps=25}Придётся прыгать."
"{alpha=.5}{cps=25}Я собрался с духом."
"{cps=25}Прыжок!"
scene window2
play sound"vzmah.mp3"
with fade
"{alpha=.5}{cps=25}Ощущения полёта незабываемы."
"{alpha=.5}{cps=25}С трудом разглядев подоконник, я схватился за него рукой."
"{cps=25}Было опасно, но у меня получилось."
"{alpha=.5}{cps=25}Я подтянулся и залез в комнату."
scene black
with fade
"{alpha=.5}{cps=25}Было темно."
a"{cps=25}Есть здесь кто?"
"{alpha=.5}{cps=25}."
"{alpha=.5}{cps=25}.."
"{alpha=.5}{cps=25}..."
play sound "choir.mp3"
scene kristinahome3
"{alpha=.5}{cps=25}В комнате зажегся яркий свет."
show kristina8
k"{cps=25}ААААА!"
a"{cps=25}ААаа!"
"{alpha=.5}{cps=25}Кристина взяла табуретку и кинула её в меня."
scene kristinahome4
play sound"vzmah.mp3"
"{alpha=.5}{cps=25}Табурет очень опасное оружие в руках профессионала, но к счастью Кристина не была таковым, и табурет улетел в окно."
scene kristinahome3
show kristina8
a"{cps=25}Успокойся! Это я Серега."
k"{cps=25}Ты? Ты. Ты очень меня испугал."
a"{cps=25}Я стучал в дверь, но мне так никто и не открыл, так что пришлось лезть в окно."
"{alpha=.5}{cps=25}Похоже она очень злилась, но её лицо скоро смягчилось."
hide kristina8
show kristina7
k"{cps=25}Больше так никогда не делай."
play music "Relax.mp3"
"{alpha=.5}{cps=25}Кристина была завернута в какое-то сине-зеленое одеяло. Похоже она почти легла спать."
a"{cps=25}Вообщем-то по поводу моего прихода."
a"{cps=25}Что произошло на дискотеке?"
"{cps=25}Похоже ей трудно говорить, но я должен узнать причину."
k"{cps=25}Прости меня."
k"{cps=25}Пару дней назад ко мне подошёл тренер и предложил присоединится к олимпийской сборной."
k"{cps=25}Только для этого надо уехать в другой город."
k"{cps=25}Понимаешь, такой шанс выпадает раз в жизни."
a"{cps=25}Но как же мы без тебя?"
if (score2 == 7):
    jump Kristina_good
else:
    jump Kristina_bad
label Kristina_good:
k"{cps=25}Я понимаю, что ты делаешь это ради своей матери."
k"{cps=25}Мне как члену олимпийской сбороной дадут хороший аванс, которого хватит на то чтобы помочь тебе."
a"{cps=25}И ты что, отдашь мне эти деньги просто так?"
k"{cps=25}Да, ведь из-за меня вы не сможете участвовать в турнире."
"{cps=25}Конечно предложение было очень хорошее, но и нашу команду я не хотел терять."
k"{cps=25}Тебе наверное сейчас тяжело думать об этом.{w=1} Давай встретимся завтра в обед."
"{cps=25}Неплохая идея.{w=1} Возможно за ночь мне что-нибудь удастся придумать. Тем более нужно учитывать, что я вломился в чужой дом посреди ночи."
a"{cps=25}Хорошо."
"{alpha=.5}{cps=25}Я направился домой."
scene street3v2
with fade
scene laptop1
with Fade(2.0, 0.0, 0.8, color= '#000000')
pause
a"{cps=25}Тяжелый день. Нужно лечь спать."
jump Kristina_good2
label Kristina_bad:
k"{cps=25}Прости я не могу больше. Ты должен уйти."
"{cps=25}Похоже мне её не убедить."
a"{cps=25}Тогда прощай."
k"{cps=25}Прощай."
"{alpha=.5}{cps=25}Я вышел из её дома и понял, что это конец."
scene black
"{alpha=.5}{cps=25}Прошло 2 недели."
"{alpha=.5}{cps=25}Денис всё таки решился мне помочь и мы поехали на соревнования в Рио-де-жанейро"
"{alpha=.5}{cps=25}Он сказал, что приведёт с собой нового профессионального игрока."
jump Tamara
label Kristina_good2:
"{cps=25}Итак, передо мной встал выбор."
"{cps=25}Либо я гарантированно получаю деньги, либо я рискую и пытаюсь остановить Кристину, но сохраняю нашу команду."
"{alpha=.5}{cps=25}С такими мыслями я заснул."
scene laptop2
with Fade(0.2, 0.0, 0.8, color= '#fff')
play music "Utro.mp3"
"{alpha=.5}{cps=25}Я встал очень рано. Солнце только вышло из-за горизонта."
a"{cps=25}Пойду встречу Кристину у её дома."
scene kristinahome2
"{alpha=.5}{cps=25}Стучаться в дом так рано не хотелось, так что оставалось только ждать."
"{alpha=.5}{cps=25}И я ждал."
scene black
scene kristinahome2
"{alpha=.5}{cps=25}Ждал."
scene black
scene kristinahome2
"{alpha=.5}{cps=25}И ждал."
"{cps=25}Хм.."
"{alpha=.5}{cps=25}Пока я летал в облаках, кто-то подошел ко мне почти вплотную."
show tamara
t"{cps=25}Подглядываешь!"
a"{cps=25}Нет!"
t"{cps=25}Что ты здесь забыл?"
"{alpha=.5}{cps=25}А с чего это мне рассказывать ей?"
t"{cps=25}Я знаю, ты живешь в другой стороне."
"{alpha=.5}{cps=25}Откуда? А впрочем не важно."
a"{cps=25}Я жду Кристину."
t"{cps=25}Кристину значит, но она скорее всего уже уехала."
play music "trevoga.mp3"
a"{cps=25}Уехала?"
t"{cps=25}Когда она вчера забирала у меня свою медицинскую карточку, я поинтересовалась о времени её отъезда."
t"{cps=25}И она сказала, что уезжает рано утром на следующий день."
t"{cps=25}То есть уже сегодняшний."
"{cps=25}Выходит, Кристина сказала встретиться позже, чтобы незаметно уехать."
a"{cps=25}Что же мне делать?"
t"{cps=25}Она наверное уже в аэропорту. Тебе надо поспешить."
"{cps=25}А Тамара иногда умеет разговаривать нормально."
a"{cps=25}Да, спасибо."
t"{cps=25}Действуй как мужчина, и ты поднимешься в моих глазах."
scene black
"{alpha=.5}{cps=25}Я отдал честь и побежал искать маршрутку до аэропорта."
"{alpha=.5}{cps=25}Мне повезло, и я доехал быстро."
stop music fadeout 1
scene aero
"{alpha=.5}{cps=25}Но на пути встала преграда в виде пропускного пункта."
"{cps=25}Если я попытаюсь резко вбежать, то могут подумать, что я террорист."
"{alpha=.5}{cps=25}Нужно придумать способ похитрее."
menu:
    "Сказать что потерял какого-то родственника":
        jump Krisina3_1
    "Притвориться больным":
        jump Krisina3_2
    "Найти чёрный вход":
        jump Krisina3_3
label Krisina3_1:
"{alpha=.5}{cps=25}Я сделал растерянный вид и подошёл к охраннику."
a"{cps=25}Ребёнок, моя сестра, она пропала, потерялась где-то здесь."
ohr"{cps=25}Что? Срочно объявим в мегафон. Стойте здесь."
"{alpha=.5}{cps=25}Охранник отошел на десять метров, чтобы позвать другого охранника."
"{cps=25}Мой шанс."
"{alpha=.5}{cps=25}Я отбежал и скрылся за угол."
"{cps=25}Отлично! Теперь нужно найти самолёт."
"{alpha=.5}{cps=25}Я отшёл на безопасное расстояние и взглянул в окно."
jump Krisina3_done
label Krisina3_2:
a"{cps=25}(Кашляя) Извините можно доктора, похоже меня сейчас вырвет."
ohr"{cps=25}Конечно, молодой человек, подождите немного."
"{alpha=.5}{cps=25}Охранник отошел на десять метров, чтобы позвать другого охранника."
"{cps=25}Мой шанс."
"{alpha=.5}{cps=25}Я отбежал и скрылся за угол."
"{cps=25}Отлично! Теперь нужно найти самолёт."
"{alpha=.5}{cps=25}Я отшёл на безопасное расстояние и взглянул в окно."
jump Krisina3_done
label Krisina3_3:
"{alpha=.5}{cps=25}Я обошёл помещение и нашёл проход для персонала."
"{cps=25}Но как же туда пройти?"
"{alpha=.5}{cps=25}В спешке я посмотрел в толпу прохожих."
"{alpha=.5}{cps=25}И заметил.."
"{cps=25}Не может быть."
show viaches2
v"{cps=25}Привет, братан!"
a"{cps=25}Привет, ты не говорил, что работаешь пилотом."
v"{cps=25}Да вот недавно устроился. На самом деле, в армии я служил в авиации, поэтому у меня есть опыт. Кстати, а ты тут зачем?"
a"{cps=25}Я тут..{w=0.5} из-за одной девушки."
v"{cps=25}Ого.. девушки.{w=0.5} Сколько ей?{w=0.5} Она красивая?{w=0.5} Дай её телефончик?"
a"{cps=25}На это нет времени.Ты должен провести меня к самолёту."
v"{cps=25}Без проблем!"
jump Krisina3_done
label Krisina3_done:
scene black
"{cps=25}Кристина!{w=0.5} Она почти зашла."
"{alpha=.5}{cps=25}Расталкивая людей я пробрался на площадку."
a"{cps=25}Нет, стой!"
scene kristinafly
"{alpha=.5}{cps=25}Я увидел, что она повернулась."
"{alpha=.5}{cps=25}Кристина стояла на верху лестницы в самолёт, сильный ветер раздувал её волосы."
"{alpha=.5}{cps=25}Наши взгляды встретились."
"{alpha=.5}{cps=25}Я не знал, как выразить свои мысли."
a"{cps=25}Пожалуйста, не уходи!"
k"{cps=25}Но как же твоя мама?"
a"{cps=25}Да, она член моей семьи и я хочу ей помочь, но наша команда."
a"{cps=25}Вы все мне тоже как семья."
a"{cps=25}Поэтому я не хочу тебя терять."
scene black
"{alpha=.5}{cps=25}Кристина закрыла глаза и сказала."
k"{cps=25}Я тоже, я тоже не хочу."
a"{cps=25}Тогда уходим от сюда."
scene aero
k"{cps=25}Угу."
"{alpha=.5}{cps=25}Отлично!"
play sound "Punch.mp3"
ohr"{cps=25}Попался, бегун."
"{alpha=.5}{cps=25}От удара по макушке я прилег поспать."
scene black
"{alpha=.5}{cps=25}После того как я искренне раскаялся в произошедшем, охранники меня отпустили."
"{alpha=.5}{cps=25}В итоге мне всё таки удалось сохранить Кристину в команде."
"{alpha=.5}{cps=25}Остальное время нужно потратить на тренировки."
jump All_done2
label Krisina2_2:
play music "Computer.mp3"
show laptop1
with Dissolve(2.5)
pause
"{alpha=.5}{cps=25}Я пришёл домой и сразу же написал ей."
"{alpha=.5}{cps=25}{w=4}Ответа нет."
"{alpha=.5}{cps=25}Ожидаемо."
"{cps=25}Неужели всё так и закончиться?{w=2} Похоже, что да."
scene black
stop music fadeout 1
"{alpha=.5}{cps=25}Прошло 2 недели."
"{alpha=.5}{cps=25}Денис всё таки решился мне помочь и мы поехали на соревнования в Рио-де-жанейро"
"{alpha=.5}{cps=25}Он сказал, что приведёт с собой нового профессионального игрока."
jump Tamara

label Alyona2:
a"{cps=25}Не хочешь потанцевать?"
show alyona2
l"{cps=25}С тобой не хотелось бы, но похоже других кандидатов нет."
a"{cps=25}Не бойся, после меня руки помоешь."
"{alpha=.5}{cps=25}Алёна фыркнула."
play music "Relax.mp3"
scene alenadance
"{alpha=.5}{cps=25}Я положил руки к ней на талию."
"{cps=25}Мы медленно начали кружится."
l"{cps=25}Эй, ты то хоть рад, что мы прошли отборочные."
a"{cps=25}Конечно!"
l"{cps=25}Если выиграем на что потратишь деньги?"
a"{cps=25}Это личное."
l"{cps=25}Небось на какую-нибудь ерунду."
a"{cps=25}Нет."
l"{cps=25}Ну а тогда на что?"
"{cps=25}Она слишком настырная. Придётся рассказать."
a"{cps=25}Моя мать сильно больна, и я собираю деньги на её операцию."
l"{cps=25}Сочувствую.."
a"{cps=25}Поэтому нужно победить в турнире."
l"{cps=25}Я постораюсь ради тебя и твоей мамы."
"{alpha=.5}{cps=25}Песня закончилась, и я уже начал отходить как Алёна меня остановила."
l"{cps=25}У меня к тебе есть одна просьба."
a"{cps=25}И какая же?"
l"{cps=25}Завтра расскажу."
"{cps=25}Да она издевается."
l"{cps=25}Приходи в южный парк."
a"{cps=25}Ну ладно."
scene disco
"{alpha=.5}{cps=25}Она ушла в другую часть помещения."
a"{cps=25}Наверное, пора идти домой."
"{alpha=.5}{cps=25}Я со всеми попрощался и направился домой."
stop music fadeout 1
scene street4
with fade
scene laptop1
with fade
a"{cps=25}Как же хочется спать."
scene black
scene laptop2
with fade
play music "Utro.mp3"
"{alpha=.5}{cps=25}Я проснулся в хорошем настроении.{/alpha}"
"{cps=25}Южный парк. Давно я там не был."
"{alpha=.5}{cps=25}Я оделся и вышел на улицу.{/alpha}"
scene schooltrip
with fade
scene street3
with fade
show alyona1
l"{cps=25}Привет."
a"{cps=25}Привет."
l"{cps=25}Идём за мной!"
"{cps=25}?"
a"{cps=25}Хорошо."
scene black
"{alpha=.5}{cps=25}Алёна развернулась на 180 градусов и зашагала вперёд.{/alpha}"
"{alpha=.5}{cps=25}Я постарался от неё не отставать.{/alpha}"
"{alpha=.5}{cps=25}Мы шли вдоль дороги очень далеко, встречая на своём пути разные магазины и киоски.{/alpha}"
a"{cps=25}Долго ещё?"
l"{cps=25}Терпи!"
"{alpha=.5}{cps=25}Скоро мы свернули с дороги на лесную тропинку.{/alpha}"
"{alpha=.5}{cps=25}Тропинка привела нас к лесной чаще, естественно тут мы не остановились.{/alpha}"
a"{cps=25}Да куда ты нас вообще ведёшь?"
l"{cps=25}Почти пришли."
"{alpha=.5}{cps=25}Через 10 минут мы всё таки добрались до места назначения.{/alpha}"
scene palatka
with fade
a"{cps=25}Наконец-то!"
a"{cps=25}Где мы чёрт возьми!"
show alyona1
l"{cps=25}Мы у меня дома."
a"{cps=25}У тебя дома?"
hide alyona1
"{alpha=.5}{cps=25}Я осмотрелся. Напротив меня стояла палатка, рядом с ней что-то напоминавшее табурет.{/alpha}"
"{alpha=.5}{cps=25}Так же у дерева лежал котелок. Еда в нём очень сильно воняла.{/alpha}"
show alyona1
l"{cps=25}Да. Я тут живу последние пару дней."
a"{cps=25}Почему?"
hide alyona1
if (score3 == 5):
    show alyona2
    l"{cps=25}Потому что я снова сбежала из дома."
else:
    show alyona2
    l"{cps=25}Потому что я сбежала из дома."
"{cps=25}Я не удивлён."
a"{cps=25}Ну что сказать. Неплохо. Зачем же ты привела меня сюда?"
l"{cps=25}Просто, просто у меня нет еды, интернета, и я скоро сойду с ума здесь."
l"{cps=25}Помоги!"
"{cps=25}Хм.."
a"{cps=25}А что же я могу сделать?"
hide alyona2
show alyona1
l"{cps=25}Придумай что нибудь!"
"{cps=25}Легко сказать."
a"{cps=25}Хорошо. Первым делом еда."
a"{cps=25}Завтра я приду и принесу еду."
l"{cps=25}Нет."
l"{cps=25}Ты должен сделать это сегодня."
a"{cps=25}А если у меня сегодня есть ещё дела."
l"{cps=25}Значит сделаешь их завтра."
l"{cps=25}Прекрасная девушка нуждается в твоей помощи,а ты собираешься сбежать."
"{cps=25}Чёрт."
a"{cps=25}Нет."
l"{cps=25}Тогда добудь еды, охотник."
"{alpha=.5}{cps=25}Я развернулся и пошёл.{/alpha}"
scene black
"{alpha=.5}{cps=25}Недалеко от леса я увидел придорожный магазин.{/alpha}"
"{alpha=.5}{cps=25}Я купил сосиски, булочки и колу, после чего направился назад.{/alpha}"
scene palatka2
with fade
show alyona2
l"{cps=25}Ты очень долго."
a"{cps=25}25 минут прошло."
l"{cps=25}Ладно, давай готовить."
a"{cps=25}Если честно, я тоже сильно проголодался."
"{cps=25}Ещё бы. Целый день ходьбы по лесам выведет любого."
"{alpha=.5}{cps=25}Мы развели костёр.{/alpha}"
scene black
#добавить звук костра
play music "fire.mp3"
l"{cps=25}А что дальше?"
a"{cps=25}Есть что-нибудь напоминающее шампур?"
show sworda:
    xalign 0.5
    yalign 0.5
l"{cps=25}Есть меч."
a"{cps=25}Меч? Зачем тебе меч?!"
l"{cps=25}Мало ли кого можно встретить в лесу."
a"{cps=25}Ладно. Меч тоже подойдёт."
"{alpha=.5}{cps=25}Я воткнул сосиски в меч и поставил его над огнём.{/alpha}"
a"{cps=25}Теперь ждём."
"{cps=25}Земля потянула меня к себе."
hide sworda
"{cps=25}И всё-таки жизнь в лесу имеет свои плюсы."
"{cps=25}Лёгкий ветерок, тепло от костра, звуки кукушки. Всё это особенно успокаивало."
"{cps=25}Я давно так не расслаблялся."
"{cps=25}В условиях тренировок это сделать особенно трудно."
"{cps=25}Надо будет всех сюда пригласить."
"{cps=25}..."
l"{cps=25}Эй, не спать! Еда почти готова."
"{alpha=.5}{cps=25}Алёна прервала поток моих мыслей.{/alpha}"
a"{cps=25}Не сплю я, не сплю."
scene fire
with fade
"{alpha=.5}{cps=25}Действительно. Сосиски были почти готовы.{/alpha}"
"{alpha=.5}{cps=25}Я аккуратно вытащил меч.{/alpha}"
a"{cps=25}Горячо!"
l"{cps=25}Вытаскивай сосиски!"
scene black
with fade
"{alpha=.5}{cps=25}Через накоторое время мы уже уплетали сосиски с колой.{/alpha}"
scene fire2
with fade
l"{cps=25}Оо да! Прекрасное сочетание."
l"{cps=25}Ты просто лучший Серёж. Я хочу, чтобы ты каждый день мне готовил."
a"{cps=25}Ты должна сама научиться готовить."
l"{cps=25}Зануда."
scene black
"{cps=25}Похоже я засыпаю."
"{alpha=.5}{cps=25}Я снова упал на траву, однако теперь не один.{/alpha}"
scene alenaongrass
with fade
"{alpha=.5}{cps=25}Алёна довольно лежала рядом.{/alpha}"
l"{cps=25}Я наелась."
a"{cps=25}Я тоже."
l"{cps=25}Ты посмотри какие звёзды!"
a"{cps=25}Красиво."
if score3 == 5:
    a"{cps=25}Кстати, почему ты снова сбежала из дома. В прошлый раз мы с твоим отцом вроде всё обсудили."
else:
    a"{cps=25}Твои родители тебя наверое ищут."
l"{cps=25}Да они совсем меня не понимают."
if score3 == 5:
    l"{cps=25}Знаешь, что мне сказали на следующий день?"
    a"{cps=25}И что же?"
    l"{cps=25}Когда ты начнёшь встречаться с этим парнем?"
    "{alpha=.5}{cps=25}Я закашлял.{/alpha}"
    l"{cps=25}Вот-вот. Я тоже в шоке была."
l"{cps=25}Нужно тренироваться, готовиться к турниру, а они говорят, чтобы я нашла себе парня."
a"{cps=25}Да уж, у меня таких проблем ещё не возникало."
l"{cps=25}Вот поэтому я и здесь."
a"{cps=25}..."
"{alpha=.5}{cps=25}Тут было сложно помочь.{/alpha}"
l"{cps=25}Не бери в голову. Как-нибудь разрулим."
a"{cps=25}Надеюсь."
scene black
"{alpha=.5}{cps=25}Глаза начали закрываться.{/alpha}"
"{cps=25}Дойти бы до палатки."
"{cps=25}Сил нет."
"{alpha=.5}{cps=25}.{/alpha}"
"{alpha=.5}{cps=25}..{/alpha}"
stop music fadeout 1
play music "veter.mp3"
"{alpha=.5}{cps=25}...{/alpha}"
"{alpha=.5}{cps=25}Я проснулся от ужасного холода.{/alpha}"
a"{cps=25}Плохая была идея спать на улице."
"{cps=25}Моя рука сильно затекла."
a"{cps=25}Что?"
stop music fadeout 1
"{alpha=.5}{cps=25}Я повернулся налево. Там лежала дрожащая Алёна.{/alpha}"
scene alenaongrass2
a"{cps=25}Эй! Нужно залезть в палатку."
l"{cps=25}Отото."
a"{cps=25}Отото?"
l"{cps=25}Отнеси меня."
"{cps=25}Хм.."
scene black
"{alpha=.5}{cps=25}Я взял Алёну на руки и отнёс в палатку.{/alpha}"
l"{cps=25}Всё. Завтра возвращаюсь."
l"{cps=25}В таком холоде, я больше спать не буду."
a"{cps=25}Ну и правильно."
"{alpha=.5}{cps=25}Я взглянул на время.{w=2.0} 4:28. Я всё ещё хочу спать.{/alpha}"
menu:
    "Лечь в палатку вместе с Алёной.":
        jump Alena_palatka1
    "Пойти домой.":
        jump Alena_palatka2
label Alena_palatka1:
"{cps=25}Да, я слишком сонный, чтобы идти."
"{alpha=.5}{cps=25}Я рухнул в палатку.{/alpha}"
"{cps=25}."
"{cps=25}.."
"{cps=25}..."
play music "utro.mp3"
scene palatka
with hpunch
show alyona5
l"{cps=25}Извращенец!{w=0.5} Какого чёрта ты лёг спать со мной?!"
a"{cps=25}Так палатка одна."
hide alyona5
show alyona2
l"{cps=25}Всё равно ты не должен был этого делать."
a"{cps=25}Ладно, я пошёл."
hide alyona2
l"{cps=25}Да давай!"
show alyona1
l"{cps=25}И спасибо тебе за всё."
a"{cps=25}Пожалуйста."
label Alena_palatka2:
"{alpha=.5}{cps=25}Я направился домой.{/alpha}"
jump All_done2









label All_done2:
scene laptop2
a"{cps=25}Итак, пришло время турнира."
"{alpha=.5}{cps=25}Я собрался и направился на встречу с командой.{/alpha}"
play music "Street.mp3"
scene schooltrip
with fade
scene street3
with fade
show alyona1
show fiona14 at right
show kristina1 at left
k"{cps=25}Мы опаздываем."
scene tournament
with fade
"{alpha=.5}{cps=25}Когда мы пришли всё уже началось.{/alpha}"
play music "trevoga.mp3"
define kom = Character('Комментатор', color="#ffffe0")
kom"{cps=25}- Сегодня в этом зале собрались 8 лучших команд нашего региона для того чтобы побороться за приз в 500000 рублей"
kom"{cps=25}- Представляем вашему вниманию турнирную сетку"
"{alpha=.5}{cps=25}Турнирная сетка высветилась на табло, находившееся высоко над сценой.{/alpha}"
"{alpha=.5}{cps=25}Я вгляделся в неё и заметил кое-что интересное.{/alpha}"
"{alpha=.5}{cps=25}Среди списка команд есть и моя прошлая.{/alpha}"
"{alpha=.5}{cps=25}Я думал, что без меня и Вячеслава они ничего не смогут.{/alpha}"
"{alpha=.5}{cps=25}Я смогу встретиться с ними только в финале.{/alpha}"
"{alpha=.5}{cps=25}Девчонки тоже внимательно следили за таблицей.{/alpha}"
"{alpha=.5}{cps=25}Вскоре нас проводили в будку ожидания.{/alpha}"
scene black
"{alpha=.5}{cps=25}Время начало тянуться медленней.{/alpha}"
a"{cps=25}Сегодня первый матч."
k"{cps=25}Я очень волнуюсь."
f"{cps=25}Мы все волнуемся."
a"{cps=25}Всё будет хорошо."
"{alpha=.5}{cps=25}В этот момент двери открылись, и нас позвали.{/alpha}"
scene tournament
with fade
"{alpha=.5}{cps=25}В зале почти никого не было.{/alpha}"
"{cps=25}Неудевительно, ведь мы команда новичков, поэтому болельщиков у нас не нашлось.{w=0.5} Но похоже то же самое можно было сказать и про наших оппонентов."
"{alpha=.5}{cps=25}На сцене были кабинки для игроков.{/alpha}"
"{alpha=.5}{cps=25}Они были звуконепроницаемые для того, чтобы не отвлекать игроков, и в то же время не давать им слышать разговор комментаторов.{/alpha}"
"{alpha=.5}{cps=25}Мы поздоровались с противоположной командой и прошли в кабинки.{/alpha}"
a"{cps=25}Поехали!"
jump previugame3
label choise1n3:
hide screen restartn3
$game1vibor+=1
hide screen kristina_karta1n3
hide screen fiona_karta1n3
hide screen alena_karta1n3
hide screen gg_karta1n3
show ggkarta1:
    xalign 0.3
    yalign 0.6
show alenakarta1:
    xalign 0.1
    yalign 0.6
show fionakarta1:
    xalign 0.3
    yalign 0.2
show kristinakarta2:
    xalign 0.1
    yalign 0.2
if game1vibor==1:
    "wewewewdfdffdfdfdfdfdfd"
    if sluchain1 == 1:
        $attack+=1;
        show sword1:
            xalign 0.1
            yalign 0.04
        pause 2
        hide kristinakarta2
        jump choise0n3
    else:
        hide fionakarta1
        hide alenakarta1
        hide ggkarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Перейти к защите":
                jump armor_three
else:
    if game1vibor==2:
        if sluchain2 == 1:
            $attack+=1;
            show sword2:
                xalign 0.15
                yalign 0.04
            pause 2
            hide kristinakarta2
            jump choise0n3
        else:
            hide fionakarta1
            hide alenakarta1
            hide ggkarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Перейти к защите":
                    jump armor_three
    else:
        if game1vibor==3:
            if sluchain3 == 1:
                $attack+=1;
                show sword3:
                    xalign 0.2
                    yalign 0.04
                pause 2
                hide kristinakarta2
                jump choise0n3
            else:
                hide fionakarta1
                hide alenakarta1
                hide ggkarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Перейти к защите":
                        jump armor_three


label choise2n3:
hide screen restartn3
$game1vibor+=1
hide screen kristina_karta1n3
hide screen fiona_karta1n3
hide screen alena_karta1n3
hide screen gg_karta1n3
show ggkarta1:
    xalign 0.3
    yalign 0.6
show alenakarta1:
    xalign 0.1
    yalign 0.6
show fionakarta2:
    xalign 0.3
    yalign 0.2
show kristinakarta1:
    xalign 0.1
    yalign 0.2
if game1vibor==1:
    if sluchain1 == 2:
        $attack+=1;
        show sword1:
            xalign 0.1
            yalign 0.04
        pause 2
        hide fionakarta2
        jump choise0n3
    else:
        hide kristinakarta1
        hide alenakarta1
        hide ggkarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Перейти к защите":
                jump armor_three
else:
    if game1vibor==2:
        if sluchain2 == 2:
            $attack+=1;
            show sword2:
                xalign 0.15
                yalign 0.04
            pause 2
            hide fionakarta2
            jump choise0n3
        else:
            hide kristinakarta1
            hide alenakarta1
            hide ggkarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Перейти к защите":
                    jump armor_three
    else:
        if game1vibor==3:
            if sluchain3 == 2:
                $attack+=1;
                show sword3:
                    xalign 0.2
                    yalign 0.04
                pause 2
                hide fionakarta2
                jump choise0n3
            else:
                hide kristinakarta1
                hide alenakarta1
                hide ggkarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Перейти к защите":
                        jump armor_three


label choise3n3:
hide screen restartn3
$game1vibor+=1
hide screen kristina_karta1n3
hide screen fiona_karta1n3
hide screen alena_karta1n3
hide screen gg_karta1n3
show ggkarta1:
    xalign 0.3
    yalign 0.6
show alenakarta2:
    xalign 0.1
    yalign 0.6
show fionakarta1:
    xalign 0.3
    yalign 0.2
show kristinakarta1:
    xalign 0.1
    yalign 0.2
if game1vibor==1:
    if sluchain1 == 3:
        $attack+=1;
        show sword1:
            xalign 0.1
            yalign 0.04
        pause 2
        hide alenakarta2
        jump choise0n3
    else:
        hide kristinakarta1
        hide fionakarta1
        hide ggkarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Перейти к защите":
                jump armor_three
else:
    if game1vibor==2:
        if sluchain2 == 3:
            $attack+=1;
            show sword2:
                xalign 0.15
                yalign 0.04
            pause 2
            hide alenakarta2
            jump choise0n3
        else:
            hide kristinakarta1
            hide fionakarta1
            hide ggkarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Перейти к защите":
                    jump armor_three
    else:
        if game1vibor==3:
            if sluchain3 == 3:
                $attack+=1;
                show sword3:
                    xalign 0.2
                    yalign 0.04
                pause 2
                hide alenakarta2
                jump choise0n3
            else:
                hide kristinakarta1
                hide fionakarta1
                hide ggkarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Перейти к защите":
                        jump armor_three
label choise4n3:
hide screen restartn3
$game1vibor+=1
hide screen kristina_karta1n3
hide screen fiona_karta1n3
hide screen alena_karta1n3
hide screen gg_karta1n3
show ggkarta2:
    xalign 0.3
    yalign 0.6
show alenakarta1:
    xalign 0.1
    yalign 0.6
show fionakarta1:
    xalign 0.3
    yalign 0.2
show kristinakarta1:
    xalign 0.1
    yalign 0.2
if game1vibor==1:
    if sluchain1 == 4:
        $attack+=1;
        show sword1:
            xalign 0.1
            yalign 0.04
        pause 2
        hide ggkarta2
        jump choise0n3
    else:
        hide kristinakarta1
        hide fionakarta1
        hide alenakarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Перейти к защите":
                jump armor_three
else:
    if game1vibor==2:
        if sluchain2 == 4:
            $attack+=1;
            show sword2:
                xalign 0.15
                yalign 0.04
            pause 2
            hide ggkarta2
            jump choise0n3
        else:
            hide kristinakarta1
            hide fionakarta1
            hide alenakarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Перейти к защите":
                    jump armor_three
    else:
        if game1vibor==3:
            if sluchain3 == 4:
                $attack+=1;
                show sword3:
                    xalign 0.2
                    yalign 0.04
                pause 2
                hide alenakarta2
                jump choise0n3
            else:
                hide kristinakarta1
                hide fionakarta1
                hide ggkarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Перейти к защите":
                        jump armor_three

label previugame3:
    menu:
        "Прочитать правила":
            jump pravila3
        "Начать игру":
            jump game3
    label pravila3:
    scene pravila1
    "Приветсвую в мини-игре!"
    "Для победы над противником вам нужно набрать достаточное количество атаки и защиты."
    "Очки атаки вы зарабатываете,поочерёдно угадывая синие карты, которые открылись после начала игры."
    "Очки защиты вы зарабатываете,поочерёдно угадывая красные карты, которые открылись после начала игры."
    menu:
        "Начать игру":
            jump game3
    label game3:
    "У противника сильная защита и средняя атака."
    hide screen kristina_karta1n3
    hide screen fiona_karta1n3
    hide screen alena_karta1n3
    hide screen gg_karta1n3
    hide screen viacheslav_karta1n3
    hide screen tamara_karta1n3
    hide screen gopnik_karta1n3
    hide screen starik_karta1n3
    window hide
    scene background4
    $armor = 0
    $attack = 0
    $game1vibor2=0
    $game1vibor=0
    $sluchain1 = 0
    $sluchain2 = 0
    $sluchain3 = 0
    $sluchain4 = 0
    screen restartn3:
        imagebutton xalign 0.5 yalign 0.2:
            idle ("restart.png")
            action Jump("previugame3")
    show kristinakarta1:
        xalign 0.1
        yalign 0.2
    show fionakarta1:
        xalign 0.3
        yalign 0.2
    show alenakarta1:
        xalign 0.1
        yalign 0.6
    show ggkarta1:
        xalign 0.3
        yalign 0.6
    show viacheslavkarta1:
        xalign 0.65
        yalign 0.2
    show tamarakarta1:
        xalign 0.85
        yalign 0.2
    show gopnikkarta1:
        xalign 0.65
        yalign 0.6
    show starikkarta1:
        xalign 0.85
        yalign 0.6
    $sluchain1 = renpy.random.randint(1,4)
    $sluchain1v2 = renpy.random.randint(1,4)
####Разворот первых двух карт
    pause 2
    if sluchain1 == 1:#Первая синяя карта
        hide kristinakarta1
        show kristinakarta2:
            xalign 0.1
            yalign 0.2
    if sluchain1v2 == 1:#Первая красная карта
        hide viacheslavkarta1
        show viacheslavkarta2:
            xalign 0.65
            yalign 0.2
    if sluchain1 == 2:
        hide fionakarta1
        show fionakarta2:
            xalign 0.3
            yalign 0.2
    if sluchain1v2 == 2:
        hide tamarakarta1
        show tamarakarta2:
            xalign 0.85
            yalign 0.2
    if sluchain1 == 3:
        hide alenakarta1
        show alenakarta2:
            xalign 0.1
            yalign 0.6
    if sluchain1v2 == 3:
        hide gopnikkarta1
        show gopnikkarta2:
            xalign 0.65
            yalign 0.6
    if sluchain1 == 4:
        hide ggkarta1
        show ggkarta2:
            xalign 0.3
            yalign 0.6
    if sluchain1v2 == 4:
        hide starikkarta1
        show starikkarta2:
            xalign 0.85
            yalign 0.6
#####Разворот обратно этих же карт
    pause 2
    if sluchain1 == 1:
        hide kristinakarta2
        show kristinakarta1:
            xalign 0.1
            yalign 0.2
    if sluchain1v2 == 1:
        hide viacheslavkarta2
        show viacheslavkarta1:
            xalign 0.65
            yalign 0.2
    if sluchain1 == 2:
        hide fionakarta2
        show fionakarta1:
            xalign 0.3
            yalign 0.2
    if sluchain1v2 == 2:
        hide tamarakarta2
        show tamarakarta1:
            xalign 0.85
            yalign 0.2
    if sluchain1 == 3:
        hide alenakarta2
        show alenakarta1:
            xalign 0.1
            yalign 0.6
    if sluchain1v2 == 3:
        hide gopnikkarta2
        show gopnikkarta1:
            xalign 0.65
            yalign 0.6
    if sluchain1 == 4:
        hide ggkarta2
        show ggkarta1:
            xalign 0.3
            yalign 0.6
    if sluchain1v2 == 4:
        hide starikkarta2
        show starikkarta1:
            xalign 0.85
            yalign 0.6

    pause 2
#######Razvorot sleduyushih dvuh kart

    $sluchain2 = renpy.random.randint(1,4)
    $sluchain2v2 = renpy.random.randint(1,4)
    if sluchain2 == 1:#Первая синяя карта
        hide kristinakarta1
        show kristinakarta2:
            xalign 0.1
            yalign 0.2
    if sluchain2v2 == 1:#Первая красная карта
        hide viacheslavkarta1
        show viacheslavkarta2:
            xalign 0.65
            yalign 0.2
    if sluchain2 == 2:
        hide fionakarta1
        show fionakarta2:
            xalign 0.3
            yalign 0.2
    if sluchain2v2 == 2:
        hide tamarakarta1
        show tamarakarta2:
            xalign 0.85
            yalign 0.2
    if sluchain2 == 3:
        hide alenakarta1
        show alenakarta2:
            xalign 0.1
            yalign 0.6
    if sluchain2v2 == 3:
        hide gopnikkarta1
        show gopnikkarta2:
            xalign 0.65
            yalign 0.6
    if sluchain2 == 4:
        hide ggkarta1
        show ggkarta2:
            xalign 0.3
            yalign 0.6
    if sluchain2v2 == 4:
        hide starikkarta1
        show starikkarta2:
            xalign 0.85
            yalign 0.6
#####Разворот обратно этих же карт
    pause 2
    if sluchain2 == 1:
        hide kristinakarta2
        show kristinakarta1:
            xalign 0.1
            yalign 0.2
    if sluchain2v2 == 1:
        hide viacheslavkarta2
        show viacheslavkarta1:
            xalign 0.65
            yalign 0.2
    if sluchain2 == 2:
        hide fionakarta2
        show fionakarta1:
            xalign 0.3
            yalign 0.2
    if sluchain2v2 == 2:
        hide tamarakarta2
        show tamarakarta1:
            xalign 0.85
            yalign 0.2
    if sluchain2 == 3:
        hide alenakarta2
        show alenakarta1:
            xalign 0.1
            yalign 0.6
    if sluchain2v2 == 3:
        hide gopnikkarta2
        show gopnikkarta1:
            xalign 0.65
            yalign 0.6
    if sluchain2 == 4:
        hide ggkarta2
        show ggkarta1:
            xalign 0.3
            yalign 0.6
    if sluchain2v2 == 4:
        hide starikkarta2
        show starikkarta1:
            xalign 0.85
            yalign 0.6

    pause 2
################################
    $sluchain3 = renpy.random.randint(1,4)
    $sluchain3v2 = renpy.random.randint(1,4)
    if sluchain3 == 1:
        hide kristinakarta1
        show kristinakarta2:
            xalign 0.1
            yalign 0.2
    if sluchain3v2 == 1:
        hide viacheslavkarta1
        show viacheslavkarta2:
            xalign 0.65
            yalign 0.2
    if sluchain3 == 2:
        hide fionakarta1
        show fionakarta2:
            xalign 0.3
            yalign 0.2
    if sluchain3v2 == 2:
        hide tamarakarta1
        show tamarakarta2:
            xalign 0.85
            yalign 0.2
    if sluchain3 == 3:
        hide alenakarta1
        show alenakarta2:
            xalign 0.1
            yalign 0.6
    if sluchain3v2 == 3:
        hide gopnikkarta1
        show gopnikkarta2:
            xalign 0.65
            yalign 0.6
    if sluchain3 == 4:
        hide ggkarta1
        show ggkarta2:
            xalign 0.3
            yalign 0.6
    if sluchain3v2 == 4:
        hide starikkarta1
        show starikkarta2:
            xalign 0.85
            yalign 0.6
    pause 2
########################
    if sluchain3 == 1:
        hide kristinakarta2
        show kristinakarta1:
            xalign 0.1
            yalign 0.2
    if sluchain3v2 == 1:
        hide viacheslavkarta2
        show viacheslavkarta1:
            xalign 0.65
            yalign 0.2
    if sluchain3 == 2:
        hide fionakarta2
        show fionakarta1:
            xalign 0.3
            yalign 0.2
    if sluchain3v2 == 2:
        hide tamarakarta2
        show tamarakarta1:
            xalign 0.85
            yalign 0.2
    if sluchain3 == 3:
        hide alenakarta2
        show alenakarta1:
            xalign 0.1
            yalign 0.6
    if sluchain3v2 == 3:
        hide gopnikkarta2
        show gopnikkarta1:
            xalign 0.65
            yalign 0.6
    if sluchain3 == 4:
        hide ggkarta2
        show ggkarta1:
            xalign 0.3
            yalign 0.6
    if sluchain3v2 == 4:
        hide starikkarta2
        show starikkarta1:
            xalign 0.85
            yalign 0.6
    pause 2
#################
    hide kristinakarta1
    hide fionakarta1
    hide alenakarta1
    hide ggkarta1
    hide viacheslavkarta1
    hide tamarakarta1
    hide gopnikkarta1
    hide starikkarta1


    label choise0n3:
    hide screen kristina_karta1n3
    hide screen fiona_karta1n3
    hide screen alena_karta1n3
    hide screen gg_karta1n3
    if game1vibor==3:
        window show
        "Вы заработали максимальную атаку."
        menu:
            "Перейти к защите":
                jump armor_three
    screen kristina_karta1n3:
        imagebutton xalign 0.1 yalign 0.2:
            idle ("karta2.png")
            hover ("karta3.png")
            action Jump("choise1n3")
    show screen kristina_karta1n3
    screen fiona_karta1n3:
        imagebutton xalign 0.3 yalign 0.2:
            idle ("karta2.png")
            hover ("karta3.png")
            action Jump("choise2n3")
    show screen fiona_karta1n3
    screen alena_karta1n3:
        imagebutton xalign 0.1 yalign 0.6:
            idle ("karta2.png")
            hover ("karta3.png")
            action Jump("choise3n3")
    show screen alena_karta1n3
    screen gg_karta1n3:
        imagebutton xalign 0.3 yalign 0.6:
            idle ("karta2.png")
            hover ("karta3.png")
            action Jump("choise4n3")
    show screen gg_karta1n3
    call screen restartn3

label armor_three:
    hide screen viacheslav_karta1n3
    hide screen tamara_karta1n3
    hide screen gopnik_karta1n3
    hide screen starik_karta1n3
    window hide
    if game1vibor2==3:
        window show
        "Вы заработали максимальную защиту."
        menu:
            "Начать битву":
                jump fight_three
    screen viacheslav_karta1n3:
        imagebutton xalign 0.65 yalign 0.2:
            idle ("karta4.png")
            hover ("karta5.png")
            action Jump("choise5n3")
    show screen viacheslav_karta1n3
    screen tamara_karta1n3:
        imagebutton xalign 0.85 yalign 0.2:
            idle ("karta4.png")
            hover ("karta5.png")
            action Jump("choise6n3")
    show screen tamara_karta1n3
    screen gopnik_karta1n3:
        imagebutton xalign 0.65 yalign 0.6:
            idle ("karta4.png")
            hover ("karta5.png")
            action Jump("choise7n3")
    show screen gopnik_karta1n3
    screen starik_karta1n3:
        imagebutton xalign 0.85 yalign 0.6:
            idle ("karta4.png")
            hover ("karta5.png")
            action Jump("choise8n3")
    show screen starik_karta1n3
    call screen restartn3

label choise5n3:
hide screen restartn3
$game1vibor2+=1
hide screen starik_karta1n3
hide screen gopnik_karta1n3
hide screen tamara_karta1n3
hide screen viacheslav_karta1n3
show starikkarta1:
    xalign 0.85
    yalign 0.2
show gopnikkarta1:
    xalign 0.65
    yalign 0.6
show tamarakarta1:
    xalign 0.85
    yalign 0.6
show viacheslavkarta2:
    xalign 0.65
    yalign 0.2
if game1vibor2==1:
    if sluchain1v2 == 1:
        $armor+=1;
        show shield1:
            xalign 0.6
            yalign 0.04
        pause 2
        hide viacheslavkarta2
        jump armor_three
    else:
        hide starikkarta1
        hide gopnikkarta1
        hide tamarakarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Начать битву":
                jump fight_three
else:
    if game1vibor2==2:
        if sluchain2v2 == 1:
            $armor+=1;
            show shield2:
                xalign 0.65
                yalign 0.04
            pause 2
            hide viacheslavkarta2
            jump armor_three
        else:
            hide starikkarta1
            hide gopnikkarta1
            hide tamarakarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Начать битву":
                    jump fight_three
    else:
        if game1vibor2==3:
            if sluchain3v2 == 1:
                $armor+=1;
                show shield3:
                    xalign 0.7
                    yalign 0.04
                pause 2
                hide viacheslavkarta2
                jump armor_three
            else:
                hide starikkarta1
                hide gopnikkarta1
                hide tamarakarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Начать битву":
                        jump fight_three
label choise6n3:
hide screen restartn3
$game1vibor2+=1
hide screen starik_karta1n3
hide screen gopnik_karta1n3
hide screen tamara_karta1n3
hide screen viacheslav_karta1n3
show starikkarta1:
    xalign 0.85
    yalign 0.2
show gopnikkarta1:
    xalign 0.65
    yalign 0.6
show viacheslavkarta1:
    xalign 0.65
    yalign 0.2
show tamarakarta2:
    xalign 0.85
    yalign 0.2
if game1vibor2==1:
    if sluchain1v2 == 2:
        $armor+=1;
        show shield1:
            xalign 0.6
            yalign 0.04
        pause 2
        hide tamarakarta2
        jump armor_three
    else:
        hide starikkarta1
        hide gopnikkarta1
        hide viacheslavkarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Начать битву":
                jump fight_three
else:
    if game1vibor2==2:
        if sluchain2v2 == 2:
            $armor+=1;
            show shield2:
                xalign 0.65
                yalign 0.04
            pause 2
            hide tamarakarta2
            jump armor_three
        else:
            hide starikkarta1
            hide gopnikkarta1
            hide viacheslavkarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Начать битву":
                    jump fight_three
    else:
        if game1vibor2==3:
            if sluchain3v2 == 2:
                $armor+=1;
                show shield3:
                    xalign 0.7
                    yalign 0.04
                pause 2
                hide tamarakarta2
                jump armor_three
            else:
                hide starikkarta1
                hide gopnikkarta1
                hide viacheslavkarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Начать битву":
                        jump fight_three
label choise7n3:
hide screen restartn3
$game1vibor2+=1
hide screen starik_karta1n3
hide screen gopnik_karta1n3
hide screen tamara_karta1n3
hide screen viacheslav_karta1n3
show starikkarta1:
    xalign 0.85
    yalign 0.2
show viacheslavkarta1:
    xalign 0.65
    yalign 0.2
show tamarakarta1:
    xalign 0.85
    yalign 0.2
show gopnikkarta2:
    xalign 0.65
    yalign 0.6
if game1vibor2==1:
    if sluchain1v2 == 3:
        $armor+=1;
        show shield1:
            xalign 0.6
            yalign 0.04
        pause 2
        hide gopnikkarta2
        jump armor_three
    else:
        hide starikkarta1
        hide tamarakarta1
        hide viacheslavkarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Начать битву":
                jump fight_three
else:
    if game1vibor2==2:
        if sluchain2v2 == 3:
            $armor+=1;
            show shield2:
                xalign 0.65
                yalign 0.04
            pause 2
            hide gopnikkarta2
            jump armor_three
        else:
            hide starikkarta1
            hide tamarakarta1
            hide viacheslavkarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Начать битву":
                    jump fight_three
    else:
        if game1vibor2==3:
            if sluchain3v2 == 3:
                $armor+=1;
                show shield3:
                    xalign 0.7
                    yalign 0.04
                pause 2
                hide gopnikkarta2
                jump armor_three
            else:
                hide starikkarta1
                hide tamarakarta1
                hide viacheslavkarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Начать битву":
                        jump fight_three
label choise8n3:
hide screen restartn3
$game1vibor2+=1
hide screen starik_karta1n3
hide screen gopnik_karta1n3
hide screen tamara_karta1n3
hide screen viacheslav_karta1n3
show starikkarta2:
    xalign 0.85
    yalign 0.6
show viacheslavkarta1:
    xalign 0.65
    yalign 0.2
show tamarakarta1:
    xalign 0.85
    yalign 0.2
show gopnikkarta1:
    xalign 0.65
    yalign 0.6
if game1vibor2==1:
    if sluchain1v2 == 4:
        $armor+=1;
        show shield1:
            xalign 0.6
            yalign 0.04
        pause 2
        hide starikkarta2
        jump armor_three
    else:
        hide gopnikkarta1
        hide tamarakarta1
        hide viacheslavkarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Начать битву":
                jump fight_three
else:
    if game1vibor2==2:
        if sluchain2v2 == 4:
            $armor+=1;
            show shield2:
                xalign 0.65
                yalign 0.04
            pause 2
            hide starikkarta2
            jump armor_three
        else:
            hide gopnikkarta1
            hide tamarakarta1
            hide viacheslavkarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Начать битву":
                    jump fight_three
    else:
        if game1vibor2==3:
            if sluchain3v2 == 4:
                $armor+=1;
                show shield3:
                    xalign 0.7
                    yalign 0.04
                pause 2
                hide starikkarta2
                jump armor_three
            else:
                hide gopnikkarta1
                hide tamarakarta1
                hide viacheslavkarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Начать битву":
                        jump fight_three
label fight_three:
    hide screen viacheslav_karta1n3
    hide screen tamara_karta1n3
    hide screen gopnik_karta1n3
    hide screen starik_karta1n3
    if attack>2 and armor>1:
        scene win
        "Атаки и защиты хватило чтобы победить!"
        jump five
    else:
        scene lose
        if attack<3 and armor<2:
            "Наша защита была разгромлена, наши атаки не достигли противника."
        else:
            if attack<3:
                "Наши атаки не достигли противника."
            if armor<2:
                "Наша защита была разгромлена."
        menu:
            "Начать заново":
                jump previugame3
label five:
a"{cps=25}Отлично! Мы прошли в полуфинал."
a"{cps=25}Выложимся завтра на полную!"
kicon"{cps=25}Да!"
ficon"{cps=25}Обязательно!"
licon"{cps=25}Завтра нужно повторить так же."
stop music fadeout 1
scene tournament
with fade
play music "school.mp3"
"{alpha=.5}{cps=25}На выходе я встретил парня с красными волосами."
show denis1
d"{cps=25}Привет ребята!"
"{alpha=.5}{cps=25}Где-то я уже его видел."
a"{cps=25}О, привет!"
d"{cps=25}Классный поединок вы тут устроили."
a"{cps=25}Мы старались."
d"{cps=25}Моя команда тоже победила в первом раунде."
d"{cps=25}Если ты и я победим всех своих соперников , то мы встретимся в финале."
a"{cps=25}Может быть."
d"{cps=25}Ладно, увидимся."
a"{cps=25}Пока!"
hide denis1
"{alpha=.5}{cps=25}Я себя плохо чувствовал после поединка."
a"{cps=25}Пойду домой."
scene laptop1
with fade
play music "Relax.mp3"
"{alpha=.5}{cps=25}Обессиленный я упал в кровать."
scene black
"{alpha=.5}{cps=25}Первый бой был не таким как я его представлял."
"{alpha=.5}{cps=25}Конечно, мы победили, но играть перед пустым залом было некомфортно."
"{cps=25}Надеюсь завтра будет лучше."
scene laptop2
play music "Utro.mp3"
"{cps=25}Утро. Мне всё ещё плохо."
"{cps=25}Прогуляюсь в больницу к маме."
scene black
"{alpha=.5}{cps=25}Она снова спала, так что недолго посидев, я вышел из больницы."
"{alpha=.5}{cps=25}Однако там меня ожидали."
play music "street.mp3"
scene schooltrip
show alyona2
show fiona2 at right
show kristina2 at left
"{cps=25}Что вы тут делаете?"
k"{cps=25}Всем было интересно, зачем ты иногда ходил в больницу."
l"{cps=25}Есть ещё одна причина по которой мы здесь."
l"{cps=25}Ты не пришёл на место встречи вовремя, и теперь мы опаздываем."
"{alpha=.5}{cps=25}Я посмотрел на время."
"{cps=25}15 минут до начала!"
a"{cps=25}Бежим!"
scene street3
with fade
"{alpha=.5}{cps=25}Пока я бежал, у меня усилилась боль в голове."
scene tournament
with fade
stop music fadeout 1
"{alpha=.5}{cps=25}На сцене стояли все команды пробившиеся в полуфинал."
"{alpha=.5}{cps=25}Среди них я разглядел Дениса. Он помахал мне рукой."
kom"{cps=25}- Итак сегодня состоится полуфинал, в результате которого нас покинут ещё две команды. 2 поединка будут проведены одновременно в разных залах."
kom"{cps=25}- Просим участников пройти в свои кабинки."
"{alpha=.5}{cps=25}Мы сели за компы и начали настраивать управление."
"{cps=25}.."
"{cps=25}Плохо что-то."
"{alpha=.5}{cps=25}Я попытался встать, чтобы выйти, но тут же упал."
"{cps=25}А потом темнота."
scene black
"{cps=25}"
d"{cps=25}Я поправил стул и уселся поудобнее."
d"{cps=25}Ребят, у вас всё нормально?"
rebiata"{cps=25}Да, а вот похоже в соседнем зале что-то произошло."
"{cps=25}Время ещё было, так что я решил пойти посмотреть."
scene ggdie with fade
play music "trevoga.mp3"
f"Боже, что с ним."
l"Похоже эпилепсия."
f"Нет, не умирай."
l"Успокойся. Всё не так серьёзно."
k"Но играть он не сможет."
k"Я позову организаторов."
scene black
scene tournament with fade
show fiona15
stop music fadeout 1
f"Если нас дисквалифицируют, то Сергей не сможет оплатить операцию своей матери."
"{cps=25}Я не знал, что у него такие благие намерения."
d"{cps=25}Здрасте, я знакомый Сергея."
d"{cps=25}Может я могу чем-нибудь помочь?"
show alyona5 at right
show fiona15 at left with move
d"{cps=25}Даже не знаю."
show kristina9
k"{cps=25}Организаторы уже вызвали скорую, но..."
d"{cps=25}Но?"
k"{cps=25}Но они не смогут перенести поединок."
k"{cps=25}Похоже это конец."
"{cps=25}Не хотелось бы мне подводить команду, но.."
d"{cps=25}Я могу его заменить."
f"{cps=25}Но ты же сам сейчас должен сейчас играть."
d"{cps=25}Команда меня поймёт, а у вас серьёзный повод для того чтобы выиграть."
"{alpha=.5}{cps=25}Организатор сказал, что даёт нам 3 минуты."
"{alpha=.5}{cps=25}Я предупредил команду и сел к девчонкам."
jump previugame4
label choise1n4:
hide screen restartn4
$game1vibor+=1
hide screen kristina_karta1n4
hide screen fiona_karta1n4
hide screen alena_karta1n4
hide screen gg_karta1n4
show ggkarta1:
    xalign 0.3
    yalign 0.6
show alenakarta1:
    xalign 0.1
    yalign 0.6
show fionakarta1:
    xalign 0.3
    yalign 0.2
show kristinakarta2:
    xalign 0.1
    yalign 0.2
if game1vibor==1:
    if sluchain1 == 1:
        $attack+=1;
        show sword1:
            xalign 0.1
            yalign 0.04
        pause 2
        hide kristinakarta2
        jump choise0n4
    else:
        hide fionakarta1
        hide alenakarta1
        hide ggkarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Перейти к защите":
                jump armor_four
else:
    if game1vibor==2:
        if sluchain2 == 1:
            $attack+=1;
            show sword2:
                xalign 0.15
                yalign 0.04
            pause 2
            hide kristinakarta2
            jump choise0n4
        else:
            hide fionakarta1
            hide alenakarta1
            hide ggkarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Перейти к защите":
                    jump armor_four
    else:
        if game1vibor==3:
            if sluchain3 == 1:
                $attack+=1;
                show sword3:
                    xalign 0.2
                    yalign 0.04
                pause 2
                hide kristinakarta2
                jump choise0n4
            else:
                hide fionakarta1
                hide alenakarta1
                hide ggkarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Перейти к защите":
                        jump armor_four


label choise2n4:
hide screen restartn4
$game1vibor+=1
hide screen kristina_karta1n4
hide screen fiona_karta1n4
hide screen alena_karta1n4
hide screen gg_karta1n4
show ggkarta1:
    xalign 0.3
    yalign 0.6
show alenakarta1:
    xalign 0.1
    yalign 0.6
show fionakarta2:
    xalign 0.3
    yalign 0.2
show kristinakarta1:
    xalign 0.1
    yalign 0.2
if game1vibor==1:
    if sluchain1 == 2:
        $attack+=1;
        show sword1:
            xalign 0.1
            yalign 0.04
        pause 2
        hide fionakarta2
        jump choise0n4
    else:
        hide kristinakarta1
        hide alenakarta1
        hide ggkarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Перейти к защите":
                jump armor_four
else:
    if game1vibor==2:
        if sluchain2 == 2:
            $attack+=1;
            show sword2:
                xalign 0.15
                yalign 0.04
            pause 2
            hide fionakarta2
            jump choise0n4
        else:
            hide kristinakarta1
            hide alenakarta1
            hide ggkarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Перейти к защите":
                    jump armor_four
    else:
        if game1vibor==3:
            if sluchain3 == 2:
                $attack+=1;
                show sword3:
                    xalign 0.2
                    yalign 0.04
                pause 2
                hide fionakarta2
                jump choise0n4
            else:
                hide kristinakarta1
                hide alenakarta1
                hide ggkarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Перейти к защите":
                        jump armor_four


label choise3n4:
hide screen restartn4
$game1vibor+=1
hide screen kristina_karta1n4
hide screen fiona_karta1n4
hide screen alena_karta1n4
hide screen gg_karta1n4
show ggkarta1:
    xalign 0.3
    yalign 0.6
show alenakarta2:
    xalign 0.1
    yalign 0.6
show fionakarta1:
    xalign 0.3
    yalign 0.2
show kristinakarta1:
    xalign 0.1
    yalign 0.2
if game1vibor==1:
    if sluchain1 == 3:
        $attack+=1;
        show sword1:
            xalign 0.1
            yalign 0.04
        pause 2
        hide alenakarta2
        jump choise0n4
    else:
        hide kristinakarta1
        hide fionakarta1
        hide ggkarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Перейти к защите":
                jump armor_four
else:
    if game1vibor==2:
        if sluchain2 == 3:
            $attack+=1;
            show sword2:
                xalign 0.15
                yalign 0.04
            pause 2
            hide alenakarta2
            jump choise0n4
        else:
            hide kristinakarta1
            hide fionakarta1
            hide ggkarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Перейти к защите":
                    jump armor_four
    else:
        if game1vibor==3:
            if sluchain3 == 3:
                $attack+=1;
                show sword3:
                    xalign 0.2
                    yalign 0.04
                pause 2
                hide alenakarta2
                jump choise0n4
            else:
                hide kristinakarta1
                hide fionakarta1
                hide ggkarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Перейти к защите":
                        jump armor_four
label choise4n4:
hide screen restartn4
$game1vibor+=1
hide screen kristina_karta1n4
hide screen fiona_karta1n4
hide screen alena_karta1n4
hide screen gg_karta1n4
show ggkarta2:
    xalign 0.3
    yalign 0.6
show alenakarta1:
    xalign 0.1
    yalign 0.6
show fionakarta1:
    xalign 0.3
    yalign 0.2
show kristinakarta1:
    xalign 0.1
    yalign 0.2
if game1vibor==1:
    if sluchain1 == 4:
        $attack+=1;
        show sword1:
            xalign 0.1
            yalign 0.04
        pause 2
        hide ggkarta2
        jump choise0n4
    else:
        hide kristinakarta1
        hide fionakarta1
        hide alenakarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Перейти к защите":
                jump armor_four
else:
    if game1vibor==2:
        if sluchain2 == 4:
            $attack+=1;
            show sword2:
                xalign 0.15
                yalign 0.04
            pause 2
            hide ggkarta2
            jump choise0n4
        else:
            hide kristinakarta1
            hide fionakarta1
            hide alenakarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Перейти к защите":
                    jump armor_four
    else:
        if game1vibor==3:
            if sluchain3 == 4:
                $attack+=1;
                show sword3:
                    xalign 0.2
                    yalign 0.04
                pause 2
                hide alenakarta2
                jump choise0n4
            else:
                hide kristinakarta1
                hide fionakarta1
                hide ggkarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Перейти к защите":
                        jump armor_four

label previugame4:
    menu:
        "Прочитать правила":
            jump pravila4
        "Начать игру":
            jump game4
    label pravila4:
    scene pravila1
    "Приветсвую в мини-игре!"
    "Для победы над противником вам нужно набрать достаточное количество атаки и защиты."
    "Очки атаки вы зарабатываете,поочерёдно угадывая синие карты, которые открылись после начала игры."
    "Очки защиты вы зарабатываете,поочерёдно угадывая красные карты, которые открылись после начала игры."
    menu:
        "Начать игру":
            jump game4
    label game4:
    "У противника сильная защита и сильная атака."
    hide screen kristina_karta1n4
    hide screen fiona_karta1n4
    hide screen alena_karta1n4
    hide screen gg_karta1n4
    hide screen viacheslav_karta1n4
    hide screen tamara_karta1n4
    hide screen gopnik_karta1n4
    hide screen starik_karta1n4
    window hide
    scene background4
    $armor = 0
    $attack = 0
    $game1vibor2=0
    $game1vibor=0
    $sluchain1 = 0
    $sluchain2 = 0
    $sluchain3 = 0
    $sluchain4 = 0
    screen restartn4:
        imagebutton xalign 0.5 yalign 0.2:
            idle ("restart.png")
            action Jump("previugame4")
    show kristinakarta1:
        xalign 0.1
        yalign 0.2
    show fionakarta1:
        xalign 0.3
        yalign 0.2
    show alenakarta1:
        xalign 0.1
        yalign 0.6
    show ggkarta1:
        xalign 0.3
        yalign 0.6
    show viacheslavkarta1:
        xalign 0.65
        yalign 0.2
    show tamarakarta1:
        xalign 0.85
        yalign 0.2
    show gopnikkarta1:
        xalign 0.65
        yalign 0.6
    show starikkarta1:
        xalign 0.85
        yalign 0.6
    $sluchain1 = renpy.random.randint(1,4)
    $sluchain1v2 = renpy.random.randint(1,4)
####Разворот первых двух карт
    pause 2
    if sluchain1 == 1:#Первая синяя карта
        hide kristinakarta1
        show kristinakarta2:
            xalign 0.1
            yalign 0.2
    if sluchain1v2 == 1:#Первая красная карта
        hide viacheslavkarta1
        show viacheslavkarta2:
            xalign 0.65
            yalign 0.2
    if sluchain1 == 2:
        hide fionakarta1
        show fionakarta2:
            xalign 0.3
            yalign 0.2
    if sluchain1v2 == 2:
        hide tamarakarta1
        show tamarakarta2:
            xalign 0.85
            yalign 0.2
    if sluchain1 == 3:
        hide alenakarta1
        show alenakarta2:
            xalign 0.1
            yalign 0.6
    if sluchain1v2 == 3:
        hide gopnikkarta1
        show gopnikkarta2:
            xalign 0.65
            yalign 0.6
    if sluchain1 == 4:
        hide ggkarta1
        show ggkarta2:
            xalign 0.3
            yalign 0.6
    if sluchain1v2 == 4:
        hide starikkarta1
        show starikkarta2:
            xalign 0.85
            yalign 0.6
#####Разворот обратно этих же карт
    pause 2
    if sluchain1 == 1:
        hide kristinakarta2
        show kristinakarta1:
            xalign 0.1
            yalign 0.2
    if sluchain1v2 == 1:
        hide viacheslavkarta2
        show viacheslavkarta1:
            xalign 0.65
            yalign 0.2
    if sluchain1 == 2:
        hide fionakarta2
        show fionakarta1:
            xalign 0.3
            yalign 0.2
    if sluchain1v2 == 2:
        hide tamarakarta2
        show tamarakarta1:
            xalign 0.85
            yalign 0.2
    if sluchain1 == 3:
        hide alenakarta2
        show alenakarta1:
            xalign 0.1
            yalign 0.6
    if sluchain1v2 == 3:
        hide gopnikkarta2
        show gopnikkarta1:
            xalign 0.65
            yalign 0.6
    if sluchain1 == 4:
        hide ggkarta2
        show ggkarta1:
            xalign 0.3
            yalign 0.6
    if sluchain1v2 == 4:
        hide starikkarta2
        show starikkarta1:
            xalign 0.85
            yalign 0.6

    pause 2
#######Razvorot sleduyushih dvuh kart

    $sluchain2 = renpy.random.randint(1,4)
    $sluchain2v2 = renpy.random.randint(1,4)
    if sluchain2 == 1:#Первая синяя карта
        hide kristinakarta1
        show kristinakarta2:
            xalign 0.1
            yalign 0.2
    if sluchain2v2 == 1:#Первая красная карта
        hide viacheslavkarta1
        show viacheslavkarta2:
            xalign 0.65
            yalign 0.2
    if sluchain2 == 2:
        hide fionakarta1
        show fionakarta2:
            xalign 0.3
            yalign 0.2
    if sluchain2v2 == 2:
        hide tamarakarta1
        show tamarakarta2:
            xalign 0.85
            yalign 0.2
    if sluchain2 == 3:
        hide alenakarta1
        show alenakarta2:
            xalign 0.1
            yalign 0.6
    if sluchain2v2 == 3:
        hide gopnikkarta1
        show gopnikkarta2:
            xalign 0.65
            yalign 0.6
    if sluchain2 == 4:
        hide ggkarta1
        show ggkarta2:
            xalign 0.3
            yalign 0.6
    if sluchain2v2 == 4:
        hide starikkarta1
        show starikkarta2:
            xalign 0.85
            yalign 0.6
#####Разворот обратно этих же карт
    pause 2
    if sluchain2 == 1:
        hide kristinakarta2
        show kristinakarta1:
            xalign 0.1
            yalign 0.2
    if sluchain2v2 == 1:
        hide viacheslavkarta2
        show viacheslavkarta1:
            xalign 0.65
            yalign 0.2
    if sluchain2 == 2:
        hide fionakarta2
        show fionakarta1:
            xalign 0.3
            yalign 0.2
    if sluchain2v2 == 2:
        hide tamarakarta2
        show tamarakarta1:
            xalign 0.85
            yalign 0.2
    if sluchain2 == 3:
        hide alenakarta2
        show alenakarta1:
            xalign 0.1
            yalign 0.6
    if sluchain2v2 == 3:
        hide gopnikkarta2
        show gopnikkarta1:
            xalign 0.65
            yalign 0.6
    if sluchain2 == 4:
        hide ggkarta2
        show ggkarta1:
            xalign 0.3
            yalign 0.6
    if sluchain2v2 == 4:
        hide starikkarta2
        show starikkarta1:
            xalign 0.85
            yalign 0.6

    pause 2
################################
    $sluchain3 = renpy.random.randint(1,4)
    $sluchain3v2 = renpy.random.randint(1,4)
    if sluchain3 == 1:
        hide kristinakarta1
        show kristinakarta2:
            xalign 0.1
            yalign 0.2
    if sluchain3v2 == 1:
        hide viacheslavkarta1
        show viacheslavkarta2:
            xalign 0.65
            yalign 0.2
    if sluchain3 == 2:
        hide fionakarta1
        show fionakarta2:
            xalign 0.3
            yalign 0.2
    if sluchain3v2 == 2:
        hide tamarakarta1
        show tamarakarta2:
            xalign 0.85
            yalign 0.2
    if sluchain3 == 3:
        hide alenakarta1
        show alenakarta2:
            xalign 0.1
            yalign 0.6
    if sluchain3v2 == 3:
        hide gopnikkarta1
        show gopnikkarta2:
            xalign 0.65
            yalign 0.6
    if sluchain3 == 4:
        hide ggkarta1
        show ggkarta2:
            xalign 0.3
            yalign 0.6
    if sluchain3v2 == 4:
        hide starikkarta1
        show starikkarta2:
            xalign 0.85
            yalign 0.6
    pause 2
########################
    if sluchain3 == 1:
        hide kristinakarta2
        show kristinakarta1:
            xalign 0.1
            yalign 0.2
    if sluchain3v2 == 1:
        hide viacheslavkarta2
        show viacheslavkarta1:
            xalign 0.65
            yalign 0.2
    if sluchain3 == 2:
        hide fionakarta2
        show fionakarta1:
            xalign 0.3
            yalign 0.2
    if sluchain3v2 == 2:
        hide tamarakarta2
        show tamarakarta1:
            xalign 0.85
            yalign 0.2
    if sluchain3 == 3:
        hide alenakarta2
        show alenakarta1:
            xalign 0.1
            yalign 0.6
    if sluchain3v2 == 3:
        hide gopnikkarta2
        show gopnikkarta1:
            xalign 0.65
            yalign 0.6
    if sluchain3 == 4:
        hide ggkarta2
        show ggkarta1:
            xalign 0.3
            yalign 0.6
    if sluchain3v2 == 4:
        hide starikkarta2
        show starikkarta1:
            xalign 0.85
            yalign 0.6
    pause 2
#################
    hide kristinakarta1
    hide fionakarta1
    hide alenakarta1
    hide ggkarta1
    hide viacheslavkarta1
    hide tamarakarta1
    hide gopnikkarta1
    hide starikkarta1


    label choise0n4:
    hide screen kristina_karta1n4
    hide screen fiona_karta1n4
    hide screen alena_karta1n4
    hide screen gg_karta1n4
    if game1vibor==3:
        window show
        "Вы заработали максимальную атаку."
        menu:
            "Перейти к защите":
                jump armor_four
    screen kristina_karta1n4:
        imagebutton xalign 0.1 yalign 0.2:
            idle ("karta2.png")
            hover ("karta3.png")
            action Jump("choise1n4")
    show screen kristina_karta1n4
    screen fiona_karta1n4:
        imagebutton xalign 0.3 yalign 0.2:
            idle ("karta2.png")
            hover ("karta3.png")
            action Jump("choise2n4")
    show screen fiona_karta1n4
    screen alena_karta1n4:
        imagebutton xalign 0.1 yalign 0.6:
            idle ("karta2.png")
            hover ("karta3.png")
            action Jump("choise3n4")
    show screen alena_karta1n4
    screen gg_karta1n4:
        imagebutton xalign 0.3 yalign 0.6:
            idle ("karta2.png")
            hover ("karta3.png")
            action Jump("choise4n4")
    show screen gg_karta1n4
    call screen restartn4

label armor_four:
    hide screen viacheslav_karta1n4
    hide screen tamara_karta1n4
    hide screen gopnik_karta1n4
    hide screen starik_karta1n4
    window hide
    if game1vibor2==3:
        window show
        "Вы заработали максимальную защиту."
        menu:
            "Начать битву":
                jump fight_four
    screen viacheslav_karta1n4:
        imagebutton xalign 0.65 yalign 0.2:
            idle ("karta4.png")
            hover ("karta5.png")
            action Jump("choise5n4")
    show screen viacheslav_karta1n4
    screen tamara_karta1n4:
        imagebutton xalign 0.85 yalign 0.2:
            idle ("karta4.png")
            hover ("karta5.png")
            action Jump("choise6n4")
    show screen tamara_karta1n4
    screen gopnik_karta1n4:
        imagebutton xalign 0.65 yalign 0.6:
            idle ("karta4.png")
            hover ("karta5.png")
            action Jump("choise7n4")
    show screen gopnik_karta1n4
    screen starik_karta1n4:
        imagebutton xalign 0.85 yalign 0.6:
            idle ("karta4.png")
            hover ("karta5.png")
            action Jump("choise8n4")
    show screen starik_karta1n4
    call screen restartn4

label choise5n4:
hide screen restartn4
$game1vibor2+=1
hide screen starik_karta1n4
hide screen gopnik_karta1n4
hide screen tamara_karta1n4
hide screen viacheslav_karta1n4
show starikkarta1:
    xalign 0.85
    yalign 0.2
show gopnikkarta1:
    xalign 0.65
    yalign 0.6
show tamarakarta1:
    xalign 0.85
    yalign 0.6
show viacheslavkarta2:
    xalign 0.65
    yalign 0.2
if game1vibor2==1:
    if sluchain1v2 == 1:
        $armor+=1;
        show shield1:
            xalign 0.6
            yalign 0.04
        pause 2
        hide viacheslavkarta2
        jump armor_four
    else:
        hide starikkarta1
        hide gopnikkarta1
        hide tamarakarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Начать битву":
                jump fight_four
else:
    if game1vibor2==2:
        if sluchain2v2 == 1:
            $armor+=1;
            show shield2:
                xalign 0.65
                yalign 0.04
            pause 2
            hide viacheslavkarta2
            jump armor_four
        else:
            hide starikkarta1
            hide gopnikkarta1
            hide tamarakarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Начать битву":
                    jump fight_four
    else:
        if game1vibor2==3:
            if sluchain3v2 == 1:
                $armor+=1;
                show shield3:
                    xalign 0.7
                    yalign 0.04
                pause 2
                hide viacheslavkarta2
                jump armor_four
            else:
                hide starikkarta1
                hide gopnikkarta1
                hide tamarakarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Начать битву":
                        jump fight_four
label choise6n4:
hide screen restartn4
$game1vibor2+=1
hide screen starik_karta1n4
hide screen gopnik_karta1n4
hide screen tamara_karta1n4
hide screen viacheslav_karta1n4
show starikkarta1:
    xalign 0.85
    yalign 0.2
show gopnikkarta1:
    xalign 0.65
    yalign 0.6
show viacheslavkarta1:
    xalign 0.65
    yalign 0.2
show tamarakarta2:
    xalign 0.85
    yalign 0.2
if game1vibor2==1:
    if sluchain1v2 == 2:
        $armor+=1;
        show shield1:
            xalign 0.6
            yalign 0.04
        pause 2
        hide tamarakarta2
        jump armor_four
    else:
        hide starikkarta1
        hide gopnikkarta1
        hide viacheslavkarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Начать битву":
                jump fight_four
else:
    if game1vibor2==2:
        if sluchain2v2 == 2:
            $armor+=1;
            show shield2:
                xalign 0.65
                yalign 0.04
            pause 2
            hide tamarakarta2
            jump armor_four
        else:
            hide starikkarta1
            hide gopnikkarta1
            hide viacheslavkarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Начать битву":
                    jump fight_four
    else:
        if game1vibor2==3:
            if sluchain3v2 == 2:
                $armor+=1;
                show shield3:
                    xalign 0.7
                    yalign 0.04
                pause 2
                hide tamarakarta2
                jump armor_four
            else:
                hide starikkarta1
                hide gopnikkarta1
                hide viacheslavkarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Начать битву":
                        jump fight_four
label choise7n4:
hide screen restartn4
$game1vibor2+=1
hide screen starik_karta1n4
hide screen gopnik_karta1n4
hide screen tamara_karta1n4
hide screen viacheslav_karta1n4
show starikkarta1:
    xalign 0.85
    yalign 0.2
show viacheslavkarta1:
    xalign 0.65
    yalign 0.2
show tamarakarta1:
    xalign 0.85
    yalign 0.2
show gopnikkarta2:
    xalign 0.65
    yalign 0.6
if game1vibor2==1:
    if sluchain1v2 == 3:
        $armor+=1;
        show shield1:
            xalign 0.6
            yalign 0.04
        pause 2
        hide gopnikkarta2
        jump armor_four
    else:
        hide starikkarta1
        hide tamarakarta1
        hide viacheslavkarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Начать битву":
                jump fight_four
else:
    if game1vibor2==2:
        if sluchain2v2 == 3:
            $armor+=1;
            show shield2:
                xalign 0.65
                yalign 0.04
            pause 2
            hide gopnikkarta2
            jump armor_four
        else:
            hide starikkarta1
            hide tamarakarta1
            hide viacheslavkarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Начать битву":
                    jump fight_four
    else:
        if game1vibor2==3:
            if sluchain3v2 == 3:
                $armor+=1;
                show shield3:
                    xalign 0.7
                    yalign 0.04
                pause 2
                hide gopnikkarta2
                jump armor_four
            else:
                hide starikkarta1
                hide tamarakarta1
                hide viacheslavkarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Начать битву":
                        jump fight_four
label choise8n4:
hide screen restartn4
$game1vibor2+=1
hide screen starik_karta1n4
hide screen gopnik_karta1n4
hide screen tamara_karta1n4
hide screen viacheslav_karta1n4
show starikkarta2:
    xalign 0.85
    yalign 0.6
show viacheslavkarta1:
    xalign 0.65
    yalign 0.2
show tamarakarta1:
    xalign 0.85
    yalign 0.2
show gopnikkarta1:
    xalign 0.65
    yalign 0.6
if game1vibor2==1:
    if sluchain1v2 == 4:
        $armor+=1;
        show shield1:
            xalign 0.6
            yalign 0.04
        pause 2
        hide starikkarta2
        jump armor_four
    else:
        hide gopnikkarta1
        hide tamarakarta1
        hide viacheslavkarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Начать битву":
                jump fight_four
else:
    if game1vibor2==2:
        if sluchain2v2 == 4:
            $armor+=1;
            show shield2:
                xalign 0.65
                yalign 0.04
            pause 2
            hide starikkarta2
            jump armor_four
        else:
            hide gopnikkarta1
            hide tamarakarta1
            hide viacheslavkarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Начать битву":
                    jump fight_four
    else:
        if game1vibor2==3:
            if sluchain3v2 == 4:
                $armor+=1;
                show shield3:
                    xalign 0.7
                    yalign 0.04
                pause 2
                hide starikkarta2
                jump armor_four
            else:
                hide gopnikkarta1
                hide tamarakarta1
                hide viacheslavkarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Начать битву":
                        jump fight_four
label fight_four:
    hide screen viacheslav_karta1n4
    hide screen tamara_karta1n4
    hide screen gopnik_karta1n4
    hide screen starik_karta1n4
    if attack>2 and armor>2:
        scene win
        "Атаки и защиты хватило чтобы победить!"
        jump six
    else:
        scene lose
        if attack<3 and armor<3:
            "Наша защита была разгромлена, наши атаки не достигли противника."
        else:
            if attack<3:
                "Наши атаки не достигли противника."
            if armor<3:
                "Наша защита была разгромлена."
        menu:
            "Начать заново":
                jump previugame4
label six:
d"{cps=25}Отлично."
ficon"{cps=25}Спасибо тебе."
kicon"{cps=25}Да, мы как - нибудь тебя отблагодарим."
d"{cps=25}Наверное вам пора."
"{cps=25}Они молча кивнули и ушли."
"{cps=25}И мне тоже пора."
scene black
"{alpha=.5}{cps=25}- Денис поступил так, как и должен был поступить настоящий киберспортсмен."
play music "war.mp3"
"{cps=25}Я нёс её на себе."
"{cps=25}'Оставь меня лейтенант' говорит она, однако я продолжаю идти."
"{cps=25}Ещё пару метров."
show tamara6
t"{cps=25}Лейтенант! Ты угробил ещё одну девушку."
a"{cps=25}Нет."
t"{cps=25}Я даю тебе последний шанс."
a"{cps=25}Я вас не подведу!"
hide tamara6
"{alpha=.5}{cps=25}С криками, я побежал в атаку."
a"{cps=25}Урааааа!"
stop music fadeout 1
scene top with fade
a"{cps=25}Аааааа!"
"{cps=25}Что?"
"{cps=25}Я очнулся в палате, в холодном поту."
a"{cps=25}Просто сон."
ficon"{cps=25}Что тебе снилось?"
menu:
    "Высадка в Нормандии":
        jump seven
    "Битва за Москву":
        jump seven
label seven:
scene hospital
play music "Cafe.mp3"
show alyona2
show kristina2 at right
show fiona2 at left
l"{cps=25}Бред."
hide kristina2
show kristina3 at right
k"{cps=25}А мне бы хотелось увидеть такой сон."
a"{cps=25}Не думаю."
"{alpha=.5}{cps=25}Тут я вспомнил, что произошло до этого."
a"{cps=25}Что случилось после того, как меня вырубило?"
hide kristina3
show kristina1 at right
k"{cps=25}Тебя унесли в больницу, а мы остались играть полуфинал."
f"{cps=25}Тебя заменил один парень, Денис."
a"{cps=25}Денис? Он же сам должен был играть полуфинал?"
f"{cps=25}Он сказал, что наша победа важнее."
"{alpha=.5}{cps=25}Я даже не подозревал, что Денис настолько хороший человек. Я перед ним в огромном долгу."
"{alpha=.5}{cps=25}В это время к нам зашёл врач. По его словам у меня случился приступ эпилепсии."
"{alpha=.5}{cps=25}Но он сказал, что в большинстве случаев после припадка наступает ремиссия, то есть приступы отсутствуют в течении 4-5 лет."
"{cps=25}Я успокоился."
hide fiona2
show fiona14 at left
f"{cps=25}То есть он сможет пойти на финал."
l"{cps=25}Только если не будет забывать о лечении."
a"{cps=25}А вы победили?"
k"{cps=25}Да, хоть и с трудом."
a"{cps=25}Тогда завтра мы сможем сразиться."
f"{cps=25}Да!!"
"{cps=25}Я рад. Ведь столько труда было вложено. Проиграть из-за меня было бы ужасно."
l"{cps=25}Думаю всем пора, завтра встретимся."
"{alpha=.5}{cps=25}Девчонки попрощались и вышли."
"{alpha=.5}{cps=25}Я тоже долго не сидел и пошёл домой."
stop music fadeout 1
scene schooltrip with fade
scene laptop1 with fade
"{alpha=.5}{cps=25}Лучше пораньше лечь спать."
scene laptop2 with fade
"{alpha=.5}{cps=25}Я проснулся в бодром настроении."
a"{cps=25}Отличный день для победы."
scene street3 with fade
show kristina9
show fiona2 at left
show alyona3 at right
k"{cps=25}Пошлите!"
a"{cps=25}Да."
scene budka
play music "trevoga.mp3"
"{alpha=.5}{cps=25}Мы сидели и молчали. {w=1.0}Каждому было тяжело от волнения. {w=1.0}Главное перетерпеть этот момент."
scene black
scene budka
"{alpha=.5}{cps=25}Прошла минута."
scene black
pause 1
scene budka
"{alpha=.5}{cps=25}Две."
scene black
pause 1
scene budka
"{alpha=.5}{cps=25}Три."
"{alpha=.5}{cps=25}А мы всё сидели и смотрели в пол."
scene black
pause 1
scene budka
"{cps=25}Четыре."
"{alpha=.5}{cps=25}Дверь открылась, и нас позвали на сцену."
a"{cps=25}Пора."
f"{cps=25}Иди впереди, как капитан."
a"{cps=25}Если все согласны."
"{alpha=.5}{cps=25}Мы выстроились в ряд и пошли вперёд."
stop music fadeout 1
scene tournament
"{alpha=.5}{cps=25}Все кричали Вперёд (ввести название команды)! Вперёд (ввести название команды)!,давали нам пять."
"{alpha=.5}{cps=25}Мнение зрителя самое главное. {w=1.0}Многие команды без поддержки проигрывают турниры, наоборот, у команд любимых всеми есть стимул побеждать."
"{alpha=.5}{cps=25}Мы это почувствовали проходя мимо них."
scene black
"{alpha=.5}{cps=25}Дальше я увидел кубок. Он был красив."
"{alpha=.5}{cps=25}Не то что бы я никогда не видел кубков, но этот мог быть заслужен нами."
"{alpha=.5}{cps=25}Я уже был счастлив."
"{alpha=.5}{cps=25}В моменты, когда выходишь представлять свою команду, ты получаешь награду."
"{alpha=.5}{cps=25}Столько удовольствия и гордости, сколько нигде не получишь."
"{alpha=.5}{cps=25}Нас проводили в кабинки."
"{alpha=.5}{cps=25}Они были звукоизолирующими , но я понимал,что кричат в зале."
a"{cps=25}Погнали!"









jump previugame5


label choise1n5:
hide screen restartn5
$game1vibor+=1
hide screen kristina_karta1n5
hide screen fiona_karta1n5
hide screen alena_karta1n5
hide screen gg_karta1n5
show ggkarta1:
    xalign 0.3
    yalign 0.6
show alenakarta1:
    xalign 0.1
    yalign 0.6
show fionakarta1:
    xalign 0.3
    yalign 0.2
show kristinakarta2:
    xalign 0.1
    yalign 0.2
if game1vibor==1:
    if sluchain1 == 1:
        $attack+=1;
        show sword1:
            xalign 0.1
            yalign 0.04
        pause 2
        hide kristinakarta2
        jump choise0n5
    else:
        hide fionakarta1
        hide alenakarta1
        hide ggkarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Перейти к защите":
                jump armor_five
else:
    if game1vibor==2:
        if sluchain2 == 1:
            $attack+=1;
            show sword2:
                xalign 0.15
                yalign 0.04
            pause 2
            hide kristinakarta2
            jump choise0n5
        else:
            hide fionakarta1
            hide alenakarta1
            hide ggkarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Перейти к защите":
                    jump armor_five
    else:
        if game1vibor==3:
            if sluchain3 == 1:
                $attack+=1;
                show sword3:
                    xalign 0.2
                    yalign 0.04
                pause 2
                hide kristinakarta2
                jump choise0n5
            else:
                hide fionakarta1
                hide alenakarta1
                hide ggkarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Перейти к защите":
                        jump armor_five
        else:
            if game1vibor==4:
                if sluchain4 == 1:
                    $attack+=1;
                    show sword4:
                        xalign 0.25
                        yalign 0.04
                    pause 2
                    hide kristinakarta2
                    jump choise0n5
                else:
                    hide fionakarta1
                    hide alenakarta1
                    hide ggkarta1
                    window show
                    "Увы вы ошиблись."
                    menu:
                        "Перейти к защите":
                            jump armor_five

label choise2n5:
hide screen restartn5
$game1vibor+=1
hide screen kristina_karta1n5
hide screen fiona_karta1n5
hide screen alena_karta1n5
hide screen gg_karta1n5
show ggkarta1:
    xalign 0.3
    yalign 0.6
show alenakarta1:
    xalign 0.1
    yalign 0.6
show fionakarta2:
    xalign 0.3
    yalign 0.2
show kristinakarta1:
    xalign 0.1
    yalign 0.2
if game1vibor==1:
    if sluchain1 == 2:
        $attack+=1;
        show sword1:
            xalign 0.1
            yalign 0.04
        pause 2
        hide fionakarta2
        jump choise0n5
    else:
        hide kristinakarta1
        hide alenakarta1
        hide ggkarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Перейти к защите":
                jump armor_five
else:
    if game1vibor==2:
        if sluchain2 == 2:
            $attack+=1;
            show sword2:
                xalign 0.15
                yalign 0.04
            pause 2
            hide fionakarta2
            jump choise0n5
        else:
            hide kristinakarta1
            hide alenakarta1
            hide ggkarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Перейти к защите":
                    jump armor_five
    else:
        if game1vibor==3:
            if sluchain3 == 2:
                $attack+=1;
                show sword3:
                    xalign 0.2
                    yalign 0.04
                pause 2
                hide fionakarta2
                jump choise0n5
            else:
                hide kristinakarta1
                hide alenakarta1
                hide ggkarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Перейти к защите":
                        jump armor_five
        else:
            if game1vibor==4:
                if sluchain4 == 2:
                    $attack+=1;
                    show sword4:
                        xalign 0.25
                        yalign 0.04
                    pause 2
                    hide kristinakarta2
                    jump choise0n5
                else:
                    hide fionakarta1
                    hide alenakarta1
                    hide ggkarta1
                    window show
                    "Увы вы ошиблись."
                    menu:
                        "Перейти к защите":
                            jump armor_five

label choise3n5:
hide screen restartn5
$game1vibor+=1
hide screen kristina_karta1n5
hide screen fiona_karta1n5
hide screen alena_karta1n5
hide screen gg_karta1n5
show ggkarta1:
    xalign 0.3
    yalign 0.6
show alenakarta2:
    xalign 0.1
    yalign 0.6
show fionakarta1:
    xalign 0.3
    yalign 0.2
show kristinakarta1:
    xalign 0.1
    yalign 0.2
if game1vibor==1:
    if sluchain1 == 3:
        $attack+=1;
        show sword1:
            xalign 0.1
            yalign 0.04
        pause 2
        hide alenakarta2
        jump choise0n5
    else:
        hide kristinakarta1
        hide fionakarta1
        hide ggkarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Перейти к защите":
                jump armor_five
else:
    if game1vibor==2:
        if sluchain2 == 3:
            $attack+=1;
            show sword2:
                xalign 0.15
                yalign 0.04
            pause 2
            hide alenakarta2
            jump choise0n5
        else:
            hide kristinakarta1
            hide fionakarta1
            hide ggkarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Перейти к защите":
                    jump armor_five
    else:
        if game1vibor==3:
            if sluchain3 == 3:
                $attack+=1;
                show sword3:
                    xalign 0.2
                    yalign 0.04
                pause 2
                hide alenakarta2
                jump choise0n5
            else:
                hide kristinakarta1
                hide fionakarta1
                hide ggkarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Перейти к защите":
                        jump armor_five
        else:
            if game1vibor==4:
                if sluchain4 == 3:
                    $attack+=1;
                    show sword4:
                        xalign 0.25
                        yalign 0.04
                    pause 2
                    hide kristinakarta2
                    jump choise0n5
                else:
                    hide fionakarta1
                    hide alenakarta1
                    hide ggkarta1
                    window show
                    "Увы вы ошиблись."
                    menu:
                        "Перейти к защите":
                            jump armor_five
label choise4n5:
hide screen restartn5
$game1vibor+=1
hide screen kristina_karta1n5
hide screen fiona_karta1n5
hide screen alena_karta1n5
hide screen gg_karta1n5
show ggkarta2:
    xalign 0.3
    yalign 0.6
show alenakarta1:
    xalign 0.1
    yalign 0.6
show fionakarta1:
    xalign 0.3
    yalign 0.2
show kristinakarta1:
    xalign 0.1
    yalign 0.2
if game1vibor==1:
    if sluchain1 == 4:
        $attack+=1;
        show sword1:
            xalign 0.1
            yalign 0.04
        pause 2
        hide ggkarta2
        jump choise0n5
    else:
        hide kristinakarta1
        hide fionakarta1
        hide alenakarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Перейти к защите":
                jump armor_five
else:
    if game1vibor==2:
        if sluchain2 == 4:
            $attack+=1;
            show sword2:
                xalign 0.15
                yalign 0.04
            pause 2
            hide ggkarta2
            jump choise0n5
        else:
            hide kristinakarta1
            hide fionakarta1
            hide alenakarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Перейти к защите":
                    jump armor_five
    else:
        if game1vibor==3:
            if sluchain3 == 4:
                $attack+=1;
                show sword3:
                    xalign 0.2
                    yalign 0.04
                pause 2
                hide alenakarta2
                jump choise0n5
            else:
                hide kristinakarta1
                hide fionakarta1
                hide ggkarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Перейти к защите":
                        jump armor_five
        else:
            if game1vibor==4:
                if sluchain4 == 4:
                    $attack+=1;
                    show sword4:
                        xalign 0.25
                        yalign 0.04
                    pause 2
                    hide kristinakarta2
                    jump choise0n5
                else:
                    hide fionakarta1
                    hide alenakarta1
                    hide ggkarta1
                    window show
                    "Увы вы ошиблись."
                    menu:
                        "Перейти к защите":
                            jump armor_five

label previugame5:
    menu:
        "Прочитать правила":
            jump pravila5
        "Начать игру":
            jump game5
    label pravila5:
    scene pravila5
    "Приветсвую в мини-игре!"
    "Для победы над противником вам нужно набрать достаточное количество атаки и защиты."
    "Очки атаки вы зарабатываете,поочерёдно угадывая синие карты, которые открылись после начала игры."
    "Очки защиты вы зарабатываете,поочерёдно угадывая красные карты, которые открылись после начала игры."
    menu:
        "Начать игру":
            jump game5
    label game5:
    "У противника сильная защита и сильная атака."
    hide screen kristina_karta1n5
    hide screen fiona_karta1n5
    hide screen alena_karta1n5
    hide screen gg_karta1n5
    hide screen viacheslav_karta1n5
    hide screen tamara_karta1n5
    hide screen gopnik_karta1n5
    hide screen starik_karta1n5
    window hide
    scene background4
    $armor = 0
    $attack = 0
    $game1vibor2=0
    $game1vibor=0
    $sluchain1 = 0
    $sluchain2 = 0
    $sluchain3 = 0
    $sluchain4 = 0
    screen restartn5:
        imagebutton xalign 0.5 yalign 0.2:
            idle ("restart.png")
            action Jump("previugame5")
    show kristinakarta1:
        xalign 0.1
        yalign 0.2
    show fionakarta1:
        xalign 0.3
        yalign 0.2
    show alenakarta1:
        xalign 0.1
        yalign 0.6
    show ggkarta1:
        xalign 0.3
        yalign 0.6
    show viacheslavkarta1:
        xalign 0.65
        yalign 0.2
    show tamarakarta1:
        xalign 0.85
        yalign 0.2
    show gopnikkarta1:
        xalign 0.65
        yalign 0.6
    show starikkarta1:
        xalign 0.85
        yalign 0.6
    $sluchain1 = renpy.random.randint(1,4)
    $sluchain1v2 = renpy.random.randint(1,4)
####Разворот первых двух карт
    pause 2
    if sluchain1 == 1:#Первая синяя карта
        hide kristinakarta1
        show kristinakarta2:
            xalign 0.1
            yalign 0.2
    if sluchain1v2 == 1:#Первая красная карта
        hide viacheslavkarta1
        show viacheslavkarta2:
            xalign 0.65
            yalign 0.2
    if sluchain1 == 2:
        hide fionakarta1
        show fionakarta2:
            xalign 0.3
            yalign 0.2
    if sluchain1v2 == 2:
        hide tamarakarta1
        show tamarakarta2:
            xalign 0.85
            yalign 0.2
    if sluchain1 == 3:
        hide alenakarta1
        show alenakarta2:
            xalign 0.1
            yalign 0.6
    if sluchain1v2 == 3:
        hide gopnikkarta1
        show gopnikkarta2:
            xalign 0.65
            yalign 0.6
    if sluchain1 == 4:
        hide ggkarta1
        show ggkarta2:
            xalign 0.3
            yalign 0.6
    if sluchain1v2 == 4:
        hide starikkarta1
        show starikkarta2:
            xalign 0.85
            yalign 0.6
#####Разворот обратно этих же карт
    pause 2
    if sluchain1 == 1:
        hide kristinakarta2
        show kristinakarta1:
            xalign 0.1
            yalign 0.2
    if sluchain1v2 == 1:
        hide viacheslavkarta2
        show viacheslavkarta1:
            xalign 0.65
            yalign 0.2
    if sluchain1 == 2:
        hide fionakarta2
        show fionakarta1:
            xalign 0.3
            yalign 0.2
    if sluchain1v2 == 2:
        hide tamarakarta2
        show tamarakarta1:
            xalign 0.85
            yalign 0.2
    if sluchain1 == 3:
        hide alenakarta2
        show alenakarta1:
            xalign 0.1
            yalign 0.6
    if sluchain1v2 == 3:
        hide gopnikkarta2
        show gopnikkarta1:
            xalign 0.65
            yalign 0.6
    if sluchain1 == 4:
        hide ggkarta2
        show ggkarta1:
            xalign 0.3
            yalign 0.6
    if sluchain1v2 == 4:
        hide starikkarta2
        show starikkarta1:
            xalign 0.85
            yalign 0.6

    pause 2
#######Razvorot sleduyushih dvuh kart

    $sluchain2 = renpy.random.randint(1,4)
    $sluchain2v2 = renpy.random.randint(1,4)
    if sluchain2 == 1:#Первая синяя карта
        hide kristinakarta1
        show kristinakarta2:
            xalign 0.1
            yalign 0.2
    if sluchain2v2 == 1:#Первая красная карта
        hide viacheslavkarta1
        show viacheslavkarta2:
            xalign 0.65
            yalign 0.2
    if sluchain2 == 2:
        hide fionakarta1
        show fionakarta2:
            xalign 0.3
            yalign 0.2
    if sluchain2v2 == 2:
        hide tamarakarta1
        show tamarakarta2:
            xalign 0.85
            yalign 0.2
    if sluchain2 == 3:
        hide alenakarta1
        show alenakarta2:
            xalign 0.1
            yalign 0.6
    if sluchain2v2 == 3:
        hide gopnikkarta1
        show gopnikkarta2:
            xalign 0.65
            yalign 0.6
    if sluchain2 == 4:
        hide ggkarta1
        show ggkarta2:
            xalign 0.3
            yalign 0.6
    if sluchain2v2 == 4:
        hide starikkarta1
        show starikkarta2:
            xalign 0.85
            yalign 0.6
#####Разворот обратно этих же карт
    pause 2
    if sluchain2 == 1:
        hide kristinakarta2
        show kristinakarta1:
            xalign 0.1
            yalign 0.2
    if sluchain2v2 == 1:
        hide viacheslavkarta2
        show viacheslavkarta1:
            xalign 0.65
            yalign 0.2
    if sluchain2 == 2:
        hide fionakarta2
        show fionakarta1:
            xalign 0.3
            yalign 0.2
    if sluchain2v2 == 2:
        hide tamarakarta2
        show tamarakarta1:
            xalign 0.85
            yalign 0.2
    if sluchain2 == 3:
        hide alenakarta2
        show alenakarta1:
            xalign 0.1
            yalign 0.6
    if sluchain2v2 == 3:
        hide gopnikkarta2
        show gopnikkarta1:
            xalign 0.65
            yalign 0.6
    if sluchain2 == 4:
        hide ggkarta2
        show ggkarta1:
            xalign 0.3
            yalign 0.6
    if sluchain2v2 == 4:
        hide starikkarta2
        show starikkarta1:
            xalign 0.85
            yalign 0.6

    pause 2
################################
    $sluchain3 = renpy.random.randint(1,4)
    $sluchain3v2 = renpy.random.randint(1,4)
    if sluchain3 == 1:
        hide kristinakarta1
        show kristinakarta2:
            xalign 0.1
            yalign 0.2
    if sluchain3v2 == 1:
        hide viacheslavkarta1
        show viacheslavkarta2:
            xalign 0.65
            yalign 0.2
    if sluchain3 == 2:
        hide fionakarta1
        show fionakarta2:
            xalign 0.3
            yalign 0.2
    if sluchain3v2 == 2:
        hide tamarakarta1
        show tamarakarta2:
            xalign 0.85
            yalign 0.2
    if sluchain3 == 3:
        hide alenakarta1
        show alenakarta2:
            xalign 0.1
            yalign 0.6
    if sluchain3v2 == 3:
        hide gopnikkarta1
        show gopnikkarta2:
            xalign 0.65
            yalign 0.6
    if sluchain3 == 4:
        hide ggkarta1
        show ggkarta2:
            xalign 0.3
            yalign 0.6
    if sluchain3v2 == 4:
        hide starikkarta1
        show starikkarta2:
            xalign 0.85
            yalign 0.6
    pause 2
########################
    if sluchain3 == 1:
        hide kristinakarta2
        show kristinakarta1:
            xalign 0.1
            yalign 0.2
    if sluchain3v2 == 1:
        hide viacheslavkarta2
        show viacheslavkarta1:
            xalign 0.65
            yalign 0.2
    if sluchain3 == 2:
        hide fionakarta2
        show fionakarta1:
            xalign 0.3
            yalign 0.2
    if sluchain3v2 == 2:
        hide tamarakarta2
        show tamarakarta1:
            xalign 0.85
            yalign 0.2
    if sluchain3 == 3:
        hide alenakarta2
        show alenakarta1:
            xalign 0.1
            yalign 0.6
    if sluchain3v2 == 3:
        hide gopnikkarta2
        show gopnikkarta1:
            xalign 0.65
            yalign 0.6
    if sluchain3 == 4:
        hide ggkarta2
        show ggkarta1:
            xalign 0.3
            yalign 0.6
    if sluchain3v2 == 4:
        hide starikkarta2
        show starikkarta1:
            xalign 0.85
            yalign 0.6
    pause 2
####Разворот последний двух карт
    $sluchain4 = renpy.random.randint(1,4)
    $sluchain4v2 = renpy.random.randint(1,4)
    if sluchain4 == 1:#Первая синяя карта
        hide kristinakarta1
        show kristinakarta2:
            xalign 0.1
            yalign 0.2
    if sluchain4v2 == 1:#Первая красная карта
        hide viacheslavkarta1
        show viacheslavkarta2:
            xalign 0.65
            yalign 0.2
    if sluchain4 == 2:
        hide fionakarta1
        show fionakarta2:
            xalign 0.3
            yalign 0.2
    if sluchain4v2 == 2:
        hide tamarakarta1
        show tamarakarta2:
            xalign 0.85
            yalign 0.2
    if sluchain4 == 3:
        hide alenakarta1
        show alenakarta2:
            xalign 0.1
            yalign 0.6
    if sluchain4v2 == 3:
        hide gopnikkarta1
        show gopnikkarta2:
            xalign 0.65
            yalign 0.6
    if sluchain4 == 4:
        hide ggkarta1
        show ggkarta2:
            xalign 0.3
            yalign 0.6
    if sluchain4v2 == 4:
        hide starikkarta1
        show starikkarta2:
            xalign 0.85
            yalign 0.6
#####Разворот обратно этих же карт
    pause 2
    if sluchain4 == 1:
        hide kristinakarta2
        show kristinakarta1:
            xalign 0.1
            yalign 0.2
    if sluchain4v2 == 1:
        hide viacheslavkarta2
        show viacheslavkarta1:
            xalign 0.65
            yalign 0.2
    if sluchain4 == 2:
        hide fionakarta2
        show fionakarta1:
            xalign 0.3
            yalign 0.2
    if sluchain4v2 == 2:
        hide tamarakarta2
        show tamarakarta1:
            xalign 0.85
            yalign 0.2
    if sluchain4 == 3:
        hide alenakarta2
        show alenakarta1:
            xalign 0.1
            yalign 0.6
    if sluchain4v2 == 3:
        hide gopnikkarta2
        show gopnikkarta1:
            xalign 0.65
            yalign 0.6
    if sluchain4 == 4:
        hide ggkarta2
        show ggkarta1:
            xalign 0.3
            yalign 0.6
    if sluchain4v2 == 4:
        hide starikkarta2
        show starikkarta1:
            xalign 0.85
            yalign 0.6

    pause 2
################# Последний разворот

    hide kristinakarta1
    hide fionakarta1
    hide alenakarta1
    hide ggkarta1
    hide viacheslavkarta1
    hide tamarakarta1
    hide gopnikkarta1
    hide starikkarta1


    label choise0n5:
    hide screen kristina_karta1n5
    hide screen fiona_karta1n5
    hide screen alena_karta1n5
    hide screen gg_karta1n5
    if game1vibor==4:
        window show
        "Вы заработали максимальную атаку."
        menu:
            "Перейти к защите":
                jump armor_five
    screen kristina_karta1n5:
        imagebutton xalign 0.1 yalign 0.2:
            idle ("karta2.png")
            hover ("karta3.png")
            action Jump("choise1n5")
    show screen kristina_karta1n5
    screen fiona_karta1n5:
        imagebutton xalign 0.3 yalign 0.2:
            idle ("karta2.png")
            hover ("karta3.png")
            action Jump("choise2n5")
    show screen fiona_karta1n5
    screen alena_karta1n5:
        imagebutton xalign 0.1 yalign 0.6:
            idle ("karta2.png")
            hover ("karta3.png")
            action Jump("choise3n5")
    show screen alena_karta1n5
    screen gg_karta1n5:
        imagebutton xalign 0.3 yalign 0.6:
            idle ("karta2.png")
            hover ("karta3.png")
            action Jump("choise4n5")
    show screen gg_karta1n5
    call screen restartn5

label armor_five:
    hide screen viacheslav_karta1n5
    hide screen tamara_karta1n5
    hide screen gopnik_karta1n5
    hide screen starik_karta1n45
    window hide
    if game1vibor2==4:
        window show
        "Вы заработали максимальную защиту."
        menu:
            "Начать битву":
                jump fight_five
    screen viacheslav_karta1n5:
        imagebutton xalign 0.65 yalign 0.2:
            idle ("karta4.png")
            hover ("karta5.png")
            action Jump("choise5n5")
    show screen viacheslav_karta1n5
    screen tamara_karta1n5:
        imagebutton xalign 0.85 yalign 0.2:
            idle ("karta4.png")
            hover ("karta5.png")
            action Jump("choise6n5")
    show screen tamara_karta1n5
    screen gopnik_karta1n5:
        imagebutton xalign 0.65 yalign 0.6:
            idle ("karta4.png")
            hover ("karta5.png")
            action Jump("choise7n5")
    show screen gopnik_karta1n5
    screen starik_karta1n5:
        imagebutton xalign 0.85 yalign 0.6:
            idle ("karta4.png")
            hover ("karta5.png")
            action Jump("choise8n5")
    show screen starik_karta1n5
    call screen restartn5

label choise5n5:
hide screen restartn5
$game1vibor2+=1
hide screen starik_karta1n5
hide screen gopnik_karta1n5
hide screen tamara_karta1n5
hide screen viacheslav_karta1n5
show starikkarta1:
    xalign 0.85
    yalign 0.2
show gopnikkarta1:
    xalign 0.65
    yalign 0.6
show tamarakarta1:
    xalign 0.85
    yalign 0.6
show viacheslavkarta2:
    xalign 0.65
    yalign 0.2
if game1vibor2==1:
    if sluchain1v2 == 1:
        $armor+=1;
        show shield1:
            xalign 0.6
            yalign 0.04
        pause 2
        hide viacheslavkarta2
        jump armor_five
    else:
        hide starikkarta1
        hide gopnikkarta1
        hide tamarakarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Начать битву":
                jump fight_five
else:
    if game1vibor2==2:
        if sluchain2v2 == 1:
            $armor+=1;
            show shield2:
                xalign 0.65
                yalign 0.04
            pause 2
            hide viacheslavkarta2
            jump armor_five
        else:
            hide starikkarta1
            hide gopnikkarta1
            hide tamarakarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Начать битву":
                    jump fight_five
    else:
        if game1vibor2==3:
            if sluchain3v2 == 1:
                $armor+=1;
                show shield3:
                    xalign 0.7
                    yalign 0.04
                pause 2
                hide viacheslavkarta2
                jump armor_five
            else:
                hide starikkarta1
                hide gopnikkarta1
                hide tamarakarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Начать битву":
                        jump fight_five
        else:
            if game1vibor2==4:
                if sluchain3v2 == 1:
                    $armor+=1;
                    show shield4:
                        xalign 0.75
                        yalign 0.04
                    pause 2
                    hide viacheslavkarta2
                    jump armor_five
                else:
                    hide starikkarta1
                    hide gopnikkarta1
                    hide tamarakarta1
                    window show
                    "Увы вы ошиблись."
                    menu:
                        "Начать битву":
                            jump fight_five

label choise6n5:
hide screen restartn5
$game1vibor2+=1
hide screen starik_karta1n5
hide screen gopnik_karta1n5
hide screen tamara_karta1n5
hide screen viacheslav_karta1n5
show starikkarta1:
    xalign 0.85
    yalign 0.2
show gopnikkarta1:
    xalign 0.65
    yalign 0.6
show viacheslavkarta1:
    xalign 0.65
    yalign 0.2
show tamarakarta2:
    xalign 0.85
    yalign 0.2
if game1vibor2==1:
    if sluchain1v2 == 2:
        $armor+=1;
        show shield1:
            xalign 0.6
            yalign 0.04
        pause 2
        hide tamarakarta2
        jump armor_five
    else:
        hide starikkarta1
        hide gopnikkarta1
        hide viacheslavkarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Начать битву":
                jump fight_five
else:
    if game1vibor2==2:
        if sluchain2v2 == 2:
            $armor+=1;
            show shield2:
                xalign 0.65
                yalign 0.04
            pause 2
            hide tamarakarta2
            jump armor_five
        else:
            hide starikkarta1
            hide gopnikkarta1
            hide viacheslavkarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Начать битву":
                    jump fight_five
    else:
        if game1vibor2==3:
            if sluchain3v2 == 2:
                $armor+=1;
                show shield3:
                    xalign 0.7
                    yalign 0.04
                pause 2
                hide tamarakarta2
                jump armor_five
            else:
                hide starikkarta1
                hide gopnikkarta1
                hide viacheslavkarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Начать битву":
                        jump fight_five
        else:
            if game1vibor2==4:
                if sluchain3v2 == 2:
                    $armor+=1;
                    show shield4:
                        xalign 0.75
                        yalign 0.04
                    pause 2
                    hide viacheslavkarta2
                    jump armor_five
                else:
                    hide starikkarta1
                    hide gopnikkarta1
                    hide tamarakarta1
                    window show
                    "Увы вы ошиблись."
                    menu:
                        "Начать битву":
                            jump fight_five
label choise7n5:
hide screen restartn5
$game1vibor2+=1
hide screen starik_karta1n5
hide screen gopnik_karta1n5
hide screen tamara_karta1n5
hide screen viacheslav_karta1n5
show starikkarta1:
    xalign 0.85
    yalign 0.2
show viacheslavkarta1:
    xalign 0.65
    yalign 0.2
show tamarakarta1:
    xalign 0.85
    yalign 0.2
show gopnikkarta2:
    xalign 0.65
    yalign 0.6
if game1vibor2==1:
    if sluchain1v2 == 3:
        $armor+=1;
        show shield1:
            xalign 0.6
            yalign 0.04
        pause 2
        hide gopnikkarta2
        jump armor_five
    else:
        hide starikkarta1
        hide tamarakarta1
        hide viacheslavkarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Начать битву":
                jump fight_five
else:
    if game1vibor2==2:
        if sluchain2v2 == 3:
            $armor+=1;
            show shield2:
                xalign 0.65
                yalign 0.04
            pause 2
            hide gopnikkarta2
            jump armor_five
        else:
            hide starikkarta1
            hide tamarakarta1
            hide viacheslavkarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Начать битву":
                    jump fight_five
    else:
        if game1vibor2==3:
            if sluchain3v2 == 3:
                $armor+=1;
                show shield3:
                    xalign 0.7
                    yalign 0.04
                pause 2
                hide gopnikkarta2
                jump armor_five
            else:
                hide starikkarta1
                hide tamarakarta1
                hide viacheslavkarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Начать битву":
                        jump fight_five
        else:
            if game1vibor2==4:
                if sluchain3v2 == 3:
                    $armor+=1;
                    show shield4:
                        xalign 0.75
                        yalign 0.04
                    pause 2
                    hide viacheslavkarta2
                    jump armor_five
                else:
                    hide starikkarta1
                    hide gopnikkarta1
                    hide tamarakarta1
                    window show
                    "Увы вы ошиблись."
                    menu:
                        "Начать битву":
                            jump fight_five
label choise8n5:
hide screen restartn5
$game1vibor2+=1
hide screen starik_karta1n5
hide screen gopnik_karta1n5
hide screen tamara_karta1n5
hide screen viacheslav_karta1n5
show starikkarta2:
    xalign 0.85
    yalign 0.6
show viacheslavkarta1:
    xalign 0.65
    yalign 0.2
show tamarakarta1:
    xalign 0.85
    yalign 0.2
show gopnikkarta1:
    xalign 0.65
    yalign 0.6
if game1vibor2==1:
    if sluchain1v2 == 4:
        $armor+=1;
        show shield1:
            xalign 0.6
            yalign 0.04
        pause 2
        hide starikkarta2
        jump armor_five
    else:
        hide gopnikkarta1
        hide tamarakarta1
        hide viacheslavkarta1
        window show
        "Увы вы ошиблись."
        menu:
            "Начать битву":
                jump fight_five
else:
    if game1vibor2==2:
        if sluchain2v2 == 4:
            $armor+=1;
            show shield2:
                xalign 0.65
                yalign 0.04
            pause 2
            hide starikkarta2
            jump armor_five
        else:
            hide gopnikkarta1
            hide tamarakarta1
            hide viacheslavkarta1
            window show
            "Увы вы ошиблись."
            menu:
                "Начать битву":
                    jump fight_five
    else:
        if game1vibor2==3:
            if sluchain3v2 == 4:
                $armor+=1;
                show shield3:
                    xalign 0.7
                    yalign 0.04
                pause 2
                hide starikkarta2
                jump armor_five
            else:
                hide gopnikkarta1
                hide tamarakarta1
                hide viacheslavkarta1
                window show
                "Увы вы ошиблись."
                menu:
                    "Начать битву":
                        jump fight_five
        else:
            if game1vibor2==4:
                if sluchain3v2 == 4:
                    $armor+=1;
                    show shield4:
                        xalign 0.75
                        yalign 0.04
                    pause 2
                    hide viacheslavkarta2
                    jump armor_five
                else:
                    hide starikkarta1
                    hide gopnikkarta1
                    hide tamarakarta1
                    window show
                    "Увы вы ошиблись."
                    menu:
                        "Начать битву":
                            jump fight_five
label fight_five:
    hide screen viacheslav_karta1n5
    hide screen tamara_karta1n5
    hide screen gopnik_karta1n5
    hide screen starik_karta1n5
    if attack>3 and armor>3:
        scene win
        "Атаки и защиты хватило чтобы победить!"
        jump eight
    else:
        scene lose
        if attack<4 and armor<4:
            "Наша защита была разгромлена, наши атаки не достигли противника."
        else:
            if attack<4:
                "Наши атаки не достигли противника."
            if armor<4:
                "Наша защита была разгромлена."
        menu:
            "Начать заново":
                jump previugame5

label eight:
play music "Good_Times.mp3"
a"{cps=25}Мы сделали это!"
licon"{cps=25}Победа!"
ficon"{cps=25}Да!Да!Да!"
kicon"{cps=25}Ура!"
scene tournament
"{alpha=.5}{cps=25}Я вскочил со стула."
"{cps=25}Кубок наш."
"{alpha=.5}{cps=25}Мы вышли из кабинки, чтобы его забрать."
scene win2 with fade
kom"{cps=25}И победителем турнира становится команда новичков. Аплодисменты (введите название команды)!"
"{alpha=.5}{cps=25}Девочки указали на кубок. Это значило, что я должен был его поднять."
"{alpha=.5}{cps=25}Я так и сделал."
"{alpha=.5}{cps=25}На нём была надпись 'Самой лучшей команде!'"
"{alpha=.5}{cps=25}Я поцеловал эту надпись."
ficon"{cps=25}Дай и нам тоже подержать!"
a"{cps=25}Непременно!"
scene tournament
"{alpha=.5}{cps=25}Я передал им кубок."
"{alpha=.5}{cps=25}После того, как все подержали кубок, мы направились в сторону выхода."
"{alpha=.5}{cps=25}Нас поздравляли все зрители."
scene street3v2
show alyona2 at left
show kristina2
show fiona2 at right
k"{cps=25}Непременно!"
l"{cps=25}Сначала я немного перенервничала, но в игре всё пошло как по маслу."
f"{cps=25}Да, было страшно."
a"{cps=25}Всё позади, ведь мы выиграли."
l"{cps=25}Мы с Кристиной и Фионой договорились, что выигрыш отдадим тебе."
a"{cps=25}Но.."
l"{cps=25}Тебе же не хватает на операцию."
a"{cps=25}Да."
l"{cps=25}Тогда и мы тебе поможем. Ведь наша команда, уже как семья."
a"{cps=25}Спасибо. Спасибо вам всем!"
scene black
stop music fadeout 1
"{alpha=.5}{cps=25}Прошла неделя."
"{alpha=.5}{cps=25}Операция мамы прошла удачно, но пока она лежит в больнице."
"{alpha=.5}{cps=25}Я отдыхаю после турнира."
scene laptop1
"{alpha=.5}{cps=25}И иногда играю."
"{alpha=.5}{cps=25}Наша команда. Мы решили разойтись. Играть профессионально очень трудно, и некоторые хотели заняться чем-то ещё."
a"{cps=25}Сообщение от Дениса."
d"{cps=25}Привет! Ты не хочешь сыграть ещё один турнир? Я тут уломал одного твоего знакомого с нами поехать. Это Вячеслав. Ну так ты как?"
a"{cps=25}Почему бы и нет."
d"{cps=25}Хорошо, тогда нам нужен ещё один человек, у тебя нет предложений."
menu:
    "Фиона!":
        if score1 == 5:
            jump FionaFinalGood
        else:
            a"{cps=25}Наверное Фиона хотела бы продолжить играть!"
            d"{cps=25}Окей, спроси у неё."
            "{alpha=.5}{cps=25}Я тут же написал Фионе, но она отказалась.{w=1.0} Печально."
            "{alpha=.5}{cps=25}Я написал об этом Денису."
            d"{cps=25}Ничего, я уже подобрал другую кандидатуру."
            jump Tamara
    "Кристина!":
        if score2 == 7:
            jump KristinaFinal
        else:
            a"{cps=25}Наверное Кристина хотела бы продолжить играть!"
            d"{cps=25}Окей, спроси у неё."
            "{alpha=.5}{cps=25}Я тут же написал Кристина , но она отказалась.{w=1.0} Печально."
            "{alpha=.5}{cps=25}Я написал об этом Денису."
            d"{cps=25}Ничего, я уже подобрал другую кандидатуру."
            jump Tamara
    "Алёна!":
        if score3 == 5:
            jump AlenaFinalGood
        else:
            a"{cps=25}Наверное Алёна хотела бы продолжить играть!"
            d"{cps=25}Окей, спроси у неё."
            "{alpha=.5}{cps=25}Я тут же написал Алёне , но она отказалась.{w=1.0} Печально."
            "{alpha=.5}{cps=25}Я написал об этом Денису."
            d"{cps=25}Ничего, я уже подобрал другую кандидатуру."
            jump Tamara


label FionaFinalGood:
scene beach
with fade
show fionainbikini
f"{cps=25}Эй, а я и не знала, что тут такие пустые пляжи."
a"{cps=25}Для нас, как игроков, выделена отдельная пляжная зона."
f"{cps=25}Классно! Тогда пошли поплаваем!"
scene black
"{alpha=.5}{cps=25}Мы поплескались в воде, но я быстро замёрз."
scene beach
with Dissolve(2.5)
show fionainbikini with Dissolve(.5)
f"{cps=25}Уже сдулся, слабак."
a"{cps=25}Это от природы у меня."
f"{cps=25}Конечно."
"{alpha=.5}{cps=25}Фиона села рядом со мной."
scene black
f"{cps=25}А почему ты позвал в новую команду меня, а не Кристину или Алёну?"
a"{cps=25}После победы я понял, что я хочу разделять с тобой все положительные эмоции и всегда быть рядом."
f"{cps=25}Оу."
"{alpha=.5}{cps=25}Наступило молчание. Немного погодя она его прервала."
f"{cps=25}Я тоже."
jump titri3
label AlenaFinalGood:
scene beach
with fade
show alenainbikini with Dissolve(.5)
l"{cps=25}Увидел меня в купальнике и сразу потерял дар речи?{w=1.0} Ну я могу тебя понять."
"{alpha=.5}{cps=25}Я бы возразил, но Алёна в купальнике и правда была восхитительна."
a"{cps=25}Может пойдём поплаваем?"
l"{cps=25}Не хочу."
"{alpha=.5}{cps=25}На пляже мы были одни, и я начал чувствовать себя неловко.{w=1.0} В ответ на моё молчание Алёна сделала шаг вперёд."
scene black
l"{cps=25}А почему ты позвал в новую команду меня, а не Фиону или Кристину?"
menu:
    "Глупая шутка":
        a"{cps=25}Я мазохист."
        "{alpha=.5}{cps=25}Предфкушая удар, я закрыл глаза."
        l"{cps=25}Ооо, тогда будешь уничтожен...{w=1.0} моим сокрушительным..."
        scene alenafinal
        l"{cps=25}Поффттелуейм."
        "{alpha=.5}{cps=25}Последнюю часть предложения Алёна сказала мне в рот."
        jump titri2
    "Искренность":
        a"{cps=25}После победы я понял, что я хочу разделять с тобой все положительные эмоции и всегда быть рядом."
        l"{cps=25}Оу."
        "{alpha=.5}{cps=25}Наступило молчание. Немного погодя она его прервала."
        l"{cps=25}Я тоже."
        "{alpha=.5}{cps=25}Она медленно потянулась в мою сторону. Я понял, что нужно сделать то же самое."
        jump titri2
label KristinaFinal:
scene beach
with fade
show kristinakupalnik4 with Dissolve(.5)
k"{cps=25}Мне..идёт?"
menu:
    "Да!":
        jump idet
    "Да!!":
        jump idet
label idet:
hide kristinakupalnik4
show kristinakupalnik3
"{alpha=.5}{cps=25}Кристина перестала смущаться, а вот я нет."
k"{cps=25}Сергей."
a"{cps=25}Что?"
k"{cps=25}Нуу..{w=1.0} Эмм...{w=1.0}..."
"{alpha=.5}{cps=25}Мы были на пляже одни.{w=1.0} Скорее всего Кристина хотела поинтересоваться, почему из всех игроков я позвал в команду именно её."
"{alpha=.5}{cps=25}Я и сам задумывался, почему же я это сделал."
"{alpha=.5}{cps=25}В этот момент что-то потянуло меня в сторону Кристины."
scene kristinafinal
"{alpha=.5}{cps=25}Кристина не сопротивлялась, а, значит, я был прав."
jump titri4

init:#Для титров
    transform txt_up:
        yalign 2
        linear 22.0 yalign -1.5
label Tamara:
stop music fadeout 1
scene beach
with fade
show tamara5 with Dissolve(.5)
t"{cps=25}Как же я давно не была на пляжах."
"{cps=25}Да, то что этим человеком окажется Тамара, я не ожидал."
a"{cps=25}Тамара, а как вы познакомились с Денисом."
t"{cps=25}Во первых, давай перейдём на ты. Мы же всё таки в команде."
t"{cps=25}А во вторых, Денис как то попал в мою больницу, где мы и разговорились."
a"{cps=25}Понятно."
"{alpha=.5}{cps=25}Тамара допила бутылку вина и направилась в мою сторону."
t"{cps=25}Теперь нас ожидает приятное будующее."
jump titri
label titri:
    scene black#{color=#0A0A0A}{/color}
    play music "Good_Times.mp3"
    show text"{b}Концовка - Тамара {p} {p} {p} {p} В создании новеллы участвовали: {p} Данис Батыршин {p} Тимур Галиев {p} {p} {p} {p} Отдельное спасибо:{p} Аюпов Рэм {p} Лобанов Никита {p} {p} {p} Danis Studio 2020{/b}" at txt_up
    pause 20
return
label titri2:
    scene alenafinal#{color=#0A0A0A}{/color}
    play music "Good_Times.mp3"
    show text"{b}{color=#000000}Концовка - Алёна {p} {p} {p} {p} В создании новеллы участвовали: {p} Данис Батыршин {p} Тимур Галиев {p} {p} {p} {p} Отдельное спасибо:{p} Аюпов Рэм {p} Лобанов Никита {p} {p} {p} Danis Studio 2020{/b}{/color}" at txt_up
    pause 20
return
label titri3:
    scene fionafinal#{color=#0A0A0A}{/color}
    play music "Good_Times.mp3"
    show text"{b}{color=#000000}Концовка - Фиона {p} {p} {p} {p} В создании новеллы участвовали: {p} Данис Батыршин {p} Тимур Галиев {p} {p} {p} {p} Отдельное спасибо:{p} Аюпов Рэм {p} Лобанов Никита {p} {p} {p} Danis Studio 2020{/b}{/color}" at txt_up
    pause 20
return
label titri4:
    scene kristinafinal#{color=#0A0A0A}{/color}
    play music "Good_Times.mp3"
    show text"{b}{color=#000000}Концовка - Кристина {p} {p} {p} {p} В создании новеллы участвовали: {p} Данис Батыршин {p} Тимур Галиев {p} {p} {p} {p} Отдельное спасибо:{p} Аюпов Рэм {p} Лобанов Никита {p} {p} {p} Danis Studio 2020{/b}{/color}" at txt_up
    pause 20
return
