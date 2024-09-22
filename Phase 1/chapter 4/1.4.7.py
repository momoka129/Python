sentence = "I never expected it, but love found its way into my life. " \
           "Meeting you has been the most beautiful surprise, and now I know " \
           "what it feels like to truly care for someone. Together, we've built " \
           "something special, and I'm so grateful to have found love in you. " \
           "This journey has only just begun, and I can't wait to see where it takes us."

count = 0

for x in sentence:
    if x == 'a':
        count += 1

print(f"There are total {count} a in the sentence.")