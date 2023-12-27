# CSV DATA ANALYZER: NIKE SHOE SALES

# Description:
Project Overview:

The objective of this project is to provide a user-friendly interface for analyzing and exploring sales data for a range of Nike products. The primary script, main_script.py, acts as the entry point for users, allowing them to filter and sort the sales dataset based on product category, gender, and sorting criteria. Leveraging the pandas library, the script reads the data from a CSV file, interacts with the user through input prompts, and then displays the filtered and sorted results. This project aims to empower users to dynamically interact with sales data, gaining insights tailored to their specific preferences.

File Descriptions:
 
The main functionality is encapsulated in main_script.py, where users can input their criteria and view the corresponding results. It imports three crucial functions from the "project" module: get_category(), get_gender(), and assert_quantity_sold(). The "project" module, contained in project.py, houses these functions, ensuring modularity and ease of testing. Additionally, the testing script, testing_script.py, plays a vital role in verifying the correctness of individual functions within the "project" module, guaranteeing the reliability of the codebase.

Design Choices:

In the design of this project, careful considerations were made to enhance modularity and user-friendliness. The decision to separate user input functions from data manipulation functions in the "project" module allows for easier testing and maintenance. Constants were introduced to centralize options for category, gender, and sorting, promoting consistency and manageability. The project also incorporates case-insensitive comparisons for category and gender inputs, ensuring a more user-friendly experience. The inclusion of a testing script underscores the commitment to code reliability, allowing for confident modifications and additions to the project in the future.

User Interaction and Flexibility:

The project prioritizes a positive user experience by providing a clear and interactive interface. Users are prompted to input their preferences for category, gender, and sorting options, making the exploration of sales data intuitive. The project encourages a dynamic and flexible analysis, allowing users to tailor the results to their specific needs. By implementing these design choices, the project aims to strike a balance between simplicity and functionality, making it accessible for users with varying levels of data analysis expertise.

TODO
1. download pandas (import pandas as pd)
