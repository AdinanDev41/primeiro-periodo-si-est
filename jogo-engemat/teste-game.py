import pygame
import sys
import random

pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Missão Lógica")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PAPER_COLOR = (250, 250, 240)
BUTTON_COLOR = (100, 100, 250)
BUTTON_HOVER_COLOR = (150, 150, 255)
BUTTON_ALPHA = 180
BACK_BUTTON_COLOR = (200, 0, 0)
BACK_BUTTON_HOVER_COLOR = (255, 50, 50)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
HIGHLIGHT_COLOR = (255, 255, 0)
DRAWER_HIGHLIGHT_COLOR = (255, 200, 0, 150)
TRANSPARENT = (0, 0, 0, 0)

# Fontes
title_font = pygame.font.SysFont("arial", 48, bold=True)
text_font = pygame.font.SysFont("arial", 24)
small_font = pygame.font.SysFont("arial", 20)
button_font = pygame.font.SysFont("arial", 22, bold=True)

# Estados do jogo
STATE_MENU = "menu"
STATE_EXPLANATION = "explanation"
STATE_GAME = "game"
STATE_DRAWER = "drawer"
STATE_QUESTION = "question"
STATE_DOOR = "door"
current_state = STATE_MENU

# Imagens (substitua pelos seus arquivos reais)
try:
    bg_menu = pygame.image.load("fundo-tela.jpeg")
    bg_menu = pygame.transform.scale(bg_menu, (WIDTH, HEIGHT))
    
    game_rooms = ["inicio.jpg", "cozinha.jpg", "sala.jpg"]
    room_images = []
    for img in game_rooms:
        try:
            room_img = pygame.image.load(img)
            room_images.append(pygame.transform.scale(room_img, (WIDTH, HEIGHT)))
        except:
            fallback = pygame.Surface((WIDTH, HEIGHT))
            fallback.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            room_images.append(fallback)
    
    arrow_left = pygame.transform.scale(pygame.image.load("seta-esquerda.png"), (60, 60))
    arrow_right = pygame.transform.scale(pygame.image.load("seta-direita.png"), (60, 60))
    
    try:
        locked_door = pygame.transform.scale(pygame.image.load("cadeado-fechado.png"), (100, 100))
        unlocked_door = pygame.transform.scale(pygame.image.load("cadeado-aberto.png"), (100, 100))
    except:
        locked_door = pygame.Surface((100, 100))
        locked_door.fill(RED)
        unlocked_door = pygame.Surface((100, 100))
        unlocked_door.fill(GREEN)
except Exception as e:
    print(f"Erro ao carregar imagens: {e}")
    sys.exit()

# Áreas interativas (gavetas) para cada cômodo - agora mais visíveis
drawer_areas = [
    [(200, 300, 120, 60), (400, 250, 120, 60)],  # Cômodo 0 (largura aumentada para 120)
    [(150, 350, 120, 60), (500, 300, 120, 60)],  # Cômodo 1
    [(300, 400, 120, 60), (600, 350, 120, 60)]   # Cômodo 2
]

# Porta em cada cômodo
door_positions = [
    (700, 400),  # Cômodo 0
    (700, 350),  # Cômodo 1
    (700, 300)   # Cômodo 2
]

# Questões para cada gaveta em cada cômodo (focando apenas em "e", "ou" e "não")
questions = [
    [  # Cômodo 0
        {
            "question": "Se A é verdadeiro e B é falso, qual o valor de 'A e B'?",
            "options": ["Verdadeiro", "Falso"],
            "answer": 1,
            "key": True,
            "explanation": "'A e B' só é verdadeiro quando ambos são verdadeiros."
        },
        {
            "question": "Se A é falso, qual o valor de 'não A'?",
            "options": ["Verdadeiro", "Falso"],
            "answer": 0,
            "key": False,
            "explanation": "A negação inverte o valor lógico."
        }
    ],
    [  # Cômodo 1
        {
            "question": "Se A é verdadeiro ou B é falso, qual o valor se ambos forem verdadeiros?",
            "options": ["Verdadeiro", "Falso"],
            "answer": 0,
            "key": True,
            "explanation": "Basta um ser verdadeiro para 'ou' ser verdadeiro."
        },
        {
            "question": "Se 'não A' é falso, qual o valor de A?",
            "options": ["Verdadeiro", "Falso"],
            "answer": 0,
            "key": False,
            "explanation": "Se a negação é falsa, o original é verdadeiro."
        }
    ],
    [  # Cômodo 2
        {
            "question": "'A e B' é verdadeiro somente quando:",
            "options": ["A ou B é verdadeiro", "A e B são verdadeiros", "A é falso"],
            "answer": 1,
            "key": True,
            "explanation": "O operador 'e' requer que ambos sejam verdadeiros."
        },
        {
            "question": "'A ou B' é falso quando:",
            "options": ["A é falso", "B é falso", "Ambos são falsos"],
            "answer": 2,
            "key": False,
            "explanation": "'Ou' só é falso quando ambos operandos são falsos."
        }
    ]
]

