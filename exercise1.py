def analyze_message(message):
    upper_count = 0
    punct_count = 0
    alpha_count = 0
    consecutive_count = 1
    is_spam = False

    total_chars = len(message)

    for i in range(total_chars):
        char = message[i]

        if char.isupper():
            upper_count += 1

        if char.isalpha():
            alpha_count += 1

        if char == '!' or char == '?':
            punct_count += 1

        if i > 0:
            if message[i] == message[i - 1]:
                consecutive_count += 1
                if consecutive_count > 3:
                    is_spam = True
            else:
                consecutive_count = 1

    caps_ratio = 0
    if alpha_count > 0:
        caps_ratio = upper_count / alpha_count

    if caps_ratio >= 0.6 or punct_count >= 5:
        category = "AGGRESSIVE"
    elif caps_ratio >= 0.3 or punct_count >= 3:
        category = "URGENT"
    else:
        category = "CALM"

    return category, is_spam


if __name__ == "__main__":
    message = "HELLO!!! Are you there????"
    category, is_spam = analyze_message(message)
    print("Message:", message)
    print("Category:", category)
    print("Spam:", is_spam)
