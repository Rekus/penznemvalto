def currency_converter(amount, from_currency, to_currency):
    x = 1.15
    amount_1 = 0

    if amount < 0:
        print("Hibás összeg. Az átváltott összeg nem lehet negatív!")
        return

    if from_currency == "EUR" and to_currency == "USD":
        amount_1 = amount * x
    elif from_currency == "USD" and to_currency == "EUR":
        amount_1 = amount / x
    else:
        print("Hibás valuta párosítás!")
        return

    print("Átváltott összeg:", amount_1, to_currency)

#Tesztelés
currency_converter(100, "EUR", "USD")
currency_converter(100, "USD", "EUR")
currency_converter(-50, "EUR", "USD")
currency_converter(100, "GBP", "USD")