import pygame
import random
global title_font
global main_font
global score
pygame.init()
title_font = pygame.font.SysFont('Courier', 40)
main_font = pygame.font.SysFont('Courier',18,True)

# Score object, evaluates score
class Score:

    def __init__(self):
        '''Stores score'''
        self.score = 0
        self.w_count = 0
        self.l_count = 0
        self.history = []

    def show_score(self):
        return str(self.score)

    def win_loss_ratio(self):
        if self.w_count == 0 or self.l_count == 0:
            return 'N/A'
        return str(round(self.w_count/self.l_count,2))

    def win(self):
        self.history.append('win')
        self.w_count += 1
        streak = False
        if len(self.history) >= 5:
            streak = True
            for score in self.history[len(self.history)-5:]:
                if score == 'loss':
                    streak = False
                    break
        if streak == True:
            self.score += 2
        else:
            self.score += 1

    def loss(self):
        self.history.append('loss')
        self.l_count += 1

    def reset(self):
        self.score = 0
        self.w_count = 0
        self.l_count = 0
        self.history = []


# Displays main menu
def main_menu():
    screen = pygame.display.set_mode((800,450))
    pygame.display.set_caption("Organic Chemistry")
    screen.fill((36,255,0))
    
    start_button = pygame.rect.Rect(320, 185, 160, 80)
    inst_button = pygame.rect.Rect(255, 315, 300, 80)
    pygame.draw.rect(screen, (255,0,36), start_button)
    pygame.draw.rect(screen, (255,0,36), inst_button)
    
    texts = []
    for text in ["Organic chem","Start","Instrucions"]:
        texts.append(title_font.render(text,True,(0,0,0)))
    for i,pos in enumerate([(255,50),(335,200),(270,330)]):
        screen.blit(texts[i],pos)
    
    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 1:
                if start_button.collidepoint(ev.pos):
                    diff_select(screen)
                    break
                elif inst_button.collidepoint(ev.pos):
                    inst_page(screen)
                    break
        pygame.display.flip()
    pygame.quit()

# Displays instruction page
def inst_page(screen):
    screen.fill((36,255,0))

    menu_button = pygame.rect.Rect(30,50,40,40)
    start_button = pygame.rect.Rect(320, 315, 160, 80)
    pygame.draw.rect(screen, (255,0,36), menu_button)
    pygame.draw.rect(screen, (255,0,36), start_button)

    texts = []
    for text,font in [["Instructions",title_font],["These are instructions",main_font],["Start",title_font]]:
        texts.append(font.render(text,True,(0,0,0)))
    for i,pos in enumerate([(100,50),(50,100),(335,330)]):
        screen.blit(texts[i],pos)

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 1:
                if menu_button.collidepoint(ev.pos):
                    main_menu()
                    break
                elif start_button.collidepoint(ev.pos):
                    diff_select(screen)
                    break
        pygame.display.flip()
    pygame.quit()

# Allows player to select dificulty and starts game controller
def diff_select(screen):
    pygame.display.set_mode((1344,756))
    pygame.display.set_caption("Organic Chemistry")
    screen.fill((36,255,0))
    title_text = title_font.render("Difficulty Select",True,(0,0,0))
    screen.blit(title_text,(120,50))
    menu_button = pygame.rect.Rect(30,50,60,40)
    menu_text = main_font.render("Menu",True,(0,0,0))
    pygame.draw.rect(screen, (255,0,36), menu_button)
    screen.blit(menu_text,(40,60))
    buttons,button_texts = make_labled_buttons([[220, 165, 800, 80],[220, 315, 800, 80],[220, 465, 800, 80]],["Easy - Skeletal formulae","Medium - Only names, hints","Hard - Only names"],title_font)
    print_labled_buttons(screen,buttons,button_texts,(255,0,36),[15,15])
    
    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 1:
                if menu_button.collidepoint(ev.pos):
                    main_menu()
                    break
                elif buttons[0].collidepoint(ev.pos):
                    main_control(screen,0)
                    break
                elif buttons[1].collidepoint(ev.pos):
                    main_control(screen,1)
                    break
                elif buttons[2].collidepoint(ev.pos):
                    main_control(screen,2)
                    break
        pygame.display.flip()
    pygame.quit()

# Game controller
def main_control(screen,diff):
    score.reset()
    stop = False
    while not stop:
        question = generate()
        random.shuffle(question[-1])
        stop = game(screen,question)

# Creates buttons, a button is a rectangle and text
def make_labled_buttons(coordinates,texts,font=main_font,pos_only=False):
    buttons = []
    button_texts = []
    if pos_only:
        for x in coordinates:
            buttons.append(pygame.rect.Rect(x,600,160,80))
    else:
        for x,y,sx,sy in coordinates:
            buttons.append(pygame.rect.Rect(x,y,sx,sy))
    for i,text in enumerate(texts):
        max_length = buttons[i].width
        if font.size(text)[0] > max_length-40:
            lines = []
            text = split_text(text,max_length,font)
            for line in text:
                lines.append(font.render(line,True,(0,0,0)))
            button_texts.append(lines)
        else:
            button_texts.append(font.render(text,True,(0,0,0)))
    return buttons,button_texts

