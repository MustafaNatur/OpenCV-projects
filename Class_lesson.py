##############################################################################################################
                                               ## Классы в питоне ##
                                               #####################
# классы позволяют разделять объекты либо их пораждать. Пример с собаками породами и их именами
#Синтаксис. Важно, что в названии класса каждое новое слово начинается с заглавной буквы
#создание экземпляра класса
# У каждго класса есть констурктор который позволяет не создовать экземпляры в невалидном состоянии
###############################################################################################################
class Person():
    def set(self, race, name, age): #аргументы self-это аргумент, передающий экзмепляр класса (болванка класса)
        self.race = race           # def - это так называемый метод
        self.age = age
        self.name = name
ivan = Person()
ivan.set('Nigger', 'ivan', 12)
##############################################################################################################
# Попробуем написать программу для дамажа персонажа в игре и повторим материаол еще раз

class Unit():                             #Объявдение имени класса

    def set(self, race, name, health):    #создание метода и введение переменных
        self.name = name                  #собственно переменные
        self.race = race                  #собственно переменные
        self.health = health              #собственно переменные

    def hit(self, damage):
        self.health = self.health - damage

Ork=Unit()                                #Создание элемента класса

Ork.set("Nigger", "Oliver", 100 )         #Определение аргументов для элементов класса
Ork.hit(10)
print(Ork.health)                         #Вывод результатов)
###########################################################################################################