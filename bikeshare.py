import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#Refactoring code change 1
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
    while True:
        city = input('Would you like to see data for Chicago, New York City, or Washington?').lower()
        if city not in ['chicago','new york city','washington']:
            print('Please enter a valid city name from the list (chicago,new york,washington)')
        else:
            break
    # TO DO: get user input for month (all,    january, february, ... , j 
    while True:
        month= input('Which month data you would like to see - (January, February,....,June) or "All"?').lower()
        if month not in ['all','january','february','march','april','may','june']:
            print('Please enter a valid day of week January, February, March, April, May,June or All:')
        else:
            break       
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day= input('which day data would you like to see- Monday, Tuesday, ... Sunday or "All"?').lower()
        if day not in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
            print('Please enter a valid day of week (Monday, Tuesday, ... Sunday or All):')
        else:
            break
    print('-'*40)
    return city, month, day

#Refactoring code changes 2
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
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day and hour of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.strftime('%B')
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        df = df[df['month']==month.title()]
    if day != 'all':
        df = df[df['day_of_week']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('Most common month :',df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('Most common day of the week :',df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print('Most common start hour :',df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most common start station :',df['Start Station'].mode()[0]);

    # TO DO: display most commonly used end station
    print('Most common end station :',df['End Station'].mode()[0]);

    # TO DO: display most frequent combination of start station and end station trip
    # group by and size() will give the distinct count of start and end stations
    # we can then sort the values and extract the index 
    print('Frequent combination of start and end station trip :',df.groupby(['Start Station','End Station']).size().sort_values(ascending=False).index.tolist()[0])
    
    # perform a group by , sort and extract the first value                  
    print('Total trips between these 2 stations :',df.groupby(['Start Station','End Station']).size().sort_values(ascending=False)[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time in hours :',df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Average travel time in mins:',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print()
    print('Displaying User Type breakdown:\n')
    print(df['User Type'].value_counts().to_string())

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('\nDisplaying Gender counts:\n')
        print(df['Gender'].value_counts().to_string())
    else:
        print('No Gender data to report!')
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('\nDisplaying year of birth stats:\n')
        print('Earliest birth year :',int(df['Birth Year'].min()))
        print('Most recent birth year :',int(df['Birth Year'].max()))
        print('Most common birth year :',int(df['Birth Year'].mode()[0]))
    else:
        print('No Birth Year data to report!')
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        print('User input : City - {} , Month - {} , Day - {}'.format(city,month,day))
        
        df = load_data(city, month, day)
        #print(df.head())
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
