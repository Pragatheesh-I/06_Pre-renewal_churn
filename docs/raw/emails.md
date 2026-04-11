## Emails dataset info

- Total rows: 123,389.
- Total columns: 27.
- `Time_to_Renewal` distribution:
  - `prior_year`: 40,022
  - `14_out`: 32,493
  - `45_out`: 28,008
  - `pre_renewal`: 22,866
- `Year` distribution:
  - `2025`: 81,625
  - `2026`: 41,762
  - `2024`: 2
- The pre-renewal subset contains 22,866 rows and is the primary focus for pre-renewal churn analysis.

### Dataset overview

1. Metadata

- `Co_Ref`: Customer reference code. Customers can appear multiple times (most frequent ids appear 8 times), so treat `Co_Ref` as an identifier for grouping or joining, not as a unique feature.
- `Time_to_Renewal`: Renewal timing label.
- `Year`: Year of the email.

2. CRM status and accreditation
- `crm_accreditation_completed`: `No` 46,193; `Not Discussed` 34,870; `Yes` 21,291; missing 21,035.
- `crm_timely_completion`: `Not Discussed` 62,517; `No` 36,986; missing 21,035; `Yes` 2,851.
- `crm_progress_towards_accreditation`: `Yes` 53,395; `Not Discussed` 45,953; missing 21,035; `No` 3,006.
- `crm_delays_in_accreditation`: `No` 60,816; `Yes` 40,318; missing 21,035; `Not Discussed` 1,203.

3. Contractor sentiment and engagement
- `crm_contractor_suggested_leave`: `No` 79,371; missing 21,035; `Not Discussed` 14,289; `Yes` 8,694.
- `crm_contractor_engagement`: `Yes` 71,129; `No` 31,188; missing 21,035.
- `crm_contractor_sentiment`: `Neutral` 53,576; `Not Discussed` 31,167; missing 21,035; `Satisfied` 11,405; `Dissatisfied` 6,177.
- `crm_contractor_sentiment_score`: `50` 53,554; `Not Discussed` 31,171; missing 21,035; `80` 7,055; `20` 3,006.

4. Competitors, payment, and issues
- `crm_dts_or_ssip_mentioned`: `No` 63,631; `Yes` 38,697; missing 21,035.
- `crm_customer_payment_intention`: `Not Discussed` 69,476; `Yes` 28,236; missing 21,035; `No` 4,638.
- `crm_competitors_mentioned`: `No` 79,549; `Not Discussed` 26,957; missing 11,155; `Yes` 5,724.

5. Membership, renewal, and agent activity
- `crm_membership_level`: `In progress` 45,219; `Accredited` 35,847; `Not Discussed` 29,891; missing 11,155.
- `crm_platform_issues_raised`: `No` 84,965; `Not Discussed` 19,946; missing 11,155; `Yes` 7,323.
- `crm_agent_chased_contractor`: `Yes` 75,030; `No` 36,710; missing 11,155.
- `crm_agent_chase_count`: `0` 37,199; `1` 31,223; `2` 23,726; missing 11,155; `3` 10,397.
- `crm_accreditation_issues`: `Not Discussed` 54,235; `Yes` 44,787; `No` 13,212; missing 11,155.
- `crm_membership_overdue`: `Not Discussed` 54,110; `Yes` 30,137; `No` 27,937; missing 11,155.
- `crm_auto_renewal_status`: `0` 105,135; missing 11,155; `2` 4,702; `1` 2,348.

6. Customer feedback and risk signals
- `crm_dissatisified_with_renewal_price`: `Not Discussed` 70,611; `No` 33,063; missing 11,155; `Yes` 8,519.
- `crm_customer_complained`: `No` 104,315; missing 11,475; `Yes` 7,568.
- `crm_refund_mentioned`: `No` 110,163; missing 11,475; `Yes` 1,700; `Not Discussed` 27.
- `crm_negative_customer_experience`: `No` 66,587; `Not Discussed` 26,962; `Yes` 18,360; missing 11,475.
- `crm_dissatisfaction_with_support`: `No` 66,336; `Not Discussed` 34,818; `Yes` 10,698; missing 11,475.
- `crm_financial_hardship_mentioned`: `Not Discussed` 72,242; `No` 33,120; missing 11,475; `Yes` 6,516.

### Data preprocessing plan

- Filter to `Time_to_Renewal == "pre_renewal"` for the pre-renewal analysis set (22,866 rows).
- Convert `Year` to integer type.
- Normalize missing/unknown values across fields:
  - treat `NaN`, empty strings, and `Not Discussed` as a single missing/unknown category.
- Standardize binary-like columns:
  - map `Yes`/`No` values consistently.
  - map stray text and invalid labels in `crm_dts_or_ssip_mentioned`, `crm_customer_payment_intention`, `crm_competitors_mentioned`, `crm_customer_complained`, `crm_refund_mentioned`, `crm_negative_customer_experience`, `crm_dissatisfaction_with_support`, and `crm_financial_hardship_mentioned` into clean categories.
- Clean `crm_agent_chase_count`:
  - parse numeric values (`0`, `1`, `2`, ...) into integer counts.
  - treat non-numeric values such as `Multiple`, `Not specified`, and verbose text as missing, then impute.
- Clean `crm_membership_level`:
  - consolidate variants like `In progress`/`In Progress`, `Accredited`, `Not Accredited`, `Members only`, and `Standard`.
  - set rare or inconsistent values to `Other` or `Unknown`.
- Clean `crm_auto_renewal_status`:
  - keep numeric states `0`, `1`, `2` and map text/noise to missing.
- Clean `crm_contractor_sentiment_score`:
  - parse numeric scores and treat invalid text entries as missing.
- Impute missing values for cleaned data:
  - use mode imputation for categorical cleaned fields.
  - use median imputation for numeric cleaned fields (`crm_agent_chase_count_clean`, `crm_contractor_sentiment_score_clean`).
- Treat `Co_Ref` as an identifier only:
  - use it for deduplication, grouping, or joins, but not as a raw predictive feature unless encoded intentionally.
- Save cleaned output separately for modeling, e.g. `dataset/processed/emails_preprocessed.csv`.

### Notes on data quality

- Many CRM fields are dominated by `Not Discussed` or missing values.
- Several fields contain inconsistent text labels or non-standard values that should be normalized before modeling.
- `crm_agent_chase_count`, `crm_membership_level`, `crm_auto_renewal_status`, `crm_dts_or_ssip_mentioned`, and `crm_competitors_mentioned` are especially noisy and should be cleaned carefully.

