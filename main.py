from aiogram import Dispatcher, types, F, filters, Bot
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import asyncio


bot = Bot(token="7463682515:AAFG7QjOVpPp508stqFiiD-pbqm40nlwIyM")
dp = Dispatcher(bot=bot)

mainn_button = ReplyKeyboardMarkup(keyboard=mainn_button2, resize_keyboard=True)
mainn_button2 = [
    [KeyboardButton(text="O'zbek tili (Узбекский язык)", callback_data="uzb"),KeyboardButton(text="Rus tili (Ryccкий язык)", callback_data="rus")]
]

keyboards = [
    [KeyboardButton(text='Lavashlar'),KeyboardButton(text="Burgerlar")],
    [KeyboardButton(text="Menuga qaytish")]
]



burgerlar = [
    [KeyboardButton(text="Kids-Kvadrich"), KeyboardButton(text="Gamburger")],
    [KeyboardButton(text="Dablchizburger"), KeyboardButton(text="Chizburger")],
    [KeyboardButton(text="Menuga qaytish")]
]



lavashsh = [
    [KeyboardButton(text='Mol goshtidan lavash'), KeyboardButton(text="Tovuq goshtidan lavash")],
    [KeyboardButton(text="Mol goshtidan pishloqli lavash"), KeyboardButton(text="Tovuq goshtidan pishloqli lavash")],
    [KeyboardButton(text="Mol goshtidan qalampirli lavash"), KeyboardButton(text="Tovuq goshtidan qalampirli lavash")],
    [KeyboardButton(text="Menuga qaytish")]
]


balans = [
    [KeyboardButton(text='Uzcard'), KeyboardButton(text="Humo"), KeyboardButton(text="UnionPay")],
    [KeyboardButton(text="Orqaga qaytish")]
    
]

balans_orqaga = [
    [KeyboardButton(text='Balans toldirish'), KeyboardButton(text="Menuga qaytish")]
    
    
]


