class Solution:
    def judgeCircle(self, moves: str) -> bool:
        position = {
            "x":0,
            "y":0
         }
        moves=list(moves)
        for dirr in moves:
            if dirr=="L":
                position["x"] -= 1
            elif dirr=="R":
                position["x"] += 1 
            elif dirr=="D":
                position["y"] -= 1
            else:
                position["y"] += 1
        for key,value in position.items():
            if value != 0:
                return False
        return True
                