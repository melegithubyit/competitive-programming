class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = (celsius + 273.15) + 0.00000
        Far = (celsius * 1.80 + 32.00) + 0.00000
        return [kelvin, Far]
        