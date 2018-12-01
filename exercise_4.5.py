class Spell:
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation
    def __str__(self):
        return self.name +""+ self.incantation + "\n"+ self.get_description()
    def get_description(self):
        return "no description"
    def execute(self):
        print(self.incantation)

class Accio(Spell):
    def __init__(self):
        Spell.__init__(self,"Accio","Summoning Charm")
    def get_description(self):
        return "this charm does something"
    def spelltoo():
        print(spell)

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self,"Confundo","confundus charm")

    def get_description(self):
        return "causs the victim to become confused and befudddled"

def study_spell(spell):
    print(spell)

spell = Accio()
spell.execute()
print("end spell.execute()")
study_spell(spell)
print("end of study_spell(spell")
study_spell(Confundo())
print("end of study_spell(Confundo())")
print(Accio())
print("This is where my code begins")
Accio.spelltoo()
