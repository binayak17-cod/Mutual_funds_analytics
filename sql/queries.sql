-- Common analytical queries for mutual fund data

-- 1. Fetch latest NAV for all schemes
SELECT 
    s.scheme_code,
    s.scheme_name,
    s.scheme_type,
    h.nav_date AS latest_date,
    h.nav AS latest_nav
FROM mutual_fund_schemes s
JOIN daily_nav_history h ON s.scheme_code = h.scheme_code
WHERE h.nav_date = (
    SELECT MAX(nav_date) 
    FROM daily_nav_history 
    WHERE scheme_code = s.scheme_code
);

-- 2. Calculate average annual returns (CAGR equivalent)
-- Note: Simplified return based on first and last NAVs in the database
WITH scheme_endpoints AS (
    SELECT 
        scheme_code,
        MIN(nav_date) as start_date,
        MAX(nav_date) as end_date
    FROM daily_nav_history
    GROUP BY scheme_code
),
start_navs AS (
    SELECT h.scheme_code, h.nav as start_nav, h.nav_date
    FROM daily_nav_history h
    JOIN scheme_endpoints e ON h.scheme_code = e.scheme_code AND h.nav_date = e.start_date
),
end_navs AS (
    SELECT h.scheme_code, h.nav as end_nav, h.nav_date
    FROM daily_nav_history h
    JOIN scheme_endpoints e ON h.scheme_code = e.scheme_code AND h.nav_date = e.end_date
)
SELECT 
    s.scheme_code,
    s.scheme_name,
    sn.nav_date as start_date,
    sn.start_nav,
    en.nav_date as end_date,
    en.end_nav,
    (en.end_nav - sn.start_nav) / sn.start_nav * 100 AS absolute_return_pct,
    -- Annualized Return: (End / Start) ^ (365 / days) - 1
    (POWER(en.end_nav / sn.start_nav, 365.0 / JULIANDAY(en.nav_date) - JULIANDAY(sn.nav_date)) - 1) * 100 AS cagr_pct
FROM mutual_fund_schemes s
JOIN start_navs sn ON s.scheme_code = sn.scheme_code
JOIN end_navs en ON s.scheme_code = en.scheme_code;

-- 3. Find historical drawdowns (peak-to-trough drop)
WITH running_peaks AS (
    SELECT 
        scheme_code,
        nav_date,
        nav,
        MAX(nav) OVER (PARTITION BY scheme_code ORDER BY nav_date) as peak_nav
    FROM daily_nav_history
),
drawdowns AS (
    SELECT 
        scheme_code,
        nav_date,
        nav,
        peak_nav,
        (nav - peak_nav) / peak_nav * 100 AS drawdown_pct
    FROM running_peaks
)
SELECT 
    scheme_code,
    MIN(drawdown_pct) AS max_drawdown_pct
FROM drawdowns
GROUP BY scheme_code;
