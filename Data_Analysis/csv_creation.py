import csv
import random
from datetime import datetime, timedelta

# Sample data for mobile phone products with both positive and negative tweets
mobile_phones = ['iPhone', 'Samsung Galaxy', 'Google Pixel', 'OnePlus', 'Xiaomi']
positive_tweets = [
    "Just got my new {}! Loving it so far.",
    "The camera quality on the {} is amazing.",
    "Really happy with the performance of my new {}.",
    "The {} is really sleek and fast.",
    "The display on the {} is so vibrant and clear.",
    "The {} has exceeded my expectations!",
    "Battery life on the {} is excellent.",
    "My {} runs all my apps smoothly.",
    "I'm impressed with the build quality of the {}.",
    "The {} is a great value for the price."
]
negative_tweets = [
    "Battery life on the {} could be better.",
    "Having some issues with my {}. Anyone else?",
    "Not too impressed with the {}. Expected more.",
    "Why is my {} overheating?",
    "The {} keeps crashing. Frustrated!",
    "Touchscreen on my {} is unresponsive at times.",
    "My {} is slower than expected.",
    "Experiencing connectivity issues with the {}.",
    "The camera on the {} is disappointing.",
    "I regret buying the {}. Not worth the money."
]
sentiments=['positive','negative','neutral']

# Combine positive and negative tweets
all_tweets = positive_tweets + negative_tweets

# Generate random date
def random_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    )

# Define date range
start_date = datetime(2016, 7, 1)
end_date = datetime(2016, 9, 30)

# Generate CSV data for mobile phone products
mobile_rows = []
for i in range(2000):
    product = random.choice(mobile_phones)
    tweet = random.choice(all_tweets).format(product)
    date_time = random_date(start_date, end_date).strftime('%Y-%m-%d %H:%M:%S')
    sentiments = random.choice(sentiments)
    mobile_rows.append([product, tweet, date_time,sentiments])

# Write to CSV file
with open('mobile_phone_tweets_mixed.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['product', 'content', 'date_time','sentiments'])
    writer.writerows(mobile_rows)

print("CSV file 'mobile_phone_tweets_mixed.csv' has been created.")