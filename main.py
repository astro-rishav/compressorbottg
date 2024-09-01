
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram import Update
import ffmpeg

# Set up logging
logging.basicConfig(level=logging.INFO)

# Set up the bot
TOKEN = 7391936956:AAEdKDqoBZAqSDdrg6DsPtKVN9ueliyhF64

# Define the video compression function
def compress_video(update: Update, context):
    # Get the video file from the message
    video_file = context.bot.getFile(update.message.video.file_id)

    # Save the video file to a temporary location
    video_file.download('temp.mp4')

    # Compress the video using FFmpeg
    ffmpeg.input('temp.mp4').output('output.mp4', vcodec='libx264', crf=28).run()

    # Send the compressed video back to the user
    context.bot.send_video(chat_id=(link unavailable), video=open('output.mp4', 'rb'))

# Define the bot commands and handlers
def start(update: Update, context):
    context.bot.send_message(chat_id=(link unavailable), text='Send me a video to compress!')

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.video, compress_video))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
 
