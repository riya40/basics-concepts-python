class Functions:
    @staticmethod
    def payment_calculation(principle, rate_of_interest, years):
        n = 12 * years
        r = rate_of_interest / (12 * 100)
        payment = (principle * r) / (1 - (1 + r) ** (-n))
        return payment

    def addition(a,b):
        c = a+b
        return c