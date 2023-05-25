from textblob import TextBlob
import pyttsx3

engine = pyttsx3.init()

heading = """
 __  __  _         _       _                          __  __        __              _    
|  \/  |(_) _ __  (_) ___ | |_  _ __  _   _    ___   / _| \ \      / /  ___   _ __ | | __
| |\/| || || '_ \ | |/ __|| __|| '__|| | | |  / _ \ | |_   \ \ /\ / /  / _ \ | '__|| |/ /
| |  | || || | | || |\__ \| |_ | |   | |_| | | (_) ||  _|   \ V  V /  | (_) || |   |   <
|_|  |_||_||_| |_||_||___/ \__||_|    \__, |  \___/ |_|      \_/\_/    \___/ |_|   |_|\_\\
                                      |___/


"""


def get_polarity(phrase):
    return TextBlob(phrase).sentiment.polarity


print(heading)
engine.say(
    "Hello Employee number 2445320! We hope you had a great day at work. It's time to submit your employee wellness statement"
)

engine.say("Enter your employee wellness statement: ")
engine.runAndWait()
phrase = input("> ")
blob = TextBlob(phrase)
while (get_polarity(phrase)) < 0.5:
    print("Please try again and be more positive this time: ")
    engine.say(
        "Employee number 2445320! That was not a very positive employee wellness statement. Please try again and be more positive this time. We know how much you love working here!"
    )
    engine.runAndWait()
    phrase = input("> ")

print("We appreciate you too!")
engine.say(
    "Employee number 2445320! Thank you for such a kind and positive statement! We here are the ministry of work appreciate you too! Have a great day!"
)
engine.runAndWait()
