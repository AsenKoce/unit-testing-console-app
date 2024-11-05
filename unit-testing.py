import unittest

exchange_rates = {
    "BGN": 1.0,
    "TRY": 7.5,   # Примерен курс: 1 BGN = 7.5 TRY
    "EUR": 0.51,  # Примерен курс: 1 BGN = 0.51 EUR
    "USD": 0.55   # Примерен курс: 1 BGN = 0.55 USD
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency not in exchange_rates:
        return f"Грешка: '{from_currency}' не е поддържана валута."
    if to_currency not in exchange_rates:
        return f"Грешка: '{to_currency}' не е поддържана валута."
    
    amount_in_bgn = amount / exchange_rates[from_currency]
    converted_amount = amount_in_bgn * exchange_rates[to_currency]
    
    return f"{amount} {from_currency} са равни на {converted_amount:.2f} {to_currency}."

class TestCurrencyConverter(unittest.TestCase):
    def test_valid_conversion_bgn_to_eur(self):
        result = convert_currency(20, 'BGN', 'EUR')
        self.assertEqual(result, "20 BGN са равни на 10.20 EUR.")
    
    def test_invalid_from_currency(self):
        result = convert_currency(100, 'GBP', 'USD')
        self.assertEqual(result, "Грешка: 'GBP' не е поддържана валута.")
    
    def test_conversion_same_currency(self):
        result = convert_currency(100, 'BGN', 'BGN')
        self.assertEqual(result, "100 BGN са равни на 100.00 BGN.")
        
if __name__ == '__main__':
    unittest.main()
