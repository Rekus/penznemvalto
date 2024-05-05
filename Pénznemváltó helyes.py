def get_exchange_rate(from_currency, to_currency):
    exchange_rates = {
        ("EUR", "USD"): 1.15,
        ("USD", "EUR"): 1/1.15
    }
    return exchange_rates.get((from_currency, to_currency))

def convert_currency(amount, from_currency, to_currency):
    if amount <= 0:
        print("Hibás összeg. Az átváltott összegnem lehet negatív!")
        return

    exchange_rate = get_exchange_rate(from_currency, to_currency)
    if exchange_rate is None:
        print("Hibás valuta párosítás!")
        return
    converted_amount = amount * exchange_rate

    print("Az átváltott összeg:", converted_amount, to_currency)

#Tesztelés
convert_currency(100, "EUR", 'USD')
convert_currency(100, "USD", "EUR")
convert_currency(-50, "EUR", "USD")
convert_currency(100, "GBP", "USD")

