{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define your apps data\n",
    "app_data = {\n",
    "    'App': ['Bumble', 'Tinder'],\n",
    "    'Payment Method': ['Premium Subscription', 'Premium Subscription'],\n",
    "    'Features': ['Chat', 'Dating'],\n",
    "    'Sentiment': ['Neutral', 'Positive'],\n",
    "    'Sentiment Score': [{'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0},\n",
    "                         {'neg': 0.0, 'neu': 0.756, 'pos': 0.244, 'compound': 0.3587}]\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a dataframe\n",
    "app_df = pd.DataFrame(app_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Initialize VADER sentiment analyzer\n",
    "sentiment_analyzer = SentimentIntensityAnalyzer()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Perform sentiment analysis for both apps\n",
    "for index, row in app_df.iterrows():\n",
    "    sentiment_scores = sentiment_analyzer.polarity_scores(row['Sentiment'])\n",
    "    app_df.at[index, 'Sentiment Score'] = sentiment_scores"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Data cleaning\n",
    "app_df['Sentiment Score'] = app_df['Sentiment Score'].apply(lambda x: {k: np.round(v, 2) for k, v in x.items()})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Data visualization\n",
    "# Pie chart for sentiment\n",
    "sentiment_compound = app_df['Sentiment Score'].apply(lambda x: x['compound'])\n",
    "plt.pie([sentiment_compound.sum(), 1 - sentiment_compound.sum()], labels=['Positive Sentiment', 'Negative Sentiment'])\n",
    "plt.title('Sentiment Analysis')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Bar chart for payment method and features\n",
    "payments = app_df['Payment Method'].value_counts()\n",
    "features = app_df['Features'].value_counts()\n",
    "\n",
    "plt.figure(figsize=(10,5))\n",
    "plt.subplot(1, 2, 1)\n",
    "plt.bar(payments.index, payments.values)\n",
    "plt.title('Payment Method')\n",
    "plt.xlabel('Payment Method')\n",
    "plt.ylabel('Count')\n",
    "\n",
    "plt.subplot(1, 2, 2)\n",
    "plt.bar(features.index, features.values)\n",
    "plt.title('Features')\n",
    "plt.xlabel('Features')\n",
    "plt.ylabel('Count')\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Competitive analysis\n",
    "def analyze_competition(df):\n",
    "    competition_df = pd.DataFrame(columns=['App', 'Competitive Advantage'])\n",
    "\n",
    "    for index, row in df.iterrows():\n",
    "        competitive_advantage = []\n",
    "\n",
    "        for i, comp_row in df.iterrows():\n",
    "            if i == index:\n",
    "                continue\n",
    "\n",
    "            if row['Payment Method'] != comp_row['Payment Method']:\n",
    "                competitive_advantage.append('Payment Method')\n",
    "\n",
    "            if row['Features'] != comp_row['Features']:\n",
    "                competitive_advantage.append('Features')\n",
    "\n",
    "            if row['Sentiment Score']['compound'] != comp_row['Sentiment Score']['compound']:\n",
    "                competitive_advantage.append('Sentiment')\n",
    "\n",
    "        competition_df.loc[index] = [row['App'], competitive_advantage]\n",
    "\n",
    "    return competition_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "      App             Competitive Advantage\n",
       "0  Bumble  [Sentiment]\n",
       "1  Tinder  [Sentiment]"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Print the results of the competitive analysis\n",
    "competition_df = analyze_competition(app_df)\n",
    "competition_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Visualization of competitive analysis\n",
    "competitive_advantage_counts = competition_df['Competitive Advantage'].apply(lambda x: len(x)).value_counts()\n",
    "plt.figure(figsize=(5,3))\n",
    "plt.pie(competitive_advantage_counts.values, labels=competitive_advantage_counts.index)\n",
    "plt.title('Competitive Advantage')\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
