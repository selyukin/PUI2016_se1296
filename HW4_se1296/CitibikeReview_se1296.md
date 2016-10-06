# HW4, Assignment 1
## Author: Sofiya Elyukin
## Reviewing Citibike Project Proposal for gsm317


### Part 1: The Null Hypothesis 
#### Idea: Young adults are more likely to choose biking for commuting.
#### Null Hypothesis: The ratio of subscribers aged 25-34 biking on weekends over biking on weekdays is the same or higher than the ratio of subscribers aged 35-44 biking over weekends to biking on weekdays.
   
    H0 : Old.weekend/Old.week <= Young.weekend/Young.week
    H1 : Old.weekend/Old.week > Young.weekend/Young.week

   The stated null hypothesis and formula match each other, however, they do not analyze commuting habits. Instead, they simply compare weekday vs. weekend use for young and old CitiBike subscribers. In order to analyze commuting habits, the null hypothesis should compare weekday rushhours to the rest of the weekday. Looking at weekdays and weekends as a whole would mean that even a 1pm Wednesday bike ride is considered a commute. Therefore, weekday should be replaced with rush hour, defined for example as 6am-9am and 4pm-7pm, and weekend should be replaced with the remaining times. Rephrasing the null hypothesis thusly would give you: The ratio of subscribers aged 35-44 biking during rush hours over those biking outside of rush hours is equal to or greater than the ratio of subscribers aged 25-34 biking during rush hours over those biking outside of rush hours. As formulas, the null and alternative hypotheses would then be:
     
     H0 : old.rushhour/old.nonrush >= young.rushhour/young.nonrushhour
     H1 : old.rushhour/old.nonrush < young.rushhour/young.nonrushhour
   
   
### Part 2: The Data
   
   The data necessary for this project are the ages of the subscribers and the times of the trips, taken from 'Date' (which was created by converting the 'startime' variable. Citibike users who are not subscribers were dropped from the dataframe, as were all columns aside from "Age" and "Date". The variable "age" was created by subtracting the values in the "Birth Year" column from 2016. While all ages below 25 and over 35 were dropped, this data should be further manipulated to create two bins for the two age groups being studied. Additionally, further work is necessary on the "Date" column. Currently, the value of each cell in this column represents the start day *and* start time of each trip. A 'split' is necessary to separate these two attributes. Once that is done, the day of the week for each date would need to be determined in order to drop all Saturday and Sunday rows. Trip times (based on hours) would then have to be categorized as occurring during or outside of rush hours. Even using the original null hypothesis, splitting the date column and ascribing a day of the week to each date would have been necessasy, with the difference being that time could be dropped and each trip would then have to be categorized as weekday or weekend.

### Part 3: The Test
   
   I would use a t-test for this project because it "looks at the difference between two groups on some variable of interest" (http://www.csun.edu/~amarenco/Fcs%20682/When%20to%20use%20what%20test.pdf). There is a single dichotomous independent variable, i.e. the age group that subscribers are in, and a single continuous dependent variable, i.e. the ratio of subscribers.