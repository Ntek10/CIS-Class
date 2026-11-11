#M9p2.py    Nick     11/01/2026

def computeBattingAverage(hits, atBats):
    if atBats == 0:
        return 0.0
    return hits / atBats

playerCount = 0

while True:
    lastName = input("Enter player's last name (or 'q' to quit): ")
    if lastName.lower() == 'q':
        break
    hits = int(input("Enter number of hits: "))
    atBats = int(input("Enter number of at bats: "))
    
    battingAvg = computeBattingAverage(hits, atBats)
    playerCount += 1
    
    print(f"Player: {lastName} | Batting Average: {battingAvg:.3f}\n")

print(f"\nTotal number of players entered: {playerCount}")
