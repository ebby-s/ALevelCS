import pygame
import random

# add highscore table, credits, gifs

# Module to Evaluate the score 
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

def diff_select(screen):
    pygame.display.set_mode((1344,756))
    pygame.display.set_caption("Organic Chemistry")
    screen.fill((36,255,0))
    
    menu_button = pygame.rect.Rect(30,50,40,40)
    easy_button = pygame.rect.Rect(220, 165, 800, 80)
    med_button = pygame.rect.Rect(220, 315, 800, 80)
    hard_button = pygame.rect.Rect(220, 465, 800, 80)
    pygame.draw.rect(screen, (255,0,36), menu_button)
    pygame.draw.rect(screen, (255,0,36), easy_button)
    pygame.draw.rect(screen, (255,0,36), med_button)
    pygame.draw.rect(screen, (255,0,36), hard_button)

    texts = []
    for text in ["Difficulty Select","Easy - Skeletal formulae","Medium - Only names, hints","Hard - Only names"]:
        texts.append(title_font.render(text,True,(0,0,0)))
    for i,pos in enumerate([(100,50),(235,180),(235,330),(235,480)]):
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
                elif easy_button.collidepoint(ev.pos):
                    main_control(screen,0)
                    break
                elif med_button.collidepoint(ev.pos):
                    main_control(screen,1)
                    break
                elif hard_button.collidepoint(ev.pos):
                    main_control(screen,2)
                    break
        pygame.display.flip()
    pygame.quit()

def main_control(screen,diff):
    score.reset()
    stop = False
    while not stop:
        question = generate()
        random.shuffle(question[-1])
        stop = game(screen,question)

def game(screen,question):
    pygame.display.set_mode((1344,756))
    pygame.display.set_caption("Organic Chemistry")
    ans_buttons = []
    ans_texts = []
    for x in [190,390,590,790,990]:
        ans_buttons.append(pygame.rect.Rect(x,600,160,80))
    drag = [False,0]
    for text in question[-1]:
        ans_texts.append(title_font.render(text,True,(0,0,0)))

    buttons = []
    button_texts = []
    for x,y,sx,sy in [[50,300,160,80],[1130,300,160,80],[30,50,60,40],[50,630,80,40],[1216,630,80,40]]:
        buttons.append(pygame.rect.Rect(x,y,sx,sy))
    for text in [question[0],question[1],'Menu','Reset','Submit']:
        button_texts.append(main_font.render(text,True,(0,0,0)))
    
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
        
        for i,button in enumerate(buttons):
            pygame.draw.rect(screen, (255,0,36), button)
            screen.blit(button_texts[i],(button.x+10,button.y+10))
        for i,button in enumerate(ans_buttons):
            pygame.draw.rect(screen, (0,36,255), button)
            screen.blit(ans_texts[i],(button.x+20,button.y+20))
        score_text = title_font.render("Score: "+score.show_score()+"   W/L Ratio: "+score.win_loss_ratio(),True,(0,0,0))
        screen.blit(score_text,(120,50))
        pygame.display.flip()
    pygame.quit()
    return True

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

def load_text(filename):
    inputs = []
    outputs = []
    processes = []
    all_processes = []
    file = open(filename,'r')
    lines = file.readlines()
    for line in lines:
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
'''
def load_picture(filename):
    '''

pygame.init()
global title_font
global main_font
global score
title_font = pygame.font.SysFont('Courier', 40)
main_font = pygame.font.SysFont('Courier',18)
score = Score()

if __name__ == '__main__':
    main_menu()
