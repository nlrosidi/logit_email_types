# logit_email_types
Logistic regression on email to measure the effectiveness of email type to user logins.

## What is logistic regression?
Logistic regression is a statistical model that measures the relationship between the categorical dependent variable and independent variable(s), meaning we can measure the impact the independent variables have on the dependent variables. 

In this exercise, we want to measure the effectiveness on different types of emails as it relates to a user login. 

## Why use logistic regression over linear regression?
Consider the linear probability model

    Y = a + BX + e

where
* Y is the dependent variable (1 if the event happens, 0 if the event doesn't happen)
* ***a*** is the coefficient of the constant term
* ***B*** is the coefficient(s) of the independent variable(s)
* X is the coefficient of the independent variables(s)
* e is the error term

Using a linear probability model will probability give you the correct answer in terms of sign and significant levels of your independent variables, but won't have any predictive powers. The problems for using a linear probaility model are: