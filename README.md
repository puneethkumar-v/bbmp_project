# BBMP Project Details:

## PROJECT TEAM SIZE: 5 members

## Contribution Details:

## Installing a virtual environment package to maintain dependencies for python projects:

```sh
sudo apt-get install virtualenv
```

## Creating a virtual environment for the project:

```sh
virtualenv example-environment
```

## Activating a virtual environment space:

```sh
cd example-environment
source bin/activate
```

## Cloning the Repo:

```sh
git clone https://github.com/puneethkumar-v/bbmp_project.git
```

## Installing the project dependencies:

```sh
cd bbmp-project
pip -r install requirements.txt
```

## Creating a seperate feature branch to work on:

```sh
git checkout -b newBranchName
```

## Command to run the project:

```sh
python3 manage.py runserver
```

## Adding and Commiting of the changes after completing the feature:

```sh
git add .
git commit -m "Enter brief description about the changes you've made"
```

## Push the code to the main branch

```sh
git push -u origin main
```

## After completing the above process now it's time to make a Pull Request

    * Go to the Repo link [bbmp_project: repo](https://github.com/puneethkumar-v/bbmp_project.git)
    * Make a pull request using all the avaialble option

## REQUIREMENTS:

- Web Technology to analyze and render the data from dataset
- Tools to construct tables using web tech
- Conversion of the data from pdf to csv file
- Tools to explore the visualization(graphs) for the dataset

## RESOURCE PROVIDED:

- 3 pdf's of the dataset including the objective of the dataset

## Services providing we will be providing:

- Building a web page to fetch the data from a csv file and render in the form of table
- Adding Functionalities such as Filtering, Sorting the table data on a particular column
- Searching on overall dataset for exact Roads
- Analyzing the dataset through Visualization library
- Complete ppt for the entire process of both phase 1 and 2
- Thorough training of the entire Project for the students

## FUNCTIONALITIES that will be added on the project:

- Phase 1: Deadline 16th January 2023

  - [ ] Filtering
  - [ ] Searching
  - [ ] Sorting

- Phase 2:
  - [ ] Visualization

## TODO:

- 09/01/2023:
  - [x] Creating a GitHub Repo
  - [x] Adding a README file
  - [x] Adding info regarding Contribution Guideline
  - [x] Starting a Django Project
  - [x] Creating a First Application inside a project called phase1

* 10/01/2023:
  - [x] Retrieving the data from excel sheet
  - [x] Experimenting with the libraries like pandas, openpyxl, to fetch the data
  - [x] Trying to analyze the data extracted from the excel sheet
  - [x] Rendering the data on the webpage

- 11/01/2023:

  - [ ] Inserting Data to DB from excel sheet
  - [x] Exploring jQuery for the Functionalities
  - [x] Going through the Objective Documentation to understand more about the Dataset
  - [x] ppt presentation preparation

- 12/01/2023:
  - [ ] Inserting Data to DB from excel
  - [ ] Verifying/Pre-processing the excel sheet
  - [ ] Discussed regarding DataBase Schema design
  - [x] PPt presentation
