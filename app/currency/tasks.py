from bs4 import BeautifulSoup

from celery import shared_task

from currency import consts, model_choices as mch
from currency.models import Rate, Source
from currency.utils import to_decimal

from django.conf import settings
from django.core.mail import send_mail

import requests


@shared_task
def parse_privatbank():

    code_name = consts.CODE_NAME_PRIVATBANK
    source = Source.objects.filter(code_name=code_name).last()
    if source is None:
        source = Source.objects.create(code_name=code_name, name='PrivatBank')

    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'
    response = requests.get(url)
    response.raise_for_status()
    rates = response.json()
    available_currency_types = {
        'EUR': mch.RateTypeChoices.EUR,
        'USD': mch.RateTypeChoices.USD,
    }

    for rate in rates:
        buy = to_decimal(rate['buy'])
        sale = to_decimal(rate['sale'])
        currency_type = rate['ccy']
        source = source

        if currency_type not in available_currency_types:
            continue

        last_rate = Rate.objects\
            .filter(type=available_currency_types[currency_type], source=source)\
            .order_by('-created')\
            .first()

        if last_rate is None or last_rate.buy != buy or last_rate.sale != sale:
            Rate.objects.create(
                buy=buy,
                sale=sale,
                type=available_currency_types[currency_type],
                source=source,
            )


@shared_task
def parse_monobank():

    code_name = consts.CODE_NAME_MONOBANK
    source = Source.objects.filter(code_name=code_name).last()
    if source is None:
        source = Source.objects.create(code_name=code_name, name='MonoBank')

    url = 'https://api.monobank.ua/bank/currency'
    response = requests.get(url)
    response.raise_for_status()
    rates = response.json()
    rates_sorted = list(filter(lambda rate: "rateBuy" in rate and "rateSell" in rate and rate.get('currencyCodeB') == 980, rates))

    # for rate in rates:
    #     if "rateBuy" in rate and "rateSell" in rate and rate.get('currencyCodeB') == 980:
    #         rates_sorted.append(rate)

    available_currency_types = {
        978: mch.RateTypeChoices.EUR,
        840: mch.RateTypeChoices.USD,
    }

    for rate in rates_sorted:
        buy = to_decimal(rate['rateBuy'])
        sale = to_decimal(rate['rateSell'])
        currency_type = rate['currencyCodeA']
        source = source

        if currency_type not in available_currency_types:
            continue

        last_rate = Rate.objects \
            .filter(type=available_currency_types[currency_type], source=source) \
            .order_by('-created') \
            .first()

        if last_rate is None or last_rate.buy != buy or last_rate.sale != sale:
            Rate.objects.create(
                buy=buy,
                sale=sale,
                type=available_currency_types[currency_type],
                source=source,
            )


@shared_task
def parse_vkurse():

    code_name = consts.CODE_NAME_VKURSE
    Source.objects.get_or_create(code_name=code_name, name='Vkurse')
    source = Source.objects.filter(code_name=code_name).last()
    # if source is None:
    #     source = Source.objects.create(code_name=code_name, name='Vkurse')

    url = 'http://vkurse.dp.ua/course.json'
    response = requests.get(url)
    response.raise_for_status()
    rates = response.json()

    available_currency_types = {
        'Euro': mch.RateTypeChoices.EUR,
        'Dollar': mch.RateTypeChoices.USD,
    }

    for rate in rates.items():
        buy = to_decimal(rate[1].get('buy'))
        sale = to_decimal(rate[1].get('sale'))
        currency_type = rate[0]
        source = source

        if currency_type not in available_currency_types:
            continue

        last_rate = Rate.objects \
            .filter(type=available_currency_types[currency_type], source=source) \
            .order_by('-created') \
            .first()

        if last_rate is None or last_rate.buy != buy or last_rate.sale != sale:
            Rate.objects.create(
                buy=buy,
                sale=sale,
                type=available_currency_types[currency_type],
                source=source,
            )


