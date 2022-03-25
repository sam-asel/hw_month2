import os
import random
from envparse import env


class Casino:
    def init(self):
        self.__cash = int(os.environ.get('MY_MONEY'))

        while int(self.__cash) > 0:
            self.__slot = random.randint(1, 30)
            print(self.__slot)
            self.__bet = int(input('Make your bet: '))
            if self.bet > self.cash:
                print('You have not enough money')
            else:
                self.__choice = int(input('Choice the slot: '))

                if self.slot == self.choice:
                    self.cash += self.bet
                    print(f'You win\n Your cash after win: {self.__cash}')
                    if self.slot == self.choice:
                        ans = input('Введите yes для продолжение введите no для выхода: ')
                        if ans == 'yes':
                            continue
                        if ans == 'no':
                            break

                else:
                    self.cash -= self.bet
                    print(f' You lost \n Your cash after lost: {self.__cash}')
                    if self.slot != self.choice:
                        ans = input('Введите yes для продолжение введите no для выхода: ')
                        if ans == 'yes':
                            continue
                        if ans == 'no':
                            break

    @property
    def slot(self):
        return self.__slot

    @slot.setter
    def slot(self, value):
        self.__slot = value


env.read_envfile('settings.env')