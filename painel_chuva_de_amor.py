import time
import os
import random

fundo_vermelho = "\033[41m"
cores_texto = [
    "\033[97m", "\033[93m", "\033[95m",
    "\033[96m", "\033[91m", "\033[92m",
]
reset = "\033[0m"

coracoes = ["❤️", "💕", "💞", "💓", "💖", "💘", "❣️", "💗", "💝"]

frases = [
    "Te amo com todas as forças ❤️", "Você é o amor da minha vida 💘", "Meu mundo é melhor com você 💞",
    "Cada segundo com você vale ouro 💎", "Meu coração bate por você 💓", "Nunca vou te deixar 💍",
    "Você é meu sonho real ✨", "Com você até o impossível é fácil 💫", "Quero envelhecer ao seu lado 👴👵",
    "Sou completamente seu(a) 💖", "Nosso amor não tem fim ♾️", "Você é meu sol ☀️",
    "Você ilumina tudo 🌟", "Te amarei em todas as vidas 🔁", "Meu porto seguro ⚓", "Minha paz tem seu nome 🕊️",
    "Se amar é viver, vivo por você 🌹", "Você me completa 🧩", "Meu coração é só teu 💘",
    "Você é minha melhor parte 💑", "Amo sua alma 💫", "Você é meu lar 🏠", "Você é meu destino 🗺️",
    "Sorte a minha te ter 🍀", "Você é meu tudo 💯", "Me apaixono por você todo dia 😍", "Sempre serei seu 💋",
    "Com você tudo faz sentido 🎯", "Seu amor é meu remédio 💊", "Você me dá vida 🌈",
    "Prometo te fazer feliz todos os dias 🥰", "Te amo sem medidas 📏", "Você é a razão do meu sorriso 😊",
    "Nada me separa de você 🚫", "Te amo até o infinito 💞", "Sou louco(a) por você 🤯",
    "Quero você pra sempre ⏳", "Seu cheiro mora em mim 🌬️", "Te quero aqui, agora e sempre ⏰",
    "Você é minha música favorita 🎵", "Te carrego no peito ❤️", "Te vejo até de olhos fechados 😌",
    "Você me faz bem 🌺", "Você é minha vibe 💫", "Você é meu céu estrelado 🌌",
    "Seu amor é poesia 📖", "Você é minha calmaria 🌊", "Te amar é meu destino 🔮",
    "Você é o melhor de mim 🌟", "Sou seu(a), eternamente 💍"
]

def limpar_tela():
    os.system("clear" if os.name == "posix" else "cls")

def painel_animado(largura):
    cor = random.choice(cores_texto)
    coracao = random.choice(coracoes)
    borda = f"{cor}{coracao*3}{reset}"
    mensagem = f"{cor} TE AMO INFINITO {reset}"
    espaço = (largura - len(mensagem)) // 2
    linha = " " * espaço + borda + mensagem + borda
    return linha

def animar_amor():
    largura = os.get_terminal_size().columns
    altura = os.get_terminal_size().lines

    try:
        while True:
            limpar_tela()
            painel = painel_animado(largura)
            print(fundo_vermelho + painel + reset + "\n")

            for _ in range(altura - 4):
                linha = ""
                for _ in range(random.randint(3, 6)):
                    cor = random.choice(cores_texto)
                    frase = random.choice(frases)
                    coracao = random.choice(coracoes)
                    espaco = " " * random.randint(0, max(0, largura - len(frase) - 5))
                    linha += espaco + cor + frase + " " + coracao + reset + "\n"
                print(fundo_vermelho + linha + reset)
            print(fundo_vermelho + painel + reset)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\033[1;31mSaindo...\033[0m Mas o amor continua eterno 💖")

if __name__ == "__main__":
    animar_amor()