@shared_task
def parse_alfabank():

    code_name = consts.CODE_NAME_ALFABANK
    source = Source.objects.filter(code_name=code_name).last()
    if source is None:
        source = Source.objects.create(code_name=code_name, name='AlfaBank')

    url = "https://old.alfabank.ua/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    currencies = soup.find(class_="currency-tab-block").find_all(class_='rate-number')
    rates = [
        {"type": mch.RateTypeChoices.USD,
         "buy": currencies[0].get_text().strip(),
         "sale": currencies[1].get_text().strip()
         },
        {"type": mch.RateTypeChoices.EUR,
         "buy": currencies[2].get_text().strip(),
         "sale": currencies[3].get_text().strip()
         }
    ]

    for rate in rates:
        buy = to_decimal(rate['buy'])
        sale = to_decimal(rate['sale'])
        currency_type = rate['type']
        source = source

        last_rate = Rate.objects \
            .filter(type=currency_type, source=source) \
            .order_by('-created') \
            .first()

        if last_rate is None or last_rate.buy != buy or last_rate.sale != sale:
            Rate.objects.create(
                buy=buy,
                sale=sale,
                type=currency_type,
                source=source,
            )


@shared_task
def parse_oschadbank():

    code_name = consts.CODE_NAME_OSCHADBANK
    source = Source.objects.filter(code_name=code_name).last()
    if source is None:
        source = Source.objects.create(code_name=code_name, name='OschadBank')

    url = "https://www.oschadbank.ua/currency-rate"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    currency_items = soup.find_all(class_="currency__item")
    eur = currency_items[0].find_all(class_="currency__item_value")
    usd = currency_items[1].find_all(class_="currency__item_value")

    rates = [
        {"type": mch.RateTypeChoices.USD,
         "buy": usd[0].get_text(),
         "sale": usd[1].get_text()
         },
        {"type": mch.RateTypeChoices.EUR,
         "buy": eur[0].get_text(),
         "sale": eur[1].get_text()
         }
    ]

    for rate in rates:
        buy = to_decimal(rate['buy'])
        sale = to_decimal(rate['sale'])
        currency_type = rate['type']
        source = source

        last_rate = Rate.objects \
            .filter(type=currency_type, source=source) \
            .order_by('-created') \
            .first()

        if last_rate is None or last_rate.buy != buy or last_rate.sale != sale:
            Rate.objects.create(
                buy=buy,
                sale=sale,
                type=currency_type,
                source=source,
            )


@shared_task
def parse_obmen_dp_ua():

    code_name = consts.CODE_NAME_OBMENDPUA
    source = Source.objects.filter(code_name=code_name).last()
    if source is None:
        source = Source.objects.create(code_name=code_name, name='ObmenDpUa')

    url = "https://obmen.dp.ua/?gclid" \
          "=Cj0KCQiA15yNBhDTARIsAGnwe0XvX9RmQcNF7wHEvkupWmEChvlqLFR0vNsV2ezHOijTXEorju7A_JsaAsY1EALw_wcB "
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    currencies_tab = soup.find(class_="currencies__tab-content")
    currencies_sale = currencies_tab.find_all(class_="currencies__block-sale")
    currencies_buy = currencies_tab.find_all(class_="currencies__block-buy")

    rates = [
        {"type": mch.RateTypeChoices.USD,
         "buy": currencies_buy[0].find(class_="currencies__block-num").get_text(),
         "sale": currencies_sale[0].find(class_="currencies__block-num").get_text()
         },
        {"type": mch.RateTypeChoices.EUR,
         "buy": currencies_buy[1].find(class_="currencies__block-num").get_text(),
         "sale": currencies_sale[1].find(class_="currencies__block-num").get_text()
         }
    ]

    for rate in rates:
        buy = to_decimal(rate['buy'])
        sale = to_decimal(rate['sale'])
        currency_type = rate['type']
        source = source

        last_rate = Rate.objects \
            .filter(type=currency_type, source=source) \
            .order_by('-created') \
            .first()

        if last_rate is None or last_rate.buy != buy or last_rate.sale != sale:
            Rate.objects.create(
                buy=buy,
                sale=sale,
                type=currency_type,
                source=source,
            )


@shared_task(
    autoretry_for=(ConnectionError,),
    retry_kwargs={'max_retries': 5},
)
def send_email_in_background(subject, body):
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [settings.DEFAULT_FROM_EMAIL],
        fail_silently=False,
    )
