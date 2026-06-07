# You can place the script of your game in this file.

########################################################
##### D E F I N I T I O N S #################################
########################################################
define narrator = Character(None, color="#fff", show_two_window=True, ctc="ctc", ctc_position="fixed")
define me = Character('О Б Р И', color="#fff", show_two_window=True, ctc="ctc", ctc_position="fixed")
define mai = Character('М А Я', color="#fff", show_two_window=True, ctc="ctc", ctc_position="fixed")
define maishawnee = Character(' М А Я ', color="#fff", show_two_window=True, what_ruby_style=style.ruby_style, what_line_leading=30, what_line_spacing=30, ctc="ctc", ctc_position="fixed")
define girl = Character('Д Е В О Ч К А', color="#fff", show_two_window=True, ctc="ctc", ctc_position="fixed")
define girlshawnee = Character(' Д Е В О Ч К А ', color="#fff", show_two_window=True, what_ruby_style=style.ruby_style, what_line_leading=30, what_line_spacing=30, ctc="ctc", ctc_position="fixed")
define jackson = Character('Д Ж Е К С О Н', color="#fff", show_two_window=True, ctc="ctc", ctc_position="fixed")
define captain = Character('К А П И Т А Н', color="#fff", show_two_window=True, ctc="ctc", ctc_position="fixed")
define daniels = Character('Д Э Н И Э Л С', color="#fff", show_two_window=True, ctc="ctc", ctc_position="fixed")
define mctavish = Character('М А К Т А В И Ш', color="#fff", show_two_window=True, ctc="ctc", ctc_position="fixed")
define scout = Character('Р А З В Е Д Ч И К', color="#fff", show_two_window=True, ctc="ctc", ctc_position="fixed")

########################################################
##### B A C K G R O U N D S ###############################
########################################################
image caveback:
    contains:
        "back/cave.jpg"
    contains:
        "back/cave2.jpg"
        alpha 0
        linear 0.2 alpha 0.5
        linear 0.2 alpha 0
        repeat
    contains:
        "black"
        alpha 0
        linear 1.0 alpha 0.3
        linear 1.0 alpha 0
        7.0
        repeat
    contains:
        im.MatrixColor("back/cave2.jpg", im.matrix.tint(1, .9, .9))
        alpha 0
        linear 0.5 alpha 1.0
        linear 0.5 alpha 0
        5.0
        repeat
image plains = "back/plains.jpg"
image plainsnight = "back/plains_night.jpg"
image map = "back/map.jpg"
image forest = "back/forest.jpg"
image forest2:
    "back/forest.jpg"
    xzoom -1
image forestnight:
    contains:
        "back/forestnight.jpg"
    contains:
        "back/forestfire.jpg"
        alpha 0
        linear 5.0 alpha 0.3
        linear 5.0 alpha 0
        repeat
    contains:
        "blacksmoke"
        alpha 0.4
    contains:
        "back/forestfire.jpg"
        additive 1.0
        alpha 0.2
        linear 0.5 alpha 0
        linear 0.5 alpha 0.2
        repeat
image canopy = "back/canopy.jpg"
image forestfade:
    contains:
        "back/forest.jpg"
    contains:
        im.Grayscale("back/forest.jpg")
        alpha .4
        xalign 0.5
        yalign 0.5
        linear 2.0 xalign 0.7 yalign 0.7 zoom 1.1
        linear 2.0 xalign 0.9 yalign 0.5 zoom 1.2
        linear 2.0 xalign 0.7 yalign 0.3 zoom 1.1
        linear 2.0 xalign 0.5 yalign 0.5 zoom 1.0
        linear 2.0 xalign 0.3 yalign 0.7 zoom 1.1
        linear 2.0 xalign 0.1 yalign 0.5 zoom 1.2
        linear 2.0 xalign 0.3 yalign 0.3 zoom 1.1
        linear 2.0 xalign 0.5 yalign 0.5 zoom 1.0
        repeat
    contains:
        im.Grayscale("back/forest.jpg")
        alpha .4
        xalign 0.3
        yalign 0.7
        linear 3.0 xalign 0.1 yalign 0.5 zoom 1.2
        linear 3.0 xalign 0.3 yalign 0.3 zoom 1.1
        linear 3.0 xalign 0.5 yalign 0.5 zoom 1.0
        linear 3.0 xalign 0.7 yalign 0.7 zoom 1.1
        linear 3.0 xalign 0.9 yalign 0.5 zoom 1.2
        linear 3.0 xalign 0.7 yalign 0.3 zoom 1.1
        linear 3.0 xalign 0.5 yalign 0.5 zoom 1.0
        linear 3.0 xalign 0.3 yalign 0.7 zoom 1.1
        repeat
image forestfade2:
    contains:
        "back/forest.jpg"
    contains:
        "back/forest.jpg"
        alpha .2
        xalign 0.5
        yalign 0.5
        linear 2.0 xalign 0.7 yalign 0.7 zoom 1.05
        linear 2.0 xalign 0.9 yalign 0.5 zoom 1.1
        linear 2.0 xalign 0.7 yalign 0.3 zoom 1.05
        linear 2.0 xalign 0.5 yalign 0.5 zoom 1.0
        linear 2.0 xalign 0.3 yalign 0.7 zoom 1.05
        linear 2.0 xalign 0.1 yalign 0.5 zoom 1.1
        linear 2.0 xalign 0.3 yalign 0.3 zoom 1.05
        linear 2.0 xalign 0.5 yalign 0.5 zoom 1.0
        repeat
    contains:
        "back/forest.jpg"
        alpha .2
        xalign 0.3
        yalign 0.7
        linear 3.0 xalign 0.1 yalign 0.5 zoom 1.1
        linear 3.0 xalign 0.3 yalign 0.3 zoom 1.05
        linear 3.0 xalign 0.5 yalign 0.5 zoom 1.0
        linear 3.0 xalign 0.7 yalign 0.7 zoom 1.05
        linear 3.0 xalign 0.9 yalign 0.5 zoom 1.1
        linear 3.0 xalign 0.7 yalign 0.3 zoom 1.05
        linear 3.0 xalign 0.5 yalign 0.5 zoom 1.0
        linear 3.0 xalign 0.3 yalign 0.7 zoom 1.05
        repeat        
image forestrain:
    contains:
        "black"
    contains:
        alpha 0.5
        xzoom -1
        im.Grayscale("back/forest.jpg")
    contains:
        alpha 0.3
        xzoom -1
        "back/forest.jpg"
    contains:
        "heavyrain2"
    contains:
        alpha 0.7
        "smoke2"
    contains:
        "mist"
    contains:
        "heavyrain2"
image forestrainjackson:
    contains:
        "black"
    contains:
        alpha 0.5
        xzoom -1
        im.Grayscale("back/forest.jpg")
    contains:
        alpha 0.3
        xzoom -1
        "back/forest.jpg"    
    contains:
        "heavyrain2"
    contains:
        "jackson determined"
        xalign 0.5
        yalign 1.0
    contains:
        alpha 0.7
        "smoke2"
    contains:
        silhouetted("character/jackson/jackson_determined.png",0,0,0)
        xalign 0.5
        yalign 1.0
        alpha 0.9
    contains:
        "mist"
    contains:
        "heavyrain2"
image barn = "back/barninterior.jpg"
image barnday = "back/barninteriorday.jpg"
image barn night = im.MatrixColor ("back/barninterior.jpg", im.matrix.brightness(-0.05)*im.matrix.tint(.5, .5, 1)*im.matrix.saturation(0.4))
image barnrun:
    "back/barninterior.jpg" with hpunch
    0.2
    "back/barninterior.jpg" with vpunch
    0.2
    repeat
image fieldback = "back/battlefield.jpg"
image fieldback2 = "back/battlefield2.jpg"
image sky = "back/sky.jpg"
image sky2 = "back/sky2.jpg"
image sky3 = "back/sky3.jpg"
image sky4 = "back/sky4.jpg"
image village = "back/village_day.jpg"
image field:
    contains:
        "black"
    contains:
        alpha 0.5
        "back/field.jpg"
    contains:
        "heavyrain2"
image flashback1:
    contains:
        "back/flashback1.jpg"
    contains:
        "snowlighter"
    contains:
        "mist"
    contains:
        "gui/black_bars3.png"
image flashback2:
    contains:
        "back/flashback2.jpg"
    contains:
        "snowlighter"
    contains:
        "mist"
    contains:
        "gui/black_bars3.png"
image flashback3:
    contains:
        "back/flashback3.jpg"
    contains:
        "snowlighter"
    contains:
        "mist"
    contains:
        "gui/black_bars3.png"
image flashback4:
    contains:
        "back/flashback4.jpg"
    contains:
        "heavyrain2"
    contains:
        "mist"
    contains:
        "gui/black_bars3.png"
image flashback5:
    contains:
        "back/flashback5.jpg"
    contains:
        "heavyrain2"
        alpha 0.8
        zoom 3.0
        rotate -10
        xalign 0.5
        yalign 0.5
        pause 0.4
        xalign 0.6
        yalign 0.6
        zoom 3.1
        pause 0.4
        xalign 0.4
        yalign 0.4
        zoom 2.9
        pause 0.4
        xalign 0.55
        yalign 0.4
        zoom 3.0
        pause 0.4
        xalign 0.4
        yalign 0.6
        zoom 3.1
        pause 0.4
        xalign 0.5
        zoom 3.0
        repeat
    contains:
        "mist"
    contains:
        "gui/black_bars3.png"
image flashback6:
    contains:
        "black"
    contains:
        "rainfall"
    contains:
        "mist"
    contains:
        "gui/black_bars3.png"        
image leaves:
    contains:
        "effects/leaves.png"
        alpha 1.0
        linear 3.0 zoom 1.01 alpha 1.3
        linear 3.0 zoom 1.0 alpha 1.0
        repeat
image credits:
    contains:
        "black"
    contains:
        "barn"
        alpha 0
        pause 4.0
        linear 5.0 alpha 1.0
    contains:
        "cg1"
        alpha 0
        10.0
        linear 10.0 alpha 1.0
        35.0
        linear 10.0 alpha 0
    contains:
        "cg2"
        alpha 0
        45.0
        linear 10.0 alpha 1.0
        35.0
        linear 10.0 alpha 0
    contains:
        "cg3"
        alpha 0
        80.0
        linear 10.0 alpha 1.0
        35.0
        linear 10.0 alpha 0
    contains:
        "cg4"
        alpha 0
        115.0
        linear 10.0 alpha 1.0
        35.0
        linear 10.0 alpha 0
    contains:
        "cg5"
        alpha 0
        150.0
        linear 10.0 alpha 1.0
        35.0
        linear 10.0 alpha 0
    contains:
        "cg6"
        alpha 0
        185.0
        linear 10.0 alpha 1.0
        25.0
        linear 10.0 alpha 0
    contains:
        "transparent"
########################################################
##### C H A R A C T E R   A R T #############################
########################################################
image mai happy = "character/mai/mai_happy.png"
image mai happy large = "character/mai/mai_happy_large.png"
image mai happy2 = "character/mai/mai_happy2.png"
image mai sad = "character/mai/mai_sad.png"
image mai sad large = "character/mai/mai_sad_large.png"
image mai cry = "character/mai/mai_cry.png"
image mai cry2 = "character/mai/mai_cry2.png"
image mai soot = "character/mai/mai_soot.png"
image mai soot2 = "character/mai/mai_soot2.png"
image mai normal = "character/mai/mai_normal.png"
image mai normal large = "character/mai/mai_normal_large.png"
image mai worry = "character/mai/mai_worry.png"
image mai worry large = "character/mai/mai_worry_large.png"
image mai angry = "character/mai/mai_angry.png"
image mai gulp = "character/mai/mai_gulp.png"
image mai angry large = "character/mai/mai_angry_large.png"
image mai2 dangle:
    "character/mai/mai_full.png"
    xalign 1.48
    yalign 2.5
    linear 2.0 rotate 1 yalign 2.52
    linear 2.0 rotate 0 yalign 2.5
    linear 2.0 rotate -1 yalign 2.51
    linear 2.0 rotate 0 yalign 2.5
    repeat
image mai2 fall:
    "character/mai/mai_full.png"
    xalign 1.48
    yalign 2.5
    linear 0.3 yalign -0.5
    
image mai hit:
    contains:
        "barn" with hpunch
        pause 0.5
        repeat
    contains:
        "mai angry"
        xalign 0.5 yalign 1.0
        linear 0.02 xalign 0.51
        linear 0.04 xalign 0.49
        linear 0.02 xalign 0.5
        linear 0.02 xalign 0.51
        linear 0.04 xalign 0.49
        linear 0.02 xalign 0.5
        pause 0.5
        repeat
image mai bounce:
    contains:
        "barn" with vpunch
        pause 0.5
        repeat
    contains:
        "mai worry"
        xalign 0.5 yalign 1.0
        linear 0.02 xalign 0.501 yalign 1.03
        linear 0.04 xalign 0.499 yalign 1.06
        linear 0.02 xalign 0.5 yalign 1.1
        linear 0.02 xalign 0.501 yalign 1.06
        linear 0.04 xalign 0.499 yalign 1.03
        linear 0.02 xalign 0.5 yalign 1.0
        pause 0.5
        repeat
image maifire normal:
    contains:
        silhouetted("character/mai/mai_normal.png", 0, 0, 0)
        xalign 0.51
        yalign 1.0
        alpha 0.1
        zoom 1.01
        linear 0.5 zoom 1.02 xalign 0.5
        linear 0.5 zoom 1.01 xalign 0.49
        linear 0.5 zoom 1.02 xalign 0.5
        linear 0.5 zoom 1.01 xalign 0.51
        linear 0.5 zoom 1.03 xalign 0.5
        linear 0.5 zoom 1.01 xalign 0.51
        repeat
    contains:
        im.MatrixColor ("character/mai/mai_normal.png", im.matrix.brightness(-0.25)*im.matrix.tint(.5, .5, 1)*im.matrix.saturation(0.4))
        xalign 0.5
        yalign 1.0
    contains:
        im.MatrixColor ("character/mai/mai_normal.png", im.matrix.brightness(0.05)*im.matrix.tint(1, .8, .8))
        xalign 0.5
        yalign 1.0
        alpha 0.1
        linear 0.5 alpha 0.15
        linear 0.5 alpha 0.1
        linear 0.5 alpha 0.2
        linear 0.5 alpha 0.12
        linear 0.5 alpha 0.1
        linear 0.5 alpha 0.2
        linear 0.5 alpha 0.1
        repeat
image maifire happy:
    contains:
        silhouetted("character/mai/mai_happy.png", 0, 0, 0)
        xalign 0.51
        yalign 1.0
        alpha 0.1
        zoom 1.01
        linear 0.5 zoom 1.02 xalign 0.5
        linear 0.5 zoom 1.01 xalign 0.49
        linear 0.5 zoom 1.02 xalign 0.5
        linear 0.5 zoom 1.01 xalign 0.51
        linear 0.5 zoom 1.03 xalign 0.5
        linear 0.5 zoom 1.01 xalign 0.51
        repeat
    contains:
        im.MatrixColor ("character/mai/mai_happy.png", im.matrix.brightness(-0.25)*im.matrix.tint(.5, .5, 1)*im.matrix.saturation(0.4))
        xalign 0.5
        yalign 1.0
    contains:
        im.MatrixColor ("character/mai/mai_happy.png", im.matrix.brightness(0.05)*im.matrix.tint(1, .8, .8))
        xalign 0.5
        yalign 1.0
        alpha 0.1
        linear 0.5 alpha 0.15
        linear 0.5 alpha 0.1
        linear 0.5 alpha 0.2
        linear 0.5 alpha 0.12
        linear 0.5 alpha 0.1
        linear 0.5 alpha 0.2
        linear 0.5 alpha 0.1
        repeat
image maifire happy2:
    contains:
        silhouetted("character/mai/mai_happy2.png", 0, 0, 0)
        xalign 0.51
        yalign 1.0
        alpha 0.1
        zoom 1.01
        linear 0.5 zoom 1.02 xalign 0.5
        linear 0.5 zoom 1.01 xalign 0.49
        linear 0.5 zoom 1.02 xalign 0.5
        linear 0.5 zoom 1.01 xalign 0.51
        linear 0.5 zoom 1.03 xalign 0.5
        linear 0.5 zoom 1.01 xalign 0.51
        repeat
    contains:
        im.MatrixColor ("character/mai/mai_happy2.png", im.matrix.brightness(-0.25)*im.matrix.tint(.5, .5, 1)*im.matrix.saturation(0.4))
        xalign 0.5
        yalign 1.0
    contains:
        im.MatrixColor ("character/mai/mai_happy2.png", im.matrix.brightness(0.05)*im.matrix.tint(1, .8, .8))
        xalign 0.5
        yalign 1.0
        alpha 0.1
        linear 0.5 alpha 0.15
        linear 0.5 alpha 0.1
        linear 0.5 alpha 0.2
        linear 0.5 alpha 0.12
        linear 0.5 alpha 0.1
        linear 0.5 alpha 0.2
        linear 0.5 alpha 0.1
        repeat
image maifire angry:
    contains:
        silhouetted("character/mai/mai_angry.png", 0, 0, 0)
        xalign 0.51
        yalign 1.0
        alpha 0.1
        zoom 1.01
        linear 0.5 zoom 1.02 xalign 0.5
        linear 0.5 zoom 1.01 xalign 0.49
        linear 0.5 zoom 1.02 xalign 0.5
        linear 0.5 zoom 1.01 xalign 0.51
        linear 0.5 zoom 1.03 xalign 0.5
        linear 0.5 zoom 1.01 xalign 0.51
        repeat
    contains:
        im.MatrixColor ("character/mai/mai_angry.png", im.matrix.brightness(-0.25)*im.matrix.tint(.5, .5, 1)*im.matrix.saturation(0.4))
        xalign 0.5
        yalign 1.0
    contains:
        im.MatrixColor ("character/mai/mai_angry.png", im.matrix.brightness(0.05)*im.matrix.tint(1, .8, .8))
        xalign 0.5
        yalign 1.0
        alpha 0.1
        linear 0.5 alpha 0.15
        linear 0.5 alpha 0.1
        linear 0.5 alpha 0.2
        linear 0.5 alpha 0.12
        linear 0.5 alpha 0.1
        linear 0.5 alpha 0.2
        linear 0.5 alpha 0.1
        repeat
image maifire worry:
    contains:
        silhouetted("character/mai/mai_worry.png", 0, 0, 0)
        xalign 0.51
        yalign 1.0
        alpha 0.1
        zoom 1.01
        linear 0.5 zoom 1.02 xalign 0.5
        linear 0.5 zoom 1.01 xalign 0.49
        linear 0.5 zoom 1.02 xalign 0.5
        linear 0.5 zoom 1.01 xalign 0.51
        linear 0.5 zoom 1.03 xalign 0.5
        linear 0.5 zoom 1.01 xalign 0.51
        repeat
    contains:
        im.MatrixColor ("character/mai/mai_worry.png", im.matrix.brightness(-0.25)*im.matrix.tint(.5, .5, 1)*im.matrix.saturation(0.4))
        xalign 0.5
        yalign 1.0
    contains:
        im.MatrixColor ("character/mai/mai_worry.png", im.matrix.brightness(0.05)*im.matrix.tint(1, .8, .8))
        xalign 0.5
        yalign 1.0
        alpha 0.1
        linear 0.5 alpha 0.15
        linear 0.5 alpha 0.1
        linear 0.5 alpha 0.2
        linear 0.5 alpha 0.12
        linear 0.5 alpha 0.1
        linear 0.5 alpha 0.2
        linear 0.5 alpha 0.1
        repeat
image maifire hiccup:
    "maifire worry" with hpunch
    3.0
    repeat
image maifire cry:
    contains:
        silhouetted("character/mai/mai_cry.png", 0, 0, 0)
        xalign 0.51
        yalign 1.0
        alpha 0.1
        zoom 1.01
        linear 0.5 zoom 1.02 xalign 0.5
        linear 0.5 zoom 1.01 xalign 0.49
        linear 0.5 zoom 1.02 xalign 0.5
        linear 0.5 zoom 1.01 xalign 0.51
        linear 0.5 zoom 1.03 xalign 0.5
        linear 0.5 zoom 1.01 xalign 0.51
        repeat
    contains:
        im.MatrixColor ("character/mai/mai_cry.png", im.matrix.brightness(-0.25)*im.matrix.tint(.5, .5, 1)*im.matrix.saturation(0.4))
        xalign 0.5
        yalign 1.0
    contains:
        im.MatrixColor ("character/mai/mai_cry.png", im.matrix.brightness(0.05)*im.matrix.tint(1, .8, .8))
        xalign 0.5
        yalign 1.0
        alpha 0.1
        linear 0.5 alpha 0.15
        linear 0.5 alpha 0.1
        linear 0.5 alpha 0.2
        linear 0.5 alpha 0.12
        linear 0.5 alpha 0.1
        linear 0.5 alpha 0.2
        linear 0.5 alpha 0.1
        repeat
image maifire sad:
    contains:
        silhouetted("character/mai/mai_sad.png", 0, 0, 0)
        xalign 0.51
        yalign 1.0
        alpha 0.1
        zoom 1.01
        linear 0.5 zoom 1.02 xalign 0.5
        linear 0.5 zoom 1.01 xalign 0.49
        linear 0.5 zoom 1.02 xalign 0.5
        linear 0.5 zoom 1.01 xalign 0.51
        linear 0.5 zoom 1.03 xalign 0.5
        linear 0.5 zoom 1.01 xalign 0.51
        repeat
    contains:
        im.MatrixColor ("character/mai/mai_sad.png", im.matrix.brightness(-0.25)*im.matrix.tint(.5, .5, 1)*im.matrix.saturation(0.4))
        xalign 0.5
        yalign 1.0
    contains:
        im.MatrixColor ("character/mai/mai_sad.png", im.matrix.brightness(0.05)*im.matrix.tint(1, .8, .8))
        xalign 0.5
        yalign 1.0
        alpha 0.1
        linear 0.5 alpha 0.15
        linear 0.5 alpha 0.1
        linear 0.5 alpha 0.2
        linear 0.5 alpha 0.12
        linear 0.5 alpha 0.1
        linear 0.5 alpha 0.2
        linear 0.5 alpha 0.1
        repeat
image maifire gulp:
    contains:
        silhouetted("character/mai/mai_gulp.png", 0, 0, 0)
        xalign 0.51
        yalign 1.0
        alpha 0.1
        zoom 1.01
        linear 0.5 zoom 1.02 xalign 0.5
        linear 0.5 zoom 1.01 xalign 0.49
        linear 0.5 zoom 1.02 xalign 0.5
        linear 0.5 zoom 1.01 xalign 0.51
        linear 0.5 zoom 1.03 xalign 0.5
        linear 0.5 zoom 1.01 xalign 0.51
        repeat
    contains:
        im.MatrixColor ("character/mai/mai_gulp.png", im.matrix.brightness(-0.25)*im.matrix.tint(.5, .5, 1)*im.matrix.saturation(0.4))
        xalign 0.5
        yalign 1.0
    contains:
        im.MatrixColor ("character/mai/mai_gulp.png", im.matrix.brightness(0.05)*im.matrix.tint(1, .8, .8))
        xalign 0.5
        yalign 1.0
        alpha 0.1
        linear 0.5 alpha 0.15
        linear 0.5 alpha 0.1
        linear 0.5 alpha 0.2
        linear 0.5 alpha 0.12
        linear 0.5 alpha 0.1
        linear 0.5 alpha 0.2
        linear 0.5 alpha 0.1
        repeat
image darkmai happy = im.MatrixColor ("character/mai/mai_happy.png", im.matrix.brightness(-0.05)*im.matrix.saturation(0.8))
image darkmai happy2 = im.MatrixColor ("character/mai/mai_happy2.png", im.matrix.brightness(-0.05)*im.matrix.saturation(0.8))
image darkmai sad = im.MatrixColor ("character/mai/mai_sad.png", im.matrix.brightness(-0.05)*im.matrix.saturation(0.8))
image darkmai cry = im.MatrixColor ("character/mai/mai_cry.png", im.matrix.brightness(-0.05)*im.matrix.saturation(0.8))
image darkmai normal = im.MatrixColor ("character/mai/mai_normal.png", im.matrix.brightness(-0.05)*im.matrix.saturation(0.8))
image darkmai worry = im.MatrixColor ("character/mai/mai_worry.png", im.matrix.brightness(-0.05)*im.matrix.saturation(0.8))
image darkmai angry = im.MatrixColor ("character/mai/mai_angry.png", im.matrix.brightness(-0.05)*im.matrix.saturation(0.8))

image jackson determined = "character/jackson/jackson_determined.png"
image jackson evil = "character/jackson/jackson_evil.png"
image jackson shock = "character/jackson/jackson_shock.png"
image jackson bored = "character/jackson/jackson_bored.png"
image jackson angry = "character/jackson/jackson_angry.png"

image jackson dark determined = im.MatrixColor ("character/jackson/jackson_determined.png", im.matrix.brightness(-0.05)*im.matrix.saturation(0.8))
image jackson dark evil = im.MatrixColor ("character/jackson/jackson_evil.png", im.matrix.brightness(-0.05)*im.matrix.saturation(0.8))
image jackson dark shock = im.MatrixColor ("character/jackson/jackson_shock.png", im.matrix.brightness(-0.05)*im.matrix.saturation(0.8))
image jackson dark bored = im.MatrixColor ("character/jackson/jackson_bored.png", im.matrix.brightness(-0.05)*im.matrix.saturation(0.8))
image jackson dark angry = im.MatrixColor ("character/jackson/jackson_angry.png", im.matrix.brightness(-0.05)*im.matrix.saturation(0.8))

image jackson night determined = im.MatrixColor ("character/jackson/jackson_determined.png", im.matrix.brightness(-0.15)*im.matrix.tint(.5, .5, 1)*im.matrix.saturation(0.4))
image jackson night bored = im.MatrixColor ("character/jackson/jackson_bored.png", im.matrix.brightness(-0.15)*im.matrix.tint(.5, .5, 1)*im.matrix.saturation(0.4))
image jackson night shock = im.MatrixColor ("character/jackson/jackson_shock.png", im.matrix.brightness(-0.15)*im.matrix.tint(.5, .5, 1)*im.matrix.saturation(0.4))
image jackson night evil = im.MatrixColor ("character/jackson/jackson_evil.png", im.matrix.brightness(-0.15)*im.matrix.tint(.5, .5, 1)*im.matrix.saturation(0.4))
image jackson night angry = im.MatrixColor ("character/jackson/jackson_angry.png", im.matrix.brightness(-0.15)*im.matrix.tint(.5, .5, 1)*im.matrix.saturation(0.4))

########################################################
##### C R E D I T S #######################################
########################################################
image creditscroll:
    contains:
        alpha 0
        yalign 0.48
        xalign 0.5
        "gui/title.png"
        linear 3.0 alpha 1.0
        4.5
        linear 14.0 ypos 0.0 yanchor 1.0
    contains:    
        Text([      
    "{b}{size=26}WarGirl Games{/size}{/b} \n \n \n"
    "\n{b}{size=-5}Created by{/b} \nDesertFox \n \n \n"
    "\n{b}{size=-5}Written by{/b} \nDesertFox \n \n \n"
    "\n{b}{size=-5}Editing{/size}{/b} \nDesertFox \n \n \n"
    "\n{b}{size=-5}Programming{/size}{/b} \nDesertFox \n \n \n"
    "\n{b}{size=-5}Additional Art{/size}{/b} \nDesertFox \n \n \n"
    "\n \n \n \n \n \n \n"
    "\n{b}{size=26}Collateral Damage Studios{/size}{/b} \n \n \n"
    "\n{b}{size=-5}Producer{/size}{/b} \nNg Kian Chuan \n \n \n"
    "\n{b}{size=-5}Character Art{/size}{/b} \nTan Hui Tian \n \n"
    "\n{b}{size=-5}CG Art{/size}{/b} \nTan Hui Tian \n \n \n"
    "\n{b}{size=-5}Background Art{/size}{/b} \nTan Hui Tian \n \n \n"
    "\n{b}{size=-5}Concept Art{/size}{/b} \nTan Hui Tian \n \n \n"
    "\n \n \n \n \n \n \n"
    "\n{b}{size=26}Seycara Music and Arts{/size}{/b}\n \n \n"
    "\n{b}{size=-5}Music Composed and Conducted by{/size}{/b} \nYuang Chen \n \n \n"
    "\n{b}{size=-5}Performances Featuring{/size}{/b} \nThe Seycara Orchestra \n \n \n"
    "\n{b}{size=-5}Flute/Piccolo{/size}{/b} \nNicholas Ashland \nDanika Jorgenson \n \n \n"
    "\n{b}{size=-5}Oboe/English Horn{/size}{/b} \nAnnabelle Kleinschmidt \n \n \n"
    "\n{b}{size=-5}Clarinet{/size}{/b} \nKazuki Sakagami \n \n \n"
    "\n{b}{size=-5}Bassoon/Contrabassoon{/size}{/b} \nJason Huang \n \n \n"
    "\n{b}{size=-5}French Horn{/size}{/b} \nKirk Huckaba \nKathleen Ray \nSydni Harrison \n \n \n"
    "\n{b}{size=-5}Trumpet{/size}{/b} \nTania Hayes \nAlex Vyhinsky \n \n \n"
    "\n{b}{size=-5}Trombone{/size}{/b} \nPhilip Borg \nJoseph Baker \n \n \n"
    "\n{b}{size=-5}Bass Trombone{/size}{/b} \nJosephine Baker \n \n \n"
    "\n{b}{size=-5}Tuba{/size}{/b} \nIvan Tsvirinkal \n \n \n"
    "\n{b}{size=-5}Percussion{/size}{/b} \nLeonard Maxwell \nKeith Kendall \nJay Howston \n \n \n"
    "\n{b}{size=-5}Piano/Celeste{/size}{/b} \nJennifer Liang \n \n \n"
    "\n{b}{size=-5}Violin I{/size}{/b} \nYoshiyuki Oshiro \nVera Hastings \nKazuya Takanabe \nMoe Waterhouse \n \n \n"
    "\n{b}{size=-5}Violin II{/size}{/b} \nTimothy Leblanc \nGeorgina Smith \nUra Fova \n \n \n"
    "\n{b}{size=-5}Viola{/size}{/b} \nHarold Gillings \nHoward Torvin \n \n \n"
    "\n{b}{size=-5}Cello{/size}{/b} \nNina Valenciano \nCaleb Jareth \nRory Quinten \n \n \n"
    "\n{b}{size=-5}Double Bass{/size}{/b} \nAmanda Orizaga \nDaniel Farris \n \n \n"
    "\n{b}{size=-5}Produced and Mastered by{/size}{/b} \nTakumi Nishimura \n \n \n"
    "\n{b}{i}'After All'{/i}{/b} \n{size=-5}Vocals{/size} \nSagisapon\n{size=-5}Music and Lyrics{/size} \nSeycara Music and Arts \n \n \n"
    "\n \n \n \n \n \n \n"
    "\n{b}{size=-5}Sound Design{/size}{/b} \nDesertFox \n \n \n"
    "\n{b}{size=-5}Sound Library{/size}{/b} \nKaizanmurou \nThe Matchmaker \nMaoudamashii \nSoundBible \nMike Koenig \nRHumphries \nErdie \nPingel \nFreqMan \nFreesound \nSmap Sounds \nTheMSsoundeffects \nSoundEffectsFactory \nMaskey \ncopyrighy free sound-effect \nMySoundEffect \nBerlin Atmospheres \niWav \nHot Ideas \n \n \n"
    "\n{b}{size=-5}Rainfall MV{/size}{/b} \nFootage Oasis \n \n \n"
    "\n{b}{size=-5}Beta Testing{/size}{/b} \nRyan Jackson \nPal \nYuang Chen \nMama Miller \n \n \n"
    "\n{b}{size=-5}Special Thanks{/size}{/b} \nNg Kian Chuan \nYuang Chen \nJohn Tibbetts \nMichael Brand \nAlexander Kimball \nColin Gogian \nVitezslav Konecny \nFlavio Reis \nhoruseye \nRewind \nwindFx \nbiskmater \nVenron \nRichard \nHWaie \nRyan Jackson \n'Pal' Miller \nL \nNissim Farin \nThe Hyperspace Forums \nThe Lemmasoft Forums \nThe Steam Community \nValve \nMichael Pitzer \nPyTom \nArraxis \nVNsNow \nFemHype \n \n \n"
    "\n{b}{size=-5}Built using the{/size} \nRen'Py Engine{/b} \n \n \n"
    "\n{size=-15}{image=gui/logo2.png}{/size}"
    "\n{b}{size=-5}© 2015 WarGirl Games\nhttp://war-girl.com{/size}{/b} \n \n \n"
    "\n{size=-5}{image=gui/cds.png}{/size}"
    "\n{b}{size=-5}C.D.S Collateral Damage Studios\nhttp://www.collateralds.com{/size}{/b} \n \n \n"
    "\n{size=-15}{image=gui/sey_logo.png}{/size}"
    "\n{b}{size=-5}© 2015 Seycara Music and Arts\nhttp://www.seycara.com{/size}{/b} \n \n \n \n \n \n"
    "\n{b}{size=-3}Thanks for playing{/b}!{/size} \n \n \n \n"  
    ], outlines=[(2, "#000000", 0, 0)], text_align=0.5, color="#ffffff")
        anchor (0.5, 0.0)
        pos (0.5, 1.0)
        6.5
        linear 230.0 ypos 0.0 yanchor 1.0
########################################################
##### C G S #############################################
########################################################
init:
    image cg1 = "cg/cg1.jpg"
    image cg2 = "cg/cg2.jpg"
    image cg3 = "cg/cg3.jpg"
    image cg4 = "cg/cg4.jpg"
    image cg5 = "cg/cg5.jpg"
    image cg6 = "cg/cg6.jpg"
    image cg6 2 = "cg/cg6_2.jpg"
    image bg1 = "back/battlefield.jpg"
    image bg2 = "back/barninterior.jpg"
    image bg3 = "back/forest.jpg"
    image bg4 = "back/plains.jpg"
    image bg5 = "back/village_day.jpg"
    image bg6 = "back/sky.jpg"
    image bg7 = "back/sky2.jpg"
    image bg8 = "back/sky3.jpg"
    image bg9 = "back/map.jpg"
    image bg10 = "back/barninteriorday.jpg"
    image bg11 = im.MatrixColor ("back/barninterior.jpg", im.matrix.brightness(-0.05)*im.matrix.tint(.5, .5, 1)*im.matrix.saturation(0.4))
    image bg12 = "forestnight"
    image bg13 = "field"
    image bg14 = "back/canopy.jpg"
    image concept1 = "concept/concept1.jpg"
    image concept2 = "concept/concept2.jpg"
    image concept3 = "concept/concept3.jpg"
    image concept4 = "concept/concept4.jpg"
    image concept5 = "concept/concept5.jpg"
    image concept6 = "concept/concept6.jpg"
    image concept7 = "concept/concept7.jpg"
    image concept8 = "concept/concept8.jpg"
image cg4 large:
    contains:
        "cg/cg4_large.jpg"
        rotate 0
        xalign 0.7
        yalign 0.6
        1.5
        linear 6.0 xalign 0.5 yalign 0.449 rotate -5.5
        2.0
image cg5fade:
    contains:
        "cg/cg5.jpg"
    contains:
        "cg/cg5.jpg"
        alpha 0
        pause 1.0
        alpha 1.0
        "cg/cg5.jpg" with hpunch
        pause 0.1
        alpha 0
        pause 17.75
        repeat
    contains:
        "cg/cg5.jpg"
        alpha .2
        xalign 0.5
        yalign 0.5
        linear 2.0 xalign 0.7 yalign 0.7 zoom 1.05
        linear 2.0 xalign 0.9 yalign 0.5 zoom 1.1
        linear 2.0 xalign 0.7 yalign 0.3 zoom 1.05
        linear 2.0 xalign 0.5 yalign 0.5 zoom 1.0
        linear 2.0 xalign 0.3 yalign 0.7 zoom 1.05
        linear 2.0 xalign 0.1 yalign 0.5 zoom 1.1
        linear 2.0 xalign 0.3 yalign 0.3 zoom 1.05
        linear 2.0 xalign 0.5 yalign 0.5 zoom 1.0
        pause 1.75
        repeat
    contains:
        "cg/cg5.jpg"
        alpha .2
        xalign 0.3
        yalign 0.7
        linear 3.0 xalign 0.1 yalign 0.5 zoom 1.1
        linear 3.0 xalign 0.3 yalign 0.3 zoom 1.05
        linear 3.0 xalign 0.5 yalign 0.5 zoom 1.0
        linear 3.0 xalign 0.7 yalign 0.7 zoom 1.05
        linear 3.0 xalign 0.9 yalign 0.5 zoom 1.1
        linear 3.0 xalign 0.7 yalign 0.3 zoom 1.05
        linear 3.0 xalign 0.5 yalign 0.5 zoom 1.0
        linear 3.0 xalign 0.3 yalign 0.7 zoom 1.05
        repeat     
image cg7:
    contains:
        "cg/cg7.jpg"
    contains:
        "heavyrain3"
image cg6 large:
    contains:
        "cg/cg6_large.jpg"
        xalign 0.1
        yalign 1.0
        2.0
        linear 12.0 xalign 0.5 yalign 0.05
        2.0
image cg8:
    contains:
        "back/village_large.jpg"
        yalign 0.9
        xalign 0.2
        linear 10.01 yalign 0.1
    contains:
        "character/jackson/jackson_large.png"
        xalign 0.5
        yalign 0.65
        rotate -2
        linear 10.0 yalign 0.03
image object1 = "cg/object1.png"
image object2 = "cg/object2.png"
image object3 = "cg/object3.png"
image object4 = "cg/object4.png"
image object5 = "cg/object5.png"
########################################################
##### E F F E C T S #######################################
########################################################
image sparklight = SnowBlossom(anim.Filmstrip("effects/spark.png", (12.5, 12.5), (4, 4), .13), 20, 20, (20, -400), (-20, 200), 3, horizontal=True)
image sparklight2 = SnowBlossom(anim.Filmstrip("effects/spark.png", (12.5, 12.5), (4, 4), .13), 10, 20, (20, -400), (-20, -200), 3, horizontal=False)
image spark:
    additive 1.0
    contains:
        "sparklight"
    contains:
        "sparklight"
    contains:
        "sparklight"
        zoom 1.5
        alpha 0.4
    contains:
        "sparklight"
        zoom 1.2
        alpha 0.8
image gunsmoke:
    additive 1.0
    contains:
        alpha 0
        pause 1.0
        alpha 1.5
        "effects/gunsmoke1.png"
        pause 0.05
        "effects/gunsmoke2.png"
        pause 0.05
        "effects/gunsmoke3.png"
        pause 0.05
        "effects/gunsmoke4.png"
        pause 0.05
        "effects/gunsmoke5.png"
        pause 0.05
        "effects/gunsmoke6.png"
        pause 0.05
        "effects/gunsmoke7.png"
        pause 0.05
        "effects/gunsmoke8.png"
        pause 0.05
        "effects/gunsmoke9.png"
        pause 0.05
        "effects/gunsmoke10.png"
        pause 0.05
        "effects/gunsmoke11.png"
        pause 0.05
        "effects/gunsmoke12.png"
        pause 0.05
        "effects/gunsmoke13.png"
        pause 0.07
        "effects/gunsmoke14.png"
        pause 0.07
        "effects/gunsmoke15.png"
        pause 0.07
        "effects/gunsmoke16.png"
        pause 0.07
        "effects/gunsmoke17.png"
        pause 0.07
        "effects/gunsmoke18.png"
        pause 0.07
        "effects/gunsmoke19.png"
        pause 0.07
        "effects/gunsmoke20.png"
        pause 0.07
        "effects/gunsmoke21.png"
        pause 0.07
        "effects/gunsmoke22.png"
        pause 0.07
        "effects/gunsmoke23.png"
        pause 0.07
        "effects/gunsmoke24.png"
        pause 0.07
        "effects/gunsmoke25.png"
        pause 0.07
        "effects/gunsmoke26.png"
        pause 0.07
        "effects/gunsmoke27.png"
        pause 0.07
        alpha 0
        pause 16.1
        repeat
image gunsmoke2:
    additive 1.0
    contains:
        alpha 0
        pause 1.0
        alpha 1.5
        "effects/gunsmoke1.png"
        pause 0.05
        "effects/gunsmoke2.png"
        pause 0.05
        "effects/gunsmoke3.png"
        pause 0.05
        "effects/gunsmoke4.png"
        pause 0.05
        "effects/gunsmoke5.png"
        pause 0.05
        "effects/gunsmoke6.png"
        pause 0.05
        "effects/gunsmoke7.png"
        pause 0.05
        "effects/gunsmoke8.png"
        pause 0.05
        "effects/gunsmoke9.png"
        pause 0.05
        "effects/gunsmoke10.png"
        pause 0.05
        "effects/gunsmoke11.png"
        pause 0.05
        "effects/gunsmoke12.png"
        pause 0.05
        "effects/gunsmoke13.png"
        pause 0.05
        "effects/gunsmoke14.png"
        pause 0.05
        "effects/gunsmoke15.png"
        pause 0.05
        "effects/gunsmoke16.png"
        pause 0.05
        "effects/gunsmoke17.png"
        pause 0.05
        "effects/gunsmoke18.png"
        pause 0.05
        "effects/gunsmoke19.png"
        pause 0.05
        "effects/gunsmoke20.png"
        pause 0.05
        "effects/gunsmoke21.png"
        pause 0.05
        "effects/gunsmoke22.png"
        pause 0.05
        "effects/gunsmoke23.png"
        pause 0.05
        "effects/gunsmoke24.png"
        pause 0.05
        "effects/gunsmoke25.png"
        pause 0.05
        "effects/gunsmoke26.png"
        pause 0.05
        "effects/gunsmoke27.png"
        pause 0.05
        alpha 0
        pause 17.4
        repeat
image blast:
    contains:
        "effects/blast3.png"
        additive 0.7
        alpha 0
        pause 1.0
        linear 0.2 alpha 5.5
        linear 0.2 alpha 0.5
        linear 0.1 alpha 0
        pause 17.25
        repeat
    contains:
        "effects/blast.png"
        additive 1.0
        alpha 0
        pause 1.0
        linear 0.2 alpha 2.0
        linear 0.2 alpha 0.5
        linear 0.1 alpha 0
        pause 17.25
        repeat
    contains:
        "spark"
        alpha 0
        pause 1.0
        linear 1.0 alpha 0.5
        linear 5.0 alpha 0
        pause 11.75
        repeat
    contains:
        "gunsmoke2"
        yzoom -1
        xpos 0.32
        ypos -0.3
        alpha 1.0
        pause 0.5
        linear 1.0 xpos 0.2
        pause 17.25
        repeat
    contains:
        "gunsmoke"
        xzoom -1
        xpos 0.75
        ypos -0.1
        alpha 1.0
        pause 1.0
        linear 1.0 xpos 0.6
        linear 1.0 alpha 0
        pause 15.75
        repeat
    contains:
        "gunsmoke"
        xpos 0.7
        alpha 1.0
        pause 1.0
        linear 1.0 xpos 0.5 alpha 0.5
        pause 16.75
        repeat
    contains:
        "blacksmoke"
        additive 0.5
        alpha 0
        pause 1.5
        linear 1.0 alpha 0.8
        linear 5.0 alpha 0
        pause 11.75
        repeat
image smoke:
    additive 0.2
    contains:
        "effects/smoke1.png" 
        alpha 0
        linear 4.5 alpha 1.5
        linear 3.5 alpha 0
        repeat
    contains:
        "effects/smoke2.png" 
        alpha 0
        linear 2.5 alpha 1.5
        linear 2.5 alpha 0
        repeat
    contains:
        "effects/smoke3.png" 
        alpha 0
        linear 2.0 alpha 1.5
        linear 2.0 alpha 0
        repeat
    contains:
        "effects/smoke4.png" 
        alpha 0
        linear 5.0 alpha 1.5
        linear 2.0 alpha 0
        repeat
image smoke2:
    additive 0.2
    contains:
        "effects/smoke1.png" 
        alpha 0
        rotate 180
        xalign 0.5
        yalign 0.5
        linear 4.5 alpha 1.5
        linear 3.5 alpha 0
        repeat
    contains:
        "effects/smoke2.png" 
        alpha 0
        rotate 180
        xalign 0.5
        yalign 0.5
        linear 2.5 alpha 1.5
        linear 2.5 alpha 0
        repeat
    contains:
        "effects/smoke3.png" 
        alpha 0
        rotate 180
        xalign 0.5
        yalign 0.5
        linear 2.0 alpha 1.5
        linear 2.0 alpha 0
        repeat
    contains:
        "effects/smoke4.png" 
        alpha 0
        rotate 180
        xalign 0.5
        yalign 0.5
        linear 5.0 alpha 1.5
        linear 2.0 alpha 0
        repeat
image blacksmoke:
    additive 0
    contains:
        im.MatrixColor("effects/smoke1.png",
                                         im.matrix.brightness(-10) * im.matrix.tint(255, 20, 147))
        alpha 0
        yzoom -1
        linear 4.5 alpha 1
        linear 3.5 alpha 0
        repeat
    contains:
        im.MatrixColor("effects/smoke2.png",
                                         im.matrix.brightness(-10) * im.matrix.tint(255, 20, 147))
        alpha 0
        yzoom -1
        linear 2.5 alpha 1
        linear 2.5 alpha 0
        repeat
    contains:
        im.MatrixColor("effects/smoke3.png",
                                         im.matrix.brightness(-10) * im.matrix.tint(255, 20, 147))
        alpha 0
        yzoom -1
        linear 2.0 alpha 1
        linear 2.0 alpha 0
        repeat
    contains:
        im.MatrixColor("effects/smoke4.png",
                                         im.matrix.brightness(-10) * im.matrix.tint(255, 20, 147))
        alpha 0
        yzoom -1
        linear 5.0 alpha 1
        linear 2.0 alpha 0
        repeat    
image blacksmoke2:
    additive 0
    contains:
        im.MatrixColor("effects/smoke1.png",
                                         im.matrix.brightness(-10) * im.matrix.tint(255, 20, 147))
        alpha 0
        yzoom -1
        linear 4.5 alpha 0.5
        linear 3.5 alpha 0
        repeat
    contains:
        im.MatrixColor("effects/smoke2.png",
                                         im.matrix.brightness(-10) * im.matrix.tint(255, 20, 147))
        alpha 0
        yzoom -1
        linear 2.5 alpha 0.5
        linear 2.5 alpha 0
        repeat
    contains:
        im.MatrixColor("effects/smoke3.png",
                                         im.matrix.brightness(-10) * im.matrix.tint(255, 20, 147))
        alpha 0
        yzoom -1
        linear 2.0 alpha 0.5
        linear 2.0 alpha 0
        repeat
    contains:
        im.MatrixColor("effects/smoke4.png",
                                         im.matrix.brightness(-10) * im.matrix.tint(255, 20, 147))
        alpha 0
        yzoom -1
        linear 5.0 alpha 0.5
        linear 2.0 alpha 0
        repeat    
image speedlines = "effects/speedlines.png"
image heavyrain:
    contains:
        "effects/heavyrain1.png"
        alpha 0
        linear 0.1 alpha 0.3
        linear 0.1 alpha 0
        linear 0.1 alpha 0
        linear 0.1 alpha 0
        repeat
    contains:
        "effects/heavyrain2.png"
        alpha 0.3
        linear 0.1 alpha 0
        linear 0.1 alpha 0
        linear 0.1 alpha 0
        linear 0.1 alpha 0.3
        repeat
    contains:
        "effects/heavyrain3.png"
        alpha 0
        linear 0.1 alpha 0
        linear 0.1 alpha 0.3
        linear 0.1 alpha 0
        linear 0.1 alpha 0
        repeat
    contains:
        "effects/heavyrain4.png"
        alpha 0
        linear 0.1 alpha 0
        linear 0.1 alpha 0
        linear 0.1 alpha 0.3
        linear 0.1 alpha 0
        repeat
    contains:
        "effects/heavyrain4.png"
        alpha 0
        additive 0
        linear 10.0
        linear 1.0 alpha 0.6 additive 1.0
        linear 1.0 alpha 0 additive 0
        repeat
image heavyrain2:
    contains:
        "effects/heavyrain1.png"
        alpha 0
        linear 0.1 alpha 0.2
        linear 0.1 alpha 0
        linear 0.1 alpha 0
        linear 0.1 alpha 0
        repeat
    contains:
        "effects/heavyrain2.png"
        alpha 0.3
        linear 0.1 alpha 0
        linear 0.1 alpha 0
        linear 0.1 alpha 0
        linear 0.1 alpha 0.2
        repeat
    contains:
        "effects/heavyrain3.png"
        alpha 0
        linear 0.1 alpha 0
        linear 0.1 alpha 0.2
        linear 0.1 alpha 0
        linear 0.1 alpha 0
        repeat
    contains:
        "effects/heavyrain4.png"
        alpha 0
        linear 0.1 alpha 0
        linear 0.1 alpha 0
        linear 0.1 alpha 0.2
        linear 0.1 alpha 0
        repeat
    contains:
        "effects/heavyrain4.png"
        alpha 0
        additive 0
        linear 10.0
        linear 1.0 alpha 0.5 additive 1.0
        linear 1.0 alpha 0 additive 0
        repeat

image heavyrain3:
    contains:
        "effects/heavyrain1.png"
        zoom 1.3
        rotate -5
        yalign 0.5
        xalign 0.5
        alpha 0
        linear 0.1 alpha 0.2
        linear 0.1 alpha 0
        linear 0.1 alpha 0
        linear 0.1 alpha 0
        repeat
    contains:
        "effects/heavyrain2.png"
        zoom 1.3
        rotate -5
        yalign 0.5
        xalign 0.5
        alpha 0.3
        linear 0.1 alpha 0
        linear 0.1 alpha 0
        linear 0.1 alpha 0
        linear 0.1 alpha 0.2
        repeat
    contains:
        "effects/heavyrain3.png"
        zoom 1.3
        rotate -5
        yalign 0.5
        xalign 0.5
        alpha 0
        linear 0.1 alpha 0
        linear 0.1 alpha 0.2
        linear 0.1 alpha 0
        linear 0.1 alpha 0
        repeat
    contains:
        "effects/heavyrain4.png"
        zoom 1.3
        rotate -5
        yalign 0.5
        xalign 0.5
        alpha 0
        linear 0.1 alpha 0
        linear 0.1 alpha 0
        linear 0.1 alpha 0.2
        linear 0.1 alpha 0
        repeat
    contains:
        "effects/heavyrain4.png"
        zoom 1.3
        rotate -5
        yalign 0.5
        xalign 0.5
        alpha 0
        additive 0
        linear 10.0
        linear 1.0 alpha 0.5 additive 1.0
        linear 1.0 alpha 0 additive 0
        repeat        
        
image snow2 = SnowBlossom("effects/snowflake.png", 200, 20, (20, 800), (20, 600))
image snowlight2 = SnowBlossom("effects/snowflake.png", 50, 20, (20, 200), (20, 150))
image rainlight2 = SnowBlossom(im.MatrixColor("effects/snowflake.png", im.matrix.brightness(-.9)*im.matrix.tint(255, 20, 147)), 500, 20, (10, 15), (50, 15000), fast=True)
image snow:
    contains:
        "snow2"
        zoom 0.5
        alpha 0.3
    contains:
        "snow2"
        alpha 0.7
    contains:
        "snow2"
        zoom 2.0
        alpha 0.5
    contains:
        "snow2"
        zoom 2.0
        alpha 0.5
    contains:
        "snow2"
        zoom 3.0
        alpha 0.4
    contains:
        "snow2"
        zoom 7.0
        alpha 0.3
    contains:
        "snow2"
        zoom 10.0
        alpha 0.2
        
image snowlighter:
    contains:
        "snowlight2"
        zoom 2.0
        alpha 0.05
    contains:
        "snowlight2"
        zoom 3.0
        alpha 0.1
    contains:
        "snowlight2"
        zoom 5.0
        alpha 0.2
    contains:
        "snowlight2"
        zoom 6.0
        alpha 0.2
    contains:
        "snowlight2"
        zoom 7.0
        alpha 0.2
    contains:
        "snowlight2"
        zoom 10.0
        alpha 0.2
        
image rainlighter:
    contains:
        "rainlight2"
        zoom 5.0
        alpha 0.3
    contains:
        "rainlight2"
        zoom 6.0
        alpha 0.2
    contains:
        "rainlight2"
        zoom 7.0
        alpha 0.1
    contains:
        "rainlight2"
        zoom 10.0
        alpha 0.1
        
image snowlight:
    contains:
        "snowlight2"
        zoom 0.5
        alpha 0.3
    contains:
        "snowlight2"
        alpha 0.4
    contains:
        "snowlight2"
        zoom 2.0
        alpha 0.3
    contains:
        "snowlight2"
        zoom 2.0
        alpha 0.4
    contains:
        "snowlight2"
        zoom 3.0
        alpha 0.4
    contains:
        "snowlight2"
        zoom 7.0
        alpha 0.3
    contains:
        "snowlight2"
        zoom 10.0
        alpha 0.2        
        
image blackbars:
    additive 1.0
    contains:
        "gui/black_bars2.png"
        alpha 0.1
        linear 5.0 alpha 0.2
        linear 5.0 alpha 0.1
        2.0
        repeat

image mist: 
    additive 0.4
    "effects/mist1.png" with Dissolve(1.5, alpha=True)
    4.0
    "effects/mist2.png" with Dissolve(1.5, alpha=True)
    4.0
    "effects/mist3.png" with Dissolve(1.5, alpha=True)
    4.0
    "effects/mist2.png" with Dissolve(1.5, alpha=True)
    4.0
    "effects/mist3.png" with Dissolve(1.5, alpha=True)
    4.0
    "effects/mist2.png" with Dissolve(1.5, alpha=True)
    4.0
    repeat        
        
image cave 1:
    contains:
        "caveglow"
        alpha 0.5
    contains:
        "cavewoman1"
        alpha 1.1
        linear 1.0 alpha 1.1
        linear 1.0 alpha 1.5
        linear 1.0 alpha 1.1
        repeat
image cave 2:
    contains:
        "caveglow"
        alpha 0.5
    contains:
        "cavewoman2"
        alpha 1.1
        linear 1.0 alpha 1.1
        linear 1.0 alpha 1.5
        linear 1.0 alpha 1.1
        repeat
    contains:
        "caveman1"
        alpha 1.1
        linear 1.0 alpha 1.1
        linear 1.0 alpha 1.5
        linear 1.0 alpha 1.1
        repeat      
image cave 3:
    contains:
        "caveglow"
        alpha 0.5
    contains:
        "cavewoman2"
        alpha 1.1
        linear 1.0 alpha 1.1
        linear 1.0 alpha 1.5
        linear 1.0 alpha 1.1
        repeat
    contains:
        "caveman2"
        alpha 1.1
        linear 1.0 alpha 1.1
        linear 1.0 alpha 1.5
        linear 1.0 alpha 1.1
        repeat
    contains:
        "home1"
        alpha 1.1
        linear 1.0 alpha 1.1
        linear 1.0 alpha 1.5
        linear 1.0 alpha 1.1
        repeat
image cave 4:
    contains:
        "caveglow"
        alpha 0.5
    contains:
        "cavewoman3"
        alpha 1.1
        linear 1.0 alpha 1.1
        linear 1.0 alpha 1.5
        linear 1.0 alpha 1.1
        repeat
    contains:
        "caveman4"
        alpha 1.1
        linear 1.0 alpha 1.1
        linear 1.0 alpha 1.5
        linear 1.0 alpha 1.1
        repeat
image cave 5:
    contains:
        "caveglow"
        alpha 0.5
    contains:
        "thunderbird"
        alpha 1.1
        linear 1.0 alpha 1.1
        linear 1.0 alpha 1.5
        linear 1.0 alpha 1.1
        repeat
image cave 6:
    contains:
        "caveglow"
        alpha 0.5
    contains:
        "cavewoman2"
        alpha 1.1
        linear 1.0 alpha 1.1
        linear 1.0 alpha 1.5
        linear 1.0 alpha 1.1
        repeat
    contains:
        "caveman3"
        alpha 1.1
        linear 1.0 alpha 1.1
        linear 1.0 alpha 1.5
        linear 1.0 alpha 1.1
        repeat
    contains:
        "spear1"
        alpha 1.1
        linear 1.0 alpha 1.1
        linear 1.0 alpha 1.5
        linear 1.0 alpha 1.1
        repeat
image cave 7:
    contains:
        "caveglow"
        alpha 0.5
    contains:
        "snake"
        alpha 1.1
        linear 1.0 alpha 1.1
        linear 1.0 alpha 1.5
        linear 1.0 alpha 1.1
        repeat
image cave 8:
    contains:
        "caveglow"
        alpha 0.5
    contains:
        "cavewoman2"
        alpha 1.1
        linear 1.0 alpha 1.1
        linear 1.0 alpha 1.5
        linear 1.0 alpha 1.1
        repeat
    contains:
        "snake2"
        alpha 1.1
        linear 1.0 alpha 1.1
        linear 1.0 alpha 1.5
        linear 1.0 alpha 1.1
        repeat
image cave 9:
    contains:
        "caveglow"
        alpha 0.5
image cavewoman1:
    additive 1.0
    contains:
        xalign 0.5
        yalign 0.5
        "cave/woman1.png"
        0.2
        "cave/woman2.png"
        0.2
        "cave/woman3.png"
        0.2
        repeat
image thunderbird:
    additive 1.0
    contains:
        xalign 0.6
        yalign 0.5
        "cave/thunderbird1.png"
        0.2
        "cave/thunderbird2.png"
        0.2
        "cave/thunderbird3.png"
        0.2
        repeat
image snake:
    additive 1.0
    contains:
        xalign 0.6
        yalign 0.6
        "cave/snake1.png"
        0.2
        "cave/snake2.png"
        0.2
        "cave/snake3.png"
        0.2
        repeat
image snake2:
    additive 1.0
    contains:
        xalign 1.2
        xanchor 1.0
        yalign 0.6
        "cave/snake1.png"
        0.2
        "cave/snake2.png"
        0.2
        "cave/snake3.png"
        0.2
        repeat
image cavewoman2:
    additive 1.0
    contains:
        xalign 0.3
        yalign 0.5
        "cave/woman1.png"
        0.2
        "cave/woman2.png"
        0.2
        "cave/woman3.png"
        0.2
        repeat
image cavewoman3:
    additive 1.0
    contains:
        xalign 0.4
        yalign 0.55
        rotate -10
        "cave/crouch1.png"
        0.2
        "cave/crouch2.png"
        0.2
        "cave/crouch3.png"
        0.2
        repeat
image caveman1:
    additive 1.0
    contains:
        xalign 0.7
        yalign 0.5
        "cave/man1.png"
        0.2
        "cave/man2.png"
        0.2
        "cave/man3.png"
        0.2
        repeat
image caveman2:
    additive 1.0
    contains:
        xalign 0.5
        yalign 0.5
        "cave/man1.png"
        0.2
        "cave/man2.png"
        0.2
        "cave/man3.png"
        0.2
        repeat
image caveman3:
    additive 1.0
    contains:
        xalign 0.7
        yalign 0.7
        rotate 80
        "cave/man1.png"
        0.2
        "cave/man2.png"
        0.2
        "cave/man3.png"
        0.2
        repeat
image caveman4:
    additive 1.0
    contains:
        xalign 0.6
        yalign 0.7
        rotate -80
        xzoom -1
        "cave/man1.png"
        0.2
        "cave/man2.png"
        0.2
        "cave/man3.png"
        0.2
        repeat
image spear1:
    additive 1.0
    contains:
        xalign 0.7
        yalign 0.5
        "cave/spear1.png"
        0.2
        "cave/spear2.png"
        0.2
        "cave/spear3.png"
        0.2
        repeat
image home1:
    additive 1.0
    contains:
        xalign 0.8
        yalign 0.5
        "cave/home1.png"
        0.2
        "cave/home2.png"
        0.2
        "cave/home3.png"
        0.2
        repeat    
image caveglow:
    additive 1.0
    contains:
        xalign 0.5
        yalign 0.5
        "cave/glow1.png"
        0.2
        "cave/glow2.png"
        0.2
        "cave/glow3.png"
        0.2
        repeat
        
########################################################
##### M A I N   M E N U ###################################
########################################################
image menuback:
    contains:
        "fieldback"
    contains:
        "heavyrain"
    contains:
        "britflag"
    contains:
        "gui/black_bars.png"
    contains:
        "blackbars"
        
image rainfall:
    "rainfall1"
    alpha 0.7
    
image rainfall1:
    additive 0.5
    contains:
        alpha 0.25
        zoom 1.07
        xalign 0.5
        yalign 0.5
        "rainfall/rain1.jpg"
        0.07
        xalign 0.482
        "rainfall/rain2.jpg"
        0.07
        xalign 0.464
        "rainfall/rain3.jpg"
        0.07
        xalign 0.446
        "rainfall/rain4.jpg"
        0.07
        xalign 0.428
        "rainfall/rain5.jpg"
        0.07
        xalign 0.41
        "rainfall/rain6.jpg"
        0.07
        xalign 0.392
        "rainfall/rain7.jpg"
        0.07
        xalign 0.374
        "rainfall/rain8.jpg"
        0.07
        xalign 0.356
        "rainfall/rain9.jpg"
        0.07
        xalign 0.338
        "rainfall/rain10.jpg"
        0.07
        xalign 0.32
        "rainfall/rain11.jpg"
        0.07
        xalign 0.302
        "rainfall/rain12.jpg"
        0.07
        xalign 0.284
        "rainfall/rain13.jpg"
        0.07
        xalign 0.266
        "rainfall/rain14.jpg"
        0.07
        xalign 0.248
        "rainfall/rain15.jpg"
        0.07
        xalign 0.23
        "rainfall/rain16.jpg"
        0.07
        xalign 0.212
        "rainfall/rain17.jpg"
        0.07
        xalign 0.194
        "rainfall/rain18.jpg"
        0.07
        xalign 0.176
        "rainfall/rain19.jpg"
        0.07
        xalign 0.158
        "rainfall/rain20.jpg"
        0.07
        xalign 0.140
        "rainfall/rain21.jpg"
        0.07
        repeat
    contains:
        alpha 0.25
        zoom 1.07
        yalign 0.5
        xalign 0.374
        "rainfall/rain8.jpg"
        0.07
        xalign 0.356
        "rainfall/rain9.jpg"
        0.07
        xalign 0.338
        "rainfall/rain10.jpg"
        0.07
        xalign 0.32
        "rainfall/rain11.jpg"
        0.07
        xalign 0.302
        "rainfall/rain12.jpg"
        0.07
        xalign 0.284
        "rainfall/rain13.jpg"
        0.07
        xalign 0.266
        "rainfall/rain14.jpg"
        0.07
        xalign 0.248
        "rainfall/rain15.jpg"
        0.07
        xalign 0.23
        "rainfall/rain16.jpg"
        0.07
        xalign 0.212
        "rainfall/rain17.jpg"
        0.07
        xalign 0.194
        "rainfall/rain18.jpg"
        0.07
        xalign 0.176
        "rainfall/rain19.jpg"
        0.07
        xalign 0.158
        "rainfall/rain20.jpg"
        0.07
        xalign 0.140
        "rainfall/rain21.jpg"
        0.07
        xalign 0.5
        "rainfall/rain1.jpg"
        0.07
        xalign 0.482
        "rainfall/rain2.jpg"
        0.07
        xalign 0.464
        "rainfall/rain3.jpg"
        0.07
        xalign 0.446
        "rainfall/rain4.jpg"
        0.07
        xalign 0.428
        "rainfall/rain5.jpg"
        0.07
        xalign 0.41
        "rainfall/rain6.jpg"
        0.07
        xalign 0.392
        "rainfall/rain7.jpg"
        0.07
        repeat
    contains:
        alpha 0.25
        zoom 1.07
        yalign 0.5
        xalign 0.266
        "rainfall/rain14.jpg"
        0.07
        xalign 0.248
        "rainfall/rain15.jpg"
        0.07
        xalign 0.23
        "rainfall/rain16.jpg"
        0.07
        xalign 0.212
        "rainfall/rain17.jpg"
        0.07
        xalign 0.194
        "rainfall/rain18.jpg"
        0.07
        xalign 0.176
        "rainfall/rain19.jpg"
        0.07
        xalign 0.158
        "rainfall/rain20.jpg"
        0.07
        xalign 0.140
        "rainfall/rain21.jpg"
        0.07
        xalign 0.5
        "rainfall/rain1.jpg"
        0.07
        xalign 0.482
        "rainfall/rain2.jpg"
        0.07
        xalign 0.464
        "rainfall/rain3.jpg"
        0.07
        xalign 0.446
        "rainfall/rain4.jpg"
        0.07
        xalign 0.428
        "rainfall/rain5.jpg"
        0.07
        xalign 0.41
        "rainfall/rain6.jpg"
        0.07
        xalign 0.392
        "rainfall/rain7.jpg"
        0.07
        xalign 0.374
        "rainfall/rain8.jpg"
        0.07
        xalign 0.356
        "rainfall/rain9.jpg"
        0.07
        xalign 0.338
        "rainfall/rain10.jpg"
        0.07
        xalign 0.32
        "rainfall/rain11.jpg"
        0.07
        xalign 0.302
        "rainfall/rain12.jpg"
        0.07
        xalign 0.284
        "rainfall/rain13.jpg"
        0.07
        repeat     
        
image britflag:
    contains:
        alpha 0.2
        "flag/19.jpg"
        0.07
        "flag/20.jpg"
        0.07
        "flag/21.jpg"
        0.07
        "flag/22.jpg"
        0.07
        "flag/23.jpg"
        0.07
        "flag/24.jpg"
        0.07
        "flag/25.jpg"
        0.07
        "flag/26.jpg"
        0.07
        "flag/27.jpg"
        0.07
        "flag/28.jpg"
        0.07
        "flag/29.jpg"
        0.07
        "flag/30.jpg"
        0.07
        "flag/31.jpg"
        0.07
        "flag/32.jpg"
        0.07
        "flag/33.jpg"
        0.07
        "flag/34.jpg"
        0.07
        "flag/35.jpg"
        0.07
        "flag/36.jpg"
        0.07
        "flag/37.jpg"
        0.07
        "flag/38.jpg"
        0.07
        "flag/39.jpg"
        0.07
        "flag/40.jpg"
        0.07
        "flag/41.jpg"
        0.07
        "flag/42.jpg"
        0.07
        "flag/43.jpg"
        0.07
        "flag/44.jpg"
        0.07
        "flag/45.jpg"
        0.07
        "flag/46.jpg"
        0.07
        "flag/47.jpg"
        0.07
        "flag/48.jpg"
        0.07
        "flag/49.jpg"
        0.07
        "flag/50.jpg"
        0.07
        "flag/51.jpg"
        0.07
        "flag/52.jpg"
        0.07
        "flag/53.jpg"
        0.07
        "flag/54.jpg"
        0.07
        "flag/55.jpg"
        0.07
        "flag/56.jpg"
        0.07
        "flag/57.jpg"
        0.07
        "flag/58.jpg"
        0.07
        "flag/59.jpg"
        0.07
        "flag/60.jpg"
        0.07
        "flag/61.jpg"
        0.07
        "flag/62.jpg"
        0.07
        "flag/63.jpg"
        0.07
        "flag/64.jpg"
        0.07
        "flag/65.jpg"
        0.07
        "flag/66.jpg"
        0.07
        "flag/67.jpg"
        0.07
        "flag/68.jpg"
        0.07
        "flag/69.jpg"
        0.07
        "flag/70.jpg"
        0.07
        "flag/71.jpg"
        0.07
        repeat

########################################################
##### E X T R A S ########################################
########################################################        
image splash = "gui/logo.png"
image cds = "gui/cds.png"
image seycara = "gui/sey_logo.jpg"
image transparent = "gui/transparent2.png"
image white = Solid(color("#ffffff"))
image ctc :
    xpos 0.95
    ypos 0.95
    xanchor 0
    yanchor 0
    contains:
        "gui/ctc.png"
        alpha 1.0
        linear 2.0 alpha 0.3
        linear 2.0 alpha 1.0
        repeat

init python:
    config.skip_indicator = None
        
########################################################
##### T R A N S I T I O N S #################################
########################################################    
define dissolve2 = Dissolve(4.0)
define dissolve3 = Dissolve(10.0)
define dissolve4 = Dissolve(2.0)
define dissolve5 = Dissolve(8.0)
define dissolve6 = Dissolve(0.2)
define dissolve7 = Dissolve(1.0)
define flash = Fade(.25, 0, .75, color="#fff")
define circleirisout = ImageDissolve("effects/id_circleiris.png", .2, 8)
########################################################
##### P O S I T I O N S ####################################
########################################################
define rightend = Position(xpos=1.0)
define right05 = Position(xpos=0.92)
define right1 = Position(xpos=0.9)
define right12 = Position(xpos=0.88)
define right15 = Position(xpos=0.85)
define right2 = Position(xpos=0.8)
define right25 = Position(xpos=0.75)
define right27 = Position(xpos=0.725)
define right3 = Position(xpos=0.7)
define right37 = Position(xpos=0.625)
define right35 = Position(xpos=0.65)
define right4 = Position(xpos=0.6)
define right45 = Position(xpos=0.55)
define left05 = Position(xpos=0.08)
define left1 = Position(xpos=0.1)
define left12 = Position(xpos=0.12)
define left15 = Position(xpos=0.15)
define left17 = Position(xpos=0.17)
define left2 = Position(xpos=0.2)
define left25 = Position(xpos=0.25)
define left3 = Position(xpos=0.3)
define left35 = Position(xpos=0.35)
define left37 = Position(xpos=0.37)
define left4 = Position(xpos=0.4)
define left45 = Position(xpos=0.45)  
define layover = Position(xpos=0.51, ypos=0.5, xanchor='center', yanchor='center')
define pickup = Position(xpos=0.5, ypos=1.1)
########################################################
##### S O U N D   C H A N N E L S ###########################
########################################################
init python:    
    renpy.music.register_channel("soundfx", "sfx", True)
    renpy.music.register_channel("soundfx2", "sfx", True)
    renpy.music.register_channel("soundfx3", "sfx", True)
    renpy.music.register_channel("soundfx4", "sfx", True)
    renpy.music.register_channel("soundfx5", "sfx", True)
    renpy.music.register_channel("sound2", "sfx", False)
    renpy.music.register_channel("sound3", "sfx", False)
    renpy.music.register_channel("sound4", "sfx", False)
    renpy.music.register_channel("sound5", "sfx", False)
    def silhouette_matrix (r,g,b,a=1.0):
        return im.matrix((0, 0, 0, 0, r, 
                               0, 0, 0, 0, g,
                               0, 0, 0, 0, b,
                               0, 0, 0, a, 0,))
    def silhouetted (filename, r,g,b, a = 1.0):                               
        return im.MatrixColor (Image (filename), silhouette_matrix (r,g,b,a))

########################################################
##### S P L A S H S C R E E N ##############################
########################################################
label splashscreen:
    $ renpy.block_rollback()
    scene black
    $ renpy.pause(0, hard=True)
    $ renpy.start_predict("menuback", "britflag")
    $ mouse_visible = False
    scene white with fade
    show splash at layover with dissolve
    play sound "se/hiyah.ogg"
    $ renpy.pause(3.0, hard=True)
    hide splash with dissolve
    scene white with fade
    show cds at layover with dissolve
    $ renpy.pause(3.0, hard=True)
    hide cds with dissolve
    scene black
    with fade
    play sound "se/seycara.ogg"
    scene seycara
    with dissolve
    $ renpy.pause(3.0, hard=True)
    scene black
    with fade
    pause 1.0
    show expression Text(_("{i}Over The Hills And Far Away{/i} является коммерческой собственностью студии {i}WarGirl Games{/i}.\nИстория и персонажи, представленные в игре, являются интеллектуальной собственностью разработчиков.\nВсе персонажи, появляющиеся в данном произведении, вымышлены.\nЛюбые совпадения с реально существующими людьми, живыми или умершими, являются случайными.\n \nВ игре присутствуют сцены с ненормативной лексикой, кровью и насилием.\nРекомендуется осторожность при прохождении. \n \n \n \n \n \n \n \n \n \n \n \n \n{size=12}© 2015 WarGirl Games, All Rights Reserved, Over The Hills And Far Away and all elements thereof{/size}"), size=17, yalign=0.87, kerning=4, color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve
    pause 8.0
    hide expression Text(_("{i}Over The Hills And Far Away{/i} is the commercial property of {i}WarGirl Games{/i}.\nThe story and characters contained within are the intellectual property\nof the developers. All characters appearing in this work are fictitious.\nAny resemblance to real persons, living or dead, is purely coincidental.\n \nThis game contains scenes with Strong Language, Blood and Violence.\nPlayer discretion is advised."), size=17, yalign=0.5, kerning=4, color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve
    play soundfx "se/rainbattle.ogg" fadein 10.0
    pause 0.5
    scene menuback
    with dissolve
    $ mouse_visible = True
    return
    
    
    

########################################################
##### G A M E   S T A R T #################################
########################################################
label start:
    $ store.text_history_enabled = True
    $_game_menu_screen = "preferences"
    $ mouse_visible = False
    $ renpy.stop_predict("britflag")
    stop soundfx fadeout 3.0
    stop music fadeout 3.0
    scene black
    with dissolve2
    pause 1.0
    show expression Text(_("{i}Когда придёт твой час встретить смерть — стой гордо.\nНе будь, как те, кто дрожит от страха и молится\nо лишнем мгновении жизни. Встреть свой конец с песней\nв сердце и смелостью в глазах —\nкак герой, возвращающийся домой.{/i}\n\n{size=18}- Tecumseh{/size}"), size=20, yalign=0.5, kerning=4, color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve4
    play soundfx "se/rain.ogg" fadein 20.0
    play soundfx3 "se/mud.ogg" fadein 10.0
    pause 8.0
    hide expression Text(_("{i}When it comes your time to die, be not like those whose hearts\nare filled with the fear of death, so that when their time comes\nthey weep and pray for a little more time to live their lives\nover again in a different way. Sing your death song and die\nlike a hero going home.{/i}\n\n{size=18}- Tecumseh{/size}"), size=20, yalign=0.5, kerning=4, color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve4
    pause 2.0
    show expression Text(_("Северо-Западная граница"), size=20, yalign=0.5, kerning=4, color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve
    pause 2.0
    hide expression Text(_("The Northwest Frontier"), size=20, yalign=0.5, kerning=4, color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve
    pause 1.0
    show expression Text(_("12 Октября, 1813г."), size=20, yalign=0.5, kerning=4, color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve
    pause 2.0
    hide expression Text(_("October 12th, 1813"), size=20, yalign=0.5, kerning=4, color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve
    pause 1.0
    window show
    $ mouse_visible = True
    
    "Небо потемнело, а холодный снег с дождём бьёт в лицо."
    "Эти пустые земли — дикие и продуваемые ветром."
    "Путь будет нелёгким ... и никто не знает, вернусь ли я прежним."
    "Подхваченный ветром орёл кружит над головой и улетает на юг."
    "Я иду сквозь грязь под дождём, надеясь найти хоть какое-то укрытие."
    
    window show
    scene field
    with dissolve4
    play music "music/aflight.ogg"
    
    "Один средь дикой местности я пробираюсь сквозь высокую траву на поле боя."
    "Красные и синие мундиры лежат в грязи, их тела погружаются в топкую землю."
    "Их винтовки стоят воткнутые в землю, направленные в небо."
    "Дешёвая замена надгробию. Расточительство оружия, если спросить меня ..."
    "Считая трупы, я понимаю, что это должна была быть засада или небольшой бой."
    "Возможно, это были военнопленные, направлявшиеся в американский лагерь."
    "А может, это были дезертиры?"
    "Я продолжаю идти сквозь колючие заросли и лужи, углубляясь в поле боя."
    "Мох и сорняки прилипают к моим сапогам, а сырой грунт тянет ноги под себя."
    "Проходя мимо одного трупа за другим, я невольно заглядываю в сумки и карманы на предмет еды или припасов."
    "Но удача не на моей стороне."
    "Эти солдаты уже были обобраны до того, как их оставили гнить под ледяным дождём."
    
    stop soundfx3 fadeout 1.0
    
    "Я медленно остановился на небольшом холме на краю поля."
    "Дождь продолжает идти."
    "Должен ли я следовать дальше?"
    "Чем ближе я к югу, тем меньше шансов вернуться ..."
    "Я оглядываюсь назад на долину."
    "Последний наш приказ об отступлении не оставил нам особых указаний."
    me ". . . {i}Берлингтон{/i} . . ."
    "Что-то насчёт {i}Берлингтона{/i}. Отступающие направлялись к расположенному там британскому лагерю."
    "Я стою, смотря вдаль."
    
    $ mouse_visible = False
    scene cg7
    with dissolve4
    pause 0.2
    $ mouse_visible = True
    
    "Я Уильям Обри из 41-го пехотного полка."
    "После боя на севере, на реке {i}Темзе{/i}, я бежал на юго-запад и переправился через реку {i}Детройт{/i}."
    "Теперь, глубоко на вражеской территории, я направляюсь на юг через территорию {i}Мичиган{/i}."
    "Куда я пойду отсюда? Не знаю ..."
    "Если бы британцы нашли меня в таком состоянии, как сейчас, меня бы непременно расстреляли за измену."
    "Живущий в лесу, трус и предатель короны."
    "До сих пор я не высовывался и скитался из одного убежища в другое."
    "Рыская, как дворняга, я не имел другого выбора, кроме как грабить и вторгаться в чужие владения."
    me ". . . Мне следовало бы продолжать двигаться . . ."
    "Мне уже не повернуть назад. Если уж дезертировать, то лучше бежать как можно дольше."
    "Возможно, я найду американский полк, который ищет новых рекрутов."
    me ". . . Нет . . . Нет, я покончил с войной . . ."
    "К такой жизни я не вернусь. Мне больше нет места на службе в армии."
    "Я не люблю ни короля, ни Новую Республику."
    "Я хочу лишь найти свой дом. Быть свободным человеком, найти своё счастье."
    "В конце концов, чего здесь можно добиться?"
    "Славы? Свободы? Земли?"
    "Здесь нет военной добычи для пушечного мяса."
    "Либо оставят гнить пленником, либо повесят, либо снова заставят сражаться под началом таких людей, как Проктер ..."
    "Я готов рискнуть, стать свободным человеком ..."
    
    play soundfx3 "se/mud.ogg"
    
    "Я снова начинаю идти, мои ботинки постепенно покрываются грязью."
    
    scene black
    with dissolve
    pause 1.0
    show rainfall
    with dissolve
    
    "Пробираясь через долины, я наконец замечаю небольшой амбар посреди поля."
    "Кажется, он заброшен, и я начинаю торопливо идти к нему."
    "Прожив почти неделю в глуши, я нуждаюсь в каком-нибудь укрытии."
    "Рассеянно кладу руку на плечо, пока иду, и чувствую боль в своей ране."
    "В лесу во время последнего боя меня ранили из мушкета."
    "После первых нескольких дней я почти не заметил этого, но после ночёвки в грязи рана начала кровоточить ..."
    
    stop soundfx3 fadeout 1.0
    
    "Вскоре я остановился у старого амбара."
    "Грязная хижина еле стоит, но я чувствую запах сухого сена внутри. Пока пойдёт."
    "Глядя на деревянную дверь, я тянусь к ручке, но не хватаю её."
    "За металлическую перекладину зацеплена тонкая веревка, привязывающая дверь к стене амбара."
    me ". . . Нож . . ."
    
    play sound2 "se/brush.ogg"
    
    "Засунув руку в сапог, я хватаю спрятанный клинок и вытаскиваю его."
    "Я поворачиваю грязное оружие в руке, разглядывая сломанную рукоять."
    
    play sound3 "se/wood.ogg"
    
    "Затем я медленно распилил веревку: тонкая нить разорвалась на две части."
    
    stop sound3 fadeout 1.0
    
    "Убирая нож в сапог, я вдруг подумал: возможно, я на чужой земле."
    "В этом амбаре может быть кто угодно."
    "Американский солдат с винтовкой ... Туземный мятежник с томагавком ..."
    "Или фермер, злящийся на меня за то, что я вторгся на его землю ..."
    "Я перекидываю ремень мушкета через плечо и беру оружие в руки."
    "В конце концов, лучше быть готовым к таким вещам."
    "Я подхожу и начинаю тянуть дверь амбара, пытаясь ее открыть."
    "Опираясь на деревянную раму, я хватаюсь за ручку и тяну."
    "Деревянная доска медленно начинает сдвигаться с места."
    
    stop soundfx fadeout 3.0
    stop music fadeout 7.0
    play soundfx2 "se/rain_in.ogg"
    play sound2 "se/barndoor.ogg"
    scene black
    with flash
    
    "Когда дверь амбара распахивается, я быстро вваливаюсь внутрь — в затхлое убежище."
    "Моим глазам требуется несколько секунд, чтобы привыкнуть к темноте."
    
    $ mouse_visible = False
    pause 0.5
    play music "music/first_encounter.ogg"
    window hide
    scene cg1
    with dissolve2
    pause 2.0
    window show
    $ mouse_visible = True
    $ achievement.grant("NEW_ACHIEVEMENT_1_0")
    
    "И как только это происходит, я сталкиваюсь со странным зрелищем ..."
    
    play sound2 "se/cock.ogg"
    play sound3 "se/gundrop.ogg"
    scene cg1
    with hpunch
    
    "Инстинктивно я поднимаю ствол мушкета и принимаю оборонительную стойку."
    "Похоже, это невысокая девочка — туземный ребёнок."
    "Она не может представлять особой угрозы."
    "Но внешность бывает очень обманчива ..."
    "Продолжив держать оружие наготове, я присматриваюсь."
    "На её голове синяя повязка, украшенная узорами."
    "Шаль на плечах в тон, а платье более земных тонов."
    "Темно-черные волосы заплетены по бокам в косички и завязаны на концах большими дисками, похожими на пуговицы."
    "Глаза карамельного цвета мало что выдают о том, о чем она думает."
    "На вид ей одиннадцать–двенадцать лет."
    "Хотя по ним трудно судить."
    "У неё свободная, расслабленная поза: она совсем не выглядит испуганной ..."
    "Хотя я и держу в руках мушкет, девочка ничего не делает."
    "Не плачет, не бежит, не улыбается ... Она просто смотрит на меня, как дурочка."
    "Густые брови и носик-пуговка дополняют образ, придавая ей довольно мальчишеский вид."
    
    play sound3 "se/mud.ogg"
    pause 0.2
    stop sound3 fadeout 3.0
    
    "Я делаю шаг вперед, держа кончик штыка мушкета у ее груди."
    "Наблюдая за её реакцией, я осторожно делаю жест, отгоняющий её."
    me ". . . Кыш! Катись! . . ."
    "Но она не двигается ..."
    
    play sound2 "se/cock.ogg"
    play sound3 "se/mud.ogg"
    pause 0.2
    stop sound3 fadeout 3.0
    
    "Итак, я делаю еще один шаг, на этот раз еще ближе к ней."
    "Она снова не двигается ..."
    "Я жду несколько секунд, чтобы посмотреть, не придёт ли ей в голову что-нибудь."
    "Осознает ли она вообще, что я представляю угрозу?"
    "Но девушка лишь смотрит на меня, словно я всего лишь бродячее животное."
    "В её выражении нет злобы, только не мигающее любопытство ..."
    me ". . . {i}Хааа{/i} . . ."
    "Эта ситуация безнадёжна."
    "Отказавшись от попыток запугать её, я встаю по стойке смирно и оставляю мушкет висеть на плече."
    
    scene barn
    with dissolve
    
    "Я осматриваю амбар."
    "На земляном полу лежит утоптанная солома. Её осталось достаточно, чтобы соорудить удобную подстилку."
    "Земля выглядит довольно твёрдой, но кое-где образовались лужи."
    "Толстые балки поддерживают тонкую крышу из деревянных панелей, которая едва защищает от грозы."
    "Из дыр в планках капает вода, подтверждая, что здесь давно не убирались."
    "Дверь на противоположной стене сорвана с петель, открывая вид на дождь снаружи."
    me ". . . Какая свалка . . ."
    "Старые пыльные ящики и коробки свалены у одной стороны навеса вместе с несколькими любопытными предметами."
    "Вазы разных форм, свернутые ковры, старый пергамент, сломанные солнечные часы, стеклянные бутылки ..."
    "Бывший владелец, вероятно, выбросил свои самые бесполезные вещи и перебрался в более безопасное место."
    
    scene cg1
    with dissolve4
    
    "Возвращаясь к маленькой девочке, я размышляю вслух:"
    me ". . . Молодая туземная девочка, одна в дикой природе, в сарае во время шторма . . ."
    "Может, она {i}идиотка{/i}?"
    "Вы слышали истории о белых родителях, бросающих своих детей в глуши."
    "Не желают брать на себя бремя воспитания не очень умного ребенка."
    me ". . . Не думал, что туземцы тоже так делают . . ."
    "Нужно быть идиотом, чтобы не бояться солдата с ружьем!"
    "Ее любопытный взгляд застыл."
    
    play sound3 "se/mud.ogg"
    pause 0.2
    stop sound3 fadeout 3.0
    
    "Я подхожу еще ближе, на этот раз встав прямо рядом с ней."
    "Оглядывая ее с ног до головы, я бормочу себе под нос:"
    me ". . . Девушка из племени {i}Шауни{/i}? . . ."
    girl ". . . {i}Шауни{/i} . . ."
    
    play sound2 "se/collapse.ogg"
    play sound3 "se/plop.ogg"
    scene black
    show barn
    with vpunch
    with hpunch
    scene barn
    
    me "Ага!"
    "Я падаю на задницу, хлюпая в грязь."
    "Ее ответ застал меня врасплох. Я не ожидал, что она ответит!"
    me ". . . Фууу . . ."
    
    play sound2 "se/brush.ogg"
    show mai sad
    with dissolve
    
    "Медленно поднимаясь с земли, я отряхиваю с ягодиц солому и грязь."
    me ". . . Ты Шауни? . . ."
    girl ". . . ... . . ."
    "Молчит."
    me ". . . Ты слышала? . . ."
    "Снова молчит."
    "Потом ..."
    
    show mai normal
    with dissolve
    
    girlshawnee ". . . {rb}{i}Леннавэ Нилла.{/i}{/rb}{rt}(Я Шауни){/rt} . . ."
    "{i}Леннавэ Нилла{/i} ... это значит {i}'Шауни'{/i}"
    "Я знаю этот язык лишь отчасти, потому что служил с ними в полку."
    me ". . . Забудь, как говорят индейцы. Ты знаешь английский язык? . . ."
    "Ответа не последовало."
    me ". . . Хорошо . . ."
    "Я кладу руку на рукоять мушкета, но она не сводит взгляда."
    
    stop music fadeout 5.0
    
    me ". . . Что ты здесь делаешь? . . ."
    "Она с любопытством смотрит на меня, прежде чем указать в отверстие на шторм снаружи."
    girl ". . . {i}Папапанаве.{/i} . . ."
    me ". . . Что? . . ."
    "Она продолжает указывать на дождь."
    "До меня начинает доходить, что она имеет в виду, хотя я еще не слышу ее слов ..."
    "{i}Жду, когда шторм закончится.{/i}"
    
    $ mouse_visible = False
    stop soundfx2 fadeout 3.0
    scene black
    with dissolve4
    pause 2.0
    play music "music/memories.ogg"
    play soundfx "se/wind.ogg"
    scene flashback1
    with dissolve2
    $ mouse_visible = True
    
    "Много лет назад этот континент был охвачен кровавой и разрушительной войной."
    "В то время я был ещё мальчишкой."
    "Мой отец привез меня в Америку из Англии, чтобы я нашел свое счастье."
    "Он не знал о назревающем восстании и предстоящих сражениях."
    "Война началась, пока он работал ..."
    "Красные и синие мундиры боролись за контроль над этими землями."
    "Отец решил, что будет бороться ради меня."
    "Однажды он исчез, либо поверженный в ополчении, либо убитый за свои роялистские взгляды."
    "Меня приютили соседи."
    "Американская семья, слишком религиозная, чтобы позволить ребенку страдать на улицах Бостона."
    "Я вырос в юношу, окруженный кровью, риторикой и разрухой."
    "По мере того как война продолжалась, я терял интерес к другому, правильному пути."
    "Я пытался хоть как-то заработать, но мне пришлось поступать неправильно. Это был совсем другой путь ..."
    
    scene flashback2
    with dissolve4
    
    "Некоторое время я был партнером янки, преступника, почти таким же, каким я был в те времена."
    "С грубияном по имени Уоррен Джексон."
    "Он, словно змея, соблазнил меня на порочную жизнь."
    "Пока люди боролись за свою независимость, мы в поисках счастья выбрали куда менее благородный путь."
    "Мы начали с малого, грабя дома и таунхаусы умерших ополченцев и политиков."
    "Революция принесла этим землям много горя и хаоса."
    "Многие мужчины тогда потеряли свои титулы и имущество."
    "Отсутствие эффективного правительства, враждебное ополчение и изгнание британцев ..."
    "Это был рай для преступников."
    "Мы с партнёром разбогатели на нажитом, пропивая и тратя на женщин всё до копейки."
    "Через несколько лет после окончания войны начались гонения независимых, таких как мы."
    "Людям обещали землю и свободу, если они будут бороться за независимость."
    "Но новая республика мало чем отличалась от старой."
    "Иногда мы брали оружие, бунтуя против новых налогов на наш виски."
    "Они хотели покарать нас за честно заработанную добычу!"
    "Это был не новый, анархический мир."
    "Он всё ещё принадлежал прежним землевладельцам."
    "Поэтому мой партнер обосновался в северной торговой фактории и написал мне, приглашая присоединиться."
    
    scene flashback1
    with dissolve4
    
    "Месяцами мы жили не лучше дикарей, охотясь, выслеживая и предлагая свои услуги."
    "Одной семье в глуши нужны были проводники, чтобы защитить их от туземцев и диких животных."
    "Многие из жителей таковы: они отчаянно желают стать свободными, найти клочок земли, который можно назвать своим."
    "Большинство из них были доверчивы и слабы. Но платили они достаточно хорошо."
    "Некоторые добирались до места назначения."
    "Большинству не так везло ..."
    "Мы с напарником уводили их с тропы в какой-нибудь безлюдный уголок дикой природы."
    "Тогда мы их избивали, грабили до нитки и оставляли на растерзание волкам."
    "Для большинства это были тяжёлые времена."
    "Тогда нас не очень заботила мораль ..."
    "Время шло; мы потихоньку наполняли свои кошельки, но выпивка потеряла вкус, а женщины ..."
    "Ну ... у меня пропало желание воровать у тех, у кого ничего нет."
    "Я хотел уйти."
    "Но мой партнер был не в восторге от этой идеи."
    
    scene flashback3
    with dissolve4
    
    "Мы сражались и сражались несколько дней, много раз доставая пистолеты и клинки."
    "В конце концов мы пришли к согласию и решили расстаться."
    "Когда мы расходились, мой напарник повернулся ко мне и крикнул:"
    "{i}'Скоро увидимся ...'{/i}"
    "После этого он скрылся в кустах."
    "Больше я о нём ничего не слышал ..."
    
    scene flashback1
    with dissolve4
    
    "Ах да, мы разделили добычу, и я отправился в порт, затем в Англию, навсегда отвернувшись от Нового Света."
    "Я покончил с этим континентом."
    "Мне пора было найти небольшой клочок земли и мирную жизнь."
    
    stop soundfx fadeout 5.0
    stop music fadeout 5.0
    
    "По крайней мере, я надеялся, что всё будет проще ..."
    
    $ mouse_visible = False
    scene black
    with dissolve4
    pause 2.0
    play soundfx2 "se/rain_in.ogg" fadein 3.0
    scene barn
    with dissolve4
    $ mouse_visible = True
    
    "Я сижу на краю сарая, прислонившись к деревянному столбу."
    "Пройдя несколько миль по открытой местности, мне нужно было перевести дух."
    "У меня нет сил разбираться с ... этим ..."
    
    play music "music/first_encounter.ogg"
    show mai normal
    with dissolve
    
    "Молодая девочка стоит на месте, глядя на меня."
    "Почему нельзя было покинуть это место?"
    "Всё, чего я хотел, — это немного отдохнуть от дождя."
    "Едва шевелясь, она всматривается в происходящее."
    me ". . . Что? . . ."
    "Она не отвечает"
    me ". . . Что такое? . . ."
    "Ответа всё равно нет."
    "Может быть, я её всё же напугал?"
    
    hide mai normal
    with dissolve
    
    "Во всяком случае, пока лучше ее игнорировать."
    "Это убежище подойдет для ночлега, плевать на нее."
    "Но что делать завтра?"
    "Куда мне идти отсюда? Мне нужен план."
    "Возможно, я найду дорогу к поселению на юг через холмы."
    "Хотя в такой одежде я постараюсь избегать главных дорог и фортов."
    "что еще ... что еще ..."
    "Конечно, провизия!"
    "Мне нужно собрать припасов в зависимости от того, насколько долгим будет моё путешествие."
    "Если я хочу сбежать от этой войны, мне придется нацелиться на какой-нибудь южный штат."
    "Путешествие на такое расстояние обойдется не дешево."
    "В таком случае придется найти работенку, чтобы заработать деньги."
    "Либо так, либо ограбить магазин и сбежать."
    "Может быть, даже торговать с одним из племен, если я смогу добраться до индейских земель?"
    "Может быть, добрый вождь соизволит сжалиться надо мной и даст мне бесплатное убежище?"
    me ". . . Да, кажется, это козырь в моём рукаве! . . ."
    
    show mai normal
    with dissolve
    
    "Кажется, девочка играет с каким-то кожаным мешочком."
    me ". . . Эй ... погоди-ка ... . . ."
    "Я проверяю бедро и обнаруживаю, что мой патронташ пропал."
    me ". . . Ах ты, маленькая негодяйка! Это моё! . . ."
    "Когда она его успела украсть?!"
    
    play sound5 "se/brush.ogg"
    
    "Не обращая внимания на мой возмущённый тон, девочка вытаскивает бумажный картридж и вертит его в руках."
    
    stop sound5 fadeout 2.0
    
    me ". . . Эй! Оставь это! . . ."
    "Пока я пытался встать, она разорвала пакет."
    
    play sound2 "se/rip.ogg"
    play sound3 "se/splash.ogg"
    show blacksmoke2           
    show mai worry
    with hpunch
    play sound4 "se/cough.ogg"
    show mai soot
    with dissolve
    
    "Облако пороха летит в лицо туземке."
    "У неё начинается приступ кашля."
    
    play sound4 "se/gundrop.ogg"
    
    "Она роняет коробку с патронами, которая с грохотом падает на землю."
    
    hide blacksmoke2
    with dissolve4
    
    "В конце концов девушка оказалась покрыта сажей."
    me ". . . Черт возьми! Вот почему я сказал тебе оставить это в покое! . . ."
    
    play sound3 "se/swipe.ogg"
    show mai soot
    with hpunch
    
    "Я хватаю испорченный патрон и поднимаю боеприпасы со земли."
    girl ". . . {i}Фффф{/i} . . ."
    "Девочка стонет, ведь порох попал ей в глаза."
    "Что с ней?"
    "Она что, не знает, что такое порох?"
    
    play sound3 "se/brush.ogg"
    pause 0.5
    stop sound3 fadeout 2.0
    
    "Девочка отряхивает платье руками, пытаясь убрать грязь."
    "Когда она вытирает сажу, вверх медленно поднимается черная пыль."
    
    play sound3 "se/sneeze.ogg"
    show mai soot
    with hpunch
    
    "И она снова чихает."
    me ". . . Так никогда не отмоешься . . ."
    
    show mai soot2
    with dissolve
    
    "Она останавливается и смотрит на меня."
    "Наклонившись, я указал на лужу на полу неподалёку."
    me ". . . Умойся дождевой водой . . ."
    girl ". . . ? . . ."
    me ". . . Это смоет большую часть пороха . . ."
    "Если ее оставить влажной, она не загорится."
    "То есть если она попадёт на искры ..."
    
    show mai soot
    with dissolve
    
    "После осторожного взгляда она опустила руки в лужу."
    
    play sound2 "se/wash.ogg"
    show mai gulp
    with dissolve4
    pause 1.0
    
    "Девочка медленно умывается мутной водой."
    "В конце концов черная сажа исчезает, и на ее месте появляется более или менее чистый цвет лица."
    
    show mai sad
    with dissolve
    
    me ". . . А теперь стой тихо и не трогай мои вещи . . ."
    "Я ругаю ее, но видимо, она не понимает ни слова из того, что я говорю."
    
    play sound3 "se/brush.ogg"
    pause 0.5
    stop sound3 fadeout 2.0
    
    "Схватив патронташ, я снова плюхнулся на стог сена."
    "Внутри всё ещё спрятана пуля."
    "Но без пороха патрон теперь практически бесполезен."
    me ". . . Всё равно . . ."
    "Никогда не знаешь, когда может пригодиться дополнительный пыж."
    "Я кладу оба предмета обратно в свой патронташ, который прикрепляю к поясу."
    
    show mai normal
    with dissolve
    
    "Обернувшись, я снова увидел, как девочка смотрит на меня."
    "Эти карамельные глаза следят за каждым моим движением."
    "Если подумать, мне, наверное, стоит быть осторожнее с этой девочкой."
    "Я даже не заметил, как она украла мои патроны."
    "Кто знает, что она ещё может выкинуть?"
    "Если я не буду осторожен, она может схватить мой нож или что-нибудь ещё ..."
    "Не спуская глаз с ребенка, я пытаюсь устроиться поудобнее."
    
    play sound3 "se/brush.ogg"
    pause 0.5
    stop sound3 fadeout 2.0
    
    "Когда я сажусь, я снова чувствую легкую боль. Рана болит ..."
    
    show mai worry
    with dissolve
    
    "Осторожно приспустив воротник куртки, я проверяю пулевое отверстие в руке."
    "Рана пока не загноилась, но если я не смогу в ближайшее время добраться до магазина или таверны ..."
    "Ну скажем так, прятаться под дождем и спать в грязи мне не поможет."
    "Засунув руку в карман куртки, я достаю фляжку."
    "Последняя порция рома. Мне определенно нужно добраться до таверны ..."
    
    play sound2 "se/drinking.ogg"
    
    "Я снимаю крышку и делаю глоток."
    
    stop sound2 fadeout 1.0
    play sound3 "se/wash.ogg"
    
    "Затем я наливаю немного рома на открытую ладонь и подношу ее к плечу."
    "Ром медленно стекает вниз и просачивается в рану."
    "Спирт жжёт, пока я прочищаю пулевое отверстие: кровь смешивается с ним и стекает."
    me "{i}. . . Аааа . . .{/i}"
    "Делаю легкие потирающие движения, не могу понять, улучшаю ли я ситуацию или усугубляю ее."
    "Но алкоголь в любом случае помогает."
    
    play sound2 "se/drinking.ogg"
    
    "Когда я тяжело вздыхаю и делаю ещё один глоток из фляжки, я замечаю, что девочка всё ещё наблюдает за мной."
    
    stop sound2 fadeout 1.0
    
    "С полным ртом рома я бормочу ..."
    me ". . . Что? Никогда раньше не видела, чтобы англичанин истекал кровью . . ."
    "Она ничего не говорит."
    me ". . . Не хочет говорить по-английски, эххх . . ."
    "Ничего."
    me ". . . Ну, меня это устраивает . . ."
    me "Не хочется мне говорить с туземной девчонкой."
    "Если уж мне суждено умереть здесь, то пусть лучше это будет мирно, с ромом под рукой ..."
    girlshawnee ". . . {rb}{i}Кине'ки ...{/i}{/rb}{rt}(Твоя рука ...){/rt} . . ."
    me ". . . А? . . ."
    
    play soundfx3 "se/mud.ogg"
    hide mai worry
    with dissolve
    stop soundfx3 fadeout 5.0
    play soundfx "se/rummage.ogg"
    
    "Девочка исчезает за кучей хлама по другую сторону сарая и начинает рыться в навозе."
    me ". . . Эй, что ты там делаешь? . . ."
    "Я зову ее, но ответа нет."
    me ". . . Зачем я вообще пытаюсь? . . ."
    
    play sound2 "se/drinking.ogg"
    
    "Я выпью ещё."
    
    stop sound2 fadeout 1.0
    
    "У меня хватит рома еще на день-два."
    "Лучше рассчитать."
    
    stop soundfx fadeout 1.0
    show mai sad
    with dissolve
    
    "Вскоре девочка появилась снова, сжимая в руке старый кусок ткани."
    
    play sound2 "se/mud.ogg"
    show mai sad large with dissolve
    show mai sad large at pickup with ease
    show mai sad large at center with ease
    stop sound2 fadeout 1.0
    
    "Она подходит ближе и опускается передо мной на колени."
    "Её платье упало в лужу у моих ног, пропитав ткань темно-коричневым оттенком."
    "Затем, открыв сумку, она достает оттуда небольшую баночку с каким-то кремом."
    "Девочка начинает промокать тряпку мазью, оставляя на ней пятна."
    "Должно быть, это какое-то травяное средство."
    "Арника ... или, может быть, женьшень ... возможно, что-то еще ..."
    "От крема исходит резкий запах."
    "Она указывает на мою рану, и до меня доходит, что она делает."
    "Неужели эта девчонка настолько глупа, чтобы пытаться мне помочь?"
    "Чувствуя, как возвращается жгучая боль в руке, я не в состоянии протестовать ..."
    me ". . . Лучше бы это не было ядовитым . . ."
    "Я бормочу."
    "Девочка заканчивает наносить крем на тряпку."
    
    play sound2 "se/swipe.ogg"
    show mai worry large
    with hpunch
    
    "Когда она наклоняется вперед с влажной тряпкой, я хватаю ее за предплечье и тяну к себе."
    me ". . . Во что ты играешь? . . ."
    "Взяв её руку в свою, переворачиваю, осматривая кожу."
    "Сначала она начинает отстраняться ..."
    me ". . . Стой спокойно . . ."
    
    show mai sad large
    with dissolve
    
    "Она не протестует, пока я осматриваю ее тело."
    "Осматривая ее ладони, плечи и ноги, я ищу какие-нибудь отметины."
    "У нее грубые руки, вероятно, стёртые от лазанья по деревьям и свежевания зайцев."
    "Множество разных браслетов звенят, пока я осматриваю ее с ног до головы."
    me ". . . Никаких отметин . . ."
    "Значит, она не беглая рабыня ..."
    "Эта теория отопала."
    "Так почему же она здесь?"
    me ". . . Что еще ты спрятала в этой сумке? . . ."
    
    play sound2 "se/swipe.ogg"
    show mai worry large with hpunch
    
    "Она пытается отстраниться, но я держу всё крепче."
    girlshawnee ". . . {rb}{i}Мат-тах ...  {/i}{/rb}{rt}(Нет ...){/rt} . . ."
    me ". . . Я же говорил тебе: прекрати говорить как индеец . . ."
    "Девочка снова замолкает."
    
    show mai sad large
    with dissolve
    
    "Постепенно я отпустил её, и она продолжила свою работу."
    
    play sound2 "se/rip.ogg"
    
    "Когда она начинает обматывать моё плечо грязной тряпкой, я морщусь — ткань вдавливается в открытую рану."
    "Надавливая на нее, я чувствую, как прохладный крем начинает втираться в пулевое отверстие."
    
    play sound3 "se/brush.ogg"
    pause 0.5
    stop sound3 fadeout 2.0
    
    "Тяжело завязав рану, девушка отступает, а я медленно поправляю рубашку."
    me ". . . {i}Аааа . . .{/i}"
    "Неприятно, когда мазь впитывается в кожу."
    "Девочка-индеец собирает свои вещи и снова убирает их в свою маленькую сумочку."
    "Когда она присела передо мной на корточки, я заметил, что перед ее платья, пропитан грязью."
    
    play sound2 "se/mud.ogg"
    show mai sad large at pickup with ease
    show mai sad large at center with ease
    show mai sad with dissolve
    stop sound2 fadeout 1.0
    
    "Когда она встает и начинает уходить, я бормочу в ответ ..."
    me ". . . Спасибо . . ."
    
    stop music fadeout 5.0
    show mai normal
    with dissolve
    
    "Она бросает на меня еще один свой любопытный взгляд и отвечает ..."
    girl ". . . Пожалуйста . . ."
    me ". . . ... . . ."
    me ". . . Хмм . . ."
    "Она только что ..."
    me ". . . Ты говоришь по-английски? . . ."
    
    show mai sad
    with dissolve
    
    girl ". . . Ну, это же девятнадцатый век . . ."
    "Она смотрит на меня устало."
    
    play music "music/dandelions.ogg"
    
    me ". . . Почему, черт возьми, ты не сказал этого раньше?! . . ."
    
    show mai normal
    with dissolve
    
    girl ". . . Мне нечего было сказать . . ."
    "Какая наглость у этого ребенка!"
    me ". . . И как давно? . . ."
    girl ". . . Белые торговцы часто приезжают в нашу деревню, поэтому почти все там говорят на нём . . ."
    "Должно быть, это месть за то, что я схватил ее и размахивал пистолетом перед лицом."
    "Похоже, местные говорят по-английски лучше, чем я думал."
    me ". . . Мне скоро нужно в таверну . . ."
    
    play sound3 "se/brush.ogg"
    show mai worry
    with dissolve
    
    "Я начинаю переминаться с ноги на ногу, чтобы встать. Если я останусь в этом сарае ещё дольше, я могу сойти с ума."
    girl ". . . Тебе не следует двигаться. Твоя рана так быстро не заживёт . . ."
    me ". . . Ты не хирург . . ."
    
    show mai worry
    with hpunch
    
    "Когда я пытаюсь встать, ноги подкашиваются, и я снова падаю."
    
    play sound4 "se/brush.ogg"
    
    "Немного растерявшись, я снова толкаюсь и пытаюсь встать."
    "Медленно, но я поднимаюсь и прихожу в себя."
    
    play sound2 "se/collapse.ogg"
    show mai sad
    with hpunch
    
    "Но после нескольких секунд борьбы я снова падаю в сидячее положение."
    "Я не могу ... мои ноги не выдерживают веса ..."
    "Я путешествовал без остановок несколько дней, спал на твёрдой земле, под дождём и морозом."
    "Моё тело устало от бесконечного хождения по долинам и равнинам."
    "Откинувшись на деревянный столб, я делаю несколько глубоких вдохов."
    
    show mai normal
    with dissolve
    
    "Девушка продолжает смотреть на меня, пока я сдаюсь в своей борьбе."
    me ". . . Что? . . ."
    "Бормочу я в отчаянии."
    
    show mai happy
    with dissolve
    
    girl ". . . Может, теперь ты сумеешь выздороветь . . ."
    "Она улыбается мне, как дура."
    me ". . . Чёрт возьми . . ."
    "Похоже, я застрял здесь на какое-то время ..."
    
    show mai normal
    with dissolve
    
    "Я медленно ерзаю и пытаюсь устроиться поудобнее."
    me ". . . Как тебя зовут, девочка? . . ."
    "Думаю, пока я постараюсь с ней помириться."
    girl ". . . {i}Маккитотосимью{/i} . . ."
    me ". . ."
    me ". . . Что? . . ."
    girl ". . . {i}Маккитотосимью{/i} . . ."
    me ". . . Прости, я не понял, что ты сказала . . ."
    me ". . . А что это значит? . . ."
    "Обычно индейские имена имеют какое-то значение."
    "Что-то связанное с землёй, животными или чем-то подобным ..."
    "Но девочка замолкает."
    me ". . . Значит ... {i}Макки{/i} ... {i}Маккисото ... . . .{/i}"
    girl ". . . {i}Маккитотосимью{/i} . . ."
    me ". . ."
    "Это будет раздражать больше, чем я думал."
    me ". . . Как насчёт {i}'Мая'{/i}? . . ."
    mai ". . . {i}'Мая'{/i}? . . ."
    me ". . . Считай это прозвищем . . ."
    "В любом случае это сэкономит мне время."
    mai ". . . {i}Ник{/i} ... {i}Имя{/i}? . . ."
    me ". . . Эммм ... это то, что используют союзники . . ."
    "В конце концов, если я британец, а она индейка, то мы, естественно, союзники."
    mai ". . . {i}Союзники{/i} ... . . ."
    me ". . . Что же это за слово? . . ."
    
    show mai sad
    
    me ". . . {i}Кокум{/i} ... {i}Кокумта! Кокумта!{/i} . . ."
    "Она смотрит на меня неодобрительно."
    "Подождика, это неправильно? В конце концов, это сложный язык ..."
    mai ". . . Понимаю. {i}Друзья.{/i} . . ."
    me ". . . Эм ... Ну хорошо . . ."
    "Зачем я так стараюсь с этим ребёнком?"
    
    show mai normal
    with dissolve
    
    mai ". . . Я Мая . . ."
    me ". . . Хорошо . . ."
    mai ". . .Моя деревня, когда-то принадлежавшая племени {i}Киспоко{/i} и клану {i}Петакинитииивомхсуми{/i} . . ."
    me ". . . Океей . . ."
    mai ". . . Кто вы? Как вас зовут? . . ."
    me ". . . Меня зовут Обри, я англичанин по рождению . . ."
    
    show mai sad
    
    mai ". . . У всех вас, белых мужчин, странные имена . . ."
    me ". . . Я не хочу слышать это от девушки с именем из десяти слогов . . ."
    
    show mai normal
    with dissolve
    
    me ". . . В любом случае, что ты здесь делаешь одна? . . ."
    mai ". . . Я жду, когда закончится буря . . ."
    me ". . . Я так и предполагал. Я имею в виду ... . . ."
    "Я резко останавился."
    "Я думал спросить её, почему она здесь, но мне пришла в голову другая мысль."
    me ". . . Дверь была завязана . . ."
    mai ". . ."
    me ". . . Как ты сюда попала? . . ."
    "Спросил я довольно тихим голосом."
    mai ". . . Я пролезла через эту щель в стене . . ."
    "Она указывает на сломанное отверстие в стене сарая."
    me ". . . Эмм . . ."
    "Что ж, мог бы и догадаться."
    me ". . . А что ты делаешь одна посреди этих пустых мест? . . ."
    me ". . . Здесь ведь ничего нет на многие мили вокруг . . ."
    "Кроме поля, полного трупов, конечно же."
    
    show mai sad
    with dissolve
    
    "Она делает неловкое выражение лица."
    mai ". . . Я пытаюсь найти дорогу домой ... . . ."
    me ". . . Домой? Ты хочешь сказать, что заблудилась? . . ."
    "Ничего."
    "Даже туземцы иногда теряются."
    "Тут ничего необычного нет ..."
    "Это вообще неудивительно ..."
    "Они ведь живут где придется, в лесах и у рек."
    "Часто слышал истории о скальпировании, убийствах и изнасилованиях ..."
    "Многие мужчины ненавидят и боятся их ... Но ... я сам никогда этого не чувствовал ..."
    
    stop music fadeout 5.0
    stop soundfx2 fadeout 5.0
    $ mouse_visible = False
    scene black
    with dissolve2
    window hide
    pause 2.0
    play soundfx "se/rain.ogg" fadein 20.0
    show expression Text(_("Тем временем в нескольких милях к северу, недалеко от Детройта ..."), size=20, yalign=0.5, kerning=4, color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve
    pause 3.0
    hide expression Text(_("Meanwhile, several miles north, near to Detroit . . ."), size=20, yalign=0.5, kerning=4, color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve
    pause 1.0
    pause 1.0
    window show
    scene forestrain
    with dissolve4
    $ mouse_visible = True
    play music "music/theplan.ogg"
    
    "В лесистой местности в нескольких милях к северу солдаты в синих мундирах сидят под своими изношенными брезентами."
    "Небольшой отряд, сформированный для набегов и разведки."
    "После недавних сражений в Онтарио многие британцы бегут на юг, в Соединённые Штаты."
    "Задача налётчиков — выследить дезертиров в красных мундирах, отступающих на их землю."
    "На их лагере — залитый водой кострище, а промокшие насквозь плащи свисают с ближайших веток."
    daniels ". . . Что за буря такая? . . ."
    mctavish ". . . Может, это всё индейцы пляшут танцы дождя? . . ."
    mctavish ". . . Ну, знаешь? Мы же пристрелили Текумсе, вот они теперь и отплясывают в честь этого . . ."
    daniels ". . . Скорее уж закон подлости . . ."
    "Отряд рейдеров пытается укрыться от хлещущего ливня."
    "Несколько солдат одеты в оленьи шкуры, при них томагавки и винтовки."
    "Их цель — слиться с окружением и застать врагов врасплох."
    daniels ". . . Эй, капитан, как насчёт того, чтобы двинуть к {i}Детройту{/i}? . . ."
    daniels ". . . Всё равно никакие красномундирники не сунутся так далеко на юг."
    mctavish ". . . Разве что не утонут по дороге или их не пристрелят . . ."
    
    scene forestrainjackson
    with dissolve
    
    "Лидер их отряда смотрит в мёртвую кучу пепла и догоревших углей."
    captain ". . .  . . ."
    "Он, кажется, игнорирует их разговор."
    mctavish ". . . Капитан? . . ."
    captain ". . . Наш приказ — продолжать марш на запад . . ."
    captain ". . . Если увидим каких-нибудь красномундирников — берём в плен или пристреливаем . . ."
    daniels ". . . Ага, я понял, но кто в такую бурю вообще будет путешествовать? . . ."
    daniels ". . . Почему бы не двинуть на север и не передохнуть пару дней, не взять эля да девчонок . . ."
    mctavish ". . . В {i}Детройте{/i} полно девок и скво . . ."
    daniels ". . . Эй, капитан? . . ."
    "Их босса, похоже, не удалось убедить их аргументами."
    captain ". . . Мы будем ждать докладов от разведчиков и продолжим марш на запад . . ."
    "Капитан медленно разворачивается, чтобы уйти."
    captain ". . . Можешь выпить и переспать со всеми шлюхами, какие захочется, когда эта война закончится . . ."
    captain ". . . А до тех пор тебе лучше держать рот на замке, Дэниэлс . . ."
    
    play sound2 "se/mud.ogg"
    scene forestrain
    with dissolve
    stop sound2 fadeout 5.0
    
    "С этими словами их капитан отворачивается и идёт через лагерь — проверить остальных солдат."
    daniels ". . . Д-Да, сэр . . ."
    mctavish ". . . Чёрт возьми . . ."
    mctavish ". . . И что это всё значило? . . ."
    daniels ". . . Мудак . . ."
    
    $ mouse_visible = False
    stop soundfx fadeout 5.0
    stop music fadeout 5.0
    scene black
    with dissolve2
    pause 2.0
    play soundfx2 "se/rain_in.ogg" fadein 3.0
    scene barn
    with dissolve4
    $ mouse_visible = True
    
    "Ледяной дождь начинает хлестать с новой силой — буря оборачивается худшим."
    "Мне повезло, что я нашёл это укрытие."
    "Однако ..."
    
    show mai normal
    with dissolve
    play music "music/native.ogg"
    
    "... появление воровки-индианки — не повод для радости."
    me ". . . Итак, Мая . . ."
    me ". . . Ты потерявшаяся шауни и пытаешься найти дорогу домой? . . ."
    me ". . . Где ты живёшь? . . ."
    mai ". . . У озера . . ."
    me ". . . Так. И где это озеро? . . ."
    mai ". . . Я не знаю . . ."
    me ". . . Не знаешь? . . ."
    
    show mai sad
    with dissolve
    
    mai ". . . Поэтому я и потерялась . . ."
    me ". . . Ясно . . ."
    "Я начинаю понимать её проблему."
    mai ". . . Я редко отлучаюсь из дома . . ."
    me ". . . Можешь вспомнить хоть что-нибудь ещё? . . ."
    "Я продолжаю её расспрашивать."
    me ". . . Названия фортов или поселений? Названия рек? . . ."
    me ". . . Места, которые ты проходила по пути сюда . . ."
    
    show mai normal
    with dissolve
    
    mai ". . . Я знаю названия некоторых мест поблизости . . ."
    mai ". . . Те названия, что дают им белые люди . . ."
    me ". . . Хорошо. Какие же? . . ."
    
    play sound2 "se/mud.ogg"
    show mai normal large
    with dissolve
    stop sound2 fadeout 2.0
    
    "Девочка замолкает и делает шаг вперёд."
    "Инстинктивно я откидываюсь назад, когда она приближается."
    "Затем, глубоко вздохнув ..."
    
    show mai happy large
    with dissolve
    
    "... она расплывается в широкой улыбке."
    mai ". . . Здорово, дружище! . . ."
    me ". . .  . . ."
    "Переменив позу, девочка начинает разыгрывать излишне дружелюбный балаган."
    mai ". . . Меня зовут {i}Маккитотосимев{/i}, но можешь звать меня {i}Мая{/i} . . ."
    mai ". . . Я всего лишь маленькая пилигримка, идущая на юг, усекаешь? . . ."
    me ". . . Какого чёрта ты творишь? . . ."
    
    show mai normal large
    with dissolve
    
    mai ". . . Разговариваю как белый человек . . ."
    me ". . . Так белые люди не разговаривают . . ."
    
    show mai sad large
    with dissolve
    
    mai ". . .  . . ."
    me ". . . Почему ты вдруг замолчала?! . . ."
    
    show mai normal large
    with dissolve
    
    mai ". . . Без причин . . ."
    "Ну и наглость у этой девчонки."
    me ". . . Ладно, зачем ты притворяешься американкой? . . ."
    mai ". . . Белым человеком . . ."
    me ". . . Это американский акцент . . ."
    
    show mai sad large
    with dissolve
    
    mai ". . .  . . ."
    me ". . . Хватит замолкать! . . ."
    
    show mai normal large
    with dissolve
    
    mai ". . . Я пытаюсь вспомнить названия ближайших городов . . ."
    mai ". . . Мой отец учил меня, как их произносить, когда спрашиваю дорогу . . ."
    me ". . . Так ты притворяешься пилигримкой и говоришь с акцентом? . . ."
    "Наверное, есть и более глупые способы выжить ..."
    me ". . . Ладно. Заканчивай своё представление . . ."
    "Может, тогда мы выясним, куда она вообще направляется ..."
    "Минуточку! Да и какое мне вообще дело, откуда она?!"
    
    show mai happy large
    with dissolve
    
    mai ". . . В любом случае, дружище, я надеялась, ты подскажешь мне дорогу к моему дому . . ."
    "Она снова врывается в своё представление."
    mai ". . . Не подскажешь ли дорогу к {i}'Фотвэйну'{/i}? . . ."
    me ". . . {i}'Фотвэйну'{/i}? . . ."
    mai ". . . Именно так, дружище . . ."
    "Похоже, она вспомнила."
    me ". . . Ты имеешь в виду {i}'Форт Уэйн'{/i}? . . ."
    
    show mai normal large
    with dissolve
    
    mai ". . . Это я и сказала . . ."
    "Даже когда я пытаюсь возразить, мне не хватает слов."
    "Я подношу руки к лицу и в отчаянии постепенно закрываю глаза."
    "С этой индейской девчонкой каши не сваришь."
    me ". . . Значит ... ты живёшь недалеко от {i}Форт Уэйна{/i}? . . ."
    "И всё же я задаю ей очередной вопрос."
    mai ". . . Я не знаю. Не думаю, что это слишком далеко . . ."
    
    play sound2 "se/mud.ogg"
    show mai normal
    with dissolve
    stop sound2 fadeout 2.0
    
    "Мая отступает на шаг, больше не разыгрывая из себя {i}'дружелюбную янки'{/i}."
    me ". . . Можешь вспомнить что-нибудь ещё? . . ."
    mai ". . . Мой отец научил меня нескольким способам спрашивать дорогу . . ."
    me ". . . Я не об этом спрашивал . . ."
    "С другой стороны, если прошлое представление помогло ей что-то вспомнить ..."
    "Может, стоит ещё немного подыграть ей."
    me ". . . Чему ещё он тебя научил? . . ."
    
    show mai happy2
    with dissolve
    
    maishawnee ". . . Ну... это была программа {rb}{i}шеманезе{/i}{/rb}{rt}(белый человек){/rt} . . ."
    me ". . . Я ... понял . . ."
    maishawnee ". . . Есть ещё программа {rb}{i}май-а-сквитэта{/i}{/rb}{rt}(юная девушка){/rt} . . ."
    "Девочка нагибается, окунает руки в лужицу и зачерпывает немного воды."
    
    play sound3 "se/wash.ogg"
    show mai cry2
    with dissolve
    
    "Плеская её себе в лицо, она делает вид, будто плачет."
    
    show mai cry
    with dissolve
    
    mai ". . . П-Пожалуйста ... мистер ... . . ."
    "Рыдающим и дрожащим голосом она начинает умолять, пока капли воды катятся по её щеке."
    mai ". . . Я потерялась и п-пытаюсь найти дорогу домой ... . . ."
    mai ". . . Мой х-хозяин побьёт меня, если я не вернусь вовремя! . . ."
    "Всхлипывая, Мая сжимает руки и трясётся, как задние ноги ягнёнка."
    mai ". . . Пожалуйста ... скажи мне дорогу к {i}'Фотвэйну'{/i} . . ."
    
    show mai cry2
    with dissolve
    
    "Она шмыгает носом, пытаясь сдержать слёзы."
    "Моё сердце обливается кровью при виде этого бедного создания ..."
    "... пока я не вспоминаю, что всё это — спектакль."
    
    show mai gulp
    with dissolve
    
    "Индейская девчонка вытирает глаза и быстро прекращает представление."
    
    show mai happy2
    with dissolve
    
    mai ". . . Видишь? . . ."
    me ". . . А ты маленькая хитрюга, да? . . ."
    
    show mai happy
    with dissolve
    
    mai ". . . Совсем чуть-чуть . . ."
    me ". . . Не стоит воспринимать это как комплимент . . ."
    "Я уже устал от этого сырого сарая и этой девчонки."
    "Почему я всё ещё торчу здесь?"
    "Мне стоит собраться и двинуть на юг, пока я не потратил ещё больше времени на этот разговор."
    "Но даже думая об этом, я понимаю, что мне трудно сдвинуться с места."
    
    show mai happy2
    with dissolve
    
    me ". . . Итак, мы выяснили, что ты живёшь на озере, недалеко от {i}Форт Уэйна{/i} . . ."
    "Это хоть какая-то зацепка ..."
    
    play sound3 "se/brush.ogg"
    show mai normal
    with dissolve
    
    "Засунув руку под красный мундир, я достаю клочок сложенного пергамента."
    
    play sound4 "se/map.ogg"
    show object4
    with dissolve
    
    "Разворачивая её, я вижу запылённую карту территории Мичиган."
    "Мне удалось выиграть её в игру в {i}шов-хапни{/i} ещё в {i}Форт Молдене{/i}."
    "Мы с тем солдатом были тогда оба изрядно пьяны и без гроша в кармане."
    "Вечер мы провели, ставя на кон клочки бумаги, ваксу для сапог и печенье."
    "Я и не думал, что она когда-нибудь пригодится..."
    "Проводя пальцами по карте, я нахожу {i}Форт Уэйн{/i} внизу."
    me ". . . Что ж, в той местности полно озёр и рек . . ."
    "Где-то там наверняка найдётся и деревня шауни."
    
    hide object4
    with dissolve
    
    me ". . . Можешь показать мне её? Твою деревню, то есть . . ."
    
    show mai sad
    with dissolve
    
    "Её лицо мрачнеет, когда она смотрит на пергамент."
    me ". . . Ты умеешь читать карту, ведь так? . . ."
    mai ". . . Немного . . ."
    me ". . . Ну так смотри сюда . . ."
    
    play sound4 "se/map.ogg"
    show object4
    with dissolve
    
    "Я указываю на область на карте, чуть ниже {i}Детройта{/i}."
    me ". . . Мы где-то в этом районе, так? . . ."
    me ". . . А затем вот здесь . . ."
    "Проведя пальцем дальше, я указываю на участок с подписью {i}'Множество мелких озёр'{/i}."
    me ". . . находится много озёр и ручьёв, чуть севернее {i}Форт Уэйна{/i} . . ."
    "Мая внимательно наблюдает, пока я объясняю ей самые основы картографии."
    me ". . . Если пойти вдоль реки, вот так, можно понять, как она извивается на юг . . ."
    
    play sound4 "se/map.ogg"
    
    "Проводя пальцем вдоль одной из нарисованных рек, я замечаю, что она петляет то туда, то сюда."
    
    hide object4
    with dissolve
    
    me ". . . Тебе понятно? . . ."
    
    show mai normal
    with dissolve
    
    mai ". . . Да . . ."
    me ". . . И? Узнаёшь эту местность? . . ."
    mai ". . . Ни капельки . . ."
    
    play sound2 "se/collapse.ogg"
    show mai normal
    with vpunch
    with hpunch
    
    "Я снова падаю духом во второй раз."
    "Сдаюсь, всё ... ей ничем не помочь."
    mai ". . . Но . . ."
    me ". . . Но? . . ."
    
    show mai happy
    with dissolve
    
    mai ". . . Но ... я точно знаю, что оно рядом с {i}Фотвэйном{/i} . . ."
    mai ". . . Это я точно знаю . . ."
    "Она улыбается, будто этого ей достаточно."
    me ". . . Ладно . . ."
    "Что ж, в конце концов, это ей предстоит отправиться в путь ..."
    
    play sound4 "se/map.ogg"
    
    "Я аккуратно складываю карту в маленький квадратик и убираю обратно в карман."
    
    show mai normal
    with dissolve
    
    "Мая снова начинает на меня пялиться."
    me ". . .  . . ."
    mai ". . .  . . ."
    "Это действительно её любимое занятие."
    me ". . . Что? . . ."
    mai ". . . Что ты здесь делаешь? . . ."
    me ". . . А? С чего это вдруг? . . ."
    mai ". . . Ты спросил, откуда я и почему я здесь . . ."
    mai ". . . Почему ты один бродишь по этим равнинам? . . ."
    "Девчонка задевает за живое своей пустой болтовнёй."
    me ". . . Не твоё дело . . ."
    
    show mai sad
    with dissolve
    
    mai ". . . Это не очень-то справедливо . . ."
    me ". . . Жизнь не справедлива. Привыкай . . ."
    
    show mai normal
    with dissolve
    
    mai ". . . Ты сбежал? . . ."
    me ". . . Что?! . . ."
    mai ". . . Ты одет как солдат. Ты сбежал с поля боя? . . ."
    me ". . . Не пойти бы тебе куда подальше? . . ."
    
    show mai sad
    with dissolve
    
    mai ". . . {i}'Пойти куда подальше'{/i}? . . ."
    "По её лицу расплывается недоумение."
    
    show mai normal
    with dissolve
    
    me ". . . Забудь . . ."
    "Она продолжает на меня пялиться."
    me ". . . Я не сбегал с поля боя ... по крайней мере, не потому что испугался ... . . ."
    me ". . . Всё-таки я не трус . . ."
    mai ". . . Я и не говорила, что ты трус . . ."
    "Я позволяю индейской девчонке выводить меня из себя ..."
    me ". . . Ты не поймёшь. Ты слишком мала . . ."
    mai ". . .  . . ."
    "Снова молчание."
    me ". . . Чтобы ты там ни думала, я точно не трус . . ."
    mai ". . . Ты это уже говорил . . ."
    me ". . . Хочешь получить по уху? . . ."
    
    stop music fadeout 5.0
    
    "В укрытии воцаряется недолгое молчание."
    mai ". . . Тогда почему ты сбежал? . . ."
    "Оно тут же нарушается очередным вопросом девчонки."
    me ". . . Это ... не стоит того, чтобы вдаваться в подробности ... . . ."
    "Не с кем-то вроде неё."
    "Ни с одним из них ..."
    
    $ mouse_visible = False
    stop soundfx2 fadeout 3.0
    scene black
    with dissolve2
    pause 2.0
    play music "music/memories.ogg"
    play soundfx "se/rain.ogg" fadein 10.0
    scene flashback6
    with dissolve2
    $ mouse_visible = True
    
    "На пути домой наш корабль захватили, а меня насильно зачислили на военную службу."
    "Как и многие, я получил тот самый выбор."
    "Сражайся за свою свободу и свою землю, или умри на коленях."
    "Вскоре началась вторая война, и меня отправили обратно на границу ..."
    "Красные мундиры и янки снова сражались за землю, принадлежавшую индейцам."
    "Не могу сказать, что мне было не всё равно. Но я был хорошим солдатом."
    "В тех первых сражениях мы наступали и осаждали американские города и форты."
    "Я сражался с лучшими из лучших."
    "Патрик Марлоу, Ричард Дьюкс, Джеймс Ноуленд ..."
    "Я бы даже назвал этих людей своими друзьями."
    "И, конечно, человек, который возглавлял атаку, тот, кого мы все уважали ..."
    "Генерал-майор Айзек Брок. Фигура, способная соперничать с самим Веллингтоном."
    "Кампании были тяжёлыми, но поначалу мы познали славу."
    "Под его командованием мы захватили {i}Детройт{/i} и сражались при {i}Куинстон-Хайтс{/i}."
    "Но именно там мы увидели, как пал наш храбрый лидер."
    "Многих из нас это сильно задело ..."
    "Теперь, под командованием свиньи по имени Проктер, мы заметили, как наша удача медленно угасает."
    "Индейцы продолжали храбро сражаться, но наши войска были в постоянном состоянии поражений и отступлений."
    "Я наблюдал, как наш славный полк разваливался и распадался под руководством Проктера."
    "Закалённые в боях и благородные люди, с которыми я сражался, постепенно теряли боевой дух."
    "Мы обратились к выпивке и азартным играм, чтобы убить время."
    "Многие говорили о дезертирстве, если бы только им представилась возможность ..."
    "Джон Росс, барабанщик, казался самым испуганным из нас."
    "Он засиживался допоздна, вертя в руках палочки, глядя на угли догоревшего кострища."
    "Если бы только у него хватило смелости, часто говорил он мне, он бы исчез в лесу и никогда не обернулся."
    "Мы дразнили его по этому поводу и спорили, кто убьёт его первым — индейцы или волки."
    "Возможно, он вышел из того сражения свободным человеком ..."
    "Я до сих пор смутно помню то сражение."
    "Озеро Эри пало перед американцами месяц назад, и наши силы бежали от синих мундиров."
    "Войска янки под предводительством Харрисона атаковали наши лагеря на рассвете, в разгар нашего завтрака."
    "В болоте, на наших флангах, Текумсе возглавил атаку против американских сил ..."
    
    play soundfx2 "se/battle.ogg"
    scene flashback4
    with dissolve4
    
    me ". . . Генерал-майор! . . ."
    "Я кричу в сторону деревьев, пока мои братья по оружию рассредоточиваются по лесу."
    "Прислонившись к расщеплённой сосне, я кричу снова."
    me ". . . Генерал-майор! . . ."
    "Трус исчез в разгар битвы, его нигде не было видно, пока наши ряды рассыпались и бежали."
    "В панике мы выстрелили всего раз, прежде чем отступить в деревья."
    me ". . . Генерал-майор! Проктер! Вернись! . . ."
    "И тут я вижу его ... почти размытое пятно, проносящееся через лесополосу."
    "Наш храбрый генерал-майор проезжает мимо — вспышка белого и красного — на своей лошади по пыльной тропе."
    "Как жирное животное, убегающее с поджатым хвостом, Проктер исчезает в лесу."
    "Бросая своих людей на произвол судьбы ..."
    "Пока красные мундиры бегут, наши союзники-индейцы ждут на берегах реки, стоя против американских сил."
    "Британские солдаты сдаются, а я оборачиваюсь, чтобы увидеть лицо вождя индейцев."
    
    scene flashback5
    with dissolve4
    
    "Вдалеке воин клана Пантеры смотрит мне в глаза."
    "Наши взгляды встречаются, и ни один из нас не моргает."
    "Эти глубокие тёмные радужки смотрят тоскливо ... с сожалением ..."
    "Затем он разворачивается и устремляется вперёд с боевым кличем — навстречу более великому врагу, в свете зари."
    
    scene flashback4
    with dissolve4
    
    "Задыхаясь, я прижимаю руку к боку, наблюдая, как загорелые индейцы держат позиции."
    me ". . . Чёрт ... . . ."
    "Я теряю много крови."
    "Не в силах больше смотреть, я разворачиваюсь и бегу в лес, направляясь к возвышенности."
    
    stop music fadeout 3.0
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    $ mouse_visible = False
    scene black
    with dissolve4
    pause 2.0
    play soundfx2 "se/rain_in.ogg" fadein 3.0
    scene barn
    with dissolve4
    $ mouse_visible = True
    
    "Я наблюдал, как храбрый Проктер, словно трус, ускакал прочь в лес."
    "Не в силах больше ничего сделать, я последовал его примеру и дезертировал в чащу."
    "Последние воины Текумсе пали там, сражённые выстрелами янки ..."
    "Знает ли об этом девчонка? Дошла ли весть до неё или до её деревни?"
    "Что моя дивизия предала её племя и бросила их на берегах реки?"
    "Что мы бежали в лес, пока воины Текумсе бежали под ружейный огонь американских войск?"
    ". . .  . . ."
    
    play music "music/dandelions.ogg"
    
    "Кстати, а где девчонка?"
    "Видимо, я ушёл в свои мысли ..."
    "Дрожа от холода, я кое-как встаю и разминаю ноги."
    "В любом случае, эти грёзы дали отдых моим ноющим мышцам."
    
    play soundfx3 "se/mud.ogg"
    
    "Я делаю несколько шагов вперёд и понимаю, что твёрдо стою на ногах."
    "Прохаживаясь по затхлому сараю, чтобы согреться, я осматриваю окрестности."
    
    play sound2 "se/brush.ogg"
    
    "Проводя пальцами по ближайшему ящику, я поднимаю облако белой пыли."
    
    stop soundfx3 fadeout 1.0
    
    "Смахивая омертвевшие частицы, я нахожу там выкрашенные слова {i}'Laird & Company Applejack Cider'{/i}."
    me ". . . Сидр? . . ."
    "Может, мне и тут повезло."
    
    play soundfx4 "se/rummage.ogg"
    
    "Но быстрый осмотр разбивает мои надежды."
    
    stop soundfx4 fadeout 1.0
    
    "Поднимая крышку, я не нахожу ничего, кроме соломы и битого стекла."
    "Тот, кто покупал этот алкоголь, выпил всё давным-давно."
    
    play soundfx3 "se/mud.ogg"
    play soundfx4 "se/rummage.ogg"
    
    "Возвращая крышку на место, я продолжаю пробираться сквозь пустые ящики и бочки в поисках девчонки."
    "Снаружи всё ещё падает ледяной дождь."
    "Я смотрю на дыры в потолке и на капли дождя, что падают сквозь них, разбрызгиваясь по грязной земле внизу."
    "Осень определённо вступает в свои права. По убежищу разливается леденящий сквозняк."
    
    stop soundfx3 fadeout 1.0
    stop soundfx4 fadeout 1.0
    show mai sad
    with dissolve
    play sound2 "se/wood.ogg"
    
    "Вскоре я нахожу её на другой стороне сарая."
    
    stop sound2 fadeout 2.0
    play soundfx3 "se/wood.ogg"
    
    "Мая копается в куче хлама, стоя ко мне спиной."
    "Кажется, она чем-то занята на тяжёлой опорной балке прямо перед собой."
    "С помощью маленького металлического предмета она выцарапывает картинки на деревянной поверхности."
    me ". . . Минуточку! Это же мой нож! . . ."
    "Я узнаю сломанную рукоять и скол на лезвии."
    
    show mai normal
    with dissolve
    
    mai ". . . Ты витал в облаках, вот я и одолжила его . . ."
    me ". . . Он был в моём сапоге . . ."
    "Как, чёрт возьми, она его украла?!"
    mai ". . . Ты перестал говорить и начал строить злое лицо . . ."
    
    show mai angry
    with dissolve
    pause 0.3
    show mai normal
    with dissolve
    
    mai ". . . вот как сейчас, вот я и одолжила твой нож . . ."
    me ". . . Ты маленькая воровка, в любом случае . . ."
    "Она не отвечает, слишком увлечена тем, чем занимается."
    me ". . . Я не строю такие лица . . ."
    mai ". . . Строишь . . ."
    me ". . . Тебе понравится, если я отвешу тебе по уху? . . ."
    mai ". . . Ты это уже говорил . . ."
    "Мая продолжает вырезать в тишине, используя лезвие, чтобы выцарапывать символы на дереве."
    "Я присматриваюсь поближе, пока она работает."
    
    show object2
    with dissolve7
    $ achievement.grant("NEW_ACHIEVEMENT_1_7")
    
    "В центре балки сидит какое-то странное существо."
    "Мне трудно понять, что это должно быть."
    "Кошка? Или, может, лиса?"
    "У неё глупые уши, шесть глупых усов и глупая маленькая улыбка."
    "Ноги кривые, а перспектива нарушена."
    "Я не художник, но видал и получше вырезание по дереву."
    "Дальше по балке есть и другие зарубки, которые она, должно быть, сделала."
    "Считает часы? Или, может, дни ..."
    "А может, это просто тренировочные надрезы, проверка толщины балки?"
    "В любом случае, ей не нужно многого, чтобы занять себя."
    
    hide object2
    with dissolve7
    
    me ". . . И что же это должно быть? . . ."
    
    show mai happy2
    with dissolve
    
    maishawnee ". . . {rb}{i}Ви'си.{/i}{/rb}{rt}(Собака){/rt} . . ."
    me ". . . По-английски, пожалуйста . . ."
    
    show mai happy
    with dissolve
    
    mai ". . . Это собака . . ."
    me ". . . Не похожа ни на одну собаку, которую я видел . . ."
    "У какого пса такой длинный хвост и такая плоская морда?"
    
    show mai happy2
    with dissolve
    
    mai ". . . У нас в деревне есть собака. Я всё время с ним играю . . ."
    mai ". . . Он будит меня по утрам и ложится со мной спать по ночам . . ."
    mai ". . . Он хороший пёсик . . ."
    "Ещё одно откровение о её жизни, которое мне не нужно было слышать ..."
    me ". . . Держишь его как питомца, да? . . ."
    "Не так уж и отличается от нас, наверное."
    "По крайней мере, в этом отношении ..."
    
    show mai normal
    with dissolve
    
    mai ". . . {i}'Питомец'{/i}? . . ."
    me ". . . Ну да. Ну, знаешь, питомец? . . ."
    "Она замолкает."
    me ". . . В смысле, собака принадлежит тебе. Ты владеешь собакой . . ."
    
    show mai happy
    with dissolve
    
    mai ". . . Ты забавный . . ."
    "Мая улыбается мне и качает головой."
    me ". . . Забавный? . . ."
    mai ". . . Как можно {i}владеть{/i} собакой? . . ."
    "Я сдерживаю желание спрятать лицо в ладонях."
    "Может, мы всё-таки слишком разные ..."
    "Я забыл, что у индейцев плохое понятие о собственности."
    
    show mai happy2
    with dissolve
    
    me ". . . Это довольно просто. Я знаю многих, у кого есть питомцы . . ."
    mai ". . . Белый человек может владеть животными и рабами, но мы, шауни, живём свободно со всеми . . ."
    
    show mai happy
    with dissolve
    
    mai ". . . По крайней мере, так говорит мой отец . . ."
    "Пока Мая читает мне лекцию о понятии собственности, она вырезает другие символы на балке."
    
    show mai normal
    with dissolve
    
    me ". . . Есть свои плюсы, когда животные — питомцы, знаешь ли? . . ."
    mai ". . . Например? . . ."
    "Я пытаюсь перечислить причины, которые приходят мне в голову."
    me ". . . Ну, во-первых, еда и тепло, которые щедро даются . . ."
    me ". . . Общение, безопасность, бесплатная постель, объедки... . . ."
    me ". . . Мне не кажется, что это такая уж тяжёлая жизнь . . ."
    mai ". . . Если бы незнакомый мужчина предложил тебе всё это, ты бы согласился? . . ."
    me ". . . Если бы я был бездомным псом, то, наверное, да . . ."
    mai ". . . А взамен ты бы стал его собственностью? . . ."
    me ". . . Именно так . . ."
    mai ". . . И тебя бы били, когда ты делал то, что хотел? . . ."
    mai ". . . Тебе бы дали новое имя и ошейник и приказали вести себя хорошо? . . ."
    me ". . . Ну ... да ... . . ."
    
    show mai sad
    with dissolve
    
    mai ". . . Странно это . . ."
    me ". . . Что странно? . . ."
    mai ". . . Ты бы с радостью стал рабом ради еды и постели . . ."
    me ". . . Не совсем так... . . ."
    "Вообще-то, тут она меня подловила."
    
    show mai normal
    with dissolve
    
    me ". . . Ну, если бы я был всего лишь животным, то да ... . . ."
    me ". . . Но мы говорили о {i}'что, если'{/i}, а не о том, что бы мы на самом деле ... . . ."
    "Давай же, ты позволяешь индейской девчонке перехитрить себя, Обри."
    me ". . . Слушай, тут есть разница! . . ."
    "Я повышаю голос, обороняясь."
    me ". . . Это просто устроено в природе, понятно ... . . ."
    mai ". . . Так животные должны быть рабами? . . ."
    "Думай быстрее."
    me ". . . Господство . . ."
    "Я просто выпаливаю это слово."
    mai ". . . {i}'Господство'{/i}? . . ."
    me ". . . Именно. Господство . . ."
    "Я на самом деле не помню, что означает это слово, но точно слышал его раньше."
    "Оно как-то связано с Библией и животными, это я знаю точно."
    mai ". . . Что такое {i}'Господство'{/i}? . . ."
    "Отчаянно пытая свою память воспоминаниями о тоскливых церковных проповедях, я натыкаюсь на ответ."
    "Господство. Это о правах человечества."
    me ". . . Это связано с тем, что Бог дал человеку власть над животными ... . . ."
    me ". . . Как христианин, я имею право владеть питомцами и командовать ими . . ."
    "По правде говоря, я вообще не религиозный человек."
    "Но если это заставит её заткнуться, я только за."
    mai ". . . Понятно . . ."
    "Ага! Сейчас я её припёр!"
    mai ". . . То есть ты говоришь, что ... . . ."
    "Да ... продолжай ..."
    
    show mai happy
    with dissolve
    
    mai ". . . То есть ты очень любишь животных, да? . . ."
    
    play sound2 "se/collapse.ogg"
    show mai happy
    with vpunch
    with hpunch
    
    me ". . . Что? Нет! Это не тот вывод, который нужно было сделать ... . . ."
    "Она продолжает улыбаться своей глупой улыбкой, пока я пытаюсь защитить себя."
    me ". . . и ещё есть права человека и ... . . ."
    "Забудь. Против неё не выиграть."
    
    show mai normal
    with dissolve
    
    "Я позволяю тишине вернуться, и Мая продолжает свои царапины."
    "Вскоре я замечаю свёрнутое одеяло, прислонённое к деревянной балке, рядом с её сумкой."
    me ". . . Эй ... это твоё? . . ."
    
    stop soundfx3 fadeout 2.0
    
    "Мая прекращает вырезать."
    "Она смотрит на меня, а затем на одеяло."
    
    show mai happy2
    with dissolve
    
    mai ". . . Это моё {i}мишаами{/i} . . ."
    me ". . . Значит, это твоё одеяло? . . ."
    
    show mai normal
    with dissolve
    
    mai ". . . Оно принадлежит моей деревне . . ."
    "Одеяло, которое принадлежит целой деревне?"
    me ". . . Ну, неважно. Мне холодно, так что дай его сюда . . ."
    
    stop music fadeout 5.0
    play sound2 "se/mud.ogg"
    show mai normal at pickup with ease
    show mai worry at center with ease
    stop sound2 fadeout 1.0
    
    "Глядя мне в глаза, девчонка осторожно поднимается на ноги и берёт свёрнутое одеяло."
    mai ". . . Нет . . ."
    me ". . . {i}'Нет'{/i}? Что значит {i}'нет'{/i}? . . ."
    
    show mai worry at right45 with ease
    
    "Мая медленно отступает, охраняя одеяло."
    mai ". . . Это моё {i}мишаами{/i} . . ."
    me ". . . Да ладно тебе ... у меня тут задница замерзает ... . . ."
    
    play sound2 "se/swipe.ogg"
    show mai worry at right3 with hpunch
    
    "Я тянусь к ней, но девчонка уворачивается."
    me ". . . Я дал тебе мой нож, это ведь справедливо . . ."
    me ". . . Дай мне его на время . . ."
    
    play sound3 "se/swipe.ogg"
    show mai worry at left3 with hpunch
    play soundfx4 "se/run.ogg"
    hide mai with easeoutleft
    play music "music/oddity.ogg"
    stop soundfx4 fadeout 2.0
    
    "Я снова делаю рывок вперёд, она отпрыгивает и бежит за балку."
    me ". . . Вернись, маленькая паршивка! . . ."
    
    play soundfx3 "se/mud.ogg"
    play soundfx4 "se/run.ogg"
    scene barnrun
    with dissolve
    play sound2 "se/swipe.ogg"
    
    "Я хватаю ... и снова хватаю ... но она продолжает уворачиваться от моих рук."
    
    play soundfx5 "se/rummage.ogg"
    
    "Петляя и ныряя среди кучи хлама, Мая перепрыгивает через ящики и обегает обратно."
    
    play sound2 "se/smash.ogg"
    
    "Я следую за ней, перепрыгивая через ящики и врезаясь в предметы."
    
    play sound3 "se/wash.ogg"
    
    "До меня наконец доходит, что мы бегаем по кругу."
    me ". . . А ну ... вернись! . . ."
    
    play sound2 "se/swipe.ogg"
    
    "Я окликаю Маю и снова хватаю её."
    "Гоняясь за ней по сараю, мы продолжаем играть в игру Кошки-Мышки."
    
    play sound2 "se/wash.ogg"
    
    mai ". . . Нет! . . ."
    
    play sound3 "se/smash.ogg"
    play sound4 "se/junk.ogg"
    
    "Мая нервно выкрикивает в ответ и опрокидывает запылённое оконное стекло, преграждая мне путь."
    me ". . . Ах! . . ."
    "Вскоре я задыхаюсь, так как начинается ноющая боль в руке."
    me ". . . П-Прекрати ... прекрати на секунду ... . . ."
    
    stop soundfx3 fadeout 1.0
    stop soundfx4 fadeout 1.0
    stop soundfx5 fadeout 1.0
    scene barn
    with dissolve
    
    "Останавливаясь, я подаюсь вперёд и глубоко дышу."
    me ". . . Ладно ... забирай свою ... грёбаную тряпку ... . . ."
    
    show mai normal
    with dissolve
    
    "Осторожно девчонка выходит из укрытия."
    mai ". . . Это {i}мишаами{/i} моей деревни . . ."
    me ". . . Ладно, понял я ... . . ."
    mai ". . . Тебе оно не достанется . . ."
    me ". . . Ладно ... ладно ... . . ."
    
    show mai happy
    with dissolve
    
    "Мая улыбается с торжеством."
    "Взглянув через её плечо, я широко раскрываю глаза и указываю вперёд."
    
    show mai normal
    with dissolve
    
    me ". . . Эй! А это что?! . . ."
    "С паникой в голосе я отступаю назад, пока Мая оборачивается и оглядывается."
    "Вот мой шанс!"
    
    play sound2 "se/swipe.ogg"
    show mai worry with vpunch
    
    "Я бросаюсь вперёд и выхватываю одеяло из её рук."
    me ". . . Ха-ха! Попалась! . . ."
    me ". . . Не могу поверить, что ты купилась на это ... . . ."
    
    play soundfx3 "se/mud.ogg"
    play sound2 "se/swipe.ogg"
    show mai bounce
    pause 0.1
    
    "Мая подпрыгивает на месте, пытаясь забрать своё одеяло обратно."
    "Я поворачиваюсь к ней спиной и держу его вне досягаемости."
    
    stop soundfx3
    show mai worry
    play sound2 "se/junk.ogg"
    play sound3 "se/gundrop.ogg"
    
    "Отстёгивая верёвку, связывающую одеяло, я разворачиваю его."
    me ". . . Какого чёрта? . . ."
    "Множество маленьких керамических, деревянных и металлических предметов высыпаются на грязный пол."
    "Маленькие горшочки, кисточки, наконечники стрел, маленькая тряпичная кукла, полоски ткани..."
    
    show mai sad
    with dissolve
    
    "Лицо Маи вытягивается, и её руки медленно опускаются."
    me ". . . Что всё это делало в одеяле? . . ."
    "Я спрашиваю девчонку, но она не отвечает."
    "Мая продолжает смотреть на предметы, лежащие в грязи."
    me ". . . Что такое? Это просто хлам . . ."
    
    show mai angry
    with dissolve
    
    "Её выражение лица мгновенно меняется, и Мая делает шаг вперёд."
    mai ". . . Идиот! . . ."
    
    play soundfx "se/slap.ogg"
    show mai hit
    
    "Она бьёт меня раскрытыми ладонями, а я отталкиваю её раненой рукой."
    "Резкая боль пронзает плечо, и я падаю назад, пока индейская девчонка набрасывается на меня."
    me ". . . Эй! Эй! Ой, прекрати! . . ."
    "Её удары практически безвредны, но моё ноющее тело не выносит такого раздражения."
    me ". . . Я сказал, прекрати! . . ."
    
    stop soundfx
    play sound2 "se/collapse.ogg"
    play sound3 "se/mud.ogg"
    show mai worry at pickup
    pause 0.1
    hide mai
    scene barn
    with vpunch
    stop sound3
    
    "Бросая одеяло, я здоровой рукой толкаю девчонку на землю."
    "Приземлившись в грязь, Мая покрывает свою задницу мокрой соломой и грязью."
    "На её лице застыло выражение шока."
    me ". . . Ты сделала мне больно, паршивка ... . . ."
    
    play sound3 "se/mud.ogg"
    show mai sad
    with dissolve
    stop sound3 fadeout 1.0
    
    "Сдержанно поднимаясь на ноги, она снова строит печальное выражение лица."
    me ". . . Что? Я не так уж и сильно тебя толкнул ... . . ."
    
    play sound3 "se/mud.ogg"
    show mai sad at pickup with ease
    show mai sad at center with ease
    stop sound3 fadeout 1.0
    
    "Наклоняясь, Мая выгребает хлам из грязи."
    
    play soundfx3 "se/mud.ogg"
    hide mai
    with dissolve
    
    "Затем, не говоря ни слова, она разворачивается и идёт в другой конец сарая."
    
    stop soundfx3 fadeout 5.0
    
    me ". . . И что это было? . . ."
    
    play sound3 "se/brush.ogg"
    pause 0.5
    stop sound3 fadeout 2.0
    
    "Накинув одеяло на плечи, я сажусь на сухое место с сеном и пытаюсь расслабиться ..."
    me ". . . Это просто одеяло . . ."
    
    stop music fadeout 5.0
    stop soundfx2 fadeout 5.0
    $ mouse_visible = False
    scene black
    with dissolve2
    window hide
    pause 2.0
    play soundfx "se/rain.ogg" fadein 10.0
    window show
    scene forestrain
    with dissolve4
    $ mouse_visible = True
    play music "music/theplan.ogg"
    play soundfx3 "se/mud.ogg"
    
    scout ". . . Капитан! Капитан! . . ."
    "В лагере американских рейдеров прибегает молодой разведчик."
    scout ". . . Где капитан? . . ."
    
    stop soundfx3 fadeout 5.0
    scene forestrainjackson
    with dissolve
    
    captain ". . . Что там, парень? . . ."
    "Разведчик останавливается, отчаянно пытаясь отдышаться."
    scout ". . . На юге ... возле фермы Эдвардса ... . . ."
    captain ". . . Выкладывай уже . . ."
    scout ". . . Красный мундир ... заметили красный мундир! . . ."
    captain ". . . Ферма Эдвардса? . . ."
    scout ". . . Так точно ... сэр . . ."
    captain ". . . Так далеко на юге? Ты уверен? . . ."
    scout ". . . Да, сэр . . ."
    "Капитан замолкает на несколько мгновений."
    captain ". . . Чёрт возьми ... . . ."
    scout ". . . Сэр? . . ."
    
    scene forestrain
    with dissolve
    
    "Затем их лидер медленно уходит прочь."
    scout ". . . В чём дело? . . ."
    "Один из рейдеров подходит к разведчику."
    daniels ". . . Мы были там всего лишь вчера . . ."
    "Он протягивает парню небольшую металлическую кружку, полную какой-то выпивки."
    "Капли дождя рябью расходится в напитке, падая и постепенно наполняя сосуд."
    scout ". . . Правда? . . ."
    daniels ". . . Мы наткнулись на группу британцев, отступавших . . ."
    daniels ". . . Это были просто парни, но ... . . ."
    "Дэниэлс смотрит вдаль."
    scout ". . . Приказы есть приказы ... . . ."
    daniels ". . . Вот именно . . ."
    "Солдат наклоняется в своей палатке и начинает собирать вещи."
    scout ". . . Ты что делаешь? . . ."
    daniels ". . . Без сомнения, капитан заставит нас скоро выступать . . ."
    daniels ". . . Спасибо, что предупредил . . ."
    scout ". . . Не в такую же бурю? . . ."
    daniels ". . . Ты не знаешь капитана ... . . ."
    daniels ". . . Он сдвинул бы небо и землю ради возможности пристрелить красных мундиров . . ."
    scout ". . . Он так сильно их ненавидит, да? . . ."
    "Не ответив, разведчик наблюдает, как солдаты в лагере собирают свои пожитки."
    
    stop music fadeout 5.0
    stop soundfx fadeout 5.0
    $ mouse_visible = False
    scene black
    with dissolve2
    pause 2.0
    play music "music/first_encounter.ogg"
    play soundfx2 "se/rain_in.ogg" fadein 3.0
    scene barn
    with fade
    $ mouse_visible = True
    
    "Наконец, в укрытии воцаряется тишина."
    "Прислонившись к деревянной балке, я стараюсь не шевелить рукой."
    "Лёгкое пятно крови из раны едва заметно на фоне красного мундира."
    "После нашей недавней перепалки Мая решила меня игнорировать."
    "Она сидит на корточках у дверного проёма, ко мне спиной."
    "Её руки двигаются взад-вперёд, пока она играет с чем-то на земле."
    "Я всматриваюсь, пытаясь понять, что она делает."
    "Маленькая лягушка прыгает мимо, копаясь в грязных лужах у двери."
    "Мая, присев рядом, тычет палкой ей в спину."
    "В ответ лягушка бросает на неё раздражённый взгляд и отодвигается."
    me ". . . Что ты делаешь? . . ."
    
    $ mouse_visible = False
    window hide
    scene cg2
    with dissolve2
    pause 2.0
    window show
    $ mouse_visible = True
    $ achievement.grant("NEW_ACHIEVEMENT_1_1")
    
    "Вздрогнув, она медленно поворачивается ко мне лицом и строит нахмуренное выражение."
    maishawnee ". . . {rb}{i}Англичанакэ ...{/i}{/rb}{rt}(Англичанин ...){/rt} . . ."
    me ". . . {i}'Англичан-а-кэ'{/i}? Почему ты так говоришь? . . ."
    "Она со мной резка? Или, может, это оскорбление ..."
    "Честно говоря, оскорблением было бы назвать меня французом."
    maishawnee ". . . {rb}{i}Шемагана ...{/i}{/rb}{rt}(Солдат ...){/rt} . . ."
    me ". . . Говори по-английски . . ."
    maishawnee ". . . {rb}{i}Мачеле не та-та ...{/i}{/rb}{rt}(Ты мой враг ...){/rt} . . ."
    "Она продолжает говорить на своём родном языке, не желая вести разговор."
    me ". . . Говори на грёбаном английском, хорошо ... . . ."
    "Я рычу низким голосом."
    mai ". . .  . . ."
    "Никакого ответа."
    me ". . . Тогда забудь . . ."
    "Было бы эгоистично с её стороны оставлять у себя это одеяло, когда у меня тут задница замерзает."
    "Я думал, у индейцев больше ума, чем быть сентиментальными по поводу вещей."
    "Я припоминаю, как один командующий офицер сказал нам, что у шауни нет понятия собственности."
    "Земля принадлежит всем и никому."
    "Индейцы просто занимают её, не думая о прибыли или о том, чтобы что-то на ней выращивать."
    "Во всяком случае, это обычно служит оправданием, чтобы отобрать её у них ..."
    "Наверное, Мая — ребёнок. Для неё естественно быть немного эгоистичной."
    "И, вероятно, она привязана к этому одеялу..."
    "Но что же выбрать: быть в тепле или позволить девчонке настоять на своём?"
    maishawnee ". . . {rb}{i}Матэти-и-ти ... Тота ...{/i}{/rb}{rt}(Уродливый ... Француз ...){/rt} . . ."
    me ". . . Что ты сказала? . . ."
    mai ". . . Ты не имел права брать мою сумку . . ."
    me ". . . Так ты всё-таки говоришь по-английски ... . . ."
    me ". . . Да и какая тебе разница? Это просто одеяло . . ."
    mai ". . . {i}Мишаами{/i} священно для моей деревни . . ."
    "Мая показывает те самые игрушечные наконечники стрел и керамику, теперь уже чистые."
    mai ". . . Эти предметы священны и должны храниться внутри {i}мишаами{/i}, чтобы защищать деревню . . ."
    me ". . . И что, я должен был просто замёрзнуть насмерть? . . ."
    mai ". . . Ты подверг мою деревню опасности. Она открыта для атак демонов . . ."
    me ". . . Демонов, значит ... . . ."
    me ". . . Тогда почему эта {i}'ми-ша-ар-ми'{/i} штука не находится прямо сейчас в твоей деревне? . . ."
    me ". . . Разве там она не справлялась бы лучше? . . ."
    mai ". . . Её дали мне, чтобы я уберегла её от таких, как ты . . ."
    "Мая слегка ёрзает, обхватив колени руками, чтобы согреться."
    me ". . . От таких, как я? . . ."
    mai ". . . Американцев и англичан, которые хотят с нами воевать . . ."
    me ". . . О чём ты говоришь? . . ."
    "Она смотрит на меня с надутыми щеками и издаёт слышной вздох."
    mai ". . . Много месяцев назад к нашим старейшинам приходили английские охотники и воины кикапу . . ."
    me ". . . Охотники? Ты имеешь в виду, в твоей деревне? . . ."
    "С безучастным блеском в глазах девчонка начинает рассказывать свою историю..."
    mai ". . . Это было летом . . ."
    mai ". . . Они принесли своё оружие в нашу деревню и завербовали мужчин и мальчиков сражаться . . ."
    mai ". . . Американцы должны были скоро прийти с севера, и поэтому мы должны были присоединиться к коалиции . . ."
    mai ". . . Многие мужчины в деревне были молоды и неопытны . . ."
    mai ". . . Некоторые хотели идти, но старейшины запретили . . ."
    "Племена часто разделены во мнениях — сражаться или заключать мир."
    "Я полагаю, её деревня хотела мира, не борясь за него ..."
    "Такие люди обычно не выживают во время войны."
    mai ". . . Нам сказали, что эти места опасны. Мы будем мишенью . . ."
    mai ". . . Англичане уже воевали на американских землях . . ."
    mai ". . . Если бы какие-нибудь американцы узнали об их визитах ... . . ."
    me ". . . Они бы сожгли деревню дотла . . ."
    "Мая медленно кивает."
    mai ". . . Мои старейшины сказали им, что они должны уйти, и тогда мы будем в безопасности . . ."
    mai ". . . Тогда {i}англичанакэ{/i} забрал наше {i}мишаами{/i} и пригрозил уничтожить его . . ."
    me ". . . Я ... понятно . . ."
    "Принуждать индейцев сражаться в этих краях — не новость."
    "Иногда предложить им золото и оружие недостаточно."
    "Тогда угрожаешь им, забираешь их священные вещи, их женщин и детей ..."
    mai ". . . Мы должны были сражаться против американцев и защищать свои дома . . ."
    mai ". . . Если мы этого не сделаем, то предадим своих родичей . . ."
    mai ". . . Мы должны быть союзниками, мы должны защищать конфедерацию . . ."
    mai ". . . Пророк хотел, чтобы мы присоединились к нему и его воинам . . ."
    "Пророк? Я слышал об этом человеке ..."
    "Безумный индейский жрец, брат Текумсе."
    "Они основали какой-то союз индейцев, религиозный культ ..."
    mai ". . . У наших старейшин не было выбора, и мы начали приготовления . . ."
    mai ". . . Я должна была идти с другими детьми и стариками . . ."
    me ". . . Не то чтобы это было неинтересно, но куда именно ведёт этот рассказ? . . ."
    "Я отчитываю её скучающим тоном."
    mai ". . .  . . ."
    "Мая бросает на меня смертоносный взгляд и сворачивается в ещё более меньший клубок."
    mai ". . . Забудь . . ."
    "Она снова замолкает."
    me ". . . Я не хотел быть грубым. Просто ... . . ."
    me ". . . Какое всё это имеет отношение к тому, что я взял твоё одеяло? . . ."
    mai ". . . Во времена войны, когда нам приходится бросать свои дома, {i}Шаман{/i} должен взять {i}мишаами{/i} . . ."
    mai ". . . В нём заключены все надежды нашей деревни. Он присматривает за всеми нами . . ."
    me ". . . Ладно ... значит, ты и есть {i}'Шаман'{/i}? . . ."
    mai ". . . Нет. {i}Шаман{/i} — это знахарь . . ."
    me ". . . Ты меня уже запутала . . ."
    mai ". . . Тот, кто лечит других с помощью магии . . ."
    me ". . . {i}Шаман{/i} — это что-то вроде ведьмы? Ты это мне говоришь? . . ."
    mai ". . . {i}Шаману{/i} вернули {i}мишаами{/i}, когда нашу деревню эвакуировали . . ."
    "Она игнорирует мой вопрос."
    mai ". . . Все, кто не сражался — дети, женщины, старики — должны были двинуться на юг . . ."
    mai ". . . Мы покинули деревню длинной колонной, взяв с собой что могли . . ."
    mai ". . . Когда мы оказались в безопасности, мы должны были ждать вестей о битве . . ."
    mai ". . . Но ... . . ."
    me ". . . {i}'Но'{/i} ...? . . ."
    mai ". . . Но англичане нас обманули . . ."
    mai ". . . Американцы пришли с юга, а не с севера . . ."
    mai ". . . Они первыми обнаружили наш отряд, пока наши воины были далеко . . ."
    "Возможно, они предположили, что отряд рейдеров пойдёт прямым маршем на деревню."
    "Или информация разведчика оказалась неверной."
    "Мая смотрит вдаль отсутствующим взглядом."
    mai ". . . Синие мундиры открыли огонь по женщинам и детям . . ."
    mai ". . . Они забрали всё, что смогли, у стариков и больных . . ."
    mai ". . . Старейшины деревни пытались вразумить их . . ."
    mai ". . . Они призывали мужчин быть добрыми христианами. Перестать убивать невинных . . ."
    mai ". . . Мы кричали и плакали, но им было всё равно . . ."
    mai ". . . Они хотели мести. Не больше . . ."
    "Карательная экспедиция. Ответные рейды за потери в других битвах."
    "Деревня шауни Маи, должно быть, была для них лёгкой мишенью."
    mai ". . . Мы рассеялись, каждый шауни пытался защитить себя в одиночку . . ."
    mai ". . . Когда я попыталась убежать, я нашла {i}Шамана{/i}, лежащего в грязи . . ."
    mai ". . . Он был ранен, у него кровоточила голова. Его застрелили . . ."
    mai ". . . В руках он сжимал {i}мишаами{/i} нашей деревни . . ."
    me ". . . Так ты взяла сумку и побежала? . . ."
    mai ". . . Он попросил меня пообещать. Пообещать сохранить её . . ."
    "Мая бормочет в ответ."
    mai ". . . Я бежала и бежала, пока уже не узнавала, где нахожусь . . ."
    mai ". . . Не успела я опомниться, как оставила всех позади . . ."
    mai ". . . Остальные, должно быть, каким-то образом спаслись ... . . ."
    "Индейская девчонка кусает губу."
    me ". . . И что потом? . . ."
    mai ". . . Я много дней ждала в лесу и пыталась найти дорогу домой . . ."
    mai ". . . Существовала ли моя деревня? . . ."
    mai ". . . Сожгли ли её дотла? . . ."
    mai ". . . Кому ещё удалось спастись? . . ."
    mai ". . . Бродя, я надеялась, что всё будет хорошо . . ."
    mai ". . . Но на пути домой ... меня схватили . . ."
    me ". . . Схватили? . . ."
    mai ". . . Меня схватили американцы, шедшие на север, и взяли с собой среди пленных и рабов . . ."
    me ". . . Так ты была пленницей? . . ."
    "Она кивает."
    me ". . . Понятно ... . . ."
    "Теперь становится яснее."
    "Ребёнка шауни взяли в плен."
    "И она, должно быть, тоже сбежала."
    "Вот почему она прячется в этом заброшенном сарае ..."
    me ". . . И одеяло было у тебя, когда они тебя схватили? . . ."
    mai ". . . Я сохранила его, как и обещала . . ."
    "Значит, ей удалось всё это время присматривать за сумкой."
    mai ". . . Они отвели меня на север ... . . ."
    me ". . . Можешь остановиться, думаю, я услышал достаточно . . ."
    mai ". . . Не хочешь знать? . . ."
    me ". . . Меня это все не интересует . . ."
    mai ". . .  . . ."
    "Не думаю, что мне было бы приятно слушать истории о её пленении."
    "Кто знает, что эти янки-ублюдки могли сделать с такой девчонкой, как она ..."
    "В этот момент, съёжившись, Мая выглядит ужасно маленькой."
    mai ". . . Я не видела свою деревню много месяцев . . ."
    mai ". . . Всё это время она была без защиты . . ."
    "Эти охристые глаза, яркие и блестящие, глубоко смотрят в мои."
    mai ". . . Я должна вернуть {i}мишаами{/i} {i}Шаману{/i} . . ."
    mai ". . . Я должна защищать свой народ . . ."
    me ". . .  . . ."
    "Я не знаю, что сказать."
    "С одной стороны, это всего лишь одеяло и какой-то хлам."
    "Но ... после всего ... если для неё это так священно ..."
    
    play sound3 "se/brush.ogg"
    scene barn
    with dissolve4
    stop sound3 fadeout 2.0
    
    "Поднимаясь из сидячего положения, я снимаю одеяло с плеч."
    
    play sound2 "se/mud.ogg"
    show mai sad
    with dissolve
    stop sound2 fadeout 2.0
    
    "Я прохожу половину сарая, останавливаюсь и протягиваю одеяло девчонке."
    me ". . . Держи . . ."
    
    show mai normal
    with dissolve
    
    mai ". . . Ты ... возвращаешь его мне? . . ."
    me ". . . Не прикидывайся. Это ты виновата, что затерроризировала меня . . ."
    me ". . . К тому же, я подумал, мы могли бы обменяться . . ."
    mai ". . . Обменяться? . . ."
    me ". . . Мой нож на твоё одеяло. Так будет справедливо . . ."
    "На что я только не иду, чтобы выжить в этом мире ..."
    me ". . . Что скажешь? . . ."
    
    play sound3 "se/brush.ogg"
    show mai sad
    with dissolve
    
    "Не давая мне ответа, она забирает одеяло из моих рук."
    
    play sound2 "se/mud.ogg"
    hide mai
    with dissolve
    stop sound2 fadeout 2.0
    
    "Затем Мая возвращается в своё согнутое положение в углу."
    me ". . . Эй... . . ."
    "Девчонка поворачивается ко мне спиной."
    me ". . . Эй! Где мой нож? . . ."
    "Она игнорирует меня и начинает снова раскладывать свои священные предметы на одеяле."
    me ". . . Что? Мне даже {i}'спасибо'{/i} не скажешь? . . ."
    "Никакого ответа."
    
    play sound3 "se/brush.ogg"
    
    "Снова усаживаясь на своём местечке на сене, я вздыхаю."
    
    stop music fadeout 5.0
    
    me ". . . И зачем я только стараюсь ... . . ."
    
    stop soundfx2 fadeout 5.0
    $ mouse_visible = False
    scene black
    with dissolve2
    pause 2.0
    scene barn
    with dissolve4
    $ mouse_visible = True
    play soundfx "se/thunder.ogg" fadein 3.0
    play soundfx2 "se/rain_in.ogg" fadein 3.0
    play soundfx3 "se/barninterior.ogg" fadein 3.0
    
    "Какое-то время проходит в тишине."
    "Буря становится всё более жестокой — сверкают молнии, гремят раскаты грома."
    "Капли воды падают на грязный пол, просочившись сквозь щелястые дыры в крыше."
    "Ветер дребезжит деревянными планками в стенах сарая и приносит с собой холод."
    me ". . . {i}Ммм ...{/i} . . ."
    "Меня вырывает из грёз особенно сильный раскат вдалеке."
    me ". . . Всё хуже, да ... . . ."
    "В углу Мая садится, услышав шум."
    
    play sound3 "se/brush.ogg"
    show mai worry
    with dissolve
    stop sound3 fadeout 3.0
    
    "По её лицу расплывается обеспокоенный взгляд."
    mai ". . . {i}Нннн ...{/i} . . ."
    "Неужели она боится таких сильных бурь?"
    me ". . . Это всего лишь гром, не думай об этом ... . . ."
    "Я успокаиваю её."
    
    show mai angry
    with dissolve
    
    "Услышав моё ободрение, девчонка снова морщит лицо."
    mai ". . . Я не с тобой разговариваю . . ."
    
    play sound2 "se/brush.ogg"
    play music "music/oddity.ogg"
    hide mai angry
    with dissolve
    stop sound2 fadeout 3.0
    
    "Надувшись, индейка возвращается в своё согнутое положение."
    "Какая же она маленькая паршивка..."
    
    scene cg2
    with dissolve4
    
    "Мая снова смотрит на меня с сердитым взглядом."
    me ". . . Так ты не вернёшь мне мой нож? . . ."
    mai ". . . Нет . . ."
    "Наверное, она до сих пор меня не простила."
    me ". . . Неужели того, что я вернул тебе одеяло, недостаточно? . . ."
    mai ". . . Нет . . ."
    me ". . . Чего ты от меня хочешь? . . ."
    mai ". . . Нет . . ."
    me ". . . Это не ответ . . ."
    maishawnee ". . . {rb}{i}Мат-та.{/i}{/rb}{rt}(Нет){/rt} . . ."
    "У меня нет на это сил."
    me ". . . Что нужно сделать, а? . . ."
    mai ". . .  . . ."
    me ". . . Если ты не скажешь, я не узнаю ... . . ."
    "Девчонка смотрит на свои пожитки, теперь снова завёрнутые в сумку."
    mai ". . . Я рассказала тебе о себе и о своём доме . . ."
    mai ". . . Но ты не рассказываешь мне, кто ты и откуда . . ."
    me ". . . Чего ты от меня ожидаешь? . . ."
    me ". . . Что я какой-то великий воин или вроде того? . . ."
    mai ". . . Дело не только в этом ... . . ."
    mai ". . . Ты подвергаешь мою деревню опасности, угрожаешь мне и моему народу . . ."
    mai ". . . Я не могу тебе доверять . . ."
    "Какая дерзкая девчонка."
    me ". . . То есть ты хочешь сказать ... . . ."
    me ". . . что не вернёшь мне мой нож? . . ."
    maishawnee ". . . {rb}{i}Ноолеви-а...{/i}{/rb}{rt}(Заткнись){/rt} . . ."
    "Она снова рычит что-то на шауни."
    me ". . . В последний раз — говори на грёбаном английском . . ."
    "Бормочу я в ответ."
    "Но она не даёт мне ответа."
    "Вместо этого я получаю ее обычную реакцию ..."
    "Мая молча на меня смотрит с обманчивым выражением лица."
    me ". . . {i}Хааа ...{/i} . . ."
    
    play sound3 "se/brush.ogg"
    scene barn
    with dissolve4
    
    "Я откидываюсь назад, решив оставить её в покое."
    "Даже после того, как вернул одеяло, я получаю только досаду."
    "Ладно. Если она не хочет со мной разговаривать, я и подавно."
    
    play sound3 "se/brush.ogg"
    
    "Откидываясь назад, я съёживаюсь, чтобы согреться."
    "Потеряв одеяло, я снова чувствую сильный холод."
    "Мои мышцы отчаянно ноют, и я сворачиваюсь клубком, чтобы сохранить хоть какое-то тепло."
    "Может, стоит разжечь небольшой костёр ..."
    "Нет ... здесь это, наверное, не лучшая идея."
    "Я не хочу рисковать, сжигая своё единственное укрытие."
    "В таком случае, я мог бы допить остатки рома."
    "Хотя, если могу, лучше приберегу его для другого случая ..."
    "Но у меня может не быть выбора."
    "Пока я сижу, мой взгляд блуждает по другой стороне сарая."
    "Может, там завалялось запасное одеяло или что-то вроде того, спрятанное в одном из этих ящиков?"
    "Наверное, стоит поискать ..."
    
    play sound3 "se/mud.ogg"
    
    "Вставая, я направляюсь к куче хлама."
    
    play sound4 "se/rummage.ogg"
    
    "Отбросив немного мусора в сторону, я осматриваю затхлую кучу."
    "Сколотые вазы ... сломанные инструменты ..."
    "Неужели в этой дыре нет ничего ценного?"
    "Мая молча наблюдает, пока я лавирую между ящиками и бочками."
    "Странный ребёнок ..."
    
    stop sound3 fadeout 1.0
    play sound4 "se/rummage.ogg"
    
    "Я роюсь в хламе, покрываясь пылью и грязью."
    me ". . . Давай же ... тут должно быть хоть что-то ... . . ."
    "После нескольких минут поисков я наконец нахожу то, что искал."
    "Прижатая к одной стороне, под какими-то ящиками, лежит старый рваный платок."
    me ". . . Даа . . ."
    
    play soundfx4 "se/creak.ogg" fadein 3.0
    play sound3 "se/box.ogg"
    play sound2 "se/rip.ogg"
    scene barn
    with hpunch
    
    "Я начинаю тянуть тряпку, надеясь освободить её."
    "Когда я дёргаю, я встречаю сопротивление, и платок натягивается."
    me ". . . Хм ... . . ."
    "Должно быть, он за что-то зацепился внутри одного из ящиков."
    "Может, за гвоздь или зазубренный край дерева ..."
    
    play sound3 "se/box.ogg"
    play sound4 "se/rip.ogg"
    scene barn
    with hpunch
    
    "Я снова хватаю его и борюсь. Но платок не поддаётся."
    "Сложенные ящики шатаются."
    
    play sound2 "se/brush.ogg"
    play sound4 "se/mud.ogg"
    show mai normal at rightend
    with easeinright
    stop sound2 fadeout 1.0
    stop sound4 fadeout 1.0
    
    me ". . . Хмм ... может, если потянуть в эту сторону . . ."
    "Дёргая влево и вправо, я пытаюсь расшатать платок."
    
    play sound3 "se/box.ogg"
    play sound4 "se/rip.ogg"
    scene barn
    show mai normal at rightend
    with hpunch
    
    "Но он не освобождается."
    "Я делаю шаг назад и вытираю пот со лба."
    me ". . . Придётся потрудиться ... . . ."
    "Сцепив ладони, я дышу на них и тру друг о друга."
    "Если я немного согреюсь, то должен справиться."
    
    play sound2 "se/mud.ogg"
    pause 0.1
    stop sound2 fadeout 3.0 
    
    "Но, осмотревшись, я замираю."
    "Краем глаза я замечаю девчонку."
    "Мая ждёт за ближайшей балкой и наблюдает за мной, пока я работаю."
    "Неужели она думает, что я её там не вижу?"
    me ". . .  . . ."
    mai ". . .  . . ."
    "Она молча на меня смотрит."
    "Этой девчонке действительно нужно какое-нибудь занятие ..."
    
    play sound2 "se/mud.ogg"
    pause 0.1
    stop sound2 fadeout 3.0
    
    "Возвращаясь к платку, я вытираю руки и снова хватаюсь за него."
    
    play sound3 "se/rip.ogg"
    play sound4 "se/box.ogg"
    scene barn
    show mai normal at rightend
    with hpunch
    
    "Я дёргаю ткань, пытаясь расшатать её."
    "Пыль и паутина сыплются вниз, покрывая мои волосы лёгкой пыльцой."
    "Но тряпка остаётся плотно зажатой между тяжёлыми ящиками."
    
    play sound4 "se/mud.ogg"
    show mai normal at right05
    with ease
    stop sound4 fadeout 1.0
    
    "На мгновение я останавливаюсь и смотрю на девчонку."
    "Она тихо подкрадывается ближе ко мне."
    "Она что, попытается подкрасться и напугать меня?"
    "Или ей просто интересно, чем я занят?"
    me ". . . Что тебе? . . ."
    "Я окликаю её."
    
    play sound2 "se/run.ogg"
    show mai worry
    pause 0.1
    hide mai
    with easeoutright
    stop sound2 fadeout 2.0
    
    "Мая отскакивает назад, прячась из виду."
    me ". . . Эй. Я всё ещё тебя вижу . . ."
    
    show mai normal at rightend
    with easeinright
    
    "Девчонка наблюдает за мной из своего укрытия с любопытством."
    mai ". . .  . . ."
    "Никакого ответа."
    "Что за жуткий ребёнок ..."
    "Что ж, раз она не даёт мне своё одеяло, я заберу это."
    
    play sound4 "se/box.ogg"
    play sound3 "se/rip.ogg"
    scene barn
    show mai normal at rightend
    with hpunch
    
    "Я снова тяну платок, но безуспешно."
    "Сверху раздаётся скрип, когда я сжимаю и выкручиваю ткань."
    
    play sound2 "se/mud.ogg"
    hide mai
    with easeoutright
    stop sound2 fadeout 1.0
    
    "Мая осторожно уходит из виду, пока ящики стонут под напряжением."
    me ". . . Чёрт! Почему ... ты не поддаёшься ... . . ."
    
    play sound3 "se/rip.ogg"
    play sound4 "se/box.ogg" loop
    scene barn
    with hpunch
    
    "Я в панике смотрю вверх, когда тяжёлые ящики начинают шататься и падать."
    
    stop soundfx4 fadeout 3.0
    play sound2 "se/crash.ogg"
    play sound3 "se/rip.ogg"
    play sound4 "se/rummage.ogg"
    scene barn
    with hpunch
    with vpunch
    with hpunch
    with vpunch
    pause 0.5
    queue sound5 "se/wash.ogg"
    queue sound3 "se/collapse.ogg"
    scene barn
    with vpunch
    queue sound3 "se/collapse.ogg"
    
    "Я дёргаю тряпку, она рвётся, и составленные ящики с грохотом обрушиваются вниз."
    "Реагируя быстро, я пытаюсь выпрыгнуть из-под удара."
    "Но один из ящиков врезается мне в плечо и с глухим стулом сбивает меня с ног."
    "С плеском приземляясь в грязь, платок улетает вместе со мной."
    me ". . . {i}Уххх ...{/i} . . ."
    
    play sound4 "se/mud.ogg"
    show mai happy
    with dissolve
    stop sound4 fadeout 3.0
    
    "Мая появляется, невредимая, из-за балки."
    mai ". . . {i}Фу-фу-фу ...{/i} . . ."
    "С широкой улыбкой на лице индейка торжествующе смеётся."
    me ". . . Эй! Ничего смешного! . . ."
    maishawnee ". . . {rb}{i}Псай-ви не-нот-ту!{/i}{/rb}{rt}(Великий воин, ничего не скажешь!){/rt} . . ."
    "Она продолжает смеяться и насмехаться надо мной на шауни."
    me ". . . Я мог серьёзно пострадать, знаешь ли ... . . ."
    
    show mai happy2
    with dissolve
    
    "В любом случае, я думал, она не разговаривает со мной ..."
    "Нахмурившись, я осматриваю своё тело на предмет травм."
    
    show mai normal
    with hpunch
    
    "Выгибая шею, я чувствую острую боль в спине и замираю."
    me ". . . Чёрт ... . . ."
    "Что, если я повредил что-то важное?"
    "В этот раз я мог действительно сильно покалечиться."
    "Я пытаюсь пошевелить головой, но по позвоночнику проходит удар, выводящий меня из строя."
    me ". . . Гаа ... . . ."
    "Сдаюсь. Всё, конец."
    "Я умру здесь, в этом затхлом старом сарае, с безумной индейской девчонкой, которая на меня пялится."
    mai ". . .  . . ."
    "Мая наклоняет голову с любопытством."
    me ". . . Что? . . ."
    
    play sound3 "se/brush.ogg"
    play sound4 "se/mud.ogg"
    show mai normal large
    with dissolve
    stop sound4 fadeout 3.0
    
    "Подойдя ближе, девчонка кладёт руку мне на челюсть."
    me ". . . Ты что ... . . ."
    "Медленно она начинает проводить ладонями по моим скулам и вниз по груди."
    "Мая осторожно ощупывает меня на предмет шишек и ушибов, тыкая в мою кожу."
    me ". . . Ты действительно странная ... . . ."
    "Я терпеливо жду, пока меня осматривают, слегка морщась от боли."
    "Следуя за её взглядом, я тоже проверяю себя на повреждения."
    "Кожа выглядит неповреждённой. Ни заноз, ни порезов ..."
    "Когда она надавливает на мои мышцы, я не чувствую сильной боли."
    "Плечо слегка ноет, но я не думаю, что сломал его или что-то в этом роде."
    me ". . . Хм ... . . ."
    "Возможно, повреждения были не слишком серьёзными."
    "Взяв мои вытянутые руки, Мая поворачивает их несколько раз."
                                      
    play sound4 "se/mud.ogg"
    show mai normal
    with dissolve
    stop sound4 fadeout 3.0
    
    "Затем ребёнок делает шаг назад."
    mai ". . .  . . ."
    "Она завершает своё исследование тихим взглядом, отпуская мои руки."
    me ". . . Э ... и всё? . . ."
    "Пока я это спрашиваю, я обнаруживаю, что могу снова двигаться, хоть и с болью."
    "Я поворачиваю голову так и сяк, боль в спине тихо отступает."
    "Возможно, я драматизировал ..."
    "Наверное, со мной всё в порядке."
    "Но всё равно будет болеть несколько часов ..."
    me ". . . И всё же, это было чертовски близко . . ."
    "Кусочки дерева лежат разбитые в грязи, пока пыль оседает."
    "Гвозди и щепки тонут в лужах, а солома прилипает к моей заднице."
    "Я действительно устроил здесь беспорядок."
    "Но по крайней мере теперь у меня будет чем согреться."
    me ". . . Платок ... . . ."
    "Ткань с узором выскальзывает из моих пальцев, когда я сжимаю его."
    "Взглянув на предполагаемое одеяло в своей руке, я нахожу только лоскуты разорванной материи."
    "Оно уничтожилось, как только я его выдернул."
    me ". . . {i}Хааа ...{/i} . . ."
    "Испустив вздох, я бросаю испорченную тряпку на грязный пол."
    "Почему сегодня ничего не идёт как надо?"
    
    play sound2 "se/mud.ogg"
    pause 0.1
    stop sound2 fadeout 2.0
    
    "Сидя, промокший, в луже, я свешиваю голову в знак поражения."
    "Не знаю, зачем я стараюсь ..."
    "Постепенно я понимаю, что девчонка всё ещё смотрит на меня."
    me ". . . Что ... такое ... . . ."
    "Бормочу я, ожидая ответа почему-то."
    
    play sound3 "se/brush.ogg"
    
    "Мая протягивает руку и кладёт её мне на здоровое плечо."
    "Нежным движением она похлопывает меня."
    "Она пытается меня подбодрить?"
    "Индейка ничего не говорит, прислонившись ко мне."
    "Её глаза устремлены на мою больную руку и на перевязанную рану."
    me ". . . Значит ... ты меня простила? . . ."
    "Спрашиваю я с улыбкой."
    
    show mai angry
    with dissolve
    
    "Как будто внезапно вспомнив, Мая принимает решительное выражение лица."
    mai ". . . {i}Хмф!{/i} . . ."
    
    play sound2 "se/mud.ogg"
    hide mai
    with dissolve
    
    "Девчонка разворачивается и снова направляется в свой угол."
    "Должно быть, она довольно забывчивая. Либо же она просто глупая ..."
    "Я её хорошо насмешил, и она осмотрела меня на предмет травм."
    "Она вообще на меня злится? Или это уже просто для виду?"
    
    stop sound2 fadeout 3.0
    
    "Прежде чем дойти до своей стороны сарая, индейка останавливается на полпути."
    
    play sound4 "se/thunder.ogg"
    
    "Очередной раскат грома звучит вдалеке."
    
    show mai sad
    with dissolve
    stop sound4 fadeout 5.0
    
    "На секунду она поворачивается и смотрит на меня встревоженным лицом."
    mai ". . .  . . ."
    "Или, может, она действительно боится громких звуков?"
    "Возможно, она искала отвлечения от бури."
    "Мая ждёт несколько мгновений, словно смотрит сквозь меня."
    
    play sound2 "se/mud.ogg"
    hide mai
    with dissolve
    stop sound2 fadeout 3.0
    
    "Затем, собравшись с духом, она уходит прочь."
    "В своём углу ребёнок сворачивается клубочком и отворачивается от меня."
    "Погружённая в свои мысли, она смотрит, как ледяной дождь барабанит по деревянным панелям."
    "Прямо сейчас она снова выглядит ужасно маленькой."
    me ". . .  . . ."
    
    play sound3 "se/brush.ogg"
    
    "Медленно я ползу по земляному полу к своему месту на сене."
    "Каждое маленькое движение причиняет боль, пока я продвигаюсь дюйм за дюймом."
    "Усевшись на сухую солому, я хватаюсь за её стебли и пытаюсь укрыться."
    "Это лучшее, что я могу сделать сейчас."
    "Даже если из-за этого я похож на повреждённое пугало ..."
    "Снаружи дождь продолжает идти, пока гром грохочет вдалеке."
    "Сидя там, я чувствую, как мои веки постепенно становятся всё тяжелее и тяжелее."
    "После всего, через что я прошёл, я заслуживаю хотя бы короткого сна."
    "Не похоже, чтобы девчонка собиралась что-то выкинуть."
    "Давайте заляжем на дно и посмотрим, простит ли она меня через несколько часов ..."
    "Мой пульс замедляется, и я начинаю считать удары."
    
    stop sound3 fadeout 3.0
    stop music fadeout 5.0
    
    "Мягко я погружаюсь в глубокий и целительный сон..."
    
    stop soundfx fadeout 5.0
    stop soundfx2 fadeout 5.0
    stop soundfx3 fadeout 5.0
    $ mouse_visible = False
    scene black
    with dissolve2
    pause 2.0
    scene caveback
    with dissolve4
    $ mouse_visible = True
    play soundfx "se/fire.ogg" fadein 10.0
    
    "{i}Обри...{/i}"
    "Голос эхом разносится."
    "{i}Обри...{/i}"
    "Это тот самый преследующий сон, который я всегда вижу ..."
    "Видения, которые никогда не покидают меня ..."
    "Голос зовёт, пересказывает мне истории ..."
    "И светящиеся фигуры, танцующие в огне ..."
    
    show cave 1
    with dissolve4
    play music "music/wandering.ogg"
    
    "{i}Давным-давно жила женщина, которая была совсем одна в своей деревне.{/i}"
    "{i}Она была молода и прекрасна; возможно, прекраснейшая женщина из всех, кто когда-либо жил.{/i}"
    "{i}Каждый день она расчёсывала свои длинные, густые волосы орлиным маслом.{/i}"
    "{i}Её пышное тело окрепло на оленине.{/i}"
    "{i}Кожа была мягкой, как кукурузный шёлк, а глаза — пронзительными.{/i}"
    "{i}Мужчины её племени предлагали ей дары из мяса и украшений.{/i}"
    "{i}Но женщина всегда отказывалась.{/i}"
    "{i}Она и сама лучше всех знала — она слишком прекрасна для какого попало мужчины.{/i}"
    "{i}И потому она жила одна, любуясь собственной красотой.{/i}"
    
    show cave 9
    with dissolve4
    
    "{i}Много месяцев прошло, пока она проводила время в одиночестве.{/i}"
    "{i}Сидя у озера, она смотрела на своё отражение в чистом блаженстве.{/i}"
    "{i}Она была слишком хороша, чтобы быть как все. Она была слишком прекрасна.{/i}"
    "{i}Но затем ... всё изменилось ...{/i}"
    "{i}Однажды она встретила таинственного мужчину.{/i}"
    
    show cave 2
    with dissolve4
    
    "{i}Она несла свои тяжёлые нарубленные дрова из леса.{/i}"
    "{i}Он заметил её по пути домой и неотступно преследовал.{/i}"
    "{i}Этот мужчина шёл за ней от самой реки до самой её деревни.{/i}"
    "{i}'Дева, позволь помочь тебе с твоей ношей,' — сказал он, догоняя.{/i}"
    "{i}Застигнутая врасплох, она не знала, что сказать.{/i}"
    "{i}Она была слишком взволнована, чтобы даже взглянуть ему в глаза.{/i}"
    "{i}Всё, что она могла — это улыбаться.{/i}"
    "{i}Он понёс нарубленные дрова для неё.{/i}"
    "{i}Он понёс корзины с водой с кукурузных полей для неё.{/i}"
    "{i}Мужчина заботился о ней, и она стала полагаться на него.{/i}"
    "{i}Проводя с ним время, она незаметно наблюдала за ним.{/i}"
    "{i}Этот мужчина был не похож ни на кого, кого она знала прежде.{/i}"
    "{i}Его пронзительные карие глаза несли доброе выражение.{/i}"
    "{i}Перья, вплетённые в его волосы, казалось, парили с каждым его шагом.{/i}"
    "{i}Его длинные волосы, длиннее её собственных, развевались за ним, когда он шёл рядом с ней, словно дым, гонимый ветром.{/i}"
    "{i}В первый раз в жизни девушка была поглощена кем-то, кроме себя.{/i}"
    "{i}'Позволь пригласить тебя в мой дом, познакомиться с моей семьёй.'{/i}"
    "{i}Его сильный голос поглотил её целиком, когда он говорил.{/i}"
    "{i}Этот мужчина, которым она начала восхищаться ... он имел над ней какую-то власть.{/i}"
    "{i}И прекрасная девушка последовала за ним.{/i}"
    "{i}Она не могла смотреть в его бегающие глаза, но всё это время улыбалась.{/i}"
    
    hide cave 2
    with dissolve4
    show cave 3
    with dissolve4
    
    "{i}Когда она прибыла в его дом, они оказались вдвоём.{/i}"
    "{i}Его семьи, должно быть, нет в данный момент. Это было оправданием.{/i}"
    "{i}Он рассказал ей о двух своих сёстрах и своей матери.{/i}"
    "{i}Они были дружной семьёй. Все жили вместе, как один народ ...{/i}"
    "{i}Чем больше он говорил, тем больше она восхищалась этим мужчиной и его острыми чертами.{/i}"
    "{i}Она желала остаться здесь. Она больше не могла вернуться в свой старый дом.{/i}"
    "{i}И потому она осталась с этими людьми, ибо они ценили её и нуждались в её обществе.{/i}"
    "{i}Женщина приняла этого сильного мужчину как своего мужчину и стала одной из них.{/i}"
    
    show cave 9
    with dissolve4
    
    "{i}Их жизнь была спокойной.{/i}"
    "{i}Эти люди жили сплочённо, счастливо делясь друг с другом.{/i}"
    "{i}Но со временем прекрасная девушка почувствовала, что здесь что-то не так ...{/i}"
    "{i}Временами, когда она хотела гулять, её мужчина запрещал ей.{/i}"
    "{i}За лесом скрывалось нечто спрятанное. Но она не должна была знать.{/i}"
    "{i}По ночам слышалась возня.{/i}"
    "{i}Иногда она просыпалась и замечала, что семья сплелась в каких-то странных объятиях.{/i}"
    "{i}В другие же разы они просто смотрели на неё своими пронзительными глазами и улыбались ...{/i}"
    
    show cave 4
    with dissolve4
    
    "{i}Однажды её мужчина вернулся с охоты позже обычного ...{/i}"
    "{i}Его руки были в крови и порезах, волосы спутались в колтуны, мокасины разорваны ...{/i}"
    "{i}Он был измучен. Слишком измучен, чтобы продолжать.{/i}"
    "{i}Он лёг на свою постель, положив голову на колени своей прекрасной женщины.{/i}"
    "{i}Она гладила его волосы, чувствуя усталость его духа.{/i}"
    "{i}Охота прошла неудачно, и, погнавшись за оленем к обрыву, он упал с большой высоты.{/i}"
    "{i}Раненый и разбитый, мужчина был недолгим гостем в этом мире.{/i}"
    "{i}Прекрасная женщина ощутила великую печаль, глядя на своего прекрасного мужчину ...{/i}"
    "{i}Пока она обрабатывала его раны, её муж корчился от боли.{/i}"
    "{i}Именно тогда она заметила, что его тело меняется ...{/i}"
    
    show cave 9
    with dissolve4
    
    "{i}Его дыхание замедлилось, когда он забился в конвульсиях и превратился в гигантского зверя.{/i}"
    "{i}Челюсть вывихнулась и растянулась, когда пара чудовищных клыков опустилась вниз.{/i}"
    "{i}Прекрасная женщина почувствовала, как волосы, которые она гладила, сжимаются в чешую, покрывшую его голову.{/i}"
    "{i}Длинный хвост обвился вокруг девушки, пока пара тёмно-золотых глаз вглядывалась в неё.{/i}"
    
    show cave 7
    with dissolve4
    
    "{i}Он превратился в скользкого, извивающегося змея.{/i}"
    "{i}Опрокидывая одеяла и круша горшки, монстр зашипел, а его раздвоенный язык втягивался и высовывался.{/i}"
    "{i}Всё ещё ослабленный, он не мог удержать её своей хваткой.{/i}"
    "{i}Она осторожно выскользнула из-под его массивной клыкастой головы и выбралась наружу.{/i}"
    
    hide cave 7
    with dissolve4
    show cave 8
    with dissolve4
    
    "{i}Змей увидел испуганное выражение лица женщины и последовал за ней.{/i}"
    "{i}'Мы — Змее-Люди. Мы хорошие люди и желаем тебе только добра.'{/i}"
    "{i}Женщина задрожала, споткнувшись и упав навзничь.{/i}"
    "{i}'Любовь моя, останься здесь, со мной, навсегда! Я буду любить тебя вечно!'{/i}"
    "{i}Скользящий монстр подбирался всё ближе.{/i}"
    "{i}'Если ты должна уйти, то уходи быстро.'{/i}"
    "{i}'Но я найду тебя и верну туда, где тебе место.'{/i}"
    "{i}Змей зашипел и захохотал, пока женщина отчаянно развернулась и бросилась прочь.{/i}"
    "{i}'Беги! Беги и уходи быстро! Не оглядывайся!'{/i}"
    
    hide cave 8
    with dissolve4
    show cave 1
    with dissolve4
    
    "{i}Прекрасная женщина бежала, а монстр медленно следовал за ней.{/i}"
    "{i}Её ноги топтали луга и леса.{/i}"
    "{i}Когда она достигла опушки леса, она поняла, почему туда было запрещено ходить.{/i}"
    "{i}Длинные полосы мёртвой змеиной кожи лежали в грязи.{/i}"
    "{i}Это место было гнездовьем змеев, а она должна была стать их добычей.{/i}"
    "{i}Плача от страха, женщина услышала шипение позади себя и снова побежала.{/i}"
    "{i}По холмам и равнинам она мчалась, отчаянно пытаясь сбежать.{/i}"
    "{i}Сначала её ноги двигались быстро; но затем, когда она думала о своём хорошем мужчин ...{/i}"
    "{i}... о его доброте, о его умениях ...{/i}"
    "{i}... она замедлилась.{/i}"
    "{i}Её разум спорил с её сердцем.{/i}"
    "{i}Как она могла убежать от такого прекрасного и доброго мужчины?{/i}"
    "{i}В конце концов она поняла, что потеряла зверя где-то позади себя.{/i}"
    "{i}Остановившись, желая перевести дух, девушка села отдохнуть.{/i}"
    "{i}Она устала и решила закрыть глаза и помолиться.{/i}"
    "{i}На холмике она оставалась в тишине, постепенно чувствуя, как энергия покидает её тело.{/i}"
    
    show cave 9
    with dissolve4
    
    "{i}И там ей приснился сон...{/i}"
    "{i}... тихий сон ...{/i}"
    "{i}Обри ...{/i}"
    
    stop music fadeout 7.0
    hide cave 1
    with dissolve4
    
    "Медленно видение испаряется, исчезая ..."
    "История о женщине и змее угасает, и моя голова становится тяжёлой ..."
    "Голос становится тише, нежно взывая ко мне из бездны."
    "{i}Обри ...{/i}"
    
    stop soundfx fadeout 3.0
    $ mouse_visible = False
    scene black
    with dissolve4
    pause 2.0
    scene barn night
    with dissolve4
    $ mouse_visible = True
    play soundfx2 "se/rain_in.ogg" fadein 3.0
    
    "Я просыпаюсь с испугом от своего сна."
    "Сделав несколько глубоких вдохов, я чувствую горячий пот, стекающий по моему лбу."
    "Что это я видел?"
    me ". . . Женщина ... змей ... . . ."
    "Тот же самый странный лихорадочный сон."
    "Тот, что мне снится каждую ночь уже целый год ..."
    me ". . . Я проклят ... Должно быть . . ."
    "Я не уверен, когда заснул, но, должно быть, уже темнело."
    "Если нужно угадать, я бы сказал, что сейчас за полночь."
    "Вглядываясь в темноту, мои глаза медленно привыкают к мраку."
    "Тени и отражения дождевых капель проецируются на стены сарая снаружи."
    "Хотя небо затянуто тучами, луна, должно быть, ярко светит из-за облаков."
    
    play sound2 "se/brush.ogg"
    
    "Когда я пытаюсь пошевелиться, я чувствую тяжесть, прижимающуюся ко мне."
    me ". . . Хм ... . . ."
    
    $ mouse_visible = False
    window hide
    play music "music/leafshade.ogg" fadein 10.0
    scene cg3
    with dissolve2
    pause 2.0
    window show
    $ mouse_visible = True
    $ achievement.grant("NEW_ACHIEVEMENT_1_2")
    
    "Я обнаруживаю, что Мая положила голову мне на здоровое плечо."
    "Её маленькая грудь мягко вздымается и опускается, когда она дышит."
    "Чтобы дотянуться до моего плеча, она подпёрлась старым ящиком из-под сидра."
    me ". . . Эй . . ."
    "Я слегка подталкиваю её, пытаясь разбудить."
    mai ". . . {i}Ухх ...{/i} . . ."
    "Мая издаёт тихий звук, но не просыпается."
    "Прижимаясь щекой к моему плечу, девочка тихо спит, больше не шевелясь."
    me ". . . Какая наглая паршивка ... . . ."
    "В благодарность за то, что я служил ей подушкой, наверное, я прощён."
    me ". . . Ладно ... поступай как знаешь ... . . ."
    "Тихо бормочу я."
    mai ". . . {i}Ннн ...{/i} . . ."
    "Мая издаёт ещё один тихий звук, и намёк на улыбку мелькает на её губах."
    "Для воровки-паршивки она выглядит довольно мило, когда так спит."
    me ". . .  . . ."
    "О чём я только думаю ..."
    "Стараясь не двигаться, я оглядываюсь вокруг."
    "У наших ног я замечаю, что одеяло снова завязано в узел."
    "Священные предметы, скорее всего, снова завёрнуты внутрь."
    "Я думаю развязать его, но это уже будет слишком."
    "Проверив свою левую руку, я замечаю, что повязки сменили."
    "Она перевязала рану, пока я спал?"
    me ". . . {i}Ты что ...{/i} . . ."
    "Я начинаю шептать, но осекаюсь."
    "Откинув голову назад, я слушаю дождь за окном."
    "Эта буря бушует уже больше двадцати четырёх часов."
    "Но {i}стук{/i} капель звучит немного легче, чем раньше ..."
    "Возможно, к утру стихнет."
    mai ". . . {i}Ннн!{/i} . . ."
    "Мая медленно начинает просыпаться."
    mai ". . . {i}Обри ...{/i} . . ."
    me ". . . {i}Мая?{/i} . . ."
    "Я подталкиваю её, но она, кажется, снова погружается в сон."
    "Что ж, хорошая компания ..."
    me ". . .  . . ."
    "Она потерялась и пытается найти свою семью."
    "Интересно, сможет ли она добраться, когда дождь стихнет ..."
    "Будет ли её семья рада её видеть?"
    "Сможет ли она вернуться к спокойной жизни после своего пленения?"
    me ". . . {i}Деревня шауни ... да ...{/i} . . ."
    "Звучит как мирное местечко."
    "Она на юге, у озера, глубоко на индейской территории."
    "Ничего, кроме лесов и полей на многие мили вокруг ..."
    me ". . .  . . ."
    me ". . . {i}ничего на многие мили вокруг ...{/i} . . ."
    "Внезапно меня осеняет мысль."
    "Что, если я провожу её до дома?"
    "Здесь опасная глушь, повсюду торчат лагеря синих мундиров."
    "Если мы будем держаться вместе, это может быть нам на руку ..."
    "А деревня Маи могла бы стать хорошим местом, чтобы передохнуть несколько дней."
    "Я могу обменять мундир на припасы и карты, проложить маршрут ..."
    "Тогда я смогу отправиться вниз по течению на юг, к свободе."
    "Это даст мне цель, когда взойдёт солнце."
    "И это значит, что я смогу держаться подальше от главных дорог, которыми пришлось бы добираться до городов янки."
    mai ". . . {i}Хмм ...{/i} . . ."
    "Я смотрю на маленькую индейскую девчонку, пока она пускает слюни на моё плечо."
    "Индейцы шауни вряд ли захотят, чтобы английский солдат долго прятался в их деревне."
    "Но если я верну её в целости, они могут даже наградить меня за старания."
    "Меха, золото ... может, даже невесту ..."
    me ". . . {i}Эй, Мая ... у тебя есть сестра?{/i} . . ."
    "Шепчу я в шутку."
    mai ". . .  . . ."
    "Она слишком глубоко спит, чтобы ответить."
    "В общем, неплохая идея."
    "Лучше иметь хоть какие-то козыри на пути на юг, чем не иметь никаких."
    "Мне нужно будет поговорить с девчонкой утром."
    "Подвести её к этой мысли ..."
    "Мне меньше всего нужно её спугнуть."
    mai ". . . {i}Ннн ...{/i} . . ."
    "А если она не захочет, чтобы я шёл с ней?"
    "Что тогда?"
    "Возможно, она меня ещё не простила. Может, она просто использует меня как подстилку."
    "Что ж, я всегда могу идти следом ..."
    "Выслеживать её передвижения ..."
    "Мы оба движемся на юг и избегаем войск янки, так что будем идти по одним и тем же дорогам."
    "Было бы глупо не держаться вместе хотя бы часть пути."
    me ". . . {i}какой же глупый план ...{/i} . . ."
    "И всё же это лучше, чем ничего."
    
    scene barn night
    with dissolve4
    
    "Над затхлым сараем витает спокойная атмосфера."
    "Дождь всё ещё льёт снаружи, пока Мая спит, прижавшись ко мне."
    me ". . .  . . ."
    "Может, мне стоит рассказать ей о битве на реке {i}Темза{/i}."
    "Возможно, я обязан ей этим после всего ..."
    "Она ребёнок, но в чём-то я чувствую, что должен немного поверить в неё."
    "Мая сама сказала — она не может мне доверять."
    "Я не чувствовал, что ей нужно знать обо всём этом."
    "Мы из разных миров. Чем меньше мы взаимодействуем, тем лучше."
    "Вот что я думал."
    "Наверное, я был с ней недостаточно деликатен ..."
    me ". . . {i}Господи, Обри ... ты становишься мягкотелым ...{/i} . . ."
    "Бормочу я вслух сам себе."
    "И всё же я не мог предсказать, насколько доверчивой окажется маленькая девочка."
    "То есть, я наставил на неё ружьё, а она не шелохнулась."
    
    scene cg3
    with dissolve4
    
    mai ". . . {i}Обри ...{/i} . . ."
    "Она снова произносит моё имя."
    "Потерявшись в своих мыслях, я почти подскакиваю от неожиданности."
    me ". . . {i}Что такое?{/i} . . ."
    "Она просыпается?"
    maishawnee ". . . {rb}{i}... хапикамите ...{/i}{/rb}{rt}(Суп){/rt} . . ."
    "Ребёнок бормочет что-то на шауни и снова погружается в сон."
    "Я смотрю на неё в недоумении несколько мгновений."
    "Затем начинаю улыбаться и пытаюсь тихо подавить смешок."
    me ". . . {i}какая же глупость ...{/i} . . ."
    "Что я вообще здесь делаю?"
    "В самом деле! Что происходит?"
    "Если бы кто-нибудь из моего полка увидел меня в таком виде ..."
    "Что ж, скажем так, мне бы этого никогда не забыли."
    "Стараясь оставаться неподвижным, я откидываюсь назад и усмехаюсь про себя."
    
    stop music fadeout 5.0
    
    "Слушая падающий за окном ледяной дождь, я гадаю, что принесёт завтрашний день..."
    
    stop soundfx2 fadeout 5.0
    scene black
    with dissolve4
    $ mouse_visible = False
    pause 2.0
    scene barnday
    with dissolve4
    $ mouse_visible = True
    play soundfx4 "se/barninterior.ogg"
    play sound3 "se/brush.ogg"
    
    "Когда я просыпаюсь следующим утром, дождь уже перестал лить."
    "Снаружи небо всё ещё серое и затянуто облаками."
    "Взглянув вниз, я вижу, что Мая уже встала раньше меня."
    me ". . . Хм ... . . ."
    "Как досадно ..."
    "Я хотел посмотреть, будет ли ей неловко за то, что она спала на моём плече."
    "Зевая, я оглядываю сарай, но девчонки нигде нет."
    "Сажусь и прислушиваюсь."
    me ". . . Мая ... . . ."
    "Я думал, она, может, вырезает что-то или возится с моими вещами."
    "Неужели она ушла, не сказав мне?"
    me ". . . Мая! . . ."
    "Я снова зову, но не получаю ответа."
    
    play soundfx3 "se/mud.ogg"
    
    "Постепенно я встаю и обыскиваю территорию."
    me ". . . Мая? Где ты? . . ."
    "Посмотрев на ящики из-под сидра, я не вижу её там."
    "Она не царапает балку и не сидит на корточках в ближайшем углу."
    "Где же она?"
    "Возможно, она отправилась в путь одна, как только дождь стих ..."
    "Технически, она не оправдала моих надежд вчера."
    "Хотя она и спала на моём плече, возможно, это было из удобства, а не из прощения."
    "Жаль. Я думал, может, она и я могли бы ..."
    me ". . .  . . ."
    "И всё же, возможно, она ещё не ушла."
    "Если она ждёт снаружи или просто пошла по дороге ..."
    "... может, я ещё смогу остановить её вовремя."
    
    stop soundfx3 fadeout 1.0
    play sound3 "se/brush.ogg"
    pause 0.5
    stop sound3 fadeout 2.0
    
    "Когда я направляюсь к двери, я слышу шорох поблизости."
    "Останавливаясь, оглядываюсь."
    me ". . . Мая? . . ."
    "Это донеслось оттуда, где те ящики ..."
    
    play soundfx3 "se/mud.ogg"
    play sound2 "se/rummage.ogg"
    
    "Перешагивая через кучу хлама, я пробираюсь к дальнему углу сарая."
    "Я вижу чёрные как смоль волосы, повязанные платком, и пару пуговиц-дисков, вплетённых в косички."
    
    stop soundfx3 fadeout 1.0
    play music "music/dandelions.ogg"
    show mai normal
    with dissolve
    
    "Это девчонка, прячущаяся из виду, сидя на корточках за какими-то разбитыми ящиками."
    me ". . . Мая! Вот ты где! . . ."
    mai ". . . Доброе утро . . ."
    "Она непринуждённо приветствует меня без хмурого взгляда."
    me ". . . Что ты здесь делаешь? . . ."
    mai ". . . Ищу верёвку . . ."
    me ". . . Верёвку? . . ."
    mai ". . . Она мне нужна . . ."
    "Она говорит это решительным тоном, не вдаваясь в подробности."
    "Я чувствую облегчение, видя, как она стоит на коленях, зарыв руки в старый хлам."
    me ". . . Я думал, ты могла сбежать ... . . ."
    
    show mai sad
    with dissolve
    
    mai ". . . С чего бы мне убегать? . . ."
    me ". . . Ну, я просто ... подумал, что ты могла . . ."
    "То есть ... после вчерашнего ..."
    
    show mai normal
    with dissolve
    
    mai ". . . Я пыталась тебя разбудить, но ты не шевелился . . ."
    mai ". . . Поэтому я подождала и начала искать верёвку . . ."
    me ". . . Зачем тебе верёвка? . . ."
    mai ". . . Она мне нужна . . ."
    "Сказано прямо, наверное, она не хочет вдаваться в подробности."
    me ". . . Мне снился сон ... . . ."
    mai ". . . Тебе приснился хороший сон? . . ."
    me ". . . Не очень ... . . ."
    "Это, можно сказать, кошмар — видеть, как женщина выходит замуж за змею."
    
    show mai sad
    with dissolve
    
    mai ". . . Ты в порядке? . . ."
    "Она принимает неуверенное выражение лица."
    me ". . . Со мной всё в порядке. Не беспокойся об этом . . ."
    mai ". . . Ты дрожал во сне . . ."
    me ". . . Я сказал, всё нормально . . ."
    "Меньше всего мне нужно, чтобы ребёнок беспокоился о моём самочувствии."
    
    show mai normal
    with dissolve
    
    mai ". . . Вот как ... . . ."
    me ". . . Вот так . . ."
    "Может, она думает, что ей сошло с рук то, что она спала на моём плече ..."
    mai ". . .  . . ."
    "Ну и ладно."
    mai ". . . Дождь кончился . . ."
    me ". . . А? Ах, да ... . . ."
    me ". . . Буря наконец закончилась . . ."
    "Между нами проходит несколько мгновений неловкого спокойствия."
    
    play sound2 "se/mud.ogg"
    show mai large normal
    with dissolve
    stop sound2 fadeout 3.0
    
    "Затем Мая тихо приближается ко мне."
    me ". . .  . . ."
    mai ". . .  . . ."
    "Она снова занимается своим молчаливым созерцанием, ожидая реакции."
    me ". . . Что такое? . . ."
    "Девчонка протягивает руку, предлагая мне что-то."
    "Там, зажатый в её грязной ладони, лежит мой нож."
    me ". . . Так ты обмениваешь его мне? . . ."
    mai ". . . Да . . ."
    
    play sound3 "se/brush.ogg"
    
    "Я беру своё лезвие и кладу его обратно в сапог, подальше с глаз."
    
    stop sound3 fadeout 1.0
    
    mai ". . . Вчера я не имела в виду то, что сказала ... . . ."
    me ". . . {i}'То, что сказала'{/i}? . . ."
    
    show mai large sad
    with dissolve
    
    mai ". . . Я сказала, что не доверяю тебе. Я выставила тебя плохим солдатом . . ."
    me ". . . Ах ... {i}это{/i} ... . . ."
    "Она извиняется за то, что игнорировала меня?"
    mai ". . . Я вела себя как ребёнок . . ."
    "Ты и есть ребёнок, так что не переживай об этом слишком сильно ..."
    mai ". . . Ты не мой враг. Ты хороший человек . . ."
    mai ". . . И я прощаю тебя за то, что ты взял моё {i}мишаами{/i} . . ."
    me ". . . Ааа ... . . ."
    mai ". . . Мне жаль . . ."
    "Вот она и сказала это ..."
    me ". . . Ну ... не переживай о таких вещах . . ."
    mai ". . . Я должна извиниться. Я должна исправить то, что сказала . . ."
    "Она серьёзно настроена, да?"
    me ". . . Слушай, ты украла мой нож, я украл твоё {i}мишаами{/i} . . ."
    me ". . . Мы наговорили друг другу гадостей ... . . ."
    me ". . . Я тоже ошибался, так что ... мы оба сожалеем . . ."
    "Я слегка запинаюсь."
    me ". . . Давай просто считать, что мы квиты . . ."
    "Пока это не стало ещё более странным ..."
    
    show mai large normal
    with dissolve
    
    mai ". . . {i}'Квиты'{/i}? . . ."
    me ". . . Ага. Я тебе не должен, и ты мне не должна . . ."
    me ". . . Начнём сначала . . ."
    "Она несколько мгновений смотрит на меня."
    
    show mai large happy
    with dissolve
    
    "Затем девчонка тепло улыбается."
    mai ". . . Согласна . . ."
    "Я чувствую лёгкий трепет внутри ... что-то вроде мотылька в животе."
    "Может, она и не такая уж паршивка в конце концов ..."
    me ". . . Договорились? . . ."
    mai ". . . Договорились . . ."
    
    play sound2 "se/mud.ogg"
    play sound3 "se/brush.ogg"
    hide mai
    with dissolve
    stop sound2 fadeout 3.0
    
    "Девчонка пока что поворачивается ко мне спиной и собирает свои вещи."
    "Привязав свою сумку к лямкам котомки, она позволяет {i}мишаами{/i} свисать под левой рукой."
    "Присев на корточки, она застёгивает свои маленькие красные ботинки, готовясь к путешествию."
    
    play sound2 "se/mud.ogg"
    show mai normal
    with dissolve
    stop sound2 fadeout 1.0
    
    "Встав, дитя шауни поворачивается ко мне лицом."
    mai ". . . Что ты планируешь делать? . . ."
    "Она сама завела эту тему ..."
    me ". . . Я? Посмотрим... . . ."
    "Я начинаю пересказывать свой первоначальный план."
    me ". . . Я направлюсь на юго-запад, к границам территории янки . . ."
    "По крайней мере достаточно далеко, чтобы меня не могли призвать или взять в плен."
    me ". . . Если смогу, попробую сначала добраться до {i}Винсенна{/i}. Купить припасы . . ."
    me ". . . После этого я навсегда избавлюсь от мундира и начну жизнь где-нибудь на новом месте . . ."
    me ". . . Может, буду работать в приграничном городке ... . . ."
    me ". . . На шахте или в лесозаготовительном лагере ... что-то вроде того ... . . ."
    "Я внезапно замолкаю."
    "Она заставила меня нести чушь, не осознавая этого ..."
    me ". . . В любом случае, а ты? Какие у тебя планы? . . ."
    mai ". . . Я пойду в свою деревню . . ."
    me ". . . Ты уверена, что найдёшь её сама? . . ."
    mai ". . . Она на юге, на озере у леса, и севернее {i}Фотвэйна{/i} . . ."
    mai ". . . Я должна добраться . . ."
    me ". . . Вашим людям действительно стоит научиться давать названия местам и записывать их ... . . ."
    
    show mai sad
    with dissolve
    
    mai ". . . Один синий мундир сказал мне, что это примерно пять дней пешком от {i}Фотшелби{/i}, откуда я сбежала . . ."
    me ". . . {i}Форт Шелби{/i}? . . ."
    "Я не уверен, где это."
    mai ". . . Вашим людям стоит давать своим поселениям лучшие названия ... . . ."
    me ". . . Принято . . ."
    
    show mai normal
    with dissolve
    
    me ". . . Значит, ты будешь идти на юг ещё несколько дней? . . ."
    "Если предположить, что она избегает главных дорог и сил синих мундиров в этом районе."
    mai ". . . Именно так . . ."
    me ". . . Тогда ... . . ."
    "Я обрываю себя на полуслове."
    mai ". . . Тогда? . . ."
    me ". . . Ну ... . . ."
    "Я нервно чешу затылок."
    me ". . . Ну ... раз мы движемся в одном направлении ... . . ."
    mai ". . . ? . . ."
    "Просто скажи это."
    me ". . . Ну, может, я смогу помочь тебе добраться до твоей деревни . . ."
    me ". . . Я имею в виду, у тебя наверняка есть припасы? Еда? . . ."
    me ". . . Я мог бы отдать твоим людям монеты за это . . ."
    mai ". . . Правда? . . ."
    me ". . . Или ты могла бы дать мне это бесплатно, раз я доставлю тебя домой в целости? . . ."
    
    show mai sad
    with dissolve
    
    mai ". . . Пожалуй, откажусь ... . . ."
    "Я начинаю криво усмехаться."
    
    show mai happy
    with dissolve
    
    "Медленно Мая тоже расплывается в улыбке."
    "Какой глупый разговор ..."
    me ". . . Ну? Что скажешь? . . ."
    me ". . . Хочешь побыть вместе ещё немного? . . ."
    
    show mai normal
    with dissolve
    
    "Я протягиваю свою руку."
    "Она смотрит на неё вниз, а затем вверх, мне в глаза."
    
    show mai happy2
    with dissolve
    
    mai ". . . Делай как знаешь... . . ."
    "Схватив мою руку своей, она крепко пожимает её, прежде чем отпустить."
    "На этом наш союз продолжится ещё немного."
    
    show mai normal
    with dissolve
    
    mai ". . . Только не жди, что мои родители тоже обменяют меня на монеты . . ."
    me ". . . Конечно нет ... Я не такой солдат ... . . ."
    
    show mai happy2
    with dissolve
    
    mai ". . . Вот как? . . ."
    "Я вспоминаю прошлую ночь, как сидел в темноте и размышлял в одиночестве."
    me ". . . И ... . . ."
    
    show mai normal
    with dissolve
    
    me ". . . И ... я расскажу тебе немного больше о себе . . ."
    me ". . . Если это то, что нужно, чтобы ты мне доверяла ... . . ."
    me ". . . Есть кое-какие вещи, о которых нам стоит поговорить . . ."
    mai ". . .  . . ."
    
    show mai happy2
    with dissolve
    
    mai ". . . Хорошо. Можешь рассказать мне о них, пока мы будем идти . . ."
    
    play sound2 "se/mud.ogg"
    hide mai
    with dissolve
    
    "Мая начинает брести прочь, заложив руки за спину."
    mai ". . . Ты точно не попытался бы меня купить? . . ."
    me ". . . Определённо нет . . ."
    me ". . . К тому же, ты не в моём вкусе. Я не интересуюсь паршивками-замухрышками . . ."
    mai ". . . {i}'Замухрышками'{/i}? . . ."
    me ". . . Забудь, ты всё равно не поймёшь . . ."
    mai ". . . {i}Пфуу!{/i} . . ."
    "Девчонка строит гримасу и показывает мне язык."
    
    stop sound2 fadeout 3.0
    stop music fadeout 5.0
    scene black
    with dissolve4
    
    "Собрав наши вещи, мы оба направляемся к двери сарая."
    me ". . . Подожди здесь, я проверю, чисто ли снаружи . . ."
    "Я готовлю ружьё, как будто подтверждая это."
    mai ". . . Снаружи никого нет . . ."
    me ". . . Что? . . ."
    mai ". . . Я не чувствую, чтобы кто-то двигался снаружи . . ."
    me ". . . Я лучше проверю сам, чем положусь на твои инстинкты . . ."
    
    play sound4 "se/brush.ogg"
    
    "Аккуратно подтолкнув Маю в сторону, я делаю короткий вдох и открываю дверь."
    
    stop sound4 fadeout 1.0
    stop soundfx4 fadeout 1.0
    play sound3 "se/barndoor.ogg"
    play music "music/aftertherain.ogg" noloop
    scene black
    with flash
    play soundfx "se/wind.ogg" fadein 10.0
    play sound2 "se/mud.ogg" fadein 3.0
    scene sky2
    show mist
    with dissolve
    
    "Выходя из сарая, я закрываю за собой деревянную дверь."
    "Мои кожаные сапоги медленно покрываются грязью, когда я делаю первые шаги наружу."
    "Пропитанная водой земля проседает под тяжестью моего тела."
    
    stop sound2 fadeout 2.0
    
    "Осматривая местность, я замечаю низкий туман, нависший в воздухе."
    "Слабый туман мягко льнёт к воздуху и заставляет мою тяжёлую одежду казаться влажной."
    "Проносится лёгкий ветерок, принося с собой противный холод."
    
    play sound2 "se/mud.ogg" fadein 3.0
    
    "Я плотнее закутываюсь в шинель и обхожу территорию."
    "Никаких признаков синих мундиров или фермеров."
    "Посмотрев на запад, затем на восток, я ничего не нахожу."
    
    stop sound2 fadeout 2.0
    
    "Никого в поле зрения."
    me ". . . Хорошо! Всё выглядит нормально . . ."
    
    play sound3 "se/barndoor.ogg"
    play sound2 "se/mud.ogg" fadein 3.0
    queue music "music/oddity.ogg"
    pause 0.5
    stop sound2 fadeout 2.0
    
    "Мая выходит наружу и встаёт рядом со мной."
    mai ". . . А я говорила, что снаружи никого нет . . ."
    me ". . . Ага, конечно... . . ."
    mai ". . . Я уже всё равно посмотрела . . ."
    me ". . . Что? . . ."
    mai ". . . Я проверила, пока ты собирал свои вещи . . ."
    "Наглость этого ребёнка ..."
    me ". . . Что ж, бережёного Бог бережёт ... . . ."
    "Я чувствую, как рука мягко тянет меня за рукав шинели."
    mai ". . . Мы идём? . . ."
    "Говорит Мая, невероятно ласково, с улыбкой."
    me ". . . Наглость ... . . ."
    
    play soundfx2 "se/mud.ogg" fadein 3.0
    
    "Кивнув, мы оба отправляемся в наше путешествие."
    
    scene black
    with dissolve4
    scene sky2
    show mist
    with dissolve4
    
    "Вместе мы идём по дороге и проходим мимо остатков заброшенной фермы."
    "Старые конюшни и лачуги составляют этот маленький пустынный квартал."
    "Один сарай полностью рухнул внутрь себя, а другие вот-вот последуют его примеру."
    "Древесина медленно гниёт, разрушаемая стихией без присмотра."
    "Развалившийся плуг прислонён к самодельному забору в ближайшем поле."
    "Присмотревшись, я замечаю, что металл начинает ржаветь."
    "Если хозяева вернутся скоро, он ещё может послужить. Если они вообще вернутся ..."
    "Этот пришедший в упадок военный театр, вероятно, уже не спасти."
    "Идя по мокрой тропе, мы проходим мимо таблички с ошибкой: {i}'NO TREZPASSING'{/i} (НЕ ВЛЕЗАТЬ — с ошибкой)."
    "Это всё объясняет."
    "Мая, кажется, совершенно не интересуется, ни разу не обернувшись."
    "Возможно, у неё куча мыслей в голове ..."
    "Я стараюсь выбросить ферму из головы, пока мы продолжаем путь."
    
    scene black
    with fade
    
    "Направляясь прямо на юг, мы вскоре оказываемся в знакомой местности."
    
    stop soundfx2 fadeout 3.0
    scene fieldback
    with dissolve4
    
    "Это место недавней битвы. Поле, через которое я проходил по пути к сараю."
    "Должно быть, во время бури я развернулся и забрёл обратно на север."
    "Над этой местностью висит туман, а тёмные облака вверху начинают уходить за горизонт."
    "Возможно, нам повезёт, и мы увидим солнце ..."
    "Место усеяно мёртвыми солдатами, хотя при дневном свете их трудно узнать."
    "Некоторые тела начали уходить под землю, исчезая в почве и грязи."
    "Дожди шли много дней, так что земля превратилась в чистую жидкую грязь."
    
    show object1
    with dissolve
    $ achievement.grant("NEW_ACHIEVEMENT_1_6")
    
    "Красные и синие мундиры ярко выделяются на фоне умирающей травы."
    "Но бледные лица медленно гниют до самых мышц и костей."
    "Один молодой парень лежит в высокой траве, его призрачное лицо, кажется, пребывает в покое."
    "Мальчишке не больше шестнадцати. Мундир едва сидит на его хрупкой фигуре."
    
    hide object1
    with dissolve
    play soundfx2 "se/mud.ogg" fadein 3.0
    
    "Пока мы пробираемся через поле трупов, я осторожно наблюдаю за Маей."
    
    show darkmai sad
    with dissolve
    
    "Она, должно быть, видела много сражений на этих равнинах."
    "Индейцы против британцев. Британцы против американцев. Индейцы против индейцев."
    "Любопытно взглянув на мужчин, которых мы проходим, она бормочет ..."
    maishawnee ". . . {rb}{i}Пахкотай{/i}{/rb}{rt}(Осень){/rt} . . ."
    me ". . . А? . . ."
    maishawnee ". . . {rb}{i}Пахкотай{/i}{/rb}{rt}(Осень){/rt} . . . сезон умирания . . ."
    me ". . . Аа, ты имеешь в виду осень . . ."
    
    show darkmai normal
    with dissolve
    
    maishawnee ". . . {rb}{i}Пахкотай{/i}.{/rb}{rt}(Осень){/rt} . . ."
    me ". . . {i}Пах{/i} ... {i}котай{/i} . . ."
    
    show darkmai sad
    with dissolve
    
    "С лёгким кивком Мая продолжает идти по тропе."
    "Кажется, ей больше нечего сказать, поэтому мы идём дальше молча."
    
    hide darkmai
    with dissolve
    
    me ". . . {i}Пахкотай ...{/i} да ... . . ."
    "Сезон умирания."
    "Листья опадают, растения увядают, животные исчезают в своих норах ..."
    "И всё это время люди убивают друг друга за право засеять землю в следующем году."
    
    stop soundfx2 fadeout 3.0
    
    "Пока мы идём, я иногда останавливаюсь, чтобы проверить трупы на наличие припасов."
    "Монеты, порох, печенье, пули для мушкета ..."
    "Всё, до чего смогу добраться."
    "Но насколько я могу видеть, с этих тел уже сняли всё ценное."
    "Не теряя надежды, я нахожу труп, который не был ограблен."
    "Засунув руку в карманы его шинели, я нахожу горсть сырых крекеров."
    "Удача на моей стороне впервые за долгое время ..."
    
    show darkmai sad
    with dissolve
    
    "Пока я обыскиваю тело, Мая ждёт и наблюдает."
    mai ". . . Стоит ли тебе так брать у них? . . ."
    me ". . . Мёртвым людям ни к чему порох или монеты ... . . ."
    mai ". . . Я имела в виду печенье. В нём долгоносики . . ."
    me ". . . А? . . ."
    "Посмотрев на горсть крекеров в моей руке, я замечаю множество маленьких жучков, ползающих вокруг."
    maishawnee ". . . {rb}{i}Пак-э-тон{/i} ...{/rb}{rt}(Выброси это){/rt} . . ."
    
    show darkmai normal
    with dissolve
    
    "Чтобы доказать свою правоту, я снимаю одного и поднимаю его, чтобы Мая увидела."
    
    play sound2 "se/apple.ogg"
    show darkmai worry
    with dissolve
    
    "Затем одним быстрым движением руки я отправляю его в рот с хрустом."
    me ". . . Ничего страшного в небольшом количестве белка ... . . ."
    mai ". . . Это отвратительно ... . . ."
    me ". . . В кроликах, которых ты ешь, наверное, больше паразитов . . ."
    
    play soundfx2 "se/mud.ogg" fadein 3.0
    show darkmai sad
    with dissolve
    
    "Пока мы продолжаем идти, я замечаю, что Мая начинает волочить ноги."
    me ". . . Тебе нужен перерыв? . . ."
    mai ". . . Нет, я в порядке ... . . ."
    me ". . . Ладно . . ."
    
    show darkmai normal
    with dissolve
    
    mai ". . . Я не помню, чтобы проходила мимо тех холмов вдалеке . . ."
    mai ". . . Мы идём в правильном направлении? . . ."
    "Посмотрев на серые облака вверху, я едва могу различить за ними круглый ореол света."
    me ". . . Судя по положению солнца, мы должны идти на юг ... . . ."
    me ". . . Если мы будем продолжать двигаться к тем холмам, пока облака не рассеются, тогда мы сможем точно определиться с направлением . . ."
    "Мая кивает, и мы идём дальше в тишине."
    
    show darkmai sad
    with dissolve
    
    mai ". . . Здесь действительно грязно... . . ."
    me ". . . Да уж . . ."
    mai ". . . Я не ожидала, что дождь будет идти так долго . . ."
    "Это была особенно сильная буря."
    me ". . . Смотри, не поскользнись ... . . ."
    
    stop soundfx2
    play sound2 "se/collapse.ogg"
    play sound3 "se/splash.ogg"
    play sound4 "se/plop.ogg"
    show darkmai worry at pickup
    pause 0.1
    hide darkmai
    with vpunch
    queue sound2 "se/wash.ogg"
    
    mai ". . . Ах?! . . ."
    "Как только я это говорю, ноги Маи подкашиваются, и она с грохотом падает в лужу."
    me ". . . Мая! . . ."
    
    play soundfx2 "se/mud.ogg"
    
    "Я бросаюсь к ней."
    "Мая сидит в грязи, держа свою сумку над головой, чтобы сохранить её сухой."
    mai ". . . Я спасла её ... . . ."
    me ". . . Идиотка, ты должна сначала беспокоиться о себе . . ."
    "Вскоре я помогаю юной девчонке подняться на ноги."
    
    stop soundfx2
    show darkmai worry
    with dissolve
    
    mai ". . . {i}Угххх...{/i} . . ."
    me ". . . Ты в порядке? . . ."
    
    show darkmai sad
    with dissolve
    
    mai ". . . Я в порядке... . . ."
    me ". . . Твоё платье перепачкано в грязи . . ."
    mai ". . . Зато я спасла {i}мишаами{/i} . . ."
    "Несмотря на это, она продолжает хмуриться."
    
    show darkmai normal
    with dissolve
    
    me ". . . Уверен, ты высохнешь, когда облака рассеются . . ."
   
    show darkmai happy2
    with dissolve
    
    mai ". . . Обри ... . . ."
    me ". . . Хотя, с другой стороны, это было довольно глупо . . ."
    
    show darkmai angry
    with dissolve
    
    mai ". . . Эй! . . ."
    me ". . . Ты что? Глупая? . . ."
    
    play sound2 "se/collapse.ogg"
    play sound3 "se/splash.ogg"
    play sound4 "se/plop.ogg"
    scene fieldback
    with hpunch
    queue sound2 "se/wash.ogg"
    
    "Мая толкает меня, и я падаю спиной в грязь."
    me ". . . Аргх! . . ."
    
    show darkmai angry
    with dissolve
    
    mai ". . . Ха! . . ."
    me ". . . Эй! Какого чёрта ты творишь?! . . ."
    
    show darkmai happy
    with dissolve
    
    mai ". . . Вот! И кто теперь выглядит глупо? . . ."
    me ". . . Ах ты маленькая паршивка! . . ."
    
    play sound3 "se/swipe.ogg"
    show darkmai worry
    with hpunch
    
    "Я делаю выпад в её сторону, пытаясь повалить девчонку шауни на землю."
    "Но она ловко уворачивается и делает несколько шагов назад."
    me ". . . Чёрт! . . ."
    
    show darkmai happy
    with dissolve
    
    mai ". . . Так тебе и надо! . . ."
    me ". . . А ну вернись! . . ."
    mai ". . . В любом случае, давай продолжим путь . . ."
    
    play soundfx2 "se/mud.ogg"
    hide darkmai
    with dissolve
    
    "Девчонка весело бежит вперёд, перепрыгивая через лужи."
    me ". . . Эй! Вернись! . . ."
    
    stop soundfx2 fadeout 3.0
    
    "Я зову её, но она убегает."
    me ". . . Эй! Мая! . . ."
    "Взглянув на меня, девчонка усмехается и показывает язык."
    
    play sound2 "se/collapse.ogg"
    play sound3 "se/splash.ogg"
    play sound4 "se/plop.ogg"
    queue sound2 "se/wash.ogg"
    scene fieldback
    with hpunch
    
    "Затем я наблюдаю, как она снова поскальзывается и падает в грязь."
    me ". . . {i}Хааа ...{/i} . . ."
    "Может, она и правда глупый ребёнок ..."
    me ". . . Я думаю, это делает нас квитыми, в любом случае . . ."
    "Оба перепачканные в грязи, мы оба похожи на мокрых крыс."
    
    stop music fadeout 5.0
    
    "Кое-как поднявшись на ноги, я пробираюсь сквозь увядающую траву к своей упавшей союзнице."
    
    stop soundfx fadeout 3.0
    $ mouse_visible = False
    scene black
    with dissolve4
    pause 2.0
    scene map
    with dissolve4
    pause 0.5
    $ mouse_visible = True
    play music "music/native.ogg"
    
    "Наше путешествие начинается без происшествий, пока мы бредём по грязным холмам территории Мичиган."
    "Мы продолжаем продвигаться на юг и стараемся избегать главных дорог."
    "Вся эта область была под контролем британцев до недавнего времени."
    "Теперь это снова дикая местность, полная американских рейдеров и враждебных индейцев."
    "Проходя на юг через реки, я вспоминаю сражения."
    "К востоку отсюда мы сражались в месте под названием {i}Френчтаун{/i} на реке {i}Рейзин{/i}."
    "В то время воды замёрзли, и американцы переправились, чтобы атаковать наших канадских союзников."
    "Проктер вывел наш полк из {i}Форт Молдена{/i} на юг, к {i}Френчтауну{/i}, для их защиты."
    "Мы застали врага врасплох на рассвете, когда индейцы уничтожали их разрозненные силы."
    "Наша артиллерия обстреливала их ряды, пока эссекские мушкетёры атаковали врага с фланга."
    "Их регулярные войска сломались и побежали в течение нескольких минут, но несколько стрелковых полков продержались в главном городе."
    "Им удалось отразить наши атаки, убив многих наших соотечественников своим метким огнём."
    "В конце концов они были вынуждены сдаться и попали в плен."
    "Проктер заставил нас отступить на север, к {i}Браунстауну{/i}, оставив войска янки."
    "Ходят слухи о том, что случилось с теми, кто сдался."
    "Истории о резне, устроенной индейцами, и об изуродованных трупах, разбросанных по всей сельской местности ..."
    "Снятие скальпов, грабежи, пытки, сожжение раненых ..."
    "{i}'Помните реку Рейзин'{/i} — кричали они в память об этом."
    "Я смотрю, как моя союзница шауни бредёт впереди, невинно глядя на горизонт."
    "Способна ли она на такую жестокость? Интересно ..."
    "Тёмные облака наверху наконец рассеиваются после нескольких часов ходьбы."
    "Тёплые ветра дуют над холмами и равнинами, вдыхая новую жизнь во всё, к чему прикасаются."
    "Пропитанная земля начинает высыхать, а лужи испаряются под солнечным светом."
    "Свежее ощущение охватывает весь край."
    
    scene forest
    show leaves
    with dissolve
    play soundfx "se/birds.ogg" fadein 5.0
    play sound3 "se/brush.ogg"
    
    "Когда мы подходим к лесной местности, птицы начинают подавать голос."
    me ". . . Похоже, погода наконец-то меняется . . ."
    
    play sound2 "se/brush.ogg"
    show mai happy behind leaves
    with dissolve
    
    maishawnee ". . . {rb}{i}Вашеки шеке!{/i}{/rb}{rt}(Хороший денёк!){/rt} . . ."
    "Индейская девчонка шауни подходит ко мне."
    "Солнечные лучи прорываются сквозь полог леса, оставляя тени танцующих листьев на лице Маи."
    "Свежая роса на высокой траве в подлеске сверкает при дневном свете."
    "Из кустов доносится лёгкий шорох, когда маленькие животные выходят из своих нор."
    
    show mai happy2 behind leaves
    with dissolve
    
    me ". . . Возможно, нам стоит сделать небольшой перерыв и дать ногам отдохнуть . . ."
    "В конце концов, мы идём с самого рассвета."
    
    show mai normal behind leaves
    with dissolve
    
    mai ". . . Ты уверен? . . ."
    me ". . . К тому же, у тебя короткие ножки . . ."
    me ". . . Я не уверен, как долго ты ещё сможешь идти . . ."
    
    show mai angry behind leaves
    with dissolve
    
    mai ". . . Эй! У меня не короткие ноги! . . ."
    me ". . . Я знаю ... ты просто мала для своего возраста ... . . ."
    mai ". . . Почему ты такой злой со мной? . . ."
    me ". . . Я просто честен ... . . ."
    mai ". . . Я могу продолжать! . . ."
    me ". . . Ага, конечно. Ты не продержишься и часа, идя по этой чаще . . ."
    "Что ж, это правда. У неё действительно несколько коротковатые ноги."
    mai ". . . Отвали! . . ."
    
    play sound3 "se/brush.ogg"
    play sound2 "se/walk.ogg"
    hide mai
    with dissolve
    
    "Мая решительно уходит в кусты."
    me ". . . Ты куда? . . ."
    mai ". . . Я пойду вперёд! . . ."
    me ". . . Вперёд? . . ."
    mai ". . . Я ещё могу идти, так что я пойду! . . ."
    me ". . . А? О чём ты говоришь? . . ."
    mai ". . . Потом встретимся! . . ."
    me ". . . Подожди минутку! Вернись! . . ."
    "Девчонка исчезает в лесу."
    me ". . . Упрямая паршивка ... . . ."
    "Как мне снова найти её в этой чаще?"
    "Неужели она настолько глупа, чтобы убежать одна?"
    me ". . . Если только ... . . ."
    "Она, вероятно, играет со мной, надеясь, что я побегу за ней."
    "Это её игра."
    "В таком случае, мне просто нужно набраться терпения и переждать её."
    me ". . . Она вернётся . . ."
    "Я сажусь в грязь и отдыхаю, прислонившись к стволу дерева, затем закидываю ноги."
    "Она, наверное, прячется за дубом и хихикает."
    me ". . . Тебе не перехитрить меня ... . . ."
    "Я чувствую внезапный грызущий голод в животе."
    "Засунув руку в карман, я достаю награбленное печенье и принимаюсь за обед."
    "Теперь, когда они высохли, они вполне ничего."
    "У них своеобразная комковатая текстура из-за переизбытка муки ..."
    "Но в остальном они хороши."
    
    stop music fadeout 5.0
    play soundfx2 "se/march2.ogg" fadein 10.0
    
    "Я начинаю слышать что-то ..."
    "Повторяющийся, барабанящий шум; звук марширующих поблизости!"
    
    play sound3 "se/brush.ogg"
    
    "Выронив горсть крекеров, я быстро пригибаюсь за ближайшим бревном."
    "Откуда это доносится?"
    "Пробираясь сквозь подлесок, я всматриваюсь в лесную полосу в поисках движения."
    
    show object5
    with dissolve
    
    "Близко к моей позиции я обнаруживаю полк американцев в движении."
    "Колонна продолжает свой путь на север, не сворачивая с протоптанной тропы."
    "Они не ищут дезертиров."
    "Не думаю, что они будут прочёсывать лес в поисках кого-то вроде меня."
    "Если бы это был отряд рейдеров, было бы по-другому ..."
    "Тем не менее, мне следует держать голову низко и подождать, пока они пройдут."
    "Я осторожно наблюдаю, как синие мундиры маршируют по наезженной дороге вдалеке."
    me ". . . Мая . . ."
    "Чёрт возьми, где эта девчонка?"
    "Почему она решила убежать именно в это время..."
    "Мы сражались и дурачились друг с другом большую часть утра."
    "Я думал, мы заключили новый союз, когда покидали сарай."
    "Может, это я глупый, что ввязался в спор с ребёнком ..."
    
    stop soundfx2 fadeout 10.0
    hide object5
    with dissolve
    
    "Наконец колонна начинает исчезать на севере."
    me ". . . {i}Хааа ...{/i} . . ."
    "Я вздыхаю с облегчением."
    "Кое-как поднявшись на ноги, я отряхиваю грязь с коленей."
    "Возможно, нам стоит двинуться дальше на юг, на индейские земли, прежде чем пытаться отдохнуть."
    me ". . . Мая? . . ."
    "Я тихо зову в кусты."
    
    play sound3 "se/cock.ogg"
    
    "Подобрав свой мушкет, я углубляюсь в лес."
    
    play soundfx2 "se/walk.ogg" fadein 3.0
    play soundfx3 "se/brush.ogg" fadein 3.0
    scene canopy
    with fade
    
    "Идя по лесу, я наслаждаюсь ломким солнечным светом на своём лице."
    "Птицы щебечут в своих гнёздах, а ветви танцуют на лёгком ветерке, что дует мимо."
    "Теперь, когда гроза закончилась, я начинаю чувствовать себя гораздо свежее."
    "Отражения от листьев над головой создают тёплое зелёное свечение по всему лесу."
    "Это наполняет меня чувством оптимизма."
    "Это своего рода вознаграждение за то, что я выбрался из полка Проктера целым и невредимым."
    "Прокладывая путь через подлесок, я пытаюсь прислушаться."
    
    stop soundfx2 fadeout 3.0
    stop soundfx3 fadeout 3.0
    scene forest2
    show leaves
    with fade
    
    "Я вскоре нахожу её, висящей на соседнем вязе."
    
    play soundfx4 "se/creak.ogg"
    show mai2 dangle behind leaves
    with dissolve
    play music "music/native.ogg"
    
    "Пара коротких ножек болтается сверху, пока она держится за ветку."
    "Она поправляет хватку, раскачиваясь."
    me ". . .  . . ."
    mai ". . .  . . ."
    "Мы обмениваемся тихими взглядами."
    me ". . . Что ты делаешь? . . ."
    "Ответа нет."
    
    play sound3 "se/brush.ogg"
    show mai2 fall
    pause 0.1
    play sound2 "se/fall.ogg"
    pause 0.2
    hide mai2 fall
    show mai normal at right25 behind leaves
    stop soundfx4 fadeout 1.0
    
    "Мая спрыгивает вниз и с глухим стуком приземляется на землю."
    me ". . . Пожалуйста, не делай так больше . . ."
    "Я подхожу к девчонке и кладу руку ей на голову."
    me ". . . Ты слышала марширующих солдат? . . ."
    "Мая смотрит на меня, моргает дважды и снова отводит взгляд."
    me ". . . Я волновался, что ты позволишь им поймать тебя ... . . ."
    "Она не отвечает."
    "Девчонка осторожно смотрит вперёд, пока мы ждём по лесу."
    me ". . . Что там? Ты слышишь, идут ещё? . . ."
    
    show mai angry
    
    mai ". . . {i}Тсс!{/i} . . ."
    "Она подносит указательный палец к губам, показывая, чтобы я замолчал."
    me ". . . Ты чего ... . . ."
    
    show mai normal
    with dissolve
    play sound2 "se/mud.ogg"
    pause 0.5
    show mai normal at center with dissolve
    stop sound2 fadeout 2.0
    
    "Затем, медленно, шаг за шагом, она выходит на середину поляны."
    
    play sound3 "se/wood.ogg"
    show mai normal at pickup with ease
    
    "Достав нож из своей сумки, она нагинается и начинает пилить что-то, скрытое в листве."
    me ". . . Подожди? Ты снова украла мой нож?! . . ."
    
    stop sound3 fadeout 1.0
    
    "Она заканчивает свою работу."
    me ". . . Что это? . . ."
    
    show mai happy at center with ease
    
    "Развернувшись с улыбкой, девчонка предъявляет мёртвого кролика, пойманного в самодельную ловушку."
    "С тугой верёвкой на шее, существо, вероятно, застряло, вылезая из своей норы."
    me ". . . Эта ловушка твоя? . . ."
    
    show mai happy2
    with dissolve
    
    mai ". . . Я поставила её несколько минут назад . . ."
    "Кажется, она ужасно гордится своим достижением."
    me ". . . Если увидишь ещё одного бегающего, дай мне знать . . ."
    "Я киваю в сторону мушкета, висящего на плече, как намёк."
    me ". . . Ах, и ещё ... . . ."
    
    play sound2 "se/swipe.ogg"
    show mai normal
    with hpunch
    
    "Я выхватываю нож из её рук."
    me ". . . Отдай! Я же сказал не красть мои вещи! . . ."
    mai ". . . Это не твой нож . . ."
    me ". . . А? . . ."
    "Осмотрев целую рукоять, я понимаю, что она права."
    "Он сделан из более гладкого дерева и имеет какой-то инкрустированный индейский символ."
    me ". . . Где ты это взяла? . . ."
    mai ". . . Это моё. Мой отец дал мне его . . ."
    me ". . . У тебя есть свой нож? Тогда зачем ты украла мой? . . ."
    mai ". . . Я не хотела тупить своё лезвие, вырезая на балке . . ."
    me ". . . А, вот как. Значит, ничего страшного, если {i}мой нож{/i} затупится, да? . . ."
    
    play sound3 "se/brush.ogg"
    
    "Я возвращаю инструмент ей и тянусь в свой сапог за своим."
    me ". . . А? Странно ... . . ."
    mai ". . . Что странно? . . ."
    me ". . . Моего ножа нет ... . . ."
    mai ". . . Ты потерял его? . . ."
    me ". . . Нет, я не терял его . . ."
    mai ". . . Тогда где он? . . ."
    "Пока я обыскиваю другой сапог и все свои карманы, я понимаю, что его нет."
    me ". . . Я потерял его . . ."
    "Я свешиваю голову в знак поражения."
    
    show mai sad
    with dissolve
    
    mai ". . .  . . ."
    "Девчонка протягивает руку и нежно похлопывает меня по спине."
    me ". . . Мне не нужно твоё сочувствие . . ."
    
    show mai normal
    with dissolve
    
    "Она убирает руку и настороженно наблюдает за мной, как всегда."
    me ". . . В любом случае, это был старый нож. Я всегда смогу найти другой . . ."
    "Руки Маи быстро работают, когда она перевязывает верёвку вокруг маленького кролика."
    me ". . . Этого кролика должно хватить на ужин в любом случае . . ."
    "Затем она прикрепляет добычу к своему поясу."
    me ". . . Если я добуду ещё одного или двух, нам хватит и на завтрак . . ."
    mai ". . . Я собиралась съесть его на обед . . ."
    me ". . . Мы не можем начать готовить здесь . . ."
    me ". . . В пяти минутах ходьбы по дороге находится полк янки . . ."
    mai ". . . Что же я буду есть? . . ."
    "Я засовываю руку в карман и достаю украденный паёк."
    
    show mai worry
    with dissolve
    
    me ". . . На, возьми печенье . . ."
    mai ". . . Я не буду это есть . . ."
    me ". . . Не привередничай . . ."
    "Она всё ещё не берёт их."
    me ". . . Тогда ладно. Мне больше достанется . . ."
    "Я сую корявые крекеры обратно в шинель."
    
    show mai normal
    with dissolve
    
    "Осматривая кусты в этой местности, я пытаюсь опознать ягоды."
    me ". . . Подожди ... . . ."
    mai ". . . Что там? . . ."
    
    play sound2 "se/walk.ogg"
    play sound3 "se/brush.ogg"
    hide mai
    with dissolve
    
    "Я прохожу мимо Маи и направляюсь к яблоне, растущей посреди поляны."
    
    stop sound3 fadeout 1.0
    stop sound2 fadeout 1.0
    
    "Протянув руку вверх к веткам, я срываю фрукт и поворачиваюсь к девчонке."
    
    show mai normal behind leaves
    with dissolve
    
    me ". . . Лови . . ."
    "Я бросаю ей яблоко."
    
    show mai sad
    with dissolve
    
    "Она бросает на меня опасливый взгляд."
    maishawnee ". . . {rb}{i}Мешеменаке?{/i}{/rb}{rt}(Яблоки){/rt} . . ."
    me ". . . Это яблоко. Попробуй . . ."
    
    show mai gulp
    with dissolve
    play sound2 "se/apple.ogg"
    
    "Пожав плечами, Мая откусывает кусок от сочного шара."
    "Раздаётся знакомый хруст."
    
    show mai happy
    with dissolve
    
    mai ". . . Мммм! Оно сладкое! . . ."
    "Счастливая улыбка расползается по её губам."
    me ". . . Правда? . . ."
    "Я складываю руки и усмехаюсь."
    "Это должно заставить её замолчать на некоторое время."
    
    play sound3 "se/hiccup.ogg"
    show mai worry
    with hpunch
    
    "Внезапно девчонка принимает несчастное выражение лица."
    mai ". . . ?!! . . ."
    me ". . . Мая? Что случилось? . . ."
    
    play sound2 "se/cough.ogg"
    show mai gulp
    with dissolve
    
    "Она выплёвывает куски яблока на лесную подстилку."
    "Полусъеденный червяк ползает в пережёванной кашице."
    me ". . . Ох ... . . ."
    
    show mai angry
    with dissolve
    
    mai ". . . Ты заставил меня съесть червяка! . . ."
    me ". . . Я не хотел ... . . ."
    
    show mai sad
    with dissolve
    
    "Поморщившись, девчонка вытирает рот тыльной стороной ладони."
    me ". . . В любом случае, нам нужно продолжать движение . . ."
    
    show mai normal
    with dissolve
    
    "Я кладу несколько яблок в карман на дорогу. Не могут же все они быть с жуками."
    me ". . . Сегодня вечером, когда разобьём лагерь, мы сможем хорошо поесть . . ."
    "Мая бросает на меня тихий взгляд."
    "Наклонившись, я беру её маленькую руку в свою."
    me ". . . Как думаешь, сможешь продержаться ещё немного? . . ."
    
    show mai happy2
    with dissolve
    
    mai ". . . Думаю, я справлюсь . . ."
    me ". . . Хорошо . . ."
    
    play sound3 "se/brush.ogg"
    
    "Вместе мы оба движемся дальше, во вражеские земли ..."
    
    stop music fadeout 5.0
    stop soundfx fadeout 5.0
    $ mouse_visible = False
    scene black
    with dissolve4
    pause 2.0
    scene fieldback2
    with dissolve4
    $ mouse_visible = True
    play music "music/reveal.ogg"
    
    "На поле боя к северу группа солдат в синих мундирах осматривает близлежащие трупы."
    
    show jackson dark determined
    with dissolve
    
    captain ". . . Проверьте каждого тщательно . . ."
    "Благородного вида капитан наблюдает за операцией."
    captain ". . . Ищите тех, кто выглядит свежее остальных . . ."
    "Группа уже несколько часов бродит по полю, пытаясь найти хоть какие-то зацепки."
    "Как опытные следопыты, работы у них непочатый край."
    mctavish ". . . Эй, а кого именно мы здесь ищем? . . ."
    daniels ". . . К нам поступило сообщение от разведчика с этой дороги . . ."
    daniels ". . . Говорит, что только вчера видел красный мундир, хромавшего в сторону заброшенной фермы Эдвардса . . ."
    mctavish ". . . Что ж, если он был здесь, он должен был умереть как минимум неделю назад . . ."
    mctavish ". . . Эти трупы разваливаются. Среди них нет ни одного свежего лица . . ."
    daniels ". . . Капитан? . . ."
    captain ". . . Обыщите их снова. Я хочу убедиться . . ."
    
    play sound2 "se/mud.ogg"
    hide jackson
    with dissolve
    stop sound2 fadeout 5.0
    
    "Капитан отходит, осматривая остальные силы."
    mctavish ". . . К чему всё это? Мы только прикончили этих парней на днях ... . . ."
    
    play sound4 "se/brush.ogg"
    play sound3 "se/wash.ogg"
    
    "Солдат поднимает труп из грязи и соскальзывает назад в высокую траву."
    daniels ". . . Сам знаешь, как это бывает . . ."
    mctavish ". . . Это всего лишь один красный мундир . . ."
    daniels ". . . Что ж, таков капитан ... . . ."
    "Решительный, до конца, поймать и убить британских солдат."
    daniels ". . . Сейчас он, наверное, уже слишком далеко на юге . . ."
    daniels ". . . У нас нет шансов его найти ... . . ."
    captain ". . . Вы двое! Меньше жалоб. Проверьте те тела . . ."
    mctavish ". . . Так точно, сэр! . . ."
    "Мужчины принимаются за работу, осматривая трупы."
    
    scene sky4
    with dissolve4
    
    "Облака вдалеке начинают рассеиваться, и солнце выглядывает наружу."
    "Дальше вдоль линии капитан останавливается и смотрит в высокую траву."
    
    play sound4 "se/brush.ogg"
    
    captain ". . . Что это ... . . ."
    "В листве есть небольшой разрыв и две пары глубоких отпечатков в грязи."
    "Солдатские сапоги и пара намного меньших ботинок ..."
    "Ребёнок? Или, может, женщина?"
    "Он некоторое время следует за уликами и находит след, ведущий в сторону далёких холмов."
    captain ". . . Попались . . ."
    mctavish ". . . Капитан! Мы кое-что нашли! . . ."
    "Крик откуда-то из близи."
    
    play sound2 "se/mud.ogg"
    scene fieldback2
    with fade
    show jackson dark determined
    with dissolve
    stop sound2 fadeout 5.0
    
    captain ". . . Что там? Что вы нашли? . . ."
    "Капитан направляется к солдатам."
    mctavish ". . . Нож, сэр. Он лежал в луже вон там . . ."
    captain ". . . Нож? . . ."
    mctavish ". . . Он был довольно далеко от любого из тел . . ."
    mctavish ". . . Мы думаем, его мог обронить красный мундир . . ."
    
    show jackson dark angry
    with dissolve
    
    captain ". . . И чем это вы занимались, что оказались в стороне от тел? . . ."
    mctavish ". . .  . . ."
    captain ". . . Ну? . . ."
    mctavish ". . . Отлучался по нужде, сэр . . ."
    
    play sound3 "se/swipe.ogg"
    
    "Капитан бросает на МакТавиша презрительный взгляд, прежде чем выхватить нож."
    
    show jackson dark shock
    with dissolve
    
    captain ". . . Подождите-ка ... . . ."
    "Их начальник на мгновение теряет самообладание."
    mctavish ". . . Сэр? . . ."
    "Мужчины молча смотрят на лезвие."
    
    show jackson dark bored
    with dissolve
    
    captain ". . . Ммм ... ладно . . ."
    "Положив нож в карман, капитан поворачивается и смотрит вдаль."
    
    show jackson dark determined
    with dissolve
    
    captain ". . . Хорошая находка. У нас есть всё, что нужно . . ."
    daniels ". . . Всё? Ты имеешь в виду, мы закончили? . . ."
    
    show jackson dark evil
    with dissolve
    
    captain ". . . Там внизу есть тропа, через холмы . . ."
    captain ". . . Я думаю, наш друг в красном мундире мог пройти туда . . ."
    "Капитан усмехается, говоря это."
    captain ". . . Собирайте людей. Мы движемся на юг, через холмы . . ."
    mctavish ". . . Мы уже выступаем, сэр? . . ."
    
    show jackson dark angry
    with dissolve
    
    captain ". . . Я должен повторить? . . ."
    mctavish ". . . Никак нет, сэр . . ."
    
    play sound2 "se/mud.ogg"
    hide jackson
    with dissolve
    stop sound2 fadeout 5.0
    
    "Их лидер медленно уходит прочь, ничего больше не говоря."
    mctavish ". . . Давай, скажем остальным . . ."
    daniels ". . . С ним ... всё в порядке? Я имею в виду капитана . . ."
    mctavish ". . . О чём ты говоришь? . . ."
    daniels ". . . Ну, только что у него был такой ... взгляд . . ."
    mctavish ". . . Что ты хочешь сказать? . . ."
    "Между ними проходит несколько мгновений, пока Дэниэлс смотрит вдаль."
    daniels ". . . Ничего . . ."
    mctavish ". . . Ладно. Давай. Выдвигаемся . . ."
    
    play sound2 "se/mud.ogg"
    
    "Смирившись с приказами, солдаты собираются, готовые двинуться на юг."
    
    stop sound2 fadeout 5.0
    stop music fadeout 5.0
    $ mouse_visible = False
    scene black
    with dissolve4
    pause 2.0
    scene plains
    with dissolve4
    $ mouse_visible = True
    play soundfx "se/wind.ogg"
    play sound2 "se/brush.ogg"
    play music "music/dandelions.ogg"
    
    "Мы бредём по пустым равнинам территории Мичиган."
    "Длинные поля коричневой и желтеющей травы колышутся на ветру."
    "Осенний ветерок источает сильный холод, и я застёгиваю свою шинель, пытаясь согреться."
    
    show mai normal
    with dissolve
    
    "Мая, кажется, не обращает внимания на холод, всё ещё одетая в свою летнюю одежду."
    me ". . . Тебе не холодно в таком виде? . . ."
    mai ". . . А что? Это всего лишь лёгкий ветерок . . ."
    
    show mai happy2
    with dissolve
    
    mai ". . . Когда тебе холодно, всё, что нужно сделать, это продолжать идти, и это согреет тебя . . ."
    me ". . . Мне не нравится твой энтузиазм . . ."
    
    show mai sad
    
    mai ". . . Ты вообще когда-нибудь получаешь удовольствие? . . ."
    me ". . . Не тогда, когда за мной следят силы янки, нет . . ."
    
    show mai normal
    with dissolve
    
    mai ". . . Тебе стоит больше жить настоящим моментом . . ."
    me ". . . Я думал, так и делаю . . ."
    mai ". . . Ты слишком переживаешь о том, что случится или что уже было . . ."
    
    show mai happy
    with dissolve
    
    mai ". . . Нужно принимать жизнь такой, какая она есть, и дорожить ею . . ."
    me ". . . Мудрёные слова для двенадцатилетней . . ."
    "Полагаю, с детской перспективы всё кажется намного проще ..."
    
    show mai happy2
    with dissolve
    
    mai ". . . Это не мои слова . . ."
    mai ". . . Мой отец всегда говорил мне, что мы, шауни, — часть этих земель . . ."
    mai ". . . Небо, ветер, земля ... мы все связаны с ними . . ."
    mai ". . . Всё, что мы делаем, связано с этим фактом . . ."
    "Мая мягко проводит пальцами по охристо-жёлтым травинкам."
    mai ". . . Поэтому мы должны брать у земли только то, что нам необходимо . . ."
    mai ". . . Мы должны жить только так, как должны. И, делая это, чувствовать себя по-настоящему живыми . . ."
    me ". . . Полагаю, твой отец не был солдатом ... . . ."
    "Из него бы выбили весь этот позитив."
    
    show mai normal
    with dissolve
    
    maishawnee ". . . Он вёл войну и много раз сражался под началом {rb}{i}Вейапирсенва{/i}{/rb}{rt}(Синяя Куртка){/rt} . . ."
    me ". . . А? . . ."
    
    show mai happy2
    with dissolve
    
    mai ". . . Он часто говорил мне ... . . ."
    mai ". . . {i}'Когда наступают трудные времена, мы должны держать голову высоко и жить в каждом вдохе'{/i} . . ."
    me ". . . Какая глупая мысль... . . ."
    
    show mai happy
    with dissolve
    
    mai ". . . Он сам скажет тебе это, когда вы встретитесь . . ."
    me ". . . С чего ты взяла, что я хочу говорить с твоим отцом о таких вещах? . . ."
    
    show mai happy2
    with dissolve
    
    mai ". . . Похоже, вы поладите с ним. Вы оба похожи . . ."
    me ". . . Отлично, меня сравнивают с индейцем... . . ."
    
    show mai sad
    with dissolve
    
    mai ". . . Ты не хочешь с ним встретиться? . . ."
    "Она строит печальное выражение лица."
    "Возможно, я сказал лишнее ..."
    
    stop music fadeout 5.0
    show mai normal
    with dissolve
    
    "Протянув руку, я взъерошиваю её волосы, нежно погладив девчонку по голове."
    me ". . . Я же сказал, что буду с тобой, пока мы не доберёмся до твоей деревни ... . . ."
    me ". . . Так что не похоже, что я могу избежать встречи с твоей семьёй . . ."
    "Какая неловкая фраза ..."
    
    show mai happy2
    with dissolve
    
    mai ". . . Обри ... . . ."
    "Затем Мая начинает улыбаться."
    "На что я только не иду, чтобы этот ребёнок был счастлив."
    
    play music "music/friendship.ogg"
    play sound2 "se/brush.ogg"
    show mai normal
    show speedlines with hpunch
    hide speedlines with dissolve
    
    "Внезапно маленькое существо проносится мимо по тропинке впереди."
    
    show mai happy
    
    maishawnee ". . . {rb}{i}Петакине'ти!{/i}{/rb}{rt}(Кролик){/rt} . . ."
    
    play sound3 "se/cock.ogg"
    play sound4 "se/gundrop.ogg"
    play sound2 "se/smash.ogg"
    show mai happy
    with vpunch
    with hpunch
    
    "Я пытаюсь взвести мушкет, но ружжо скользит в моих руках и с грохотом падает на землю."
    me ". . . Чёрт! . . ."
    
    play sound2 "se/brush.ogg"
    
    "Кролик быстро ныряет в высокую траву, слишком быстро, чтобы я мог прицелиться."
    "Наклоняясь, я подбираю свою Браун Бесс, но уже слишком поздно."
    me ". . . Я не могу сделать хороший выстрел в таком положении . . ."
    
    show mai happy2
    with dissolve
    
    mai ". . . Вон туда! Оно побежало туда! . . ."
    "Мая довольно ухмыляется и начинает движение по тропе."
    
    hide mai
    with dissolve
    
    play soundfx2 "se/run.ogg" fadein 3.0
    play soundfx3 "se/brush.ogg"
    $ mouse_visible = False
    window hide
    scene cg4 large
    with dissolve4
    pause 6.0
    scene cg4
    with dissolve4
    pause 1.0
    window show
    $ mouse_visible = True
    $ achievement.grant("NEW_ACHIEVEMENT_1_3")
    
    mai ". . . Давай! Беги! . . ."
    "Мая начинает мчаться вперёд по полю, преследуя кролика."
    me ". . . Эй, подожди! . . ."
    mai ". . . Ты сказал, что тебе холодно! Так начинай бежать! . . ."
    "Мая хватает меня за руку и тянет за собой."
    "Её энергия застаёт меня врасплох, пока меня тащат через золотые поля."
    "Довольно скоро мы набираем темп, когда я начинаю двигать ногами."
    "Дёргаясь то туда, то сюда, мы сходим с проторённой тропы и углубляемся в высокую траву."
    "Маленький кролик пищит, отчаянно карабкаясь прочь."
    "Но девчонка не отстаёт, не выпуская бедняжку из своего зоркого взгляда."
    "Мчась через пни и кочки на тропе, я почти не поскользнулся и не упал."
    "Мая смеётся, пока мы бежим, выкрикивая что-то вслед кролику."
    maishawnee ". . . {rb}{i}Петакине'ти!{/i}{/rb}{rt}(Кролик){/rt} {rb}{i}Петакине'ти!{/i}{/rb}{rt}(Кролик){/rt} . . ."
    "Это то, что она имела в виду под {i}'жизнью в моменте'{/i}?"
    "Чувствуя ветер на своём лице ... высокую траву, хлещущую по нашим пяткам ..."
    "Мы оба продолжаем преследование, пока маленькое существо пытается спрятаться на рыжеватых полях."
    "Его высокие пушистые уши торчат среди желтеющих лугов, пока он скачет туда-сюда."
    
    stop soundfx2 fadeout 3.0
    play sound2 "se/gundrop.ogg"
    scene plains
    with dissolve
    
    "Я отпускаю руку Маи и позволяю своему мушкету соскользнуть с плеча."
    me ". . . Продолжай преследовать и веди его обратно сюда! . . ."
    me ". . . Я приготовлюсь и пристрелю эту тварь! . . ."
    "Я кричу вслед девчонке, которая продолжает бегать за нашим ужином."
    "Если она сможет запутать животное, оно может вернуться ко мне, и это будет лёгкий выстрел."
    "Я готовлю свою Браун Бесс к действию."
    
    play sound2 "se/cock.ogg"
    
    "Достав патрон с пояса, я откусываю конец и ставлю курок на предохранительный взвод."
    "Затем, насыпав порох на полку, я накрываю его кресалом."
    "Дав прикладу почти коснуться земли, я высыпаю остатки пороха в дуло."
    "Затем я заталкиваю пулю вместе с остатками бумаги от патрона, утрамбовывая их внутри."
    "Используя шомпол, я быстро начинаю забивать пыж к казённой части ствола."
    me ". . . Готово! . . ."
    
    play sound2 "se/cock.ogg"
    show speedlines with circleirisout
    hide speedlines with dissolve
    
    "Вернув шомпол на место, я целюсь."
    "Но кролик, похоже, не собирается возвращаться в эту сторону."
    
    stop music fadeout 5.0
    
    "Медленно Мая начинает исчезать всё дальше по равнинам и скрывается из виду, преследуя эту тварь."
    me ". . . Эй! Мая! . . ."
    "Я кричу вслед девчонке, которая становится всё меньше и меньше."
    me ". . . Мая! Вернись! . . ."
    "Возможно, она слишком увлеклась погоней ..."
    me ". . . {i}Хааа ...{/i} . . ."
    "По крайней мере, она движется в правильном направлении."
    
    play sound3 "se/walk.ogg"
    
    "Я начинаю идти, следуя за ребёнком шауни и моим ужином ..."
    
    stop soundfx fadeout 3.0
    stop soundfx3 fadeout 3.0
    $ mouse_visible = False
    scene black
    with dissolve4
    pause 2.0
    scene forestnight
    with dissolve4
    play music "music/leafshade.ogg"
    play soundfx "se/fire.ogg" fadein 5.0
    play soundfx2 "se/night.ogg" fadein 5.0
    show sparklight2
    $ mouse_visible = True
    
    "Той ночью мы разбиваем лагерь на лесной поляне."
    "В укромном, глухом месте, где нас не найдут."
    "Высоко над нами луна ярко светит, освещая лёгкие облака перед собой."
    "Пока мы обустраивали лагерь, Мая ходила собирать растения, а я собирал дрова."
    "Она разбирается в растениях и ягодах лучше меня."
    "Если бы это было предоставлено мне, у нас, вероятно, было бы пищевое отравление."
    
    show maifire normal behind sparklight2
    with dissolve
    
    "Костер мягко мерцает и отбрасывает зловещие тени на опушку леса."
    "Золотые искры мерцают, взметаясь в воздух."
    "Когда они проплывают мимо, они напоминают танцующих светлячков в середине летних вечеров."
    "Над тлеющим кострищем медленно жарится наш ужин."
    "Мая не только поймала наше главное блюдо, но и обеспечила остальную часть трапезы."
    "Признаю, стыдно быть обойдённым индейской паршивкой."
    me ". . . Вкусно пахнет. Что ты использовала для приправы? . . ."
    
    show maifire happy
    with dissolve
    
    mai ". . . Немного измельчённой лаванды и несколько других растений из ближайших окрестностей . . ."
    "Кролик на вертеле с дикими ягодами и травами."
    me ". . . В любом случае, это лучше, чем сухие крекеры и паёк рома ... . . ."
    "Кстати о роме, у меня ещё осталось немного."
    
    play sound2 "se/drinking.ogg"
    show maifire normal
    with dissolve
    
    "Засунув руку в свой красный мундир, я достаю фляжку и делаю глоток."
    "Богатый и крепкий вкус успокаивает меня после сегодняшнего путешествия."
    "Прополоскав напиток во рту, я закидываю голову назад и глотаю."
    "Со временем я буду наслаждаться тёплым послевкусием, когда засну."
    "Эта мысль заставляет меня улыбнуться."
    me ". . . Ах ... . . ."
    "Вскоре я замечаю, что Мая наблюдает за мной."
    me ". . . Что? Хочешь попробовать? . . ."
    
    show maifire sad
    with dissolve
    
    mai ". . . Что это? . . ."
    me ". . . Ром. Ты когда-нибудь пробовала спиртное? . . ."
    "Она качает головой."
    "Забавно. В её возрасте я пил и курил всё, до чего мог дотянуться."
    me ". . . Тем лучше. Я слышал, ваш народ быстро подсаживается на эту дрянь . . ."
    
    show maifire angry
    with dissolve
    
    mai ". . . Эй! . . ."
    me ". . . Шучу, расслабься ... . . ."
    
    show maifire sad
    with dissolve
    
    "Я протягиваю ей фляжку."
    me ". . . Ну что? Хочешь? . . ."
    
    show maifire worry
    with dissolve
    
    "Мая неуверенно тянется и берёт фляжку."
    "Хорошо, что я не отец."
    "Давать алкоголь юным девушкам — не самая умная вещь."
    "Ну, там всего немного ..."
    "Нервничая, она смотрит на меня своими большими глазами."
    mai ". . . Сколько мне выпить? . . ."
    me ". . . Там немного осталось. В твоём возрасте, глотка должно хватить . . ."
    
    show maifire sad
    with dissolve
    
    "Снова посмотрев на фляжку, беспокойство не покидает её лица."
    mai ". . . Ладно ... . . ."
    "Она подносит горлышко бутылки к носу и нюхает."
    
    show maifire worry
    with dissolve
    
    "Недовольное выражение расплывается по её лицу, и она издаёт скулящий звук, похожий на собачий."
    me ". . . Не заставляй себя . . ."
    mai ". . . Всё в порядке ... я справлюсь ... . . ."
    
    show maifire gulp
    with dissolve
    play soundfx3 "se/drinking.ogg" fadein 1.0
    
    "Наклонив бутылку, Мая начинает пить."
    mai ". . .  . . .  . . ."
    "Она продолжает, осушая остатки рома."
    me ". . . Ну, давай ... вот это молодец . . ."
    "Я впечатлён. Она серьёзно взялась за дело."
    
    stop soundfx3 fadeout 1.0
    
    "Выпив почти до последней капли, Мая наконец опускает фляжку от губ."
    me ". . . Ну? Как оно? . . ."
    
    show maifire happy
    with dissolve
    
    "Яркая улыбка расползается по её лицу."
    mai ". . . Эхе-хе-хе ... . . ."
    me ". . . Тебе нравится? . . ."
    
    show maifire happy2
    with dissolve
    
    mai ". . . Сначала у него странный вкус ... . . ."
    mai ". . . но от него внутри становится тепло . . ."
    me ". . . Ага, вот так он и действует . . ."
    "Я забираю у неё фляжку."
    "Взболтнув её, я понимаю, что там остался ещё глоток или два."
    "Лучше приберегу на случай, когда действительно понадобится."
    "Завинтив крышку фляги, я убираю её к своим вещам ..."
    me ". . . Не говори своим старейшинам, что я дал тебе выпить . . ."
    me ". . . Меньше всего мне нужно, чтобы меня выгнали из вашей деревни за то, что я напоил тебя . . ."
    
    show maifire happy
    with dissolve
    
    mai ". . . Эхе-хе-хе ... . . ."
    
    play sound2 "se/hiccup.ogg"
    show maifire worry
    with hpunch
    
    mai ". . . {i}Ик!{/i} . . ."
    "Мая громко икает."
    me ". . . Ты только что ...? . . ."
    mai ". . . Нет, не икала! . . ."
    "Её лицо становится ярко-малинового оттенка."
    
    play sound2 "se/hiccup.ogg"
    show maifire hiccup
    with hpunch
    play soundfx3 "se/hiccups.ogg"
    
    mai ". . . {i}Ик!{/i} . . ."
    "Она начинает икать непрерывно."
    "Наверное, напиток пошёл не в то горло ..."
    me ". . . Не переживай об этом ... . . ."
    "Сев рядом с Маей, я начинаю мягко поглаживать её по спине."
    me ". . . Выпусти всё это ... . . ."
    mai ". . . {i}Ик ... ик ... ик ...{/i} . . ."
    me ". . . Я сам постоянно так икал, когда был моложе . . ."
    me ". . . Со временем вырабатывается привыкание . . ."
    "Пока я массирую спину девчонки, до меня доходит, насколько мала её фигура."
    "Размах моей руки почти достигает от плеча до плеча."
    
    stop soundfx3 fadeout 1.0
    show maifire sad
    with dissolve
    
    "Вскоре она возвращает дыхание под контроль, и икота прекращается."
    me ". . . Лучше? . . ."
    mai ". . . Да ... Спасибо ... . . ."
    "Я встаю и сажусь напротив неё."
    
    show maifire normal
    with dissolve
    
    me ". . . В любом случае, кролик выглядит почти готовым . . ."
    me ". . . Что скажешь, начнём есть? . . ."
    
    show maifire happy2
    with dissolve
    
    mai ". . . Хорошо . . ."
    "Протянув руку, я тыкаю кролика на вертеле ножом Маи и проверяю цвет."
    "Мясо выглядит почти готовым."
    "Отрезав кусочек, я отправляю кролика в рот."
    
    show maifire normal
    with hpunch
    with vpunch
    
    me ". . . Аххх ... хо ... . . ."
    "Я медленно обжигаю язык, отчаянно перекатывая мясо во рту."
    "Жар прожигает мои дёсны и заставляет меня строить глупые гримасы."
    
    show maifire worry
    with dissolve
    
    me ". . . Во ... ды ... . . ."
    "Я показываю жестом, что нужна вода."
    
    play sound3 "se/junk.ogg"
    
    "Мая шарит вокруг и в конце концов протягивает мне фляжку."
    
    play soundfx3 "se/drinking.ogg" fadein 1.0
    
    "Сорвав крышку, я отчаянно глотаю остатки жидкости."
    
    stop soundfx3 fadeout 1.0
    show maifire worry
    with hpunch
    with vpunch
    
    me ". . . Гах! . . ."
    "Проглатывая мясо, я чувствую жжение в горле, когда понимаю, что пью."
    me ". . . Это остатки моего рома!! . . ."
    "Она дала мне не фляжку с водой. Вместо этого, это был мой ром."
    
    show maifire sad
    with dissolve
    
    mai ". . . Прости! . . ."
    me ". . . Чёрт ... . . ."
    "Я вытираю подбородок и ощупываю язык указательным пальцем."
    "Ещё несколько часов мой рот будет чувствовать себя шершавым."
    
    show maifire normal
    with dissolve
    
    "Сняв наш ужин с вертела, я даю ему остыть несколько минут на ближайшем камне."
    "Над нашим лагерем снова воцаряется тишина."
    
    show maifire happy2
    with dissolve
    
    mai ". . . Я помню, как однажды проходила этим путём, много лет назад . . ."
    "Пока Мая снова не начинает говорить."
    mai ". . . Мы разбивали лагерь недалеко отсюда, у реки . . ."
    mai ". . . Если мы сможем найти ту реку, то сможем идти вдоль неё через лес . . ."
    
    show maifire normal
    with dissolve
    
    me ". . . Итак, сколько ещё нам идти до твоей деревни? . . ."
    mai ". . . Если выйдем рано, должны прибыть завтра к полудню . . ."
    me ". . . Завтра к полудню, значит ... . . ."
    "Всего лишь ещё один день, и я покончу с этой девчонкой."
    "Никаких больше глупых разговоров, никакой индейской чепухи ..."
    "Наконец-то свободен."
    me ". . . Эй, я уже некоторое время хотел спросить ... . . ."
    mai ". . . Ммм? . . ."
    me ". . . Как тебе удалось сбежать от американских войск, когда тебя схватили? . . ."
    me ". . . То есть, что произошло за те месяцы? . . ."
    "Мая бросает на меня ничего не выражающий взгляд."
    mai ". . . Зачем ты спрашиваешь? . . ."
    me ". . . Ну ... . . ."
    
    show maifire happy2
    with dissolve
    
    mai ". . . Неужели тебе интересно? . . ."
    me ". . . Идиотка, я ничего подобного не говорил . . ."
    
    show maifire sad
    with dissolve
    
    mai ". . . Тогда, наверное, я не скажу тебе . . ."
    me ". . . Эй, подожди-ка минутку ... . . ."
    
    show maifire happy2
    with dissolve
    
    mai ". . . Я хочу услышать ... . . ."
    me ". . . Ургх ... . . ."
    "Этот ребёнок играет со мной в игры."
    me ". . . Ладно . . ."
    me ". . . Мне ... мне интересна твоя история, хорошо? . . ."
    
    show maifire happy
    with dissolve
    
    mai ". . . Это было не так уж сложно, правда? . . ."
    "Чёртова паршивка."
    me ". . . Ну? Что случилось? . . ."
    
    show maifire normal
    with dissolve
    
    mai ". . . Когда меня схватили, меня отвезли в место под названием {i}'Фотстефенсон'{/i} и держали там много месяцев . . ."
    "{i}Форт Стивенсон{/i} ... это на востоке, на реке {i}Сандаски{/i}."
    mai ". . . Меня заставляли выполнять мелкие поручения для американцев . . ."
    mai ". . . Они хотели, чтобы я была полезной, поэтому я давала лекарства больным и помогала готовить для них . . ."
    mai ". . . Сначала они планировали отправить меня дальше с остальными и переместить нас на юг . . ."
    mai ". . . Но когда британцы атаковали, американцы решили взять нас с собой . . ."
    "Там летом была битва под командованием Проктера."
    "Мы не участвовали в ней, но участвовали в аналогичных осадах — в {i}Форт Мегсе{/i} и {i}Френчтауне{/i} ранее в том году."
    "Значит, Мая была в {i}Форт Стивенсоне{/i} во время осады ..."
    mai ". . . Меня держали там ещё месяц . . ."
    mai ". . . Мы начали движение на север две недели назад, когда англичане отступали . . ."
    mai ". . . Когда мы добрались до {i}Фотшелби{/i}, мне удалось разорвать оковы и сбежать . . ."
    me ". . . И всё? . . ."
    mai ". . . Больше нечего сказать . . ."
    mai ". . . Меня хорошо кормили, и они не пытались меня продать или что-то в этом роде . . ."
    mai ". . . Думаю, они считали меня слишком маленькой, чтобы быть ценной . . ."
    "Что ж, в любом случае, вряд ли её стали бы продавать на северной территории..."
    
    show maifire happy2
    with dissolve
    
    mai ". . . Один из солдат в {i}Фотстефенсоне{/i} часто играл на маленькой флейте поздно ночью . . ."
    mai ". . . Он просил меня не спать с ним, пока он в карауле . . ."
    mai ". . . Он научил меня петь песни, которые знал, и стихи . . ."
    mai ". . . Иногда он тоже просил меня танцевать . . ."
    me ". . . И ты танцевала? . . ."
    
    show maifire normal
    with dissolve
    
    mai ". . . Ну, в конце концов ... я не очень хорошо танцую . . ."
    me ". . . Могу представить . . ."
    
    show maifire happy2
    with dissolve
    
    mai ". . . Он иногда давал мне шоколад. И маркитант тоже тайком давал мне пайки . . ."
    mai ". . . Они были хорошими людьми . . ."
    me ". . . Это немного ... необычно . . ."
    
    show maifire normal
    with dissolve
    
    mai ". . . Почему? . . ."
    me ". . . Почему? Я просто ... не ожидал, что янки могут быть такими . . ."
    "Я вообще не ожидаю этого ни от кого."
    "Кто будет тратить пайки на маленькую паршивку, даже если она милая?"
    mai ". . . Доброта бывает в неожиданных местах . . ."
    
    show maifire happy2
    with dissolve
    
    mai ". . . Я видела это по твоему лицу, когда мы впервые встретились . . ."
    me ". . . Когда мы встретились? . . ."
    mai ". . . Даже когда ты наставил на меня мушкет, я знала, что ты не выстрелишь . . ."
    
    show maifire happy
    with dissolve
    
    mai ". . . В твоих глазах было слишком много доброты . . ."
    me ". . .  . . ."
    "Что? ..."
    "Какой вздор!"
    me ". . . Что ж, ты полностью неправильно меня поняла . . ."
    me ". . . Я не добрый человек . . ."
    
    show maifire happy2
    with dissolve
    
    mai ". . . Да, добрый . . ."
    "Так вот почему она не шелохнулась, когда мой штык был нацелен ей в грудь ..."
    "Она увидела доброту в моём выражении лица."
    me ". . . Я мог бы выстрелить из мушкета, знаешь ли? Я мог бы это сделать . . ."
    mai ". . . Но ты не выстрелил . . ."
    "Мая мягко улыбается."
    
    show maifire normal
    with dissolve
    
    me ". . . На. Заткнись и попробуй кролика . . ."
    "Я отрываю ещё кусок мяса и передаю его девчонке."
    me ". . . К этому времени он должен был немного остыть . . ."
    
    show maifire happy
    with dissolve
    
    "Мая жуёт блюдо и медленно расплывается в улыбке."
    mai ". . . {i}Ммммн ... ммммн нн ммн!{/i} . . ."
    me ". . . Эй, не говори с набитым ртом! . . ."
    "Она издаёт счастливые звуки, жуя мясо."
    
    show maifire happy2
    with dissolve
    
    "Проглотив кусок, она повторяет свою мысль."
    mai ". . . Вкусно! . . ."
    me ". . . Я и сам мог догадаться . . ."
    "Её старейшинам лучше угостить меня чем-нибудь хорошим, когда я доберусь до их деревни."
    
    scene sky3
    with dissolve4
    
    "Я смотрю на небеса, на эти мерцающие звёзды, кружащиеся вверху."
    "Ночь ясная, не считая нескольких лёгких облаков, и мы можем видеть много разных созвездий."
    "Вот Большая Медведица, Пояс Ориона, две медведицы ... или их было три?"
    "Простираясь широкой дугой через центр неба, раскинулся Млечный Путь."
    "Один ирландский парень в полку называл его {i}'Тропой Справедливой Коровы'{/i}."
    "Тишина и сияющие звёзды наверху успокаивают моё уставшее сердце."
    mai ". . . {i}'Подожди меня ...'{/i} . . ."
    "Затем, довольно неожиданно, Мая начинает напевать небольшую мелодию."
    mai ". . . {i}'Подожди меня-я-я ...'{/i} . . ."
    me ". . . Что ты делаешь? . . ."
    "Я перебиваю её."
    mai ". . . Это {i}песенка{/i} . . ."
    me ". . . {i}Песенка{/i}? . . ."
    mai ". . . Её научил меня тот солдат в {i}Фотстефенсоне{/i} . . ."
    me ". . . Понятно ... . . ."
    "Мая снова начинает свою песню."
    mai ". . . {i}'Подожди меня ...'{/i} . . ."
    mai ". . . {i}'Подожди меня, любовь моя ...'{/i} . . ."
    mai ". . . {i}'В том мирном месте, на которое мы все надеемся.'{/i} . . ."
    "Она продолжает напевать нежный мотив янки."
    "По мере того как она продвигается по тактам, разворачивается история."
    "История о солдате, уходящем на войну, о его детской любви, оставленной на какой-то старой ферме."
    "Он просит её подождать его возвращения с победой."
    "Но война затягивается, и он никогда не возвращается домой."
    "Она думает, что он мёртв, и не может этого вынести."
    "Другие мужчины пытаются ухаживать за ней, и она думает о том, чтобы жить дальше."
    "Но всё же солдат в своём сердце умоляет её подождать."
    "Довольно грустная история."
    mai ". . . {i}'Подожди меня ...'{/i} . . ."
    mai ". . . {i}'Пожалуйста, подожди меня-я ...'{/i} . . ."
    "Забавно ... У меня никогда не было возлюбленной."
    "Я был слишком занят борьбой и мелкими преступлениями."
    "В конце концов, быть солдатом и быть влюблённым — глупо."
    "Слишком много горя, слишком много ожидания ..."
    "И кто бы захотел плакать по такому, как я?"
    mai ". . . {i}'Ммм Ммм Хмм Мммммм ...'{/i} . . ."
    "В конце концов Мая начинает просто напевать, наверное, забыв слова."
    "Может, есть какой-то мальчик, который ей нравится, в её деревне?"
    "Какой-то бравый юный шауни, который лазает с ней по деревьям и гребёт на каноэ."
    "Свой человек, кто-то, кто может быть хорош для неё, насколько может быть хорош индеец."
    "Завтра, возможно, они воссоединятся."
    mai ". . . {i}'Хмммм Ммм Хмм ...'{/i} . . ."
    "Покачав головой, я жую ещё немного кролика и откидываюсь назад."
    
    stop music fadeout 5.0
    
    "Пока наш костёр ярко горит в темноте, мы вместе наблюдаем за космосом ..."
    
    stop soundfx fadeout 5.0
    $ mouse_visible = False
    scene black
    with dissolve4
    window hide
    pause 2.0
    show expression Text(_("Meanwhile, several miles north . . ."), size=20, yalign=0.5, kerning=4, color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve
    pause 3.0
    hide expression Text(_("Meanwhile, several miles north . . ."), size=20, yalign=0.5, kerning=4, color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve
    pause 1.0
    pause 1.0
    window show
    play music "music/theplan.ogg"
    play soundfx2 "se/night.ogg" fadein 5.0
    play soundfx3 "se/march3.ogg" fadein 5.0
    scene plainsnight
    with dissolve4
    $ mouse_visible = True
    
    "На равнинах Северо-Запада синие мундиры продолжают маршировать в темноте."
    "Они движутся вперёд, выслеживая свою добычу, надеясь найти какой-нибудь знак."
    
    show jackson night angry
    with dissolve
    
    captain ". . . Не отставай, отребье! . . ."
    "Капитан кричит на своих людей, пытаясь ускориться."
    mctavish ". . . Эй, капитан ... может, отдохнём ночью? . . ."
    daniels ". . . Мы идём с самого рассвета, сэр . . ."
    captain ". . . Прекратите ныть! Мы на охоте ... . . ."
    
    play sound3 "se/walk.ogg"
    hide jackson
    with dissolve
    stop sound3 fadeout 3.0
    
    "С безумным блеском в глазах их лидер идёт дальше, не сдерживаемый ничем."
    mctavish ". . . Так и быть лагерю . . ."
    daniels ". . . Эй ... как думаешь ... . . ."
    mctavish ". . . Что? . . ."
    daniels ". . . Тебе не кажется, что капитан ... ну, он слишком решительный? . . ."
    mctavish ". . . Решительный? . . ."
    daniels ". . . Я имею в виду, сколько миль мы уже прошли? . . ."
    daniels ". . . Мы уходим слишком далеко от фронта ... . . ."
    "Дэниэлс смотрит вслед своему командиру, который уверенно движется через луга."
    mctavish ". . . Что ж ... он действительно ненавидит красные мундиры ... . . ."
    daniels ". . . Но тебе не кажется ... . . ."
    
    show jackson night angry
    with dissolve
    
    captain ". . . Вы двое! . . ."
    "Капитан замечает, что они болтают, и назначает наказание."
    captain ". . . Скорым маршем! Живо! . . ."
    mctavish ". . . Так точно, сэр! . . ."
    
    hide jackson
    with dissolve
    
    daniels ". . . Он сумасшедший? . . ."
    mctavish ". . . Закрой рот и маршируй . . ."
    "Заботясь о своих шкурах, двое солдат идут дальше, впереди остальных."
    daniels ". . . Ублюдок. Настоящий ублюдок . . ."
    
    stop music fadeout 5.0
    stop soundfx2 fadeout 5.0
    stop soundfx3 fadeout 5.0
    $ mouse_visible = False
    scene black
    with dissolve4
    pause 2.0
    scene caveback
    with dissolve4
    $ mouse_visible = True
    play soundfx "se/fire.ogg" fadein 10.0
    
    "{i}Обри ...{/i}"
    "Голос эхом разносится. Тот же голос, что и раньше."
    "{i}Обри ...{/i}"
    "Медленно я возвращаюсь к тому сну ..."
    
    show cave 1
    with dissolve4
    play music "music/wandering.ogg"
    
    "{i}Прекрасная женщина бежала, а монстр медленно следовал за ней.{/i}"
    "{i}Её ноги топтали луга и леса.{/i}"
    "{i}Когда она достигла опушки леса, она поняла, почему туда было запрещено ходить.{/i}"
    "{i}Длинные полосы мёртвой змеиной кожи лежали в грязи.{/i}"
    "{i}Это место было гнездовьем змеев, а она должна была стать их добычей.{/i}"
    "{i}Плача от страха, женщина услышала шипение позади себя и снова побежала.{/i}"
    "{i}По холмам и равнинам она мчалась, отчаянно пытаясь сбежать.{/i}"
    "{i}Сначала её ноги двигались быстро; но затем, когда она думала о своём хорошем мужчине ...{/i}"
    "{i}... о его доброте, о его умениях ...{/i}"
    "{i}... она замедлилась.{/i}"
    "{i}Её разум спорил с её сердцем.{/i}"
    "{i}Как она могла убежать от такого прекрасного и доброго мужчины?{/i}"
    "{i}В конце концов она поняла, что потеряла зверя где-то позади себя.{/i}"
    "{i}Остановившись, желая перевести дух, девушка села отдохнуть.{/i}"
    "{i}Она устала и решила закрыть глаза и помолиться.{/i}"
    "{i}На холмике она оставалась в тишине, постепенно чувствуя, как энергия покидает её тело.{/i}"
    
    show cave 9
    with dissolve4
    
    "{i}И там ей приснился сон ...{/i}"
    "{i}... тихий сон ...{/i}"
    
    show cave 5
    with dissolve4
    
    "{i}В тот момент появилась гигантская птица. Священное существо ...{/i}"
    "{i}Её крылья простирались по всему небу. Её когти вонзались в склон холма.{/i}"
    "{i}Дух Грома обратился к ней, и его глубокий, раскатистый голос был оглушительным.{/i}"
    "{i}'Беги! Беги!! Беги!!!'{/i}"
    "{i}Девушка вскочила, зажав уши руками, когда великий голос эхом разнёсся по земле.{/i}"
    "{i}'Человек-Змей позади тебя!!! Он поймает тебя!!!'{/i}"
    "{i}Мифическая птица указала ей путь, как безмолвный хранитель.{/i}"
    "{i}Затем прекрасная женщина побежала, и страх её души пульсировал в голове.{/i}"
    "{i}Она услышала ужасный шорох змеечеловека.{/i}"
    "{i}Он приближался ... этот великий, злой змей ...{/i}"
    
    hide cave 5
    with dissolve4
    show cave 1
    with dissolve4
    
    "{i}Она бежала, пока не пересекла горы, и вскоре оказалась у озера недалеко от своего старого дома.{/i}"
    "{i}Того самого, у которого она провела много дней, глядя на своё отражение.{/i}"
    "{i}Каждый шаг приближал её всё ближе и ближе к дому.{/i}"
    "{i}Человек-змей всё ещё полз за ней, нагоняя с каждой милей.{/i}"
    "{i}Вскоре женщина добралась до своей деревни, но обнаружила, что она заброшена.{/i}"
    "{i}У неё не осталось дома.{/i}"
    "{i}Чудовище было близко, и она чувствовала его дыхание на затылке.{/i}"
    "{i}Мчась через деревню, она обогнула её и вернулась к озеру.{/i}"
    "{i}Там, у кромки воды, лежало старое деревянное копьё.{/i}"
    "{i}Услышав, как пасть зверя щёлкает, разжимаясь, женщина схватила оружие в руки.{/i}"
    "{i}Изо всех сил она метнула его в змея.{/i}"
    "{i}В одно мгновение копьё пронзило тело змея, разорвав чешуйчатую кожу.{/i}"
    "{i}Существо зашипело от боли и с огромным грохотом рухнуло на землю.{/i}"
    
    show cave 9
    with dissolve4
    
    "{i}Внезапно ревущее чёрное облако окружило женщину.{/i}"
    "{i}Её зрение затуманилось, и всё вокруг исчезло.{/i}"
    "{i}Она думала, что должна продолжать ...{/i}"
    "{i}Она не должна оглядываться на зверя.{/i}"
    "{i}И всё же она не смогла удержаться и обернулась.{/i}"
    
    show cave 6
    with dissolve4
    
    "{i}Девушка оглянулась на гигантского змея и увидела, что он превратился в мужчину, которого она любила.{/i}"
    "{i}Только теперь он был смертельно ранен.{/i}"
    "{i}Копьё глубоко вонзилось ему в грудь, и он истекал кровью на твёрдую землю.{/i}"
    "{i}Женщина подбежала к нему, полная отчаяния.{/i}"
    "{i}'Что ты наделала? Зачем убивать меня, если знаешь, как я тебя люблю?'{/i}"
    "{i}Спросил мужчина, задыхаясь от боли.{/i}"
    "{i}'Я всего лишь хотел, чтобы ты осталась рядом со мной ...'{/i}"
    "{i}'Зачем? Зачем ты это сделала?'{/i}"
    "{i}У женщины не было ответа.{/i}"
    "{i}Мужчина медленно исчез в земле, не оставив следа.{/i}"
    "{i}Не зная, что ещё делать, прекрасная девушка просто заплакала.{/i}"
    "{i}У неё было разбито сердце.{/i}"
    "{i}Девушка убила единственного мужчину, которого когда-либо любила.{/i}"
    
    hide cave 6
    with dissolve4
    show cave 1
    with dissolve4
    
    "{i}Когда она увидела своё отражение в воде, то поняла, что её красота ушла.{/i}"
    "{i}Женщина, смотревшая на неё в ответ, была измождённой и несчастной.{/i}"
    "{i}Её кожа сморщилась, волосы стали белыми, как пепел.{/i}"
    "{i}Больше не было добрых мужчин с дарами.{/i}"
    "{i}Больше не было таинственных мужчин с пронзительными глазами.{/i}"
    "{i}Шли годы, девушка становилась старой и усталой.{/i}"
    "{i}Теперь она предупреждает других молодых людей, чтобы они искали красоту в сердце.{/i}"
    "{i}Мы не должны обманываться тем, что видим на поверхности.{/i}"
    "{i}Ибо в тот день, когда сердце змея было пронзено, её сердце тоже было пронзено.{/i}"
    
    hide cave 1
    with dissolve4
    
    "{i}Мы должны искать красоту в сердце ...{/i}"
    "Вот оно что?"
    "Причина этих преследующих меня видений ..."
    "Этих снов ... этих пустых мыслей ..."
    "{i}Обри ...{/i}"
    "Чего ты хочешь? Зачем ты мучаешь меня этими снами?"
    "Я действительно проклят?"
    "Должен ли я брести в одиночестве, полный сомнений, мучимый смутными моралями?"
    "{i}Ты должен искать красоту в сердце ...{/i}"
    "Должен ли я ..."
    "{i}Вот где всё начинается ...{/i}"
    "{i}Сердце — это ...{/i}"
    "Голос снова начинает затихать ..."
    "Подожди ... умоляю я вслух ..."
    "Но видение снова растворяется в пустоте."
    "Я чувствую, как тьма сна затягивает меня в новые миры."
    
    stop music fadeout 5.0
    stop soundfx fadeout 5.0
    scene black
    with dissolve4
    
    "{i}Ищи красоту в сердце ...{/i}"
    "{i}Вот где всё начинается ...{/i}"
    
    $ mouse_visible = False
    pause 2.0
    scene map
    with dissolve4
    $ mouse_visible = True
    play music "music/first_encounter.ogg"
    
    "На следующий день мы рано собираемся и продолжаем наше путешествие."
    "Мы бредём по обширному лесу Северо-Западной территории."
    "Трудно понять, где мы сейчас находимся."
    "Пересекли ли мы границу территории Мичиган, попав в Огайо, или даже перешли на индейские земли Индианы ..."
    "Я просто полагаюсь на чувство направления Маи, пока мы идём к её деревне."
    "Каждую милю или около того у неё появляется чутьё, и мы продолжаем идти."
    
    play soundfx "se/birds.ogg" fadein 5.0
    play soundfx2 "se/brush.ogg" fadein 5.0
    scene forest
    show leaves
    with dissolve
    
    "Последние несколько часов мы также следуем вдоль реки, она как ориентир."
    "Но даже так мы теряем её из виду, когда останавливаемся каждые несколько минут и меняем направление."
    "Куда же, чёрт возьми, идёт эта девчонка?"
    
    show mai normal behind leaves
    with dissolve
    
    mai ". . . Эй, Обри ... . . ."
    me ". . . Что? . . ."
    mai ". . . Ты веришь в рай? . . ."
    "Какие глупые вопросы."
    me ". . . С чего это вдруг? . . ."
    mai ". . . Прошлой ночью, когда мы смотрели на звёзды ... . . ."
    mai ". . . Мне стало интересно ... о рае ... . . ."
    me ". . . Тебе, наверное, не стоит беспокоиться об этом в твоём возрасте . . ."
    "Я пытаюсь пробиться сквозь густые заросли."
    mai ". . .  . . ."
    "Мая просто смотрит на меня, ожидая ответа."
    me ". . . {i}Хааа ...{/i} Я не знаю . . ."
    me ". . . Не знаю, верю ли я в рай . . ."
    "Я отодвигаю толстые ветки с лица, лениво отвечая ей."
    mai ". . . Ты не христианин? . . ."
    me ". . . Нет, я христианин . . ."
    "Меня крестили как христианина, во всяком случае ..."
    mai ". . . Но ты не веришь в рай? . . ."
    me ". . . Дело не в том, что я не верю в него ... . . ."
    "Я просто не вижу смысла надеяться на него."
    me ". . . Раньше я верил . . ."
    me ". . . Но в последнее время у меня не было времени думать об этом ... . . ."
    "Существует ли рай? Существует ли первородный грех? Испытывает ли нас Бог?"
    "Наверное, ответы на такие глупые вопросы можно считать своего рода епитимьей."
    mai ". . . Понятно . . ."
    me ". . . А как насчёт тебя? Шауни верят в рай? . . ."
    
    stop soundfx2 fadeout 1.0
    
    "Мы останавливаемся на поляне."
    
    show mai happy2 behind leaves
    with dissolve
    
    "Она начинает улыбаться."
    me ". . . Мая? . . ."
    mai ". . . Смотри! Вон там! . . ."
    me ". . . Что там? . . ."
    
    play soundfx2 "se/brush.ogg"
    show mai happy2 at pickup with ease
    show mai happy at center with ease
    stop soundfx2 fadeout 1.0
    
    "Наклонившись к земле, Мая поднимает яркую бусину."
    mai ". . . {i}Вампум{/i}! . . ."
    "Она держит её на раскрытой ладони и тычет мне в лицо."
    me ". . . Что? . . ."
    
    show mai happy2
    
    mai ". . . Это бусина {i}вампум{/i} . . ."
    me ". . . Бусина? . . ."
    
    show object3
    with dissolve
    
    "Осмотрев её поближе, я вижу, что это, похоже, маленький камень или ракушка."
    me ". . . И ... что в ней особенного? . . ."
    mai ". . . Моя деревня использует {i}вампум{/i}! . . ."
    "Возможно, мы приближаемся ..."
    
    hide object3
    with dissolve
    
    mai ". . . И вон там! Смотри! . . ."
    
    play sound2 "se/walk.ogg"
    hide mai with easeoutleft
    play soundfx2 "se/brush.ogg"
    
    "Мая устремляется вперёд, и я следую за ней."
    
    scene canopy
    with fade
    
    "Пока мы продолжаем путь, мы проходим мимо маленьких коричневых хижин в лесу."
    "Странные лачуги разрисованы красочными значками и изображениями."
    
    stop soundfx2 fadeout 1.0
    scene forest
    show leaves
    with dissolve
    
    me ". . . Мая? . . ."
    
    show mai happy behind leaves
    with dissolve
    
    mai ". . . Эти {i}виккумы{/i} ... я их узнаю ... . . ."
    me ". . . {i}Вик-вумы?{/i} . . ."
    mai ". . . Мы на окраине моей деревни . . ."
    me ". . . Ты хочешь сказать, мы добрались? . . ."
    
    play sound2 "se/walk.ogg"
    hide mai with easeoutleft
    play soundfx2 "se/brush.ogg"
    
    "Мая снова устремляется прочь."
    me ". . . Мая! . . ."
    mai ". . . Кажется, я слышу людей! . . ."
    me ". . . Это не всегда хороший знак ... . . ."
    maishawnee ". . . {rb}{i}Нига! Но'та!{/i}{/rb}{rt}(Мать! Отец!){/rt} . . ."
    me ". . . {i}Хааа ...{/i} . . ."
    
    stop music fadeout 5.0
    scene black
    with fade
    
    "Следуя за девчонкой, я начинаю видеть край лесной опушки."
    "Когда мы проходим мимо всё большего количества коричневых хижин, я замечаю, что они совершенно пусты."
    "Ни жителей, ни вещей."
    "Вскоре мы выбираемся из кустов и выходим на открытое пространство."
    
    stop soundfx fadeout 3.0
    stop soundfx2 fadeout 3.0
    play sound2 "se/brush.ogg"
    scene village
    with dissolve4
    play music "music/lullaby.ogg"
    
    "Должно быть, это оно. Это деревня Маи."
    "Но ... здесь что-то не так ..."
    "Зловещая тишина нависла над этим местом."
    "Мая стоит не шелохнувшись, не двигаясь ни на дюйм."
    "Расположенная на скалистом холме над близлежащим озером, деревня оказалась полностью заброшенной."
    "Вдалеке крутые холмы лишены каких-либо признаков человеческой деятельности."
    "Нет ни рыбаков, ни каноэ, ни лесорубов, ни семей ..."
    
    show mai worry
    with dissolve
    
    "Индейская девчонка поворачивается ко мне с тревожным лицом."
    mai ". . . Я не понимаю . . ."
    "Горшки лежат разбитые в грязи, простая мебель перевёрнута и сломана ..."
    "Пепел из потухшего кострища развеян по грязной земле, покрывая старые следы слоем сажи."
    "Это место пустует уже некоторое время."
    me ". . . Мая ... . . ."
    "Сколько месяцев Мая была в плену?"
    "Как давно её племя жило здесь, у этого озера?"
    
    play sound2 "se/run.ogg"
    hide mai worry
    with dissolve
    
    "Смуглая юная девчонка бежит вперёд, отчаянно ища любые признаки жизни."
    maishawnee ". . . {rb}{i}Нига! Но'та!{/i}{/rb}{rt}(Мать! Отец!){/rt} . . ."
    "Заглядывая в двери маленьких хижин, Мая проверяет каждую из них."
    maishawnee ". . . {rb}{i}Но'ком'та! Ни-ме'сум'та!{/i}{/rb}{rt}(Бабушка! Дедушка!){/rt} . . ."
    "Я не понимаю шауни, на котором она говорит, но слышу отчаяние в её голосе."
    "Она зовёт своих близких. Свою семью и своих друзей."
    maishawnee ". . . {rb}{i}Ви'си! Пе-э-ва, пе-э-ва!{/i}{/rb}{rt}(Собачка! Иди сюда, мальчик!){/rt} . . ."
    
    show mai worry
    with dissolve
    
    "После долгих криков и беготни она возвращается ко мне."
    mai ". . . Я не понимаю . . ."
    "Мая смотрит вокруг, не зная, на чём остановить взгляд."
    mai ". . . Обри! . . ."
    me ". . .  . . ."
    
    show mai angry
    with hpunch
    
    mai ". . . Обри!! . . ."
    me ". . . Что?! . . ."
    "Я рявкаю на неё."
    
    show mai worry
    with dissolve
    
    mai ". . . Где они? Где моя семья? . . ."
    me ". . . Откуда, чёрт возьми, я знаю ... . . ."
    "Возможно, появились синие мундиры и заставили их уйти ..."
    "... может, они все были убиты во время той битвы ..."
    "... или они могли присоединиться к другому племени на юге."
    "По крайней мере, здесь нет тел."
    "Ни раненых, ни мёртвых."
    "Это место просто заброшенный город-призрак."
    me ". . . Они должны были уйти какое-то время назад ... . . ."
    mai ". . . Мы должны найти их! . . ."
    me ". . . Что ты мелешь? . . ."
    mai ". . . Мы должны искать! Мы должны найти мою семью! . . ."
    me ". . . И как мы собираемся это сделать? . . ."
    "Здесь нет золота, нет мехов, нет еды ..."
    "Ни с кем торговать и нечем торговать."
    mai ". . . Они могут прятаться, если американцы вернутся! . . ."
    mai ". . . Или они в соседней деревне! Они не могли уйти далеко! . . ."
    me ". . . Прекрати ... . . ."
    "Я не хочу этого слышать."
    mai ". . . Обри! Мы должны искать их! . . ."
    mai ". . . Они ждут, когда я вернусь домой! . . ."
    mai ". . . Мы не можем бросить их! . . ."
    
    show speedlines with hpunch
    hide speedlines with dissolve
    
    me ". . . Я сказал, прекрати! . . ."
    "Мой крик эхом разносится над рябью озёрных вод."
    mai ". . . Обри ... . . ."
    me ". . . Вся эта наша ерунда ... . . ."
    me ". . . Я не могу вернуть твоё племя . . ."
    "Я доставил тебя в твою деревню, разве этого недостаточно ..."
    me ". . . Я не могу сделать ничего другого . . ."
    
    show mai sad
    with dissolve
    
    "Постепенно паническое выражение лица Маи исчезает."
    "Его сменяет покорный, жалкий взгляд."
    mai ". . . Но ... моя семья ... . . ."
    "Я думаю промолчать, избавив её от резких слов."
    "Но кое-что нужно сказать ..."
    me ". . . Я не думаю, что они вернутся, Мая . . ."
    "Девчонка замолкает, не в силах ответить."
    me ". . . Нам здесь больше нечего делать . . ."
    "Мая и я осматриваем пустую деревушку, разбросанные вещи."
    "Это место было покинуто навсегда."
    mai ". . . Прости ... . . ."
    "Ребёнок извиняется."
    
    play sound2 "se/walk.ogg"
    hide mai sad
    with dissolve
    
    "Затем она разворачивается и идёт к ближайшему лесу."
    me ". . . Мая! . . ."
    "Я зову её, но она не отвечает."
    me ". . . Не уходи далеко! Оставайся рядом с деревней! . . ."
    
    play sound2 "se/brush.ogg"
    
    "Индейская девчонка скрывается в чаще леса и исчезает из виду."
    "Ей нужно побыть одной, чтобы прийти в себя и осмыслить случившееся."
    
    stop music fadeout 5.0
    scene canopy
    with dissolve
    
    "Я смотрю на ясное голубое небо вверху, пока дует лёгкий ветерок."
    me ". . . Чёрт ... . . ."
    
    $ mouse_visible = False
    scene black
    with dissolve4
    pause 2.0
    scene forest
    show leaves
    with dissolve4
    $ mouse_visible = True
    play sound2 "se/brush.ogg"
    play soundfx2 "se/walk.ogg" fadein 2.0
    play soundfx "se/birds.ogg" fadein 5.0
    show mai cry2 behind leaves
    with dissolve
    
    "Индейский ребёнок бредёт по лесу, её щёки залиты слезами."
    maishawnee ". . . {rb}{i}Нига ... Но'та ...{/i}{/rb}{rt}(Мать ... Отец ...){/rt} . . ."
    
    stop soundfx2 fadeout 2.0
    
    "Она тихо всхлипывает, плача по своим близким."
    "Неужели она потеряла их навсегда? Неужели они исчезли навсегда?"
    maishawnee ". . . {rb}{i}Ни-т-квем-а ...{/i}{/rb}{rt}(Сестра ...){/rt} . . ."
    "Что она может сделать, чтобы найти их снова?"
    "Куда же они ушли?"
    "Пока эти вопросы крутятся у неё в голове, ребёнок пытается успокоиться."
    "В конце концов она останавливается на поляне."
    
    play sound2 "se/brush.ogg"
    show mai sad
    with dissolve4
    
    "Вытирая глаза, Мая пытается стереть слёзы."
    "Пока она остывает, она смотрит на танцующие на ветру листья."
    maishawnee ". . . {rb}{i}Ноолеви-ло ...{/i}{/rb}{rt}(Тихо ...){/rt} . . ."
    "Сегодня необычайно тепло для осени."
    "Тем не менее, в это время года нет ни мошек, ни мух."
    "Вдалеке слышен звук нежных волн, плещущихся о берег озера."
    "Птицы продолжают перекликаться друг с другом с верхушек деревьев."
    "Грызуны в подлеске прячутся в своих норах."
    "Мая шмыгает носом, пытаясь прочистить его."
    mai ". . . Обри ... . . ."
    "Ненавидит ли он её теперь, когда они добрались?"
    "Он хотел торговать с её семьёй и уйти на юг."
    "Бросит ли он её теперь, когда она бесполезна для него?"
    maishawnee ". . . {rb}{i}Мат-та ...{/i}{/rb}{rt}(Нет ...){/rt} . . ."
    "Ей ненавистна сама мысль об этом."
    "Но она подозревает, что всё это может быть правдой."
    "Тогда, может, ей просто убежать одной?"
    "Она снова останется одна, бродя по равнинам ..."
    "Без единого друга в мире."
    
    play sound2 "se/brush.ogg"
    
    "Откуда-то из близости доносится шорох."
    
    show mai worry
    with dissolve
    
    "Вытирая глаза руками, Мая останавливается и прислушивается."
    "Не идёт ли Обри её искать?"
    
    play sound3 "se/mud.ogg"
    
    "Рядом слышны шаги и мужские голоса."
    "Но она не узнаёт их."
    "По этому лесу бродят чужие мужчины ..."
    
    play sound2 "se/brush.ogg"
    scene canopy
    with dissolve4
    
    "Мая быстро соображает и ныряет в укрытие среди деревьев."
    "Спрятавшись за ближайшей сосной, девчонка ждёт в тишине."
    
    stop soundfx fadeout 5.0
    play sound2 "se/brush.ogg"
    play music "music/reveal.ogg"
    play soundfx3 "se/mud.ogg"
    
    "Два солдата в синих мундирах выходят из кустов, оба с ружьями."
    daniels ". . . Сюда? . . ."
    mctavish ". . . О чём ты говоришь? . . ."
    daniels ". . . Мне показалось, я что-то слышал ... . . ."
    mctavish ". . . Тебе мерещится ... . . ."
    
    play sound2 "se/brush.ogg"
    
    captain ". . . Продолжайте движение! Мы почти на месте! . . ."
    "Третий солдат-янки появляется рядом с ними."
    captain ". . . Он где-то здесь ... я чувствую ... . . ."
    daniels ". . . Откуда вы знаете? . . ."
    captain ". . . Я следопыт. Это моё дело . . ."
    "Группа синих мундиров направляется через поляну."
    "Не замечая, они полностью упускают Маю."
    "Её сердцебиение замедляется, пока мужчины бредут по дикой местности."
    captain ". . . Только подождите ... вот увидите ... . . ."
    "Они начинают исчезать из виду и уходить в лес."
    mai ". . . {i}Хааа ...{/i} . . ."
    "Девчонка вздыхает с облегчением, когда они проходят мимо."
    
    stop soundfx3 fadeout 2.0
    
    captain ". . . Стойте! . . ."
    mctavish ". . . Что такое? . . ."
    "Капитан останавливается и осматривает местность."
    captain ". . . Здесь кто-то есть ... . . ."
    
    play sound3 "se/cock.ogg"
    
    "Группа готовит ружья и смотрит по сторонам."
    captain ". . . Это индейская девчонка ... . . ."
    daniels ". . . Индейская девчонка? . . ."
    
    play sound4 "se/brush.ogg"
    play sound2 "se/run.ogg"
    
    "Мая выбегает из своего укрытия и пытается направиться к деревне."
    mai ". . . Обри! . . ."
    "Громко зовёт она."
    
    play sound5 "se/swipe.ogg"
    play sound2 "se/gundrop.ogg"
    play sound3 "se/fall.ogg"
    play sound4 "se/brush.ogg"
    scene canopy
    with hpunch
    
    "Капитан протягивает руку и хватает Маю, когда она пробегает мимо."
    captain ". . . Попалась! Грязная маленькая скво! . . ."
    
    play sound2 "se/slap.ogg"
    
    mai ". . . {i}Нннн!{/i} . . ."
    
    play sound3 "se/smash.ogg"
    scene canopy
    with hpunch
    
    "Мая отчаянно сопротивляется, бросаясь на синий мундир."
    mai ". . . Отпусти меня! . . ."
    "Он пытается прижать её, но она яростно отбивается."
    
    play sound5 "se/rip.ogg"
    
    "Она рвёт его мундир, пинается и царапается."
    captain ". . . Прекрати, маленькая шлюха! . . ."
    
    play sound2 "se/collapse.ogg"
    play sound3 "se/brush.ogg"
    play sound4 "se/smash.ogg"
    scene canopy
    with hpunch
    
    "Он с силой бросает девчонку на лесную подстилку."
    
    play sound5 "se/cock.ogg"
    
    "Прежде чем она успевает встать, капитан наставляет на неё кремнёвый пистолет."
    captain ". . . Стоять на месте! . . ."
    "Мая свирепо смотрит на него снизу вверх."
    captain ". . . Что ты сказала? Ты сказала {i}'Обри'{/i}? . . ."
    "Ребёнок молчит, отказываясь отвечать."
    captain ". . . Так это действительно он ... . . ."
    mctavish ". . . Капитан? Что происходит? . . ."
    captain ". . . Ты никуда не пойдёшь, моя дорогая ... . . ."
    captain ". . . Вы двое, свяжите её и присматривайте за ней . . ."
    mctavish ". . . Что нам делать с индейским ребёнком? . . ."
    captain ". . . Она та, с кем путешествует этот красный мундир ... . . ."
    captain ". . . Это судьба, в конце концов ... . . ."
    "Капитан осматривается и замечает коричневые хижины на опушке леса."
    captain ". . . Вон там впереди деревня. Должно быть, он прячется там ... . . ."
    "Двое рейдеров обеспокоенно переглядываются."
    daniels ". . . Капитан ... кое-что вы должны знать ... . . ."
    daniels ". . . Некоторые из нас, и я в том числе, начинаем сомневаться ... . . ."
    captain ". . . Ну? . . ."
    daniels ". . . Ну ... не заходите ли вы слишком далеко . . ."
    captain ". . . Слишком далеко? . . ."
    daniels ". . . Преследовать красные мундиры — это одно, но мы далеко на юге . . ."
    daniels ". . . Мы уже несколько дней идём на голодный желудок . . ."
    daniels ". . . Вы не спали, и всё из-за одного ублюдка, которого мы выслеживаем . . ."
    "Солдат отступает назад, пока капитан угрожающе смотрит на него."
    captain ". . . Что ты говоришь, Дэниэлс? . . ."
    daniels ". . . Ну ... сэр ... . . ."
    mctavish ". . . Он говорит ... . . ."
    captain ". . . Выкладывай! . . ."
    "Солдат нервно высказывает свою мысль."
    daniels ". . . Вы никогда раньше так безумно не преследовали британцев . . ."
    mctavish ". . . Эй, полегче ... . . ."
    "Выражение лица капитана темнеет."
    captain ". . . Безумно? . . ."
    captain ". . . Ты только что назвал меня ... безумным? . . ."
    daniels ". . . Нет, капитан! Я не это имел в виду ... . . ."
    daniels ". . . Просто ... почему мы идём на все эти трудности ради одного красного мундира? . . ."
    captain ". . . Кого ты называешь безумным, Дэниэлс? . . ."
    daniels ". . . Вам нужно поспать, сэр! Вам нужен отдых! . . ."
    mctavish ". . . Он просто голоден, сэр, вот и всё . . ."
    captain ". . . Безумным?! . . ."
    daniels ". . . Сэр? . . ."
    
    play sound2 "se/cock.ogg"
    
    captain ". . . Я покажу тебе, что значит грёбаный безумный!! . . ."
    
    stop music fadeout 3.0
    play sound3 "se/flintlock2.ogg"
    scene canopy
    with flash
    
    "В одно мгновение капитан выхватывает пистолет и стреляет в солдата."
    mctavish ". . . Господи Иисусе! . . ."
    
    queue music "music/postshot.ogg" noloop
    play sound2 "se/collapse.ogg"
    play sound3 "se/brush.ogg"
    play sound4 "se/smash.ogg"
    
    "Рейдер падает на землю, истекая кровью из груди."
    captain ". . . Я не потерплю неподчинения в моих рядах ... . . ."
    "МакТавиш подбегает к Дэниэлсу, проверяя рану."
    "Но солдат лежит без сознания, в шоке."
    mctavish ". . . Капитан! Какого чёрта вы творите?! . . ."
    captain ". . . Вы должны подчиняться моим приказам ... . . ."
    
    play sound2 "se/walk.ogg"
    
    "С безумным блеском в глазах капитан поворачивается и уходит."
    captain ". . . Я покончу с этим раз и навсегда . . ."
    captain ". . . Присмотри за девчонкой и займись телом ... . . ."
    "Он уходит прочь в лес, скрываясь из виду."
    "Солдат смотрит вниз на тело своего друга."
    mctavish ". . . Дерьмо ... какого чёрта происходит ... . . ."
    "Медленно вздохнув, МакТавиш ловит взгляд девчонки."
    
    play sound2 "se/cock.ogg"
    play sound3 "se/brush.ogg"
    
    mctavish ". . . Не ... двигаться ... ни на дюйм ... . . ."
    "Взведя курок ружья, он встаёт и целится ей в голову."
    mctavish ". . . Ублюдок ... проклятый ублюдок ... . . ."
    
    stop sound3 fadeout 1.0
    stop music fadeout 4.0
    $ mouse_visible = False
    scene black
    with dissolve4
    pause 2.0
    play soundfx "se/birds.ogg" fadein 5.0
    scene village
    with dissolve4
    $ mouse_visible = True
    
    "Сидя в пустой деревне, я тычу кривой палкой в пепел кострища."
    me ". . . Мая . . ."
    "Её семьи нет ... кто знает, куда они отсюда ушли."
    "Они могли отправиться на север, чтобы присоединиться к Текумсе и сражаться."
    "Могли бродить на юго-запад, чтобы поселиться на неосвоенной территории."
    "Или ... через эти места могла пройти американская часть и уничтожить их ..."
    "Однако деревня выглядит нетронутой."
    "Нет никаких следов грабежа или чего-либо сожжённого дотла."
    "Возможно, их переселили или заставили это сделать под угрозой."
    "Мая же говорила, что британцы пытались манипулировать племенем, украв их {i}мишаами{/i}."
    
    play sound2 "se/brush.ogg"
    
    "Я слышу, как кто-то выходит из кустов позади меня."
    me ". . . Ты немного успокоилась? . . ."
    "Говорю я, не оборачиваясь, но не получаю ответа."
    me ". . . Мы решим, что делать дальше, хорошо? . . ."
    me ". . . Куда бы они ни пошли, я уверен, мы сможем это выяснить . . ."
    "Она не отвечает."
    me ". . . Подойди сюда . . ."
    "Я похлопываю по земле рядом с собой."
    "Но девчонка не появляется рядом."
    me ". . . Мая? . . ."
    
    stop soundfx fadeout 3.0
    
    "Оглянувшись, я сталкиваюсь с необычным зрелищем ..."
    "Кем-то, кого я никогда не думал увидеть снова ..."
    
    $ mouse_visible = False
    window hide
    play sound2 "se/brush.ogg"
    play music "music/ultimatum.ogg" fadein 5.0
    scene cg8
    with dissolve2
    pause 7.0
    window show
    $ mouse_visible = True
    
    "Из кустов выступает внушительная фигура."
    "Мои глаза медленно привыкают к этой сцене."
    "Длинные светлые волосы свисают сзади, туго стянутые в хвост."
    "Его синий мундир выделяется на фоне деревни и зелени лесной опушки."
    "Шрам пересекает правую бровь и веко."
    "Неся кремнёвый пистолет, персонаж останавливается передо мной."
    captain ". . . Привет, Уилл ... . . ."
    "Это мой старый партнёр ... мой друг-преступник из далёкого прошлого ..."
    me ". . . Д-Джексон! . . ."
    jackson ". . . Собственной персоной . . ."
    me ". . . Н-но я ... я думал, я ... . . ."
    jackson ". . . Что? Что ты застрелил меня? Что ты оставил меня умирать в тех лесах? . . ."
    jackson ". . . Думаешь, меня можно было так просто вывести из строя? . . ."
    "Я не знаю, что сказать."
    "Как он может быть ещё жив? И здесь, во вражеском мундире?"
    "Всё это не имеет смысла."
    
    scene village
    with dissolve
    show jackson evil
    with dissolve
    
    jackson ". . . Честно говоря, я не ожидал, что это будешь ты ... . . ."
    me ". . . Что ты здесь делаешь? . . ."
    jackson ". . . Я здесь из-за тебя, партнёр . . ."
    me ". . . Из-за меня? Ты о чём ... . . ."
    
    show jackson determined
    with dissolve
    
    jackson ". . . Где та девчонка, с которой ты путешествуешь? . . ."
    me ". . . Девчонка ... . . ."
    "Меня осеняет."
    "Мая где-то рядом. И Джексон знает, что она здесь."
    
    show jackson evil
    with dissolve
    
    jackson ". . . Она миленькая маленькая индеанка. Никогда не думал, что ты краснокожий ... . . ."
    me ". . . Я никакой не краснокожий ... не так как ты ... . . ."
    "Где бы ты ни была, Мая ... пожалуйста, спрячься."
    "Уберись в безопасное место. Не дай Джексону найти тебя."
    jackson ". . . Это не я таскаю за собой прерийную скво . . ."
    "Джексон злобно усмехается, делая несколько шагов ко мне."
    jackson ". . . Вы все одинаковые, вы любители индейцев . . ."
    jackson ". . . Белые снаружи, красные внутри . . ."
    jackson ". . . Найдёшь себе индейскую девчонку, наплодишь полукровок и бросишь их умирать в лесу . . ."
    me ". . . Я не знаю, о чём ты говоришь ... . . ."
    
    show jackson angry
    with dissolve
    
    jackson ". . . О, но я думаю, ты знаешь . . ."
    jackson ". . . Правда в том, что я выслеживал тебя уже несколько дней . . ."
    jackson ". . . Выкапывал твои кострища, доедал твои объедки, нюхал твои экскременты ... . . ."
    "Он ... следил за нами ..."
    "С каких пор? С битвы на реке {i}Темза{/i}? С {i}Детройта{/i}?"
    jackson ". . . Из нас двоих я всегда был лучшим охотником . . ."
    jackson ". . . Ты был слишком хорошо рождён, слишком образован, чтобы заметать следы . . ."
    "Мая ... где же ты ..."
    
    show jackson bored
    with dissolve
    
    jackson ". . . Я оказал этой малышке услугу, прикончив её . . ."
    me ". . . Что? . . ."
    
    show jackson evil
    with dissolve
    
    jackson ". . . Ты всё равно собирался застрелить её или продать, когда закончишь . . ."
    jackson ". . . Я знаю тебя. Ты всегда плохо обращался со своими женщинами . . ."
    "М-Мая ..."
    me ". . . Где она? . . ."
    "Неужели он ... она ... . . ."
    
    show jackson determined
    with dissolve
    
    jackson ". . . Какое тебе дело до какой-то паршивки? . . ."
    jackson ". . . Ей же будет лучше без тебя ... . . ."
    "Нет ... Мая ..."
    
    show jackson angry
    with dissolve
    
    "Медленно я тянусь к своему мушкету, лежащему поблизости."
    
    play sound2 "se/cock.ogg"
    scene cg5
    with hpunch
    $ achievement.grant("NEW_ACHIEVEMENT_1_4")
    
    jackson ". . . Ах-ах-ах ... не так быстро ... . . ."
    "Джексон поднимает пистолет и направляет его прямо мне в сердце."
    jackson ". . . Положи его и отойди . . ."
    me ". . . Хорошо ... просто расслабься ... . . ."
    "Я осторожно убираю руки от своей Браун Бесс и отступаю назад, подняв руки."
    jackson ". . . Ты всегда был импульсивным дураком . . ."
    jackson ". . . Ничего не смыслил в жизни. Мне пришлось учить тебя каждому приёму . . ."
    jackson ". . . Стрельбе, охоте, дракам... . . ."
    jackson ". . . Я имею в виду, ты даже убить меня толком не смог . . ."
    me ". . . Чего ты от меня хочешь? . . ."
    jackson ". . . Хочу? Ты всё ещё не понял? . . ."
    me ". . . Если собираешься стрелять, просто сделай это . . ."
    me ". . . Мне не нужны речи . . ."
    "Джексон строит недовольное выражение лица и скрипит зубами."
    jackson ". . . Десять лет ... десять чёртовых лет ... для тебя это ничего не значило ... . . ."
    me ". . . Это неправда ... . . ."
    jackson ". . . Ты стал жадным, у тебя появилась неуверенность ... . . ."
    jackson ". . . А когда ты больше не мог этого выносить, ты всё украл и застрелил меня! . . ."
    me ". . . Нет ... . . ."
    jackson ". . . Ты бросил меня на обочине с пулей в плече!! . . ."
    jackson ". . . Меня, твоего единственного друга в тех лесах ... . . ."
    jackson ". . . То, что мы делали ... те люди, которых мы убили ... . . ."
    "В его голосе дрожь. Трепет одиночества."
    jackson ". . . Глупый английский парень один в новой республике . . ."
    jackson ". . . Живущий ото дня ко дню, без единого друга в мире ... . . ."
    "Но одиночество вскоре исчезает, сменяясь обычной злобой и недоверием."
    jackson ". . . Оглядываясь назад, я был дураком, что вообще доверился тебе . . ."
    jackson ". . . Ты был слишком хорош для этого, слишком хорош для денег ... . . ."
    jackson ". . . Ты хоть раз боролся за что-то значимое? . . ."
    jackson ". . . Развеваешь флаг страны, которую не можешь вспомнить, стреляешь в людей, которым когда-то доверял ... . . ."
    jackson ". . . Ты думаешь, что так сможешь обрести покой? . . ."
    me ". . . Я ... . . ."
    jackson ". . . Я знаю тебя лучше ... ты никогда не обретёшь покой, будучи таким, как есть . . ."
    jackson ". . . Всё, на что ты годишься, — это убегать . . ."
    "Вдавив дуло своего пистолета мне в яремную вену, Джексон усмехается."
    jackson ". . . Что ж, больше ты не убежишь . . ."
    jackson ". . . У меня теперь есть своя маленькая армия . . ."
    jackson ". . . И я целыми днями стреляю таких английских придурков, как ты . . ."
    me ". . . Ты охотишься на дезертиров, верно? На потерявшихся красных мундиров? . . ."
    me ". . . Ты часть рейдерского отряда, который рубит всех, кого находит . . ."
    me ". . . Это не армия . . ."
    jackson ". . . За такую работу я получаю медали . . ."
    jackson ". . . А когда эта война закончится, у меня будет ещё и участок земли, и карманы, полные монет . . ."
    jackson ". . . Звучит неплохо для меня . . ."
    me ". . . Что? Отправлять мужчин домой в сосновых ящиках? . . ."
    jackson ". . . Ты, должно быть, шутишь . . ."
    jackson ". . . Для таких дезертиров, как ты, не бывает похорон . . ."
    
    play sound2 "se/cock.ogg"
    
    "С угрожающей усмешкой Джексон наводит свой кремнёвый пистолет прямо мне в грудь."
    jackson ". . . В любом случае, я никогда не был любителем затягивать казнь ... . . ."
    "Вот и всё."
    jackson ". . . Всё кончено, Обри ... в этот раз ты проиграл ... . . ."
    "Я действительно умру здесь."
    
    stop soundfx fadeout 5.0
    stop music fadeout 5.0
    scene black
    with dissolve
    
    "Я закрываю глаза в ожидании."
    "Медленно секунды уходят, и я принимаю свою судьбу ..."
    ". . .  . . ."
    "Мая ..."
    "Прости ... я не смог тебе помочь ..."
    ". . .  . . ."
    
    play sound2 "se/misfire.ogg"
    scene black
    with hpunch
    
    "Джексон стреляет."
    "Но что-то в этом выстреле звучит ... не так ..."
    
    play soundfx "se/birds.ogg" fadein 10.0
    
    "Я не чувствую ни пронзительной пули, ни жгучей боли разорванной плоти."
    "Ни сломанных костей, ни крови."
    
    scene village
    show jackson shock
    with dissolve
    
    "Я открываю глаза."
    "Осмотрев себя, я понимаю, что совершенно невредим."
    
    play sound2 "se/gundrop.ogg"
    play sound3 "se/smash.ogg"
    
    "Камень отскакивает от пистолета Джексона, который с грохотом падает на землю."
    
    play music "music/tothedeath.ogg"
    
    jackson ". . . Ч-Что за?! . . ."
    "Я смотрю в ближайший лес ... и вижу Маю, стоящую там с камнем в руке."
    "Она заставила его промахнуться!"
    "Должно быть, её камень сбил его пистолет с прицела."
    
    show jackson angry
    with dissolve
    
    jackson ". . . Т-Ты глупая паршивка! . . ."
    me ". . . Она жива ... . . ."
    jackson ". . . Я надеялся оставить её в живых и продать на каком-нибудь посту . . ."
    me ". . . Ты ублюдок! . . ."
    
    play sound2 "se/smash.ogg"
    show jackson shock
    with hpunch
    
    "Из лесной опушки Мая бросает ещё один камень, который разбивается о правую руку Джексона."
    jackson ". . . Йах! Чёрт возьми, это больно, проклятье! . . ."
    
    show jackson angry
    with dissolve
    
    jackson ". . . Всё, хватит! Я задушу эту грязную скво!! . . ."
    
    play sound2 "se/swipe.ogg"
    play sound3 "se/smash.ogg"
    show jackson shock
    with hpunch
    
    "Ещё один камень летит в нашу сторону, и мы оба уворачиваемся."
    
    play sound2 "se/cock.ogg"
    play soundfx3 "se/run.ogg"
    play sound3 "se/gundrop.ogg"
    
    "Пользуясь моментом, я бросаюсь вперёд и хватаю свой мушкет, пока Джексон шарит вокруг в поисках пистолета."
    jackson ". . . Нет ... Нет! . . ."
    "Схватив свою Браун Бесс, я бегу к лесу, пока мой враг отчаянно пытается перезарядиться."
    
    play sound2 "se/swipe.ogg"
    play sound3 "se/smash.ogg"
    play sound4 "se/brush.ogg"
    show jackson shock
    with hpunch
    
    "Мая бросает ещё один камень в Джексона, пока я хватаю её за руку."
    
    show jackson angry
    with dissolve
    
    jackson ". . . А ну вернитесь, отребье! . . ."
    
    scene forestfade2
    with fade
    play soundfx2 "se/flintlock.ogg"
    play soundfx4 "se/walk.ogg"
    play soundfx5 "se/brush.ogg"
    
    "Бежим через лесополосу, направляясь к безопасному месту."
    "Я тащу Маю за собой, пока мы исчезаем всё глубже и глубже в лесу."
    "Джексон преследует нас неподалёку, выкрикивая что-то вслед девчонке."
    
    show speedlines with circleirisout
    hide speedlines with dissolve
    
    jackson ". . . Вернись, прерийная скво!! . . ."
    "Он стреляет из пистолета нам вслед, вырывая куски из деревьев."
    jackson ". . . Ублюдок!! . . ."
    "Мы уворачиваемся и ныряем туда-сюда, избегая выстрелов."
    "Пробираясь сквозь листву, мы исцарапаны ветками и кустами, пока бежим."
    me ". . . Давай! Мы должны продолжать! . . ."
    "Мая тяжело дышит и изо всех сил пытается не отставать."
    "Я практически тащу её через подлесок в своём темпе."
    "Держа озеро с правой стороны, мы продолжаем движение."
    "Кусочки дерева и листьев разлетаются вокруг нас каждый раз, когда Джексон стреляет."
    jackson ". . . Вернитесь!! . . ."
    "Лучи света пробиваются в пологе леса над головой, когда он промахивается."
    "Вскоре мы оставляем деревню позади и углубляемся в лес."
    "Маленькие красные ботинки девчонки врезаются в грязь, пока мы бежим."
    "Она не сможет продолжать бежать дольше."
    
    stop soundfx5 fadeout 1.0
    stop soundfx3 fadeout 1.0
    stop soundfx4 fadeout 1.0
    scene forest
    show leaves
    with dissolve
    play sound3 "se/brush.ogg"
    show mai worry behind leaves
    with dissolve
    
    "В конце концов мы останавливаемся на поляне."
    "Американец довольно далеко позади, но быстро приближается."
    "Переведя дыхание, я пытаюсь придумать план."
    me ". . . Если мы продолжим идти на юг, то сможем обогнуть озеро и выйти на запад ... . . ."
    me ". . . Мы можем уйти от него в холмах и направиться к побережью ... . . ."
    me ". . . А потом попробуем найти твою семью . . ."
    
    play sound4 "se/brush.ogg"
    show mai normal
    with dissolve
    
    "Снова взяв Маю за руку, я начинаю идти."
    
    stop sound4 fadeout 1.0
    play sound2 "se/swipe.ogg"
    show mai angry
    with hpunch
    
    "Но Мая сопротивляется."
    me ". . . Что такое? Что ты делаешь? . . ."
    mai ". . . Нам нужно разделиться . . ."
    me ". . . Разделиться?! О чём ты говоришь? . . ."
    mai ". . . Он будет продолжать преследовать нас, даже если мы убежим . . ."
    mai ". . . Он не перестанет следовать за нами, пока мы не умрём . . ."
    me ". . . Тогда что ты предлагаешь? . . ."
    mai ". . . Я отвлеку его . . ."
    me ". . . Отвлечёшь его? . . ."
    mai ". . . А ты попытаешься застрелить его, прежде чем он поймает меня . . ."
    
    play sound2 "se/run.ogg"
    hide mai with easeoutleft
    
    "Прежде чем я успеваю что-либо сказать, Мая убегает обратно в сторону Джексона."
    me ". . . Подожди минутку! Мая! . . ."
    "Она убежала."
    me ". . . Чёрт ... . . ."
    
    play sound2 "se/brush.ogg"
    
    "Услышав шорох позади себя, я действую быстро."
    
    scene forestfade2
    show leaves
    with dissolve
    
    "Развернувшись, я перепрыгиваю через ближайший куст и ныряю в подлесок."
    
    stop soundfx2 fadeout 1.0
    play sound2 "se/walk.ogg"
    show jackson angry behind leaves
    with dissolve
    
    "Джексон появляется вскоре после этого."
    
    play sound3 "se/flintlock2.ogg"
    show jackson angry with flash
    
    "Выстрелив из своего кремнёвого пистолета в поляну, негодяй отчаянно ищет индейскую девчонку."
    jackson ". . . Грёбаный красный мундир ... грёбаная скво ... . . ."
    jackson ". . . Где вы оба ... . . ."
    
    play sound2 "se/walk.ogg"
    hide jackson
    with dissolve
    play soundfx2 "se/flintlock.ogg"
    
    "Ничего не найдя, он возвращается в лес."
    "Я жду, пока Джексон скроется из виду, прежде чем начать преследование."
    
    play sound3 "se/brush.ogg"
    
    "Пробираясь через подлесок, я выхожу на край поляны."
    "Синий мундир продолжает стрелять вслед за девчонкой."
    jackson ". . . Вернись сюда!! . . ."
    "Дальше вдоль лесной опушки я зарываюсь в землю за старым стволом и взвожу мушкет."
    me ". . . Он делает четыре выстрела в минуту ..."
    
    play sound4 "se/rip.ogg"
    
    "Откусывая скрученный конец патрона, я выплёвываю бумагу."
    
    play sound2 "se/cock.ogg"
    
    "Затем я ставлю курок на предохранительный взвод и насыпаю порох."
    me ". . . это даёт мне пятнадцать секунд, чтобы убить этого глупого ублюдка . . ."
    "Выглядывая из-за дерева, я наблюдаю, как Джексон продвигается на восток."
    "Следуя за его взглядом, я вижу, как Мая перебегает от укрытия к укрытию."
    "Он уже увидел её?"
    "Закрыв кресало, я заталкиваю остатки пороха, пулю и бумагу."
    me ". . . давай же ... . . ."
    "Достав шомпол, я забиваю пыж к казённой части и возвращаю его на место."
    me ". . . Наконец-то ... . . ."
    "У меня есть только один выстрел, прежде чем я выдам своё местонахождение."
    jackson ". . . Вот ты где, грязный краснокожий!! . . ."
    "Похоже, девчонка начала отвлекать его."
    
    play sound3 "se/cock.ogg"
    
    "Я изготовился со своей Браун Бесс, но обнаруживаю, что синий мундир исчез из виду."
    "Следуя за голосом Джексона, я замечаю, что он идёт в двадцати ярдах от меня, стоя ко мне спиной."
    
    play sound2 "se/brush.ogg"
    
    "Медленно я пробираюсь вперёд сквозь кусты и вижу Маю далеко впереди, забравшуюся на ветку."
    
    play sound3 "se/smash.ogg"
    play sound4 "se/creak.ogg"
    
    "Осторожно девчонка прыгает с дерева на дерево, а листья разлетаются вокруг неё."
    
    scene cg5fade
    show blast
    with dissolve
    play soundfx2 "se/flintlock2.ogg"
    
    "Дыры пробиваются в пологе леса, когда Джексон стреляет в неё выстрел за выстрелом."
    jackson ". . . Попалась, маленькая паршивка! . . ."
    "Смуглая девчонка прыгает с ветки на ветку, отчаянно пытаясь избежать выстрелов."
    "Джексон усмехается, охотясь на свою добычу."
    jackson ". . . Подожди, я покажу Обри, что поймал дикую древесную скво ... . . ."
    "Прохаживаясь по лесу, он смеётся как безумец."
    "Девчонка проворно прыгает, но она недостаточно быстра, чтобы избежать выстрелов."
    jackson ". . . Эхе-хе-хе! Ты моя! . . ."
    "Он играет с ней, заставляя её метаться туда-сюда."
    "Дроблёная кора дождём сыплется сверху, когда он стреляет в кроны деревьев, заставляя её прыгать."
    "Я чуть не окликаю Маю, чтобы отвлечь Джексона, но прикусываю язык."
    
    scene forestfade2
    with dissolve
    play soundfx2 "se/flintlock.ogg"
    
    "Это мой шанс."
    "Выхожу на позицию, скрытый за кустом, снова изготовившись и прицелившись."
    "Джексон стреляет, и Мая спрыгивает вниз, скрываясь в лесу впереди."
    "Стоя ко мне спиной, синий мундир спотыкается, перезаряжаясь."
    
    scene forest
    show leaves
    with dissolve
    
    "Целясь, я успокаиваюсь и сосредотачиваюсь на Джексоне."
    me ". . . Эй! Придурок! . . ."
    
    stop sound4 fadeout 1.0
    stop soundfx2 fadeout 1.0
    show jackson angry behind leaves
    with dissolve
    
    "Медленно он поворачивается ко мне лицом ..."
    "С безумным блеском в глазах перебежчик выглядит готовым броситься вперёд."
    
    play sound2 "se/flintlock2.ogg"
    play sound3 "se/flintlock2.ogg"
    play soundfx3 "se/tinnitus.ogg" fadein 5.0
    stop music fadeout 5.0
    stop soundfx fadeout 3.0
    pause 0.3
    scene forestfade2
    show jackson shock
    show leaves
    with flash
    
    "Прежде чем он успевает среагировать должным образом, мой выстрел проходит насквозь через его грудь."
    "Чёрный дым и искры летят мне в лицо, когда меня отбрасывает отдачей мушкета."
    jackson ". . . ! . . ."
    me ". . . ! . . ."
    jackson ". . . Н-Нет ... не может быть ... . . ."
    
    hide jackson with dissolve
    play sound2 "se/collapse.ogg"
    play sound3 "se/brush.ogg"
    play sound4 "se/smash.ogg"
    
    "Тело Джексона складывается и падает на землю."
    "Листья взлетают и танцуют, как только его фигура ударяется о лесную подстилку."
    "Его бледное лицо врезается в грязь, и спустя время он медленно перестаёт двигаться."
    "Я остаюсь на месте несколько мгновений, прежде чем позволить прикладу мушкета упасть в грязь."
    
    stop soundfx3 fadeout 3.0
    play soundfx "se/birds.ogg" fadein 5.0
    scene forest
    with dissolve
    
    "В конце концов моё дыхание возвращается, как и слух."
    me ". . . Хах ... хах ... хах ... . . ."
    "Я вдыхаю свежий воздух в лёгкие, и сердцебиение начинает спадать."
    me ". . . Я ... я сделал это ... . . ."
    "Я застрелил ублюдка."
    "Посмотрев на его труп, я толкаю его ногой."
    "Он больше не дышит..."
    me ". . . Всё кончено ... . . ."
    "Наконец-то всё кончено."
    "Это то, чего он хотел ..."
    "Я или он, как он и хотел."
    "Но не думаю, что он ожидал такого исхода."
    "Он выбрал свою сторону, как и меня призвали на мою."
    "И всё же он умирает, так и не обретя свободы."
    "Его погоня за счастьем причинила страдания многим, и всё же он маршировал вместе с {i}'благородными людьми'{/i}."
    me ". . . Скатертью дорога ... . . ."
    "Но что насчёт меня? Что мне делать?"
    "Семьи Маи больше нет, но со временем она найдёт своё племя."
    "Это оставляет меня одного, бродящим во враждебном мире."
    "У меня нет любви к моему королю. У меня нет любви к республике."
    "Джексон был прав в одном: я всегда был соотечественником без родины."
    "Солдатом без флага ..."
    "Мои угрызения совести помешали мне выбрать сторону ... помешали мне сражаться за что-то большее ..."
    "Я жил и сражался только за себя; за место, которое мог бы назвать своим домом."
    "Теперь я покончил с этим заблуждением."
    "Тем, кем я был, тем, кем я являюсь."
    "Тем, что я сделал, за что нет прощения ..."
    "Нет такой границы, которую я мог бы найти, не следуя за гербом."
    "Нет очага или кресла без могил под ними."
    "Нет постели, не отмеченной пятнами побеждённых и нечистых."
    "Орёл кружит в небе, мышь зажата в его когтях ..."
    "Теперь я вижу это яснее ..."
    "По крайней мере, сейчас у меня есть на чём сосредоточиться."
    "То, о чём стоит заботиться."
    me ". . .  . . ."
    "Когда я начинаю сосредотачиваться, я оглядываю лес."
    "Никаких следов девчонки."
    me ". . . Мая ... . . ."
    "Я зову её по имени."
    me ". . . Мая! Где ты? . . ."
    "Сложив руки рупором, я кричу в сторону леса."
    me ". . . А ну тащи свой костлявый зад сюда! . . ."
    "Проходит несколько мгновений, но девчонки не видно."
    me ". . . Чёрт ... . . ."
    
    scene canopy
    with fade
    play soundfx2 "se/walk.ogg" fadein 5.0
    play soundfx3 "se/brush.ogg" fadein 5.0
    
    "Перекинув мушкет через плечо, я оставляю труп Джексона гнить и направляюсь в подлесок."
    me ". . . Мая! Выходи сейчас же! . . ."
    "Посмотрев вверх на полог леса, я слежу за любым движением."
    "Из веток выбиты куски, а стволы помяты выстрелами."
    "Кусочки коры разбросаны по лесной подстилке."
    "Джексон и правда разнёс кроны деревьев в щепки."
    me ". . . Мая! . . ."
    "Я снова зову."
    
    stop soundfx2 fadeout 3.0
    stop soundfx3 fadeout 3.0
    
    mai ". . . Об ... ри ... . . ."
    "Откуда-то из близости я слышу нежный голос, бормочущий что-то."
    me ". . . Мая! . . ."
    
    stop soundfx fadeout 3.0
    scene black
    with fade
    play sound2 "se/brush.ogg"
    
    "Я останавливаюсь на открытом пространстве."
    "Сломанные ветки лежат вокруг. Листва истоптана и потревожена."
    "На окрестных деревьях широкие пулевые отверстия оставили свой след."
    "Мои глаза притягиваются к участку грязи в центре поляны."
    "Там распростёрта фигура, и по земле разбрызгана кровь ..."
    
    $ mouse_visible = False
    window hide
    play music "music/aflight.ogg" fadein 20.0
    scene cg6 large
    with dissolve2
    pause 10.0
    scene cg6
    with dissolve4
    pause 1.0
    window show
    $ mouse_visible = True
    $ achievement.grant("NEW_ACHIEVEMENT_1_5")
    
    "Затем я вижу её ..."
    me ". . . Нет! . . ."
    "Мая лежит, истекая кровью на земле."
    mai ". . . Он гнался за мной ... через лес . . ."
    "Лазала по деревьям, чтобы отвлечь его внимание ..."
    me ". . . Зачем ты сделала такую глупость?! . . ."
    "Если бы она не убежала тогда ... если бы она спряталась в укрытии."
    mai ". . . Прости ... . . ."
    me ". . . Глупый ребёнок . . ."
    mai ". . . Прости ... . . ."
    "Это я глупый."
    "Если бы я не позволил ей убежать тогда ..."
    "Если бы мы продолжали бежать к краю леса."
    me ". . . За что ты извиняешься в таком состоянии? . . ."
    "Ах, это потому что я отчитываю её."
    "Мая улыбается, пока в уголках её глаз появляются слабые слёзы."
    mai ". . . Прости . . ."
    "Я приседаю рядом с ней, чтобы проверить её состояние."
    me ". . . Не двигайся . . ."
    "Её лодыжки сломаны, вывернуты ... выбиты из суставов ..."
    "Судя по пологу леса над головой, она, должно быть, упала с самой вершины."
    "Огнестрельное ранение в бок, сломанные ноги ... вероятно, и позвоночник тоже сломан ..."
    mai ". . . Об ... ри ... . . ."
    "Она теряет много крови."
    "Лужа багрового цвета продолжает растекаться по земле, становясь темнее, когда впитывается в грязь."
    me ". . . Старайся не говорить . . ."
    "Холодный ветер дует с озера, небо темнеет."
    "Дикие животные в окрестных лесах шумят."
    "Но я игнорирую всё это."
    "Передо мной ничего нет, кроме Маи."
    mai ". . . Что случилось ... с тем американцем ... . . ."
    me ". . . Я разобрался с ним ... . . ."
    mai ". . . Ты ... не ранен? . . ."
    "Спрашивает обо мне в таком состоянии ..."
    me ". . . Со мной всё в порядке. Пока что беспокойся о себе . . ."
    "У тебя нет времени беспокоиться обо мне."
    mai ". . . Я пыталась ... отвлечь его ... . . ."
    me ". . . Я знаю . . ."
    mai ". . . Прости . . ."
    me ". . . Не надо . . ."
    mai ". . . Об ... ри ... . . ."
    "Она начинает с трудом подбирать слова."
    "Её тело сдаёт борьбу."
    mai ". . . Я нашла его ... на опушке леса . . ."
    mai ". . . Синий мундир ... увидел меня ... и схватил . . ."
    mai ". . . Мне удалось ... сбежать ... . . ."
    mai ". . . Вот как он ... нашёл тебя ... . . ."
    me ". . . Понятно . . ."
    "Пока она плакала в одиночестве, Джексон нашёл её и погнался за ней."
    "Всё потому, что он искал меня; выслеживал меня ..."
    "Это моя вина."
    "Если бы я разобрался с Джексоном давным-давно ..."
    "Если бы я никогда не вёл такую никчёмную жизнь."
    mai ". . . Там ... есть другие . . ."
    me ". . . Другие? Какие другие? . . ."
    mai ". . . Американцы. Они были ... с синим мундиром ... . . ."
    mai ". . . На опушке леса . . ."
    mai ". . . У них ... у всех были ружья ... . . ."
    "В таком случае, его друзья должны были услышать выстрелы."
    "Они скоро прибудут, чтобы закончить дело."
    mai ". . . Обри ... . . ."
    "С паникой в голосе Мая пытается поднять голову, но едва ли может это сделать."
    mai ". . . Обри?! . . ."
    "Отчаянно пытаясь повернуть голову, она ворочается в грязи, её глаза мечутся."
    mai ". . . Где ... где ты ... . . ."
    me ". . . Мая? . . ."
    mai ". . . Я тебя ... нигде ... не вижу . . ."
    "Должно быть, её зрение слабеет."
    me ". . . Я здесь, Мая . . ."
    "Протянув руку, я беру её ладонь в свою и мягко сжимаю."
    mai ". . . Ах ... вот ты ... где ... . . ."
    me ". . . Я здесь . . ."
    mai ". . . Ты исчез ... на мгновение ... в размытом пятне . . ."
    "Мне следовало оставить её в том сарае. Нам следовало разойтись там."
    "Возможно, тогда этой сцены не случилось бы ..."
    me ". . . Я ... здесь . . ."
    mai ". . . Ах ... . . ."
    "Её кожа холодная и влажная от грязи."
    "Светлые мышцы покрыты синяками и отёками, покрыты шрамами от падения."
    "Мая сжимает мою руку в ответ, но её силы угасают."
    mai ". . . Ах ... Об ... ри ... . . ."
    me ". . . Что такое? . . ."
    mai ". . . Можно ... мне попросить ...? . . ."
    me ". . . Попросить? . . ."
    mai ". . . {i}Мишаами{/i}... . . ."
    "Она пытается показать, но её руки почти не двигаются."
    me ". . . Твоя священная сумка? . . ."
    mai ". . . Ах ... ты запомнил ... . . ."
    "Та самая, которую я пытался украсть в сарае."
    mai ". . . Пожалуйста ... возьми её ... . . ."
    me ". . . Что ты хочешь, чтобы я с ней сделал? . . ."
    mai ". . . Сохрани ... её ... . . ."
    mai ". . . и ... найди ... мою семью ... . . ."
    "Её семью? Я бы и не знал, с чего начать ..."
    "Племена и пилигримы мигрируют по всему этому континенту."
    "Невозможно найти одну конкретную семью во всей этой неразберихе ..."
    mai ". . . Они ... захотят знать ... где я ... . . ."
    mai ". . . что со мной случилось ... . . ."
    me ". . .  . . ."
    "Я не принимаю её просьбу. Я ничего не говорю."
    "Вместо этого я просто молча держу её за руку."
    mai ". . . Эй ... Обри ... . . ."
    me ". . . Что? . . ."
    mai ". . . Ты веришь ... в загробную жизнь ...? . . ."
    me ". . . Мы уже говорили об этом . . ."
    "Как всегда, она просто смотрит на меня, ожидая настоящего ответа."
    me ". . . Я не знаю . . ."
    me ". . . Я ничего не знаю обо всём этом . . ."
    "Мая смотрит на меня нежным взглядом."
    mai ". . . Христиане ... говорят о рае ... . . ."
    mai ". . . В лагере был священник ... . . ."
    me ". . . Когда ты была пленницей? . . ."
    "Она кивает."
    mai ". . . Он говорил о месте ... . . ."
    mai ". . . Месте света и любви . . ."
    mai ". . . Где ты снова можешь увидеть свою семью и друзей ... . . ."
    "Пожалуйста ... давай не будем больше об этом говорить."
    "Слишком много времени прошло с тех пор, как я видел смысл в молитвах о рае."
    mai ". . . У нас тоже есть место, куда мы идём ... у нас тоже есть дух, который ведёт нас ... . . ."
    mai ". . . Мы молимся ... и танцуем ... и чувствуем ветер в волосах ... . . ."
    mai ". . . Мы, шауни ... становимся единым целым с небом ... . . ."
    mai ". . . Мы ничем не отличаемся ... . . ."
    "Варварские. Языческие. Сатанинские."
    "Вот какие они."
    "Странные люди, живущие на деревьях."
    "Это нам говорят с детства."
    mai ". . . Так почему же ... . . ."
    mai ". . . Почему мы такие нечистые для них? . . ."
    mai ". . . Почему они говорят, что я попаду в ад ... . . ."
    mai ". . . Почему мы те, кто будут гореть в огне ... . . ."
    mai ". . . Те, кто покинут свои земли и умрут как собаки ... . . ."
    me ". . .  . . ."
    mai ". . . Я чувствую любовь ... я тоже люблю ... . . ."
    mai ". . . У меня есть отец ... и мать ... и сестра ... . . ."
    mai ". . . Так почему же ... . . ."
    mai ". . . Почему наш народ ... . . ."
    mai ". . . Почему мы ... . . ."
    me ". . .  . . ."
    "Я не знаю."
    "Есть ли загробная жизнь ..."
    "Есть ли прощение для преступников и солдат."
    "Есть ли надежда для язычников и рабов."
    "Я ничего этого не знаю."
    "Должно же быть что-то ... должно быть ..."
    "Но в своём сердце я не могу представить, что это так."
    mai ". . . Я... не хочу ... . . ."
    mai ". . . Я не хочу умирать ... одна ... . . ."
    mai ". . . Я не хочу ... быть отдельной ... . . ."
    mai ". . . Небо ... твой рай ... должно быть для всех ... . . ."
    mai ". . . Должно быть ... . . ."
    "Паника в её голосе становится сильнее, когда она продолжает."
    mai ". . . Должно быть . . ."
    me ". . . Мая ... . . ."
    mai ". . . пожалуйста ... боги ... Бог ... . . ."
    maishawnee ". . . {rb}{i}Вишеменету ...{/i}{/rb}{rt}(Великий Дух){/rt} . . ."
    mai ". . . кто бы ни слушал ... . . ."
    mai ". . . Я не ... хочу быть одна ... больше ... . . ."
    mai ". . . Я ... не хочу ... быть ... отдельной ... . . ."
    mai ". . . Я не хочу ... быть нечистой для тебя ... . . ."
    ". . .  . . .  . . ."
    "Я знаю, эти молитвы не будут услышаны."
    "Я достаточно долго сражался, чтобы знать."
    "Это случается со всеми нами."
    "Сгнить и исчезнуть — неизбежно."
    me ". . .  . . ."
    "Но этот неискренний, воображаемый укор бессмыслен."
    "Всё, что я могу, — это смотреть, как она умирает как собака, истекая кровью в грязи."
    "Я слегка сжимаю её руку."
    me ". . . Ты не одна. Я здесь . . ."
    "Тебе осталось недолго."
    "Так что, пожалуйста ... не смотри на меня таким одиноким взглядом."
    "Пожалуйста, не проси о чём-то таком эгоистичном."
    
    stop music fadeout 5.0
    
    "Медленно девчонка наклоняет голову и смотрит ещё глубже в мои глаза."
    "Даже если она ничего не видит ... она пристально смотрит на меня ..."
    mai ". . . Об ... ри ... . . ."
    mai ". . .  . . ."
    
    play music "music/lastwish.ogg" fadein 5.0
    
    maishawnee ". . . {rb}{i}Ниахв ... Ни дже ни нух ...{/i}{/rb}{rt}(Спасибо ... брат ...){/rt} . . ."
    "Эти загадочные слова, совершенно непонятные для меня, тем не менее заставляют Маю улыбнуться."
    "Словно она совершила последнюю шалость; в последний раз поддразнила меня своими словами."
    me ". . . Мая ... . . ."
    
    scene cg6 2
    with dissolve4
    
    "Медленно свет в её глазах мерцает и гаснет, прежде чем рассеяться во тьме."
    "Эти яркие озёра мутнеют и пустеют."
    "Слёзы на её щеках скатываются вниз, к земле, разбрызгиваясь по грязи."
    "Одним последним движением дыхание покидает её тело, и её голова падает назад."
    me ". . . Мая ... . . ."
    "Всё ещё держа её за руку ... маленькая девочка шауни покоится с миром ..."
    "Мёртвая ..."
    "Её жизнь была ужасной борьбой."
    "Но в её выражении нет ни боли, ни страха."
    "Принятие омывает её лицо в последние секунды её короткой жизни."
    "Я даже не рассказал ей о себе ... о битвах."
    "И она всё равно доверяла мне всё это время."
    "Я не плачу ... я не кричу ... я не стучу кулаками по земле ..."
    "Это выбили из меня давным-давно."
    "Стоя на коленях в грязи заброшенного леса, я молча смотрю."
    "Тело девчонки не движется."
    "Волосы колышет лёгкий ветерок, но и только ..."
    "Как долго я смотрю на её труп ... я не знаю ..."
    "Возможно, в некоторой степени я хочу исполнить её желание."
    "Чего она боялась больше всего — так это быть совсем одной в этом мире."
    "Много ночей в плену, вдали от семьи, она, должно быть, сидела в темноте ..."
    "Охраняя то свёрнутое одеяло, полное индейских грёз, и плача по своим потерянным друзьям ..."
    "Лежащая рядом с ней в грязи, {i}мишаами{/i} запятнана её кровью."
    me ". . . Мая ... . . ."
    
    ". . .  . . ."
    "Адское дело — не плакать ..."
    
    stop music fadeout 10.0
    scene black
    with dissolve4
    pause 0.5
    
    "В конце концов я нахожу в себе силы собраться и покинуть это проклятое место."
    "Вокруг на многие мили лишь пустая сельская местность, я бреду без определённого направления."
    "Вскоре наступает ночь и проходит, но я решаю продолжать идти."
    
    play soundfx "se/birds.ogg" fadein 10.0
    play soundfx2 "se/march.ogg" fadein 10.0
    scene sky
    with dissolve4
    
    "Когда я бреду при свете зари, я слышу марш синих мундиров поблизости."
    "Друзья Джексона, без сомнения ..."
    "Красные мундиры ... Синие мундиры ... Индейцы ..."
    "До того, как эта война закончится, сколько ещё умрёт?"
    "Я молюсь, чтобы меня среди них не было."
    "Я запахиваюсь в свою шинель, когда холод нового дня вступает в свои права."
    "На горизонте нет никаких признаков дождя. Никаких бурь впереди."
    "Под мышкой я несу индейскую сумку Маи. Не думая, я просто взял её ..."
    "Её семья ... её племя ..."
    "Возможно, есть какой-то шанс, что их можно найти ..."
    "Всё это может быть глупым квестом. Детской фантазией."
    "В конце концов, она была из другого мира."
    "Она была глупой девчонкой ..."
    "... а я дурак, что ввязался в её невинные мечты."
    "Глядя на небо, я размышляю о звёздах вдали и о кружащихся небесах."
    "О том мирном месте, на которое мы с ней когда-то надеялись."
    "Я не видел смысла верить. Это было то, о чём я не мог молиться."
    "Но теперь ... мне остаётся только желать этого."
    "Куда мне пойти, чтобы встретиться с ней снова?"
    "Что я могу сделать, чтобы обрести тот покой, который она обрела в своём последнем вздохе?"
    "Извилистая тропа через лес начинает выравниваться, когда я двигаюсь на юг."
    "Медленно я исчезаю всё глубже в лесу, а звуки марша затихают вдалеке ..."
    
    $ renpy.block_rollback()
    $ _rollback = False
    $_game_menu_screen = None
    $ store.text_history_enabled = False
    $ mouse_visible = False
    window hide
    stop soundfx fadeout 10.0
    stop soundfx2 fadeout 10.0
    scene black
    with dissolve2
    show expression Text(_("{i}Пожалуйста, подожди меня.{/i}"), size=20, yalign=0.5, kerning=2, color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve4
    pause 1.0
    hide expression Text(_("{i}Please wait for me.{/i}"), size=20, yalign=0.5, kerning=2, color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve4
    show expression Text(_("{i}Подожди меня, Мая...{/i}"), size=20, yalign=0.5, kerning=2, color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve4
    pause 1.0
    hide expression Text(_("{i}Wait for me Mai . . .{/i}"), size=20, yalign=0.5, kerning=2, color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve4
    play music "music/after_all.ogg" noloop
    show expression Text(_("{i}. . . в том мирном месте, на которое мы все надеемся.{/i}"), size=20, yalign=0.5, kerning=2, color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve4
    pause 4.0
    hide expression Text(_("{i}. . . in that peaceful place we all hope for.{/i}"), size=20, yalign=0.5, kerning=2, color="#fff", xalign=0.5, text_xalign=0.5, drop_shadow=(2, 2)) as text
    with dissolve4
    pause 1.0
    
    scene black
    
    scene credits
    with dissolve4
    show creditscroll
    with dissolve
    $ renpy.pause(0.02, hard=True)
    $ renpy.pause(237.0, hard=True)
    stop music fadeout 5.0
    scene black
    with dissolve4
    $ mouse_visible = True
    $ store.text_history_enabled = True
    $ _rollback = True
    $ renpy.pause(2.0, hard=True)
    scene bg1
    scene bg2
    scene bg3
    scene bg4
    scene bg5
    scene bg6
    scene bg7
    scene bg8
    scene bg9
    scene bg10
    scene bg11
    scene bg12
    scene bg13
    scene bg14
    scene concept1
    scene concept2
    scene concept3
    scene concept4
    scene concept5
    scene concept6
    scene concept7
    scene concept8
    scene black
    return
