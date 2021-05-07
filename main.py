    #   Importando ferramentas uteis
import random
from bs4 import BeautifulSoup
import requests
import time

    #   Importando outro arquivo do bot
import music

    #   Importando a biblioteca do discord
import discord
from discord.ext import commands
from discord.utils import get

    #   Variaveis importantes para API do discord
client = commands.Bot(command_prefix = ';')
bot = commands.Bot(command_prefix = ';')

if __name__ == '__main__':
    print('Arquivo fonte')
else:
    print('Iniciando "main.py"')

    #   Mensagem de inicio do bot, e atividade
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name = 'https://github.com/Gazzana/MyDiscordBot.py'))

    #   Lista de comandos do bot
@client.command(help = 'Lista de comandos do bot')
async def comandos(ctx):
    embed = discord.Embed(
        tittle = 'Lista de comandos do bot',
        description = '''Comandos do bot:
        
        ➣  ; regras

        ➣  ; comandos

        ➣  ; t192

        ➣  ; b8

        ➣  ; code

        ➣  ; server

        ➣  ; calc   [n°]   [+, -, *, *, /, //, %]   [n°]

        ➣  ; join, leave

        ➣  ; flood [arg1] [arg2]

        ➣  ; jogodavelha [@player1] [@player2]
    
        ➣  ; everyone, stop

        ➣  ; prt [argumento]

        ➣  ; currency [crypto moeda]

        ➣  ; dollar [moeda]

        ➣  ; count [numero] [limite]
        
        ➣  ; kick [@] [motivo]

        ➣  ; ban [@] [motivo]
        ''',
        color = discord.Color.blue()
    )
    await ctx.send(embed=embed)

    #   Comando das regras do servidor
@client.command(help = 'Regras do servidor')
async def regras(ctx):  #   Lendo o arquivo 'text'
    f = open('regras.txt', 'r')
    regras = f.read()
    embed = discord.Embed(
        tittle = 'Regras',
        color = discord.Color.from_rgb(252, 202, 3)
    )
    embed.add_field(name = '''  𝕽𝖊𝖌𝖗𝖆𝖘 𝖉𝖔 𝖘𝖊𝖗𝖛𝖎𝖉𝖔𝖗:
    ''', value = regras, inline = True)
    await ctx.send(embed=embed)

    #   Enviando o URL do repositorio do GitHub
@client.command(help = 'Exibe o repositório do GitHub')
async def code(ctx):
    embed = discord.Embed(
        tittle = 'Codigo',
        description = ' ',
        color = discord.Color.blue()
    )
    embed.add_field(name='Sabia que eu sou open-source?', value='Visite    https://github.com/Gazzana/MyDiscordBot.py    para mais detalhes.', inline=True)
    await ctx.send(embed=embed)

    #   Horarios da aula
@client.command(help = 'Horários da Turma 192')
async def t192(ctx):
    embed = discord.Embed(
        tittle = '192',
        description = 'Cronograma da 192:',
        color = discord.Color.from_rgb(252, 202, 3)
    )
    embed.set_image(url = 'https://cdn.discordapp.com/attachments/817029853827956777/826793437234724874/horarios192.png')
    await ctx.send(embed=embed)

    #   Exibindo informaçoes do servidor
@client.command('Informações sobre o servidor')
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    s_id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    membercount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)
    
    embed = discord.Embed(
        tittle = name + " Informações do servidor",
        description = description,
        color = discord.Color.dark_blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name='Owner', value='gazzana', inline=True)
    embed.add_field(name='Id', value=s_id, inline=True)
    embed.add_field(name='Region', value=region, inline=True)
    embed.add_field(name='Member count', value=membercount, inline=True)
    await ctx.send(embed=embed)

    #   Fazendo matematica basica
