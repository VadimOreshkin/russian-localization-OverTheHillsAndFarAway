#
#
#
#
##############################################################################
# Say
##############################################################################
screen say(who, what, side_image=None, two_window=True):
    if not two_window:
        window:
            id "window"
            has vbox:
                style "say_vbox"
            if who:
                text who id "who"
            text what id "what"
    else:
        vbox:
            style "say_two_window_vbox"
            if who:
                window:
                    style "say_who_window"
                    text who:
                        id "who"
                        xalign 0.5
            window:
                id "window"
                has vbox:
                    style "say_vbox"
                text what id "what"
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0
    #use quick_back
    use quick_menu


##############################################################################
# Choice
##############################################################################
screen choice(items):
    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5
        vbox:
            style "menu"
            spacing 2
            for caption, action, chosen in items:
                if action:
                    button:
                        action action
                        style "menu_choice_button"
                        text caption style "menu_choice"
                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True
    style menu_window is default
    style menu_choice is button_text:
        clear
    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)

##############################################################################
# Input
##############################################################################
screen input(prompt):
    window style "input_window":
        has vbox
        text prompt style "input_prompt"
        input id "input" style "input_text"
    use quick_menu

##############################################################################
# Nvl
##############################################################################
screen nvl(dialogue, items=None):
    window:
        style "nvl_window"
        has vbox:
            style "nvl_vbox"
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id
                has hbox:
                    spacing 10
                if who is not None:
                    text who id who_id
                text what id what_id
        if items:
            vbox:
                id "menu"
                for caption, action, chosen in items:
                    if action:
                        button:
                            style "nvl_menu_choice_button"
                            action action
                            text caption style "nvl_menu_choice"
                    else:
                        text caption style "nvl_dialogue"
    add SideImage() xalign 0.0 yalign 1.0
    use quick_menu

##############################################################################
# Main Menu
##############################################################################
screen main_menu():
    tag menu
    add "menuback"
    vbox:
        add "gui/title.png"
        xalign 0.5
        yalign 0.08
    hbox:
        style_group "mainmenu"
        xalign 0.5
        yalign 0.92
        textbutton _("Н О В А Я   И Г Р А") action Start() at nav_eff
        textbutton _("З А Г Р У З И Т Ь") action ShowMenu("load") at nav_eff
        textbutton _("Н А С Т Р О Й К И") action ShowMenu("preferences") at nav_eff
        textbutton _("Б О Н У С") action If(renpy.get_screen("bonus"), [Show("bonus")], [Show("bonus"), Show("bonus1")]) at nav_eff
        textbutton _("С А Й Т") action OpenURL ("http://war-girl.com/") at nav_eff
        textbutton _("В Ы Й Т И") action Quit(confirm=True) at nav_eff
    on "show" action SetVariable("menu_show", True)
    on "hide" action SetVariable("menu_show", False)
    
init -2:
    style mm_button:
        size_group "mm"
    style mainmenu_button:
        background Frame("gui/frame.png", 24, 24)
        hover_background Frame("gui/frame2.png", 24, 24)
        selected_background Frame("gui/frame2.png", 24, 24)
        selected_hover_background Frame("gui/frame2.png", 24, 24)
        insensitive_background Frame("gui/frame4.png", 24, 24)
        xminimum 210
        xmargin 5
        ypadding 3
    style mainmenu_button_text:
        is default
        size 18
        idle_color "#8888"
        hover_color "#fff"
        selected_idle_color "#fff"
        selected_hover_color "#fff"
        kerning 1
        xalign 0.5
    style navmenu_button:
        background Frame("gui/frame.png", 24, 24)
        hover_background Frame("gui/frame2.png", 24, 24)
        selected_background Frame("gui/frame2.png", 24, 24)
        selected_hover_background Frame("gui/frame2.png", 24, 24)
        insensitive_background Frame("gui/frame4.png", 24, 24)
        xminimum 210
        xmargin 5
        ypadding 3
    style navmenu_button_text:
        is default
        size 18
        idle_color "#8888"
        hover_color "#fff"
        selected_idle_color "#fff"
        selected_hover_color "#fff"
        kerning 1
        xalign 0.5
    style bonusmenu_button:
        background Frame("gui/frame.png", 24, 24)
        hover_background Frame("gui/frame2.png", 24, 24)
        selected_background Frame("gui/frame2.png", 24, 24)
        selected_hover_background Frame("gui/frame2.png", 24, 24)
        insensitive_background Frame("gui/frame4.png", 24, 24)
        xminimum 300
        xmargin 5
        ypadding 3
    style bonusmenu_button_text:
        is default
        size 18
        idle_color "#8888"
        hover_color "#fff"
        selected_idle_color "#fff"
        selected_hover_color "#fff"
        kerning 1
        xalign 0.5
        
