#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.
#
# THIS EXAMPLE HAS BEEN UPDATED TO WORK WITH THE BETA VERSION 12 OF PYTHON-TELEGRAM-BOT.
# If you're still using version 11.1.0, please see the examples at
# https://github.com/python-telegram-bot/python-telegram-bot/tree/v11.1.0/examples

"""
Basic example for a bot that uses inline keyboards.
"""
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


#PWM на Blue и White + Яркость лампы 
LED = [[False, 255, False, 255, 0, 0.1], [False, 255, False, 255, 0, 0.1]] #White Blue
#ON/OFF BRIGHT SINON/OFF MAX_HIGHT DISTANCE SPEED 
LAMP=[False, 255, 1, 0.1, [255, 255, 255]]
#ON/OFF BRIGHT MODE SPEED RGB
Kbutton='0'

keyboard_f = [[InlineKeyboardButton("ON", callback_data='1'),InlineKeyboardButton("OFF", callback_data='2') ],
                [InlineKeyboardButton("SETTINGS", callback_data='3')],[InlineKeyboardButton("SW_W", callback_data='4'), InlineKeyboardButton("SW_Lamp", callback_data='5'),InlineKeyboardButton("SW_B", callback_data='6') ]]

reply_markup_f = InlineKeyboardMarkup(keyboard_f)#Готовим к вызову keyboard

keyboard_s = [[InlineKeyboardButton('LAMP_SET',callback_data='7')],
                [InlineKeyboardButton('BRIGHT_LED',callback_data='8')],
                [InlineKeyboardButton('SIN_LED',callback_data='9')],
                [InlineKeyboardButton('<--',callback_data='0')]]
reply_markup_s = InlineKeyboardMarkup(keyboard_s)#Готовим к вызову keyboard

keyboard_t1=[[InlineKeyboardButton('COLORS',callback_data='18'),InlineKeyboardButton('RAINBOW',callback_data='19')],
            [InlineKeyboardButton('COLOR',callback_data='20'),InlineKeyboardButton('WHITE',callback_data='21'),InlineKeyboardButton('LIGHTNING',callback_data='22')],
            [InlineKeyboardButton('BRIGHT_SET',callback_data='23'),InlineKeyboardButton('SPEED_SET',callback_data='24')],
            [InlineKeyboardButton('<--',callback_data='3')]]
reply_markup_t1=InlineKeyboardMarkup(keyboard_t1)

keyboard_t2=[[InlineKeyboardButton('BRIGHTNESS',callback_data='10')],
            [InlineKeyboardButton('WHITE bright',callback_data='11')],
            [InlineKeyboardButton('BLUE bright',callback_data='12')],
            [InlineKeyboardButton('<--',callback_data='3')]]
reply_markup_t2=InlineKeyboardMarkup(keyboard_t2)

keyboard_t3=[[InlineKeyboardButton('SIN Switch',callback_data='13')],
            [InlineKeyboardButton('SIN_W',callback_data='14'),InlineKeyboardButton('SIN_B',callback_data='15')],
            [InlineKeyboardButton('SET_W',callback_data='16'),InlineKeyboardButton('SET_B',callback_data='17')],
            [InlineKeyboardButton('<--',callback_data='3')]]
reply_markup_t3=InlineKeyboardMarkup(keyboard_t3)
#query=update.callback_query
#Функция создания строки
#Status
#Left:  ON
#Right: ON
#Lamp:  ON
def StatusSrting():
    #Вызываем функцию проверки статуса
    white='White: '
    blue='Blue: '
    lamp='Lamp:  '
    #Описываем левую
    if LED[0][0]==True:
        if LED[0][2]==True:
            white=white+'SIN \n(H:'+ str(LED[0][3])+';D:'+str(LED[0][4])+';S:'+str(LED[0][5])+') \n'
        else: 
            white=white+'ON('+str(LED[0][1])+') \n'
    else: 
        white=white+'OFF \n'

    #Описываем правую
    if LED[1][0]==True:
        if LED[1][2]==True:
            blue=blue+'SIN \n('+ str(LED[1][3])+','+str(LED[1][4])+','+str(LED[1][5])+') \n'
        else: 
            blue=blue+'ON('+str(LED[1][1])+') \n'
    else: 
        blue=blue+'OFF \n'

    #Описываем лампу
    if LAMP[0]==True:
        
        if LAMP[2]==0:
            lamp=lamp+'RNBW \n(B:'+str(LAMP[1])+';S:'+str(LAMP[3])+') \n'
        elif LAMP[2]==1:
            lamp=lamp+'CLRS \n(B:'+str(LAMP[1])+';S:'+str(LAMP[3])+') \n'
        elif LAMP[2]==2:
            lamp=lamp+'WT \n(B:'+str(LAMP[1])+';S:'+str(LAMP[3])+') \n'
        elif LAMP[2]==3:
            lamp=lamp+'Light \n(B:'+str(LAMP[1])+';S:'+str(LAMP[3])+') \n'
        elif LAMP[2]==4:
            lamp=lamp+'CLR \n(R:'+ str(LAMP[4][0])+';G:'+str(LAMP[4][1])+';B:'+str(LAMP[4][2])+';BR:'+str(LAMP[1])+') \n'
    else:
        lamp=lamp+'OFF \n'
    
    info= 'Status: \n'+white+blue+lamp
    return info

