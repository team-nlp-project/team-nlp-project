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
- Document each stage of the data science pipeline for this project
- Document code, hypothesises, statistical testing, exploration, modeling, key findings, and takeaways

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
| Word | Definition | 
| ----- | ----- | 
| Javascript| A programming language |
| Java | A programming language |
| Python | A programming language |
| C++ | A programming language |
| Other | Placeholder for all other programming languages not specifically named |
| Repo | A feature holding the repository url for the file on Github |
| language | A feature holding the programming language of the repo |
| readme_contents | A feature holding the text within the readme |
| clean | An engineered feature holding readme contents that were cleaned |
| stemmed | An engineered feature holding readme contents that were cleande and stemmed |
| lemmatized | An engineered feature holding readme contents that were cleaned lemmatized |
---

#### Initial Questions

[(Back to top)](#table-of-contents)

- Are there specific words or phrases that can be used as predictors for programming language?
- Are there words or phrases that have strong positive correlation with specific programming language(s)?
- Are there words or phrases that have strong negative correlation with specific programming language(s)?

#### Formal Hypotheses

[(Back to top)](#table-of-contents)

- H0 = The text of the readme can't be used to predict the programming language of the repo
- Ha = The text of the readme can be used to predict the programming language of the repo

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

- Acquired the raw data by web-scraping Github
- Used the Github proprietary API for web-scaping Github
- The raw data for each repo included the URL, the readme, and the programming language
- A local copy of the raw data was cached
___

##### Prepare

[(Back to top)](#table-of-contents)

- The raw data was cleaned (lowercased all characters, normalized unicode characters, removed non-ASCII characters)
- Stop words were removed
- New columns were created for cleaned, stemmed, and lemmatized readme text
- The four most common programming language categories were JavaScript, Java, Python, and C++: the remaining languages were placed into the 'other' category
- Data was split into train, validate, and test datasets

##### Explore

[(Back to top)](#table-of-contents)

- Answer key questions, observe trends, and identify possible predictors
- Create visualizations that show relationships between the variables
- Create stacked bar charts showing the most commonly used words in the readme's
- Create word clouds to visualize the most common words
- Use KBest and RFE to identify the most powerful predictors
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

[(Back to top)](#table-of-contents)
 
- [ ] Read this readme.md
- [ ] Clone the repo containing this readme file ( https://github.com/team-nlp-project/team-nlp-project )
- [ ] Create your own 'env.py' file which defines the credentials 'github_token' and 'github_username'
- [ ] Run the final_report.ipynb notebook