pinaaa1 = [
    [KeyboardButton(text='Pina colada harid qilish'), KeyboardButton(text="ichimliklarga qaytish")] 
]
pinaaa2 = [
    [KeyboardButton(text='Moxito harid qilish'), KeyboardButton(text="ichimliklarga qaytish")] 
]
pinaaa3 = [
    [KeyboardButton(text='Gazlangan suv harid qilish'), KeyboardButton(text="ichimliklarga qaytish")] 
]
pinaaa4 = [
    [KeyboardButton(text='Gazlanmagan suv harid qilish'), KeyboardButton(text="ichimliklarga qaytish")] 
]
pinaaa5 = [
    [KeyboardButton(text='Pepsi 1.5l harid qilish'), KeyboardButton(text="ichimliklarga qaytish")] 
]
pinaaa6 = [
    [KeyboardButton(text='Pepsi 1.5l harid qilish'), KeyboardButton(text="ichimliklarga qaytish")] 
]
pinaaa7 = [
    [KeyboardButton(text='Pepsi 0.5l harid qilish'), KeyboardButton(text="ichimliklarga qaytish")] 
]
molgosh = [
    [KeyboardButton(text='Mol goshtidan lavash harid qilish'), KeyboardButton(text="Ovqatlarga qaytish qaytish"), KeyboardButton(text="Lavashlarga qaytish qaytish")] 
]
tovuqgosh = [
    [KeyboardButton(text='Tovuq goshtidan lavash harid qilish'), KeyboardButton(text="Ovqatlarga qaytish qaytish"), KeyboardButton(text="Lavashlarga qaytish qaytish")] 
]
molgoshp = [
    [KeyboardButton(text='Mol goshtidan pishloqli lavash harid qilish'), KeyboardButton(text="Ovqatlarga qaytish qaytish"), KeyboardButton(text="Lavashlarga qaytish qaytish")] 
]
tovuqgoshp = [
    [KeyboardButton(text='Tovuq goshtidan pishloqli lavash harid qilish'), KeyboardButton(text="Ovqatlarga qaytish qaytish"), KeyboardButton(text="Lavashlarga qaytish qaytish")] 
]
molgoshq = [
    [KeyboardButton(text='Mol goshtidan qalampirli lavash harid qilish'), KeyboardButton(text="Ovqatlarga qaytish qaytish"), KeyboardButton(text="Lavashlarga qaytish qaytish")] 
]
tovuqgoshq = [
    [KeyboardButton(text='Tovuq goshtidan qalampirli lavash harid qilish'), KeyboardButton(text="Ovqatlarga qaytish qaytish"), KeyboardButton(text="Lavashlarga qaytish qaytish")] 
]
burgerrr1 = [
    [KeyboardButton(text='Kids-Kvadrich harid qilish'), KeyboardButton(text="Ovqatlarga qaytish qaytish"), KeyboardButton(text="Burgerlar qaytish qaytish")] 
]
burgerrr2 = [
    [KeyboardButton(text='Gamburger harid qilish'), KeyboardButton(text="Ovqatlarga qaytish qaytish"), KeyboardButton(text="Burgerlar qaytish qaytish")] 
]
burgerrr3 = [
    [KeyboardButton(text='Chizburger harid qilish'), KeyboardButton(text="Ovqatlarga qaytish qaytish"), KeyboardButton(text="Burgerlar qaytish qaytish")] 
]
burgerrr4 = [
    [KeyboardButton(text='Dablchizburger harid qilish qilish'), KeyboardButton(text="Ovqatlarga qaytish qaytish"), KeyboardButton(text="Burgerlar qaytish qaytish")] 
]
harid1 = ReplyKeyboardMarkup(keyboard=pinaaa1, resize_keyboard=True)
harid2 = ReplyKeyboardMarkup(keyboard=pinaaa2, resize_keyboard=True)
harid3 = ReplyKeyboardMarkup(keyboard=pinaaa3, resize_keyboard=True)
harid4 = ReplyKeyboardMarkup(keyboard=pinaaa4, resize_keyboard=True)
harid5 = ReplyKeyboardMarkup(keyboard=pinaaa5, resize_keyboard=True)
harid6 = ReplyKeyboardMarkup(keyboard=pinaaa6, resize_keyboard=True)
harid6 = ReplyKeyboardMarkup(keyboard=pinaaa7, resize_keyboard=True)
Mol_goshtidan_lavash = ReplyKeyboardMarkup(keyboard=molgosh, resize_keyboard=True)
Tovuq_goshtidan_lavash = ReplyKeyboardMarkup(keyboard=tovuqgosh, resize_keyboard=True)
Mol_goshtidan_p_lavash = ReplyKeyboardMarkup(keyboard=molgoshp, resize_keyboard=True)
Tovuq_goshtidan_p_lavash = ReplyKeyboardMarkup(keyboard=tovuqgoshp, resize_keyboard=True)
Mol_goshtidan_q_lavash = ReplyKeyboardMarkup(keyboard=molgoshq, resize_keyboard=True)
Tovuq_goshtidan_q_lavash = ReplyKeyboardMarkup(keyboard=tovuqgoshq, resize_keyboard=True)
burgerrrrrr = ReplyKeyboardMarkup(keyboard=burgerrr4, resize_keyboard=True)
burger_menu = ReplyKeyboardMarkup(keyboard=burgerlar, resize_keyboard=True)
burgerrr = ReplyKeyboardMarkup(keyboard=burgerrr1, resize_keyboard=True)
burgerrrr = ReplyKeyboardMarkup(keyboard=burgerrr2, resize_keyboard=True)
burgerrrrr = ReplyKeyboardMarkup(keyboard=burgerrr3, resize_keyboard=True)




ichimliklar = [
    [KeyboardButton(text='Pina colada'), KeyboardButton(text="Moxito"), KeyboardButton(text='Gazlangan suv 0.5l')],
    [KeyboardButton(text="Gazlanmagan suv 0.5l"),  KeyboardButton(text="Pepsi 1.5l"), KeyboardButton(text="Pepsi 0.5l")],
    [KeyboardButton(text='Pepsi razliv'),KeyboardButton(text="Menuga qaytish")]

    
]

