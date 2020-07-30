import pandas as pd

# specify the keywords to look for
keywords = [
    "public review",
    "public hearing",
    "vote",
    "public participation"
]

# open the NYC city charter text file exported from
# http://library.amlegal.com/nxt/gateway.dll/New%20York/charter/newyorkcitycharter?f=templates$fn=default.htm$3.0$vid=amlegal:newyork_ny
f = open('document.txt', 'r')

# split the text content into individual lines
lines = f.readlines()

# create empty dataframe that will be used to capture sections of the charter that contain our targetted keywords
df = pd.DataFrame(columns=['Chapter', 'Section'])

i = 0
for line in lines:
    # get the chapter the line is within. this value stays constant until the next chapter is entered.
    if line.startswith('Chapter'):
        chapter = line[7:(len(line)-1)]

    # get the section the line is within. this value stays constant until the next section is entered.
    if line.startswith('Section'):
        section = line[7:(len(line)-1)]

    # count the number keywords that are present in the line of text
    count = 0
    for keyword in keywords:
        count += line.count(keyword)

    # if at least one keyword is present in the line of text, append the current chapter-section to the dataframe
    if count > 0:
        df = df.append({'Chapter' : chapter , 'Section' : section} , ignore_index=True)

    # increase line number for next line
    i += 1

# remove duplicate chapters and sections
df = df.drop_duplicates()

# save the dataframe to a csv file
df.to_csv('inventory.csv')
