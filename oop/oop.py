class Quadro:
 
    def __init__(self,nomeQuadro,data,autore,coloriDominanti):

        self.nomeQuadro = nomeQuadro
        self.data = data
        self.autore = autore
        self.coloriDominanti = coloriDominanti

    def scheda(self):
        return f'\nScheda "{self.nomeQuadro}"\n nomeQuadro: {self.nomeQuadro}\n data: {self.data}\n autore: {self.autore}\n coloriDominanti: {self.coloriDominanti}'

Gioconda = Quadro("Gioconda","1503","Leonardo Da Vinci","colori caldi e scuri")
Girasoli = Quadro("Girasoli","1888-1889","Van Gogh","giallo")

print("Il tipo di variabile costruita è:")
print(Gioconda)
print(Girasoli)
print("\nLa singola scheda è:")
print (Gioconda.scheda())
print (Girasoli.scheda())
print("\n\naltro metodo per visualizzare le informazioni (__dict__):")
print(Gioconda.__dict__)
print(Girasoli.__dict__)