main_button = ReplyKeyboardMarkup(keyboard=keyboards, resize_keyboard=True)

lavashlar = ReplyKeyboardMarkup(keyboard=lavashsh, resize_keyboard=True)

ichimliklar_button = ReplyKeyboardMarkup(keyboard=ichimliklar, resize_keyboard=True)

balans_orqaga_button = ReplyKeyboardMarkup(keyboard=balans_orqaga, resize_keyboard=True)

balans_button = ReplyKeyboardMarkup(keyboard=balans, resize_keyboard=True)

keyboards_second = [
    [KeyboardButton(text='Ovqat'), KeyboardButton(text="Ichimliklar")],
    [KeyboardButton(text="Balans"),  KeyboardButton(text="Siz haqingizda")],
    [KeyboardButton(text="Orders")]
]

main_button_second = ReplyKeyboardMarkup(keyboard=keyboards_second, resize_keyboard=True)

@dp.message(filters.Command("start"))
async def start(message: types.Message):
    await message.answer("Assalomu alekom. \nXush kelibsiz nima buyurtma qilasiz:", reply_markup=mainn_button)






balance = 500000




@dp.message(F.text == "Siz haqingizda")
async def start(message: types.Message):
    await message.answer(f"Sizning ismingiz {message.from_user.full_name} \n \n Sizning username(ingiz) {message.from_user.username} \n \n Sizning id raqamingiz {message.from_user.id}", reply_markup=main_button_second)





# Balans_________________________________________________________________________________________________________________________________________________________________________________________________  
@dp.message(F.text == "Balans")
async def start(message: types.Message):

    await message.answer(f"Balansingiz: {balance} \nBalansizgizda pul yo'q", reply_markup=balans_orqaga_button)

@dp.message(F.text == "Balans toldirish")
async def start(message: types.Message):
    await message.answer(f"Balansingizni to'ldirish uchun carta tanlang", reply_markup=balans_button)

@dp.message(F.text == "Orqaga qaytish")
async def start(message: types.Message):
    await message.answer(f"Orqaga qaytdingiz", reply_markup=balans_orqaga_button)

@dp.message(F.text == "Menuga qaytish")
async def start(message: types.Message):
    await message.answer(f"Menuga qaytdingiz", reply_markup=main_button_second)

# Balans_________________________________________________________________________________________________________________________________________________________________________________________________  


# Ovqatlar________________________________________________________________________________________________________________________________________________________________________________________

@dp.message(F.text == "Ovqat")
async def start(message: types.Message):
    await message.answer(f"Siz ovqat tanladiz", reply_markup=main_button)









#lavash__________________________________________________________________________________________________________________________________________________________________________________________
@dp.message(F.text == "Lavashlar")
async def start(message: types.Message):
    await message.answer("Lavashalar manusi", reply_markup=lavashlar)





@dp.message(F.text == "Mol goshtidan lavash")
async def start(message: types.Message):
    await message.answer_photo(photo="https://media.express24.uz/r/600/600/OZpGZ7bkt6pXPFINvsIZq.jpg",
                            caption="Mol goshtidan lavash: \nNarxi: 32 000 so'm ", reply_markup=Mol_goshtidan_lavash )
    
@dp.message(F.text == "Mol goshtidan lavash harid qilish")
async def start(message: types.Message):
    global balance
    balance = balance - 32000

    await message.answer(f"Harid qildingiz. \nBalansingiz {balance} so'm pul qoldi", reply_markup=main_button_second )

@dp.message(F.text == "Ovqatlarga qaytish qaytish")
async def start(message: types.Message):
    await message.answer("Ovqatlarga qaytildi",reply_markup=main_button)

@dp.message(F.text == "Lavashlarga qaytish qaytish")
async def start(message: types.Message):
    await message.answer("Lavashlarga qaytildi",reply_markup=lavashlar)
