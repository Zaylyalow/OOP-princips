"""
Опишите на ООП взаимодействие студента, ментора, код-ревьюера и куратора. 
Все эти люди — люди, поэтому создадим базовый класс Human со свойством name 
(у каждого человека должно быть имя) и методом answer_question() для ответов на вопросы.
По умолчанию объект Human будет отвечать на любой вопрос так: «Очень интересный вопрос! Не знаю.»
От класса Human унаследуем классы Student, Mentor, CodeReviewer и Curator. 
Student должен уметь задавать вопросы. 
Реализуйте в классе Student метод ask_question(Human, question). При вызове этот метод должен:
1. Напечатать на экране вопрос в формате <имя человека, которому задаём вопрос>, <текст вопроса>
2. Задать вопрос question человеку, объекту класса Human. Имя объекта, которому адресован вопрос, 
передаётся при вызове метода ask_question().
Объекты классов Mentor, CodeReviewer и Curator должны уметь отвечать на вопросы при вызове 
метода answer_question(). Задан непредусмотренный вопрос — для него подойдёт ответ по умолчанию.
После того как вы допишете код, ваша программа должна вывести на экран такой текст:
Марина, мне грустненько, что делать?
Держись, всё получится. Хочешь видео с котиками?

Ира, мне грустненько, что делать?
Отдохни и возвращайся с вопросами по теории.

Евгений, когда каникулы?
Очень интересный вопрос! Не знаю.

Евгений, что не так с моим проектом?
О, вопрос про проект, это я люблю.

Виталя, как устроиться на работу питонистом?
Очень интересный вопрос! Не знаю.

Ира, как устроиться работать питонистом?
Сейчас расскажу. 
"""
class Human:
    def __init__(self, name):
        self.name = name

    def answer_question(self, question): # не изменять
        print('Очень интересный вопрос! Не знаю.')

class Student(Human):
    def ask_question(self, someone, question):
            print(f'{someone.name}, {question}')
            someone.answer_question(question)
            print()

class Curator(Human):    
    def answer_question(self, question):
        if question == 'мне грустненько, что делать?':
            print('Держись, всё получится. Хочешь видео с котиками?')
        else:
            super().answer_question(question)
            
class CodeReviewer(Human):   
    def answer_question(self, question):
        if question == 'что не так с моим проектом?':
            print('О, вопрос про проект, это я люблю.')
        else:
            super().answer_question(question) 

        
class Mentor(Human):
    def answer_question(self, question):
        if question == 'как устроиться работать питонистом?':
            print('Сейчас расскажу.')
        elif question == 'мне грустненько, что делать?':
            print('Отдохни и возвращайся с вопросами по теории.')
        else:
            super().answer_question(question) 

            
student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')
friend = Human('Виталя')


student1.ask_question(curator, 'мне грустненько, что делать?')
student1.ask_question(mentor, 'мне грустненько, что делать?')
student1.ask_question(reviewer, 'когда каникулы?')
student1.ask_question(reviewer, 'что не так с моим проектом?')
student1.ask_question(friend, 'как устроиться на работу питонистом?')
student1.ask_question(mentor, 'как устроиться работать питонистом?')