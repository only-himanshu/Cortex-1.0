import pandas as pd

FILE_PATH = "data/messages.csv"

def total_messages():
    df = pd.read_csv(FILE_PATH)
    return len(df)

def messages_per_user():
    df = pd.read_csv(FILE_PATH)
    return df.groupby("username").size().sort_values(ascending=False)

def night_owls():
    df = pd.read_csv(FILE_PATH)
    df["hour"] = pd.to_datetime(df["timestamp"]).dt.hour
    return df[df["hour"].between(0,4)]["username"].value_counts()


df = pd.read_csv("data/messages.csv")

#most active users
top_users = df.groupby("username")["message_length"].count().sort_values(ascending=False)
print(top_users.head(5))

#activity hours

df["timestamp"] = pd.to_datetime(df["timestamp"])
df["hour"] = df["timestamp"].dt.hour

peak_hours = df["hour"].value_counts().sort_index()
print(peak_hours)


if __name__=="__main__":
    print("Tottal message:", total_messages())
    print(messages_per_user())