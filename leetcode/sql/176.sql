-- 编写一个 SQL 查询，获取 Employee 表中第二高的薪水（Salary） 。
-- +----+--------+
-- | Id | Salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+
-- 例如上述 Employee 表，SQL查询应该返回 200 作为第二高的薪水。如果不存在第二高的薪水，那么查询应返回 null。
-- +---------------------+
-- | SecondHighestSalary |
-- +---------------------+
-- | 200                 |
-- +---------------------+

-- 使用嵌套的查询，将结果作为临时表再选择
SELECT (
    SELECT DISTINCT Salary
    FROM  Employee
    ORDER BY Salary DESC
    LIMIT 1, 1
) AS SecondHighestSalary