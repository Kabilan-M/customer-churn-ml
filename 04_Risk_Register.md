# Customer Churn ML - Risk Register

## Purpose

This risk register documents the main risks associated with the customer churn prediction baseline and the safeguards that should be applied before any real-world deployment.

| Risk | Likelihood | Impact | Mitigation / Safeguard |
|---|---|---|---|
| Data leakage | Medium | High | Review every feature to ensure that information available only after the prediction point is not used. Fit preprocessing only on training data. |
| Very small dataset | High | High | Treat the current model as an experimental baseline. Validate using a larger and representative dataset before production use. |
| False positives | Medium | Medium | Monitor precision and false-positive rates. Require human review before significant retention actions. |
| False negatives | Medium | High | Monitor recall and false-negative rates. Provide human review for uncertain or high-risk cases. |
| Class imbalance | Medium | Medium | Monitor both churn and non-churn classes and evaluate precision, recall and F1-score instead of relying only on accuracy. |
| Bias and poor representation | Unknown | High | Evaluate relevant customer groups when sufficient data is available and investigate material differences in model errors. |
| Privacy and data misuse | Unknown | High | Restrict access to authorized users and verify privacy, permission and permitted-use requirements before production deployment. |
| Identifier misuse | Medium | Medium | Exclude `customer_id` from model training because it is an identifier rather than a meaningful predictive feature. |
| Model degradation | Medium | High | Monitor model performance and input data over time. Suspend automated use if performance becomes unacceptable. |
| Data quality changes | Medium | High | Monitor missingness, unexpected values and changes in feature distributions. Investigate significant changes before continued use. |
| Uncertain predictions | Medium | Medium | Allow the model to abstain and send uncertain cases for human review instead of forcing an automated decision. |
| Automatic high-impact decisions | Low | High | Use the model only as decision support. Do not automatically cancel, deny or penalize customers based only on the model prediction. |

## Human Review

The model should support human decision-making rather than replace it.

Cases with uncertain predictions or potentially significant customer impact should be reviewed by an appropriate human decision-maker.

## Monitoring Conditions

The following should be monitored if the model is deployed:

- Accuracy
- Precision
- Recall
- F1-score
- False-positive rate
- False-negative rate
- Input data quality
- Missing-value rates
- Feature distribution changes
- Relevant subgroup performance where sufficient data exists

## Rollback Conditions

Automated use of the model should be suspended if:

- Significant model performance degradation is detected.
- Data leakage is discovered.
- Serious data quality problems are detected.
- Important input distributions change unexpectedly.
- Significant harmful differences in model performance are identified.
- False-positive or false-negative rates become unacceptable.

When a rollback condition occurs, the organization should return to a validated manual process or previously validated model while the issue is investigated.

## Overall Risk Assessment

The current model is an internship baseline built from a very small dataset of 12 customer records.

The model should not be considered production-ready.

A larger and representative dataset, validated prediction horizon, verified data permissions, stronger evaluation, human review, monitoring and rollback procedures are required before real-world deployment.