# Python_Homework

## Table of Contents
* General Information
* PyBank Logic
* PyRamen Logic

## General Information

* On this homework assigment, both (PyBank and PyRamen) required of utilizing two of the most complex topics learned on week 2 : csv data extraction and list and/or dictionary looping.  

### PyBank Logic

* The project was divided in 2 parts:
    * Part A: consisted of the data collection and analysis to produce the first 2 items on the list: Total number of months and the net profit/loss of the entire file.
    * Part B: consisted of the data collection and analysis to obtain the monthly delta (profit/loss change per month) which, in turn, produced the answers for the rest of the requirements: avg. change on Profit/loss, greatest increase in profit (with the month that happened) and greates decrease in loss (with the month that it occured).
    * The block diagram (PyBank Logic and Analysis), shows the sequence or steps used to get in one dictionary: prior month PnL, current month PnL and Date from an initial dataset of month and PnL.  To get one dictionary with prior month and current month in same list, 2 extractions were processed from the budget_data.csv file, one extraction got skipped 1 row (the header) to generate prior PnL, while the second extraction skipped 2 rows (the header and the first data row) to generate current PnL and date. This was done based on the fact that the first data row has no prior month to compare it against.  
    * Once, all the data needed to obtain change (dictionary: "finrec"), a for loop calculates the change on each data row (month) and populated a dictionary named: "changes".
    * Finally, on "changes dictionary", a series of if statement compared each month to obtain the average change, the greatest increase in profits and the greatest decrease in profits (both with the month that they occured). 
    * Lastly, an output txt.file was generated to include the five metrics. 

![PyBank Analysis logic](Images/PyBank_diagram.jpg)


______________________________________
## Sources:
[1] (https://realpython.com/iterate-through-dictionary-python/)