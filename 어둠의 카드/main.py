import pygame
import sys
import random

# 파이게임 초기화
pygame.init()

# FPS 설정
clock = pygame.time.Clock()
FPS = 15

# 화면 크기 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 화면 생성
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 게임 이름 설정
pygame.display.set_caption("블랙잭")

# 덱 생성
suits = ["하트", "다이아몬드", "스페이드", "클로버"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

deck = [{"rank": rank, "suit": suit} for suit in suits for rank in ranks]

# 게임 상태
player_hand = []
dealer_hand = []
game_over = False

# 카드 이미지 로드
card_images = {}
for suit in suits:
    for rank in ranks:
        card_image = pygame.image.load(f"images/cards/{suit}_{rank}.png")
        card_images[(rank, suit)] = pygame.transform.scale(card_image, (50, 70))

# 카드 위치
player_card_positions = [(100 + i * 60, 400) for i in range(5)]
dealer_card_positions = [(100 + i * 60, 100) for i in range(5)]

# 폰트 설정
font = pygame.font.Font(None, 36)

# 게임 초기화
def init_game():
    global player_hand, dealer_hand, game_over
    player_hand = []
    dealer_hand = []
    game_over = False
    deal_card(player_hand)
    deal_card(player_hand)
    deal_card(dealer_hand)
    deal_card(dealer_hand)

# 카드 나눠주기
def deal_card(hand):
    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)

# 카드 합계 계산
def hand_value(hand):
    value = 0
    num_aces = 0

    for card in hand:
        rank = card["rank"]
        if rank in ["K", "Q", "J"]:
            value += 10
        elif rank == "A":
            value += 11
            num_aces += 1
        else:
            value += int(rank)

    while num_aces > 0 and value > 21:
        value -= 10
        num_aces -= 1

    return value

# 화면 업데이트
def update_screen():
    screen.fill((0, 102, 0))

    for i, card in enumerate(player_hand):
        rank, suit = card["rank"], card["suit"]
        screen.blit(card_images[(rank, suit)], player_card_positions[i])

    for i, card in enumerate(dealer_hand):
        if not game_over or i > 0:
            rank, suit = card["rank"], card["suit"]
            screen.blit(card_images[(rank, suit)], dealer_card_positions[i])

    player_value = hand_value(player_hand)
    dealer_value = hand_value(dealer_hand)

    player_text = font.render(f"플레이어 합계: {player_value}", True, (255, 255, 255))
    dealer_text = font.render(f"딜러 합계: {dealer_value}", True, (255, 255, 255))
    screen.blit(player_text, (20, 20))
    screen.blit(dealer_text, (20, 60))

    if game_over:
        result_text = font.render(get_game_result(player_value, dealer_value), True, (255, 255, 255))
        restart_text = font.render("R 키로 재시작, Q 키로 종료", True, (255, 255, 255))
        screen.blit(result_text, (400, 300))
        screen.blit(restart_text, (320, 350))

    pygame.display.flip()

# 게임 결과 계산
def get_game_result(player_value, dealer_value):
    if player_value > 21:
        return "플레이어 버스트!"
    elif dealer_value > 21:
        return "딜러 버스트! 플레이어 승리!"
    elif player_value == dealer_value:
        return "무승부!"
    elif player_value > dealer_value:
        return "플레이어 승리!"
    else:
        return "딜러 승리!"

# 게임 초기화
init_game()

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                init_game()
            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    if not game_over:
        player_value = hand_value(player_hand)
        dealer_value = hand_value(dealer_hand)

        if player_value == 21 or dealer_value == 21:
            game_over = True

        update_screen()

    clock.tick(10)

