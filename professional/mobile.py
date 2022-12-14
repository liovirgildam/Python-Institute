class Mobile:
    # simple mobile class
    def __init__(self, number):
        self.number = number

    def turn_on(self):
        return f"mobile phone {self.number} is turned on."

    def turn_off(self):
        return f"mobile phone is turned off."

    def calling(self, number):
        return f"calling {number}"

lio_phone = Mobile("0011-2345")
lia_phone = Mobile("0011-6789")
print(lia_phone.turn_on())
print(lio_phone.turn_on())
print(lia_phone.calling("0011-2435"))
print(lio_phone.turn_off())
print(lia_phone.turn_off())
