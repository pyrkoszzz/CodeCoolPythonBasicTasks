class TemperatureConverter:

    @staticmethod
    def fahrenheit_to_celsius(temperature: float) -> float:
        return 32 + temperature * 9.0/5.0

    @staticmethod
    def celsius_to_fahrenheit(temperature: float) -> float:
        return 5.0 / 9.0 * (temperature - 32)


tc = TemperatureConverter()
celsius_temperature = 27
print(tc.celsius_to_fahrenheit(celsius_temperature))
