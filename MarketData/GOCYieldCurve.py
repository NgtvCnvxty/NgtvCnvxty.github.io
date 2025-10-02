################################################################################
### YIELD CURVE INTERPOLATION AND ANIMATION USING REAL DATA
################################################################################

from typing import List
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
from numpy import float64
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib
matplotlib.use('Qt5Agg')  # Set interactive backend explicitly

###############################################################################
# CONSTANTS
###############################################################################

# Data
FILE_PATH = 'GOC.xlsx'
SHEET_NAME = 'Curve'
MATURITIES = [2, 3, 5, 7, 10, 30]  # Column tenors in SHEET_NAME (will not change)

# Spline Test and Evaluation
TEST_DATE_TERM = 4.3 # Date to evaluation interpolating function
TEST_DATE = '2020-09-29' # Date of curve to use to calculate interpolating function; Must be in SHEET_NAME

# Animation
START_DATE = '2001-01-02' # Date must be in SHEET_NAME
END_DATE = '2025-09-26' # Date must be in SHEET_NAME
INTERVAL = 1  # Delay in milliseconds between animation refresh
REPEAT = False   # Whether to repeat animation after last frame
REPEAT_DELAY = 10  # Delay in milliseconds after last frame if repeat
Y_MAX = 7.0 # max value of the y-axis as a %
TEST_ANIMATION_TIME_STEP = 1 # Number of days between frames in main test

###############################################################################
# HELPER FUNCTIONS
###############################################################################

def load_data() -> pd.DataFrame:
    """
    Loads the yield curve data from the Excel file.

    :return: DataFrame with dates as index (datetime) and yields as columns.
    """
    df = pd.read_excel(FILE_PATH, sheet_name=SHEET_NAME, index_col=0, parse_dates=True)

    # Convert column names from strings to integers
    df.columns = df.columns.astype(int)

    df = df.sort_index()  # Ensure chronological order
    return df

###############################################################################
# MAIN FUNCTIONS
###############################################################################

def get_spline_for_date(date: str) -> CubicSpline:
    """
    Returns the natural cubic spline for the yield curve on the given date.

    :param date: Date in 'YYYY-MM-DD' format.
    :return: CubicSpline object.
    :raises ValueError: If the date is not in the data.
    """
    df = load_data()
    try:
        dt = pd.to_datetime(date)
    except ValueError:
        raise ValueError(f"Invalid date format: {date}. Use 'YYYY-MM-DD'.")
    if dt not in df.index:
        raise ValueError(f"No data available for date: {date}.")
    yields = df.loc[dt].values
    return CubicSpline(MATURITIES, yields, bc_type='natural')

def evaluate_spline(date: str, term: float) -> float:
    """
    Evaluates the interpolated yield at the given term for the specified date.

    :param date: Date in 'YYYY-MM-DD' format.
    :param term: Term to maturity in years (between 2 and 30).
    :return: Interpolated yield.
    :raises ValueError: If date not in data or term out of bounds.
    """
    if not (2 <= term <= 30):
        raise ValueError(f"Term {term} must be between 2 and 30 years.")
    spline = get_spline_for_date(date)
    return spline(term)

def animate_yield_curve(start_date: str, end_date: str, timestep_days: int):
    """
    Animates the yield curve evolution from start_date to end_date,
    stepping by every timestep_days trading days.

    :param start_date: Start date in 'YYYY-MM-DD' format.
    :param end_date: End date in 'YYYY-MM-DD' format.
    :param timestep_days: Step size in terms of trading days (e.g., 1 for every day, 5 for every 5th).
    :raises ValueError: If start or end date not in data, or invalid inputs.
    """
    df = load_data()
    try:
        start_dt = pd.to_datetime(start_date)
        end_dt = pd.to_datetime(end_date)
    except ValueError:
        raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")
    if start_dt > end_dt:
        raise ValueError("Start date must be before or equal to end date.")
    if timestep_days < 1:
        raise ValueError("timestep_days must be at least 1.")

    # Filter data between start and end (inclusive)
    filtered_df = df.loc[(df.index >= start_dt) & (df.index <= end_dt)]
    if filtered_df.empty:
        raise ValueError("No data in the specified date range.")
    if start_dt not in filtered_df.index:
        raise ValueError(f"No data for start date: {start_date}.")
    if end_dt not in filtered_df.index:
        raise ValueError(f"No data for end date: {end_date}.")

    # Select every timestep_days row
    selected_df = filtered_df.iloc[::timestep_days]
    dates = selected_df.index

    # Compute global max for y-lim
    #global_max = selected_df.max().max()
    upper_lim = Y_MAX

    # Enable interactive mode if needed
    plt.ion()

    # Animation Setup
    fig, ax = plt.subplots(figsize=(14, 5), facecolor='black')

    # Maximize the animation window
    manager = plt.get_current_fig_manager()
    manager.window.showMaximized()

    def update(frame: int):
        ax.clear()
        ax.set_facecolor('black')
        ax.tick_params(axis='both', colors='white')
        for spine in ax.spines.values():
            spine.set_color('white')
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.title.set_color('white')

        current_date = dates[frame]
        current_yields = selected_df.loc[current_date].values.astype(float)

        try:
            spline = CubicSpline(MATURITIES, current_yields, bc_type='natural')
            time = np.linspace(min(MATURITIES), max(MATURITIES), 100)  # Curve from 2 to 30
            ax.plot(time, spline(time), color='#d73a49')
            ax.plot(MATURITIES, current_yields, 'o', color='#04b73c')
            ax.set_title(f'Interpolated Yield Curve (Natural Cubic Spline) on {current_date.date()}')
            ax.set_xlabel('Term (years)')
            ax.set_ylabel('Yield to Maturity (%)')
            ax.set_xlim(0, 31)  # <-- Full visible x-axis range
            ax.set_ylim(0, upper_lim)
            ax.grid(True, color='white', linestyle='--', alpha=0.3)
        except ValueError as e:
            ax.text(0.5, 0.5, f'Error for {current_date.date()}: {str(e)}', ha='center', va='center',
                    transform=ax.transAxes, color='red')

    # Create animation
    ani = FuncAnimation(fig, update, frames=len(dates), interval=INTERVAL, repeat=REPEAT, repeat_delay=REPEAT_DELAY)
    # Show animation
    plt.show(block=True)

if __name__ == "__main__":

    # Test the spline and evaluation functions
    TEST_TERM = 4.3
    TEST_DATE_TERM = '2020-09-29'
    try:
        spline = get_spline_for_date(TEST_DATE_TERM)
        print(f"Spline for {TEST_DATE_TERM} created successfully.")
        yield_value = evaluate_spline(TEST_DATE_TERM, TEST_TERM)
        print(f"Interpolated yield at {TEST_TERM} years on {TEST_DATE_TERM}: {yield_value:.3f}%")
    except ValueError as e:
        print(f"Error in spline/evaluation test: {e}")

    # Test the animation with a small range (adjust dates if needed based on your data)
    start = START_DATE
    end = END_DATE
    step = TEST_ANIMATION_TIME_STEP
    try:
        animate_yield_curve(start, end, step)
    except ValueError as e:
        print(f"Error in animation test: {e}")