##############################################################################
# Navigation
##############################################################################
screen navigation():
    if main_menu:
        add "menuback"
    frame:
        style_group "yesno"
        xfill True
        yfill True
    frame:
        style_group "yesno"
        xfill True
        yfill True
    hbox:
        style_group "navmenu"
        xalign 0.5
        yalign 0.92
        if not main_menu:
            textbutton _("В Е Р Н У Т Ь С Я") action Return() at nav_eff
        else:
            textbutton _("В Е Р Н У Т Ь С Я") action Return(), [Hide("bonus"), Hide("bonus1"), Hide("bonus2"), Hide("bonus3"), Hide("menu2")], [Show("main_menu"), Hide("bonus1"), Hide("bonus2"), Hide("bonus3"), Hide("menu2")] at nav_eff
        if not main_menu:
            textbutton _("С О Х Р А Н И Т Ь") action ShowMenu("save"), [Hide("bonus"), Hide("bonus1"), Hide("bonus2"), Hide("bonus3"), Hide("menu2")], [Show("save"), Hide("bonus1"), Hide("bonus2"), Hide("bonus3"), Hide("menu2")] at nav_eff
        textbutton _("З А Г Р У З И Т Ь") action ShowMenu("load"), [Hide("bonus"), Hide("bonus1"), Hide("bonus2"), Hide("bonus3"), Hide("menu2")], [Show("load"), Hide("bonus1"), Hide("bonus2"), Hide("bonus3"), Hide("menu2")] at nav_eff
        textbutton _("Н А С Т Р О Й К И") action ShowMenu("preferences"), [Hide("bonus"), Hide("bonus1"), Hide("bonus2"), Hide("bonus3"), Hide("menu2")], [Show("preferences"), Hide("bonus1"), Hide("bonus2"), Hide("bonus3"), Hide("menu2")] at nav_eff
        if not main_menu:
            textbutton _("Г Л А В Н О Е  М Е Н Ю") action MainMenu() at nav_eff
        else:
            textbutton _("Б О Н У С") action If(renpy.get_screen("bonus"), [Show("bonus")], [Show("bonus"), Show("bonus1")]) at nav_eff
            textbutton _("С А Й Т") action OpenURL ("http://war-girl.com/") at nav_eff
        textbutton _("В Ы Й Т И") action Quit() at nav_eff
        
        #action If(renpy.get_screen("preferences"), [Hide("bonus"), Hide("bonus1"), Hide("bonus2"), Hide("bonus3"), Hide("menu2")], [Show("preferences"), Hide("bonus1"), Hide("bonus2"), Hide("bonus3"), Hide("menu2")]) at nav_eff

init -2:
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
##############################################################################
screen file_picker():
    frame:
        xmargin 60
        yalign 0.39
        style "file_picker_frame"
        has vbox
        hbox:
            xalign 0.5
            style_group "file_picker_nav"
            textbutton _("    А В Т О    ") at nav_eff:
                action FilePage("auto")
            textbutton _("   Б Ы С Т Р О Е   ") at nav_eff:
                action FilePage("quick")
            for i in range(1, 26):
                textbutton str(i) at nav_eff:
                    action FilePage(i)
        null height 30
        $ columns = 5
        $ rows = 2
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"
            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):
                # Each file slot is a button.
                button at file_eff:
                    action FileAction(i)
                    xfill True
                    bottom_padding -5
                    vbox:
                        xalign 0.5
                        yalign 0.5
                        null height 10
                        add FileScreenshot(i)
                        null height 5
                        # Показываем только время сохранения
                        $ file_time = FileTime(i, empty=_("Пустой Слот"))
                        # Если нужно, оставляем только часы и минуты
                        $ file_time = file_time[-5:] if file_time else _("Пустой Слот")
                        text "[file_time]" xalign 0.5 yalign 0.5

                        null height 5  # пространство снизу, чтобы текст не упирался в рамку

                        key "save_delete" action FileDelete(i)

screen save():
    tag menu
    use navigation
    use file_picker

screen load():
    tag menu
    use navigation
    use file_picker   

