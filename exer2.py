"""
Для класса Parrot цвет — важный параметр. Расширьте конструктор этого класса так, 
чтобы кроме имени и размера экземпляры класса принимали параметр color, цвет птицы.
Создайте экземпляр класса Parrot и положите его в переменную kesha. Название птицы —  Ара, 
размер — средний, цвет — красный.
Также расширьте конструктор класса Penguin. Экземпляры этого класса должны принимать
 дополнительный параметр genus, вид пингвина.
Создайте экземпляр класса Penguin и положите его в переменную kowalski. 
Название птицы — Королевский, размер — большой, вид — Aptenodytes.
"""

class Bird:
    
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def describe(self):
        return f'Размер птицы {self.name} — {self.size}.'


class Parrot(Bird):

    def __init__(self, name, size, color):
        super().__init__(name, size)
        self.color = color
        

class Penguin(Bird):

    def __init__(self, name, size, genus):
        super().__init__(name, size)
        self.genus = genus


kesha = Parrot('Ара', 'средний', 'красный')
kowalski = Penguin('Королевский','большой','Aptenodytes')
