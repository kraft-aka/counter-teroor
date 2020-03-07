''' Реализовать классы Сounter, Terrorists которые наследуются от класса Role у которого есть
 переменные экземпляра как team(должен быть списком), name, guns(должен быть списком)
 и hp(int), points.
Релизовать класс Gun, у которого есть поля экземпляра класса как name, damage.


В классе Role, сделать метод fire, который принимает в аргументы gun_obj,
opponent_obj и отнимает hp от opponent_obj в зависимости от урона gun_obj и
 добавляет points для того кто убил. Помните, что люди не могут убивать своих сокомандников.

Подумайте, где можно использовать Миксины'''


class Role:
    def __init__(self,name, team):
        self.name = name
        self.points = 0
        self.team = team
        self.guns = []
        self.hp = 100
        self.is_dead = False

    def fire(self, gun_obj, opponent_obj):
        if opponent_obj.team != self.team:
            damage = gun_obj.damage
            opponent_obj.hp -= damage
            self.points += 10
            if opponent_obj.hp <= 0:
                opponent_obj.is_dead = True
                print(f"{opponent_obj.name} is killed by {self.name} with {gun_obj.name}")
        else:
            return "You cannot fire to your friend"


class Counter(Role):
    def __init__(self, name):
        self.team = "counter"
        super().__init__(name, team=self.team)


class Terrorist(Role):
    def __init__(self, name):
        self.team = "terrorist"
        super().__init__(name, team=self.team)


class Gun:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


# class Snipers(Gun):


counter = Counter("achi")
counter2 = Counter("bot")
terror = Terrorist("kubat")
gun1 = Gun("kalashnikov", 25)
gun2 = Gun("eagle", 15)

counter.fire(gun1, terror)
counter.fire(gun1, terror)
counter.fire(gun1, terror)
counter.fire(gun1, terror)
print(terror.hp)
print(terror.is_dead)


