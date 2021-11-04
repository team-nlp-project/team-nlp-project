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
- Examine the 500 most forked repos on Github
- Document each stage of the data science pipeline for this project
- Document code, hypothesises, statistical testing, exploration, modeling, key findings, and takeaways
___

#### Conclusions and Takeaways 

[(Back to top)](#table-of-contents)

- Models were developed that can predict the programming language by using NLP techniques to analyse the readme
- The most accurate model was logistic regression
- The top four most common programming languages tend to use different words in their readme's, the most commonly used words tend to be related to projects that frequently use that programming language
- Our analysis of the readme's implies that certain themes may be more popular with different programming languages
___

#### Next Steps and Recommendations

[(Back to top)](#table-of-contents)

- Future work would include increasing the number of predicted programming languages beyond just the top four most commonly used programming languages
___

#### Audience

[(Back to top)](#table-of-contents)

- Members of the data science community who have at least basic knowledge of NLP.
___

#### Project Context
- The dataset was obtained by scraping Github for readme files
- The 500 most forked repo's on Github were examined
- The functions used to obtain the data are contained within the accessory .py files
- The readme's were examined using NLP techniques
___

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
___

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
- The 500 most forked repo's on Github were used as data sources
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
___

##### Explore

[(Back to top)](#table-of-contents)

- Created bar charts, word clouds, and word counts to explore the train data
- The four most common programming languages were JavaScript, Java, Python, and C++
- One of the most common words in the readme's was the programming language used
- Some of the most common words for JavaScript were function, good, and bad
- Some of the most common words for Java were terms related to the cloud and android
- Some of the most common words for Python were terms related to video analysis and data science
- Python readme's had higher word counts, on average
- The exploration of the readme's showed that these programming languages tend to be used for different purposes
___

##### Model and Evaluate

[(Back to top)](#table-of-contents)

- Models were developed on train dataset, tuned in validate dataset, and the best performing model was used on the test dataset
- Random states were set to ensure reproducibility
- The models used were decision tree, random forest, logistic regression, and K nearest neighbors
- The models were run on cleaned, cleaned + stemmed, and cleaned + lemmatized readme text
- The best performing model was logistic regression, which beat the baseline by 31%

---

### Conclusion and Next Steps

[(See Executive Summary)](#executive-summary)

- Models were developed that can predict the programming language by using NLP techniques to analyse the readme
- The most accurate model was logistic regression
- The top four most common programming languages tend to use different words in their readme's, the most commonly used words tend to be related to projects that frequently use that programming language
- Our analysis of the readme's implies that certain themes may be more popular with different programming languages
- Future work would include increasing the number of predicted programming languages beyond just the top four most commonly used programming languages

---

### Reproduce My Project

[(Back to top)](#table-of-contents)
 
- [ ] Read this readme.md
- [ ] Clone the repo containing this readme file ( https://github.com/team-nlp-project/team-nlp-project )
- [ ] Create your own 'env.py' file which defines the credentials 'github_token' and 'github_username'
- [ ] Run the final_report.ipynb notebook

