from utils import pull_classify_and_dump, n_most_least_positive, top_n_by_region

if __name__ == '__main__':
    print('______________________________________')
    print('  Geographic Word Sentiment Analyzer')
    print('       Created by John Tindel')
    print('______________________________________')
    print('   ')
    print('Instructions:')
    print('This program allows you to find the most positively- and negatively-associated words for a given locality')
    print('You will be asked to enter a name for the area you want to define (it doesn\'t matter what you name it, so long as it\'s understandable to you), then you will be prompted to enter either a city or state. You may enter more than one city/state.')
    print('Currently, you cannot enter both cities and states for analysis.')
    print('Once you have finished inputting locations, you will be asked whether to filter for only English-language reviews. If your search is for a multi-lingual area, this would be recommended.')
    print('--------------------------------------')
    print('Welome. To begin with, please provide a name for the area you want to analyze. The name is not important, but it should be something you will remember.')
    print('The name should not contain spaces.')
    name = input()
    while ' ' in name:
        print('Sorry, please enter a name without a space')
        name = input()
    print('How many positive/negative words do you want to view? Please enter an integer number (no decimals).')
    n = int(input())
    print('Would you like to base your search on cities or states? Please type "city" or "state" to indicate your choice.')
    city_state = input()
    while city_state not in ['city', 'state']:
        print('I\'m sorry, I didn\'t understand. Please type "city" or "state"')
        city_state = input()
    print('Would you like to search for a single ' + city_state + ', or several? Please type "single" or "several" to indicate your choice.')
    single_several = input()
    while single_several not in ['single', 'several']:
        print('I\'m sorry, I didn\'t understand. Please type "single" or "several".')
        single_several = input()
    print('Would you like to filter to remove non-English reviews? This may slow down the program, and might not be necessary in some areas. Type "yes" to filter for English, or "no" to not filter.')
    english_filter = input()
    while english_filter not in ['yes', 'no']:
        print('I\'m sorry, I didn\'t understand. Please type "yes" or "no".')
        english_filter = input()
    if english_filter == 'yes':
        check_english = True
    else:
        check_english = False
    if city_state == 'state':
        states = True
        citites = False
        if single_several == 'single':
            print('Enter the abbreviation for a state. For instance, instead of typing "Texas", enter "TX"')
            inputData = input()
        elif single_several == 'several':
            print('Please enter the states you would like to search for, separated by spaces. For instance, if you want to search for Minnesota and Wisconsin, type "MN WI"')
            inputData = input().split(' ')
    elif city_state == 'city':
        states = False
        cities = True
        if single_several == 'single':
            print('Enter the name of the city you would like to search for. It should be capitalized. For instance, "Edinburgh"')
            inputData = input()
        elif single_several == 'several':
            print('Please enter the names of the cities you would like to search for. For instance, "Edinburgh Glasgow"')
            inputData = input().split(' ')

    top_n_by_region(inputData, name, n, states = True, cities = False, check_english = False)

