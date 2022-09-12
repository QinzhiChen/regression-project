# Regression Project
<img width="710" alt="image" src="https://user-images.githubusercontent.com/107886541/188951062-689b1a15-12a3-4495-aaaf-a3fa614d7a57.png">

## Project Description
- The project's general idea is to find out what drives the house tax value, this project will contains several different files. 
    * The first will be the acquiring and cleaning file, which gives us a glance of the data we will going to explore next; 
    * The second will be our exploring file, which gives us the opportunity to discovering, assuming and reasoning; 
    * The third will be our modeling, which lets us to predict the house price with the best model.
    
## Project Goals
- The first goal for this project is to explore the database, and find out what drives the house tax market.
- The second goal for this project is to predict the future with our existing known information.
- The third goal is to provide recommendations to a improve our prediction.

## Project Dictionary
| Target      | Description  |
| ------------- |:-------------:|
| col 10 taxvalue      | The target variable |

----------------------------------------------------
| Features      | Description  |
| ------------- |:-------------:|
| col 1 yearbuilt      | At what year it was built |
| col 2 lots      | The size of the lot     |
| col 3 logerror | The log error     |
| col 4 longitude | The logitude in prepare for plotting      |
| col 5 latitude | The latitude in prepare for plotting      |
| col 6 bathroom | The bathroom count      |
| col 7 bedroom | The bedroom count       |
| col 8 fips | The county code      |
| col 9 zipcode | The zipcode for the area      |
| col 11 | The county name created from the fips  |
| col 12 month | The month the transaction taken place, this column is from the transaction date      |


## Project Planning
- Acquire
    * Acquired the data from SQL and saved it to the local drive
    * The acquicition also reviewed multiple tables to retrieve best possible columns without causing large size of file
    * putting the SQL code into python wrangle_zillow.py file with a function

- Prepare
    * In the wrangle_zillow.py file, the function created to examine the distribution
    * The function created to drop the null values
    * The function created to renames multiple columns name
    * The function created to remove the outliers
    * The month column created from the transaction date column and drop the transaction date column for tidiness
    * The county name created from the fips code
- Explore
    * Performed univariate analysis
    * performed exploration of the relationship between county and year built
    * examined the bathroom count
    * visualized features
- Model
    * Determine the baseline for the model
    * Create the function to determine the best model
    * Use the best model on the test to get the R square
    
## Initial Questions/Hypotheses
### Question 1
- Whether the counties have significant different on the bedroom count
- The bedroom has no significant different spread out each county. Which denied the initial assumption that the bedroom plays significant role with county taxvalue.
- However, we do find out that Los Angeles County is significant larger than the other two counties, which validated the reason why Los Angeles county has more transaction than other two counties.
### Question 2
- Whether the month is impacting the taxvalue?
- In Januaray, Los Angeles and orange county are the highest transaction volume, but the tax value was low
- The similar scenario happened in the September
- The highest tax value is in May as the graph depicted, and which the orange county was involved with the transaction
- The orange county has the highest tax value, which presumed to have the most impact on the tax value
### Question 3
- Hypothesis that if there are relationship between the month and orange county
#### Hypothesis
- HO=Mean of taxvalue of the orange county <= Mean of taxvalue of other counties
- H1=Mean of taxvalue of the orange county => Mean of taxvalue of other counties
- Alpha =0.05
- The orange county is significant higher tax value than other counties by $58958
- The people who have transaction in orange county might expected to pay higher tax rate than other counties
- Therefore we reject the hypothesis statement
- The next step should further examined whether the bedroom or other counts in orange county caused this situation. or is it because the tax rate in orange county
### Question 4
- Hypothesis that whether the bedroom count determine the tax value?
#### Hypothesis
- HO=Bedroom count is not determining the tax value
- H1=Bedroom count is determining the tax value
- Alpha =0.05
- The bedroom is determining the tax value
- It is not a strong correlation determined by the hypothesis test
- The next step for us should be examining other counts to determine whether their correlation is strong
## Findings, Recommendations, Takeaways
### Recommendation
- the Orange county has higher tax value than other counties, if the buyer wants to lower tax value, they should consider other counties
- The bedroom count is low correlation to the tax value, so the buyer should be able to buy house with more bedroom without reservation
- The data didn't have previous year information, which is recommended to help predict the trend
###  Takeaways, findings
- The polinominal is our best model, which has 180350 RMSE and 21.36% R square
- The orange county has significan high tax value
- The bedroom count has .094 correlation with the tax value
- The January and September are two high transaction months for the Los Angeles County and Ventura County

## Next Steps
- I believe the tax rate should be in play during the exploration process, which we should obtain them via past records
- I will further explore coastline area, I believe the coastline area should be higher cost on both maintain and taxvalue

## Steps to Reproduce
- Download all files on the github
- Have your own env password and username
- Read REAMME about the project planning
- Run the final report