#lavash__________________________________________________________________________________________________________________________________________________________________________________________

#lavash__________________________________________________________________________________________________________________________________________________________________________________________
@dp.message(F.text == "Tovuq goshtidan lavash")
async def start(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/get-eda/3595513/347697a54a8a1ac3270e8895fb16a7a4/M_height",
                            caption="Tovuq goshtidan lavash: \nNarxi: 30 000 so'm ", reply_markup=Tovuq_goshtidan_lavash )
    global balance
    balance = balance - 30000

    
@dp.message(F.text == "Tovuq goshtidan lavash harid qilish")
async def start(message: types.Message):
    await message.answer(f"Harid qildingiz. \nBalansingiz 220.000 so'm pul qoldi", reply_markup=main_button_second )
    

@dp.message(F.text == "Ovqatlarga qaytish qaytish")
async def start(message: types.Message):
    await message.answer("Ovqatlarga qaytildi",reply_markup=main_button)
#lavash__________________________________________________________________________________________________________________________________________________________________________________________

#lavash__________________________________________________________________________________________________________________________________________________________________________________________
@dp.message(F.text == "Mol goshtidan pishloqli lavash")
async def start(message: types.Message):
    await message.answer_photo(photo="https://media.express24.uz/r/600/600/uY_AGLHOg7pfAIruBsGHt.jpg",
                            caption="Mol goshtidan pishloqli lavash: \nNarxi: 35 000 so'm ", reply_markup=Mol_goshtidan_p_lavash )
    global balance
    balance = balance - 35000

    
@dp.message(F.text == "Mol goshtidan pishloqli lavash harid qilish")
async def start(message: types.Message):
    await message.answer(f"Harid qildingiz. \nBalansingiz 215.000 so'm pul qoldi", reply_markup=main_button_second )
    

@dp.message(F.text == "Ovqatlarga qaytish qaytish")
async def start(message: types.Message):
    await message.answer("Ovqatlarga qaytildi",reply_markup=main_button)
#lavash__________________________________________________________________________________________________________________________________________________________________________________________

#lavash__________________________________________________________________________________________________________________________________________________________________________________________
@dp.message(F.text == "Tovuq goshtidan pishloqli lavash")
async def start(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/get-eda/3595513/2957c4160077b0a3fddc8a017be92b96/M_height",
                            caption="33000: \nNarxi: 33 000 so'm ", reply_markup=Tovuq_goshtidan_p_lavash )
    global balance
    balance = balance - 33000

@dp.message(F.text == "Tovuq goshtidan pishloqli lavash harid qilish")
async def start(message: types.Message):
    await message.answer(f"Harid qildingiz. \nBalansingiz 217.000 so'm pul qoldi", reply_markup=main_button_second )
    

@dp.message(F.text == "Ovqatlarga qaytish qaytish")
async def start(message: types.Message):
    await message.answer("Ovqatlarga qaytildi",reply_markup=main_button)
#lavash__________________________________________________________________________________________________________________________________________________________________________________________

#lavash__________________________________________________________________________________________________________________________________________________________________________________________
@dp.message(F.text == "Mol goshtidan qalampirli lavash")
async def start(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/get-eda/3595513/ab09d8126be114be4d2c4fe0291604ad/M_height",
                            caption="Mol goshtidan qalampirli lavash: \nNarxi: 32 000 so'm ", reply_markup=Mol_goshtidan_q_lavash )
    global balance
    balance = balance - 32000

@dp.message(F.text == "Mol goshtidan qalampirli lavash harid qilish")
async def start(message: types.Message):
    await message.answer(f"Harid qildingiz. \nBalansingiz 218.000 so'm pul qoldi", reply_markup=main_button_second )
    

@dp.message(F.text == "Ovqatlarga qaytish qaytish")
async def start(message: types.Message):
    await message.answer("Ovqatlarga qaytildi",reply_markup=main_button)
