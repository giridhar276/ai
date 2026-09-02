class Person:
    def introduce(self):
        print("I am a person")

class Trainer(Person):
    def teach(self):
        print("I teach Python")

trainer = Trainer()
trainer.introduce()
trainer.teach()
