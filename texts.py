GREET_MESSAGE = '''
Привет 👋 
Рады видеть тебя здесь! 

*Diplomatic* — Здесь ты сможешь участвовать в розыгрышах 🎁 и отправлять доносы Мизулиной. Давай весело проведем время вместе!
'''

DONOS_MESSAGE = '''
🚨 <b>Оформляем донос Мизулиной</b>: 

✍️ Напишите донос, указав <b>объект доноса</b> и <b>причину</b>
📩 Вскоре он будет доставлен до специалистов
'''

DONOS_SUCCESSFUL = '''
✅ <b>Донос успешно отправлен</b>
Благодарим вас за вклад в развитие страны
'''

def ACCOUNT_INFO(user, id):
    print(user)
    return f'''
⚙️ <b>Мой аккаунт</b>
Вся необходимая информация о профиле

<b>{user['name'][0]}</b>
<b>{user['name'][1]}</b>

🌐 ID: {id}
⭐ Баллы: {user['xp']}
💸 Баланс: {user['money']} р.

💶 Мой кошелёк: 0₽
💷 Мой партнёрский счёт: 0₽
💎 Подписка до:  отсутствует
⚙️ Лимит запросов в сутки: 0/9

🔎 Моя статистика запросов:
├ Фотографий: 1
├ Автомобилей: 2
├ Электронных почт: 1
└ Номеров телефонов: 29
'''