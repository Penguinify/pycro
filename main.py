# 1.10 on the readability scale lmao
code = 0
import configparser
import console
import threading
from itertools import count
import pygame
from interpreter import loadinterpreterrequirments, pengumacode, finish
pygame.init()
run = True
import pygame_gui
from pygame_gui.windows.ui_file_dialog import UIFileDialog
from pygame_gui.elements.ui_button import UIButton
console.loadconsolerequirments()
loadinterpreterrequirments()
print('Import Installation Complete!')
print('Loading Pycro+ 1.0')

# credit to https://www.pygame.org/project-AAfilledRoundedRect-2349-.html

def AAfilledRoundedRect(surface,rect,color,radius=0.4):

    """
    AAfilledRoundedRect(surface,rect,color,radius=0.4)

    surface : destination
    rect    : rectangle
    color   : rgb or rgba
    radius  : 0 <= radius <= 1
    """

    rect         = pygame.Rect(rect)
    color        = pygame.Color(*color)
    alpha        = color.a
    color.a      = 0
    pos          = rect.topleft
    rect.topleft = 0,0
    rectangle    = pygame.Surface(rect.size,pygame.SRCALPHA)

    circle       = pygame.Surface([min(rect.size)*3]*2,pygame.SRCALPHA)
    pygame.draw.ellipse(circle,(0,0,0),circle.get_rect(),0)
    circle       = pygame.transform.smoothscale(circle,[int(min(rect.size)*radius)]*2)

    radius              = rectangle.blit(circle,(0,0))
    radius.bottomright  = rect.bottomright
    rectangle.blit(circle,radius)
    radius.topright     = rect.topright
    rectangle.blit(circle,radius)
    radius.bottomleft   = rect.bottomleft
    rectangle.blit(circle,radius)
    rectangle.fill((0,0,0),rect.inflate(-radius.w,0))
    rectangle.fill((0,0,0),rect.inflate(0,-radius.h))
    rectangle.fill(color,special_flags=pygame.BLEND_RGBA_MAX)
    rectangle.fill((255,255,255,alpha),special_flags=pygame.BLEND_RGBA_MIN)

    return surface.blit(rectangle,pos)


"""
# anti blocking code club
"""

def antiblockcode(item):
    pengumacode(item)


#Variables

class colors:
    white = (255,255,255)
    black = (0,0,10)
    bright_blue = (0,163,255)
    controlpanelgray = (170,170,170)
    vibrant_red = (255, 18, 18)
    whitchly_purple = (142, 0, 173)
    teal_taffe = (0, 255, 136)

class fonts:
    header96 = pygame.font.Font('assets/fonts/Comfortaa/static/Comfortaa-Medium.ttf',96)
    medium42 = pygame.font.Font('assets/fonts/Comfortaa/static/Comfortaa-Medium.ttf',42)
    syntax24 = pygame.font.Font('assets/fonts/RobotoMono-Italic.ttf',24)

class sprites:
    class selectwindowsize:
        class rectangles:
            top = pygame.Rect(41,35,558,125)
            mid = pygame.Rect(41,177,558,125)
            low = pygame.Rect(41,319,558,125)
        class text:
            top = fonts.header96.render('1920x1080',True,colors.black)
            mid = fonts.header96.render('1440x1024',True,colors.black)
    class editor:
        class polygons:
            start = pygame.Rect(375,35,37,45)
            stop = pygame.Rect(300,35,37,45)
            newfile = pygame.Rect(596,411,247,202)
            opensave = pygame.Rect(243,411,247,202)
            discopen = pygame.Rect(949,411,247,202)
            wiki = pygame.Rect(57,148,76,45)
            saveandexit = pygame.Rect(216,858,164,27)
            save = pygame.Rect(47,858,56,27)
            syntaxon = pygame.Rect(70,245,255,27)
        class images:
            background = pygame.image.load('assets/images/background.png')
            controlbackground = pygame.image.load('assets/images/controlbackground.png')
            start = pygame.image.load('assets/images/go.png')
            stop = pygame.image.load('assets/images/stop.png')
            homebackground = pygame.image.load('assets/images/homescreen.png')
            homelogo = pygame.image.load('assets/images/logo.png')
            controlelements = pygame.image.load('assets/images/control panel elements.png')
            iconify = pygame.image.load('assets/images/iconify.png')
        class text:
            syntaxhighlightingon = fonts.syntax24.render('Syntax Highlighting', True, colors.white)
            syntaxhighlightingoff = fonts.syntax24.render('Syntax Highlighting', True, colors.controlpanelgray)
            
