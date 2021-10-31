# Using Natural Language Processing to Determine the Programming Languages of Github Projects

---

<img src="https://gowithcode.com/wp-content/uploads/2021/04/top-programming-languages.jpg" alt="Programming Languages" title="Programming Languages Image" width="600" height="300" />

---

# Table of Contents

---

- [Executive Summary](#executive-summary)
    - [Project Objectives](#project-objectives)
    - [Conclusions and Takeaways](#conclusions-and-takeaways)
    - [Next Steps and Recommendations](#next-steps-and-recommendations)    
- [Data Dictionary](#data-dictionary)
- [Initial Questions](#initial-questions)
- [Formal Hypotheses](#formal-hypotheses)
- [Pipeline Stages Breakdown](#pipeline-stages-breakdown)
    - [Plan](#plan)
    - [Acquire](#acquire)
    - [Prepare](#prepare)
    - [Explore](#explore)
    - [Model and Evaluate](#model-and-evaluate)
- [Conclusion and Next Steps](#conclusion-and-next-steps)
- [Reproduce My Project](#reproduce-my-project)

---

### Executive Summary

[(Back to top)](#table-of-contents)

---

#### Project Objectives

[(Back to top)](#table-of-contents)

- Create machine learning models that determine the programming language used within Github repos
- Analyze the repo's readme's with natural language processing (NLP) techniques
- Acquire the data from Github by web scraping
- Document each stage of the data science pipeline for this project
- Document code, hypothesises, statistical testing, exploration, modeling, key findings, and takeaways
- Improve reproducibility by storing complex functions in modules

#### Conclusions and Takeaways 

[(Back to top)](#table-of-contents)

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
- The best drivers identified were:
    - `back_legroom`
    - `city_fuel_economy`
    - `engine_displacement`
    - `fuel_tank_volume`
    - `height`
    - `highway_fuel_economy`
    - `horsepower`
    - `length`
    - `maximum_seating`
    - `mileage`
    - `wheelbase`
    - `width`
    - `year`

- Best-peforming model outperformed basline by:
    - Having an RMSE value that was 9,172 dollars less
    - R^2 improvement over baseline from 0 to 0.89

#### Next Steps and Recommendations

[(Back to top)](#table-of-contents)

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
- Try more combinations of categorical features to see if I can optimize performance
- Do more nuanced imputation using means/modes of subgroups instead of just means/modes of whole population
- Try less imputation and see how that affects model performance (drop more nulls)

#### Audience
- Members of the data science community who have at least basic knowledge of NLP.

#### Project Context
- The dataset was obtained by scraping Github for readme files
- The functions used to obtain the data are contained within the acquire.py

#### Data Dictionary

[(Back to top)](#table-of-contents)

---
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
| Feature                        | Description                                                                                                            | Data Type | Notes |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------- | --------- | ------------- |
| `back_legroom`                  |  Legroom in the rear seat (inches)                                                          |   float     |   Used in model    |
| `city_fuel_economy`                  |  Gas mileage in city (mpg)                                                        |   float     |   Used in model    |
| `engine_displacement`                  |  measure of the cylinder volume of engine (cubic centimeters)                                                       |   float     |   Used in model    |
| `fuel_tank_volume`                  |  Volume of fuel tank (gallons)                                                          |   float     |   Used in model    |
| `height`                  |  Height of vehicle (inches)                                                        |   float     |   Used in model    |
| `highway_fuel_economy`                  |  Gas mileage in highway (mpg)                                                       |   float     |   Used in model    |
| `horsepower`                  |  Measure of engine power                                                          |   float     |   Used in model    |
| `length`                  |  Length of vehicle (inches)                                                         |   float     |   Used in model    |
| `maximum_seating`                  |  Total number of seats                                                         |   float     |   Used in model    |
| `mileage`                  |  Mileage of vehicle (miles)                                                          |   float     |   Used in model    |
| `wheelbase`                  |  Distance between centers of front and rear wheels (inches)                                                         |   float     |   Used in model    |
| `width`                  |  Width of vehicle (inches)                                                        |   float     |   Used in model    |
| `year`                  |  Year car was released                                                         |   int     |   Used in model    |


---
| Target | Definition | Data Type | Notes |
| ----- | ----- | ----- | ----- |
| `price` | Sales price of used car | float | Value being predicted |

---

#### Initial Questions

[(Back to top)](#table-of-contents)

- Are there specific words or phrases that can be used as predictors for programming language?
- Are there words or phrases that have strong positive correlation with specific programming language(s)?
- Are there words or phrases that have strong negative correlation with specific programming language(s)?

#### Formal Hypotheses

[(Back to top)](#table-of-contents)

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
- See notebook for formal hypotheses and statistical testing

---

### Pipeline Stages Breakdown

---

##### Plan

[(Back to top)](#table-of-contents)

- [x] Create README.md with data dictionary, project goals
- [x] Create an initial hypotheses
- [x] Create a set of functions to automatically acquire data by web scraping from Github and then save a local copy
- [x] Create a set of functions to automatically clean and prepare the data.
- [x] Define and test statistical hypothesises, and document the takeaways
- [x] Create a baseline model to predict programming language.
- [x] Train several different models to predict programming language.
- [x] Evaluate the models on train and validate datasets.
- [x] Evaluate the single best performing model on the test dataset.
- [x] Document the code, process, takeaways, and conclusions in a jupyter notebook
- [x] Minimize clutter in the jupyter notebook by storing and using the complex functions in separate module files
- [x] Create a minimal viable product (MVP) first, and improve the model if time allows
___

##### Acquire

[(Back to top)](#table-of-contents)

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
- Store functions that are needed to acquire data from Kaggle; make sure the acquire.py module contains the necessary imports to run my code.
- The final function will return a pandas DataFrame.
- Import the acquire function from the acquire.py module and use it to acquire the data in the Final Report Notebook.
- Complete some initial data summarization (`.info()`, `.describe()`, `.shape()`, ...).
___

##### Prepare

[(Back to top)](#table-of-contents)

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
- Store functions needed to prepare the data; make sure the module contains the necessary imports to run the code. The final function should do the following:
    - Split the data into train/validate/test.
    - Handle any missing values.
    - Handle erroneous data and/or outliers that need addressing.
    - Encode variables as needed.
    - Identify unit measures and decide how to best scale any numeric data
    - Remove outliers
- Import the prepare function from the prepare.py module and use it to prepare the data in the Final Report Notebook.
- Plot distributions of individual variables.
___

##### Explore

[(Back to top)](#table-of-contents)

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
- Answer key questions, my hypotheses, and figure out the features that can be used in a regression model to best predict the target variable. 
- Run statistical tests in data exploration. Document my hypotheses, set an alpha before running the tests, and document the findings well.
- Create visualizations and run statistical tests that work toward discovering variable relationships (independent with independent and independent with dependent). 
- Summarize my conclusions, provide clear answers to my specific questions, and summarize any takeaways/action plan from the work above.
___

##### Model and Evaluate

[(Back to top)](#table-of-contents)

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
- Establish a baseline accuracy to determine if having a model is better than no model and train and compare at least 4 different models. Document these steps well.
- Train (fit, transform, evaluate) multiple models, varying the algorithm and/or hyperparameters you use.
- Compare evaluation metrics across all the models you train and select the ones you want to evaluate using your validate split.
- Feature Selection (after initial iteration through pipeline): Are there any variables that seem to provide limited to no additional information? If so, remove them.
- Based on the evaluation of the models using the train and validate datasets, choose the best model to try with the test data, once.
- Test the final model on the out-of-sample data (the testing dataset), summarize the performance, interpret and document the results.

---

### Conclusion and Next Steps

[(See Executive Summary)](#executive-summary)

---

### Reproduce My Project

---

[(Back to top)](#table-of-contents)
 
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
- [x] Read this README.md
- [ ] Download the modules (.py files), and final_report.ipynb files into your working directory
- [ ] Download complete dataset from Kaggle at this [link](https://www.kaggle.com/ananaymital/us-used-cars-dataset?select=used_cars_data.csv) and save in same repo as above files
- [ ] Run the final_report.ipynb notebook

