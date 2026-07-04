"""app_femi.py - custom feature engineering project.

A supervised regression project using chocolate sales data.

Author: Oluwafemi Salawu
Date: 2026-07-03

Process:
    - Load a CSV dataset.
    - Rename revenue to total_sales.
    - Create engineered features.
    - Train a supervised regression model.
    - Evaluate model performance.
    - Predict one new sale.
    - Create and save useful charts.

Data Source:
- data/raw/sales.csv

Terminal command to run this file from the root project folder:

uv run python -m mlstudio.app_femi
"""

# === Section 1a. DECLARE IMPORTS ===

import logging
from pathlib import Path
from typing import Final

from datafun_toolkit.logger import get_logger, log_header
from matplotlib.axes import Axes
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

# === Section 1b. CONFIGURE LOGGER ONCE PER MODULE ===

LOG: logging.Logger = get_logger("ML", level="DEBUG")
log_header(LOG, "ML")

# === Section 1c. Global Constants and Configuration ===

DATASET_NAME: Final[str] = "sales"
IMAGE_DIR: Final[Path] = Path("docs/images")

# Target column we want to predict.
TARGET_COL: Final[str] = "total_sales"

# Features used for prediction.
FEATURE_COLS: Final[list[str]] = [
    "quantity",
    "unit_price",
    "discount",
    "cost",
    "order_month",
    "order_day_of_week",
    "discounted_unit_price",
    "gross_sales",
    "discount_amount",
]

TEST_SIZE: Final[float] = 0.20
RANDOM_STATE: Final[int] = 42

pd.set_option("display.max_columns", 50)
pd.set_option("display.width", 120)


# === Section 2. Load the Data ===


