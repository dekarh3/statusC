# -*- coding: utf-8 -*-

import string

IN_NAME = ['СНИЛС', 'СтатусПроверки', 'ПоступилоОбращение', 'ПримечаниеПоОтработкеСБ',
            'СтатусБумажногоНосителяПоДоговору', 'СтатусБумажногоНосителяПоЗаявлению', 'СтатусОплаты',
            'ЯвляетсяДублем', 'ПричинаПоДоговору', 'Статус_бумаги', 'Статус_СБ', 'Статус_КЦ']

IN_SNILS = ['СНИЛС', 'СтраховойНомер', 'Страховой_номер']

OUT_STAT = {
'Статус бумаги' : ['—', 'Бумага принята', 'Ошибка', 'Нет бумаги', 'Готов к прозвону', 'Нет документов','Отутствуют сканы документов'],
'Статус СБ' : ['—', 'Блок СБ', 'Блок по СС', 'Блок по умершим', 'Блок по телефону', 'Умер ЗЛ', 'Блок паспорт', 'Блок по адресам',
               'Блок партнер', 'Террорист', 'Наш блок', 'Дубль сверки', 'Дезинформация', 'Поступило обращение',
               'Блок по возрасту', 'Дубль сверки фонда'],
'Статус КоллЦентра' : ['—', 'Подтверждает', 'Отказ', 'Недозвон', 'В работе', 'Заключал, но будет расторгать', 'Неправильный номер',
                       'Неверные данные', 'Подтверждает, но неверные данные', 'Ок, но требуется подтверждение', 'Актуализация',
                       'Отключен'],
'Фонд - Статус бумаги' : ['—', 'Бумага принята', 'Ошибка', 'Нет бумаги', 'Готов к прозвону', 'Нет документов'],
'Фонд - Статус СБ' : ['—', 'Блок СБ', 'Блок по СС', 'Блок по умершим', 'Блок по телефону', 'Умер ЗЛ', 'Блок паспорт',
                      'Блок по адресам', 'Блок партнер', 'Террорист', 'Наш блок', 'Дубль сверки', 'Дезинформация',
                      'Поступило обращение', 'Блок по возрасту', 'Дубль сверки фонда',
                      'Некорректный СНИЛС', 'Не пройдена СМС верификация', 'Отрицательный перепрозвон', 'Проводится проверка'],
'Фонд - Статус КоллЦентра' : ['—', 'Подтверждает', 'Отказ', 'Недозвон', 'В работе', 'Заключал, но будет расторгать',
                              'Неправильный номер', 'Неверные данные', 'Подтверждает, но неверные данные',
                              'Ок, но требуется подтверждение', 'Актуализация', 'Отключен',
                              'Акцепт прозвона', 'Одобрено инф. письмом'],
'Статус оплаты' : ['—', 'Оплачено', 'Аванс', 'К оплате'],
'Выгружено' : ['—', 'Да'],
'Статус перепрозвона' : ['—', 'ОК', 'На перепрозвон']
}



IN_STAT_FOND =  {
'СтатусПроверки' : {'' : ['Статус КоллЦентра', None],
    'Не дозвонился' : ['Статус КоллЦентра','Недозвон'],
    'По указанным номерам ЗЛ отсутствует' : ['Статус КоллЦентра', 'Недозвон'],
    'ЗЛ подтверждает факт заключения договора, но данные указаны с ошибками' : ['Статус КоллЦентра', 'Подтверждает, но неверные данные'],
    'ЗЛ подтверждает факт заключения договора' : ['Статус КоллЦентра', 'Подтверждает'],
    'Отказ от факта заключения договора' : ['Статус КоллЦентра','Отказ'],
    'Договор заключал, но будет расторгать' : ['Статус КоллЦентра', 'Заключал, но будет расторгать'],
    'Негатив' : ['Статус КоллЦентра', 'Отказ'],
    'Подтверждает заключение, но договор не подписывал' : ['Статус КоллЦентра', 'Отказ']},
'ПоступилоОбращение' : {'' : ['Статус СБ', None], 'Отказ' : ['Статус СБ', 'Поступило обращение']},
'ПричинаИзмененияСтатусаЗЛ' : {'': ['Статус СБ', None],
    'блок по письму подразделения - по проверке внутренней СБ' : ['Статус СБ', 'Блок СБ'],
    'на перепроверке - агенты по умершим': ['Статус СБ', 'Блок по умершим'],
    'Не пройдена СМС верификация': ['Фонд - Статус СБ', 'Не пройдена СМС верификация'],
    'негативный перепрозвон': ['Фонд - Статус СБ', 'Отрицательный перепрозвон'],
    'недействительные паспорта': ['Статус СБ', 'Блок паспорт'],
    'письмо от РО': ['Статус СБ', 'Поступило обращение'],
    'проводится проверка': ['Фонд - Статус СБ', 'Проводится проверка'],
    'реестр недобросовестных договоров (умершие)': ['Статус СБ', 'Блок по умершим'],
    'субагенты по умершим': ['Статус СБ', 'Блок по умершим'],
    'умер ЗЛ': ['Статус СБ', 'Умер ЗЛ']},
'ПримечаниеПоОтработкеСБ' : {'': ['Фонд - Статус КоллЦентра', None],
    'Акцепт прозвона': ['Фонд - Статус КоллЦентра', 'Акцепт прозвона'],
    'Одобрено инф. письмом': ['Фонд - Статус КоллЦентра', 'Одобрено инф. письмом']},
'СтатусБумажногоНосителяПоДоговору' : {'': [None, None], 'Исправили': [None, None], 'Наличие бумаги': [None, None],
                                       'Выявлены ошибки': [None, None], 'Отсутствие бумаги': [None, None]},             # Вручную, в обоих полях Исправили или Наличие бумаги
'СтатусБумажногоНосителяПоЗаявлению' : {'': [None, None], 'Исправили': [None, None], 'Наличие бумаги': [None, None],
                                        'Выявлены ошибки': [None, None], 'Отсутствие бумаги': [None, None]},
'СтатусОплаты' : {'': [None, None], 'Оплата': [None, None], 'Вычет': [None, None]},
'ЯвляетсяДублем' : {'Да' : ['Статус СБ', 'Дубль сверки фонда'], 'Нет': ['Статус СБ', None]},
'ПричинаПоДоговору' : {'': ['Статус СБ', None],
    'СНИЛС на другое застрахованное лицо': ['Фонд - Статус СБ', 'Некорректный СНИЛС'],
    'Страховой номер упразднен': ['Фонд - Статус СБ', 'Некорректный СНИЛС']}
                }

