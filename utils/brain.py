import random
import pandas as pd

FILE_PATH = "data/messages.csv"

ROASTS = {
    "ghost": [
        "{user} exists only in the member list.",
        "{user} joined the server just to observe humanity.",
        "{user} is a professional lurker."
    ],
    "spam": [
        "{user} types faster than they think.",
        "{user} single-handedly keeps this server alive.",
        "{user} talks so much even the bot is tired."
    ],
    "night_owl": [
        "{user} fears sunlight and loves 3AM conversations.",
        "{user} sleeps when the server sleeps? Never."
    ],
    "one_liner": [
        "{user} believes one word is enough.",
        "{user} communicates exclusively in short bursts."
    ],
    "essay": [
        "{user} writes essays no one asked for.",
        "{user} thinks this is an English exam."
    ]
}

def generate_roast():
    df = pd.read_csv(FILE_PATH)

    user_stats = df.groupby("username").agg(
        total_msgs=("message_length", "count"),
        avg_length=("message_length", "mean")
    )
    
    user = random.choice(user_stats.index.tolist())
    stats = user_stats.loc[user]

    #deciding roast type
    if stats.total_msgs<5:
        category = "ghost"
    elif stats.total_msgs > 50:
        category = "spam"
    elif stats.avg_length < 5:
        category = "one_liner"
    elif stats.avg_length > 100:
        category = "essay"
    else:
        category = "night_owl"

    roast = random.choice(ROASTS[category])
    return roast.format(user=user)    