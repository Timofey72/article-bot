START = 'Вы хотите сделать платную публикацию без очереди или бесплатную?'

PAYMENT_START = '''
📍 Для оплаты вам необходимо перевести деньги на карточку. После оплаты нажмите на кнопку "✅ Оплатил".\n
СУММА: <b>200 р.</b>
НОМЕР КАРТЫ: <b>1234123412341234</b>
'''

PAYMENT_CONFIRM = '''
📷 Чтобы подтвердить платеж отправьте фотографию с чеком перевода.
'''

PAYMENT_FINISH = '''
✅ Спасибо за оплату. Публикация будет выложена в канал сразу после проверки чека.
'''

NOT_CORRECT_CHECK = '''
⚠️ Некорректный формат чека.
Отправьте скриншот чека в формате фотографии!
'''

ARTICLE_FREE_INFO = '''
❗️ В бесплатном тарифе вам придется ждать очередь, перед отправкой вашей публикации в канал.
'''

ARTICLE_DESCRIPTION = '''
📃 <b>Создание публикации: Описание</b> 📃

Отправьте боту описание для вашего товара!
Описание не должно превышать 900 символов. 
'''

ARTICLE_CITY = '''
📃 <b>Создание публикации: Город</b> 📃

Укажите ваш город. Он будет отображаться в публикации.
'''

ARTICLE_PHONE = '''
📃 <b>Создание публикации: Номер телефона</b> 📃

Укажите ваш номер телефона в формате +7.
'''

ARTICLE_PRICE = '''
📃 <b>Создание публикации: Цена</b> 📃

Теперь укажите цену вашего товара в рублях.
'''

ARTICLE_PHOTO = '''
📃 <b>Создание публикации: Фотографии</b> 📃

Отправьте боту одну фотографию товара! Потом вы сможете добавить еще фотографии.
'''

ARTICLE_PHOTO_SUCCESS = '''
<b>Фотография успешно добавлена!</b>
Выберите действие ниже 👇
'''

ARTICLE_PHOTO_SAVE = '''
Все фотографии успешно сохранены!
Публикация отправлена на проверку.
'''

DESCRIPTION_LIMIT = '''
⚠️ Некорректно указано описание.
Описание не должно превышать 900 символов!
'''

CITY_LIMIT = '''
⚠️ Некорректно указан город.
Название города не должно превышать 25 символов!
'''

PHONE_FORMAT_ERROR = '''
⚠️ Некорректный формат номера телефона.
Укажите его в формате +7
'''

PRICE_FORMAT_ERROR = '''
⚠️ Некорректный формат цены.
Укажите целое, натуральное число без лишних символов!
'''

PHOTO_ERROR = '''
⚠️ Некорректно указаны фотографии.
Отправьте одну фотографию!
'''

PHOTO_LIMIT = '''
⚠️ Много фотографий.
Превышен лимит фотографий!
'''

ARTICLE_TEMPLATE = '''
%s

💡 Информация
Номер телефона: <code>%s</code>
Город: <i>%s</i>
Цена: <i>%s</i> руб.
'''

ARTICLE_PUBLISH = '''
❗️ Пользователь хочет опубликовать статью выше.👆 Опубликовать или изменить?
'''

CHECK_TEXT = '''
✅ Публикация оплачена!
Чек приложен к сообщению.
'''

ADMIN_GREETING = '''
Привет, администратор! Твой ID: <code>%s</code>

Выбери необходимый пункт 👇
'''
