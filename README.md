# ml-02-features

[![Workflow Guide](https://img.shields.io/badge/Pro--Guide-pro--analytics--02-green)](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](./pyproject.toml)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Professional Python project: engineering and selecting features for machine learning.

## Project Description

This project focuses on how to prepare data for machine learning
by engineering and selecting features.

We learn to:

- handle missing values and outliers
- encode categorical variables
- scale and transform numeric features
- select the features most likely to help a model

Good features matter a great deal. This project helps build that intuition.

## Example Notebook + Your Notebook

Keep the example notebook as it is.
Either copy it or use it to build a new notebook that ends in _yourname.
See [docs/your-files.md] for more.

Links:

- [ml_02_case.ipynb](notebooks/ml_02_case.ipynb)

## Working Files

You'll work with these areas:

- **data/raw** - raw data for exploration (only if you add a dataset)
- **docs/** - project narrative and documentation
- **src/mlstudio/** - the app is an example; run only (no need to modify)
- **notebooks/** - interactive analysis
- **pyproject.toml** - update authorship & links
- **zensical.toml** - update authorship & links

## Instructions (pro-analytics-02)

Follow the
[step-by-step workflow guide](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to complete:

1. Phase 1. **Start & Run**
2. Phase 2. **Change Authorship**
3. Phase 3. **Read & Understand**
4. Phase 4. **Modify**
5. Phase 5. **Apply**

## Challenges

Challenges are expected.
Sometimes instructions may not quite match your operating system.
When issues occur, share screenshots, error messages, and details about what you tried.
Working through issues is part of implementing professional projects.

## Success

After completing Phase 1. **Start & Run**, you'll have your own GitHub project,
with the example notebook executed and committed,
and running the example module will print out:

```shell
========================
Executed successfully!
========================
```

A new file `project.log` will appear in the root project folder.

## Command Reference

<details>
<summary>Show command reference</summary>

### In a machine terminal (open in your `Repos` folder)

After you get a copy of this repo in your own GitHub account,
open a machine terminal in your `Repos` folder:

```shell
# Replace username with YOUR GitHub username.
git clone https://github.com/Airfirm/ml-02-features

cd ml-02-features
code .
```

### In a VS Code terminal

These are listed for convenience.
For best results, follow the detailed instructions in
[pro-analytics-02 guide](https://denisecase.github.io/pro-analytics-02/).

```shell
uv self update
uv python pin 3.14
uv lock --upgrade
uv sync --extra dev --extra docs --upgrade

uvx pre-commit install
uvx pre-commit autoupdate

git add -A
uvx pre-commit run --all-files
# repeat if changes were made
uvx pre-commit run --all-files

# run the example module to verify the environment (.venv/)
uv run python -m mlstudio.app_case

# run common chores
uv run ruff format .
uv run ruff check . --fix
uv run python -m pyright
uv run python -m pytest
uv run python -m zensical build

# save progress
git add -A
git commit -m "update"
git push -u origin main
```

</details>

## Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.
- You do not need to add to or modify `tests/`. They are provided for example only.
- Many files are silent helpers. Explore as you like, but nothing is required.
- You do NOT need to understand everything; understanding builds naturally over time.

## Troubleshooting >>>

If you see something like this in your terminal: `>>>` or `...`
You accidentally started Python interactive mode.
It happens.
Press `Ctrl+c` (both keys together) or `Ctrl+Z` then `Enter` on Windows.

## Example Output (Can Remove this Section after You Verify)

```shell
2026-07-04 11:00:52 | INFO | ML | === RUN START ===
2026-07-04 11:00:52 | INFO | ML | project=ML
2026-07-04 11:00:52 | INFO | ML | repo_dir=ml-02-features
2026-07-04 11:00:52 | INFO | ML | python=3.14.2
2026-07-04 11:00:52 | INFO | ML | os=Windows 11
2026-07-04 11:00:52 | INFO | ML | shell=powershell
2026-07-04 11:00:52 | INFO | ML | cwd=.
2026-07-04 11:00:52 | INFO | ML | github_actions=False
2026-07-04 11:00:52 | INFO | ML | === RUN START ===
2026-07-04 11:00:52 | INFO | ML | project=ML
2026-07-04 11:00:52 | INFO | ML | repo_dir=ml-02-features
2026-07-04 11:00:52 | INFO | ML | python=3.14.2
2026-07-04 11:00:52 | INFO | ML | os=Windows 11
2026-07-04 11:00:52 | INFO | ML | shell=powershell
2026-07-04 11:00:52 | INFO | ML | cwd=.
2026-07-04 11:00:52 | INFO | ML | github_actions=False
2026-07-04 11:00:52 | INFO | ML | ========================
2026-07-04 11:00:52 | INFO | ML | START main()
2026-07-04 11:00:52 | INFO | ML | ========================
2026-07-04 11:00:52 | INFO | ML | Load dataset..............
2026-07-04 11:00:52 | INFO | ML | Loading dataset: sales
2026-07-04 11:00:53 | INFO | ML | Loaded: 1000000 rows, 11 columns
2026-07-04 11:00:53 | DEBUG | ML |
      order_id  order_date product_id store_id customer_id  quantity  unit_price  discount  revenue   cost  profit
0  0RD00000001  2023-01-07      P0080     S093     C040749         5       14.43      0.15    61.33  42.77   18.56
1  0RD00000002  2023-10-22      P0173     S065     C020161         3       12.01      0.00    36.03  19.06   16.97
2  0RD00000003  2023-05-07      P0115     S078     C048069         2       10.02      0.00    20.04  10.29    9.75
3  0RD00000004  2024-06-23      P0186     S088     C047901         2       14.66      0.10    26.39  16.35   10.04
4  0RD00000005  2024-09-24      P0197     S054     C033950         1       12.34      0.00    12.34   7.94    4.40
2026-07-04 11:00:53 | INFO | ML | Inspect dataset...........
2026-07-04 11:00:53 | INFO | ML | Column names
2026-07-04 11:00:53 | DEBUG | ML | ['order_id', 'order_date', 'product_id', 'store_id', 'customer_id', 'quantity', 'unit_price', 'discount', 'revenue', 'cost', 'profit']
2026-07-04 11:00:53 | INFO | ML | DataFrame info
<class 'pandas.DataFrame'>
RangeIndex: 1000000 entries, 0 to 999999
Data columns (total 11 columns):
 #   Column       Non-Null Count    Dtype
---  ------       --------------    -----
 0   order_id     1000000 non-null  str
 1   order_date   1000000 non-null  str
 2   product_id   1000000 non-null  str
 3   store_id     1000000 non-null  str
 4   customer_id  1000000 non-null  str
 5   quantity     1000000 non-null  int64
 6   unit_price   1000000 non-null  float64
 7   discount     1000000 non-null  float64
 8   revenue      1000000 non-null  float64
 9   cost         1000000 non-null  float64
 10  profit       1000000 non-null  float64
dtypes: float64(5), int64(1), str(5)
memory usage: 83.9 MB
2026-07-04 11:00:53 | INFO | ML | Dataset shape: 1000000 rows, 11 columns
2026-07-04 11:00:53 | INFO | ML | Check data quality........
2026-07-04 11:00:53 | INFO | ML | Missing values by column
2026-07-04 11:00:53 | DEBUG | ML |
order_id       0
order_date     0
product_id     0
store_id       0
customer_id    0
quantity       0
unit_price     0
discount       0
revenue        0
cost           0
profit         0
dtype: int64
2026-07-04 11:00:54 | INFO | ML | Duplicate row count: 0
2026-07-04 11:00:54 | INFO | ML | Engineer features.........
2026-07-04 11:00:54 | INFO | ML | Engineering new features
2026-07-04 11:00:54 | INFO | ML | Created engineered features
2026-07-04 11:00:54 | INFO | ML | New features: order_month, order_day_of_week, discounted_unit_price, gross_sales, discount_amount
2026-07-04 11:00:54 | INFO | ML | Create clean view.........
2026-07-04 11:00:54 | INFO | ML | Creating clean modeling view
2026-07-04 11:00:54 | INFO | ML | Clean view: 1000000 rows, 10 columns
2026-07-04 11:00:54 | INFO | ML | Train supervised model....
2026-07-04 11:00:54 | INFO | ML | Training LinearRegression model
2026-07-04 11:00:55 | INFO | ML | Mean absolute error: 0.00
2026-07-04 11:00:55 | INFO | ML | R-squared: 1.00
2026-07-04 11:00:55 | INFO | ML | Predict one case..........
2026-07-04 11:00:55 | INFO | ML | Predicting one new chocolate sale
2026-07-04 11:00:55 | INFO | ML | New case:
   quantity  unit_price  discount  cost  order_month  order_day_of_week  discounted_unit_price  gross_sales  \
0         4        12.5       0.1  25.0           12                  5                  11.25         50.0

   discount_amount
0              5.0
2026-07-04 11:00:55 | INFO | ML | Predicted total sales: 45.00
2026-07-04 11:00:55 | INFO | ML | Create charts.............
2026-07-04 11:00:55 | INFO | ML | Creating output image folder if needed
2026-07-04 11:00:55 | INFO | ML | Creating chart: quantity vs total sales
2026-07-04 11:00:57 | INFO | ML | Saved chart: docs\images\quantity_vs_total_sales_femi.png
2026-07-04 11:00:57 | INFO | ML | Creating chart: discounted unit price vs total sales
2026-07-04 11:00:59 | INFO | ML | Saved chart: docs\images\discounted_unit_price_vs_total_sales_femi.png
2026-07-04 11:00:59 | INFO | ML | Creating chart: model coefficients
2026-07-04 11:00:59 | INFO | ML | Saved chart: docs\images\model_coefficients_sales_femi.png
2026-07-04 11:00:59 | INFO | ML | Summarize workflow........
2026-07-04 11:00:59 | INFO | ML | ========================
2026-07-04 11:00:59 | INFO | ML | SUMMARY
2026-07-04 11:00:59 | INFO | ML | ========================
2026-07-04 11:00:59 | INFO | ML | Dataset: sales
2026-07-04 11:00:59 | INFO | ML | Original rows: 1000000
2026-07-04 11:00:59 | INFO | ML | Rows after feature engineering: 1000000
2026-07-04 11:00:59 | INFO | ML | Clean rows: 1000000
2026-07-04 11:00:59 | INFO | ML | Features: ['quantity', 'unit_price', 'discount', 'cost', 'order_month', 'order_day_of_week', 'discounted_unit_price', 'gross_sales', 'discount_amount']
2026-07-04 11:00:59 | INFO | ML | Target: total_sales
2026-07-04 11:00:59 | INFO | ML | Technical modification: applied feature engineering to chocolate sales data
2026-07-04 11:00:59 | INFO | ML | New problem: predict total_sales using quantity, price, discount, cost, date features, and engineered sales features
2026-07-04 11:00:59 | INFO | ML | ----- in a script, call plt.show() once at the end to display all charts -----
2026-07-04 11:00:59 | INFO | ML | ----- in a script, CLOSE the chart windows with the close button to CONTINUE -----
2026-07-04 11:05:05 | INFO | ML | Workflow complete
2026-07-04 11:05:05 | INFO | ML | IMPORTANT: This script creates chart windows.
2026-07-04 11:05:05 | INFO | ML | Close chart windows and terminate this process with CTRL+c as needed.
2026-07-04 11:05:05 | INFO | ML | ========================
2026-07-04 11:05:05 | INFO | ML | Executed successfully!
2026-07-04 11:05:05 | INFO | ML | ========================
```

## Findings and Visuals

Take screenshots of your charts and provide them here with a discussion.
In Markdown, display a figure by using:
an exclamation mark immediately followed by square brackets containing a useful caption
immediately followed by parentheses containing the relative path to your figure.
Note: When you start typing the path with a dot (.) for "here, in this directory",
the IDE may help complete the path.

In your custom project, follow this example, but

- your figures and narrative should reflect your work,
- this `README.md` should include your commands, process, and visuals, and
- `docs/index.md` should include your narrative.

Remove unnecessary instructional comments in your custom files.

Update figures to present interesting results from your custom project:

![Provide a Useful Caption](./docs/images/Figure_1.png)

![Provide a Useful Caption](./docs/images/Figure_2.png)

## Project Documentation

Additional project instructions, terms, and notes:

[docs/index.md](docs/index.md)

## Citation

[CITATION.cff](./CITATION.cff)

## License

[MIT](./LICENSE)
