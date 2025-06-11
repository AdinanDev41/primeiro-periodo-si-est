# Importação de bibliotecas necessárias
import pygame  # Biblioteca para criação de jogos
import sys     # Fornece acesso a funcionalidades do sistema
import random  # Geração de números aleatórios

# Inicializa todos os módulos do pygame
pygame.init()

# CONFIGURAÇÕES DA TELA

WIDTH, HEIGHT = 900, 600  # Largura e altura da janela
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Cria a janela do jogo
pygame.display.set_caption("Missão Lógica")  # Título da janela

# DEFININDO CORES (formato RGB)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PAPER_COLOR = (250, 250, 240)  # Cor de fundo para textos/explicações
BUTTON_COLOR = (100, 100, 250)  # Cor padrão dos botões
BUTTON_HOVER_COLOR = (150, 150, 255)  # Cor quando mouse está sobre o botão
BACK_BUTTON_COLOR = (200, 0, 0)  # Cor do botão de voltar
BACK_BUTTON_HOVER_COLOR = (255, 50, 50)  # Cor do botão de voltar com hover
GREEN = (0, 200, 0)  # Cor para feedback positivo
RED = (200, 0, 0)  # Cor para feedback negativo
HIGHLIGHT_COLOR = (255, 255, 0)  # Cor para destacar elementos
DRAWER_HIGHLIGHT_COLOR = (255, 200, 0, 150)  # Cor para destacar gavetas (com transparência)
TRANSPARENT = (0, 0, 0, 0)  # Cor totalmente transparente

# CONFIGURAÇÃO DE FONTES

title_font = pygame.font.SysFont("arial", 48, bold=True)  # Fonte para títulos
text_font = pygame.font.SysFont("arial", 24)  # Fonte para texto normal
small_font = pygame.font.SysFont("arial", 20)  # Fonte para texto pequeno
button_font = pygame.font.SysFont("arial", 22, bold=True)  # Fonte para botões

# ESTADOS DO JOGO (controlam a tela atual)

STATE_MENU = "menu"          # Tela inicial
STATE_EXPLANATION = "explanation"  # Tela de explicação dos conceitos lógicos
STATE_GAME = "game"          # Jogo principal (exploração dos cômodos)
STATE_DRAWER = "drawer"      # Tela quando o jogador abre uma gaveta
STATE_QUESTION = "question"  # Tela de pergunta quando interage com uma gaveta
STATE_DOOR = "door"         # Tela de interação com a porta
current_state = STATE_MENU   # Estado inicial do jogo

# CARREGAMENTO DE IMAGENS (com fallback em caso de erro)

try:
    # Carrega imagem de fundo do menu
    bg_menu = pygame.image.load("fundo-tela.jpeg")
    bg_menu = pygame.transform.scale(bg_menu, (WIDTH, HEIGHT))
    
    # Lista de imagens dos cômodos (salas) do jogo
    game_rooms = ["inicio.jpg", "cozinha.jpg", "sala.jpg"]
    room_images = []
    
    for img in game_rooms:
        try:
            # Tenta carregar cada imagem da sala
            room_img = pygame.image.load(img)
            room_images.append(pygame.transform.scale(room_img, (WIDTH, HEIGHT)))
        except:
            # Se falhar, cria uma cor sólida aleatória como fallback
            fallback = pygame.Surface((WIDTH, HEIGHT))
            fallback.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            room_images.append(fallback)
    
    # Carrega ícones de setas para navegação
    arrow_left = pygame.transform.scale(pygame.image.load("seta-esquerda.png"), (60, 60))
    arrow_right = pygame.transform.scale(pygame.image.load("seta-direita.png"), (60, 60))
    
    # Carrega ícones de cadeado (porta trancada/destrancada)
    try:
        locked_door = pygame.transform.scale(pygame.image.load("cadeado-fechado.png"), (100, 100))
        unlocked_door = pygame.transform.scale(pygame.image.load("cadeado-aberto.png"), (100, 100))
    except:
        # Fallback: cria retângulos coloridos se as imagens não carregarem
        locked_door = pygame.Surface((100, 100))
        locked_door.fill(RED)
        unlocked_door = pygame.Surface((100, 100))
        unlocked_door.fill(GREEN)
