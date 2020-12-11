from instabot import Bot
import credential
bot = Bot()
bot.login(username = "username",password = "password")
bot.upload_photo("name of your image.jpg",caption="Enter the caption")