init -2:
    style file_picker_frame:
        background None
    style file_picker_nav_button:
        background Frame("gui/frame.png", 24, 24)
        hover_background Frame("gui/frame2.png", 24, 24)
        selected_background Frame("gui/frame2.png", 24, 24)
        selected_hover_background Frame("gui/frame2.png", 24, 24)
        insensitive_background Frame("gui/frame4.png", 24, 24)
        xminimum 40
        #xmaximum 120
        xmargin 4
        ypadding 2
        xpadding 1
    style file_picker_nav_button_text:
        idle_color "#8888"
        hover_color "#fff"
        selected_idle_color "#fff"
        selected_hover_color "#fff"
        insensitive_color "#4448"
        xalign 0.5
        size 18
        kerning 1
    style file_picker_button:
        #is large_button
        background Frame("gui/frame.png", 24, 24)
        hover_background Frame("gui/frame2.png", 24, 24)
        selected_background Frame("gui/frame2.png", 24, 24)
        selected_hover_background Frame("gui/frame2.png", 24, 24)
        insensitive_background Frame("gui/frame4.png", 24, 24)
        activate_sound "se/click.ogg"
        hover_sound "se/hover.ogg"
        xmargin 3
        ymargin 3
    style file_picker_text:
        idle_color "#8888"
        hover_color "#fff"
        selected_idle_color "#fff"
        selected_hover_color "#fff"
        insensitive_color "#4448"
        size 18
    
        #is large_button_text

##############################################################################
# Preferences
##############################################################################
screen preferences():
    tag menu
    use navigation
    grid 2 1:
        style_group "prefs"
        xfill True
        xsize 1200
        xalign 0.5
        yalign 0.4
        vbox:
            frame:
                style_group "pref"
                has vbox
                hbox:
                    xalign 0.5
                    label _("Экран")
                null height 10
                hbox:
                    xalign 0.5
                    textbutton _("О К Н О") action Preference("display", "window") at nav_eff
                    textbutton _("В О  В Е С Ь  Э К Р А Н") action Preference("display", "fullscreen") at nav_eff
            null height 23
            frame:
                style_group "pref"
                has vbox
                hbox:
                    xalign 0.5
                    label _("Пропуск")
                null height 10
                hbox:
                    xalign 0.5
                    textbutton _("П Р О Ч И Т А Н Н О Е") action Preference("skip", "seen") at nav_eff
                    textbutton _("В С Ё") action Preference("skip", "all") at nav_eff
            null height 23
            frame:
                style_group "pref"
                has vbox
                hbox:
                    xalign 0.5
                    label _("Скорость текста")
                null height 10
                hbox:
                    xalign 0.5
                    bar value Preference("text speed")
        vbox:
            frame:
                style_group "pref"
                has vbox
                hbox:
                    xalign 0.5
                    label _("Автопроигрывание")
                null height 10
                hbox:
                    xalign 0.5
                    bar value Preference("auto-forward time")
                    if config.has_voice:
                        textbutton _("Ждать голос") action Preference("wait for voice", "toggle")
            null height 28
            frame:
                style_group "pref"
                has vbox
                hbox:
                    xalign 0.5
                    label _("Музыка")
                null height 10
                hbox:
                    xalign 0.5
                    bar value Preference("music volume")
            null height 28
            frame:
                style_group "pref"
                has vbox
                hbox:
                    xalign 0.5
                    label _("Звуки")
                null height 10
                hbox:
                    xalign 0.5
                    bar value Preference("sound volume")
            if config.has_voice:
                null height 20
                frame:
                    style_group "pref"
                    has vbox
                    hbox:
                        xalign 0.5
                        label _("Голос")
                    null height 10
                    hbox:
                        xalign 0.5
                        bar value Preference("voice volume")
                        textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                        if config.sample_voice:
                            textbutton _("Test"):
                                action Play("voice", config.sample_voice)
                                style "soundtest_button"
init -2:
    style pref_frame:
        background None
        xfill False
        xmargin 5
        top_margin 5
        xpadding 10
        ypadding 20
    style pref_vbox:
        xfill True
        xalign 0.5
    style pref_button:
        background Frame("gui/frame.png", 24, 24)
        hover_background Frame("gui/frame2.png", 24, 24)
        selected_background Frame("gui/frame2.png", 24, 24)
        selected_hover_background Frame("gui/frame2.png", 24, 24)
        insensitive_background Frame("gui/frame4.png", 24, 24)
        xminimum 220
        xmargin 10
        ypadding 2
    style pref_button_text:        
        is default
        size 18
        idle_color "#8888"
        hover_color "#fff"
        selected_idle_color "#fff"
        selected_hover_color "#fff"
        insensitive_color "#4448"
        kerning 1
        xalign 0.5
    style pref_slider:
        xmaximum 400
        xalign 1.0
        hover_sound "se/hover.ogg"
        activate_sound "se/click.ogg"
    style soundtest_button:
        xalign 1.0

