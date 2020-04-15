# Research and Development into Advanced Manufacturing Revision Tool - SFIA-1

V1.0

## Overview

The R and D into AM Revision tool was created for the practical purpose of exam preparation (MSc in Advanced Mechanical Engineering). The user is a provided with an inbuilt randomised set of questions which are 'fed' to the user until the question given is answered correctly. Only when all questions are answered correctly will the quiz end. An analysis page is then generated, illustrating the number of times each question was answered incorrectly. This provides the user knowledge of which areas of the course material require further revision.

## The Brief

In order to meet the requirements of SFIA-1 it was necessary to fulfil the CRUD criteria. In addition, it was necessary to utilise methodologies and applications in support of the application as well as creating complementary documentation.

## Requirements
  - The creation of a Trello Board (See Japanese concept of Kanban) to illustrate user requirements, degrees of difficulty for each facet of the overall design, user stories and timeframes in which you expect to complete phases of work. 
  - Utilisation of a relational database using SQL. To demonstrate a comprehensive understanding of the proposeed architecture, create a complementary entity relationship diagram.
  - Supporting documentation created during the planning phase including a risk assessment.
  - The implementation of CRUD using the python programming language and Flask website framework.
  - Validation of the functionality of the website using automated testing in keeping with the test driven development methodology. 
  - Automated deployment using Jenkins. 
  
 ## Risk Assessment
 
 Illustrated below is a rudimentary risk assessment, where potential problems that could be encountered over the duration of the project have been identified.
 
 ![Riskassessment](https://user-images.githubusercontent.com/60216123/79338566-6eed9880-7f1f-11ea-8a2f-6a546f97caf4.png)

 ## Trello

The Trello board created for this project is depicted below. Further information can be found by expanding each container providing further insight into the thinking process in the design process.

![Screenshot 2020-04-15 at 13 56 34](https://user-images.githubusercontent.com/60216123/79339622-0ef7f180-7f21-11ea-8d53-4fdea585320c.png)

 ##  ERD
 
Two entity relationship diagrams (ERD) were created. The first of which displays the proposed relationships between the tables, underpinning the architecture of website.

![ERDfirst](https://user-images.githubusercontent.com/60216123/79341762-300e1180-7f24-11ea-9200-35d80f44a2a4.png)

The second ERD was constructed retrospectively, after the architecture was finalised. Although more tables are present it is less inter-connected for simplicity. Rather than connecting the tables in the models file, it was decided (based on advice from my project supervisor) to exchange information in certain circumstances in the routes file.  

![ERDfinal](https://user-images.githubusercontent.com/60216123/79341764-313f3e80-7f24-11ea-8113-ad79ff890d83.png)

 ## Future Improvements

- As described in the Trello board, it would be beneficial for the user to be able to manually add questions and answers as opposed to uploading a csv file of questions in the backend of the website.
- Beautification of the website using HTML bootstrap or a similar library.
- Add a match question and answer to the website, where the user views seperately randomised questions and answers and has to correctly match them up.
