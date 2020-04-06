import time
import pandas as pd
import numpy as np

# CITY_DATA
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# Define Months
months = ['january','february','march','april','may','june']

# Define Week_Days
week_days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

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
    print('Please Enter your city choice!')
    city = input().lower()
    while(city not in ['chicago','new york city', 'washington']):
        print('Please reenter your city choice!')
        city = input().lower() 
    
    # Get user input for month (all, january, february, ... , june)
    print('Please Enter your month choice(all means all selected)!')
    month = input().lower()
    while(month not in ['all','january','february','march','april','may','june']):
        print('Please reenter your month choice!')
        month = input().lower() 

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('Please Enter your weekday choice(all means all selected)!')
    day = input().lower()
    while(day not in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']):
        print('Please reenter your day choice!')
        day = input().lower() 
        
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
    
    # drop na
    df.dropna(inplace =True)
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month']==month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']== day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('Most common month is:',months[df.month.mode()[0]-1])

    # TO DO: display the most common day of week
    print('Most common week day is:', df.day_of_week.mode()[0])

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Hour'] = df['Start Time'].dt.hour
    print('Most Frequent Start Hour:', df['Hour'].mode()[0])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most Commonly Used Start Station is:',df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Most Commonly Used End Station is:',df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    # Exclude the cases when 'Start Station' == 'End Station'
    df = df[df['Start Station']!=df['End Station']]
    df['Combo_stations'] = df['Start Station'] + ' TO ' + df['End Station']
    print('Most Commonly Used Start Station is:',df['Combo_stations'] .mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Travel Time is:', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Total Travel Time is:', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of User Types__\n', df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print('Counts of Gender__\n', df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    df.dropna(inplace=True)
    #df.sort_values(by = ['Birth Year'], ascending = True, inplace = True)
    #print(df['Birth Year'].head())
    #print(df['Birth Year'].tail())
    #print(df['Birth Year'])
    if 'Birth Year' in df.columns:
        print('Earliest year of birth is :', df['Birth Year'].min())
        print('Most Recent year of birth is :', df['Birth Year'].max())
        print('Most Common year of birth is :', df['Birth Year'].mode()[0])
    
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
