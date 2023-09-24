import random

# 카드 덱 만들기
suits = ['하트', '다이아몬드', '스페이드', '클로버']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]

# 카드 셔플
random.shuffle(deck)

# 플레이어와 딜러의 손 초기화
player_hand = []
dealer_hand = []

# 카드 한 장을 나눠주는 함수
def deal_card(hand):
    card = deck.pop()
    hand.append(card)

# 핸드의 점수 계산
def calculate_score(hand):
    score = 0
    ace_count = 0  # Ace 카드 수
    for card in hand:
        rank = card['rank']
        if rank == 'A':
            ace_count += 1
            score += 11
        elif rank in ['K', 'Q', 'J']:
            score += 10
        else:
            score += int(rank)
    
    # Ace 카드가 있을 때 점수 계산을 조정
    while ace_count > 0 and score > 21:
        score -= 10
        ace_count -= 1

    return score

# 초기 카드 나눠주기
deal_card(player_hand)
deal_card(dealer_hand)
deal_card(player_hand)

# 게임 진행
while True:
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    print("\n플레이어 카드:", [f"{card['rank']} of {card['suit']}" for card in player_hand], "- 점수:", player_score)
    print("딜러 카드:", [f"{card['rank']} of {card['suit']}" for card in dealer_hand[:1]], "- 점수: ?")

    # 플레이어가 21을 초과하면 패배
    if player_score > 21:
        print("\n플레이어가 21을 초과하여 패배했습니다.")
        break

    # 플레이어가 21에 도달하면 이기기
    if player_score == 21:
        print("\n플레이어가 21에 도달하여 승리했습니다!")
        break

    # 플레이어에게 더 카드를 받을지 물어보기
    choice = input("\n카드를 더 받으시겠습니까? (y/n): ").strip().lower()
    if choice == 'y':
        deal_card(player_hand)
    else:
        # 딜러가 17 이하일 때 카드를 계속 뽑음
        while dealer_score < 17:
            deal_card(dealer_hand)
            dealer_score = calculate_score(dealer_hand)

        print("\n딜러 카드:", [f"{card['rank']} of {card['suit']}" for card in dealer_hand], "- 점수:", dealer_score)

        # 딜러가 21을 초과하면 승리
        if dealer_score > 21:
            print("\n딜러가 21을 초과하여 승리했습니다!")
        elif dealer_score == player_score:
            print("\n무승부!")
        elif dealer_score > player_score:
            print("\n딜러가 이겼습니다!")
        else:
            print("\n플레이어가 이겼습니다!")

        break
