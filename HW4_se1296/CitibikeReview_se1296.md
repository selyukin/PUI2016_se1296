# HW4, Assignment 1
## Author: Sofiya Elyukin
## Reviewing Citibike Project Proposal of Gregory Mayes (gsm317)


### Part 1: The Null Hypothesis 
#### Idea: Young adults are more likely to choose biking for commuting.
#### Null Hypothesis: The ratio of subscribers aged 25-34 biking on weekends over biking on weekdays is the same or higher than the ratio of subscribers aged 35-44 biking over weekends to biking on weekdays.
    H0 : Old.weekend/Old.week <= Young.weekend/Young.week
    H1 : Old.weekend/Old.week > Young.weekend/Young.week

   I believe the stated null hypothesis is in fact the alternative hypothesis. Because we hope to reject the null hypothesis, it should state the opposite  of what one expects or hopes the research result to be. Therefore, given that the research idea is that young adults are **more** likely to use Citibike for commuting, the null hypothesis should be that their ratio is the same or **lower** than the ratio for adults aged 35-44. Written out as formulas, the null and alternative hypotheses are, respectively:
    
    H0 : Old.weekend/Old.week >= Young.weekend/Young.week
    H1 : Old.weekend/Old.week < Young.weekend/Young.week


### The Data
The data necessary for this project are the ages of the subscribers and the days of the trips. Citibike users who are not subscribers were dropped from the dataframe, as were all columns aside from "Age" and "Date". The variable "age" was created by converting the "Birth Year" column. Further work is necessary though in order to change the format of the "Date" column. Currently the data is in the form of 'YYYY-MM-DD HH:MM:SS' rather than grouped as weekday or weekend. Once that is done though, the data shoud be ready for the statistical test.