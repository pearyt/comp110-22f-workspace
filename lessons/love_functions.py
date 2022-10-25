subject = input("Who do you love? ")

def love(subject: str):
    return f"I love you {subject}!"

print(love(subject))


n = int(input("How many times to iterate?"))
def spread_love(subject: str, n: int):
    love_note = ""
    var = 0
    while var <= n:
        love_note += love(subject)
        love_note += "\n"
        var += 1
    return love_note


print(spread_love("Bob", 2))