def load_data() -> pd.DataFrame:
    """Load the chocolate sales dataset from the data/raw folder."""
    LOG.info(f"Loading dataset: {DATASET_NAME}")

    df: pd.DataFrame = pd.read_csv(f"data/raw/{DATASET_NAME}.csv")

    LOG.info(f"Loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    LOG.debug(f"\n{df.head()}")

    return df


# === Section 3. Inspect Data Shape and Structure ===


def inspect_basic(df: pd.DataFrame) -> None:
    """Inspect basic dataset structure."""
    LOG.info("Column names")
    LOG.debug(f"{list(df.columns)}")

    LOG.info("DataFrame info")
    df.info()

    LOG.info(f"Dataset shape: {df.shape[0]} rows, {df.shape[1]} columns")


# === Section 4. Check Data Quality ===


def check_quality(df: pd.DataFrame) -> None:
    """Check missing values and duplicate rows."""
    LOG.info("Missing values by column")
    LOG.debug(f"\n{df.isna().sum()}")

    duplicate_count: int = df.duplicated().sum()
    LOG.info(f"Duplicate row count: {duplicate_count}")


# === Section 5. Engineer Features ===


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create engineered features for the chocolate sales dataset."""
    LOG.info("Engineering new features")

    df_features = df.copy()

    # Rename revenue to total_sales for clearer target naming.
    if "revenue" in df_features.columns:
        df_features = df_features.rename(columns={"revenue": "total_sales"})

    # Convert order_date to datetime so we can create date-based features.
    df_features["order_date"] = pd.to_datetime(df_features["order_date"])

    # Date features.
    df_features["order_month"] = df_features["order_date"].dt.month
    df_features["order_day_of_week"] = df_features["order_date"].dt.dayofweek

    # Price and discount features.
    df_features["discounted_unit_price"] = df_features["unit_price"] * (
        1 - df_features["discount"]
    )
    df_features["gross_sales"] = df_features["quantity"] * df_features["unit_price"]
    df_features["discount_amount"] = (
        df_features["gross_sales"] * df_features["discount"]
    )

    LOG.info("Created engineered features")
    LOG.info(
        "New features: order_month, order_day_of_week, "
        "discounted_unit_price, gross_sales, discount_amount"
    )

    return df_features


# === Section 6. Create a Clean View ===


def make_clean_view(df: pd.DataFrame) -> pd.DataFrame:
    """Create a cleaned view for modeling."""
    LOG.info("Creating clean modeling view")

    selected_cols: list[str] = FEATURE_COLS + [TARGET_COL]

    df_selected: pd.DataFrame = df[selected_cols]  # type: ignore[assignment]
    df_no_missing: pd.DataFrame = df_selected.dropna()
    df_clean: pd.DataFrame = df_no_missing.copy()

    LOG.info(f"Clean view: {df_clean.shape[0]} rows, {df_clean.shape[1]} columns")

    return df_clean


# === Section 7. Train Supervised Model ===


def train_model(df_clean: pd.DataFrame) -> LinearRegression:
    """Train a supervised regression model."""
    LOG.info("Training LinearRegression model")

    x = df_clean[FEATURE_COLS]
    y = df_clean[TARGET_COL]

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
    )

    model = LinearRegression()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    mae: float = mean_absolute_error(y_test, y_pred)
    r2: float = r2_score(y_test, y_pred)

    LOG.info(f"Mean absolute error: {mae:.2f}")
    LOG.info(f"R-squared: {r2:.2f}")

    return model


# === Section 8. Predict One New Case ===


def predict_example(model: LinearRegression) -> None:
    """Use the trained model to predict one new chocolate sale."""
    LOG.info("Predicting one new chocolate sale")

    new_case = pd.DataFrame(
        [
            {
                "quantity": 4,
                "unit_price": 12.50,
                "discount": 0.10,
                "cost": 25.00,
                "order_month": 12,
                "order_day_of_week": 5,
                "discounted_unit_price": 12.50 * (1 - 0.10),
                "gross_sales": 4 * 12.50,
                "discount_amount": (4 * 12.50) * 0.10,
            }
        ]
    )

    predicted_total_sales: float = model.predict(new_case)[0]

    LOG.info(f"New case:\n{new_case}")
    LOG.info(f"Predicted total sales: {predicted_total_sales:.2f}")


# === Section 9. Create Visualizations ===


def make_plots(df_clean: pd.DataFrame, model: LinearRegression) -> None:
    """Create and save charts for the supervised regression project."""
    LOG.info("Creating output image folder if needed")
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)

    LOG.info("Creating chart: quantity vs total sales")

    fig, ax = plt.subplots(figsize=(9, 5))

    quantity_plt: Axes = sns.scatterplot(
        data=df_clean,
        x="quantity",
        y=TARGET_COL,
        ax=ax,
    )

    quantity_plt.set_title("Quantity vs Total Sales")
    quantity_plt.set_xlabel("Quantity")
    quantity_plt.set_ylabel("Total Sales")

    fig.tight_layout()
    quantity_path = IMAGE_DIR / "quantity_vs_total_sales_femi.png"
    fig.savefig(quantity_path)
    LOG.info(f"Saved chart: {quantity_path}")

    LOG.info("Creating chart: discounted unit price vs total sales")

    fig, ax = plt.subplots(figsize=(9, 5))

    price_plt: Axes = sns.scatterplot(
        data=df_clean,
        x="discounted_unit_price",
        y=TARGET_COL,
        ax=ax,
    )

    price_plt.set_title("Discounted Unit Price vs Total Sales")
    price_plt.set_xlabel("Discounted Unit Price")
    price_plt.set_ylabel("Total Sales")

    fig.tight_layout()
    price_path = IMAGE_DIR / "discounted_unit_price_vs_total_sales_femi.png"
    fig.savefig(price_path)
    LOG.info(f"Saved chart: {price_path}")

    LOG.info("Creating chart: model coefficients")

    fig, ax = plt.subplots(figsize=(9, 5))

    coefficient_df = pd.DataFrame(
        {
            "feature": FEATURE_COLS,
            "coefficient": model.coef_,
        }
    ).sort_values("coefficient", ascending=False)

    bar_plt: Axes = sns.barplot(
        data=coefficient_df,
        x="coefficient",
        y="feature",
        ax=ax,
    )

    bar_plt.set_title("Model Coefficients")
    bar_plt.set_xlabel("Coefficient")
    bar_plt.set_ylabel("Feature")

    fig.tight_layout()
    coefficient_path = IMAGE_DIR / "model_coefficients_sales_femi.png"
    fig.savefig(coefficient_path)
    LOG.info(f"Saved chart: {coefficient_path}")


# === Section 10. Summary and Next Steps ===


def summarize(
    df: pd.DataFrame, df_features: pd.DataFrame, df_clean: pd.DataFrame
) -> None:
    """Log a brief summary."""
    LOG.info("========================")
    LOG.info("SUMMARY")
    LOG.info("========================")
    LOG.info(f"Dataset: {DATASET_NAME}")
    LOG.info(f"Original rows: {df.shape[0]}")
    LOG.info(f"Rows after feature engineering: {df_features.shape[0]}")
    LOG.info(f"Clean rows: {df_clean.shape[0]}")
    LOG.info(f"Features: {FEATURE_COLS}")
    LOG.info(f"Target: {TARGET_COL}")
    LOG.info(
        "Technical modification: applied feature engineering to chocolate sales data"
    )
    LOG.info(
        "New problem: predict total_sales using quantity, price, discount, cost, "
        "date features, and engineered sales features"
    )


# === DEFINE THE MAIN FUNCTION THAT CALLS OTHER FUNCTIONS ===


def main() -> None:
    """Main function to run the supervised ML workflow."""
    log_header(LOG, "ML")

    LOG.info("========================")
    LOG.info("START main()")
    LOG.info("========================")

    LOG.info("Load dataset..............")
    df = load_data()

    LOG.info("Inspect dataset...........")
    inspect_basic(df)

    LOG.info("Check data quality........")
    check_quality(df)

    LOG.info("Engineer features.........")
    df_features = engineer_features(df)

    LOG.info("Create clean view.........")
    df_clean = make_clean_view(df_features)

    LOG.info("Train supervised model....")
    model = train_model(df_clean)

    LOG.info("Predict one case..........")
    predict_example(model)

    LOG.info("Create charts.............")
    make_plots(df_clean, model)

    LOG.info("Summarize workflow........")
    summarize(df, df_features, df_clean)

    LOG.info(
        "----- in a script, call plt.show() once at the end to display all charts -----"
    )
    LOG.info(
        "----- in a script, CLOSE the chart windows with the close button to CONTINUE -----"
    )

    plt.show()

    LOG.info("Workflow complete")
    LOG.info("IMPORTANT: This script creates chart windows.")
    LOG.info("Close chart windows and terminate this process with CTRL+c as needed.")
    LOG.info("========================")
    LOG.info("Executed successfully!")
    LOG.info("========================")


# === CONDITIONAL EXECUTION GUARD ===

if __name__ == "__main__":
    main()
