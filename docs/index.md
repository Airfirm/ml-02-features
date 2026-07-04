# Project Documentation

## Phase 4. Technical Modification

For my Phase 4 technical modification, I changed the example project from predicting a student score to predicting chocolate sales.
The original example used the `hours_scores_case` data to predict a student’s `score`. I modified the project to use the Chocolate Sales dataset and predict `total_sales`.

I changed the dataset from the small student score example to the Kaggle Chocolate Sales dataset.
I also renamed the original `revenue` column to `total_sales` so the target variable would be easier to understand. In addition, I created new engineered features from the existing data, including:

* `order_month`
* `order_day_of_week`
* `discounted_unit_price`
* `gross_sales`
* `discount_amount`

I chose this change because the `ml-02-features` project focuses on feature engineering.
Creating new features from date, price, quantity, and discount information helped me apply the skills from the module to a new business-related prediction problem.

I verified that the modification worked by running the project from the root folder with:

```shell
uv run python -m mlstudio.app_femi
```

The `project.log` confirmed that the dataset loaded successfully, the new features were created, the clean modeling view was created, the Linear Regression model trained,
a prediction was made, and charts were saved.

The log showed that the dataset had 1,000,000 rows and 11 original columns. After feature engineering, the clean view had 1,000,000 rows and 10 columns. The model produced:

* Mean absolute error: `0.00`
* R-squared: `1.00`
* Predicted total sales for one new case: `45.00`

The project also saved charts to the `docs/images` folder:

* `quantity_vs_total_sales_femi.png`
* `discounted_unit_price_vs_total_sales_femi.png`
* `model_coefficients_sales_femi.png`

Compared with the example project, my version uses a larger real-world sales dataset and creates new engineered features instead of only using the original columns.
This matters because feature engineering can help a model better represent the business logic behind sales.
For example, total sales are affected by quantity, price, and discount, so features like `gross_sales`, `discount_amount`, and `discounted_unit_price` are useful.

This modification was moderate.
The code structure was already organized, which helped, but it was more challenging than simply changing one value because I had to rename the target, create new features,
update the feature list, change the prediction case, save charts, and confirm everything worked using the log.

## Phase 5. Custom Project

For my custom project, I applied the feature engineering workflow to a new problem using the Chocolate Sales Dataset 2023–2024 from Kaggle.
Instead of predicting a student score, I created a sales prediction problem.

My custom prediction question is:

**Given quantity, unit price, discount, cost, order month, day of week, and engineered price features, I want to predict total sales.**

This changed the project from an educational student-score example to a business sales prediction example.
The custom project uses sales transaction data to predict the amount of revenue from a chocolate sale.

### Basis and Data

The original example dataset was a small student score dataset. It used features such as:

* `hours_studied`
* `practice_quizzes`
* `attendance_pct`
* `sleep_hours`
* `prior_score`

The original target was:

* `score`

For my custom project, I used the Chocolate Sales Dataset 2023–2024 from Kaggle. The dataset file is named `sales.csv`.

The source is:

```text
https://www.kaggle.com/datasets/ssssws/chocolate-sales-dataset-2023-2024
```

The raw data file is kept locally at:

```text
data/raw/sales.csv
```

The original dataset columns included:

* `order_id`
* `order_date`
* `product_id`
* `store_id`
* `customer_id`
* `quantity`
* `unit_price`
* `discount`
* `revenue`
* `cost`
* `profit`

I chose this dataset because it connects feature engineering to a realistic business problem. Sales data is useful for understanding how quantity, price, discount, and timing affect total sales.
I changed the original example because I wanted to apply the skills to a different dataset that had more rows and more opportunities for feature engineering.

One important limitation is that the dataset is very large, with 1,000,000 rows. Because the file is large, it should not be committed directly to GitHub.
Instead, the README should explain that users need to download `sales.csv` from Kaggle and place it in `data/raw/sales.csv`.

Another assumption is that `revenue` represents the total sales amount. I renamed this column to `total_sales` for clarity.

### Modeling Approach

This project uses supervised learning.

I know it is supervised because the dataset has a known target value that the model is trying to predict. The target variable is `total_sales`.

This is a regression task because the target is numeric. The model is predicting a continuous sales amount instead of a category.

This project is not classification because the target is not a label such as “high” or “low.” It is not clustering because the model is not just finding groups.
It is also not a recommendation system because it is not recommending products. The task is supervised regression.

A numeric target works well for this approach. Since `total_sales` is a number, a regression model can learn the relationship between input features and the target sales amount.

