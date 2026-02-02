from dbase import Database
from config import DBASE,PRIX,FORA,ADMIN
from aiogram.types import Message

async def DefUser(bot,message: Message,iduser,idp,dat,tim,minit,namp,name,dolj):
    #print(message.from_user.full_name)
    print(f"{iduser=},{idp=},{dat=},{tim=} {minit=}")

    if minit < int(PRIX) :     # разница 4 соатдан  кичик булса "Келиш" деб хисоблаймиз
        # проверим если неть запись с признаком prz=0 (пришел)
        # то добавляем запись в таблицу davomad
        tup = (iduser,dat,0)
        async with Database(DBASE) as dbs:
            st = "SELECT * FROM davomad WHERE user_id = ? AND data = ? AND PRZ = ?"
            zp = await dbs.fetch_one(st, tup)  # Данные офиса
            if zp is  None:
                sql = '''INSERT INTO davomad (user_id, office_id, data, time, prz,raz)  VALUES (?, ?, ?, ?, ?, ?)'''
                tp = (iduser,idp,dat,tim,0,minit)
                await dbs.IUD(sql, tp)
                sz = f"Келиш белгиланди. {dat}; {tim}"
                await message.answer(sz)
                print(sz + f"{ iduser=},{idp=} Запись в таблицу dovomad произведен.")

                tss = f"{namp}\n{name}\n{dolj}\n{dat}\n{tim}\n"

                if minit > FORA:
                    sv = f"кечикиш {minit} минут."
                    await message.answer(sv)
                    print(sv + f"{ iduser=},{idp=}")
                    tss = tss + sv
                await bot.send_message(chat_id=ADMIN, text=tss)  # Админга хабар
            else:
                print(f"Сиз бир марта {dat}; {tim} да белгиландингиз. {iduser=},{idp=}")
                await message.answer(f"Сиз {dat}; {tim} да келгансиз")
    else:                     # Кетиш
        pass
