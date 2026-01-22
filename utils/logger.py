import csv
import os
from datetime import datetime



def log_message(message):

    FILE_PATH = "data/messages.csv"
    os.makedirs("data", exist_ok=True)

    file_exists = os.path.isfile(FILE_PATH)

    with open(FILE_PATH, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        #write header here once
        if not file_exists:
            writer.writerow([
                "user_id",
                "username",
                "channel",
                "timestamp",
                "message_length"
            ])

        writer.writerow([
            message.author.id,
            message.author.name,
            message.channel.name,
            message.created_at.isoformat(),
            len(message.content)
        ])    