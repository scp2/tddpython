from leilao.dominio import Usuario, Lance, Leilao

user1 = Usuario('User 1')
user2 = Usuario('User 2')

lance_user1 = Lance(user1, 100)
lance_user2 = Lance(user2, 150)

leilao = Leilao('Test')

leilao.lances.append(lance_user1)
leilao.lances.append(lance_user2)

for lance in leilao.lances:
    print(f'O usuário {lance.usuario.nome} deu um lance de {lance.valor}')