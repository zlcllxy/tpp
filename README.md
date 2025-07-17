# Taiwan People's Party Facebook Selected "Recall" Topic Posts Sentiment Analysis Project README

Through **Apify Facebook Posts Scraper**, I extracted 100 posts containing the keyword "recall" from Taiwan People's Party (TPP) official fan page before July 17, 2025, and completed the analysis. The results and process are detailed below.

## 1 Research Motivation

The 2025 recall election has become the most central issue in Taiwanese politics. As the upcoming recall vote targets Legislative Yuan members all affiliated with the Kuomintang (KMT), whether the Taiwanese People's Party, a key third party cooperating with the KMT in the legislature, can assist those facing recall in opposing it has become a focal point for external observers. Official party social media posts often influence the direction of issues and public sentiment. This study focuses on the Taiwanese People's Party’s official Facebook page, analysing the sentiment of posts related to the "recall" to observe how the party promotes the recall issue and what the effects are. Due to funding limitations, only the 100 posts made before the pre-voting publicity cooling-off period were selected for analysis.

## 2 Method Overview

| Step | Technology/Package | Output |
|------|-------------------|---------|
| Data Extraction | Apify Facebook Posts Scraper | `tpp_posts.csv` |
| Data Cleaning | pandas | `tpp_dabaimian.csv` |
| Sentiment Classification | SnowNLP | `tpp_dabaimian_sentiment.csv` |
| Engagement Calculation | pandas | `sentiment_engagement_summary.csv` |
| Result Visualization | seaborn, matplotlib | `Figure_1.jpg`, `Figure_2.jpg` |

### Classification Thresholds
- Positive: sentiment score > 0.6
- Neutral: 0.4 ≤ sentiment score ≤ 0.6
- Negative: sentiment score < 0.4

### Engagement Metrics
`total_engagement = likes + comments + shares`

## 3 Environment Setup

```bash
python -m venv venv
source venv/bin/activate          # Windows use venv\Scripts\activate
pip install -r requirements.txt   # Install dependencies
```

## 4 Execution Method

1. Place `tpp_posts.csv` in the project root directory.
2. Execute in terminal:
   ```bash
   python clean.py
   ```
   The script will sequentially complete data filtering, sentiment analysis, engagement calculation, and output all intermediate and final result files while automatically generating two analysis charts.
3. Open `Figure_1.jpg` and `Figure_2.jpg` to view the visualization results.

## 5 Main Results

### 5.1 Post Sentiment Distribution
- **Negative** accounts for over 90%, showing that TPP primarily uses critical and warning tones when discussing recalls.

### 5.2 Average Engagement by Sentiment Category
- **Positive** posts, though having the lowest proportion, have the highest average engagement; negative posts are most numerous but show moderate engagement performance, indicating that positive mobilization language is more effective in triggering fan participation.

## 6 File Structure

```text
├── clean.py
├── tpp_posts.csv
├── tpp_dabaimian.csv
├── tpp_dabaimian_sentiment.csv
├── sentiment_engagement_summary.csv
├── Figure_1.jpg
├── Figure_2.jpg
└── README.md   ← Current file
```

## 7 Conclusions and Future Work

1. **Conclusions**
   - After reviewing the texts classified by the system as having positive and negative sentiments, it can be observed that posts regarded as having negative emotions mostly directly call for opposing the recall, while those regarded as having positive emotions are primarily texts criticising the ruling party’s policies. Among the TPP “withdrawal” posts, those directly opposing the recall constitute the vast majority, but texts criticising the ruling party appear to be more effective in driving engagement.
2. **Limitations**
   - The sample size of posts is insufficient; this study cannot further determine the relationship between the level of interaction on posts and their ultimate mobilisation capability.