except Exception as e:
    print(f"Erro ao carregar imagens: {e}")
    sys.exit()


# ÁREAS INTERATIVAS (GAVETAS) PARA CADA CÔMODO
# Formato: (x, y, largura, altura)

drawer_areas = [
    [(200, 300, 120, 60), (400, 250, 120, 60)],  # Cômodo 0
    [(150, 350, 120, 60), (500, 300, 120, 60)],  # Cômodo 1
    [(300, 400, 120, 60), (600, 350, 120, 60)]   # Cômodo 2
]

# POSIÇÕES DAS PORTAS EM CADA CÔMODO

door_positions = [
    (700, 400),  # Cômodo 0
    (700, 350),  # Cômodo 1
    (700, 300)   # Cômodo 2
]

# BANCO DE PERGUNTAS PARA CADA GAVETA

questions = [
    [  # Cômodo 0
        {
            "question": "Se A é verdadeiro e B é falso, qual o valor de 'A e B'?",
            "options": ["Verdadeiro", "Falso"],
            "answer": 1,  # Índice da resposta correta (Falso)
            "key": True,  # Esta questão dá uma chave se respondida corretamente
            "explanation": "'A e B' só é verdadeiro quando ambos são verdadeiros."
        },
        {
            "question": "Se A é falso, qual o valor de 'não A'?",
            "options": ["Verdadeiro", "Falso"],
            "answer": 0,  # Índice da resposta correta (Verdadeiro)
            "key": False,  # Esta questão não dá chave
            "explanation": "A negação inverte o valor lógico."
        }
    ],
    [  # Cômodo 1
        {
            "question": "Se A é verdadeiro ou B é falso, qual o valor se ambos forem verdadeiros?",
            "options": ["Verdadeiro", "Falso"],
            "answer": 0,  # Resposta correta: Verdadeiro
            "key": True,
            "explanation": "Basta um ser verdadeiro para 'ou' ser verdadeiro."
        },
        {
            "question": "Se 'não A' é falso, qual o valor de A?",
            "options": ["Verdadeiro", "Falso"],
            "answer": 0,  # Resposta correta: Verdadeiro
            "key": False,
            "explanation": "Se a negação é falsa, o original é verdadeiro."
        }
    ],
    [  # Cômodo 2
        {
            "question": "'A e B' é verdadeiro somente quando:",
            "options": ["A ou B é verdadeiro", "A e B são verdadeiros", "A é falso"],
            "answer": 1,  # Resposta correta: "A e B são verdadeiros"
            "key": True,
            "explanation": "O operador 'e' requer que ambos sejam verdadeiros."
        },
        {
            "question": "'A ou B' é falso quando:",
            "options": ["A é falso", "B é falso", "Ambos são falsos"],
            "answer": 2,  # Resposta correta: "Ambos são falsos"
            "key": False,
            "explanation": "'Ou' só é falso quando ambos operandos são falsos."
        }
    ]
]

# VARIÁVEIS DE ESTADO DO JOGO

room_index = 0  # Índice do cômodo atual (0, 1 ou 2)
current_drawer = None  # Gaveta selecionada no momento
current_question = None  # Pergunta atual sendo exibida
keys_collected = [False, False, False]  # Chaves coletadas em cada cômodo
door_locked = True  # Estado da porta (trancada/destrancada)
show_message = False  # Controla se deve exibir mensagem de feedback
message_text = ""  # Texto da mensagem de feedback
game_won = False  # Indica se o jogador venceu o jogo
hovered_drawer = None  # Gaveta sob o mouse (para efeito hover)
hovered_button = None  # Botão sob o mouse (para efeito hover)

# DEFINIÇÃO DOS RETÂNGULOS DOS BOTÕES

