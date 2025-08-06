# Write your MySQL query statement below
select Sales.year,Product.Product_name,Sales.price from Sales join Product on Sales.product_id=Product.product_id