class storage:
    keywords = ['delay','press','release','say','forever','repeat','end']
    texthelp = {'say':' display|anytext', 'delay':' length|float   [offset|float]', 'repeat':' length|int', 'press':' key/mb|bit.ly/acceptablekeys', 'release':' key/mb|bit.ly/acceptablekeys', 'forever':' what are you doing here?', 'end':'ends a repeat'}
    syntaxhighlighting = False
# pygame_gui
manager = pygame_gui.UIManager((1440, 1240),'pipassets/penguin.json')

#Support
#https://stackoverflow.com/questions/63801960/how-to-prompt-user-to-open-a-file-with-python3-pygame
def selectfile(directory = '/saves/'):
    global name
    file_selection = UIFileDialog(rect=pygame.Rect(0, 0, 700, 400), manager=manager, initial_file_path=directory,window_title='Open Save')
    while True:
        time_delta = pygame.time.Clock().tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                        
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == file_selection.ok_button:
                    name = file_selection.current_file_path
                    print(name)
                    return name
                if event.ui_element == file_selection.cancel_button:
                    return
                if event.ui_element == file_selection.close_window_button:
                    return
                    
            manager.process_events(event)

        manager.update(time_delta)
        window.blit(sprites.editor.images.homebackground, (0,0))
        manager.draw_ui(window)
        pygame.display.update()
        pygame.time.Clock().tick(30)

def selectwindowsize():
    global window
    global size
    window = pygame.display.set_mode((640,480))
    
    #draw
    
    window.fill(colors.bright_blue)
    
    pygame.draw.rect(window, colors.white, sprites.selectwindowsize.rectangles.top)
    pygame.draw.rect(window, colors.white, sprites.selectwindowsize.rectangles.mid)
    pygame.draw.rect(window, colors.white, sprites.selectwindowsize.rectangles.low)
    
    window.blit(sprites.selectwindowsize.text.top, (89,44))
    window.blit(sprites.selectwindowsize.text.mid, (79,188))
    
    pygame.display.update()
    
    #mainloop
    mainrun = True
    
    while mainrun == True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if sprites.selectwindowsize.rectangles.mid.collidepoint(event.pos):
                    size = [1440,1024]
                    window = pygame.display.set_mode((1440,1024))
                    pygame.display.set_caption('Pycro 0.6b')
                    pygame.display.set_icon(sprites.editor.images.iconify)
                    mainrun = False
                 
# HOMREE OIGJEIOTJEOIT

