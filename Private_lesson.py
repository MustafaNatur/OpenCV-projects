#приватные атрибуты или защищиенные переменные
#в питоне нет концепта привоатности и поэтому этот язык базируется на соглашениях
class Character():
    MAX_HEALTH=100 #защищенный атрибут (ИМЕНА КОНСТАНТ ЗАИСЫВАЮТСЯ с CapsLock) это договоренность в python сообществе

    def __init__(self, race, damage = 10):
        self.__race = race
        self.damage = damage


unit = Character('Ork')
unit.__init__('nigga')
print(unit.__race)

# Чтобы закрыть доступ к переменным из вне используется так называемый name mangling
#  (искажение имени) путем следущего синтаксиса---> self.__race = race
#                                                   print(unit.__race)----> error