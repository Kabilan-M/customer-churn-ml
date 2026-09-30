# Responsible Data Card

## Dataset purpose

This dataset is used to support customer churn prediction.

The intended decision is to identify customers who may be at risk of leaving so that a retention team can review the risk and decide whether an appropriate retention action is needed.

The model should support human decision-making. It must not automatically cancel a customer's service, deny a customer a service, or make other high-impact decisions without appropriate human review.

## Provenance and permission

The dataset was provided by RabTech Academy as the starter customer churn training dataset for this internship task.

The supplied materials do not document the original data collection process, individual consent status, licensing terms, or the identities of the original data subjects.

Therefore, consent and licensing should not be assumed from the dataset alone.

Before production use, the organization should verify that the data was collected and can be used for customer churn prediction for the intended purpose.

## Population and representation

The dataset contains 12 customer records.

The dataset includes customers represented by the following plan types:

- Basic
- Standard
- Pro

The dataset is small and may not represent the full population of real-world customers.

The supplied dataset does not provide enough information to determine whether all relevant customer groups are represented or whether the sample is representative of a larger customer population.

The dataset contains 5 churned customers and 7 customers who did not churn.

Because the dataset is small, model performance and observed patterns should not be assumed to generalize to a larger production population without additional validation.

## Features and target

The dataset contains the following features:

- customer_id: Identifier for each customer. It should generally not be used as a predictive feature.
- tenure_months: Number of months associated with the customer's tenure.
- support_tickets: Number of support tickets associated with the customer.
- monthly_spend_inr: Customer's monthly spending amount in INR.
- last_login_days: Number of days since the customer's last login.
- plan_type: Customer's subscription plan type.
- churned: Target label indicating whether the customer churned. A value of 1 represents churn and a value of 0 represents no churn.

Potential leakage must be checked before model training. Any feature that contains information that would only become available after the churn decision or after the prediction point should not be used for prediction.

The dataset does not document any explicit sensitive attributes. However, potential proxy relationships should still be considered before production deployment.

## Quality checks

The dataset contains 12 rows and 7 columns.

Missing-value check:

- No missing values were found in the supplied dataset.

Duplicate check:

- No duplicate rows were found in the supplied dataset.

Target balance:

- Churned customers: 5
- Non-churned customers: 7

The target is therefore not perfectly balanced, but both classes are represented.

The dataset is very small, so train/test evaluation results may have high uncertainty. A separate validation dataset or larger dataset would be required before production use.

Train/test separation should be performed before fitting preprocessing steps or the model to avoid data leakage.

## Risks and safeguards

### Data leakage risk

A feature may contain information that would not be available at the time the churn prediction is made.

Safeguard:
Review every feature and remove any feature that contains future information. Fit preprocessing only on the training data.

### Small dataset risk

The dataset contains only 12 customer records, so a model may not generalize well to new customers.

Safeguard:
Treat the model as a baseline only and validate it using a substantially larger and representative dataset before production use.

### False-positive risk

A false positive occurs when the model predicts that a customer will churn when the customer would not have churned.

Possible impact:
The company may spend unnecessary retention resources or offer unnecessary incentives.

Safeguard:
Monitor precision and false-positive rates and use human review before taking significant customer actions.

### False-negative risk

A false negative occurs when the model predicts that a customer will not churn when the customer would actually churn.

Possible impact:
A potentially at-risk customer may be missed, resulting in a missed retention opportunity.

Safeguard:
Monitor recall and false-negative rates and provide a human-review process for uncertain or high-risk cases.

### Privacy risk

The dataset contains a customer identifier and customer-related behavioral and spending attributes. It does not provide names, phone numbers, email addresses, or other directly identifying contact information in the supplied columns.

Safeguard:
Limit access to authorized users, avoid exposing unnecessary customer information, and verify privacy and permitted-use requirements before production deployment.

### Bias and representation risk

The small dataset may not represent the broader customer population. Differences in customer groups may therefore be missed.

Safeguard:
Evaluate performance across relevant groups when sufficient data is available and investigate material differences in error rates before deployment.

### Misuse risk

A churn prediction should not be used as the sole basis for punitive or high-impact decisions about customers.

Safeguard:
Use the model as decision support, require appropriate human review, document the intended use, and restrict out-of-scope uses.

### Model degradation risk

Customer behavior and data patterns may change over time.

Safeguard:
Monitor model performance and input data after deployment. Suspend automated use and return to a validated manual or previous process if performance or data quality becomes unacceptable.

## Intended evaluation

The first evaluation should compare the machine-learning model against a simple non-ML baseline.

Baseline:
A majority-class classifier that predicts the most common target class for every customer.

Model performance measures:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix
- ROC-AUC, where appropriate

Because false negatives and false positives have different business consequences, precision and recall should be considered alongside accuracy rather than relying on accuracy alone.

Error analysis should examine false positives and false negatives to understand where the model makes mistakes.

Before production use, evaluation should also consider:

- Calibration of predicted probabilities
- Performance on a larger independent validation dataset
- Relevant subgroup performance where sufficient data exists
- Data quality and missingness
- Potential data leakage
- Changes in data distribution over time

If the model is uncertain about a prediction, it should be able to abstain and send the case for human review rather than forcing an automated decision.