##############################################################################
# Yes/No Prompt
##############################################################################
screen yesno_prompt(message, yes_action, no_action):
    modal True
    frame:
        style_group "yesno"
        xfill True
        yfill True
        frame:
            style_group "yesnobox"
            xalign 0.5
            yalign 0.5
            xfill True
            yminimum 150
            has vbox:
                xalign .5
                yalign .5
                spacing 30

            # Переводим стандартные английские сообщения на русский
            $ msg = message
            if "Are you sure you want to quit?" in msg:
                $ msg = "Вы точно хотите выйти?"
            elif "Are you sure you want to return to the main menu?" in msg:
                $ msg = "Вы точно хотите вернуться в главное меню?"
            elif "unsaved progress" in msg and ("load" in msg.lower() or "return" in msg.lower()):
                $ msg = "Несохранённый прогресс будет потерян. Вы уверены, что хотите продолжить?"
            elif "Are you sure you want to overwrite your save?" in msg:
                $ msg = "Вы точно хотите перезаписать сохранение?"
            elif "this will lose unsaved progress." in msg:
                $ msg = "Несохранённый прогресс будет потерян."

            label _(msg):
                xalign 0.5
                    
            hbox:
                style_group "yesno"
                xalign 0.5
                spacing 40
                textbutton _("Д А") action yes_action at nav_eff
                textbutton _("Н Е Т") action no_action at nav_eff
    key "game_menu" action no_action

init -2:
    style yesno_frame:
        background "transparent"
    style yesnobox_frame:
        background "gui/yesnobox.png"
    style yesno_button:
        background Frame("gui/frame.png", 24, 24)
        hover_background Frame("gui/frame2.png", 24, 24)
        selected_background Frame("gui/frame2.png", 24, 24)
        selected_hover_background Frame("gui/frame2.png", 24, 24)
        insensitive_background Frame("gui/frame4.png", 24, 24)
        xminimum 210
        xmargin 10
        ypadding 3
    style yesno_button_text:
        is default
        size 18
        idle_color "#8888"
        hover_color "#fff"
        selected_idle_color "#fff"
        selected_hover_color "#fff"
        insensitive_color "#4448"
        kerning 1
        xalign 0.5
    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


##############################################################################
# Quick Menu
##############################################################################
screen quick_menu():
    add "gui/quickmenu_back.png"
    #imagebutton idle "gui/quickmenu_back.png" hover "gui/quickmenu_back.png" action NullAction hovered Show("quick_menu") unhovered Hide("quick_menu")
    hbox:
        style_group "quick"
        xalign 0.5
        yalign 0.04
        textbutton _("Ж У Р Н А Л") action ShowMenu('text_history') at quick_eff
        textbutton _("С О Х Р А Н И Т Ь") action ShowMenu('save') at quick_eff
        textbutton _("З А Г Р У З И Т Ь") action ShowMenu('load') at quick_eff
        textbutton _("Б. С О Х Р А Н Е Н И Е") action QuickSave() at quick_eff
        textbutton _("Б. З А Г Р У З К А") action QuickLoad() at quick_eff
        textbutton _("П Р О П У С К") action Skip() at quick_eff
        textbutton _("А В Т О") action Preference("auto-forward", "toggle") at quick_eff
        textbutton _("Н А С Т Р О Й К И") action ShowMenu('preferences') at quick_eff
    
        
init -2:
    style quick_button:
        is default
        background Frame("gui/frame.png", 24, 24)
        hover_background Frame("gui/frame2.png", 24, 24)
        selected_background Frame("gui/frame2.png", 24, 24)
        selected_hover_background Frame("gui/frame2.png", 24, 24)
        insensitive_background Frame("gui/frame.png", 24, 24)
        xminimum 160
        ypadding 3
        xpadding 15
        xmargin 5
        kerning 0
        activate_sound "se/click.ogg"
        hover_sound "se/hover.ogg"
        
    style quick_button_text:
        is default
        size 18
        idle_color "#8888"
        hover_color "#fff"
        selected_idle_color "#fff"
        selected_hover_color "#fff"
        insensitive_color "#4448"
        kerning 0
        xalign 0.5

    transform quick_eff:
        on idle:
            alpha 1.0
            ypos 0
        on insensitive:
            alpha 0.5
            ypos 0
        on selected_idle:
            alpha 0.5
            ypos 0
        on hover:
            alpha 1.0
            linear 0.2 ypos 0.1
        on selected_hover:
            alpha 1.0
            linear 0.2 ypos 0.1
    transform nav_eff:
        on idle:
            ypos 0
        on selected_idle:
            linear 0.2 ypos -0.1
        on hover:
            linear 0.2 ypos -0.1
        on selected_hover:
            linear 0.2 ypos -0.1
    transform file_eff:
        on idle:
            ypos 0
        on selected_idle:
            linear 0.2 ypos -0.01
        on hover:
            linear 0.2 ypos -0.01
        on selected_hover:
            linear 0.2 ypos -0.01
            
            
