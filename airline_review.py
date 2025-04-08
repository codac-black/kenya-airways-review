import random
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import re

airlines_input = ['kenya-airways'] # you can include other airlines 
airline = []
overall_rating = []
review_title = []
name = []
date = []
verified = []
reviews = []
type_of_traveller = []
seat_type = []
route = []
date_flown = []
foodbev = []
entertainment = []
seat_comfort = []
staff_service = []
money_value = []
recommended = []
ground_service = []
wifi_connectivity = []
aircraft = []
place = []  # Added new list for place/location

def airline_inp(inp):
    mapping = {
        'singapore-airlines': 'Singapore Airlines',
        'qatar-airways': 'Qatar Airways',
        'ana-all-nippon-airways': 'All Nippon Airways',
        'emirates': 'Emirates',
        'japan-airlines': 'Japan Airlines',
        'turkish-airlines': 'Turkish Airlines',
        'air-france': 'Air France',
        'cathay-pacific-airways': 'Cathay Pacific Airways',
        'eva-air': 'EVA Air',
        'korean-air': 'Korean Air',
        'kenya-airways': 'Kenya Airways'
    }
    airline.append(mapping.get(inp, 'Unknown Airline'))

def fill_with_value(lst, length, value):
    if len(lst) >= length:
        lst.pop()
    while len(lst) < length:
        lst.append(value)

def fill_values(lst, length):
    if len(lst) >= length:
        lst.pop()
    while len(lst) < length:
        if lst == overall_rating:
            lst.append(random.randint(1, 10))
        elif lst == verified:
            lst.append(random.choice(['Trip Verified', 'Not Verified']))
        elif lst == type_of_traveller:
            lst.append(random.choice(['Solo Leisure', 'Family Leisure', 'Couple Leisure', 'Business']))
        elif lst == seat_type:
            lst.append(random.choice(['Economy Class', 'Business Class', 'Premium Economy', 'First Class']))
        elif lst == route or lst == date_flown or lst == aircraft:
            lst.append('undefined')
        elif lst == place:  # Add handling for place list
            lst.append('Not Specified')

features1 = [verified, overall_rating, type_of_traveller, seat_type, route, date_flown, aircraft, place]  # Added place to features
features2 = [foodbev, entertainment, seat_comfort, staff_service, money_value, ground_service, wifi_connectivity]

for airline_input in airlines_input:
    website = f'https://www.airlinequality.com/airline-reviews/{airline_input}'
    page_size = 100
    page = 30

    for i in range(1, page + 1):
        print(f"Scraping data from {airline_input} Page {i} ")
        url = f"{website}/page/{i}/?sortby=post_date%3ADesc&pagesize={page_size}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        review_ratings = soup.find_all('div', {'itemprop': 'reviewRating'})
        for rating in review_ratings:
            rating_value = rating.find("span", {"itemprop": "ratingValue"})
            if rating_value:
                overall_rating.append(rating_value.get_text())

        retitle = soup.find_all('div', {'class': 'body'})
        for title in retitle:
            review_value = title.find("h2", {"class": "text_header"})
            if review_value:
                review_title.append(review_value.get_text())

        # Extract name and place together
        for header in soup.find_all("h3", {"class": "text_sub_header"}):
            # Find the name span
            name_span = header.find("span", {"itemprop": "name"})
            if name_span:
                name.append(name_span.get_text())
                
                # Extract place from the full h3 text
                full_text = header.get_text()
                location_match = re.search(r'\(([^)]+)\)', full_text)
                if location_match:
                    place.append(location_match.group(1))
                else:
                    place.append('Not Specified')
                
        for para in soup.find_all("time", {"itemprop": "datePublished"}):
            date.append(para.get_text())
        for para in soup.find_all("em"):
            verified.append(para.get_text())
        for para in soup.find_all("div", {"class": "text_content"}):
            reviews.append(para.get_text())
            airline_inp(airline_input)

        rows = soup.find_all('tr')
        for row in rows:
            header = row.find('td', class_='review-rating-header')
            value_td = row.find('td', class_='review-value')
            star_td = row.find('td', class_='review-rating-stars')

            if header:
                header_text = header.text.strip()
                if value_td:
                    value_text = value_td.text.strip()
                    if header_text == 'Type Of Traveller':
                        type_of_traveller.append(value_text)
                    elif header_text == 'Seat Type':
                        seat_type.append(value_text)
                    elif header_text == 'Route':
                        route.append(value_text)
                    elif header_text == 'Date Flown':
                        date_flown.append(value_text)
                    elif header_text == 'Recommended':
                        recommended.append(value_text)
                    elif header_text == 'Aircraft':
                        aircraft.append(value_text)

                if star_td:
                    star_count = star_td.find_all('span', class_='star fill')
                    if header_text == 'Seat Comfort':
                        seat_comfort.append(len(star_count))
                    elif header_text == 'Cabin Staff Service':
                        staff_service.append(len(star_count))
                    elif header_text == 'Food & Beverages':
                        foodbev.append(len(star_count))
                    elif header_text == 'Inflight Entertainment':
                        entertainment.append(len(star_count))
                    elif header_text == 'Value For Money':
                        money_value.append(len(star_count))
                    elif header_text == 'Ground Service':
                        ground_service.append(len(star_count))
                    elif header_text == 'Wifi & Connectivity':
                        wifi_connectivity.append(len(star_count))

        print(f"   ---> {len(reviews)} Total records")

    print(f'done scraping {airline_input}')
    target_length = len(reviews)

    while True:
        for feat1 in features1:
            fill_values(feat1, target_length)
        for feat2 in features2:
            value_to_fill = random.randint(1, 5)
            fill_with_value(feat2, target_length, value_to_fill)
        if all(len(lst) == target_length for lst in features1 + features2):
            break

    print("All lists are now of equal length.")

    df = pd.DataFrame()
    df['Title'] = review_title
    df['Name'] = name
    df['Place'] = place  # Add the new Place column
    df['Review Date'] = date
    df['Airline'] = airline
    df['Verified'] = verified
    df['Reviews'] = reviews
    df['Type of Traveller'] = type_of_traveller
    df['Month Flown'] = date_flown
    df['Route'] = route
    df['Class'] = seat_type
    df['Aircraft'] = aircraft
    df['Seat Comfort'] = seat_comfort
    df['Staff Service'] = staff_service
    df['Food & Beverages'] = foodbev
    df['Inflight Entertainment'] = entertainment
    df['Ground Service'] = ground_service
    df['Wifi & Connectivity'] = wifi_connectivity
    df['Value For Money'] = money_value
    df['Overall Rating'] = overall_rating
    df['Recommended'] = recommended

    df['Reviews'] = df['Reviews'].str.split('|', expand=True)[1]
    df['Title'] = df['Title'].str.replace('"', '')
    df['Reviews'].replace('None', np.nan, inplace=True)
    df = df.dropna(subset=['Reviews'])
    df['Verified'] = df['Verified'].replace({'Trip Verified': True, 'Not Verified': False})
    df['Review Date'] = pd.to_datetime(df['Review Date'], format='mixed', errors='coerce')
    df['Overall Rating'] = df['Overall Rating'].astype(int)

    df.to_csv('airline_reviews.csv', index=False)
