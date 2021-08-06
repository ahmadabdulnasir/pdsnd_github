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
         else:
            print(f"Invalid Choice of City: {selected_city}"
    # TO DO: get user input for month (all, january, february, ... , june)
    get_month_input = True
    month = ''
    allowed_month_choice = ["all", "january", "febuary", "march", "april" "may", "june"]
    while get_month_input:
        selected_month = input("Please Select a City: ")
        if selected_month.lower() in allowed_month_choice:
            month = selected_month.lower()
            get_month_input = False
        else:
            print(f"Invalid Choice of Month: {selected_month}"


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    get_day_input = True
    day = ''
    allowed_day_choice = ["all", "monday", "tuesday", "wednesday", "thursday" "friday", "saturday", "sunday"]
    while get_day_input:
        selected_day = input("Please Select a Day: ")
        if selected_day.lower() in allowed_day_choice:
            month = selected_day.lower()
            get_day_input = False
        else:
            print(f"Invalid Choice of Day: {selected_day}"


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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


def boot():
    pass

if __name__ == "__main__":
    boot()
