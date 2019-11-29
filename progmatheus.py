import os
from peewee import *
db = SqliteDatabase ("CampeonatoFutebol.db")

class BaseModel(Model):
    class Meta:
        database = db


class Socio_torcedor(BaseModel):
    nome = CharField()
    idade = CharField()
    time = CharField()
    assinatura = CharField()
    tempo_como_socio = CharField()

    def __str__(self):
        return("Nome do sócio torcedor: " + self.nome + "\n" + "Idade: " + self.idade + "\n" + "Time: " + self.time + "\n" + "Assinatura: " + self.assinatura + "\n" + "Tempo como sócio: " + self.tempo_como_socio)


class Tecnico(BaseModel):
    nome = CharField()
    idade = CharField()
    time_atual = CharField()
    titulos = CharField()
    primeiro_time = CharField()

    def __str__(self):
        return("Nome do técnico: " + self.nome + "\n" + "Idade: " + self.idade + "\n" + "Time atual: " + self.time_atual + "\n" + "Titulos: " + self.titulos + "\n" + "Primeiro time: " + self.primeiro_time)


class Jogador(BaseModel):
    nome = CharField()
    time = CharField()
    idade = CharField()
    tempo_time = CharField()
    primeiro_time = CharField()
    titulos = CharField()
    gols = CharField()
    assistencias = CharField()
    cartoes_vermelhos = CharField()
    cartoes_amarelos = CharField()

    def __str__(self):
        return("Nome do jogador: " + self.nome + "\n" + "Time: " + self.time + "\n" + "Idade: " + self.idade + "\n" + "Tempo no time: " + self.tempo_time + "\n" + "Primeiro time: " + self.primeiro_time + "\n" + "Titulos: " + self.titulos + "\n" + "Gols: " + self.gols + "\n" + "Assistencias: " + self.assistencias + "\n" + "Cartões vermelhos: " + self.cartoes_vermelhos + "\n" + "Cartões amarelos: " + self.cartoes_amarelos)


class Estadio(BaseModel):
    nome = CharField()
    capacidade_max = CharField()
    cidade = CharField()
    tipo_gramado = CharField()
    recorde_publico = CharField()

    def __str__(self):
        return("Nome do estadio: " + self.nome + "\n" + "Capacidade máxima: " + self.capacidade_max + "\n" + "Cidade: " + self.cidade + "\n" + "Tipo do gramado: " + self.tipo_gramado + "\n" + "Recorde de público: " + self.recorde_publico)


class Time(BaseModel):
    nome = CharField()
    tecnico = ForeignKeyField(Tecnico)
    jogadores = ForeignKeyField(Jogador)
    estadio = ForeignKeyField(Estadio)
    socio_torcedor = ForeignKeyField(Socio_torcedor)

    def __str__(self):
        return("Nome do time: " + self.nome + "\n" + str(self.tecnico) + "\n" + "\n" + str(self.jogadores) + "\n" + "\n" + str(self.estadio) + "\n" + "\n" + str(self.socio_torcedor)) 


class Campeonato(BaseModel):
    nome = CharField()
    pontuacao = CharField()
    colocacao = CharField()
    quantidade_rodadas = CharField()
    time = ForeignKeyField(Time)
    quantidade_times_participantes = CharField()

    def __str__(self):
        return("\n" + "Nome do campeonato: " + self.nome + "\n" + "Pontuação: " + self.pontuacao + "\n" + "Colocação: " + self.colocacao + "\n" + "Quantidade de rodadas: " + self.quantidade_rodadas + "\n" + "\n" + str(self.time) + "\n" + "Quantidade de times participantes: " + self.quantidade_times_participantes)


class Arbitro(BaseModel):
    nome = CharField()
    idade = CharField()
    funcao = CharField()
    associacao = CharField()

    def __str__(self):
        return("Nome do arbitro: " + self.nome + "\n" + "Idade: " + self.idade + "\n" + "Função: " + self.funcao + "\n" + "Associacao: " + self.associacao)


class Produto(BaseModel):
    camisa = CharField()
    bebida = CharField()
    comida = CharField()
    lembrancinha = CharField()

    def __str__(self):
        return("Camisa: " + self.camisa + "\n" + "Bebida: " + self.bebida + "\n" + "Comida: " + self.comida + "\n" + "Lembrancinha" + self.lembrancinha)