# Variáveis de jogo
room_index = 0
current_drawer = None
current_question = None
keys_collected = [False, False, False]
door_locked = True
show_message = False
message_text = ""
game_won = False
hovered_drawer = None
hovered_button = None

# Retângulos para os botões
cela_button_rect = pygame.Rect(WIDTH // 2 - 120, HEIGHT // 2 - 100, 240, 70)
back_button_rect = pygame.Rect(20, 20, 100, 40)
continue_button_rect = pygame.Rect(WIDTH - 150, HEIGHT - 70, 130, 50)
arrow_left_rect = pygame.Rect(30, HEIGHT // 2 - 30, 60, 60)
arrow_right_rect = pygame.Rect(WIDTH - 90, HEIGHT // 2 - 30, 60, 60)
door_rect = pygame.Rect(0, 0, 120, 120)  # Aumentado para ficar mais visível

def draw_button(rect, text, color, hover_color=None, hover=False):
    """Função auxiliar para desenhar botões com efeito hover"""
    if hover and hover_color:
        pygame.draw.rect(screen, hover_color, rect, border_radius=8)
    else:
        pygame.draw.rect(screen, color, rect, border_radius=8)
    
    # Adiciona borda para melhor visibilidade
    pygame.draw.rect(screen, BLACK, rect, 2, border_radius=8)
    
    button_text = button_font.render(text, True, WHITE)
    screen.blit(button_text, (
        rect.centerx - button_text.get_width() // 2,
        rect.centery - button_text.get_height() // 2
    ))

def draw_explanation():
    screen.fill(PAPER_COLOR)

    title = title_font.render("CONECTIVOS LÓGICOS", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 40))

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

    y_offset = 120
    for line in lines:
        text = text_font.render(line, True, BLACK)
        screen.blit(text, (60, y_offset))
        y_offset += 35 if line else 20

    # Botão Voltar com efeito hover
    draw_button(back_button_rect, "Voltar", BACK_BUTTON_COLOR, BACK_BUTTON_HOVER_COLOR, 
               back_button_rect.collidepoint(pygame.mouse.get_pos()))

    # Botão Continuar com efeito hover
    draw_button(continue_button_rect, "Continuar", BUTTON_COLOR, BUTTON_HOVER_COLOR,
               continue_button_rect.collidepoint(pygame.mouse.get_pos()))

def draw_empty_drawer():
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    screen.blit(overlay, (0, 0))
    
    message = text_font.render("Esta gaveta está vazia!", True, WHITE)
    screen.blit(message, (WIDTH // 2 - message.get_width() // 2, HEIGHT // 2 - 50))
    
    # Botão Voltar com efeito hover
    draw_button(back_button_rect, "Voltar", BACK_BUTTON_COLOR, BACK_BUTTON_HOVER_COLOR,
               back_button_rect.collidepoint(pygame.mouse.get_pos()))

def draw_question(question_data):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    screen.blit(overlay, (0, 0))
    
    # Título da questão
    question_title = title_font.render("Desafio Lógico", True, HIGHLIGHT_COLOR)
    screen.blit(question_title, (WIDTH // 2 - question_title.get_width() // 2, HEIGHT // 2 - 180))
    
    # Texto da questão
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
    
    for i, line in enumerate(question_lines):
        question_text = text_font.render(line, True, WHITE)
        screen.blit(question_text, (WIDTH // 2 - question_text.get_width() // 2, HEIGHT // 2 - 120 + i * 30))
    
    # Opções de resposta
    option_rects = []
    for i, option in enumerate(question_data["options"]):
        option_rect = pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2 - 50 + i * 70, 400, 60)
        option_rects.append(option_rect)
        
        # Efeito hover para opções
        hover = option_rect.collidepoint(pygame.mouse.get_pos())
        draw_button(option_rect, option, BUTTON_COLOR, BUTTON_HOVER_COLOR, hover)
    
    return option_rects

def draw_message():
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    screen.blit(overlay, (0, 0))
    
    # Mensagem principal
    message = text_font.render(message_text, True, WHITE)
    screen.blit(message, (WIDTH // 2 - message.get_width() // 2, HEIGHT // 2 - 50))
    
    # Exibir explicação se disponível
    if current_question and "explanation" in current_question and "Resposta correta" in message_text:
        explanation = text_font.render(current_question["explanation"], True, GREEN)
        screen.blit(explanation, (WIDTH // 2 - explanation.get_width() // 2, HEIGHT // 2 + 10))
    
    # Botão Voltar com efeito hover
    draw_button(back_button_rect, "Voltar", BACK_BUTTON_COLOR, BACK_BUTTON_HOVER_COLOR,
               back_button_rect.collidepoint(pygame.mouse.get_pos()))

def draw_door():
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    screen.blit(overlay, (0, 0))
    
    all_keys_collected = all(keys_collected)
    
    if door_locked:
        if all_keys_collected:
            message = text_font.render("Você coletou todas as chaves! A porta pode ser aberta.", True, GREEN)
            screen.blit(message, (WIDTH // 2 - message.get_width() // 2, HEIGHT // 2 - 100))
            
            # Botão de abrir porta com efeito hover
            draw_button(continue_button_rect, "Abrir Porta", GREEN, (0, 255, 0),
                       continue_button_rect.collidepoint(pygame.mouse.get_pos()))
        else:
            keys_needed = sum(1 for key in keys_collected if not key)
            message = text_font.render(f"Porta trancada! Faltam {keys_needed} chaves.", True, RED)
            screen.blit(message, (WIDTH // 2 - message.get_width() // 2, HEIGHT // 2 - 50))
            
            # Mostrar status das chaves
            for i, key in enumerate(keys_collected):
                key_text = small_font.render(f"Cômodo {i+1}: {'✔' if key else '✖'}", 
                                          True, GREEN if key else RED)
                screen.blit(key_text, (WIDTH // 2 - 100, HEIGHT // 2 + 20 + i * 30))
    else:
        message = title_font.render("PARABÉNS! VOCÊ ESCAPOU!", True, GREEN)
        screen.blit(message, (WIDTH // 2 - message.get_width() // 2, HEIGHT // 2 - 100))
        
        sub_message = text_font.render("Você resolveu todos os desafios lógicos!", True, WHITE)
        screen.blit(sub_message, (WIDTH // 2 - sub_message.get_width() // 2, HEIGHT // 2 - 30))
    
    # Botão Voltar com efeito hover
    draw_button(back_button_rect, "Voltar", BACK_BUTTON_COLOR, BACK_BUTTON_HOVER_COLOR,
               back_button_rect.collidepoint(pygame.mouse.get_pos()))

# Loop principal do jogo
clock = pygame.time.Clock()
running = True

while running:
    mouse_pos = pygame.mouse.get_pos()
    hovered_drawer = None
    hovered_button = None
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if current_state == STATE_MENU and cela_button_rect.collidepoint(event.pos):
                current_state = STATE_EXPLANATION

            elif current_state == STATE_EXPLANATION:
                if back_button_rect.collidepoint(event.pos):
                    current_state = STATE_MENU
                elif continue_button_rect.collidepoint(event.pos):
                    current_state = STATE_GAME

            elif current_state == STATE_GAME:
                # Verificar cliques nas gavetas
                for i, drawer in enumerate(drawer_areas[room_index]):
                    drawer_rect = pygame.Rect(drawer)
                    if drawer_rect.collidepoint(event.pos):
                        current_drawer = i
                        current_state = STATE_QUESTION
                        current_question = questions[room_index][current_drawer]
                
                # Verificar clique na porta
                door_rect.x, door_rect.y = door_positions[room_index]
                if door_rect.collidepoint(event.pos):
                    current_state = STATE_DOOR
                
                # Verificar setas de navegação
                if arrow_left_rect.collidepoint(event.pos):
                    room_index = (room_index - 1) % len(room_images)
                elif arrow_right_rect.collidepoint(event.pos):
                    room_index = (room_index + 1) % len(room_images)

            elif current_state == STATE_DRAWER and back_button_rect.collidepoint(event.pos):
                current_state = STATE_GAME
                show_message = False

            elif current_state == STATE_QUESTION:
                option_rects = draw_question(current_question)
                for i, rect in enumerate(option_rects):
                    if rect.collidepoint(event.pos):
                        if i == current_question["answer"]:
                            message_text = "Resposta correta!"
                            if current_question["key"]:
                                keys_collected[room_index] = True
                                message_text += " Você encontrou uma chave!"
                        else:
                            message_text = "Resposta incorreta. Tente novamente!"
                        
                        current_state = STATE_DRAWER
                        show_message = True

            elif current_state == STATE_DOOR:
                if back_button_rect.collidepoint(event.pos):
                    current_state = STATE_GAME
                elif continue_button_rect.collidepoint(event.pos) and all(keys_collected):
                    door_locked = False
                    game_won = True

    # Verificar hover sobre elementos interativos
    if current_state == STATE_GAME:
        for i, drawer in enumerate(drawer_areas[room_index]):
            drawer_rect = pygame.Rect(drawer)
            if drawer_rect.collidepoint(mouse_pos):
                hovered_drawer = i
                break
    
    # Desenhar o estado atual
    screen.fill(BLACK)
    
    if current_state == STATE_MENU:
        screen.blit(bg_menu, (0, 0))
        title = title_font.render("Missão Lógica", True, WHITE)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))
        
        # Efeito hover para o botão principal
        hover = cela_button_rect.collidepoint(mouse_pos)
        draw_button(cela_button_rect, "Explorar Casa", BUTTON_COLOR, BUTTON_HOVER_COLOR, hover)

    elif current_state == STATE_EXPLANATION:
        draw_explanation()

    elif current_state == STATE_GAME:
        screen.blit(room_images[room_index], (0, 0))
        
        # Desenhar setas de navegação com efeito hover
        hover_left = arrow_left_rect.collidepoint(mouse_pos)
        hover_right = arrow_right_rect.collidepoint(mouse_pos)
        
        if hover_left:
            pygame.draw.rect(screen, HIGHLIGHT_COLOR, arrow_left_rect.inflate(10, 10), border_radius=5)
        if hover_right:
            pygame.draw.rect(screen, HIGHLIGHT_COLOR, arrow_right_rect.inflate(10, 10), border_radius=5)
        
        screen.blit(arrow_left, arrow_left_rect.topleft)
        screen.blit(arrow_right, arrow_right_rect.topleft)
        
        # Desenhar porta (trancada ou destrancada) com efeito hover
        door_rect.x, door_rect.y = door_positions[room_index]
        if door_locked:
            if door_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, HIGHLIGHT_COLOR, door_rect.inflate(10, 10), border_radius=5)
            screen.blit(locked_door, door_rect.topleft)
        else:
            screen.blit(unlocked_door, door_rect.topleft)
        
        # Destacar gavetas quando o mouse passa sobre elas
        for i, drawer in enumerate(drawer_areas[room_index]):
            drawer_rect = pygame.Rect(drawer)
            if i == hovered_drawer:
                highlight = pygame.Surface((drawer_rect.width, drawer_rect.height), pygame.SRCALPHA)
                highlight.fill(DRAWER_HIGHLIGHT_COLOR)
                screen.blit(highlight, drawer_rect.topleft)
            
            # Desenhar borda para tornar as gavetas mais visíveis
            pygame.draw.rect(screen, HIGHLIGHT_COLOR, drawer_rect, 2)
        
        # Mostrar contador de chaves com ícone
        keys_count = sum(keys_collected)
        keys_text = small_font.render(f"Chaves: {keys_count}/3", True, WHITE)
        key_icon = small_font.render("🔑", True, WHITE)
        screen.blit(key_icon, (WIDTH - 180, 20))
        screen.blit(keys_text, (WIDTH - 150, 20))
        
        # Mostrar em qual cômodo o jogador está
        room_text = small_font.render(f"Cômodo: {room_index + 1}/{len(room_images)}", True, WHITE)
        screen.blit(room_text, (20, 20))

    elif current_state == STATE_DRAWER:
        if show_message:
            draw_message()
        else:
            draw_empty_drawer()

    elif current_state == STATE_QUESTION:
        draw_question(current_question)

    elif current_state == STATE_DOOR:
        draw_door()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()