import pygame

def main_menu():
    window_size = (800,450)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Organic Chemistry")
    screen.fill((36,255,0))
    title_font = pygame.font.SysFont('Courier', 40)
    title_text = title_font.render("Organic chem",True,(0,0,0))
    screen.blit(title_text,(255,50))
    start_button = pygame.rect.Rect(320, 185, 160, 80)
    start_text = title_font.render("Start",True,(0,0,0))
    inst_button = pygame.rect.Rect(255, 315, 300, 80)
    inst_text = title_font.render("Instrucions",True,(0,0,0))
    pygame.draw.rect(screen, (255,0,36), start_button)
    screen.blit(start_text,(335,200))
    pygame.draw.rect(screen, (255,0,36), inst_button)
    screen.blit(inst_text,(270,330))

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
    title_font = pygame.font.SysFont('Courier', 40)
    main_font = pygame.font.SysFont('Courier',18)
    title_text = title_font.render("Instructions",True,(0,0,0))
    instructions_text = main_font.render("These are instructions",True,(0,0,0))
    screen.blit(title_text,(30,30))
    screen.blit(instructions_text,(50,100))
    start_button = pygame.rect.Rect(320, 315, 160, 80)
    start_text = title_font.render("Start",True,(0,0,0))
    pygame.draw.rect(screen, (255,0,36), start_button)
    screen.blit(start_text,(335,330))

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 1:
                if start_button.collidepoint(ev.pos):
                    diff_select(screen)
                    break
        pygame.display.flip()
    pygame.quit()

def diff_select(screen):
    window_size = (1344,756)
    pygame.display.set_mode(window_size)
    pygame.display.set_caption("Organic Chemistry")
    screen.fill((36,255,0))
    title_font = pygame.font.SysFont('Courier', 40)
    main_font = pygame.font.SysFont('Courier',18)
    title_text = title_font.render("Difficulty Select",True,(0,0,0))
    easy_text = title_font.render("Easy - Skeletal formulae",True,(0,0,0))
    med_text = title_font.render("Medium - Only names, hints",True,(0,0,0))
    hard_text = title_font.render("Hard - Only names",True,(0,0,0))
    easy_button = pygame.rect.Rect(220, 165, 800, 80)
    med_button = pygame.rect.Rect(220, 315, 800, 80)
    hard_button = pygame.rect.Rect(220, 465, 800, 80)
    screen.blit(title_text,(30,30))
    pygame.draw.rect(screen, (255,0,36), easy_button)
    pygame.draw.rect(screen, (255,0,36), med_button)
    pygame.draw.rect(screen, (255,0,36), hard_button)
    screen.blit(easy_text,(235,180))
    screen.blit(med_text,(235,330))
    screen.blit(hard_text,(235,480))

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            if ev.button == 1:
                if easy_button.collidepoint(ev.pos):
                    main_menu()
                    break
                elif med_button.collidepoint(ev.pos):
                    main_menu()
                    break
                elif hard_button.collidepoint(ev.pos):
                    main_menu()
                    break
        pygame.display.flip()
    pygame.quit()


pygame.init()
main_menu()
