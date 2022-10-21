

# this code is absolute garbage, dont look at it.


def loadinterpreterrequirments():
    global keyboard
    global mouse
    global left
    global right
    global middle
    global end
    import pynput
    keyboard = pynput.keyboard.Controller()
    mouse = pynput.mouse.Controller()
    left = pynput.mouse.Button.left
    right = pynput.mouse.Button.right
    middle = pynput.mouse.Button.middle
    end = 0
def pengumacode(code):
    global end
    end = False
    from time import sleep
    from random import randint
    import threading
    counter = 0
    foreverloop = []
    skiplines = []
    # interpreter
    for line in code:
        if end == True:
            return
        if line in skiplines:
            skiplines.pop(0)
            continue
        
        line = line.split(' ')
        print(line)
        
        if line[0] == 'say':
            line.pop(0)
            print(' '.join(line))
        
        elif line[0] == 'delay':
            try:
                try:
                    if line[2]:
                        line[1] = float(line[1])
                        line[2] = float(line[2])
                        line[1] = line[1] * 10
                        line[2] = line[2] * 10
                        line = randint(line[1],line[2])
                        sleep(line / 10)
                except:
                    sleep(float(line[1]))
            except:
                print('[Syntax Error] : Error #2 (invalid float/integer) Has occured at line {0}'.format(counter))
                return
        
        elif line[0] == 'press':
            try:
                if line[1] == 'left' or line[1] == 'right' or line[1] == 'middle':
                    if line[1] == 'left':
                        mouse.press(left)
                    if line[1] == 'right':
                        mouse.press(left)
                    if line[1] == 'middle':
                        mouse.press(left)
                else:
                    if line[1] == 'shift':
                        keyboard.press(keyboard._Key.shift)
                    else:
                        keyboard.press(line[1])
            except:
                print('[Syntax Error] : Error #1 (invalid character or string) Has occured at line {0}. For list of accepted formats please use the accepted formats here ui.formats/link'.format(counter))
        
        elif line[0] == 'release':
            try:
                if line[1] == 'left' or line[1] == 'right' or line[1] == 'middle':
                    if line[1] == 'left':
                        mouse.release(left)
                    if line[1] == 'right':
                        mouse.release(left)
                    if line[1] == 'middle':
                        mouse.release(left)
                else:
                    if line[1] == 'shift':
                        keyboard.release(keyboard._Key.shift)
                    else:
                        keyboard.release(line[1])
                    
            except:
                print('[Syntax Error] : Error #1 (invalid character) Has occured at line {0}'.format(counter))
        
        elif line[0] == 'forever':
            foreverloop = code[counter:]
            print(foreverloop)
        
        
        # under here is the shadow realm... The unforgivable cess pool of coding
        
        
        
        # dont look here, i made this at 1 am 
        # i had a mental breakdown over repeats
        
        elif line[0] == 'repeat':
            end = 0
            ending = 0
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
                print(i)
                print(counter)
                print(endnumber)
                print(ending)
                        
                print(end)
            repeatloop = code[counter + 1:end]
            
            print(f"{repeatloop} is what your ballin for")
            
            repeatcounter = [0]
            saveline = line
            skiplines = repeatloop
            while repeatcounter[0] < int(saveline[1]):
                for line in repeatloop:
                    line = line.split(' ')
                    if line[0] == 'say':
                        line.pop(0)
                        print(' '.join(line))
            
                    elif line[0] == 'delay':
                        try:
                            try:
                                if line[2]:
                                    line[1] = float(line[1])
                                    line[2] = float(line[2])
                                    line[1] = line[1] * 10
                                    line[2] = line[2] * 10
                                    line = randint(line[1],line[2])
                                    sleep(line / 10)
                            except:
                                sleep(float(line[1]))
                        except:
                            print('[Syntax Error] : Error #2 (invalid float/integer) Has occured at line {0}'.format(counter))
                            return
                    
                    elif line[0] == 'press':
                        try:
                            if line[1] == 'left' or line[1] == 'right' or line[1] == 'middle':
                                if line[1] == 'left':
                                    mouse.press(left)
                                if line[1] == 'right':
                                    mouse.press(left)
                                if line[1] == 'middle':
                                    mouse.press(left)
                            else:
                                if line[1] == 'shift':
                                    keyboard.press(keyboard._Key.shift)
                                else:
                                    keyboard.press(line[1])
                        except:
                            print('[Syntax Error] : Error #1 (invalid character or string) Has occured at line {0}. For list of accepted formats please use the accepted formats here ui.formats/link'.format(counter))
                    
                    elif line[0] == 'release':
                        try:
                            if line[1] == 'left' or line[1] == 'right' or line[1] == 'middle':
                                if line[1] == 'left':
                                    mouse.release(left)
                                if line[1] == 'right':
                                    mouse.release(left)
                                if line[1] == 'middle':
                                    mouse.release(left)
                            else:
                                if line[1] == 'shift':
                                    keyboard.release(keyboard._Key.shift)
                                else:
                                    keyboard.release(line[1])
                        except:
                            print('[Syntax Error] : Error #1 (invalid character or string) Has occured at line {0}. For list of accepted formats please use the accepted formats here ui.formats/link'.format(counter))
                    
                    elif line[0] == 'end':
                        #ignore that stuff
                        pass
                    
                    else:
                        print('[Syntax Error] : Error #1 (invalid keyword) Has occured at line {0}'.format(counter))
                repeatcounter[0] += 1
                    
        
        
        # end of repeat stuff.... I know, I know, this code is very optimised but I forgot when I asked.
        
        
        
        elif line[0] == 'end':
            #ignore that stuff
            pass
        else:
            print('[Syntax Error] : Error #1 (invalid keyword) Has occured at line {0}'.format(counter))
        
        if not foreverloop == []:
            while True:
                if end == True:
                    return
                counter = 0
                for line in foreverloop:
                    if line in skiplines:
                        skiplines.pop(0)
                        continue
                    
                    line = line.split(' ')
                    print(line)
                    if line[0] == 'say':
                        line.pop(0)
                        print(' '.join(line))
                    
                    elif line[0] == 'delay':
                        try:
                            try:
                                if line[2]:
                                    line[1] = float(line[1])
                                    line[2] = float(line[2])
                                    line[1] = line[1] * 10
                                    line[2] = line[2] * 10
                                    line = randint(line[1],line[2])
                                    sleep(line / 10)
                            except:
                                sleep(float(line[1]))
                        except:
                            print('[Syntax Error] : Error #2 (invalid float/integer) Has occured at line {0}'.format(counter))
                            return
                    
                    elif line[0] == 'press':
                        try:
                            if line[1] == 'left' or line[1] == 'right' or line[1] == 'middle':
                                if line[1] == 'left':
                                    mouse.press(left)
                                if line[1] == 'right':
                                    mouse.press(left)
                                if line[1] == 'middle':
                                    mouse.press(left)
                            else:
                                if line[0] == 'shift':
                                    keyboard.press(keyboard._Key.shift)
                                else:
                                    keyboard.press(line[1])
                        except:
                            print('[Syntax Error] : Error #1 (invalid character or string) Has occured at line {0}. For list of accepted formats please use the accepted formats here ui.formats/link'.format(counter))
                    
                    elif line[0] == 'repeat':
                        end = 0
                        ending = 0
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
                        repeatloop = code[counter + 1:end]
                        
                        print(f"{repeatloop} is what your ballin for")
                        
                        repeatcounter = [0]
                        saveline = line
                        skiplines = repeatloop
                        while repeatcounter[0] < int(saveline[1]):
                            for line in repeatloop:
                                line = line.split(' ')
                                if line[0] == 'say':
                                    line.pop(0)
                                    print(' '.join(line))
                        
                                elif line[0] == 'delay':
                                    try:
                                        try:
                                            if line[2]:
                                                line[1] = float(line[1])
                                                line[2] = float(line[2])
                                                line[1] = line[1] * 10
                                                line[2] = line[2] * 10
                                                line = randint(line[1],line[2])
                                                sleep(line / 10)
                                        except:
                                            sleep(float(line[1]))
                                    except:
                                        print('[Syntax Error] : Error #2 (invalid float/integer) Has occured at line {0}'.format(counter))
                                        return
                                
                                elif line[0] == 'press':
                                    try:
                                        if line[1] == 'left' or line[1] == 'right' or line[1] == 'middle':
                                            if line[1] == 'left':
                                                mouse.press(left)
                                            if line[1] == 'right':
                                                mouse.press(left)
                                            if line[1] == 'middle':
                                                mouse.press(left)
                                        else:
                                            if line[1] == 'shift':
                                                keyboard.press(keyboard._Key.shift)
                                            else:
                                                keyboard.press(line[1])
                                    except:
                                        print('[Syntax Error] : Error #1 (invalid character or string) Has occured at line {0}. For list of accepted formats please use the accepted formats here ui.formats/link'.format(counter))
                                
                                elif line[0] == 'release':
                                    try:
                                        if line[1] == 'left' or line[1] == 'right' or line[1] == 'middle':
                                            if line[1] == 'left':
                                                mouse.release(left)
                                            if line[1] == 'right':
                                                mouse.release(left)
                                            if line[1] == 'middle':
                                                mouse.release(left)
                                        else:
                                            if line[1] == 'shift':
                                                keyboard.release(keyboard._Key.shift)
                                            else:
                                                keyboard.release(line[1])
                                    except:
                                        print('[Syntax Error] : Error #1 (invalid character or string) Has occured at line {0}. For list of accepted formats please use the accepted formats here ui.formats/link'.format(counter))
                                
                                elif line[0] == 'end':
                                    #ignore that stuff
                                    pass
                                
                                else:
                                    print('[Syntax Error] : Error #1 (invalid keyword) Has occured at line {0}'.format(counter))
                            repeatcounter[0] += 1
                    
                    
                    elif line[0] == 'release':
                        try:
                            if line[1] == 'left' or line[1] == 'right' or line[1] == 'middle':
                                if line[1] == 'left':
                                    mouse.release(left)
                                if line[1] == 'right':
                                    mouse.release(left)
                                if line[1] == 'middle':
                                    mouse.release(left)
                            else:
                                if line[1] == 'shift':
                                    keyboard.release(keyboard._Key.shift) 
                                else:
                                    keyboard.release(line[1])
                        except:
                            print('[Syntax Error] : Error #1 (invalid character) Has occured at line {0}'.format(counter))
                    
                    elif line[0] == 'forever':
                        foreverloop = code[counter:]
                        print(foreverloop)
                    else:
                        print('[Syntax Error] : Error #1 (invalid keyword) Has occured at line {0}'.format(counter))
                    counter += 1

def finish():
    global end
    end = True
             