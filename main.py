import pygame
pygame.init()
tamanho = (800,600)
relogio = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho )
pygame.display.set_caption("Iron man do techio")
branco = (255,255,255)
preto = (0,0,0)
possicaoXpersona = 400
possicaoYpersona = 300
movimentoXpersona = 0
movimentoYpersona = 0
fonte = pygame.font.SysFont("comicsans",14)
iron = pygame.image.load("assets/iron.png")
fundo = pygame.image.load("assets/fundo.png")


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
        #movimento X
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:   #direita
            movimentoXpersona = 7
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:    #esquerda
            movimentoXpersona = -7
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:     #direita
            movimentoXpersona = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:      #esquerda
            movimentoXpersona = 0
        #movimento Y
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:    #baixo
            movimentoYpersona = 7
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:      #alto
            movimentoYpersona = -7
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_DOWN:      #baixo      
            movimentoYpersona = 0
        elif evento.type == pygame.KEYUP and evento.key == pygame.K_UP:        #alto
            movimentoYpersona = 0

    possicaoYpersona = possicaoYpersona + movimentoYpersona   #movimento Y
    possicaoXpersona = possicaoXpersona + movimentoXpersona   #movimento X 

    if possicaoXpersona < 0:      #restigir movimento em X
        possicaoXpersona = 10
    elif possicaoXpersona > 550:
        possicaoXpersona = 540 
    if possicaoYpersona < 40:     #restigir movimento em Y
        possicaoYpersona = 40
    elif possicaoYpersona > 473:
        possicaoYpersona = 463  

    tela.fill(branco) 
    tela.blit(fundo,(0,0))
    tela.blit(iron, (possicaoXpersona,possicaoYpersona))
    #pygame.draw.circle(tela,preto,(possicaoXpersona,possicaoYpersona),40,0) 

    texto = fonte.render(str(possicaoXpersona)+"-"+str(possicaoYpersona),True,branco)
    tela.blit(texto,(possicaoXpersona -30,possicaoYpersona -10))


    pygame.display.update()
    relogio.tick(60)