@client.command(help = 'Calcular matemática basica, use: ;calc [numero] [operador] [numero]')
async def calc(ctx, arg1, arg2, arg3):
    n1 = float(arg1)
    op = arg2
    n2 = float(arg3)
    if op == '+':
        result = n1 + n2

    elif op ==  '-':
        result = n1 - n2

    elif op == '*':
        result = n1 * n2

    elif op == '/':
        result = n1 / n2

    elif op == '**':
        result = n1 ** n2

    elif op == '/':
        result = n1 / n2

    elif op == '//':
        result = n1 // n2

    elif op == '%':
        result = (f'{n1 * 100 / n2}%')
    
    elif op == '=':
        reusult = 'C é burro mano?'

    else:
        result = ('Você provavelmente digitou errado, invoque o comando, e depois escolha um numero, um operador(+, -, *, //, **) e outro numero') 
    embed = discord.Embed(
        tittle = calc,
        color = discord.Color.from_rgb(252, 202, 3))
    embed.add_field(name=result, value= f'{arg1} {op} {arg3}', inline = True)
    await ctx.send(embed=embed)

    #   Spamming messsages, it doesn't work well, because discord have a anti-spam system
@client.command(help = 'Flodando mensagens, use primeiro o numero de mensagens, e por ultimo o conteúdo da mesagen')
async def flood(ctx, arg1, arg2):   #   Spam the number of times the arg1(number) is saying, and send the arg2(anything)
    limit = float(arg1)
    while 1 < limit:
        await ctx.send(arg2)

    #   Jogo da velha por chat
player1 = ''
player2 = ''
turn = ''
gameOver = True

board = []

winning_conditions = [
[0, 1, 2],
[3, 4, 5],
[6, 7, 8],
[8, 3, 6],
[1, 4, 7],
[2, 5, 8],
[8, 4, 8],
[2, 4, 6]]

    #   Iniciando o jogo
@client.command(help = 'Inicia uma partida de jogo da velha')
async def jogodavelha(ctx, p1 : discord.Member, p2 : discord.Member):
    global player1
    global player2
    global turn
    global gameOver
    global count

    if gameOver:
        global board
        board = [':white_large_square:', ':white_large_square:', ':white_large_square:',
                 ':white_large_square:', ':white_large_square:', ':white_large_square:',
                 ':white_large_square:', ':white_large_square:', ':white_large_square:']
        turn = ''
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # Print the board
        line = ''
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += ' ' + board[x]
                await ctx.send(line)
                line = ''
            else:
                line += ' ' + board[x]

        # Who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send('É vez de <@' + str(player1.id) + '>')
        elif num == 2:
            turn = player2
            await ctx.send('É vez de <@' + str(player2.id) + '>')
    else:
        await ctx.send('Um jogo já está acontecendo, acabe ele antes de começar outro.')

    #   Fazendo o player poder jogar
@client.command(help = 'Fazer jogadas de jogo da velha')
async def jogar(ctx, pos : int):
    global turn
    global player1
    global player2
    global board
    global count

    if not gameOver:
        mark = ''
        if turn == ctx.author:
            if turn == player1:
                mark = ':regional_indicator_x:'
            elif turn == player2:
                mark = ':o2:'
            if 0 < pos < 10 and board[pos - 1] == ':white_large_square:':
                board[pos - 1] = mark
                count += 1

                # print board again
                line = ''
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += ' ' + board[x]
                        await ctx.send(line)
                        line = ''
                    else:
                        line += ' ' + board[x]

                    check_winner(winning_conditions, mark)
                    if gameOver:
                        await ctx.send(mark + ' ganhou!')
                    elif count >= 9:
                        await ctx.send('Empate!')

                    # Switch turns
                    if turn == player1:
                        turn = player2
                    elif turn == player2:
                        turn = player1

            else:
                await ctx.send('Use um numero entre 1 e 9, que não esteja marcado.')
        else:
            await ctx.send('Não é sua vez!')
    else:
        await ctx.send('Inicie um novo jogo.')

def check_winner(winning_conditions, mark):
    global gameOver
    for condition in winning_conditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

    #   Cuidando de erros