#Prints buttons onto the screen
def print_labled_buttons(screen,buttons,texts,color,offset):
    for i,button in enumerate(buttons):
        pygame.draw.rect(screen, color, button)
        if type(texts[i]) == type([]):
            line_offset = 0
            for line in texts[i]:
                screen.blit(line,(button.x+offset[0],button.y+offset[1]+line_offset))
                line_offset += line.get_height()
        else:
            screen.blit(texts[i],(button.x+offset[0],button.y+offset[1]))

# Splits a line into several smaller lines to print
def split_text(text,max_length,font):
    text = text.split()
    lines = []
    line = ''
    for word in text:
        if font.size(line+' '+word)[0] >= max_length-40 and line != '':
            lines.append(line)
            line = ''
        if line != '':
            line = " ".join([line,word])
        else:
            line = word
    if line != '':
        lines.append(line)
    return lines

# One round of the game
def game(screen,question):
    pygame.display.set_mode((1344,756))
    pygame.display.set_caption("Organic Chemistry")
    drag = [False,0]
    buttons,button_texts = make_labled_buttons([[50,300,160,80],[1130,300,160,80],[30,50,60,40],[50,630,80,40],[1216,630,80,40]],[question[0],question[1],'Menu','Reset','Submit'])
    ans_buttons,ans_texts = make_labled_buttons([190,390,590,790,990],question[-1],main_font,True)
    
    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 1:
                
                for i,button in enumerate(buttons):
                    if button.collidepoint(ev.pos):
                        if i == 2:
                            main_menu()
                            return True
                        elif i == 3:
                            for i,x in enumerate([190,390,590,790,990]):
                                ans_buttons[i].x = x
                                ans_buttons[i].y = 600
                        elif i == 4:
                            ans = []
                            for i,button in enumerate(ans_buttons):
                                if button.y < 470:
                                    ans.append([i,button.x])
                            correct(question[2],question[3],ans)
                            return False
                            
                for i,button in enumerate(ans_buttons):
                    if button.collidepoint(ev.pos):
                        drag = [True,i]
                        mouse_x, mouse_y = ev.pos
                        offset_x = button.x - mouse_x
                        offset_y = button.y - mouse_y
                        
        elif ev.type == pygame.MOUSEBUTTONUP:
            if ev.button == 1:            
                drag[0] = False
                
        elif ev.type == pygame.MOUSEMOTION:
            if drag[0]:
                mouse_x, mouse_y = ev.pos
                ans_buttons[drag[1]].x = mouse_x + offset_x
                ans_buttons[drag[1]].y = mouse_y + offset_y

        screen.fill((36,255,0))
        screen.fill((255,0,36),(0,550,1344,20))
        print_labled_buttons(screen,buttons,button_texts,(255,0,36),[10,10])
        print_labled_buttons(screen,ans_buttons,ans_texts,(0,102,255),[10,10])
        score_text = title_font.render("Score: "+score.show_score()+"   W/L Ratio: "+score.win_loss_ratio(),True,(0,0,0))
        screen.blit(score_text,(120,50))
        pygame.display.flip()
    pygame.quit()
    return True

# Generates questions from contents of questions file
def generate():
    i,o,p,allp = load_text('questions.txt')

    ps = []
    val = random.randint(0,len(i)-1)
    
    for j in p[val]:
        ps.append(j)
    while len(ps) < 5:
        k = random.choice(allp)
        if k not in ps:
            ps.append(k)
    
    return [i[val],o[val],p[val],ps]

# Corrects the answer entered by the player and changes the score
def correct(correct_ans,ans_order,ans):
    ans = sort(ans)
    print(correct_ans,ans_order,ans)
    correct_numbers = []
    for p in correct_ans:
        correct_numbers.append(ans_order.index(p))

    ans_list = []
    for a in ans:
        ans_list.append(a[0])
    if correct_numbers == ans_list:
        score.win()
    else:
        score.loss()

# Just a bubble sort
def sort(things):
    done = False
    while not done:
        done = True
        for i in range(len(things)-1):
            if things[i][1] > things[i+1][1]:
                done = False
                j = things[i]
                things[i] = things[i+1]
                things[i+1] = j
    return things

# Loads contents of a file
def load_text(filename):
    inputs = []
    outputs = []
    processes = []
    all_processes = []
    file = open(filename,'r')
    lines = file.readlines()
    for line in lines:
        if "%" in line:
            continue
        if '\n' in line:
            line = line[:-1]
        line = line.split(';')
        inputs.append(line[0])
        outputs.append(line[1])
        processes.append(line[2:])
    for i in processes:
        for process in i:
            if process not in all_processes:
                all_processes.append(process)
    return [inputs,outputs,processes,all_processes]

score = Score()

if __name__ == '__main__':
    main_menu()
