# Logit on Email Types
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
* The error terms are heteroskedastic. Heteroscedasticity is when the variability (or variance) of a variable is unequal across the range of values of a variable that predicts it. For example, annual income might be heteroscedastic when age is a predictor. If we assume teenage workers earn close to minimum wage, there isn't a lot of variability during their teen years. However, as teens turn into 20-somethings, and 20-somethings turn into 30-somethings, the variance will increase as some people jump up in their tax bracket while others increase gradually. The variance between the "haves" and "have-nots" widen with age. In linear regression, it is assumed that the error of a regression model is homoscedastic across all values, which isn't the case in this example. The result of heteroscedasticity in this example is that annual income is accurately predicted by age but only in the early years.
* The error term is not normally distributed since the dependent variable only takes on two values, 0 or 1.
* The predicted probabilities can be greater than 1 or less than 0, which can lead to problems if the predicted values are used in subsequent analysis. 

### Logistic Regression

The logistic regression model will solve these problems.

    ln[p/(1-p)] = a + BX + e 
or
    
    [p/(1-p)] = exp(a + BX + e)

where

* p is the probability that the event Y (dependent variable) occurs, p(Y=1)
* p/(1-p) is the "odds ratio"
* ln[p/(1-p)] is the log odds ratio, or "logit"
* all the other variables of the model are the same

A logistic regression is simply a non-linear transformation of a linear regression, which can help you more accurately predict the behavior and contributions of your variables.

## What's included

This repo includes a python script, data in csv format, and a step-by-step guide with explanations about the impelmentation and underlying math. The guide is offered as an HTML or iPython notebook. 




