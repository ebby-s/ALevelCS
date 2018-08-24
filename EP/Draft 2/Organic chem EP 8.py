import pygame
import random

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
    stop = False
    while not stop:
        question = generate()
        random.shuffle(question[-1])
        stop = game(screen,question)

def game(screen,question):
    score.reset()
    ans_buttons = []
    ans_texts = []
    for x in [190,390,590,790,990]:
        ans_buttons.append(pygame.rect.Rect(x,600,160,80))
    drag = [False,0]
    for text in question[-1]:
        ans_texts.append(title_font.render(text,True,(0,0,0)))
    
    in_box = pygame.rect.Rect(50,300,160,80)
    out_box = pygame.rect.Rect(1130,300,160,80)
    menu_button = pygame.rect.Rect(30,50,40,40)
    reset_button = pygame.rect.Rect(50,630,40,40)
    submit_button = pygame.rect.Rect(1256,630,40,40)
    
    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 1:
                if menu_button.collidepoint(ev.pos):
                    main_menu()
                    break
                elif reset_button.collidepoint(ev.pos):
                    for i,x in enumerate([190,390,590,790,990]):
                        ans_buttons[i].x = x
                        ans_buttons[i].y = 600
                elif submit_button.collidepoint(ev.pos):
                    correct()
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
        pygame.draw.rect(screen, (255,0,36), menu_button)
        pygame.draw.rect(screen, (255,0,36), in_box)
        pygame.draw.rect(screen, (255,0,36), out_box)
        pygame.draw.rect(screen, (255,0,36), reset_button)
        pygame.draw.rect(screen, (255,0,36), submit_button)
        for i,button in enumerate(ans_buttons):
            pygame.draw.rect(screen, (0,36,255), button)
            screen.blit(ans_texts[i],(button.x+20,button.y+20))
        score_text = title_font.render("Score: "+score.show_score()+"   W/L Ratio: "+score.win_loss_ratio(),True,(0,0,0))
        screen.blit(score_text,(100,50))
        pygame.display.flip()
    pygame.quit()
    return True

def generate():
    i = ['q0','q1','q2','q3','q4','q5','q6','q7','q8','q9']
    p = ['p0','p1','p2','p3','p4','p5','p6','p7','p8','p9']
    o = ['a0','a1','a2','a3','a4','a5','a6','a7','a8','a9']
    allp = ['abb','bcc','cdd','dee','eff','fgg','ghh','hii','ijj','jkk']

    ps = []
    val = random.randint(0,9)
    
    for j in p[val]:
        ps.append(j)
    while len(ps) < 5:
        k = random.choice(allp)
        if k not in ps:
            ps.append(k)
    
    return [i[val],o[val],p[val],ps]

pygame.init()
global title_font
global main_font
global score
title_font = pygame.font.SysFont('Courier', 40)
main_font = pygame.font.SysFont('Courier',18)
score = Score()

main_menu()