#lavash__________________________________________________________________________________________________________________________________________________________________________________________

#lavash__________________________________________________________________________________________________________________________________________________________________________________________
@dp.message(F.text == "Tovuq goshtidan qalampirli lavash")
async def start(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/get-eda/3595513/2957c4160077b0a3fddc8a017be92b96/M_height",
                            caption="Tovuq goshtidan qalampirli lavash: \nNarxi: 30 000 so'm ", reply_markup=Tovuq_goshtidan_q_lavash )
    global balance
    balance = balance - 30000

@dp.message(F.text == "Tovuq goshtidan qalampirli lavash harid qilish")
async def start(message: types.Message):
    await message.answer(f"Harid qildingiz. \nBalansingiz 220.000 so'm pul qoldi", reply_markup=main_button_second )
    

@dp.message(F.text == "Ovqatlarga qaytish qaytish")
async def start(message: types.Message):
    await message.answer("Ovqatlarga qaytildi",reply_markup=main_button)
#lavash__________________________________________________________________________________________________________________________________________________________________________________________
# Burgerlar________________________________________________________________________________________________________________________________________________________________________________________________
@dp.message(F.text == "Burgerlar")
async def start(message: types.Message):
    await message.answer("Burgerlar manusi", reply_markup=burger_menu)

@dp.message(F.text == "Kids-Kvadrich")
async def start(message: types.Message):
    await message.answer_photo(photo="https://media.express24.uz/r/600/600/5PiUaFhkobZqbFJvyjW9m.jpg",
                            caption="Kids-Kvadrich: \nNarxi: 16 000 so'm ", reply_markup=burgerrr )
    global balance
    balance = balance - 16000

@dp.message(F.text == "Kids-Kvadrich harid qilish")
async def start(message: types.Message):
    await message.answer(f"Harid qildingiz. \nBalansingiz 234.000 so'm pul qoldi", reply_markup=main_button_second )
  
@dp.message(F.text == "Ovqatlarga qaytish qaytish")
async def start(message: types.Message):
    await message.answer("Ovqatlarga qaytildi",reply_markup=main_button)

@dp.message(F.text == "Burgerlar qaytish qaytish")
async def start(message: types.Message):
    await message.answer("Burgerlar qaytildi",reply_markup=burger_menu)


@dp.message(F.text == "Gamburger")
async def start(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/get-sprav-products/9854027/2a0000018a742bb060fd3fa5b984c4ce4651/M_height",
                            caption="Gamburger: \nNarxi: 25 000 so'm ", reply_markup=burgerrrr )
    global balance
    balance = balance - 25000

@dp.message(F.text == "Gamburger harid qilish")
async def start(message: types.Message):
    await message.answer(f"Harid qildingiz. \nBalansingiz 225.000 so'm pul qoldi", reply_markup=main_button_second )
  
@dp.message(F.text == "Ovqatlarga qaytish qaytish")
async def start(message: types.Message):
    await message.answer("Ovqatlarga qaytildi",reply_markup=main_button)

@dp.message(F.text == "Burgerlarga qaytish")
async def start(message: types.Message):
    await message.answer("Burgerlar qaytildi",reply_markup=burger_menu)


@dp.message(F.text == "Chizburger")
async def start(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTnn8c1fBoI0-uOJ6PJRddQoYNdYRTmeCjdrL4BXCH1PC_qqKUsN86R5sv-ZGmssoEokr8&usqp=CAU",
                            caption="Chizburger: \nNarxi: 37 000 so'm ", reply_markup=burgerrrrr )
    global balance
    balance = balance - 37000

@dp.message(F.text == "Chizburger harid qilish")
async def start(message: types.Message):
    await message.answer(f"Harid qildingiz. \nBalansingiz 213.000 so'm pul qoldi", reply_markup=main_button_second )
  
@dp.message(F.text == "Ovqatlarga qaytish qaytish")
async def start(message: types.Message):
    await message.answer("Ovqatlarga qaytildi",reply_markup=main_button)

