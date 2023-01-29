class Bird:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def describe(self, full=False):
        return f'Размер птицы {self.name} — {self.size}.'


class Parrot(Bird):
    def __init__(self, name, size, color):
        super().__init__(name, size)
        self.color = color
    # Переопределите метод describe().
    
    def describe(self, full=False):
        if full == True:
            return (
                   f'Попугай {self.name} — заметная птица, окрас её перьев — {self.color}, а '
                   f'размер — {self.size}. Интересный факт: попугаи чувствуют ритм, а '
                   f'вовсе не бездумно двигаются под музыку. Если сменить '
                   f'композицию, то и темп движений птицы изменится.')
        else:
            return super().describe()
            
        

class Penguin(Bird):
    def __init__(self, name, size, genus):
        super().__init__(name, size)
        self.genus = genus
    # Переопределите метод describe().
    
    def describe(self, full=False):
        if full == True:
            return (
                   f'Размер пингвина {self.name} из рода {self.genus} — {self.size}. Интересный факт: '
                   f'однажды группа геологов-разведчиков похитила пингвинье яйцо, '
                   f'и их принялась преследовать вся стая, не пытаясь, впрочем, при ' 
                   f'этом нападать. Посовещавшись, похитители вернули птицам яйцо, '
                   f'и те отстали.')
        else:
            return super().describe()
        


kesha = Parrot('Ара', 'средний', 'красный')
kowalski = Penguin('Королевский', 'большой', 'Aptenodytes')

# Вызов метода у созданных объектов.
print(kesha.describe())
print(kowalski.describe(True))
