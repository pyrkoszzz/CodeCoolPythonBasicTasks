from forex_python.converter import CurrencyRates


class CurrencyConverter:
    def __init__(self):
        self.currency_rates = CurrencyRates()

    def convert_currency(self, amount: float, from_currency: str, to_currency: str) -> (float, str):
        try:
            rate = self.currency_rates.get_rate(from_currency, to_currency)
            converted_amount = amount * rate
            return converted_amount, to_currency
        except Exception as e:
            return f"Conversion failed. Error: {e}"


if __name__ == "__main__":
    converter = CurrencyConverter()

    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the source currency code: ").upper()
    to_currency = input("Enter the target currency code: ").upper()

    result = converter.convert_currency(amount, from_currency, to_currency)

    if isinstance(result, tuple):
        converted_amount, target_currency = result
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {target_currency}.")
    else:
        print(result)
