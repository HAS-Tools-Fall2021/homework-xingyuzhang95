<center>

### Xingyu Zhang
### 10/10/2021
### Assignment 7

</center>


## Grade:
### 1. Forecast Submision:
**1/3:** I don't see anything in your markdown here answering the questions of the assignment. This appears to be your submisison from Assignment 7. 

### 2. Graded Script
Refer to [the rubric](https://github.com/HAS-Tools-Fall2021/Course-Materials21/blob/main/Content/Starter_Codes/week7_code_review_rubric.md) for details on scoring:
- **Readability:2/3** You had some comments however some of the comments appeared to be copied straight from the starter code and were not descriptive (e.g. the comment on the top line). Also you are misisng doc strings in your function. 
- **Style:3/3** Good work no pep-8 errors
- **Code:2/3** I don't see where in your code you are generating the forecast values or the print statments that were required. Also I had to adjust the path for the input data to get the code to run. Overall you code is nicely done although I would like to see a bit more analysis per my previous comment. 
____________
</br>

### Code instruction
- please download this whole folder; this folder include 3 plots, 1 code and 1 data. Some code may be not as efficient and effective as we expected. Therefore, please leave your revision or suggestions at the end of this file.
- You will see three plots generated after the run, which will be used in this markdown file.
- Go through the generated plots and have a sense of what the flow will be for next week (hint: we know the October mean and the evolution trend of October flow this year; then guess a value).
- Fill all blanks.
</br>

### Forecast
We generated three plots as follows:
1. Time series plot of observed daily flow during 1989-2021. The time series is stationary.
![](assets/ReadMe-5dc6fda0.png)

2. Boxplot of daily observed flow before and after 2014: we see the distribution of October flow changes during these two periods. The time series is stationary with 12 month peried change
![](assets/ReadMe-cd815ef6.png)

3. boxplot the flow difference between each month.Jun has the lowest flow and Mar has the largest.
![](assets/ReadMe-b73fd6c2.png)

- Therefore, we forecasted weekly mean for next week and two weeks laters should be **170** and **180** cfs, respectively.
</br>

### Code revision or suggestion from Steph Serrano

- First:
  - The script is easy to read and understand. The variables were clear and the comments before each plot were helpful in preparing the user for whatever was going to be produced in the interactive window!
  - The third boxplot did not have docstrings attached properly! Although there were comments in the middle of the function explaining why the x- and y- label were separated even though they could have been included, That could have been done with docstrings to follow PEP8 Style. It should be added after the "def" statement on line 65, then the rest of the function can continue. Docstrings can be added by beginning a sentence within a function with three apostrophes (') and ending said sentence with the same three apostrophes!
    - **Example:** ''' Insert statements/docstrings here. '''

- Second:
  - PEP8 style is consistently followed throughout! Line 70 is 5 characters too long (each line should be 79 characters). The line could either be shortened to be more succinct or a slash (/) could be used to denote a break in the sentence that is being continued in the next line of code.

- Third:
  - The code is written succinctly and efficiently. The function was done well to show the boxplot of flows by month although I wonder if the function can be messed with to return only specific months rather than all 12! Just a suggestion to maybe mess around with sometime!
  - I talked to Dr. Condon and she said to make an educated guess for your forecast submission for this week. However, for the next script, the flow values that you would like to have added to the Excel.CSV file have to come directly from the script you create! The reviewers should not be making educated guesses based on your plots/instructions! Other than that, nice script! Thank you (:
