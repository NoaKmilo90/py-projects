from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from telegram import ChatAction
import feedparser
import wget



def start(update, context):

    update.message.reply_text('Kochiniwa, puedo enviarte el último capítulo de Nadie Sabe Nada \nsi me envías el comando /samante \n\nPronto haré más cosas, samanté pa ti')


def resumen(update, context):
    
    podcast = feedparser.parse('https://fapi-top.prisasd.com/podcast/playser/nadie_sabe_nada/itunestfp/podcast.xml')

    titulo = podcast.entries[0].title

    desc = podcast.entries[0].description
    
    update.message.reply_text('Título: ' + titulo + '\n\n' + desc)



def archivo(update, chat):    
    
    podcast = feedparser.parse('https://fapi-top.prisasd.com/podcast/playser/nadie_sabe_nada/itunestfp/podcast.xml')

    update.message.reply_text('Descargando audio...')

    arch = podcast.entries[0].link

    cap = arch

    chat = update.message.chat
    wget.download(cap, 'samante.mp3')

    chat.send_action(
        action=ChatAction.UPLOAD_AUDIO,

       timeout=None
    )

    chat.send_audio(
        audio=open('samante.mp3', 'rb')
    )


if __name__ == '__main__':

    updater = Updater(token='1318683281:AAGJH_kwbeHP0wgoqTnDPeoGBcA5XzFTJlk', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    dp.add_handler(CommandHandler('resumen', resumen))

    dp.add_handler(CommandHandler('archivo', archivo))

   
    updater.start_polling()
    updater.idle()
