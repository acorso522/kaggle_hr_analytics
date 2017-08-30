# HR Analytics
https://www.kaggle.com/ludobenistant/hr-analytics

Why are our best and most experienced employees leaving prematurely? Have fun with this database and try to predict which valuable employees will leave next. Fields in the dataset include:

    Satisfaction Level
    Last evaluation
    Number of projects
    Average monthly hours
    Time spent at the company
    Whether they have had a work accident
    Whether they have had a promotion in the last 5 years
    Departments (column sales)
    Salary
    Whether the employee has left

## Required Files
- HR_comma_sep.csv in your working directory

## Package Requirements
### Python
- rpy2
- numpy
- pandas
- os
- sys
- warnings
- math
- sklearn
- xgboost
- flask
### R
- dplyr
- ggplot2

## Running flask application
Run flask app by executing the following command in your shell of choice

```python
python Documents/github/kaggle_hr_analytics/flask_app.py
```
We can then retrieve results by POSTing to http://127.0.0.1:8080/predict (local) with a JSON request as follows: 

```json
{
	"satisfaction_level":[0.01], 
	"time_spend_company":[3]
}
```