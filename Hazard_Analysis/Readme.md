# Hazardous Materials Incident Analysis

## Project Motivation & Background

As a National Guard Hazardous Materials Specialist with four years of experience in an aviation unit, I've led spill cleanup operations, conducted safety checks, and trained new soldiers on hazmat protocols. Hazardous materials spills can cause serious harm to people and the environment, so I'm passionate about spotting trends, predicting future incidents, and helping teams build better safety plans.

## What the Function Does

The main function, `analyze_hazmat_incidents()`, runs the full analysis pipeline:

1. **Load & clean data**: Read the raw incident data and remove errors.  
2. **Create features**: Compute metrics like spill volume, injury counts, and chemical types.  
3. **Train models**: Build Random Forest and linear regression models to predict incident risk and cost.  
4. **Generate visuals**: Make charts and a live Dash dashboard to explore trends and outputs.  

This single function ties together data prep, modeling, and reporting so anyone can reproduce the results.

## Dataset

We use the U.S. Hazardous Materials Incident Data from Kaggle:

- **Link:** https://www.kaggle.com/datasets/phmsa/us-hazardous-materials-incident-data

## References

1. [U.S. DOT PHMSA Annual Hazardous Materials Incident Report (2021)](https://www.phmsa.dot.gov/sites/phmsa.dot.gov/files/docs/annual-hazardous-materials-incident-report-2021.pdf)  
2. [UNEP Global Overview of Hazardous Materials Incidents (2020)](https://www.unep.org/resources/report/global-overview-hazardous-materials-incidents-2020)  
