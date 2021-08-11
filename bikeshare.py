#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__author__ = 'Ahmad Abdulnasir Shuaib <me@ahmadabdulnasir.com.ng>'
__homepage__ = https://ahmadabdulnasir.com.ng
__copyright__ = 'Copyright (c) 2021, salafi'
__version__ = "0.01t"
"""

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'DATA/chicago.csv',
              'new york city': 'DATA/new_york_city.csv',
              'washington': 'DATA/washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    get_city_input = True
    city = ''
    while get_city_input:
        selected_city = input("Please Select a City: ")
        if selected_city.lower() in CITY_DATA.keys():
            city = selected_city.lower()
            get_city_input = False
            break
        else:
            print("Invalid Choice of City: {}.\n Valid Choice are: {}".format(selected_city, CITY_DATA.keys()))
    # TO DO: get user input for month (all, january, february, ... , june)
    get_month_input = True
    month = ''
    allowed_month_choice = ["all", "january", "febuary", "march", "april" "may", "june"]
    while get_month_input:
        selected_month = input("Please Select a Month: ")
        if selected_month.lower() in allowed_month_choice:
            month = selected_month.lower()
            get_month_input = False
            break
        else:
            print("Invalid Choice of Month: {}.\nValid Choice are: {}".format(selected_month, allowed_month_choice))
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    get_day_input = True
    day = ''
    allowed_day_choice = ["all", "monday", "tuesday", "wednesday", "thursday" "friday", "saturday", "sunday"]
    while get_day_input:
        selected_day = input("Please Select a Day: ")
        if selected_day.lower() in allowed_day_choice:
            day = selected_day.lower()
            get_day_input = False
            break
        else:
            print("Invalid Choice of Day: {}.\nValid Choice are:{}".format(selected_day, allowed_day_choice))
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month, day of week, hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('The Most Popular Month is:- ', popular_month)

    # display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('The Most Day Of Week is:- ', popular_day_of_week)

    # display the most common start hour
    popular_common_start_hour = df['hour'].mode()[0]
    print('The Most Common Start Hour is:- ', popular_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The Most Start Station is:- ', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The Most End Station is:- ', popular_end_station)

    # display most frequent combination of start station and end station trip
    grouped_field = df.groupby(['Start Station','End Station'])
    popular_combination_station = grouped_field.size().sort_values(ascending=False).head(1)
    print('The Most frequent combination of Start Station and End Station trip is:-')
    print(popular_combination_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:- ', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:- ', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User Stats:- ')
    print(df['User Type'].value_counts())

    if city != 'washington':
        # washington city data has no Gender and Birth Year, as such we cannot perform the calculations below
        # Display counts of gender
        print('Gender Stats:- ')
        print(df['Gender'].value_counts())

        # Display earliest, most recent, and most common year of birth
        print('Birth Year Stats:- ')
        most_common_year = df['Birth Year'].mode()[0]
        print('Most Common Year:',most_common_year)
        most_recent_year = df['Birth Year'].max()
        print('Most Recent Year:- ',most_recent_year)
        earliest_year = df['Birth Year'].min()
        print('Earliest Year:- ',earliest_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
