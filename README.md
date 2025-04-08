# Kenya Airways Customer Review Analysis

## Project Overview
This project analyzes customer reviews of Kenya Airways collected from [Airline Quality](https://www.airlinequality.com/) to provide insights into passenger satisfaction, service quality metrics, and trends over time. The analysis helps identify strengths, weaknesses, and improvement opportunities for Kenya Airways' services.

## Live Dashboard
The interactive dashboard is available on Tableau Public:
[Kenya Airways Review Dashboard](https://public.tableau.com/views/kenyaairwaysreview/Dashboard1)

![image](https://github.com/user-attachments/assets/2f57e5c2-01f3-4889-93b1-8f528a899059)


## Motivation
The analysis was conducted to:
1. Understand customer perception of Kenya Airways across different service dimensions
2. Identify patterns in customer satisfaction based on variables like aircraft type, travel class, and traveler type
3. Track changes in customer sentiment over time
4. Map geographical differences in customer satisfaction
5. Provide actionable insights for service improvement

## Key Findings
- Kenya Airways has an overall average rating of 3.1/10
- Service metrics show that staff service (2.8/10) performs slightly better than other categories
- The lowest rated areas are ground service and value for money (both 2.1/10)
- Boeing 787/E190 aircraft received the highest ratings (5.2/10), while E190 alone received the lowest (1.4/10)
- Significant fluctuations in customer satisfaction appear across different months
- Reviews come from passengers across multiple continents, with varying satisfaction levels by country

## Data Collection
The data was collected using a Python web scraper that extracts reviews from Airline Quality website. The script:
- Collects basic review information (title, reviewer name, date, etc.)
- Extracts ratings for specific service aspects (seat comfort, staff service, etc.)
- Records reviewer metadata (traveler type, seat class, route, etc.)
- Captures reviewer location data for geographical analysis

## Technologies Used
- **Data Collection**: Python, BeautifulSoup, Requests
- **Data Processing**: Pandas, NumPy
- **Data Visualization**: Tableau Public
- **Geospatial Analysis**: Integration with Mapbox via Tableau

## Repository Contents
- `airline_review.py`: Python scraper code for collecting airline reviews
- `airline_reviews.csv`: Processed dataset of Kenya Airways reviews
- `Countries.csv`: Reference data for country mapping

## Dashboard Features
The interactive dashboard includes:
- Overall performance metrics across different service categories
- Monthly trend analysis of customer satisfaction (2016-2025)
- Aircraft type comparison showing ratings and review counts
- Geographical distribution of reviews and satisfaction levels
- Filtering options by traveler type, class, and other variables

## Future Work
Potential extensions to this analysis include:
- Sentiment analysis of review text to extract qualitative insights
- Comparative analysis with other African and global airlines
- Predictive modeling to forecast customer satisfaction based on service improvements
- Route-specific analysis to identify problematic flights or destinations

## License
This project is for educational and analytical purposes. The data has been collected from publicly available reviews.

## Acknowledgments
- Data sourced from [Airline Quality](https://www.airlinequality.com/)
- Visualization powered by Tableau Public
- Mapping support from Mapbox and OpenStreetMap