@jogodavelha.error
async def jogodavelha_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Por favor mencione duas pessoas para começar um jogo.')
    elif isinstance(error, commands.BadArgument):
        await ctx.send('Você prescisa mencionar jogadores, Ex: <@395989582635728896>')
        
    #   Cuidando de erros
@jogar.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Por favor, digite a posição que você gostaria de marcar.')
    elif isinstance(error, commands.BadArgument):
        await ctx.send('Use ">jogar [Número entre 1 e 9]"')

    #   Enviando @everyone muito rapido
@client.command(help = 'Enviando @everyone, muito rapido')
async def everyone(ctx):
    global n
    n = 1
    while n < 2:
        await ctx.send('@everyone')
    #   Interrompendo o spam
@client.command(help = 'Interrompendo o spam de @everyone')
async def stop(ctx):
    global n
    n = 3
    await ctx.send('Spam interrompido')

    #   Printando o argumento
@client.command(help = 'Este comando é meio inutil, ele só printa a sua mensagem para o console do host')
async def prt(ctx, arg):
    x = arg
    print(x)
    await ctx.send('Mensagem enviada!')

@client.command(help = 'Simplesmente envia uma mensagem v a z i a')
async def blank(ctx):
    await ctx.send('⠀')

    #   Traduzindo cripto moedas para o argumento 2
@client.command(help = 'Pega o valor de uma criptomoeda e traduz para o segundo argumento')
async def currency(ctx, arg1, arg2):
    def get_value(coin, moeda):
        url = 'https://www.google.com/search?q=' + coin + '+price+' + moeda
        HTML = requests.get(url)
        soup = BeautifulSoup(HTML.text, 'html.parser')
        text = soup.find('div', attrs = {'class':'BNeawe iBp4i AP7Wnd'}).find('div', attrs = {'class':'BNeawe iBp4i AP7Wnd'}).text
        return text
    price = get_value(arg1, arg2)

    embed = discord.Embed(
        tittle = 'Valor',
        color = discord.Color.from_rgb(252, 202, 3)
    )
    embed.add_field(name = price, value = f'Valor do {arg1} em {arg2}' , inline = True)
    embed.set_image(url = 'https://cdn.discordapp.com/attachments/803615269745852428/837048412402221106/Z.png')
    await ctx.send(embed=embed)

@client.command(help = 'Traduz o dolar para a moeda citada na mensagem')
async def dollar(ctx, arg):
    def get_value(coin):
        url = 'https://www.google.com/search?q=dollar+para+' + coin
        HTML = requests.get(url)
        soup = BeautifulSoup(HTML.text, 'html.parser')
        text = soup.find('div', attrs = {'class': 'BNeawe iBp4i AP7Wnd'}).find('div', attrs = {'class':'BNeawe iBp4i AP7Wnd'}).text
        return text
        
    moeda = get_value(arg)

    embed = discord.Embed(
        tittle = f'Dollar para {arg}',
        color = discord.Color.dark_blue()
    )
    embed.add_field(name = moeda, value = f'Um Dollar em {arg}')
    embed.set_image(url = 'https://cdn.discordapp.com/attachments/830830730912464917/837144642419163216/2Q.png')

    await ctx.send(embed=embed)

    #   Expulsando membros
@client.command(help = 'Kickar membros')
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason=reason)

    #   Banindo membros
@client.command(help = 'Banir membros')
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason=reason)

    #   Contando MUITO
@client.command(help = 'Conta do primeiro numero, ate o ultimo numero do comando')
async def count(ctx, arg1, arg2):
    arg1, arg2 = int(arg1), int(arg2)
    while arg1 < arg2:
        await ctx.send(arg1)
        arg1 += 1

@client.command(help = 'Limpa o chat')
async def clear(ctx):
    f = open('vazio.txt', 'r')
    void = f.read()
    await ctx.send('⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀')

    #   Fazendo o discord reconhecer o bot
client.run('token')