#def Status(update,context):
 #   update


def FKey(query):
   # keyboard = [[InlineKeyboardButton("ON", callback_data='1'),InlineKeyboardButton("OFF", callback_data='2') ],
   #             [InlineKeyboardButton("SETTINGS", callback_data='3')],[InlineKeyboardButton("SW_W", callback_data='4'), InlineKeyboardButton("SW_Lamp", callback_data='5'),InlineKeyboardButton("SW_B", callback_data='6') ]]
#Описываем клавиатуру 
    ##keyboard1= [[KeyboardButton('ON'),KeyboardButton('OFF')],
    ##            [KeyboardButton('SETTINGS')],
    ##            [KeyboardButton('SW_B'),KeyboardButton('SW_L'),KeyboardButton('SW_W')]]
    ##reply_markup = InlineKeyboardMarkup(keyboardF,resize_keyboard=True)#Готовим к вызову keyboard
    #query = update.callback_query
    query.edit_message_text(text=StatusSrting())
    query.edit_message_reply_markup(reply_markup=reply_markup_f)
    #update.message.reply_text(StatusFunc(), reply_markup=reply_markup,one_time_keyboard=True)

def SKey(query,KBtn):#второй слой
    #query = update.callback_query
   # keyboard=[[InlineKeyboardButton('LAMP Set',callback_data='6')],
   #             [InlineKeyboardButton('Bright LED',callback_data='7')],
   #             [InlineKeyboardButton('SIN LED',callback_data='8')],
   #             [InlineKeyboardButton('back',callback_data='0')]]
    ##reply_markup=InlineKeyboardMarkup(keyboardS)
    if KBtn==3:
        query.edit_message_text(text=StatusSrting())
        query.edit_message_reply_markup(reply_markup=reply_markup_s)
       #query.edit_message_text(text=StatusSrting())
    else:
        if KBtn==1:
            LED[0][0]=LED[1][0]=LAMP[0]=True
        #query.edit_message_text(text=StatusSrting())

        elif KBtn==2:
            LED[0][0]=LED[1][0]=LAMP[0]=False
        #query.edit_message_text(text=StatusSrting())

    #elif KBtn==3:
     #  query.edit_message_reply_markup(reply_markup=reply_markup_s)
     # #query.edit_message_text(text=StatusSrting())

        elif KBtn==4:#SW_W
            if LED[0][0]==True:
                LED[0][0]=False
            else:
                LED[0][0]=True
        #query.edit_message_text(text=StatusSrting())

        elif KBtn==5:#SW_LAMP
            if LAMP[0]==True:
                LAMP[0]=False
            else:
                LAMP[0]=True
        #query.edit_message_text(text=StatusSrting())

        elif KBtn==6:#SW_B
            if LED[1][0]==True:
                LED[1][0]=False
            else:
                LED[1][0]=True
        query.edit_message_text(text=StatusSrting())
        query.edit_message_reply_markup(reply_markup=reply_markup_f)
    
def TKey(query,KBtn):
    if KBtn==7:
        reply_markup_temp=reply_markup_t1
    if KBtn==8:
        reply_markup_temp=reply_markup_t2
    if KBtn==9:
        reply_markup_temp=reply_markup_t3
    query.edit_message_text(text=StatusSrting())
    query.edit_message_reply_markup(reply_markup=reply_markup_temp)
        

def start(update, context):
    keyboard = [[InlineKeyboardButton("ААААааааа", callback_data='0')],
                 [InlineKeyboardButton("БЛЯЯЯдь!", callback_data='0')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('— Не лезь, блядь, дебил, сука, ебаный. Ты чё, хххуёл, я те сказали что ли? Залезь, наххуй, нака обратно, блядь! Дебил, блядь.', reply_markup=reply_markup)


def button(update, context):
    query = update.callback_query
    Kbutton=int(query.data)
    if Kbutton==0:
        FKey(query=query)
    if 1<=Kbutton<=6:
        SKey(query=query,KBtn=Kbutton)
    if 7<=Kbutton<=9:
        TKey(query=query,KBtn=Kbutton)
    #updater.dispatcher.add_handler(CallbackQueryHandler(button))
    print(Kbutton)


def help(update, context):
    update.message.reply_text("Use /start to test this bot.")
    print(Kbutton)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("558870400:AAGdrq_zjcFyMPGvoUiGOXYPJ_XORRBVkZs",use_context=True)

    
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

   # if Kbutton==0:
    

    updater.dispatcher.add_handler(CommandHandler('Status', FKey))
    #updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    
    
    updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
