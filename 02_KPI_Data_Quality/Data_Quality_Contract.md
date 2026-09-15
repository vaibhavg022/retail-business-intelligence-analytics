# Data Quality Contract — Retail Orders

**Version:** 1.0  
**Decision Owner:** Head of Commerce / Operations Manager  
**Expected Grain:** One row per unique `order_id`  
**Refresh Cadence:** Daily

## Trustworthy Data Definition

The dataset is considered trustworthy for KPI reporting when all critical quality rules pass and the freshness SLA is satisfied.

## Failure Thresholds

| ID | Dimension | Field | Threshold | Severity | Action |
|---|---|---|---:|---|---|
| DQ-01 | Completeness | order_id | 100% | Critical | Block KPI publication; quarantine affected rows |
| DQ-02 | Uniqueness | order_id | 100% | Critical | Block KPI publication; deduplicate |
| DQ-03 | Completeness | order_date | 100% | Critical | Block KPI publication |
| DQ-04 | Validity | order_date | 100% | Critical | Quarantine invalid dates |
| DQ-05 | Completeness | city | ≥98% | Warning/Fail | Warn below 99%; fail below 98% |
| DQ-06 | Validity | categorical fields | 100% | Critical | Resolve unmapped values |
| DQ-07 | Validity | quantity | 100% | Critical | Quarantine invalid rows |
| DQ-08 | Validity | unit_price | 100% | Critical | Quarantine invalid rows |
| DQ-09 | Validity | discount_pct | 100% | Critical | Quarantine invalid rows |
| DQ-10 | Consistency | payment_status | 100% | Critical | Resolve unresolved values |
| DQ-11 | Freshness | order_date | ≤1 day lag | Critical | Alert owner and block refresh |

## Escalation Workflow

1. Run automated data-quality checks after the daily load.
2. Alert the data/operations owner when a critical rule fails.
3. Quarantine failed records.
4. Correct the source data.
5. Rerun the profile.
6. Publish KPIs only after the contract passes.

## Audit Evidence

Retain the run timestamp, row count, check results, failed-row count/sample, latest valid date, and final PASS/FAIL decision.
