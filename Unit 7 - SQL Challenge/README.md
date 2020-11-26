# SQL Challenge - Employee Database: A Mystery in Two Parts

As a data engineer in Hewlett Packard, my manager made a request to research on employee data from the 1980s to 1990s. Six CSV databases were available to conduct the analysis. Since there are numerous rows of employee data and the information are scattered across the files, I must go through the below 3 steps to complete my task.


## **1.  Data Modeling**

To conduct any data analysis, any data engineer must know what information the databases contain and how the attributes are related to one another. The perfect way is to map it out in a Entity Relationship Diagram (ERD) in  [http://www.quickdatabasediagrams.com]( http://www.quickdatabasediagrams.com).

![Image](https://github.com/cecileung1208/Homework/blob/master/Unit%207%20-%20SQL%20Challenge/Output%20Files/ERD%20-%20Employee%20Database.png)

* Each box represents a table and its attributes (columns). 
* The key represents the primary keys uniquely identifies the records in each table.
* The line that connects to each table shows how the tables are related through common attirbutes.

![Image](https://github.com/cecileung1208/Homework/blob/master/Unit%207%20-%20SQL%20Challenge/Output%20Files/Relationship.png)

The [Data Model](https://github.com/cecileung1208/Homework/blob/master/Unit%207%20-%20SQL%20Challenge/Output%20Files/ERD%20-%20Employee%20Database.png) is saved in the output directory.

    
## **2.  Data Engineering**

Based on the above Entity Relationship Diagram (ERD), a [table schema](https://github.com/cecileung1208/Homework/blob/master/Unit%207%20-%20SQL%20Challenge/Employee_SQL/Table_Schema.sql) has been exported as an sql files to create the tables in Postregres.

The table schema information is based on the six CSV files where all data types, primary keys, foreign keys, and other constraints are specified .

After running the table_schema.sql and creating the headings for each table for Postregres, we must import ach CSV file into the corresponding SQL table. 
Note be sure to import the data in the same order that the tables were created and account for the headers when importing to avoid errors.

The below table shows which table corresponds to which CSV file.

| SQL Table Name    | Corresponding CSV Table |
| ------------- | ------------- |
| "Departments"  | [departments.csv](https://github.com/cecileung1208/Homework/blob/master/Unit%207%20-%20SQL%20Challenge/Resources/departments.csv)  |
| "Dept_Emp"  | [dept_emp.csv](https://github.com/cecileung1208/Homework/blob/master/Unit%207%20-%20SQL%20Challenge/Resources/dept_emp.csv)  |
| "Dept_Manager"  | [dept_manager.csv](https://github.com/cecileung1208/Homework/blob/master/Unit%207%20-%20SQL%20Challenge/Resources/dept_manager.csv)  |
| "Employees"  | [employees.csv](https://github.com/cecileung1208/Homework/blob/master/Unit%207%20-%20SQL%20Challenge/Resources/employees.csv)  |
| "Salaries"  | [salaries.csv](https://github.com/cecileung1208/Homework/blob/master/Unit%207%20-%20SQL%20Challenge/Resources/salaries.csv)  |
| "Titles"  | [titles.csv](https://github.com/cecileung1208/Homework/blob/master/Unit%207%20-%20SQL%20Challenge/Resources/titles.csv)  |

## **3.  Data Analysis**

After completing the Data Modeling and Data Engineering steps, we have enough understanding and infomrmation to extract specific employee information from the databases. 

To conduct our Employee Data Analysis, a [queries sql file](https://github.com/cecileung1208/Homework/blob/master/Unit%207%20-%20SQL%20Challenge/Employee_SQL/Queries.sql) has been created to retrieve the following employee information.

1.  List the following details of each employee: employee number, last name, first name, sex, and salary.

2.  List first name, last name, and hire date for employees who were hired in 1986.

3.  List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name.

4.  List the department of each employee with the following information: employee number, last name, first name, and department name.

5.  List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."

6.  List all employees in the Sales department, including their employee number, last name, first name, and department name.

7.  List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.

8.  In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
