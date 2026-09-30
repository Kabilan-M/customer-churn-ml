# ML Problem-Framing Memo

## 1. Problem Statement

The goal is to build a customer churn prediction model that can help identify customers who may be at risk of leaving.

The model is intended to support a retention team by identifying potential churn risk before an appropriate retention action is considered.

The model should be used as decision support and not as an automatic decision-maker.

## 2. Decision to Support

The decision supported by the model is:

"Should this customer be reviewed by the retention team because they may be at risk of churn?"

The model should not automatically cancel services, deny services, penalize customers, or make other high-impact decisions.

A human reviewer should consider the prediction together with other relevant information before taking action.

## 3. Prediction Target

The prediction target is the `churned` column.

The target is binary:

- 1 = Customer churned
- 0 = Customer did not churn

The model will attempt to predict the likelihood of customer churn using the available customer attributes.

## 4. Unit of Observation

The unit of observation is one customer record.

Each row in the supplied dataset represents one customer.

The dataset contains 12 customer records.

## 5. Available Features

The supplied dataset contains the following fields:

- `customer_id`
- `tenure_months`
- `support_tickets`
- `monthly_spend_inr`
- `last_login_days`
- `plan_type`
- `churned`

The `customer_id` field is an identifier and should not normally be used as a predictive feature.

The remaining customer attributes may be considered as potential predictive features after checking their availability at prediction time and checking for leakage.

## 6. Action Window

The supplied dataset does not contain enough documented time information to establish an exact 30-day, 60-day, or 90-day prediction window.

Therefore, this baseline project treats the prediction as identifying churn risk before a retention decision is made.

For production use, the business should define a specific prediction horizon using timestamped historical data and the actual retention workflow.

## 7. Non-ML Baseline

Before evaluating a machine-learning model, a simple non-ML baseline will be used.

The baseline will predict the majority class for every customer.

In the supplied dataset:

- 5 customers have `churned = 1`
- 7 customers have `churned = 0`

Therefore, the majority-class baseline predicts `0` (no churn) for every customer.

The machine-learning model should be compared against this baseline rather than being evaluated in isolation.

## 8. Candidate ML Baseline

A Logistic Regression classifier will be used as the initial machine-learning baseline.

Logistic Regression is appropriate for this binary classification problem and provides a simple, interpretable starting point.

More complex models should only be considered after establishing a reliable baseline and sufficient evaluation data.

## 9. Data Splitting and Leakage Prevention

The dataset should be separated into training and test data before fitting preprocessing steps.

Preprocessing should be fitted using only the training data and then applied to the test data.

Features that contain information unavailable at the time of prediction must not be used.

The `customer_id` field should be excluded from model training because it is an identifier rather than a meaningful predictive attribute.

## 10. Business Error Costs

### False Positive

A false positive occurs when the model predicts that a customer will churn but the customer does not actually churn.

Potential costs include:

- Unnecessary retention effort
- Unnecessary discounts or incentives
- Additional staff time
- Possible customer annoyance

### False Negative

A false negative occurs when the model predicts that a customer will not churn but the customer actually churns.

Potential costs include:

- Missed retention opportunities
- Loss of a customer
- Potential loss of revenue

The exact monetary cost of false positives and false negatives should be estimated using real business data before production deployment.

## 11. Model Evaluation Metrics

The baseline model will be evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix
- ROC-AUC, where appropriate

Accuracy alone will not be used as the only measure because false positives and false negatives have different business consequences.

Recall is important for measuring how many actual churn cases are detected.

Precision is important for measuring how many customers identified as at risk actually churn.

## 12. Human Review

The model should not make final customer decisions automatically.

A proposed workflow is:

Customer data
→ Churn risk prediction
→ Risk assessment
→ Human review
→ Appropriate retention action

Human reviewers should have the ability to override the model when the prediction is incorrect or when additional context is available.

## 13. Abstention

The system should be able to abstain when the prediction is uncertain.

For example, if the model produces a probability close to the decision boundary, the case can be sent for human review instead of forcing an automatic churn-risk classification.

The abstention threshold should be determined using validation data and business costs rather than being assumed from the training dataset.

## 14. Monitoring

If the model is eventually deployed, the following should be monitored:

- Precision
- Recall
- F1-score
- False-positive rate
- False-negative rate
- Prediction distribution
- Input data quality
- Missing-value rates
- Changes in feature distributions
- Performance across relevant customer groups where sufficient data exists

Monitoring should continue after deployment because customer behavior and data patterns may change over time.

## 15. Rollback Conditions

Automated use of the model should be suspended if:

- Model performance decreases materially
- Data quality problems are detected
- Data leakage is discovered
- Important input distributions change unexpectedly
- Significant harmful differences in performance are identified
- The model produces unacceptable false-positive or false-negative rates

If a rollback condition occurs, the organization should return to a validated manual process or previously validated model while the issue is investigated.

## 16. Limitations

The supplied dataset contains only 12 customer records.

Therefore, the baseline results may have high uncertainty and may not generalize to a larger customer population.

The dataset also does not provide enough documented information about the original collection process, consent, licensing, or the exact prediction time window.

The model should therefore be treated as an internship baseline and not as a production-ready customer decision system.

## 17. Conclusion

The customer churn problem is a reasonable candidate for a supervised binary classification baseline because the supplied dataset contains a binary churn outcome.

However, the very small dataset and limited documentation mean that the resulting model should be treated as an experimental baseline.

Before production use, the organization should obtain a larger and representative dataset, establish the prediction horizon, verify data permissions, validate leakage controls, evaluate business costs, test model performance, and maintain human review and monitoring.