def home():
    run = True
    opacity = 255
    global name
    name = ''
    linerenderx = 0
    pipeline = fonts.medium42.render('|', True, colors.white)
    selectingname = False
    window.blit(sprites.editor.images.homebackground, (0,0))
    
    while run == True:
        #fadub
        window.blit(sprites.editor.images.homebackground, (0,0))
        fadein = pygame.Surface((1440,1024))
        fadein.set_alpha(opacity)
        fadein.fill((0,0,0))
        fadein.blit(sprites.editor.images.homelogo, (460,240))
        window.blit(fadein, (0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if sprites.editor.polygons.newfile.collidepoint(event.pos):
                    selectingname = True
                    
                elif sprites.editor.polygons.opensave.collidepoint(event.pos):
                    #openfile
                    try:
                        with open(selectfile('assets/saves/ '), 'r') as filereader:
                            global code
                            code = filereader.readlines()
                            counter = 0
                            code.pop(0)
                            for i in code:
                                if '\n' in i:
                                    code[counter] = i[:-1]
                                counter += 1
                            if code == []:
                                code = ['']
                            return
                    except:
                        pass
                
                elif sprites.editor.polygons.discopen.collidepoint(event.pos):
                    try:
                        with open(selectfile('/'), 'r') as filereader:
                            code = filereader.readlines()
                            counter = 0
                            code.pop(0)
                            for i in code:
                                if '\n' in i:
                                    code[counter] = i[:-1]
                                counter += 1
                            return
                    except:
                        pass
                
                
            #selectingname
            if event.type == pygame.KEYDOWN and selectingname == True:
                if len(str(pygame.key.name(event.key))) == 1 and len(name)<13:
                    if int(pygame.key.get_mods()) == 1:
                        name= name + str(pygame.key.name(event.key)).upper()
                    else:
                        name = name + str(pygame.key.name(event.key))
                        
                if str(pygame.key.name(event.key)) == "space":
                    name = name + ' '
                    
                if str(pygame.key.name(event.key)) == "backspace":
                    if len(name) > 0:
                        name = name[:-1]
                    else:
                        selectingname = False
                        linerenderx = 0
                        
                if str(pygame.key.name(event.key)) == "return":
                    try:
                        name = 'assets/saves/' + name + '.ppmc'
                        filecreation = open(name, 'x')
                        filecreation = open(name, 'a')
                        filecreation.write('pycroversion == 0.4D')
                        filecreation.close()
                        return
                    except:
                        print('Creation Failure!')

        if selectingname == True:    
            if linerenderx < 466.9:  
                AAfilledRoundedRect(window,(linerenderx,666,505,64),colors.bright_blue,1)
            else:
                AAfilledRoundedRect(window,(467,666,505,64),colors.bright_blue,1)
            text = fonts.medium42.render(name,True,colors.white)
            window.blit(text,(500,674))
            linerenderx = linerenderx + (linerenderx - (text.get_width() + 500))/-3
            window.blit(pipeline,(linerenderx,670))
        
        pygame.display.update()
        opacity -= 5
        pygame.time.Clock().tick(60)
         
def save(file,code):
    # save file
    filesave = open(file)
    print(code)
    code = ['pycroversion == 0.4D'] + code
    print(code)
    with open(name, 'r+') as filesave:
        filesave.truncate(0)
    with open(file, 'w') as filesave:
        for i in code:
            filesave.write(i + '\n')
    
    # config
    editor = config_obj['PENGU']
    
    editor['syntax'] = str(storage.syntaxhighlighting)
    
    with open('assets/other/user.ini', 'w') as configfile:
        config_obj.write(configfile)
    
    
#MAIN

# pygame_gui is my best friend 3-.__O›

def main():
    global run
    global code
    global config_obj
    
    pygame.key.set_repeat(300,50)
    
    code = ['']
    
    home()
    
    console.openconsolewindow(())
    
    #user config
    config_obj = configparser.ConfigParser()
    config_obj.read("assets/other/user.ini")
    storage.syntaxhighlighting = config_obj["PENGU"]['syntax']
    
    line = 0
    subline = 0
    foreverrenderh = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    linerenderx = 1920
    linerendery = 83
    
    pipeline = fonts.medium42.render('|', True, colors.white)
    
    #
    pygame.draw.rect(window,colors.controlpanelgray,sprites.editor.polygons.start)
    pygame.draw.rect(window,colors.controlpanelgray,sprites.editor.polygons.stop)
    
    # title
    titletext = str(name).split('/')
    
    counter = 0
    
    for i in titletext:
        if '.ppmc' in i:
            titletext = i[:-5]
        counter += 1
            
    titletext = fonts.medium42.render(titletext,True,colors.whitchly_purple)
    
    # main
    
    while run == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save(name,code)                
                run = False
                pygame.quit()
                quit('User Ended Process')
            
            # start
            if event.type == pygame.MOUSEBUTTONDOWN:
                if sprites.editor.polygons.start.collidepoint(event.pos):
                    save(name,code)
                    if not antiblocking.is_alive:
                        antiblocking = threading.Thread(target=antiblockcode,args=(code,))
                        antiblocking.start()
                elif sprites.editor.polygons.stop.collidepoint(event.pos):
                    finish()
                elif sprites.editor.polygons.wiki.collidepoint(event.pos):
                    pass #dothis shit later
                elif sprites.editor.polygons.save.collidepoint(event.pos):
                    save(name,code)
                elif sprites.editor.polygons.saveandexit.collidepoint(event.pos):
                    save(name,code)
                    return
                elif sprites.editor.polygons.syntaxon.collidepoint(event.pos):
                    storage.syntaxhighlighting = not storage.syntaxhighlighting
                
            
            if event.type == pygame.KEYDOWN:
                # text editor
                if not len(code[line]) > 41:
                    if len(str(pygame.key.name(event.key))) == 1:
                        subline += 1
                        if int(pygame.key.get_mods()) == 1:
                            code[line]= code[line][:subline - 1] + str(pygame.key.name(event.key)).upper() + code[line][subline - 1:]
                        else:
                            code[line] = code[line][:subline - 1] + str(pygame.key.name(event.key)) + code[line][subline - 1:]
                    if str(pygame.key.name(event.key)) == "space":
                        code[line] = code[line][:subline] + ' ' + code[line][subline:]
                        subline += 1

                if str(pygame.key.name(event.key)) == "backspace":
                    if len(code[line]) > 0 and subline > 0:
                        code[line] = code[line][:subline - 1] + code[line][subline:]
                        subline -= 1
                    elif line > 0:
                        code.pop(line)
                        line -= 1
                        subline = len(code[line])
                if str(pygame.key.name(event.key)) == "return":
                    code.insert(line + 1, '')
                    subline = 0
                    line += 1
                if event.key == pygame.K_LEFT and 0 < subline: subline -= 1     
                if event.key == pygame.K_RIGHT and len(code[line]) > subline: subline += 1
                if event.key == pygame.K_UP and line > 0:
                    line -= 1
                    if subline > len(code[line]):
                        subline = len(code[line])
                if event.key == pygame.K_DOWN and line < len(code) -1 : line += 1    
                
        #draw frame
        window.blit(sprites.editor.images.background,(0,0))
        window.blit(sprites.editor.images.controlbackground,(23,15))
        window.blit(sprites.editor.images.start,(375,35))
        window.blit(sprites.editor.images.stop,(300,35))
        window.blit(sprites.editor.images.controlelements,(64,128))
        #name
        window.blit(titletext,(500,34))
        
        #syntax HIGH lighting
        if storage.syntaxhighlighting == True:
            counter = 0
            linekeyword = []
            for space in code:
                space = space.split(' ')
                if not space[0] in storage.keywords:
                    invalidtext = fonts.medium42.render(' '.join(space),True,(colors.black))
                    AAfilledRoundedRect(window,(500, counter * 50 + 120,invalidtext.get_width(),6),colors.vibrant_red,1)
                if counter == line and space[0] in storage.keywords and len(space) > 1:
                    linekeyword = []
                    linekeyword.append(space[0])
                    linekeyword.append(counter)
                counter += 1
        
        #draw text
        counter = 0
        for i in code:
            temptext = fonts.medium42.render(i,True,colors.white)
            window.blit(temptext,(500,counter * 50 + 82))
            counter += 1
        try:
            counter = 0
            if len(code[line]) == subline:
                temptext = fonts.medium42.render(code[line],True,colors.black)
            else:
                temptext = fonts.medium42.render(code[line][:-1*(len(code[line])-subline)],True,colors.black)
        except:
            line = 0
        
        if storage.syntaxhighlighting == True: window.blit(sprites.editor.text.syntaxhighlightingon, (76,250))
        else: window.blit(sprites.editor.text.syntaxhighlightingoff,(76,250))
                
        richtext = code[line]
        
        #draw line/ other animations
        linerenderx = linerenderx + (linerenderx - (temptext.get_width() + 495))/-3
        linerendery = linerendery + (linerendery - (line * 50 + 78))/-3
        
        window.blit(pipeline,(linerenderx, linerendery))
        
        if storage.syntaxhighlighting == True:
            if not linekeyword == []:
                AAfilledRoundedRect(window,(linerenderx + 20,linerendery + 38,len(storage.texthelp[linekeyword[0]]) * 13 + 30,30), (0,0,0,140))
                window.blit(fonts.syntax24.render(storage.texthelp[linekeyword[0]],True,colors.white),(linerenderx + 15,linerendery + 35))
            counter = 0
            repeatcounter = 0
            for space in code:
                if space == 'forever':
                    foreverrenderh[0] = foreverrenderh[0] + (foreverrenderh[0] - len(code[counter:]) * 50)/-2
                    AAfilledRoundedRect(window,(470,counter * 50 + 90,6,foreverrenderh[0]),colors.bright_blue,1)
                space = space.split(' ')
                if space[0] == 'repeat':
                    ending = 0
                    end = 0
                    endnumber = -1
                    for i in code:
                        ending += 1
                        if not end == 0:
                            continue
                        if ending > counter:
                            i = i.split(' ')
                            if i[0] == 'end' and endnumber == 0:
                                end = ending
                            elif i[0] == 'repeat':
                                endnumber += 1
                            elif i[0] == 'end':
                                endnumber -= 1
                    if code[counter:end] == []:
                        foreverrenderh[repeatcounter + 1] = foreverrenderh[repeatcounter + 1] + (foreverrenderh[repeatcounter + 1] - len(code[counter:]) * 50)/-2
                        AAfilledRoundedRect(window,(485,counter * 50 + 90,6,foreverrenderh[repeatcounter + 1]),colors.whitchly_purple,1)
                    
                    else:
                        foreverrenderh[repeatcounter + 1] = foreverrenderh[repeatcounter + 1] + (foreverrenderh[repeatcounter + 1] - len(code[counter:end]) * 50)/-2
                        AAfilledRoundedRect(window,(485,counter * 50 + 90,6,foreverrenderh[repeatcounter + 1]),colors.whitchly_purple,1)
                
                counter += 1
        
        #update frame
        pygame.display.update()
        pygame.time.Clock().tick(30)
                


print('Pycro+ 1.0 Has been Loaded!')

if __name__ == "__main__":
    selectwindowsize()
    while True:
        main()
