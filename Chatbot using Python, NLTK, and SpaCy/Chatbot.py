import nltk
from nltk.chat.util import Chat, reflections

# Define the rules for our chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?", ]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there", ]
    ],
    [
        r"what is your name ?",
        ["I am a bot created by Zayab Akhtar. you can call me crazy!", ]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?", ]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind", ]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?", ]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that", "How can I help you?:)", ]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude\nSeriously you are asking me this?", ]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse", ]
    ],
    [
        r"(.*) created ?",
        ["Zayab created me using Python's NLTK library ", "top secret ;)", ]
    ],
    [
        r"(.*) (location|city) ?",
        ['Pakistan, Islamabad', ]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always", "Too hot man here in %1", "Too cold man here in %1", "Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.", ]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2", "Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ", ]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football", ]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy", "Ronaldo", "Roony"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
    ],
    [
        r"i am looking for online guides and courses to learn data science, can you suggest?",
        ["Crazy_Tech has many great articles with each step explanation along with code, you can explore"]
    ],
    [
        r"quit",
        ["BBye take care. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ],
]

# Create the chatbot
chat = Chat(pairs, reflections)

# Start the conversation
def start_conversation():
    print("Hi! I am a chatbot created by Zayab Akhtar for your service")
    chat.converse()

# Call the function to start the conversation
start_conversation()