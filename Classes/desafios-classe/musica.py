class Música:
    nome = ""
    artista = ""
    duracao = int

djavan = Música()
djavan.nome = "Açai"
djavan.artista = "Djavan"
djavan.duracao = int(2)

paul = Música()
paul.nome = "My Love"
paul.artista = "Paul Mccartney"
paul.duracao = int(3)


print(f"{djavan.nome}, de {djavan.artista}, toca por {djavan.duracao} minutos de groove puro!")
print(f"{paul.nome}, de {paul.artista}, toca por {paul.duracao} minutos de groove puro!")