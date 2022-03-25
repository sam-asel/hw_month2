import random

round_number = 0


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value > 0:
            self.__health = value
        else:
            self.__health = 0

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} Health: {self.__health} ' \
               f'[{self.__damage}]'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        GameEntity.__init__(self, name, health, damage)


class Hero(GameEntity):
    def __init__(self, name, health, damage, skill):
        GameEntity.__init__(self, name, health, damage)
        self.__skill = skill

    @property
    def skill(self):
        return self.__skill

    @skill.setter
    def skill(self, value):
        self.__skill = value

    def apply_super_power(self, boss, heroes):
        raise NotImplementedError("Must be implemented")


class Warrior(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, "CRITICAL DAMAGE")

    def apply_super_power(self, boss, heroes):
        coeff = random.randint(2, 5)
        boss.health = boss.health - coeff * self.damage
        print(f'{self.name} hit critically: {coeff * self.damage}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, "BOOST")

    def apply_super_power(self, boss, heroes):
        if round_number % 2 == 0:
            boost = random.randint(5, 10)
            for h in heroes:
                if h.health > 0:
                    h.damage += boost


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        Hero.__init__(self, name, health, damage, "HEAL")
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for h in heroes:
            if h.health > 0 and self != h:
                h.health = h.health + self.__heal_points


class Berserk(Hero):
    def __init__(self, name, health, damage):
        Hero.__init__(self, name, health, damage, "SAVE DAMAGE AND RETURN")

    def apply_super_power(self, boss, heroes):
        range = [5, 10, 15]
        saved = random.choice(range)
        self.health += saved
        boss.health -= saved


def start():
    boss = Boss("Dark Wider", 1500, 50)

    warrior = Warrior("Ahiles", 270, 15)
    medic_1 = Medic("Elis", 200, 5, 15)
    magic = Magic("Merlin", 280, 30)
    berserk = Berserk("John", 250, 10)
    medic_2 = Medic("Aibolit", 230, 10, 5)
    heroes = [warrior, medic_1, magic, berserk, medic_2]

    print_stats(boss, heroes)

    while (not is_game_finished(boss, heroes)):
        play_round(boss, heroes)


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss_hits(boss, heroes)
    heroes_hit(boss, heroes)
    heroes_skills(boss, heroes)
    print_stats(boss, heroes)


def boss_hits(boss, heroes):
    for h in heroes:
        if h.health > 0 and boss.health > 0:
            h.health = h.health - boss.damage


def heroes_hit(boss, heroes):
    for h in heroes:
        if h.health > 0 and boss.health > 0:
            boss.health = boss.health - h.damage


def heroes_skills(boss, heroes):
    for h in heroes:
        if h.health > 0 and boss.health > 0:
            h.apply_super_power(boss, heroes)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print("Heroes won!!!")
        return True

    all_heroes_dead = True
    for h in heroes:
        if h.health > 0:
            all_heroes_dead = False
            break

    if all_heroes_dead:
        print("Boss won!!!")

    return all_heroes_dead


def print_stats(boss, heroes):
    print("------------- ROUND: " + str(round_number) + " -------------")
    print(boss)
    for h in heroes:
        print(h)


start()
