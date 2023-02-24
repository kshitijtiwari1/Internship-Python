USE sql_final_task;
SHOW TABLES;
CREATE TABLE kshitij_combined (
SELECT kshitij_sales.Customer_ID, kshitij_sales.Sales_ID, kshitij_sales.Item, kshitij_sales.Units, kshitij_sales.`Unit Cost`, kshitij_sales.Total, kshitij_customer.Customer, kshitij_customer.Region, kshitij_sales.OrderDate
  FROM kshitij_customer
  JOIN kshitij_sales
    ON kshitij_customer.Customer_ID = kshitij_sales.Customer_ID) ;
    
ALTER TABLE kshitij_combined
  ADD PRIMARY KEY (Sales_ID);
  
SELECT * FROM kshitij_combined;
LIMIT 10;
  
SELECT DISTINCT Item FROM kshitij_combined;

SELECT `Unit Cost` AS negative_cost FROM kshitij_combined
 WHERE `Unit Cost` < 0; 
 
SELECT MAX(`Unit Cost`), MIN(`Unit Cost`) , Item FROM kshitij_combined
 GROUP BY Item;
 
SELECT SUM(Total), OrderDate AS Total_Sales FROM kshitij_combined
 WHERE OrderDate BETWEEN "01-01-2021" AND "31-12-2021";
 
SELECT MAX(Item) FROM kshitij_combined 
  WHERE OrderDate BETWEEN "01-01-2021" AND "31-12-2021";
  
SELECT MAX(Region), MIN(Region) FROM kshitij_combined;

SELECT Customer, MAX(Total) FROM kshitij_combined
 WHERE OrderDate BETWEEN "01-01-2022" AND "31-12-2022"
 GROUP BY Customer;
 
SELECT MAX(`Unit Cost`), MIN(`Unit Cost`) FROM kshitij_combined;

SELECT DISTINCT Item FROM kshitij_combined
 WHERE Item LIKE 'P%';
 
SELECT * FROM kshitij_combined
 WHERE Item IN ('pen', 'pencil');
 
SELECT * FROM kshitij_combined
 WHERE `Unit Cost` BETWEEN 1 AND 100;
 
SELECT COUNT(Customer), Customer FROM kshitij_combined
 GROUP BY Customer;
 
SELECT MAX(Total), Item, Region FROM kshitij_combined
 GROUP BY Item;