I used Linear Regression because it is appropriate for an introductory supervised regression workflow.
It is simple, easy to interpret, and works well when the target is closely related to numeric features such as quantity, unit price, discount, and engineered sales values.

### Target

In the original example, the target variable was:

```text
score
```

The model used student study habits and prior performance to predict a student’s final score.

In my custom project, the target variable is:

```text
total_sales
```

This target came from the original `revenue` column, which I renamed to `total_sales`.

Changing the target changes the meaning of the model. Instead of predicting an academic score, the model predicts a business sales amount.
The evaluation still uses regression metrics because both targets are numeric. However, the interpretation is different. In the original example, the prediction tells us an expected student score.
In my project, the prediction tells us an expected sales amount for a chocolate transaction.

### Features

The original example features were:

* `hours_studied`
* `practice_quizzes`
* `attendance_pct`
* `sleep_hours`
* `prior_score`

These features were used to predict `score`.

For my custom project, I used the following features:

* `quantity`
* `unit_price`
* `discount`
* `cost`
* `order_month`
* `order_day_of_week`
* `discounted_unit_price`
* `gross_sales`
* `discount_amount`

I kept useful numeric features from the sales dataset, such as `quantity`, `unit_price`, `discount`, and `cost`.
I removed ID columns such as `order_id`, `product_id`, `store_id`, and `customer_id` from the model because they are identifiers and are not directly useful as numeric
regression features without additional encoding.

I added date-based features from `order_date`:

* `order_month`
* `order_day_of_week`

These may help the model capture sales patterns related to seasonality or shopping behavior.

I also added engineered sales features:

* `discounted_unit_price`
* `gross_sales`
* `discount_amount`

These features are useful because they combine price, quantity, and discount information. They help represent the actual business calculation behind total sales.

### Evaluation and Results

I evaluated the model using regression metrics:

* Mean absolute error
* R-squared

The `project.log` showed:

```text
Mean absolute error: 0.00
R-squared: 1.00
```

The model also predicted one new chocolate sale. The new case used:

* `quantity`: 4
* `unit_price`: 12.50
* `discount`: 0.10
* `cost`: 25.00
* `order_month`: 12
* `order_day_of_week`: 5
* `discounted_unit_price`: 11.25
* `gross_sales`: 50.00
* `discount_amount`: 5.00

The predicted total sales amount was:

```text
45.00
```

This result makes sense because 4 items at $12.50 each equals $50.00 in gross sales, and a 10% discount equals $5.00. After the discount, the total sales amount is $45.00.

The result was useful because it confirmed that the feature engineering captured the relationship between quantity, price, discount, and total sales.
However, the result was also a reminder that some engineered features may be very close to the target calculation.
Because `gross_sales` and `discount_amount` directly relate to `total_sales`, the model may perform almost perfectly.
A future improvement would be to test models with and without those directly related features to see how much they influence the results.

The project also created and saved charts to the `docs/images` folder:

![Quantity vs Total Sales](./images/quantity_vs_total_sales_femi.png)

This chart shows the relationship between quantity and total sales.

![Discounted Unit Price vs Total Sales](./images/discounted_unit_price_vs_total_sales_femi.png)

This chart shows the relationship between discounted unit price and total sales.

![Model Coefficients](./images/model_coefficients_sales_femi.png)

This chart shows how each feature contributed to the Linear Regression model.

### Summary

I implemented my custom model by modifying the original example app and applying it to a new sales prediction problem.
I changed the data source to the Chocolate Sales dataset, renamed `revenue` to `total_sales`, engineered new features, updated the feature list, trained a
Linear Regression model, made one prediction, and saved charts to the documentation images folder.

The model loaded 1,000,000 rows and 11 original columns. It found no missing values and no duplicate rows. After feature engineering, the clean modeling view had 1,000,000 rows and 10 columns.

The main results were:

* Mean absolute error: `0.00`
* R-squared: `1.00`
* Predicted total sales for one new case: `45.00`

I learned that feature engineering can make a model much more connected to the real-world meaning of the data.
Creating features such as `discounted_unit_price`, `gross_sales`, and `discount_amount` helped show how the sales amount is affected by quantity, price, and discount.

I exercised the skills covered in this project by loading a new dataset, checking data quality, creating new features, selecting a target, selecting input features,
training a model, evaluating results, creating visuals, saving artifacts, and documenting the workflow.

These skills could be applied to many real business problems in the future, such as predicting sales, forecasting demand, estimating customer spending, evaluating discounts,
or identifying which features have the strongest relationship with revenue.
