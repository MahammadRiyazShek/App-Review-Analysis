import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Define your apps data
app_data = {
    'App': ['Bumble', 'Tinder'],
    'Payment Method': ['Premium Subscription', 'Premium Subscription'],
    'Features': ['Chat', 'Dating'],
    'Sentiment': ['Neutral', 'Positive'],
    'Sentiment Score': [{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0},
                         {'neg': 0.0, 'neu': 0.756, 'pos': 0.244, 'compound': 0.3587}]
}

# Create a dataframe
app_df = pd.DataFrame(app_data)

# Initialize VADER sentiment analyzer
sentiment_analyzer = SentimentIntensityAnalyzer()

# Perform sentiment analysis for both apps
for index, row in app_df.iterrows():
    sentiment_scores = sentiment_analyzer.polarity_scores(row['Sentiment'])
    app_df.at[index, 'Sentiment Score'] = sentiment_scores

# Data cleaning
app_df['Sentiment Score'] = app_df['Sentiment Score'].apply(lambda x: {k: np.round(v, 2) for k, v in x.items()})

# Data visualization
# Pie chart for sentiment
sentiment_compound = app_df['Sentiment Score'].apply(lambda x: x['compound'])
plt.pie([sentiment_compound.sum(), 1 - sentiment_compound.sum()], labels=['Positive Sentiment', 'Negative Sentiment'])
plt.title('Sentiment Analysis')
plt.show()

# Bar chart for payment method and features
payments = app_df['Payment Method'].value_counts()
features = app_df['Features'].value_counts()

plt.figure(figsize=(10,5))
plt.subplot(1, 2, 1)
plt.bar(payments.index, payments.values)
plt.title('Payment Method')
plt.xlabel('Payment Method')
plt.ylabel('Count')

plt.subplot(1, 2, 2)
plt.bar(features.index, features.values)
plt.title('Features')
plt.xlabel('Features')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# Competitive analysis
def analyze_competition(df):
    competition_df = pd.DataFrame(columns=['App', 'Competitive Advantage'])

    for index, row in df.iterrows():
        competitive_advantage = []

        for i, comp_row in df.iterrows():
            if i == index:
                continue

            if row['Payment Method'] != comp_row['Payment Method']:
                competitive_advantage.append('Payment Method')

            if row['Features'] != comp_row['Features']:
                competitive_advantage.append('Features')

            if row['Sentiment Score']['compound'] != comp_row['Sentiment Score']['compound']:
                competitive_advantage.append('Sentiment')

        competition_df.loc[index] = [row['App'], competitive_advantage]

    return competition_df

# Print the results of the competitive analysis
competition_df = analyze_competition(app_df)
print(competition_df)

# Visualization of competitive analysis
competitive_advantage_counts = competition_df['Competitive Advantage'].apply(lambda x: len(x)).value_counts()
plt.figure(figsize=(5,3))
plt.pie(competitive_advantage_counts.values, labels=competitive_advantage_counts.index)
plt.title('Competitive Advantage')
plt.show()