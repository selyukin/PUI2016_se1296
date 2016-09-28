##HW #2 for PUI2016, Thursday class

### Author: Sofiya Elyukin, se1296

I collaborated with Sebastian Bana, Jonathan Geis, Luis Fernando Melchor 
Fernandez, Ben Alpert, and Marc Toneatto. Actual coding for each
script here was done individually (but with code borrowing) after a breakdown
and discussion of mostly complete scripts.

#### Assignment 1
This assignment required writing a script which loaded the MTA's realtime bus
data in json format, and then parsed the data to find how many active buses
there are for a given line and where those buses are located. 

Sebastian walked Jonathan, Fernando, and me through his script. Jonathan and I
later did the same for Ben and Marc. Specific instances of code-borrowing for 
my own script are specified in its comments.

#### Assignment 2
This assignment expanded on the previous one. Additional parsing was necessary
to determine what the next stop would be and where the bus is in relation to it,
and then the result had to be output as a CSV file as opposed to inline. An if/else
statement was necessary to account for an empty field within the dictionary holding
next stop information. 

Sebastian walked Jonathan, Fernando, and me through his script. We then jointly
refined it, specifically to account for N/A values when retrieving information
on the next stop. Specific instances of code borrowing for my own script are
specified in its comments.

#### Assignment 3:
This assignment pulled a CSV file from the CUSP Data Facility. Pandas was used 
to create a dataframe through which to manipulate/clean the data. The file I
used turned out to have its numerical values stored as strings, so it was
necessary to convert them to float. The two attributes were then plotted against
each other using .plot.

Fernando walked Sebastian, Jonathan, and me through his (then partial) script,
and we adjusted it to use the DFDATA environmental variable to retreive the
CSV file. Specific instances of code borrowing for my own script are specified
in its comments.
