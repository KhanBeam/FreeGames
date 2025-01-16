import asyncio 
import schedule
from GameScraper import EpicScraper
import aiohttp
import revolt

class Client(revolt.Client):
    async def messagesender(game_name, game_image, game_link):
        game_message = f"""
        Game Name: {game_name}
        Game Link: {game_link}
        Game Image: !!{game_image}!!
        """
        await bot.sendmessage(message.channel, Print)

async def onLogin():
    print(f'Logged in as {bot.user.username}')

async def main():
    schedule.every().day.at("19:00").do(EpicScraper.game_scraper)

    async with aiohttp.ClientSession() as session:
        client = Client(session, "BOT TOKEN HERE")
        while True:
            schedule.run_pending()
            time.sleep(1)
            await client.start()

asyncio.run(main())