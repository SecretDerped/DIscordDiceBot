import random
from disnake.ext import commands

token = 'Вставьте сюда Ваш токен'
bot = commands.Bot("!", sync_commands_debug=True)


@bot.event
async def on_ready():
    print("...Bot is ready")


@bot.slash_command(name='d',
                   description="Кидает DICES кубиков, у которых по EDGES граней")
async def roll(inter, dices: int, edges: int):
    max_dices = 24
    max_edges = 200

    if dices > max_dices:
        await inter.response.send_message('**Слишком много кубиков! Стол не выдержит!**')
    elif dices < 1:
        await inter.response.send_message('*Никаких кубиков не брошено...*')
    elif edges < 1:
        await inter.response.send_message('Кубиков с отрицательным количеством граней не существует')
    elif edges > max_edges:
        await inter.response.send_message('Кубики с таким количеством граней больше напоминают шар.'
                                          '\nВведите меньше граней.')
    else:
        throw = "] [".join(str(random.randint(1, edges)) for rolls in range(dices))
        result = f'{dices}d{edges}: [{throw}]'
        await inter.response.send_message(result)


bot.run(str(token))