@dp.message(F.text == "Burgerlar qaytish qaytish")
async def start(message: types.Message):
    await message.answer("Burgerlar qaytildi",reply_markup=burger_menu)




@dp.message(F.text == "Dablchizburger")
async def start(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0m_iadA0IwE-azJ5VoNeF0Jdah4Y5WbE1SQ&s",
                            caption="Dablchizburger: \nNarxi: 40 000 so'm ", reply_markup=burgerrrrrr )
    global balance
    balance = balance - 40000

@dp.message(F.text == "Dablchizburger harid qilish")
async def start(message: types.Message):
    await message.answer(f"Harid qildingiz. \nBalansingiz 210.000 so'm pul qoldi", reply_markup=main_button_second )
  
@dp.message(F.text == "Ovqatlarga qaytish qaytish")
async def start(message: types.Message):
    await message.answer("Ovqatlarga qaytildi",reply_markup=main_button)

@dp.message(F.text == "Burgerlar qaytish qaytish")
async def start(message: types.Message):
    await message.answer("Burgerlar qaytildi",reply_markup=burger_menu)


# Burgerlar_______________________________________________________________________________________________________________________________________________________________________________________________




# Ovqatlar_____________________________________________________________________________________________________________________________________________________________________________________________                                          



# Ichimliklar_________________________________________________________________________________________________________________________________________________________________________________________________  
@dp.message(F.text == "Ichimliklar")
async def start(message: types.Message):
    await message.answer(f"Ichimliklari menusi", reply_markup=ichimliklar_button)
# pina____________________________________________________________________________________________________________________________________________
@dp.message(F.text == "Pina colada")
async def start(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQu8CsFX1bxh0ocvFLMsJDyWg1UO5_vgFnPWw&s",
                            caption="Pina colada: \nNarxi: 15 000 so'm ", reply_markup=harid1)
    global balance
    balance = balance - 15000

@dp.message(F.text == "Pina colada harid qilish")
async def start(message: types.Message):
    await message.answer(f"Harid qildingiz. \nBalansingiz 235.000 so'm pul qoldi", reply_markup=main_button_second )
    

@dp.message(F.text == "ichimliklarga qaytish")
async def start(message: types.Message):
    await message.answer("Ichimliklarga qaytildi",reply_markup=ichimliklar_button)
# pina____________________________________________________________________________________________________________________________________________                                          
    
# Moxito____________________________________________________________________________________________________________________________________________
@dp.message(F.text == "Moxito")
async def start(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/get-eda/1463280/f8b9196d5a33a8fd001ff6512004cb94/M_height",
                            caption="Moxito: \nNarxi: 15 000 so'm ", reply_markup=harid2)
    global balance
    balance = balance - 15000
 
@dp.message(F.text == "Moxito harid qilish")
async def start(message: types.Message):
    await message.answer(f"Harid qildingiz. \nBalansingiz 235.000 so'm pul qoldi", reply_markup=main_button_second )

@dp.message(F.text == "ichimliklarga qaytish")
async def start(message: types.Message):
    await message.answer("Ichimliklarga qaytildi",reply_markup=ichimliklar_button)
# Moxito____________________________________________________________________________________________________________________________________________


# Gazlangan suv 0.5l____________________________________________________________________________________________________________________________________________
@dp.message(F.text == "Gazlangan suv 0.5l")
async def start(message: types.Message):
    await message.answer_photo(photo="https://yukber.uz/image/cache/catalog/product/YK0152/YK0152_1-600x600.jpg",
                            caption="Gazlangan suv 0.5l: \nNarxi: 5 000 so'm ", reply_markup=harid3)
    global balance
    balance = balance - 5000

@dp.message(F.text == "Gazlangan suv harid qilish")
async def start(message: types.Message):
    await message.answer(f"Harid qildingiz. \nBalansingiz 245.000 so'm pul qoldi", reply_markup=main_button_second )

