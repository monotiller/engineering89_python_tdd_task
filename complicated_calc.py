class ComplicatedCalc:

    def divisible(self, num1, num2):
        return True if num1 % num2 == 0 else False

    def modulus(self, num1, num2):
        return num1 % num2

    def positive(self, num1):
        return True if num1 > 0 else False # Since 0 is neither positive or negative, the calculator will only count values 1 and above as positive