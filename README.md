# Databricks ETL pipeline
[![CI](https://github.com/farazjawedd/python-template-ids706/actions/workflows/cicd.yml/badge.svg)](https://github.com/farazjawedd/python-template-ids706/actions/workflows/cicd.yml)

Demo video: https://youtu.be/sZw3zFSSMnw

This project demonstrates a Databricks-based ETL pipeline that extracts data, performs transformations using Spark SQL, loads the transformed data into Delta Lake, and visualizes the results. It includes features such as automated triggers and data validation.

## ETL Pipeline

#### Extract: 
We fetch the data from a github repository where it is hosted. The dataset is basically on world happiness index in 2020 for each country. Here is the screenshot for the notebook which loads the data in a pandas dataframe, converts it into a pyspark dataframe and loads it into a delta lake.

<img width="925" alt="Screenshot 2023-11-26 at 7 29 45 PM" src="https://github.com/farazjawedd/Individual3_databricks/assets/101464414/7f5b3648-aff1-43bf-8bf1-1a0a0e727429">

#### Transform and Load:
Then we transform the dataset to only get what is useful to us. In this case, I used `spark.sql` to query the columns I wanted and grouped the data by the continent, to evaluate the avg freedom and avg corruption in each continent, here is the notebook screenshot for it:

<img width="757" alt="Screenshot 2023-11-26 at 7 31 46 PM" src="https://github.com/farazjawedd/Individual3_databricks/assets/101464414/24c330d5-8c1b-4f2b-849f-227de7397d16">

#### Visualize:
In order to visualize, I plotted it into a simple line plot to see how each continent compares with each. The visualize notebook:

<img width="851" alt="Screenshot 2023-11-26 at 7 33 08 PM" src="https://github.com/farazjawedd/Individual3_databricks/assets/101464414/fd513f24-5227-46bf-afc4-f5c50e4a452b">

Here is the final plot:

<img width="660" alt="Screenshot 2023-11-26 at 7 33 26 PM" src="https://github.com/farazjawedd/Individual3_databricks/assets/101464414/b3c6df86-6230-423f-9cd1-11c94c23d2a6">

### WorkFlow:
In order to have an automated pipeline, we can set up a workflow on databricks, which has each of the notebooks as jobs and set up an automated trigger so that it runs automatically and updates everything. Here is the screenshot of the workflow:

<img width="876" alt="Screenshot 2023-11-26 at 7 34 56 PM" src="https://github.com/farazjawedd/Individual3_databricks/assets/101464414/7e3823ea-a426-482e-8f47-3e433f8ea11d">

I manually triggered it a few times to see if it's working:

<img width="943" alt="Screenshot 2023-11-26 at 7 35 27 PM" src="https://github.com/farazjawedd/Individual3_databricks/assets/101464414/4598acec-2c7b-4c1d-861a-081f8566aeb9">

The associated `py` files for my notebooks on databricks are in the `Databricks Notebooks` folder in the repository.

#### Benefits of delta lake:
Some of the benefits I learned about Delta lake:

- Schema Evolution:
Supports easy evolution of data schema without complex migration.

- Time Travel:
Enables querying historical data snapshots for auditing and debugging.

- Optimized Data Compaction:
Automatically handles data compaction, reducing storage footprint.

- Concurrency Control:
Manages multiple read and write operations for data consistency.


-------------


The Github Action workflow and pipeline has the following:

- Dockerfile for containerization
- .devcontainer.json for Visual Studio Code development containers
- Makefile for common project tasks
- requirements.txt for managing dependencies
- main.py for your project code
- test_main.py for testing your code

## Getting Started

1. Clone this repository to your local machine.
2. Install Python 3.x on your system.
3. (Optional) Install Docker for containerization.
4. (Optional) Install Visual Studio Code with the "Remote - Containers" extension.

## Usage

- Run your project's `main.py` script using Python.
- Test your code with the provided `test_main.py` script.
- Use the Makefile commands for common tasks, e.g., `make install-dependencies`, `make run`, `make test`.

- This also includes a docker container for running your scripts on a virtual envt. 
