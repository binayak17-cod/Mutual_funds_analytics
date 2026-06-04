-- Database schema for Mutual Funds Analytics

-- Table to store mutual fund schemes metadata
CREATE TABLE IF NOT EXISTS mutual_fund_schemes (
    scheme_code INTEGER PRIMARY KEY,
    scheme_name TEXT NOT NULL,
    fund_house TEXT,
    scheme_type TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store NAV time-series details
CREATE TABLE IF NOT EXISTS daily_nav_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scheme_code INTEGER NOT NULL,
    nav_date DATE NOT NULL,
    nav DECIMAL(10, 4) NOT NULL,
    daily_return DECIMAL(10, 6),
    rolling_30_nav DECIMAL(10, 4),
    rolling_90_nav DECIMAL(10, 4),
    rolling_volatility_30d DECIMAL(10, 6),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(scheme_code) REFERENCES mutual_fund_schemes(scheme_code),
    UNIQUE(scheme_code, nav_date)
);

-- Index for faster chronological lookups by scheme
CREATE INDEX IF NOT EXISTS idx_nav_history_scheme_date 
ON daily_nav_history (scheme_code, nav_date ASC);
