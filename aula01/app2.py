class Ninja:
    def __init__(self, nacao, vila):
        self.nacao = nacao
        self.vila = vila
        
    def atacar(self):
        print("Joga Shuriken!")

    def defesa(self):
        return "Jutsu substituição!"


class Ambu(Ninja):
    def __init__(self, nacao, vila, especialidade):
        super().__init__(nacao, vila)
        self.especialidade = especialidade



n1 = Ninja("Fogo", "Folha")

print(f"De onde veio o ninja? {n1.nacao} e {n1.vila}")
n1.atacar()
print(n1.defesa())


print("-" * 40)


a1 = Ambu("Montanha", "Folha", "Água")

print(f"De onde veio o ninja? {a1.nacao} e {a1.vila}")
print(f"Qual é a especialidade dele? {a1.especialidade}")
a1.atacar()
print(a1.defesa())

    