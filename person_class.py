class Person:
    def __init__(self, name, fav_dialogue):
        self.name = name
        self.fav_dialogue = fav_dialogue

    def talk(self):
        print(self.fav_dialogue)


person = Person('Ammar', 'Let us demonstrate....')
person.talk()