class Narrador(BaseModel):
    nome = CharField()
    idade = CharField()
    emissora = CharField()

    def __str__(self):
        return("Nome do narrador: " + self.nome + "\n" + "Idade: " + self.idade + "\n" + "Emissora: " + self.emissora)


class Partida(BaseModel):
    nome_times = CharField()
    gols_time_A = CharField()
    gols_time_B = CharField()
    estadio = ForeignKeyField(Estadio)
    arbitragem = ForeignKeyField(Arbitro)
    produtos = ForeignKeyField(Produto)
    narrador = ForeignKeyField(Narrador)
    quantidade_faltas_A = CharField()
    quantidade_faltas_B = CharField()
    cartoes_amarelos_A = CharField()
    cartoes_amarelos_B = CharField()
    cartoes_vermelhos_A = CharField()
    cartoes_vermelhos_B = CharField()


    def __str__(self):
        return("Partida entre: " + self.nome_times + "\n" + "Gols do time A: " + self.gols_time_A + "\n" + "Gols do time B: " + self.gols_time_B + "\n" + str(self.estadio) + "\n" + str(self.arbitragem) + "\n" + "\n" + str(self.produtos) + "\n" + str(self.narrador) + "\n" + "Quantidade de faltas time A: " + self.quantidade_faltas_A + "\n" + "Quantidade de faltas time B: " + self.quantidade_faltas_B + "\n" + "Cartoes amarelos time A: " + self.cartoes_amarelos_A + "\n" + "Cartoes amarelos time B: " + self.cartoes_amarelos_B + "\n" + "Cartoes vermelhos time A: " + self.cartoes_vermelhos_A + "\n" + "Cartoes vermelhos time B: " + self.cartoes_vermelhos_B)
        

if __name__ == "__main__":
    if os.path.exists("CampeonatoFutebol.db"):
        os.remove("CampeonatoFutebol.db")


    db.connect()
    db.create_tables([Socio_torcedor, Tecnico, Jogador, Estadio, Time, Campeonato, Arbitro, Produto, Narrador, Partida])


    carlao = Socio_torcedor.create(nome = "Carlos Henrique de Morais", idade = "18", time = "Flamengo", assinatura = "Platina", tempo_como_socio = "3 anos" )

    jj = Tecnico.create(nome = "Jorge Jesus", idade = "65", time_atual = "Flamengo", titulos = "3 Campeonatos Portugues, 1 Campeonato Brasileiro, 1 Libertadores, 1 Mundial de Clubes", primeiro_time = "Amora")

    messi = Jogador.create(nome = "Lionel Messi", idade = "32", time = "Flamengo", tempo_time = "3 meses", primeiro_time = "Barcelona", titulos = "Golden Boy 2005, 5 Ballon d'Or, 6 the best of fifa, 4 Uefa Champions League", gols = "620", assistencias = "240", cartoes_vermelhos = "2", cartoes_amarelos = "80")

    maracana = Estadio.create(nome = "Maracanã", capacidade_max = "78.838 espectadores", cidade = "Rio de Janeiro", tipo_gramado = "Natural", recorde_publico = "199.854 mil pessoas", )

    flamengo = Time.create(nome = "Flamengo", tecnico =jj, jogadores = messi, estadio = maracana, socio_torcedor = carlao)

    brasileirao = Campeonato.create(nome = "Campeonato Brasileiro Série A", pontuacao = "81", colocacao = "1", quantidade_rodadas = "38", time = flamengo, quantidade_times_participantes = "20")

    pitana = Arbitro.create(nome = "Néstor Pitana", idade = "44 anos", funcao = "Arbitro Central", associacao = "FIFA, CONMEBOL, AFA")

    consumo_estadio = Produto.create(camisa = "Camisa do Flamengo", bebida = "Coca - cola", comida = "Cachorro - quente", lembrancinha = "chaveiro do Flamengo")

    milton = Narrador.create(nome = "Milton Leite", idade = "60 anos", emissora = "SporTV")

    flamengoXsantos = Partida.create(nome_times = "Flamengo X Santos", gols_time_A = "5", gols_time_B = "5", estadio = maracana, arbitragem = pitana, produtos = consumo_estadio, narrador = milton, quantidade_faltas_A = "17", quantidade_faltas_B = "16", cartoes_amarelos_A = "4", cartoes_amarelos_B = "4", cartoes_vermelhos_A = "1", cartoes_vermelhos_B = "1" )


    
    
    
   
    
    print(brasileirao)
    print()
    print(flamengoXsantos)