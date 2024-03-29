START = 'Вы хотите сделать платную публикацию без очереди или бесплатную?'

PAYMENT_START = '''
📍 Для оплаты вам необходимо перевести деньги на карту. После оплаты нажмите на кнопку "✅ Оплатил".\n
СУММА: <b>%s р.</b>
НОМЕР КАРТЫ: <b>%s</b> (%s)
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

Отправьте боту до 10 фотографий.
'''

ARTICLE_PHOTO_SUCCESS = '''
<b>Фотографии успешно добавлены!</b>
Выберите действие ниже 👇
'''

ARTICLE_PHOTO_SAVE = '''
Благодарим за предложенную новость. Ваше объявление проходит модерацию, сразу после \
проверки оно будет опубликовано в нашем канале.
'''

DESCRIPTION_LIMIT = '''
⚠️ Некорректно указано описание.
Описание не должно превышать 890 символов!
'''

CITY_LIMIT = '''
⚠️ Некорректно указан город.
Название города не должно превышать 25 символов!
'''

PHONE_FORMAT_ERROR = '''
⚠️ Некорректный формат номера телефона.
Укажите его в формате +7, без пробелов и лишних символов.
'''

PRICE_FORMAT_ERROR = '''
⚠️ Некорректный формат цены.
Укажите целое, натуральное число без лишних символов!
Максимальное количество символов - 14
'''

PHOTO_ERROR = '''
⚠️ Некорректно указаны фотографии.
Отправьте до 10 фотографий!
'''

PHOTO_LIMIT = '''
⚠️ Много фотографий.
Превышен лимит фотографий!
'''

ARTICLE_TEMPLATE = '''
%s
Цена %s руб, %s, %s

✅Свои объявления присылайте в бота:  @%s
'''

ARTICLE_PUBLISH = '''
❗️ Пользователь @%s (ID: <code>%s</code>) хочет опубликовать статью выше.👆 Опубликовать или изменить?
'''

CHECK_TEXT = '''
✅ Публикация оплачена!
Чек приложен к сообщению.
'''

ADMIN_GREETING = '''
Привет, администратор!

Выбери необходимый пункт 👇
'''

ADMIN_SEND_MESSAGE = '''
Выберите пользователя, которому хотите отправить сообщение.
'''

MESSAGE_FOR_ALL = '''
Какое сообщение вы хотите отправить всем пользователям?
'''

MESSAGE_FOR_USER = '''
Какое сообщение вы хотите отправить пользователю с ID:
<i>%s</i>
'''

MESSAGE_SENT_SUCCESS = '''
Ваше сообщение успешно отправлено!
'''

EDIT_DESCRIPTION = '''
📝 Отправьте новое описание.
'''

EDIT_CITY = '''
📝 Отправьте новый город.
'''

EDIT_PHONE = '''
📝 Отправьте новый номер телефона.
'''

EDIT_PRICE = '''
📝 Отправьте новую цену.
'''

EDIT_SUCCESS = '''
📨 Данные успешно сохранены!
'''

UNKNOWN_COMMAND = '''
<b>❗️ Неизвестная команда</b>

Выполните команду /start
'''

USER_BLOCKED = '''
❌ Пользователь заблокирован!
'''
