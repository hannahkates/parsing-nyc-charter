# Finding Keywords in the NYC City Charter

## When would this be useful?
If you want to find all the references to specific topics or keywords in the City Charter but don't know which section(s) they are in.

## What does the script do?
It intakes a [list of keywords](https://github.com/hannahkates/parsing-nyc-charter/blob/master/find_sections_with_keywords.py#L4) and a [text file of the NYC City Charter](https://github.com/hannahkates/parsing-nyc-charter/blob/master/document.txt). It iterates through each line of text in the NYC City Charter to see if one of the keywords is present. If it finds one of the keywords, it records the Chapter and Section number in a table. The final output is [`inventory.csv`](https://github.com/hannahkates/parsing-nyc-charter/blob/master/inventory.csv) a list of all Chapter and Section numbers that contain your keyword. This will allow you to then do targeted reading of only those sections, instead of the entire document.

## How to use
- Install python 3
- Install pandas
- Clone the github repository to you computer and navigate inside of it
- Update the keywords in the script according to your needs
- Run the script `python find_sections_with_keywords.py`
