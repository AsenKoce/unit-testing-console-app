exchange_rates = {
    "BGN": 1.0,
    "TRY": 7.5,   # 1 BGN = 7.5 TRY
    "EUR": 0.51,  # 1 BGN = 0.51 EUR
    "USD": 0.55   # 1 BGN = 0.55 USD
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency not in exchange_rates:
        return f"Грешка: '{from_currency}' не е поддържана валута."
    if to_currency not in exchange_rates:
        return f"Грешка: '{to_currency}' не е поддържана валута."
    
    amount_in_bgn = amount / exchange_rates[from_currency]
    
    converted_amount = amount_in_bgn * exchange_rates[to_currency]
    
    return f"{amount} {from_currency} са равни на {converted_amount:.2f} {to_currency}."

while True:
    try:
        print("\n Въведете 'стоп' за край на програмата.")
        from_currency = input("Въведете валутата, от която искате да преобразувате (BGN, TRY, EUR, USD): ").upper()
        if from_currency == 'СТОП':
            break
        to_currency = input("Въведете валутата, в която искате да преобразувате (BGN, TRY, EUR, USD): ").upper()
        if to_currency == 'СТОП':
            break
        amount = float(input("Въведете сумата за преобразуване: "))
        
        result = convert_currency(amount, from_currency, to_currency)
        print(result)
        
    except ValueError:
        print("Грешка: Моля, въведете валидно число за сумата.")
