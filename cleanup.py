#cleanup.py
def preprocess(rawDate):
    month = ""

    # Get Review
    review = rawDate

    # Dictionary of Months
    months = {
        "January":  1, "May":    5, "September": 9,
        "February": 2, "June":   6, "October":  10,
        "March":    3, "July":   7, "November": 11,
        "April":    4, "August": 8, "December": 12
    }

    # Target month from string and remove everything before it
    for key in months:
        if (review.find(key) != -1):
            index = review.find(key)
            temp_string = review[index:len(review)]
            month = months[key]
            break

    # Remove comma
    temp_string = temp_string.replace(",", "")

    # Split string and assign to variables
    temp_list = temp_string.split()
    day = temp_list[1]
    year = temp_list[2]

    # Cast to integers
    new_day = int(day)
    new_month = int(month)
    new_year = int(year)

    # Clean up String to follow YY MM DD format
    date = '%d %d %d' % (new_year, new_month, new_day)

    # Return the date String
    return date
