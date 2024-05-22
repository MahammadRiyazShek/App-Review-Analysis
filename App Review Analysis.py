import pandas as pd
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

# Print the updated dataframe
print(app_df)

# Perform competitive analysis
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
print(analyze_competition(app_df))
