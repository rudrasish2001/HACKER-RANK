def minion_game(string):
    vowels = 'AEIOU'
    str_len = len(string)
    player1, player2 = 0, 0
    for i in range(str_len):
        if s[i] in vowels:
            player1 += (str_len-i)
        else:
            player2 += (str_len-i)
    
    if player1 > player2:
        print("Kevin" , player1)
    elif player1 < player2:
        print("Stuart", player2)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)