#CG Gallery
#Galleries:
init python:
    #list the CG gallery images here:
    gallery_cg_items = ["cg1", "cg2", "cg3", "cg4", "cg5", "cg6"]
    gallery_concept_items = ["concept1", "concept6", "concept2", "concept7", "concept3", "concept4", "concept5", "concept8"]
    gallery_bg_items = ["bg1", "bg2", "bg3", "bg4", "bg5", "bg14", "bg9"]
    #how many rows and columns in the gallery screens?
    gal_rows = 3
    gal_cols = 3
    #thumbnail size in pixels:
    thumbnail_x = 270
    thumbnail_y = 152
    gal_cells = gal_rows * gal_cols
    
    g_cg = Gallery()
    for gal_item in gallery_cg_items:
        g_cg.button(gal_item + " butt")
        g_cg.image(gal_item)
        g_cg.unlock(gal_item)
        if gal_item == "cg6":
            g_cg.image("cg6 2")
            g_cg.unlock("cg6 2")
    g_cg.transition = dissolve
    cg_page=0
    
    g_concept = Gallery()
    for gal_item in gallery_concept_items:
        g_concept.button(gal_item + " butt")
        g_concept.image(gal_item)
        g_concept.unlock(gal_item)
    g_concept.transition = dissolve
    concept_page=0
    
    g_bg = Gallery()
    for gal_item in gallery_bg_items:
        g_bg.button(gal_item + " butt")
        g_bg.image(gal_item)
        g_bg.unlock(gal_item)
        if gal_item == "bg1":
            g_bg.image("bg13")
            g_bg.unlock("bg13")
        if gal_item == "bg2":
            g_bg.image("bg11")
            g_bg.unlock("bg11")
            g_bg.image("bg10")
            g_bg.unlock("bg10")
        if gal_item == "bg3":
            g_bg.image("bg12")
            g_bg.unlock("bg12")
        if gal_item == "bg14":
            g_bg.image("bg7")
            g_bg.unlock("bg7")
            g_bg.image("bg8")
            g_bg.unlock("bg8")
            g_bg.image("bg6")
            g_bg.unlock("bg6")
    g_bg.transition = dissolve
    bg_page=0

init +1 python:
    #Here we create the thumbnails. We create a grayscale thumbnail image for BGs, but we use a special "locked" image for CGs to prevent spoilers.
    for gal_item in gallery_cg_items:
        renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y))
        
    for gal_item in gallery_concept_items:
        renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y))
        
    for gal_item in gallery_bg_items:
        renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y))
        
screen bonus():
    tag menu
    use navigation
    
    vbox:
        style_group "bonusmenu"
        xalign 0.9
        yalign 0.45
        vbox:
            textbutton "А Р Т  C G" action If(renpy.get_screen("bonus1"), [Show("bonus1")], [Show("bonus1"), Show("bonus1")]) focus_mask True at nav_eff
            null height 10
            textbutton "К О Н Ц Е П Т - А Р Т" action If(renpy.get_screen("bonus2"), [Show("bonus2")], [Show("bonus2"), Show("bonus2")]) focus_mask True at nav_eff
            null height 10
            textbutton "Ф О Н О В Ы Й  А Р Т" action If(renpy.get_screen("bonus3"), [Show("bonus3")], [Show("bonus3"), Show("bonus3")]) focus_mask True at nav_eff
    
