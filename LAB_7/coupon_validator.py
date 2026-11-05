from datetime import datetime, date
import math


def split_code(code):
    if not isinstance(code, str):
        return None

    code = code.strip().upper()

    if code.count("-") != 1:
        return None

    prefix, value = code.split("-")

    if not prefix or not value:
        return None

    try:
        number = int(value)
    except ValueError:
        return None

    return prefix, number


def most_expensive(prices_csv):
    if not isinstance(prices_csv, str) or not prices_csv.strip():
        return None

    try:
        prices = [float(p.strip()) for p in prices_csv.split(",")]

        if not all(math.isfinite(p) and p >= 0 for p in prices):
            return None

        return max(prices)

    except ValueError:
        return None


def expiry_days(date_text):
    if not isinstance(date_text, str):
        return None

    try:
        expiry_date = datetime.strptime(date_text, "%Y-%m-%d").date()

        if expiry_date.isoformat() != date_text:
            return None

        start_date = date(2024, 1, 1)

        return (expiry_date - start_date).days

    except ValueError:
        return None


def main():
    print("==== Running split_code ====")
    user_input = input("Enter a coupon code (e.g. save-20): ")
    result = split_code(user_input)
    print("Prefix and Value:", result)

    print("\n==== Running most_expensive ====")
    user_input = input("Enter item prices as CSV (e.g. 199,49.5,320): ")
    result = most_expensive(user_input)
    print("Most Expensive Item:", result)

    print("\n==== Running expiry_days ====")
    user_input = input("Enter an expiry date as YYYY-MM-DD: ")
    result = expiry_days(user_input)
    print("Days Since 2024:", result)


if __name__ == "__main__":
    main()