@dp.message(F.text == "ichimliklarga qaytish")
async def start(message: types.Message):
    await message.answer("Ichimliklarga qaytildi",reply_markup=ichimliklar_button)
# Gazlangan suv 0.5l____________________________________________________________________________________________________________________________________________

# Gazlanmagan suv 0.5l____________________________________________________________________________________________________________________________________________
@dp.message(F.text == "Gazlanmagan suv 0.5l")
async def start(message: types.Message):
    await message.answer_photo(photo="https://yukber.uz/image/cache/catalog/product/YK0365/YK0365_1-600x600.jpg",
                            caption="Gazlanmagan suv 0.5l: \nNarxi: 5 000 so'm ", reply_markup=harid4)
    global balance
    balance = balance - 5000

@dp.message(F.text == "Gazlanmagan suv harid qilish")
async def start(message: types.Message):
    await message.answer(f"Harid qildingiz. \nBalansingiz 245.000 so'm pul qoldi", reply_markup=main_button_second )

@dp.message(F.text == "ichimliklarga qaytish")
async def start(message: types.Message):
    await message.answer("Ichimliklarga qaytildi",reply_markup=ichimliklar_button)
# Gazlanmagan suv 0.5l____________________________________________________________________________________________________________________________________________

# Pepsi 1.5l____________________________________________________________________________________________________________________________________________
@dp.message(F.text == "Pepsi 1.5l")
async def start(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/get-sprav-products/5399152/2a0000018a742bac08237a6e050bcb729f7b/M_height",
                            caption="Pepsi 1.5l: \nNarxi: 20 000 so'm ", reply_markup=harid5)
    global balance
    balance = balance - 20000

@dp.message(F.text == "Pepsi 1.5l harid qilish")
async def start(message: types.Message):
    await message.answer(f"Harid qildingiz. \nBalansingiz 230.000 so'm pul qoldi", reply_markup=main_button_second )

@dp.message(F.text == "ichimliklarga qaytish")
async def start(message: types.Message):
    await message.answer("Ichimliklarga qaytildi",reply_markup=ichimliklar_button)
# Pepsi 1.5l____________________________________________________________________________________________________________________________________________

# Pepsi razliv____________________________________________________________________________________________________________________________________________
@dp.message(F.text == "Pepsi razliv")
async def start(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/get-eda/1447609/cff648470685f6296ab66061781bebcb/M_height",
                            caption="Pepsi razliv: \nNarxi: 9 000 so'm ", reply_markup=harid6)
    global balance
    balance = balance - 9000

@dp.message(F.text == "Pepsi razliv harid qilish")
async def start(message: types.Message):
    await message.answer(f"Harid qildingiz. \nBalansingiz 241.000 so'm pul qoldi", reply_markup=main_button_second )

@dp.message(F.text == "ichimliklarga qaytish")
async def start(message: types.Message):
    await message.answer("Ichimliklarga qaytildi",reply_markup=ichimliklar_button)
# Pepsi razliv____________________________________________________________________________________________________________________________________________

# Pepsi 0.5l____________________________________________________________________________________________________________________________________________
@dp.message(F.text == "Pepsi 0.5l")
async def start(message: types.Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/get-sprav-products/9854027/2a0000018a742bb53a861b3373ee0e1e6c25/M_height",
                            caption="Pepsi 0.5l: \nNarxi: 11 000 so'm ", reply_markup=harid7)
    global balance
    balance = balance - 11000

@dp.message(F.text == "Pepsi 0.5l harid qilish")
async def start(message: types.Message):
    await message.answer(f"Harid qildingiz. \nBalansingiz 239.000 so'm pul qoldi", reply_markup=main_button_second )

@dp.message(F.text == "ichimliklarga qaytish")
async def start(message: types.Message):
    await message.answer("Ichimliklarga qaytildi",reply_markup=ichimliklar_button)
# Pepsi 0.5l____________________________________________________________________________________________________________________________________________

# Ichimliklar_________________________________________________________________________________________________________________________________________________________________________________________________  





async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())






