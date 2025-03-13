-- 1.1. The number of created leads per week grouped by course type
SELECT 
    c.type AS course_type,
    weekofyear(l.created_at) AS week_of_year,
    COUNT(l.id) AS leads_count
FROM 
    leads l
JOIN 
    courses c ON l.course_id = c.id
GROUP BY 
    course_type, week_of_year
ORDER BY 
    week_of_year, course_type;
    
    
-- 1.2. The number of WON flex leads per country created from 01.01.2024
SELECT
    d.country_name AS country,
    COUNT(l.id) AS number_of_WON_flex_leads
FROM
    leads l
JOIN
    courses c ON l.course_id = c.id
JOIN
    domains d ON l.user_id = d.id
WHERE
    l.status = "WON"
    AND c.type = "FLEX"
    AND l.created_at >= "2024-01-01"
GROUP BY
    d.country_name;
    
    
-- 1.3. User email, lead id and lost reason for users who have lost flex leads from 01.07.2024
SELECT
    u.email AS user_email,
    l.id AS lead_id,
    l.lost_reason
FROM
    leads l
JOIN
    courses c ON l.course_id = c.id
JOIN
    users u ON l.user_id = u.id
WHERE
    l.status = "LOST"
    AND c.type = "FLEX"
    AND l.created_at >= "2024-07-01";