cela_button_rect = pygame.Rect(WIDTH // 2 - 120, HEIGHT // 2 - 100, 240, 70)  # Botão principal
back_button_rect = pygame.Rect(20, 20, 100, 40)  # Botão de voltar
continue_button_rect = pygame.Rect(WIDTH - 150, HEIGHT - 70, 130, 50)  # Botão de continuar
arrow_left_rect = pygame.Rect(30, HEIGHT // 2 - 30, 60, 60)  # Seta esquerda
arrow_right_rect = pygame.Rect(WIDTH - 90, HEIGHT // 2 - 30, 60, 60)  # Seta direita
door_rect = pygame.Rect(0, 0, 120, 120)  # Área clicável da porta

# FUNÇÕES AUXILIARES

def draw_button(rect, text, color, hover_color=None, hover=False):
    """
    Desenha um botão na tela com efeito hover.
    
    Parâmetros:
        rect: Retângulo que define posição/tamanho do botão
        text: Texto do botão
        color: Cor normal do botão
        hover_color: Cor quando mouse está sobre o botão
        hover: Booleano indicando se o mouse está sobre o botão
    """
    # Desenha o retângulo do botão
    if hover and hover_color:
        pygame.draw.rect(screen, hover_color, rect, border_radius=8)
    else:
        pygame.draw.rect(screen, color, rect, border_radius=8)
    
    # Adiciona borda para melhor visibilidade
    pygame.draw.rect(screen, BLACK, rect, 2, border_radius=8)
    
    # Renderiza o texto centralizado no botão
    button_text = button_font.render(text, True, WHITE)
    screen.blit(button_text, (
        rect.centerx - button_text.get_width() // 2,
        rect.centery - button_text.get_height() // 2
    ))

def draw_explanation():
    """Desenha a tela de explicação dos conceitos lógicos."""
    screen.fill(PAPER_COLOR)  # Fundo estilo papel
    
    # Título
    title = title_font.render("CONECTIVOS LÓGICOS", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 40))
    
    # Texto explicativo (dividido em linhas)
    lines = [
        "1. E (conjunção):",
        "   'A e B' é verdadeiro somente quando A e B são verdadeiros.",
        "",
        "2. OU (disjunção):",
        "   'A ou B' é verdadeiro quando pelo menos um dos dois é verdadeiro.",
        "",
        "3. NÃO (negação):",
        "   'não A' inverte o valor lógico de A.",
        "   Se A é verdadeiro, 'não A' é falso.",
        "   Se A é falso, 'não A' é verdadeiro."
    ]
    
    # Renderiza cada linha de texto
    y_offset = 120
    for line in lines:
        text = text_font.render(line, True, BLACK)
        screen.blit(text, (60, y_offset))
        y_offset += 35 if line else 20  # Ajusta espaçamento
    
    # Botões de navegação
    draw_button(back_button_rect, "Voltar", BACK_BUTTON_COLOR, BACK_BUTTON_HOVER_COLOR, 
               back_button_rect.collidepoint(pygame.mouse.get_pos()))
    draw_button(continue_button_rect, "Continuar", BUTTON_COLOR, BUTTON_HOVER_COLOR,
               continue_button_rect.collidepoint(pygame.mouse.get_pos()))

def draw_empty_drawer():
    """Desenha a tela quando uma gaveta vazia é aberta."""
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))  # Overlay semi-transparente
    screen.blit(overlay, (0, 0))
    
    # Mensagem de gaveta vazia
    message = text_font.render("Esta gaveta está vazia!", True, WHITE)
    screen.blit(message, (WIDTH // 2 - message.get_width() // 2, HEIGHT // 2 - 50))
    
    # Botão Voltar
    draw_button(back_button_rect, "Voltar", BACK_BUTTON_COLOR, BACK_BUTTON_HOVER_COLOR,
               back_button_rect.collidepoint(pygame.mouse.get_pos()))

def draw_question(question_data):
    """
    Desenha a tela de pergunta com opções de resposta.
    
    Parâmetros:
        question_data: Dicionário com os dados da pergunta
    Retorna:
        Lista de retângulos das opções de resposta (para detecção de clique)
    """
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))  # Overlay semi-transparente
    screen.blit(overlay, (0, 0))
    
    # Título da questão
    question_title = title_font.render("Desafio Lógico", True, HIGHLIGHT_COLOR)
    screen.blit(question_title, (WIDTH // 2 - question_title.get_width() // 2, HEIGHT // 2 - 180))
    
    # Quebra o texto da pergunta em várias linhas se necessário
    question_lines = []
    words = question_data["question"].split()
    current_line = ""
    
    for word in words:
        test_line = current_line + word + " "
        if text_font.size(test_line)[0] < WIDTH - 100:
            current_line = test_line
        else:
            question_lines.append(current_line)
            current_line = word + " "
    
    if current_line:
        question_lines.append(current_line)
    
    # Renderiza cada linha da pergunta
    for i, line in enumerate(question_lines):
        question_text = text_font.render(line, True, WHITE)
        screen.blit(question_text, (WIDTH // 2 - question_text.get_width() // 2, HEIGHT // 2 - 120 + i * 30))
    
    # Desenha as opções de resposta como botões
    option_rects = []
    for i, option in enumerate(question_data["options"]):
        option_rect = pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2 - 50 + i * 70, 400, 60)
        option_rects.append(option_rect)
        
        # Efeito hover para opções
        hover = option_rect.collidepoint(pygame.mouse.get_pos())
        draw_button(option_rect, option, BUTTON_COLOR, BUTTON_HOVER_COLOR, hover)
    
    return option_rects

def draw_message():
    """Desenha a tela de mensagem de feedback após responder uma pergunta."""
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))  # Overlay semi-transparente
    screen.blit(overlay, (0, 0))
    
    # Mensagem principal
    message = text_font.render(message_text, True, WHITE)
    screen.blit(message, (WIDTH // 2 - message.get_width() // 2, HEIGHT // 2 - 50))
    
    # Se a resposta estiver correta, mostra a explicação
    if current_question and "explanation" in current_question and "Resposta correta" in message_text:
        explanation = text_font.render(current_question["explanation"], True, GREEN)
        screen.blit(explanation, (WIDTH // 2 - explanation.get_width() // 2, HEIGHT // 2 + 10))
    
    # Botão Voltar
    draw_button(back_button_rect, "Voltar", BACK_BUTTON_COLOR, BACK_BUTTON_HOVER_COLOR,
               back_button_rect.collidepoint(pygame.mouse.get_pos()))

def draw_door():
    """Desenha a tela de interação com a porta."""
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))  # Overlay semi-transparente
    screen.blit(overlay, (0, 0))
    
    all_keys_collected = all(keys_collected)  # Verifica se todas as chaves foram coletadas
    
    if door_locked:
        if all_keys_collected:
            # Mensagem quando todas as chaves foram coletadas
            message = text_font.render("Você coletou todas as chaves! A porta pode ser aberta.", True, GREEN)
            screen.blit(message, (WIDTH // 2 - message.get_width() // 2, HEIGHT // 2 - 100))
            
            # Botão para abrir a porta
            draw_button(continue_button_rect, "Abrir Porta", GREEN, (0, 255, 0),
                       continue_button_rect.collidepoint(pygame.mouse.get_pos()))
        else:
            # Mensagem quando faltam chaves
            keys_needed = sum(1 for key in keys_collected if not key)
            message = text_font.render(f"Porta trancada! Faltam {keys_needed} chaves.", True, RED)
            screen.blit(message, (WIDTH // 2 - message.get_width() // 2, HEIGHT // 2 - 50))
            
            # Mostra o status de cada chave
            for i, key in enumerate(keys_collected):
                key_text = small_font.render(f"Cômodo {i+1}: {'✔' if key else '✖'}", 
                                          True, GREEN if key else RED)
                screen.blit(key_text, (WIDTH // 2 - 100, HEIGHT // 2 + 20 + i * 30))
    else:
        # Tela de vitória
        message = title_font.render("PARABÉNS! VOCÊ ESCAPOU!", True, GREEN)
        screen.blit(message, (WIDTH // 2 - message.get_width() // 2, HEIGHT // 2 - 100))
        
        sub_message = text_font.render("Você resolveu todos os desafios lógicos!", True, WHITE)
        screen.blit(sub_message, (WIDTH // 2 - sub_message.get_width() // 2, HEIGHT // 2 - 30))
    
    # Botão Voltar
    draw_button(back_button_rect, "Voltar", BACK_BUTTON_COLOR, BACK_BUTTON_HOVER_COLOR,
               back_button_rect.collidepoint(pygame.mouse.get_pos()))

# LOOP PRINCIPAL DO JOGO

clock = pygame.time.Clock()  # Objeto para controlar o FPS
running = True  # Controla se o jogo está em execução

while running:
    mouse_pos = pygame.mouse.get_pos()  # Obtém a posição do mouse
    hovered_drawer = None  # Reseta a gaveta destacada
    hovered_button = None  # Reseta o botão destacado
    
    # Processa todos os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Evento de fechar a janela
            running = False

        # Verifica cliques do mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Estado MENU - Botão para iniciar o jogo
            if current_state == STATE_MENU and cela_button_rect.collidepoint(event.pos):
                current_state = STATE_EXPLANATION

            # Estado EXPLANATION - Botões de navegação
            elif current_state == STATE_EXPLANATION:
                if back_button_rect.collidepoint(event.pos):  # Volta ao menu
                    current_state = STATE_MENU
                elif continue_button_rect.collidepoint(event.pos):  # Vai para o jogo
                    current_state = STATE_GAME

            # Estado GAME - Interações durante a exploração
            elif current_state == STATE_GAME:
                # Verifica clique nas gavetas
                for i, drawer in enumerate(drawer_areas[room_index]):
                    drawer_rect = pygame.Rect(drawer)
                    if drawer_rect.collidepoint(event.pos):
                        current_drawer = i
                        current_state = STATE_QUESTION
                        current_question = questions[room_index][current_drawer]
                
                # Verifica clique na porta
                door_rect.x, door_rect.y = door_positions[room_index]
                if door_rect.collidepoint(event.pos):
                    current_state = STATE_DOOR
                
                # Verifica clique nas setas de navegação entre cômodos
                if arrow_left_rect.collidepoint(event.pos):
                    room_index = (room_index - 1) % len(room_images)
                elif arrow_right_rect.collidepoint(event.pos):
                    room_index = (room_index + 1) % len(room_images)

            # Estado DRAWER - Botão para voltar ao jogo
            elif current_state == STATE_DRAWER and back_button_rect.collidepoint(event.pos):
                current_state = STATE_GAME
                show_message = False

            # Estado QUESTION - Processa resposta do jogador
            elif current_state == STATE_QUESTION:
                option_rects = draw_question(current_question)
                for i, rect in enumerate(option_rects):
                    if rect.collidepoint(event.pos):
                        if i == current_question["answer"]:  # Resposta correta
                            message_text = "Resposta correta!"
                            if current_question["key"]:  # Se esta pergunta dá uma chave
                                keys_collected[room_index] = True
                                message_text += " Você encontrou uma chave!"
                        else:  # Resposta incorreta
                            message_text = "Resposta incorreta. Tente novamente!"
                        
                        current_state = STATE_DRAWER
                        show_message = True

            # Estado DOOR - Interação com a porta
            elif current_state == STATE_DOOR:
                if back_button_rect.collidepoint(event.pos):  # Volta ao jogo
                    current_state = STATE_GAME
                elif continue_button_rect.collidepoint(event.pos) and all(keys_collected):  # Abre a porta
                    door_locked = False
                    game_won = True

    # Verifica se o mouse está sobre uma gaveta (para efeito hover)
    if current_state == STATE_GAME:
        for i, drawer in enumerate(drawer_areas[room_index]):
            drawer_rect = pygame.Rect(drawer)
            if drawer_rect.collidepoint(mouse_pos):
                hovered_drawer = i
                break

    # RENDERIZAÇÃO DO ESTADO ATUAL

    screen.fill(BLACK)  # Limpa a tela
    
    # Estado MENU - Tela inicial
    if current_state == STATE_MENU:
        screen.blit(bg_menu, (0, 0))  # Fundo do menu
        
        # Título do jogo
        title = title_font.render("Missão Lógica", True, WHITE)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))
        
        # Botão principal com efeito hover
        hover = cela_button_rect.collidepoint(mouse_pos)
        draw_button(cela_button_rect, "Explorar Casa", BUTTON_COLOR, BUTTON_HOVER_COLOR, hover)

    # Estado EXPLANATION - Tela de explicação dos conceitos
    elif current_state == STATE_EXPLANATION:
        draw_explanation()

    # Estado GAME - Jogo principal (exploração dos cômodos)
    elif current_state == STATE_GAME:
        screen.blit(room_images[room_index], (0, 0))  # Imagem do cômodo atual
        
        # Seta de navegação para a esquerda (hover)
        hover_left = arrow_left_rect.collidepoint(mouse_pos)
        if hover_left:
            pygame.draw.rect(screen, HIGHLIGHT_COLOR, arrow_left_rect.inflate(10, 10), border_radius=5)
        
        # Seta de navegação para a direita (hover)
        hover_right = arrow_right_rect.collidepoint(mouse_pos)
        if hover_right:
            pygame.draw.rect(screen, HIGHLIGHT_COLOR, arrow_right_rect.inflate(10, 10), border_radius=5)
        
        # Desenha as setas
        screen.blit(arrow_left, arrow_left_rect.topleft)
        screen.blit(arrow_right, arrow_right_rect.topleft)
        
        # Porta (com efeito hover)
        door_rect.x, door_rect.y = door_positions[room_index]
        if door_locked:
            if door_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, HIGHLIGHT_COLOR, door_rect.inflate(10, 10), border_radius=5)
            screen.blit(locked_door, door_rect.topleft)
        else:
            screen.blit(unlocked_door, door_rect.topleft)
        
        # Destaca gavetas quando o mouse passa sobre elas
        for i, drawer in enumerate(drawer_areas[room_index]):
            drawer_rect = pygame.Rect(drawer)
            if i == hovered_drawer:
                highlight = pygame.Surface((drawer_rect.width, drawer_rect.height), pygame.SRCALPHA)
                highlight.fill(DRAWER_HIGHLIGHT_COLOR)
                screen.blit(highlight, drawer_rect.topleft)
            
            # Borda para tornar as gavetas mais visíveis
            pygame.draw.rect(screen, HIGHLIGHT_COLOR, drawer_rect, 2)
        
        # Mostra contador de chaves coletadas
        keys_count = sum(keys_collected)
        keys_text = small_font.render(f"Chaves: {keys_count}/3", True, WHITE)
        key_icon = small_font.render("🔑", True, WHITE)
        screen.blit(key_icon, (WIDTH - 180, 20))
        screen.blit(keys_text, (WIDTH - 150, 20))
        
        # Mostra em qual cômodo o jogador está
        room_text = small_font.render(f"Cômodo: {room_index + 1}/{len(room_images)}", True, WHITE)
        screen.blit(room_text, (20, 20))

    # Estado DRAWER - Tela de gaveta (vazia ou com mensagem)
    elif current_state == STATE_DRAWER:
        if show_message:
            draw_message()
        else:
            draw_empty_drawer()

    # Estado QUESTION - Tela de pergunta
    elif current_state == STATE_QUESTION:
        draw_question(current_question)

    # Estado DOOR - Tela de interação com a porta
    elif current_state == STATE_DOOR:
        draw_door()

    pygame.display.flip()  # Atualiza a tela
    clock.tick(60)  # Mantém o jogo em 60 FPS

# Encerra o pygame e sai do jogo
pygame.quit()
sys.exit() 