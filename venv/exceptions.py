class GameOver(Exception):
    '''
    Call this exception to and the game
    '''

    def __int__(self, player):
        super().__init__()
        self.player = player

    @staticmethod
    def save_score(self):
        '''
        Save score to "scores.txt"
        '''
        file = open('scores.txt', 'a')
        row = f'{self.name}: {self.score}\n'
        file.write(row)


class EnemyDown(Exception):
    '''
    Call this exception when our enemy down
    '''

    def __int__(self):
        super().__init__()
