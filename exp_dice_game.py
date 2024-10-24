import random


class Dice:


    # constructor
    def __init__(self, max_score, color="Red"):
        self.max_score = max_score
        self.color = color

    # throw the dice
    def throw_dice(self):
        possible_scores = range(1, self.max_score + 1)
        result = random.choice(possible_scores)
        print(f"🎲 {result}")
        return result


class Game:
    

    def __init__(self, 
                 max_turns: int, 
                 dice: Dice
                 ):
        self.max_turns = max_turns
        self.dice = dice
        self.scores = []
        self.current_turn = 1
        self.total_score = 0


    def take_turn(self):
        if self.current_turn <= self.max_turns:
            dice_result = self.dice.throw_dice()
            self.scores.append(dice_result)
            self.current_turn += 1

            current_score = self.calc_total_score()
            print(f"Current score: {current_score}")
        else:
            print("Game is already over")

    def reset(self):
        self.current_turn = 1
        self.scores = []
        self.total_score = 0

    
    def calc_total_score(self):
        total_score = sum(self.scores)
        self.total_score = total_score
        return total_score


    def __repr__(self) -> str:
        description = f"""
                      Game:

                      Turn: {self.current_turn}
                      Scores: {self.scores}
                      Current score: {self.total_score}
                      """
        
        return description
    


# define the Game
my_dice = Dice(10)
my_game = Game(5, my_dice)



pass