IN_STAT_OUR =   {
'Статус_бумаги' : {'—' : ['Статус бумаги', '—'],
    'Бумага принята': ['Статус бумаги', 'Бумага принята'],
    'Ошибка': ['Статус бумаги', 'Ошибка'],
    'Нет бумаги': ['Статус бумаги', 'Нет бумаги'],
    'Готов к прозвону': ['Статус бумаги', 'Готов к прозвону'],
    'Нет документов': ['Статус бумаги', 'Нет документов'],
    'Отутствуют сканы документов': ['Статус бумаги', 'Отутствуют сканы документов']},
'Статус_СБ' : {'—': ['Статус СБ', '—'],
    'Блок СБ': ['Статус СБ', 'Блок СБ'],
    'Блок по СС': ['Статус СБ', 'Блок по СС'],
    'Блок по умершим': ['Статус СБ', 'Блок по умершим'],
    'Блок по телефону': ['Статус СБ', 'Блок по телефону'],
    'Умер ЗЛ': ['Статус СБ', 'Умер ЗЛ'],
    'Блок паспорт': ['Статус СБ', 'Блок паспорт'],
    'Блок по адресам': ['Статус СБ', 'Блок по адресам'],
    'Блок партнер': ['Статус СБ', 'Блок партнер'],
    'Террорист': ['Статус СБ', 'Террорист'],
    'Наш блок': ['Статус СБ', 'Наш блок'],
    'Дубль сверки': ['Статус СБ', 'Дубль сверки'],
    'Дезинформация': ['Статус СБ', 'Дезинформация'],
    'Поступило обращение': ['Статус СБ', 'Поступило обращение'],
    'Блок по возрасту': ['Статус СБ', 'Блок по возрасту'],
    'Дубль сверки фонда': ['Статус СБ', 'Дубль сверки фонда']},
'Статус_КЦ' : {'—': ['Статус КоллЦентра', '—'],
    'Подтверждает': ['Статус КоллЦентра', 'Подтверждает'],
    'Отказ': ['Статус КоллЦентра', 'Отказ'],
    'Недозвон': ['Статус КоллЦентра', 'Недозвон'],
    'В работе': ['Статус КоллЦентра', 'В работе'],
    'Заключал, но будет расторгать': ['Статус КоллЦентра', 'Заключал, но будет расторгать'],
    'Неправильный номер': ['Статус КоллЦентра', 'Неправильный номер'],
    'Неверные данные': ['Статус КоллЦентра', 'Неверные данные'],
    'Подтверждает, но неверные данные': ['Статус КоллЦентра', 'Подтверждает, но неверные данные'],
    'Ок, но требуется подтверждение': ['Статус КоллЦентра', 'Ок, но требуется подтверждение'],
    'Актуализация': ['Статус КоллЦентра', 'Актуализация'],
    'Отключен': ['Статус КоллЦентра', 'Отключен']}
                }

OUT_NAME = ['СНИЛС', 'Статус бумаги', 'Статус СБ', 'Статус КоллЦентра','Фонд - Статус бумаги', 'Фонд - Статус СБ',
       'Фонд - Статус КоллЦентра', 'Статус оплаты', 'Выгружено', 'Статус перепрозвона']

def lenl(a):
    try:
        if a != None:
            a = str(a).strip()
            if  a != '':
                a = ''.join([char for char in a if char in string.digits])
                return len(a)
        return 0
    except TypeError:
        return 0


def l(a):
    try:
        if a != None:
            a = str(a).strip()
            if  a != '':
                a = ''.join([char for char in a if char in string.digits])
                if len(a) > 0:
                    return int(a)
                else:
                    return 0
        return 0
    except TypeError:
        return 0

def s(a):
    try:
        if a != None:
            return str(a).strip().replace(u"\xa0", u" ")
        return ''
    except TypeError:
        return ''