screen bonus1():
    tag menu2
    frame background None xpos 10:
        grid gal_rows gal_cols:
            xpos 80
            ypos 100
            $ i = 0
            $ next_cg_page = cg_page + 1
            if next_cg_page > int(len(gallery_cg_items)/gal_cells):
                $ next_cg_page = 0
            for gal_item in gallery_cg_items:
                $ i += 1
                if i <= (cg_page+1)*gal_cells and i>cg_page*gal_cells:
                    add g_cg.make_button(gal_item + " butt", gal_item + " butt", im.Scale("gui/gallocked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=Image("gui/gallery_border.png", xalign=0.5, yalign=0.5), background=Frame("gui/frame.png",24,24), xpadding = 0, xmargin=3, ymargin=3)
            for j in range(i, (cg_page+1)*gal_cells): #we need this to fully fill the grid
                add "gui/galblank.png"

screen bonus2():
    tag menu2
    frame background None xpos 10:
        grid gal_rows gal_cols:
            xpos 80
            ypos 100
            $ i = 0
            $ next_concept_page = concept_page + 1
            if next_concept_page > int(len(gallery_concept_items)/gal_cells):
                $ next_concept_page = 0
            for gal_item in gallery_concept_items:
                $ i += 1
                if i <= (concept_page+1)*gal_cells and i>concept_page*gal_cells:
                    add g_concept.make_button(gal_item + " butt", gal_item + " butt", im.Scale("gui/gallocked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=Image("gui/gallery_border.png", xalign=0.5, yalign=0.5), background=Frame("gui/frame.png",24,24), xpadding = 0, xmargin=3, ymargin=3)
            for j in range(i, (concept_page+1)*gal_cells): #we need this to fully fill the grid
                add "gui/galblank.png"         
                
screen bonus3():
    tag menu2
    frame background None xpos 10:
        grid gal_rows gal_cols:
            xpos 80
            ypos 100
            $ i = 0
            $ next_bg_page = bg_page + 1
            if next_bg_page > int(len(gallery_bg_items)/gal_cells):
                $ next_bg_page = 0
            for gal_item in gallery_bg_items:
                $ i += 1
                if i <= (bg_page+1)*gal_cells and i>bg_page*gal_cells:
                    add g_bg.make_button(gal_item + " butt", gal_item + " butt", im.Scale("gui/gallocked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=Image("gui/gallery_border.png", xalign=0.5, yalign=0.5), background=Frame("gui/frame.png",24,24), xpadding = 0, xmargin=3, ymargin=3)
            for j in range(i, (bg_page+1)*gal_cells): #we need this to fully fill the grid
                add "gui/galblank.png"
                    
########################################################################################################################
#### TEXT HISTORY ######################################################################################################
########################################################################################################################
init 1 python:
    #style.vscrollbar.top_bar=Frame("gui/frame.png", 20,20)
    #style.vscrollbar.bottom_bar=Frame("gui/frame.png", 20,20)
    #style.vscrollbar.xmaximum = 30
    #style.vscrollbar.top_margin = 20
    style.vscrollbar.ymaximum = 630
    style.vscrollbar.thumb = "gui/thumb_idle.png"
    style.vscrollbar.hover_thumb = "gui/thumb_hover.png"
    style.vscrollbar.thumb_offset = 12
    style.vscrollbar.xpos=20
    #style.vscrollbar.yalign = 0.25
    
    
    
init -4 python:
    store.text_history_enabled = False    
    
init -3 python:
    style.readback_window.background = None
    style.readback_window.xmaximum = 1320
    style.readback_window.xminimum = 1320
    style.readback_window.align = (.5, .55)
    
    style.readback_frame.background = Frame("gui/frame.png", 24, 24)
    style.readback_frame.xpadding = 10
    style.readback_frame.ypadding = 10
    #style.readback_frame.top_margin = 20
    style.readback_frame.bottom_margin = 80
    #style.readback_frame.left_padding = 1
    #style.readback_frame.right_padding = -600
    #style.readback_frame.top_padding = 95
    #style.readback_frame.bottom_padding = 92
    #style.readback_frame.xanchor = 0.5
    #style.readback_frame.yanchor = 0.07
    
    style.ruby_style = Style(style.default)
    style.ruby_style.size = 12
    style.ruby_style.yoffset = 22
    style.default.ruby_style = style.ruby_style
    
    style.readback_button.background = Frame("gui/frame.png", 24, 24)
    style.readback_button.hover_background = Frame("gui/frame2.png", 24, 24)
    style.readback_button.xminimum = 210
    style.readback_button.xmaximum = 210
    style.readback_button.ypadding = 3
    style.readback_button.xmargin = 10
    style.readback_button.hover_sound = "se/hover.ogg"
    style.readback_button_text.size = 18
    style.readback_text.color = "#fff"
    style.readback_text.ruby_style = style.ruby_style
    style.readback_text.line_leading = 30
    style.readback_text.size = 18
    style.readback_text.xalign = 0.0
    style.readback_label_text.size = 22
    style.readback_label_text.bold = True
    
    style.readback2_frame.background = "transparent"
    
    # starts adding new config variables
    config.locked = False 
    
    # Configuration Variable for Text History 
    config.readback_buffer_length = 100 # number of lines stored
    config.readback_full = True # True = completely replaces rollback, False = readback accessible from game menu only (dev mode)
    config.readback_disallowed_tags = ["size"] # a list of tags that will be removed in the text history
    config.readback_choice_prefix = ">> "   # this is prefixed to the choices the user makes in readback
    
    # ends adding new config variables
    config.locked = True
    
    ShawneeList = {
                " М А Я ": 20,
                " Д Е В О Ч К А ": 20,
                }

    NonShawneeList = {
                None: -15,
                "Д Ж Е К С О Н": -15,
                "О Б Р И": -15,
                "М А Я": -15,
                "Д Е В О Ч К А": -15,
                "К А П И Т А Н": -15,
                "Д Э Н И Э Л С": -15,
                "М А К Т А В И Ш": -15,
                "Р А З В Е Д Ч И К": -15,
                }

    NameList = {
                None: "gui/none_th.png",
                "Д Ж Е К С О Н": "gui/jackson_th.png",
                "О Б Р И": "gui/aubrey_th.png",
                "М А Я": "gui/mai_th.png",
                "Д Е В О Ч К А": "gui/mai_th.png",
                " М А Я ": "gui/mai_th.png",
                " Д Е В О Ч К А ": "gui/mai_th.png",
                "К А П И Т А Н": "gui/nobody_th.png",
                "Д Э Н И Э Л С": "gui/nobody_th.png",
                "М А К Т А В И Ш": "gui/nobody_th.png",
                "Р А З В Е Д Ч И К": "gui/nobody_th.png",
                }

    def HistoryImage(name = None):
        if name in NameList:
            return NameList[name]
        else:
            return Null()
            
    def StyleChoice(name = None):
        if name in ShawneeList:
            return ShawneeList[name]
        else:
            return NonShawneeList[name]
        
            
init -2 python:

    # Two custom characters that store what they said
    class ReadbackADVCharacter(ADVCharacter):
        def do_done(self, who, what):
            store_say(who, what)
            store.current_voice = ''
            return

    class ReadbackNVLCharacter(NVLCharacter):
        def do_done(self, who, what):
            store_say(who, what)
            store.current_voice = ''
            return
            
    # this enables us to show the current line in readback without having to bother the buffer with raw shows
    def say_wrapper(who, what, **kwargs):
        store_current_line(who, what)
        return renpy.show_display_say(who, what, **kwargs)
    
    config.nvl_show_display_say = say_wrapper
    
    adv = ReadbackADVCharacter(show_function=say_wrapper)
    nvl = ReadbackNVLCharacter()
    NVLCharacter = ReadbackNVLCharacter
    
    # rewriting voice function to replay voice files when you clicked dialogues in text history screen
    def voice(file, **kwargs):
        if not config.has_voice:
            return
        
        _voice.play = file
        
        store.current_voice = file

    # overwriting standard menu handler
    # Overwriting menu functions makes Text History log choice which users choose.
    def menu(items, **add_input): 
        
        newitems = []
        for label, val in items:
            if val == None:
                narrator(label, interact=False)
            else:
                newitems.append((label, val))
                
        rv = renpy.display_menu(newitems, **add_input)
        
        # logging menu choice label.
        for label, val in items:
            if rv == val:
                store.current_voice = ''
                store_say(None, config.readback_choice_prefix + label)
        return rv
        
    def nvl_screen_dialogue(): 
        """
         Returns widget_properties and dialogue for the current NVL
         mode screen.
         """

        widget_properties = { }
        dialogue = [ ]
        
        for i, entry in enumerate(nvl_list):
            if not entry:
                continue

            who, what, kwargs = entry

            if i == len(nvl_list) - 1:
                who_id = "who"
                what_id = "what"
                window_id = "window"

            else:
                who_id = "who%d" % i
                what_id = "what%d" % i
                window_id = "window%d" % i
                
            widget_properties[who_id] = kwargs["who_args"]
            widget_properties[what_id] = kwargs["what_args"]
            widget_properties[window_id] = kwargs["window_args"]

            dialogue.append((who, what, who_id, what_id, window_id))
        
        return widget_properties, dialogue
        
    # Overwriting nvl menu function
    def nvl_menu(items):

        renpy.mode('nvl_menu')
        
        if nvl_list is None:
            store.nvl_list = [ ]

        screen = None
        
        if renpy.has_screen("nvl_choice"):
            screen = "nvl_choice"
        elif renpy.has_screen("nvl"):
            screen = "nvl"
            
        if screen is not None:

            widget_properties, dialogue = nvl_screen_dialogue()        

            rv = renpy.display_menu(
                items,
                widget_properties=widget_properties,
                screen=screen,
                scope={ "dialogue" : dialogue },
                window_style=style.nvl_menu_window,
                choice_style=style.nvl_menu_choice,
                choice_chosen_style=style.nvl_menu_choice_chosen,
                choice_button_style=style.nvl_menu_choice_button,
                choice_chosen_button_style=style.nvl_menu_choice_chosen_button,
                type="nvl",                      
                )
                
            for label, val in items:
                if rv == val:
                    store.current_voice = ''
                    store_say(None, config.readback_choice_prefix + label)
            return rv
            
        # Traditional version.
        ui.layer("transient")
        ui.clear()
        ui.close()

        ui.window(style=__s(style.nvl_window))
        ui.vbox(style=__s(style.nvl_vbox))
        for i in nvl_list:
            if not i:
                continue

            who, what, kw = i            
            rv = renpy.show_display_say(who, what, **kw)
        renpy.display_menu(items, interact=False,
                           window_style=__s(style.nvl_menu_window),
                           choice_style=__s(style.nvl_menu_choice),
                           choice_chosen_style=__s(style.nvl_menu_choice_chosen),
                           choice_button_style=__s(style.nvl_menu_choice_button),
                           choice_chosen_button_style=__s(style.nvl_menu_choice_chosen_button),
                           )
        ui.close()
        roll_forward = renpy.roll_forward_info()
        rv = ui.interact(roll_forward=roll_forward)
        renpy.checkpoint(rv)
        for label, val in items:
            if rv == val:
                store.current_voice = ''
                store_say(None, config.readback_choice_prefix + label)
        return rv
        
    ## readback
    readback_buffer = []
    current_line = None
    current_voice = None
    def side_image(prefix_tag="side"):
        """
        :doc: side_image_function

        Returns the side image associated with the currently speaking character,
        or a Null displayable if no such side image exists.
        """

        name = renpy.get_side_image(prefix_tag, image_tag=config.side_image_tag, not_showing=config.side_image_only_not_showing)
        if name is None:
            return Null()
        else:
            return ImageReference(name)
            
    def store_say(who, what):
        global readback_buffer, current_voice
        if preparse_say_for_store(what):
            new_line = (preparse_say_for_store(who), preparse_say_for_store(what), current_voice)
            readback_buffer = readback_buffer + [new_line]
            readback_prune()
    def store_current_line(who, what):
        global current_line, current_voice
        current_line = (preparse_say_for_store(who), preparse_say_for_store(what), current_voice)
    # remove text tags from dialogue lines 
    disallowed_tags_regexp = ""
    for tag in config.readback_disallowed_tags:
        if disallowed_tags_regexp != "":
            disallowed_tags_regexp += "|"
        disallowed_tags_regexp += "{"+tag+"=.*?}|{"+tag+"}|{/"+tag+"}"
    import re
    remove_tags_expr = re.compile(disallowed_tags_regexp) # remove tags undesirable in readback
    def preparse_say_for_store(input):
        global remove_tags_expr
        if input:
            return re.sub(remove_tags_expr, "", input)
    def readback_prune():
        global readback_buffer
        while len(readback_buffer) > config.readback_buffer_length:
            del readback_buffer[0]
    # keymap overriding to show text_history.
    def readback_catcher():
        ui.add(renpy.Keymap(rollback=If(store.text_history_enabled,[ SetVariable("yvalue", 1.0), ShowMenu("text_history")])))
        ui.add(renpy.Keymap(rollforward=ui.returns(None)))
    if config.readback_full:
        config.rollback_enabled = False
        config.overlay_functions.append(readback_catcher) 
    
init python:
    yvalue = 1.0
    class NewAdj(renpy.display.behavior.Adjustment):
        def change(self,value):
            if value > self._range and self._value == self._range:
                return Return()
            else:
                return renpy.display.behavior.Adjustment.change(self, value)         
    def store_yvalue(y):
        global yvalue
        yvalue = int(y)
        
        
screen text_history:
    tag menu
    add "transparent"
    if not current_line and len(readback_buffer) == 0:
        $ lines_to_show = []
    elif current_line and len(readback_buffer) == 0:
        $ lines_to_show = [current_line]
    elif current_line and not ( ( len(readback_buffer) == 3 and current_line == readback_buffer[-2]) or current_line == readback_buffer[-1]):  
        $ lines_to_show = readback_buffer + [current_line]
    else:
        $ lines_to_show = readback_buffer
    $ adj = NewAdj(changed = store_yvalue, step = 300)
    window:
        style_group "readback"
        side "c r":
            frame:
                has viewport:
                    mousewheel True
                    draggable True
                    yinitial yvalue
                    yadjustment adj
                    side_spacing 200
                vbox:
                    for line in lines_to_show:
                        frame:
                            style_group "readback2"
                            right_padding 70
                            xminimum 1165
                            xmaximum 1165
                            yminimum 150
                            ymaximum 150
                            hbox:
                                style_group "readback"
                                vbox:
                                    frame:
                                        style_group "readback2"
                                        xpadding 10
                                        ypadding 10
                                        add HistoryImage( line[0] )
                                null width 40
                                vbox:
                                    xalign .5
                                    yalign .5
                                    if line[0] and line[0] != " ":
                                        vbox:
                                            label line[0] # name
                                            null height -5
                                    if line[1]:   
                                        # if there's no voice just log a dialogue
                                        if not line[2]:
                                            text line[1]:
                                                line_spacing StyleChoice( line[0] )
                                     # else, dialogue will be saved as a button of which plays voice when clicked
                                    else: 
                                        textbutton line[1] action Play("voice", line[2] )
                        null height -5
            bar adjustment adj style 'vscrollbar'
        textbutton _("Назад") action Return() align (0.5, 0.95)
        
                            
