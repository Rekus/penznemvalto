def currency_converter(amount, from_currency, to_currency):
    exchange_rate = 1.15
    converted_amount=0

    if amount < 0:
        print("Hibás összeg. Az átváltott összeg nem lehet negatív!")
        return

    if from_currency == "EUR" and to_currency == "USD":
        converted_amount = amount * exchange_rate
    elif from_currency == "USD" and to_currency == "EUR":
        converted_amount = amount / exchange_rate
    else:
        print("Hibás valuta párosítás!")
        return

    print("Átváltott összeg:", converted_amount, to_currency)

#Tesztelés
currency_converter(100, "EUR", "USD")
currency_converter(100, "USD", "EUR")
currency_converter(-50, "EUR", "USD")
currency_converter(100, "GBP", "USD")
