__author__ = 'eguoshi'

# The Adventure of Tom!
# A 2D platformer, your goal is to reach the end of the
# level by overcoming numerous obstacles in your way
# through a combination of skills, items, and wit.
# See 'How to Play' for more information, or just watch this video:
# http://www.youtube.com/watch?v=pCrzDWdvKq8&feature=g-crec-u

import simplegui
import math
import random
from time import time

hex = [str(n) for n in range(10)] + [chr(n) for n in range(ord('A'),ord('G'))]

def color(r,g,b):
    return '#'+hex[r//16]+hex[r%16]+hex[g//16]+hex[g%16]+hex[b//16]+hex[b%16]

#directory = "http://commondatastorage.googleapis.com/codeskulptor-demos/adventTom_assets/"
directory = "assets/"

def load_image(name):
    return simplegui.load_image(directory + name)

def load_sound(name):
    return simplegui.load_sound(directory + name)

ready = False

# The player character, Tom
class Tom():
    IMAGE_SIZE = (100,100)
    SIZE = (100,100)
    IMAGE = load_image("Tom.png")
    GUN = load_image("Pellet_Gun.png")
    TERMINAL = [3,10]

    FIRE_SOUND = load_sound("pistol-01.wav") # http://www.mediacollege.com/downloads/sound-effects/weapons/pistol-01.wav
    THRUSTER_SOUND = load_sound("thrust2.mp3") # http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3
    JUMP_SOUND = load_sound("step.mp3") # http://www.freesound.org/people/CGEffex/sounds/89769/
    JUMP_SOUND.set_volume(0.1)
    STEP_SOUND = load_sound("step.mp3") # http://www.freesound.org/people/CGEffex/sounds/89769/
    STEP_SOUND.set_volume(0.03)
    STEP_SOUND_SNOW = load_sound("step.mp3") # http://www.freesound.org/people/CGEffex/sounds/89769/
    STEP_SOUND_SNOW.set_volume(0.01)
    HIT_SOUND = load_sound("hit.wav") # http://www.mediacollege.com/downloads/sound-effects/hit/
    SLIDE_SOUND = load_sound("friction.mp3") # http://www.freesound.org/people/RutgerMuller/sounds/51153/ Rutger Muller
    FLAME_SOUND = load_sound("fire.mp3") # http://www.freesound.org/people/nthompson/sounds/47252/

    def __init__(self, pos):
        self.pos = pos
        self.frame = 0
        self.left = False
        self.right = False
        self.up = False
        self.jump = False
        self.vel = [0,0]
        self.delta = [0,0]
        self.ground = '  '
        self.gun = 0
        self.gun_max = 0
        self.arm = None
        self.pellets = []
        self.jetpack = 0
        self.jetpack_max = 0
        self.jetpack_jump = 0
        self.jetpack_jump_max = 0
        self.propel = False
        self.max_health = 500
        self.health = 500
        self.hit = 0
        self.heal = 0

        self.wall = 0

        self.direction = 0

        self.jump_keys = (32,87)
        self.jet_keys = (32,87)
        self.disable = True

    def draw(self, canvas):
        if self.propel:
            Tom.THRUSTER_SOUND.play()
        else:
            Tom.THRUSTER_SOUND.pause()
        Tom.SLIDE_SOUND.rewind()
        if self.hit % 10 < 5 and self.health > 0:
            if self.jetpack > 0:
                flip = self.wall and self.vel[1] > 0 and self.ground == '  '
                canvas.draw_image(Item.JETPACK_IMAGE, (25,25+50*int(self.propel)), (50,50), (self.pos[0] - camera.pos[0] + int(flip) * self.wall * -5,self.pos[1]-50-camera.pos[1]), (50,50),(0 if self.direction == 0 else (.2 if self.direction > 0 else -.2))*(-1 if flip else 1))
            if self.ground == '  ' and self.wall and self.vel[1] > 0:
                canvas.draw_image(Tom.IMAGE, (Tom.IMAGE_SIZE[0] * 11.5, Tom.IMAGE_SIZE[1] * (int(self.arm != None) + 2 * int(self.wall < 0) + 0.5)), Tom.IMAGE_SIZE, (self.pos[0]-camera.pos[0] - 10*self.wall,self.pos[1] - 36 - camera.pos[1]), Tom.SIZE)
                Tom.SLIDE_SOUND.play()
            elif abs(self.direction) < 0.1:
                canvas.draw_image(Tom.IMAGE, (Tom.IMAGE_SIZE[0] * 0.5, Tom.IMAGE_SIZE[1] * (int(self.arm != None) + 0.5)), Tom.IMAGE_SIZE, (self.pos[0]-camera.pos[0],self.pos[1] - 40 - camera.pos[1]), Tom.SIZE)
            else:
                canvas.draw_image(Tom.IMAGE, (Tom.IMAGE_SIZE[0] * ((1 if self.direction > 0 else -1) * self.frame//5%10 + 1.5), Tom.IMAGE_SIZE[0] * (2 * int(self.direction < 0) + int(self.arm != None) + 0.5)), Tom.IMAGE_SIZE, (self.pos[0] - camera.pos[0],self.pos[1] - 40 - camera.pos[1]), Tom.SIZE)
            if self.arm != None:
                canvas.draw_image(Tom.GUN, (250,(50 if -math.pi/2 < self.arm < math.pi/2 else 150)), (500,100), self.shoulder(), (100,20), self.arm)
            for p in self.pellets:
                canvas.draw_image(Item.PELLET_IMAGE, (3,3), (6,6), camera.adjust(p.pos), (6,6))

    def update(self):
        f = True
        accel = [0,Physics.GRAVITY]
        cell = [p//50 for p in self.boundingbox()]
        if self.hit:
            self.hit -= 1
            if self.heal:
                self.heal -= 1
            else:
                self.health -= 1
                if self.health <= 0:
                    self.health = 0
                    self.hit = 0
                    self.heal = 0
                    return False
        elif self.heal:
            self.heal -= 1
            self.health += 1
            if self.health >= self.max_health:
                self.health = self.max_health
        on_ground = Physics.DENSITY[self.ground[0]] > 0 or Physics.DENSITY[self.ground[1]] > 0
        pos = (self.pos[0],self.pos[1])
        if on_ground or (self.frame//1 != 14 and self.frame//1 != 14+25):
            self.frame += 1
            if on_ground and self.direction != 0 and self.frame%25 == 1:
                self.STEP_SOUND.rewind()
                self.STEP_SOUND_SNOW.rewind()
                if 'S' in self.ground:
                    self.STEP_SOUND_SNOW.play()
                else:
                    self.STEP_SOUND.play()
            self.frame %= 50
        self.propel = False
        if self.jump:
            if on_ground:
                Tom.JUMP_SOUND.rewind()
                Tom.JUMP_SOUND.play()
                accel[1] += (-5.25 - abs(self.delta[0])*0.3) * (0.7 if level.value(level.pos(self.core())) == 'S' else 1)
                self.up = False
            elif self.wall and (self.left if self.wall < 0 else self.right):
                Tom.JUMP_SOUND.rewind()
                Tom.JUMP_SOUND.play()
                accel[1] -= self.vel[1]/2 + 3.5
                accel[0] += 3 * -self.wall
                if self.wall  < 0:
                    if self.disable:
                        self.left = False
                    self.direction = 1
                else:
                    if self.disable:
                        self.right = False
                    self.direction = -1
                self.wall = 0
                f = False
                self.up = False
            self.jump = False
        if self.up and self.jetpack > 0 and self.jetpack_jump < self.jetpack_jump_max:
                accel[1] -= .2
                self.jetpack -= (1 + max(-self.vel[1],0))
                self.jetpack_jump += (1 + max(-self.vel[1],0))
                self.propel = True
        dir_old = self.direction
        if self.left and not self.right:
            self.direction -= 0.5
            if self.direction < -1:
                self.direction = -1
            accel[0] += (self.direction + dir_old)/2 * (.3)
        elif self.right and not self.left:
            self.direction += 0.5
            if self.direction > 1:
                self.direction = 1
            accel[0] += (self.direction + dir_old)/2 * (.3)
        elif on_ground:
            if abs(self.direction) < 0.25:
                self.direction = 0
            elif self.direction < 0:
                self.direction += 0.25
            else:
                self.direction -= 0.25
            if abs(self.vel[0]) < 0.1:
                accel[0] = -self.vel[0]
            elif self.vel[0] < 0:
                accel[0] += 0.1
            else:
                accel[0] -= 0.1
        if f:
            f = Physics.FRICTION[self.ground[0]] + Physics.FRICTION[self.ground[1]]
            accel[0] *= f
        if self.wall and self.vel[1] + accel[1] > 0:
            accel[1] *= 0.7
        self.vel[0] += accel[0] / 2
        self.pos[0] += self.vel[0]
        cell_new = [int(p//50) for p in self.boundingbox()]
        self.wall = 0
        if cell[0] != cell_new[0] or cell[1] != cell_new[1]:
            box = self.boundingbox()
            side = box[0] if self.vel[0] < 0 else box[1]
            hits = [level.pos((side,k)) for k in (box[3],(box[3]+box[2])/2,box[2])]
            collide = False
            for h in hits:
                if Physics.DENSITY[level.value(h)] > 0.5:
                    collide = True
                    break
            if collide:
                if Physics.DENSITY[level.value((cell[0],cell[3]+1))] == 0:
                    self.wall = 1 if self.vel[0] > 0 else -1
                if self.vel[0] > 0:
                    self.pos[X] = self.pos[X] - side%50 - .000000001
                else:
                    self.pos[X] = self.pos[X] + (-side)%50 + .000000001
                if not self.left and not self.right:
                    self.vel[X] = 0
                else:
                    self.vel[X] /= 100
            else:
                for h in hits:
                    c = level.value(h)
                    if c in '.gj+BO':
                        level.items[h].activate(self)
                        if c != 'B':
                            level[h[1]][h[0]] = ' '

                self.wall = 0
        self.vel[0] += accel[0] / 2
        terminal = Tom.TERMINAL[0] / 3 if level.value(level.pos(self.core())) == 'S' else Tom.TERMINAL[0]
        if self.vel[0] > terminal:
            self.vel[0] = terminal
        elif self.vel[0] < -terminal:
            self.vel[0] = -terminal

        self.vel[1] += accel[1] / 2
        if self.vel[1] < 0:
            self.ground = '  '
        self.pos[1] += self.vel[1]
        cell_new = [int(p//50) for p in self.boundingbox()]
        if cell[2] != cell_new[2] or cell[3] != cell_new[3]:
            up = self.vel[1] > 0
            box = self.boundingbox()
            side = box[2] if self.vel[1] < 0 else box[3]
            hits = [level.pos((k,side)) for k in box[0:2]]
            collide = False
            for h in hits:
                if Physics.DENSITY[level.value(h)] > 0.5 or level.value(h) in 'S-' and self.vel[1] > 0:
                    collide = True
                    if level.value(h) == 'N' and self.vel[1] > 0 and h not in level.fragile.keys():
                        level.fragile[h] = 100
                if level.value(h) == '!':
                    self.hit = 200
                    self.vel[0] = self.vel[1] = self.delta[0] = self.delta[1] = accel[0] = accel[1] = 0
                    point = 0
                    while point < len(level.checkpoints) - 1 and level.checkpoints[point+1][0] < self.pos[0]:
                        point += 1
                    checkpoint = level.checkpoints[point]
                    camera.pan(checkpoint,self.hit)
                    self.pos[0] = checkpoint[0]
                    self.pos[1] = checkpoint[1]
                    self.left = self.right = self.up = False
                    frame.set_mousedrag_handler(nothing)
                    frame.set_mouseclick_handler(nothing)
                    frame.set_keydown_handler(nothing)
                    Tom.HIT_SOUND.rewind()
                    Tom.HIT_SOUND.play()
                    break

            if up:
                self.ground = level.value(hits[0]) + level.value(hits[1])
            if collide:
                snow = Physics.DENSITY[self.ground[0]] + Physics.DENSITY[self.ground[1]] < 0.25
                if abs(self.vel[1]) > 1:
                    if snow:
                        Tom.STEP_SOUND_SNOW.rewind()
                        Tom.STEP_SOUND_SNOW.play()
                    else:
                        Tom.JUMP_SOUND.rewind()
                        Tom.JUMP_SOUND.play()
                if self.vel[1] < 0:
                    self.pos[1] = self.pos[1] + (-side)%50 + .000000001
                elif not snow:
                    self.pos[1] = self.pos[1] - side%50 - .000000001
                self.vel[1] = 0
            else:
                for h in hits:
                    c = level.value(h)
                    if c in '.gj+BO':
                        level.items[h].activate(self)
                        if c != 'B':
                            level[h[1]][h[0]] = ' '
        if self.hit == 0:
            for k in range(cell_new[0], cell_new[1]+1, 1):
                for j in range(cell_new[2], cell_new[3]+1, 1):
                    if level[j][k] == '^':
                        self.hit = 100
                        Tom.HIT_SOUND.rewind()
                        Tom.HIT_SOUND.play()
                        break
                if self.hit > 0:
                    break
        self.vel[Y] += accel[1] / 2
        self.vel[1] *= 0.995

        self.delta[0] = self.pos[0]-pos[0]
        self.delta[1] = self.pos[1]-pos[1]


        if on_ground and self.jetpack_jump > 0:
            self.jetpack_jump = max(self.jetpack_jump - 5, 0)

        self.pos[X] %= len(level[0])*50

        for p in self.pellets:
            if not p.update():
                self.pellets.remove(p)

        if self.hit == 0:
            for e in on_screen_enemies:
                if intersect_boxes(self.boundingbox(),e.boundingbox()):
                    self.hit = e.attack
                    Tom.HIT_SOUND.rewind()
                    Tom.HIT_SOUND.play()
                    break

        if level.lavaspeed and self.pos[1] > level.lava:
            self.health = 0
            self.FLAME_SOUND.rewind()
            self.FLAME_SOUND.play()
        return True

    def reset(self, pos):
        self.pos[0] = pos[0]
        self.pos[1] = pos[1]
        self.frame = 0
        self.left = False
        self.right = False
        self.up = False
        self.vel = [0,0]
        self.delta = [0,0]
        self.ground = '  '
        self.gun = 0
        self.gun_max = 0
        self.arm = None
        self.pellets = []
        self.jetpack = 0
        self.jetpack_max = 0
        self.jetpack_jump = 0
        self.jetpack_jump_max = 0
        self.propel = False
        self.max_health = 500
        self.health = 500
        self.hit = 0
        self.heal = 0
        self.fell = False

        self.wall = 0

        self.direction = 0

    def keydown(self,key):
        if key == simplegui.KEY_MAP['a']:
            self.left = True
        elif key == simplegui.KEY_MAP['d']:
            self.right = True
        else:
            if key in self.jet_keys:
                self.up = True
            if key in self.jump_keys:
                self.jump = True


    def keyup(self,key):
        if key == simplegui.KEY_MAP['a']:
            self.left = False
        elif key == simplegui.KEY_MAP['d']:
            self.right = False
        else:
            if key in self.jet_keys:
                self.up = False
            if key in self.jump_keys:
                self.jump = False

    def set_jump(self, keys):
        self.jump_keys = keys

    def set_jet(self, keys):
        self.jet_keys = keys

    def set_disable(self, d):
        self.disable = d

    def mouseclick(self, pos):
        if not self.gun:
            return
        s = self.shoulder()
        self.arm = math.atan2(pos[1] - s[1],pos[0] - s[0])
        power = 400
        self.pellets.append(Pellet([s[0]+camera.pos[0]+45*math.cos(self.arm-(.15 if -math.pi/2 < self.arm < math.pi/2 else -.15)),s[1]+camera.pos[1]+45*math.sin(self.arm-(.15 if -math.pi/2 < self.arm < math.pi/2 else -.15))],[power*math.cos(self.arm)/40 + self.delta[0],power*math.sin(self.arm)/40 + self.delta[1]]))
        self.gun -= 1
        Tom.FIRE_SOUND.rewind()
        Tom.FIRE_SOUND.play()
        if self.gun == 0:
            self.arm = None

    def mousedrag(self, pos):
        if not self.gun:
            return
        s = self.shoulder()
        self.arm = math.atan2(pos[1] - s[1],pos[0] - s[0])

    def boundingbox(self):
        h = self.height()
        w = self.width()
        return (self.pos[0] - w/2, self.pos[0] + w/2, self.pos[1] - h, self.pos[1] - 1);

    def height(self):
        if self.direction == 0:
            return 81
        else:
            return 77

    def width(self):
        return 42

    def core(self):
        return (self.pos[X], self.pos[Y] - self.height()/2)

    def standing_feet(self):
        return ((self.pos[X]-17,self.pos[Y]),(self.pos[X]+17,self.pos[Y]))

    def shoulder(self):
        if self.direction == 0:
            return (self.pos[0] - 5 - camera.pos[0],self.pos[1] - 63 - camera.pos[1])
        disp = (10 if self.direction<0 else -10) if self.wall and self.vel[1] > 0 and self.ground == '  ' else (-3 if self.direction<0 else 3)
        return (self.pos[0] + disp - camera.pos[0],self.pos[1] - 60 - camera.pos[1])

# Buttons for use with the Menus, activate actions upon clicks
class Button():

    def __init__(self, image, size, pos, trigger, attr = None, active = True):
        self.image = load_image(image)
        self.pos = pos
        self.size = size
        self.trigger = trigger
        self.attr = attr
        self.active = active
        self.group = ()

    def draw(self, canvas):
        canvas.draw_image(self.image, (self.size[0]/2, self.size[1] * (1-int(self.active)+0.5)), self.size, self.pos, self.size)

    def contains(self, pos):
        return pos[0] > self.pos[0] - self.size[0]/2 and pos[0] < self.pos[0] + self.size[0]/2 and pos[1] > self.pos[1] - self.size[1]/2 and pos[1] < self.pos[1] + self.size[1]/2

    def set_group(self,g):
        self.group = g

    def activate(self):
        self.active = True
        for b in self.group:
            b.active = False
        if self.attr is None:
            self.trigger()
        else:
            self.trigger(self.attr)

tom = Tom([0,0])


# Menu navigation, uses buttons
class Menu():

    player_name = ""
    name_input = False

    def draw_menu(canvas):
        canvas.draw_image(Menu.MENU_SCREEN, (400,300), (800,600), (400,300), (800,600))
        for b in Menu.buttons:
            b.draw(canvas)
        if not Menu.buttons:
            canvas.draw_text("Loading"+'.'*(time()*10)//4,(200,300),20,"black")

    def draw_title(canvas):
        global frame_count
        frame_count += 1
        if frame_count % 25 == 1:
            Tom.STEP_SOUND.rewind()
            Tom.STEP_SOUND.play()
        Menu.draw_menu(canvas)
        canvas.draw_image(Tom.IMAGE, (Tom.IMAGE_SIZE[0] * (frame_count//5%10 + 1.5), Tom.IMAGE_SIZE[0] * 0.5), Tom.IMAGE_SIZE, (400,320), Tom.SIZE)
        if ready:
            canvas.draw_text("Click to start!",(320,250),20,"black")
        else:
            canvas.draw_text("Loading"+"."*(frame_count//20%4),(320,250),20,"black")

    def draw_high_scores(canvas):
        Menu.draw_menu(canvas)
        canvas.draw_image(Menu.LEVEL_BUTTONS[Menu.level_num].image, (Menu.LEVEL_THUMBNAIL_SIZE[0]/2,Menu.LEVEL_THUMBNAIL_SIZE[1]/2), Menu.LEVEL_THUMBNAIL_SIZE, (400,100), Menu.LEVEL_THUMBNAIL_SIZE)
        count = 0
        for score in levels[Menu.level_num].high_scores:
            canvas.draw_text(str(count+1)+". ", (300,200+50*count),15, "black")
            canvas.draw_text(str(score[0]), (350,200+50*count),15,"black")
            canvas.draw_text(score[2].replace('\n',''), (425, 200+50*count),15,"black")
            count += 1

    def draw_how_to_play(canvas):
        Menu.draw_menu(canvas)
        canvas.draw_image(Menu.HOW_TO_PLAY_DISPLAY, (400, 300), (800,600), (400,300), (800,600))

    def draw_credits(canvas):
        Menu.draw_menu(canvas)
        canvas.draw_image(Menu.CREDITS_DISPLAY, (400,300), (800,600), (400,300), (800,600))

    def click_menu(pos):
        for b in Menu.buttons:
            if b.contains(pos):
                b.activate()
                return

    def enter_main_menu():
        frame.set_draw_handler(Menu.draw_menu)
        Menu.buttons = (Menu.PLAY_GAME, Menu.HOW_TO_PLAY, Menu.CREDITS, Menu.HIGH_SCORES)

    def enter_level_selection_menu():
        frame.set_draw_handler(Menu.draw_menu)
        Menu.play = True
        Menu.buttons = Menu.LEVEL_BUTTONS

    def enter_options_menu():
        pass

    def enter_high_scores_menu():
        frame.set_draw_handler(Menu.draw_menu)
        Menu.play = False
        Menu.buttons = Menu.LEVEL_BUTTONS

    def enter_credits():
        frame.set_draw_handler(Menu.draw_credits)
        Menu.play = False
        Menu.buttons = (Menu.BACK_TO_MAIN_MENU,)

    def enter_how_to_play():
        frame.set_draw_handler(Menu.draw_how_to_play)
        Menu.play = False
        Menu.buttons = Menu.OPTION_BUTTONS

    def select_level(num):
        Menu.level_num = num
        if Menu.play:
            Menu.buttons = ()
            global frame_count, level, score, disp_score
            frame_count = 0
            level = Level(levels[num])
            score = 0
            disp_score = 0
            timer.start()
            tom.reset(level.tom_start)
            frame.set_draw_handler(draw_midgame)
            frame.set_keydown_handler(tom.keydown)
            frame.set_keyup_handler(tom.keyup)
            frame.set_mouseclick_handler(tom.mouseclick)
            frame.set_mousedrag_handler(tom.mousedrag)
        else:
            Menu.buttons = [Menu.BACK_TO_HIGH_SCORES]
            frame.set_draw_handler(Menu.draw_high_scores)

    def level_complete(arg):
        high_scores = levels[Menu.level_num].high_scores
        high_scores.append((score, -time(), str(Menu.player_name)))
        Menu.player_name = ""
        high_scores.sort()
        high_scores.reverse()
        if len(high_scores) > 8:
            high_scores.pop(8)
        Menu.buttons = [Menu.BACK_TO_MAIN_MENU]
        frame.set_draw_handler(Menu.draw_high_scores)
        frame.set_mouseclick_handler(Menu.click_menu)

    def type_name(key):
        if key >= 0 and key < 256:
            if key == 8:
                if len(Menu.player_name) > 0:
                    Menu.player_name = Menu.player_name[0:-1]
            elif key == 13:
                Menu.player_name += '\n'
            elif len(Menu.player_name) < 10:
                Menu.player_name += chr(key)

    TITLE_SCREEN = Button("Title_Screen.png", (800,600), (400,300), enter_main_menu)

    MENU_SCREEN = load_image("Menu_Screen.png")

    PLAY_GAME = Button("PlayGame.png", (400,200), (400,200), enter_level_selection_menu)
    HIGH_SCORES = Button("HighScores.png", (150,150), (650,475), enter_high_scores_menu)
    HOW_TO_PLAY = Button("HowToPlay.png", (150,150), (150,475), enter_how_to_play)
    CREDITS = Button("Credits.png", (150,150), (400,475), enter_credits)

    JUMP_W = Button("W_Option.png", (14,18), (372,406), tom.set_jump, (87,), False)
    JUMP_SPACE = Button("Spacebar_Option.png", (84,22), (517,408), tom.set_jump, (32,), False)
    JUMP_EITHER = Button("Either_Option.png", (64,19), (667,405), tom.set_jump, (32,87), True)

    JUMP_W.set_group((JUMP_SPACE,JUMP_EITHER))
    JUMP_SPACE.set_group((JUMP_W, JUMP_EITHER))
    JUMP_EITHER.set_group((JUMP_W, JUMP_SPACE))

    JET_W = Button("W_Option.png", (14,18), (372,446), tom.set_jet, (87,), False)
    JET_SPACE = Button("Spacebar_Option.png", (84,22), (517,448), tom.set_jet, (32,), False)
    JET_EITHER = Button("Either_Option.png", (64,19), (667,445), tom.set_jet, (32,87), True)

    JET_W.set_group((JET_SPACE,JET_EITHER))
    JET_SPACE.set_group((JET_W, JET_EITHER))
    JET_EITHER.set_group((JET_W, JET_SPACE))

    DISABLE_YES = Button("Yes_Option.png", (34,18), (549,566), tom.set_disable, True, True)
    DISABLE_NO = Button("No_Option.png", (24,18), (637,566), tom.set_disable, False, False)

    DISABLE_YES.set_group((DISABLE_NO,))
    DISABLE_NO.set_group((DISABLE_YES,))

    BACK_TO_MAIN_MENU = Button("Back.png", (50,50), (25, 575), enter_main_menu)
    BACK_TO_HIGH_SCORES = Button("Back.png", (50,50), (25, 575), enter_high_scores_menu)

    HOW_TO_PLAY_DISPLAY = load_image("How to Play.png")
    CREDITS_DISPLAY = load_image("Credits Display.png")

    OPTION_BUTTONS = (JUMP_W,JUMP_SPACE, JUMP_EITHER, JET_W, JET_SPACE, JET_EITHER, DISABLE_YES, DISABLE_NO, BACK_TO_MAIN_MENU)

    buttons = [TITLE_SCREEN]

    LEVEL_ARRAY = (2,2)
    LEVEL_THUMBNAIL_SIZE = (160, 120)
    LEVEL_THUMBNAIL_DISP = (800/(LEVEL_ARRAY[0]+1),600/(LEVEL_ARRAY[1]+1))

    LEVEL_BUTTONS = []

    play = False
    level_num = -1

    count = 0
    for x in range(LEVEL_ARRAY[0]):
        for y in range(LEVEL_ARRAY[1]):
            LEVEL_BUTTONS.append(Button("Level"+str(count+1)+"Thumbnail.png", LEVEL_THUMBNAIL_SIZE, (LEVEL_THUMBNAIL_DISP[0]*(x+1), LEVEL_THUMBNAIL_DISP[1]*(y+1)), select_level, count))
            count += 1

    LEVEL_BUTTONS.append(BACK_TO_MAIN_MENU)



def dist(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

def norm(p1,p2):
    return (p1[0]-p2[0])**2+(p1[1]-p2[1])**2

def intersect_boxes(b1, b2): # (left, right, top, bottom)
    return b1[0] <= b2[1] and b1[1] >= b2[0] and b1[2] <= b2[3] and b1[3] >= b2[2]

def box_to_polygon(b):
    return ((b[0],b[2]),(b[0],b[3]),(b[1],b[3]),(b[1],b[2]))

X = 0
Y = 1

score = 0
disp_score = 0

# Information used to generate a new play of a level

class LevelInfo():


    def __init__(self, num, grid, attr, high_scores = []):
        self.num = num
        self.image = load_image("Level"+str(num+1)+".png")
        self.grid = grid
        self.attr = attr
        self.high_scores = list(high_scores)

# Rendered game level
class Level():

    TILE_IMAGE = load_image("Tiles.png")
    tile_keys = 'gj+BbOZ'

    tiles = dict()
    k = 0
    for t in tile_keys:
        tiles[t] = [25 + 50 * k, 25]
        k += 1

    snow_tile = (25,125)

    TICK_SOUND = load_sound("tick.mp3") # http://www.freesound.org/people/KorgMS2000B/sounds/54405/
    COMPLETE_SOUND = load_sound("complete.mp3") # http://www.freesound.org/people/sagetyrtle/sounds/32260/

    def __init__(self, level_info):

        self.level_info = level_info
        self.grid = list(level_info.grid)
        for k in range(len(self.grid)):
            self.grid[k] = list(self.grid[k])
        empty = ' '*len(self.grid[0])
        for k in range(12):
            self.grid.insert(0,list(empty))
        for k in range(2):
            self.grid.append(list(self.grid[-1]))
        for k in range(len(self.grid)):
            self.grid[k] = list(self.grid[k])

        self.items = dict()

        self.enemies = set()

        self.checkpoints = list()

        count = dict()
        for k in level_info.attr.keys():
            count[k] = 0


        def next_attr(c):
            attr = level_info.attr[c][count[c]]
            count[c] += 1
            return attr

        for k in range(len(self.grid[0])):
            for j in range(len(self.grid)):
                if self.grid[j][k] == 't':
                    self.tom_start = [k*50+25,(j+1)*50]
                    self.checkpoints.append(self.tom_start)
                    self.grid[j][k] = ' '
                if self.grid[j][k] == 'Y':
                    self.grid[j][k] = 'X'
                elif self.grid[j][k] == 'r':
                    self.checkpoints.append([k*50+25,(j+1)*50])
                    self.grid[j][k] = ' '
                elif self.grid[j][k] == 'm':
                    self.enemies.add(Mook([k*50+25,(j)*50+25]))
                    self.grid[j][k] = ' '
                elif self.grid[j][k] == 'f':
                    self.enemies.add(Frog([k*50+25,j*50], next_attr('f')))
                    self.grid[j][k] = ' '
                elif self.grid[j][k] == 'g':
                    self.items[(k,j)] = (Item(Item.obtain_gun, next_attr('g')))
                elif self.grid[j][k] == 'j':
                    self.items[(k,j)] = (Item(Item.obtain_jetpack, next_attr('j')))
                elif self.grid[j][k] == '+':
                    self.items[(k,j)] = (Item(Item.heal, next_attr('+')))
                elif self.grid[j][k] == '.':
                    self.items[(k,j)] = Item(Item.collect, None)
                elif self.grid[j][k] == 'O':
                    self.items[(k,j)] = (Item(Item.play, next_attr('O')))
                elif self.grid[j][k] == 'B':
                    self.items[(k,j)] = Item(Item.blue, next_attr('B'))
                    self.blue_button = ((k,j), self.items[(k,j)].attr)
                elif self.grid[j][k] == 'K':
                    self.grid[j][k] = ' '
                elif self.grid[j][k] in '^v<>':
                    self.grid[j][k] = '^'
        self.fragile = dict()

        self.blue = 0

        if 'L' in level_info.attr.keys():
            self.lavaspeed = level_info.attr['L']
            self.lava = len(self.grid)*50
        else:
            self.lavaspeed = 0

        if 'W' in level_info.attr.keys():
            self.wrap = level_info.attr['W']
        else:
            self.wrap = False

    def update(self):
        for k in self.fragile.keys():
            self.fragile[k] -= 1
            if self.fragile[k] == 0:
                del self.fragile[k]
                self.grid[k[1]][k[0]] = ' '
        if self.blue:
            self.blue -= 1
            if self.blue < 200:
                if self.blue == 0:
                    Level.tiles['b'][1] = 25
                    Level.tiles['B'][1] = 25
                    Physics.FRICTION['b'] = Physics.FRICTION[' ']
                    Physics.DENSITY['b'] = 0
                elif self.blue % 10 == 0:
                    Level.TICK_SOUND.rewind()
                    Level.TICK_SOUND.play()
                    if self.blue % 20 == 0:
                        Level.tiles['b'][1] = 25
                    else:
                        Level.tiles['b'][1] = 75
            elif self.blue % 20 == 0:
                self.TICK_SOUND.rewind()
                self.TICK_SOUND.play()
        if self.lavaspeed:
            self.lava -= self.lavaspeed

    def __getitem__(self, p):
        return self.grid[p]

    def __len__(self):
        return len(self.grid)


    def draw(self, canvas):
        canvas.draw_image(self.level_info.image,(400 + camera.pos[X],300 + camera.pos[Y]),(800,600),(400,300),(800,600))
        if camera.pos[Y] >= 0:
            x_major = camera.pos[0] // 50
            x_minor = camera.pos[0]%50-25
            y_major = camera.pos[1] // 50
            y_minor = camera.pos[1]%50-25
            for k in range(16 if x_minor == -25 else 17):
                for j in range(12 if y_minor == 25 else 13):
                    char = self[j+y_major][k+x_major]
                    if char in ' X':
                        continue
                    elif char == '.':
                        canvas.draw_image(Level.TILE_IMAGE, (25 + 50 * (frame_count//10 % 20), 175), (50,50), (k*50-x_minor,j*50-y_minor), (50,50))
                    elif char in Level.tile_keys:
                        canvas.draw_image(Level.TILE_IMAGE, Level.tiles[char], (50,50), (k*50-x_minor,j*50-y_minor),(50,50))
                    elif char == 'N':
                        x = k+x_major
                        y = j+y_major
                        if (x,y) in self.fragile.keys():
                            canvas.draw_image(Level.TILE_IMAGE, (25 + (128-self.fragile[(x,y)])//6 * 50, 225), (50,50), (k*50 - x_minor,j*50 - y_minor), (50,50))
                        else:
                            canvas.draw_image(Level.TILE_IMAGE,(25,225),(50,50),(k*50-x_minor,j*50-y_minor),(50,50))
        else:
            hue = max(255+camera.pos[Y]//64,25)
            frame.set_canvas_background(color(0,hue,hue))

    def draw_over_snow(self, canvas):
        if camera.pos[Y] >= 0:
            cells = [int(p//50) for p in tom.boundingbox()]
            x_major = int(camera.pos[0] // 50)
            x_minor = int(camera.pos[0]%50-25)
            y_major = int(camera.pos[1] // 50)
            y_minor = int(camera.pos[1]%50-25)
            for k in range(max(0,cells[0]-1),min(len(self.grid[0]),cells[1]+2)):
                for j in range(max(0,cells[2]-1),min(len(self.grid),cells[3]+2)):
                    char = self[j][k]
                    if char in 'SX':
                        canvas.draw_image(Level.TILE_IMAGE,Level.snow_tile,(50,50),(k*50-x_major*50-x_minor,j*50-y_major*50-y_minor),(50,50))
        else:
            hue = max(255+camera.pos[Y]//64,25)
            frame.set_canvas_background(color(0,hue,hue))

    def draw_over_lava(self, canvas):
        lava_line = self.lava - camera.pos[1]
        if lava_line < 600:
            canvas.draw_polygon(((0,lava_line),(800,lava_line),(800,600),(0,600)),1,"#E00000","#E00000")

    def value(self,p):
        if p[0] < 0 or p[0] >= len(self[0]):
            if self.wrap:
                if p[1] >= 0 and p[1] < len(self.grid):
                    return self[p[1]][p[0]%800]
            else:
                return 'X'
        if p[1] < 0:
            return ' '
        if p[1] >= len(self.grid):
            return '!'
        return self[p[1]][p[0]]#return grid[p[1]//1%len(grid)][p[0]//1%len(grid[0])]

    def pos(self,p):
        return (p[0]//50,p[1]//50)

# Keeps track of the camera position, usually follows Tom
class Camera():

    def __init__(self, track):
        self.pos = [0,0]
        self.track = track
        self.approach = None
        self.length = 0
        self.progress = 0

    def update(self):
        if self.approach:
            self.progress += 1
            d = 1/self.length
            self.pos[0] += self.approach[0] * d
            self.pos[1] += self.approach[1] * d
            if self.progress == self.length:
                self.approach = None
                self.length = 0
                self.progress = 0
                frame.set_keydown_handler(tom.keydown)
                frame.set_mousedrag_handler(tom.mousedrag)
                frame.set_mouseclick_handler(tom.mouseclick)
        else:
            if self.track[X] > self.pos[X] + 500:
                self.pos[X] = int(self.track[X]) - 500
            if self.track[X] < self.pos[X] + 300:
                self.pos[X] = int(self.track[X]) - 300
            if self.track[Y] > self.pos[Y] + 400:
                self.pos[Y] = int(self.track[Y]) - 400
            if self.track[Y] < self.pos[Y] + 200:
                self.pos[Y] = int(self.track[Y]) - 200
        if self.pos[X] < 0:
            self.pos[X] = 0
        if self.pos[X] > len(level[0])*50-800:
            self.pos[X] = len(level[0])*50-800
#        if self.pos[Y] < 0:
#            self.pos[Y] = 0
        if self.pos[Y] > len(level.grid)*50-700:
            self.pos[Y] = len(level.grid)*50-700

    def adjust(self,pos):
        return (pos[0]-self.pos[0],pos[1]-self.pos[1])

    def deadjust(self,pos):
        return (pos[0]+self.pos[0],pos[1]+self.pos[1])

    def pan(self,p2,t):
        p2 = [p2[0] - 400, p2[1] - 300]
        if p2[X] < 50:
            p2[X] = 50
        if p2[X] > len(level[0])*50-850:
            p2[X] = len(level[0])*50-850
#        if p2[Y] < 50:
#            p2[Y] = 50
        if p2[Y] > len(level.grid)*50-750:
            p2[Y] = len(level.grid)*50-750
        self.approach = (p2[0]-self.pos[0],p2[1]-self.pos[1])
        self.length = t

    def __getitem__(self,key):
        return self.pos[key]

# Physics constants for the game
class Physics():
    GRAVITY = 0.1

    FRICTION = dict()
    for t in 'XZ@N- S':
        FRICTION[t] = 1
    FRICTION['I'] = 0.1
    for t in ' .gj+!?^BbOS':
        FRICTION[t] = 0.08

    DENSITY = dict()
    for t in 'XZ@NI':
        DENSITY[t] = 1
    DENSITY['S'] = 0.1
    DENSITY['-'] = 0.3
    for t in ' .gj+!?^BbO':
        DENSITY[t] = 0


# Different items Tom can pick up or interact with
class Item():

    GUN_IMAGE = load_image("Gun.png")
    JETPACK_IMAGE = load_image("Jetpack.png")
    PELLET_IMAGE = load_image("Pellets.png")
    HEALTH_IMAGE = load_image("Health.png")
    COLLECTIBLE_IMAGE = load_image("Collectible.png")
    BLUE_BLOCK = load_image("BlueBlock.png")

    GUN_GET = load_sound("cockgun-02.wav") # http://www.mediacollege.com/downloads/sound-effects/weapons/cockgun-02.wav
    JETPACK_GET = load_sound("jet-start-02.wav") # http://www.mediacollege.com/downloads/sound-effects/planes/jet-start-02.wav
    COIN_GET = load_sound("coin-04.wav") # http://www.mediacollege.com/downloads/sound-effects/money/coin-04.wav
    COIN_GET.set_volume(0.4)
    HEAL_GET = load_sound("heal.mp3") # http://www.freesound.org/people/BristolStories/sounds/51713/

    def __init__(self, action, attr = ()):
        self.action = action
        self.attr = attr

    def activate(self, tom):
        self.action(tom, self.attr)

    def obtain_gun(tom, attr):
        tom.gun += attr[0]
        if attr[1] > tom.gun_max:
            tom.gun_max = attr[1]
        if tom.gun > tom.gun_max:
            tom.gun = tom.gun_max
        Item.GUN_GET.rewind()
        Item.GUN_GET.play()

    def obtain_jetpack(tom, attr):
        tom.jetpack += attr[0]
        if attr[1] > tom.jetpack_max:
            tom.jetpack_max = attr[1]
        if attr[2] > tom.jetpack_jump_max:
            tom.jetpack_jump_max = attr[2]
        if tom.jetpack > tom.jetpack_max:
            tom.jetpack = tom.jetpack_max
        Item.JETPACK_GET.rewind()
        Item.JETPACK_GET.play()

    def heal(tom, attr):
        tom.heal += attr
        Item.HEAL_GET.rewind()
        Item.HEAL_GET.play()

    def collect(tom, attr):
        global score
        tom.heal += 25
        tom.jetpack += 25
        if tom.jetpack > tom.jetpack_max:
            tom.jetpack = tom.jetpack_max
        tom.gun += 1
        if tom.gun > tom.gun_max:
            tom.gun = tom.gun_max
        score += 25
        Item.COIN_GET.rewind()
        Item.COIN_GET.play()

    def blue(tom, attr):
        if level.blue == 0:
            level.blue = attr
            Level.tiles['b'][1] = 75
            Level.tiles['B'][1] = 75
            Physics.FRICTION['b'] = 1
            Physics.DENSITY['b'] = 1

    def play(tom, sound):
        sound.play()


# Basic rolling enemy
class Mook():
    IMAGE_SIZE = (50,50)
    SIZE = (50,50)
    IMAGE = load_image("Mook.png")
    TERMINAL = 20
    #IMAGES = (STANDING_IMAGE, RUNNING_IMAGE)
    POP_SOUND = load_sound("pop.mp3") # http://www.freesound.org/people/HerbertBoland/sounds/33369/

    def __init__(self, pos):
        self.pos = pos
        self.vel = [-1,0]
        self.angle = 0
        self.ground = True
        self.health = 100
        self.attack = 100
        self.points = 100

    def draw(self, canvas):
        canvas.draw_image(Mook.IMAGE, (Mook.IMAGE_SIZE[0] * 0.5, Mook.IMAGE_SIZE[1] * 0.5), Mook.IMAGE_SIZE, (self.pos[0]-camera.pos[0],self.pos[1] - 21 - camera.pos[1]), Mook.SIZE, self.angle/21.0)
        circ = self.bounding_circle()
#        canvas.draw_circle(camera.adjust(circ[0]), circ[1], 1, "black")

    def update(self):
        if self.health <= 0:
            return False
        x0 = self.pos[0]
        self.pos[0] += self.vel[0]
        x = self.pos[X] + 21 * (1 if self.vel[0] > 0 else -1)
        h = 42
        for k in [1,h]:
            if Physics.DENSITY[level.value(level.pos((x,self.pos[1]-k)))] > 0:
                if self.vel[0] > 0:
                    self.pos[X] -= x%50
                else:
                    self.pos[X] += (-x)%50

                self.pos[X] -= self.vel[0]
                self.vel[0] = -self.vel[0]
                break
        self.angle += (self.pos[0]-x0)

        self.pos[1] += self.vel[1] + Physics.GRAVITY/2
        y = self.pos[1] - (42 if self.vel[1] < 0 else 0)
        w = 21
        for k in [-w,w]:
            if Physics.DENSITY[level.value(level.pos((self.pos[0] + k,y)))] > 0:
                if self.vel[Y] > 0:
                    self.pos[Y] -= y%50
                else:
                    self.pos[Y] += (-y)%50
                self.vel[Y] = 0
                break
        self.vel[Y] += Physics.GRAVITY
        if self.vel[Y] > Mook.TERMINAL:
            self.vel[Y] = Mook.TERMINAL

        self.pos[X] %= len(level[0])*50
        self.pos[Y] %= len(level.grid)*50
        return True

    def on_screen(self):
        return self.pos[0]+21 > camera.pos[0] and self.pos[0] - 21 < camera.pos[0] + 800 and self.pos[1] > camera.pos[1] and self.pos[1]-42 < camera.pos[1] + 600

    def bounding_circle(self):
        return ([self.pos[0],self.pos[1]-21], 21)

    def boundingbox(self):
        return (self.pos[0]-21,self.pos[0]+21,self.pos[1]-42,self.pos[1])

    def hit(self, damage):
        self.health -= damage

# More advanced enemy, not really a frog at all, spins around
class Frog():
    IMAGE_SIZE = (200,200)
    SIZE = (60,60)
    IMAGE = load_image("Frog.png")

    def __init__(self, pos, seeking):
        self.pos = pos
        self.angle = 3*math.pi/2
        self.target = self.angle
        self.jump = 1
        self.speed = 5
        self.rspeed = math.pi/30
        self.jump_distance = 150
        self.wait = 0
        self.seeking = seeking
        self.attack = 150
        self.health = 300 if seeking else 200
        if self.seeking:
            self.tom = tom
            self.points = 300
        else:
            self.startpos = [pos[0],pos[1]]
            self.radius = 200
            self.points = 200


    def draw(self, canvas):
        canvas.draw_image(Frog.IMAGE, (Frog.IMAGE_SIZE[0] * 0.5, Frog.IMAGE_SIZE[1] * (int(self.seeking) + 0.5)), Frog.IMAGE_SIZE, (self.pos[0]-camera.pos[0],self.pos[1] - camera.pos[1]), Frog.SIZE, self.angle)
#        circ = self.bounding_circle()
#        canvas.draw_circle(camera.adjust(circ[0]), circ[1], 1, "black")
#        canvas.draw_circle(camera.adjust(self.startpos), self.radius, 1, "black")

    def update(self):
        if self.health <= 0:
            return False
        if self.wait:
            self.wait -= 1
        elif self.jump:
            self.pos[0] += self.speed * math.cos(self.angle)
            self.pos[1] += self.speed * math.sin(self.angle)
            self.jump -= 1
            if self.jump == 0:
                self.wait = 30
                if self.seeking:
                    dx = tom.pos[0] - self.pos[0]
                    dy = tom.pos[1] - self.pos[1]
                    self.target = math.atan2(dy,dx)
                else:
                    dx = self.startpos[0] - self.pos[0]
                    dy = self.startpos[1] - self.pos[1]
                    theta = math.atan2(dy,dx)
                    dist = math.sqrt(dx**2 + dy**2)
                    numerator = dist**2 + self.jump_distance**2 - self.radius**2
                    denominator = 2 * dist * self.jump_distance
                    if dist > 0 and abs(numerator) < denominator:
                        a_range = math.acos(numerator / denominator)
                    else:
                        a_range = math.pi
                    r = random.random()
                    delta = r * a_range
                    self.target = theta + delta
                if self.target > self.angle:
                    while self.target > self.angle + math.pi:
                        self.target -= 2 * math.pi
                elif self.target < self.angle:
                    while self.target < self.angle - math.pi:
                        self.target += 2 * math.pi
                if self.target < self.angle:
                    self.rspeed = -abs(self.rspeed)
                else:
                    self.rspeed = abs(self.rspeed)
        elif (self.angle <= self.target if self.rspeed < 0 else self.angle > self.target):
            self.jump = self.jump_distance / self.speed
            self.wait = 50
        else:
            self.angle += self.rspeed
        return True


    def on_screen(self):
        return self.pos[0]+Frog.SIZE[0]/2 > camera.pos[0] and self.pos[0] - Frog.SIZE[0]/2 < camera.pos[0] + 800 and self.pos[1]+Frog.SIZE[1]/2 > camera.pos[1] and self.pos[1] - Frog.SIZE[1]/2 < camera.pos[1] + 600

    def bounding_circle(self):
        return ([self.pos[0],self.pos[1]], Frog.SIZE[0])

    def boundingbox(self):
        return (self.pos[0]-Frog.SIZE[0]/2,self.pos[0]+Frog.SIZE[0]/2,self.pos[1]-Frog.SIZE[1]/2,self.pos[1]+Frog.SIZE[1]/2)

    def hit(self, damage):
        self.health -= damage

# Tom's ammunition
class Pellet():

    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel

    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1] + Physics.GRAVITY/2
        self.vel[1] += Physics.GRAVITY
        pos = level.pos(self.pos)
        hit = level.value(pos)
        if Physics.DENSITY[hit] > 0:
            if hit == 'Z':
                level[pos[1]][pos[0]] = ' '
            return False
        for e in on_screen_enemies:
            circ = e.bounding_circle()
            if norm(self.pos,circ[0]) < circ[1]**2:
                e.hit(100)
                return False
        if self.pos[0] < camera.pos[0] or self.pos[0] > camera.pos[0]+800 or self.pos[1] < camera.pos[1] or self.pos[1] > camera.pos[1] + 600:
            return False
        return True

camera = Camera(tom.pos)

levels =[LevelInfo(0,
    ["                                                                                                                                                                                                         .......                 ",
    "               ............                                                                                                                                                                              .XXXXX.                 ",
    "               .....  .....                                                                                                   +                                                                    bbb   XXXXXXX                 ",
    "               YYYYY  YYYYY                                   .                                                                                                                                          XXXXXXX                 ",
    "                   Y  Y                                            g                                                  YYYY                                                                    bbb        XXXXXXX                 ",
    "                   Y .Y                                   ...    YYYYY                                                                                                                                   XXXXXXX                 ",
    "                   Y  Y                                                    f                                                                                                                       bbb  XXXXXXXXX                ",
    "                   Y. Y              ..             ..   YYYYYYYY                                               YYYY                                                                                   +XXXXXXXXX                ",
    "                   Y  Y                                                  YYYYY                                                                                                                bbb     ..XXXXXXXXX                ",
    "                   Y .Y              YYYY    j     YYYYYYYY                                                                                ..                                                        ..XXXXXXXXXXX               ",
    "    ..             Y  Y                                                                                   YYYY                           YYYYYY       .              .                             .XZZXXXXXXXXXXXYYYZZYXXXXXXX@@",
    "        ..         Y. Y        YYYYYY      m XX                                                                                                                     YYY                           XXY  YYYYYYYYYYYYYY  YXXXXXXX@@",
    "            ..                             XXXXXX            Y                                   j                                                    Y         g                                XXXY  YYYYYYYYYYYYYY  YXXXXXXXXX",
    " t                 m                     XXXXXXXXXX          Y         r                                    m           m               m       ..    Y     ..                                  XXXXY  YYYYYYYYYYYYYY  YXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXY   .YXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  m            m XXXXXXXYYYYY..YYYY..YYYYYYYYYY..YYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX               XXXXXY  YYYYYYYYYYYYYY  YXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXY   gYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX . XXXXXXXXXXXX     ..    ..          ..   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    f   f    XXXXXXY     . . . .      YXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXY   .YXXXXXXXXXXX    +     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX . XXXXXXXXXXXX                             XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX     g     XXXXXXXY               m  YXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXY   .YXXXXXXXXXX..........XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX . XXX jg XXXXX                              XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  m B m  XXXXXXXXXYYYIIIIIIIIIIIIYYYYXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXY                        YYYYYYYYYXXXXXXXXXXXXXXXXXXXXXXXX . ZZZ    XXXXX                               XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXYYYYYYYYYYYYYYYYYYYXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXY            m       m  YYYYYYYYYYYYYYYYYXXXXXXXXXXXXXXXX . ZZZ .. XXXXX                                XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYXXXXXXXXXXXX   XXXXXXXXXXXX                                 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"],
    {'f': (False, False, True),
     'g': ((30,50),(10,50),(20,50), (10,50), (10,50)),
     'j': ((500,1000,80),(1000,2000,250),(500,1000,80),(500,1000,80)),
     '+': (200, 100, 100, 300, 400, 200),
     'B': (1200,),}
    ),
    LevelInfo(1,
    ["                                                                                                                                                                                                                                 ",
    "                                                                               ......                                                                                                                                            ",
    "                                                                               ......                                                                                                                                            ",
    "                                                                               NNNNNN                                                                                                                                            ",
    "                                                               ...                                                                                                                                                               ",
    "                                                           .                              NNNNNN                                                                                                                                 ",
    "                                                          NNN                                                   . . . .               . . . .                                                                                    ",
    "                                                      .                                               YYY      . . . .                 . . . .                                                                                   ",
    "                                                     NNN                                            Y          XX XX XX       +       XX XX XX                                                                                   ",
    "               YY                 YYY            .                                              YYY             XXXXXX  .  .  .  .  .  XXXXXX                                                                                    ",
    "                                                NNN                                            Y                  XXXXXX XX XX XX XX XXXXXX                                                                                      ",
    "                        g                   .                                    ...      YYY                       XXXXXXXXXXXXXXXXXXXXX                  .                                                                     ",
    "                     YYYYYY                NNN                                         YY                           XXXXXXXXXXXXXXXXXXXXX                  Y                                                                     ",
    "               Y                  YYY                   Y   Y                    YYY                                XXXXXXXX....XXXXXXXXX                 YYY                                                               .....",
    "      Y Y                               +              YY . YY                    Y                f                XXXXXXXX....XXXXXXXXX        Y   YYYYYYYYYYYYYY                                                 f       .....",
    " t   YY YY       YYYm      mYYY              r        YYY   YYY                   Y    r                            XXXXXXXX....XXXXXXXXX        Y   Y            Y       r       m m m    ^^^   ^^^  ^^^  ^^^ r            .....",
    "XXXXXXXKXXX--XXXXXYYY  ..  YYYXXXXXXXXXXXXXXXXXXXXXXXXXXX . XXXXXXXXNNXXXXXXXXXXXXXXXXXXXXXXXXXXXYNNNYXXXXXXXXXXXXXXXXXXXXXXZZZZXXXXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   NNNN   XXXXXXX",
    "XXXXXXX XXXj.XXXXXXYYY .. YYYXXXXXXXXXXXXXXXXXXXXXXXXXXXX>  XXXXXXXXZZZZXXXXXXXXXXXXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXXZZZZXXXXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXXX  f  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX        XXXXXXXX",
    "XXXXXXX X    XXXXXXXXXYYYYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX . XXXXXXXX      XXXXXXXXXXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXX....X   f                XXXXXXXXXXXXXXXXXXXXXXXXX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX      XXXXXXXXX",
    "XXXXXXX X f mXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   XXXXXXXXXX     f  .    .XXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXX....X                    XXXXXXXXXXXXXXXXXXXXXXXXXX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX      XXXXXXXXX",
    "XXXXXXX X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-. XXXXXXXXXXXXX     . +  .XXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXX....X----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXX      XXXXXXXXX",
    "XXXXXXX.X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXX              XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX     XXXXXXXXXXXXXXXXXXXXXXXXXXXX      XXXXXXXXX",
    "XXXXXXX.X f  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX .-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   XXXXXXXXXXXXX                   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX     XXXXXXXXXXXXXXXXXXXXXXXXXXX      XXXXXXXXX",
    "XXXXXXX.Xm    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  <XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX           XXXXXXXXX  f          mXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX     XXXXXXXXXXXXXXXXXXXXXXXXXX      XXXXXXXXX",
    "XXXXXXX.XXX   gXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX . XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX           XXXXXX       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX     XXXXXXXXXXXXXXXXXXXXXXXXX      XXXXXXXXX",
    "XXXXXXX.       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX     XXXXXXXXXXXXXXXXXXXXXXXX      XXXXXXXXX",
    "XXXXXXX.       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXNNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX           Z          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX     XXXXXXXXXXXXXXXXXXXXXXXX      XXXXXXXXX",
    "XXXXXXXNNNNNNNNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX...XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXN         NZ       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX@@@@XXXXXXXXXXXXXXXXXXXXXXXX      XXXXXXXXX",
    "XXXXXXX        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX           XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX@@@@XXXXXXXXXXXXXXXXXXXXXXXX      XXXXXXXXX"],
    {'f': (True, False, False, True, False, True, True, True),
     'g': ((30,50),(10,50),(20,50)),
     'j': ((500,1000,80),),
     '+': (200, 100, 100)}
    ),
    LevelInfo(2,
    ["                                                                                                                                                                                                                   ",
    "                                                                                                                                                                                                       .            ",
    "                                                                                                                                       III                                                       .        @@        ",
    "                                                   .               ....                                                                I    .                                    .    .    .        II              ",
    "                                                   .       .II     bbbb     .                                                          I       .        . . .. .. . . .. .                    II                    ",
    "                                                   .     . b                 .                                                         I..IIII  III  IIIbIbIbbbbbbbIbIbbIbI b II b II    II                         ",
    "                                                   b                         .                                                         I                                                                            ",
    "                                                       II                     .                                                        I   .    . b                                                                 ",
    "                                                         bb  .                .                                                         III  II   b                                                                 ",
    "                                                                               .                                                              b . b                                                                 ",
    "                                                             II   .            .                                                                  b                                                                 ",
    "                                                                                .                                                            ..                                                                     ",
    "                                                                 III            .                                                           IIII                                                                    ",
    "                                                                                 .                                                    ..                                                                            ",
    "                                                            bbbb                 .                                  ..               bbbb                                                                           ",
    "                                                                                  .                                                                                                                                 ",
    " t                                    m               m  B     r                  .                    ..       ..    r  ..m    B                                                                                   ",
    "XXXIIIIIIISSS .                       XXXXXSSSSSSSSSSSSSXXXXXXXXXXXXXXXXXX---      .           ..      II  SSSSSSSSSSSXXXXXXXXXXXXXXXX                                                                              ",
    "XXXXXXXXXXXXXII .         f          XXXXXXXXXSSSSSSSSXXXXXXXXXXXXXXXXXXXX         .           II  ..      SSSSSSSSSXXXXXXXXXXXXXXXXXX                                                                              ",
    "XXXXXXXXXXXXXXXII .                 XXXXXXXXSSSSSSSSSXXXXXXXXXXXXXXXXXXXXX        III              II      SSSSSSSXXXXXXXXXXXXXXXXXXXX                                                                              ",
    "XXXXXXXXXXXXXXXXXII .    IIII      XXXXXXXXX.SSSSS.XXXXXXXXXXXXXXXXXXXXXXX   ..                       ..   SSSSSXXXXXXXXXXXXXXXXXXXXXX                                                                              ",
    "XXXXXXXXXXXXXXXXXXXII             XXXXXXXXXXSSXXXXXXXXXXXXXXXXXXXXXXXXXXXX   II                   ..  II   SSXXXXXXXXXXXXXXXXXXXXXXXXX                                                                              ",
    "XXXXXX. . . . . . XXX            XXXXXXXXXXXSSSSSSSSSSSXXXXXXXXXXXXXXXXXXX               f        II       XXXXXXXXXXXXXXXXXXXXXXXXXXX                                                                              ",
    "XXXXXX                          XXXXXXXXXXXXSSSSSSSSSSSXXXXXXXXXXXXXXXXXXX     .                           XXXXXXXXXXXXXXXXXXXXXXXXXXX                                                                              ",
    "XXXXXX        f                 XXXXXXXXXXXXXXXXXXXXXSSXXXXXXXXXXXXXXXXXXX     I              ..           XXXXXXXXXXXXXXXXXXXXXXXXXXX                                                                              ",
    "XXXXXXg              SSSSSSSSSXXXXXXXXXXXXXXXXXXXXXXXSSXXXXXXXXXXXXXXXXXXX        ..          II           XXXXXXXXXXXXXXXXXXXXXXXXXXX                                                                              ",
    "XXXXXXIIIIIIIIIIIIIIIXXXXSSSSXXXXXXXXXXXXXXXXXXXXXXXXSSXXXXXXXXXXXXXXXXXXX       III                       XXXXXXXXXXXXXXXXXXXXXXXXXXX                                                                              ",
    "XXXXXXXXXXXXXXXXXXXXXXXXX....XXXXXXXXXXXXXXXXXXXXXXXXSSXXXXXXXXXXXXXXXXXXX             ...                 XXXXXXXXXXXXXXXXXXXXXXXXXXX                                                                              ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXSSSS. . . . . . . . .------       III                 XXXXXXXXXXXXXXXXXXXXXXXXXXX                                                                              ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXSSSS . . . . . . . .                                  XXXXXXXXXXXXXXXXXXXXXXXXXXX                                                                              ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXII                               XXXXXXXXXXXXXXXXXXXXXXXXXXX                                                                              "],
    {'f': (True,False,True),
     'g': ((30,50),),
     'B': (1000,1000),
     '+': (200,)}
    ),
    LevelInfo(3,
    ["                ",
     "       @@       ",
     "                ",
     "                ",
     "                ",
     "                ",
     "...........    m",
     "XXXXXXXXXXX-----",
     "       X        ",
     "       X   f    ",
     "ZZZ^ZZZX        ",
     " . X  <X--------",
     " . X   X        ",
     " . X>  Xm       ",
     " . X   X--------",
     " . X  <X        ",
     " . X   X       m",
     " . X>  X--------",
     " . X            ",
     " . X            ",
     "ZZZXNNNNNNNNNNNN",
     "                ",
     "  ..            ",
     "  bb   ..       ",
     "       bb  ..   ",
     "           bb   ",
     "                ",
     "   NN  NN   NNNN",
     "                ",
     "                ",
     "B ^^..^^..^^    ",
     "XXXXXXXXXXXXX...",
     "                ",
     "                ",
     "....NNNN.NNN.NNN",
     "                ",
     "        f       ",
     "m               ",
     "NNN.NNNN.NNN....",
     "        f       ",
     "               m",
     "...NNN.NNNNN.NNN",
     "                ",
     "m               ",
     "XXXXXXXXXXXX....",
     "                ",
     "        f       ",
     "               m",
     "....XXXXXXXXXXXX",
     "                ",
     "        f       ",
     "m               ",
     "XXXXXXXX   XXXXX",
     "        ..      ",
     "        bb..    ",
     "          bb    ",
     "              ..",
     "     f        bb",
     "           ..   ",
     "           bb   ",
     "       ..       ",
     "       bb       ",
     "                ",
     "XXXXX           ",
     "m           B   ",
     "XXXXXXZZZXXXXXXX",
     "XXXXXX . XXXXXXX",
     "XXXXXX . XXXXXXX",
     "XXXXXX . XXXXXXX",
     "XXXXXX . XXXXXXX",
     "XXXXXX . XXXXXXX",
     "XXXXXX . XXXXXXX",
     "XXXXXX . XXXXXXX",
     "XXXXXXZZZXXXXXXX",
     "                ",
     " ..        ..   ",
     "XXX        XXX  ",
     "      ....      ",
     "      XXXX      ",
     "                ",
     "m    ....      m",
     "XXXXX f  XXXXXXX",
     "                ",
     "       ..       ",
     "     XXXX       ",
     "g               ",
     "XX           XXX",
     "                ",
     "  t..j..        ",
     "XXXXXXXX  XXXXXX",
     "XXXXXXXX  XXXXXX",
     "XXXXXXXX  XXXXXX",
     "XXXXXXXX  XXXXXX"],
    {'g': ((5,50),),
     'j': ((0,1000,1000),),
     'f': (True,False,False,True,False,True,True),
     'B': (1000,500),
     'L': 0.5,
     'W': False}
    )
]




frame = simplegui.create_frame("The Adventure of Tom",800,600)
frame.set_canvas_background("aqua")

on_screen_enemies = []

frame_count = 0

def nothing(pos):
    pass

def set_handlers(draw = nothing, keydown = nothing, keyup = nothing, mouseclick = nothing, mousedrag = nothing):
    frame.set_draw_handler(draw)
    frame.set_keydown_handler(keydown)
    frame.set_keyup_handler(keyup)
    frame.set_mouseclick_handler(mouseclick)
    frame.set_mousedrag_handler(mousedrag)


t = time()

def update():
    global on_screen_enemies, score, t
    on_screen_enemies = [e for e in level.enemies if (e.on_screen())]
    for k in [0,1]:
        if tom.health > 0:
            tom.update()
        for e in on_screen_enemies:
            if not e.update():
                level.enemies.remove(e)
                on_screen_enemies.remove(e)
                score += e.points
                Mook.POP_SOUND.rewind()
                Mook.POP_SOUND.play()
        level.update()

def draw_midgame(canvas):
    if tom.ground == '@@':
        tom.hit = tom.heal = 0
        frame.set_mousedrag_handler(nothing)
        frame.set_mouseclick_handler(nothing)
        frame.set_draw_handler(draw_endgame)
        timer.stop()
        Level.COMPLETE_SOUND.rewind()
        Level.COMPLETE_SOUND.play()
        return
    global on_screen_enemies, score, frame_count, disp_score
    camera.update()
    frame_count += 1
    if score > disp_score:
        disp_score += 4
        if disp_score > score:
            disp_score = score
    level.draw(canvas)
    tom.draw(canvas)
    if level.level_info.num == 2:
        level.draw_over_snow(canvas)
    for e in on_screen_enemies:
        e.draw(canvas)
    if level.level_info.num == 3:
        level.draw_over_lava(canvas)
    canvas.draw_line((10,30),(10+(tom.health/4 if frame_count % 2 == 0 else min(tom.max_health,tom.health - tom.hit + tom.heal)/4),30),20,"red")
#    if tom.hit % 2 == 0:
#        canvas.draw_line((10,30),(10+tom.health/4,30),20,"red")
    s = str(disp_score)
    canvas.draw_text('0'*(5-len(s)) + s,(650,50),20,"black")
    if tom.health > 0:
        if tom.gun > 0:
            canvas.draw_image(Item.GUN_IMAGE, (25,25), (50,50), (30,570), (50,50))
            n = min(tom.gun // 10 * 6, 50)
            if n > 0:
                canvas.draw_image(Item.PELLET_IMAGE, (30,n/2),(60,n), (90,550+n/2),(60,n))
            m = tom.gun % 10 * 6
            if m > 0:
                canvas.draw_image(Item.PELLET_IMAGE, (m/2,3),(m,6), (60+m/2,553+n),(m,6))
        if tom.jetpack > 0:
            canvas.draw_image(Item.JETPACK_IMAGE, (25,25), (50,50), (150, 570), (50,50))
            width = tom.jetpack*100//tom.jetpack_max
            canvas.draw_line((180,570),(180+width,570),40,"gray")
            if tom.jetpack_jump > 0:
                line_width = 40*(tom.jetpack_jump/tom.jetpack_jump_max)
                if line_width > 0:
                    canvas.draw_line((180,590-line_width/2),(180+width,590-line_width/2),line_width,"red")
    else:
        Tom.THRUSTER_SOUND.pause()
        frame.set_keyup_handler(nothing)
        frame.set_mousedrag_handler(nothing)
        if '\n' in Menu.player_name:
            message = "Click anywhere to continue"
            frame.set_mouseclick_handler(Menu.level_complete)
            frame.set_keydown_handler(nothing)
        else:
            message = "Enter your name: "+Menu.player_name
            frame.set_mouseclick_handler(nothing)
            frame.set_keydown_handler(Menu.type_name)
        canvas.draw_text("GAME OVER", (250,320), 50, "black")
        canvas.draw_text(message, (185, 360), 30, "black")

def draw_endgame(canvas):
    global score, disp_score
    message = ""
    if score > disp_score:
        disp_score += 5
        if disp_score > score:
            disp_score = score
    elif tom.gun > 0:
        tom.gun -= 1
        score += 25
        disp_score += 5
        if tom.gun == 0:
            tom.arm = None
    elif tom.jetpack > 0:
        if tom.jetpack < 10:
            score += int(tom.jetpack/2)
            disp_score = score
            tom.jetpack = 0
        else:
            tom.jetpack -= 10
            score += 5
            disp_score = score
    elif '\n' not in Menu.player_name:
        frame.set_keydown_handler(Menu.type_name)
        frame.set_mouseclick_handler(nothing)
        message = "Enter your name: "+Menu.player_name
    else:
        Menu.play = False
        frame.set_mouseclick_handler(Menu.level_complete)
        frame.set_keydown_handler(nothing)
        message = "Click anywhere to continue"
    level.draw(canvas)
    tom.draw(canvas)

    canvas.draw_line((10,30),(10+(tom.health/4 if frame_count % 2 == 0 else max(min(tom.max_health,tom.health - tom.hit + tom.heal),0)/4),30),20,"red")
#    if tom.hit % 2 == 0:
#        canvas.draw_line((10,30),(10+tom.health/4,30),20,"red")
    s = str(disp_score)
    canvas.draw_text('0'*(5-len(s)) + s,(650,50),20,"black")
    if tom.gun > 0:
        canvas.draw_image(Item.GUN_IMAGE, (25,25), (50,50), (30,570), (50,50))
        n = min(tom.gun // 10 * 6, 50)
        if n > 0:
            canvas.draw_image(Item.PELLET_IMAGE, (30,n/2),(60,n), (90,550+n/2),(60,n))
        m = tom.gun % 10 * 6
        if m > 0:
            canvas.draw_image(Item.PELLET_IMAGE, (m/2,3),(m,6), (60+m/2,553+n),(m,6))
    if tom.jetpack > 0:
        canvas.draw_image(Item.JETPACK_IMAGE, (25,25), (50,50), (150, 570), (50,50))
        width = tom.jetpack*100//tom.jetpack_max
        canvas.draw_line((180,570),(180+width,570),40,"gray")
        if tom.jetpack_jump > 0:
            line_width = 40*(tom.jetpack_jump/tom.jetpack_jump_max)
            canvas.draw_line((180,590-line_width/2),(180+width,590-line_width/2),line_width,"red")
    canvas.draw_text("COMPLETE!", (250,320), 50, "black")
    canvas.draw_text(message, (185, 360), 30, "black")

timer = simplegui.create_timer(20, update)

frame.set_draw_handler(Menu.draw_title)
def check_ready():
    if Frog.IMAGE.get_width() > 0:
        global ready
        ready = True
        ready_timer.stop()
        frame.set_mouseclick_handler(Menu.click_menu)

ready_timer = simplegui.create_timer(100, check_ready)
ready_timer.start()

frame.set_draw_handler(Menu.draw_title)
frame.start()