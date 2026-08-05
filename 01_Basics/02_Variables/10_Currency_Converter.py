"""
Question:
Convert Indian Rupees to US Dollars.
"""

inr = float(input("Enter Amount in INR: "))

exchange_rate = 87.5

usd = inr / exchange_rate

print("Amount in USD =", round(usd, 2))