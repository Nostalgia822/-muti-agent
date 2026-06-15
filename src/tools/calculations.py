"""Calculation utilities for asset valuation"""


def calculate_depreciation(
    original_cost: float,
    age: int,
    useful_life: int,
    method: str = "straight_line"
) -> float:
    """Calculate depreciation using various methods.
    
    Args:
        original_cost: Original asset cost
        age: Current age of asset
        useful_life: Expected useful life
        method: Depreciation method (straight_line, declining_balance, etc.)
    
    Returns:
        Depreciated value
    """
    if method == "straight_line":
        # Straight-line depreciation
        annual_depreciation = original_cost / useful_life
        total_depreciation = annual_depreciation * age
        return max(original_cost - total_depreciation, 0)
    
    elif method == "declining_balance":
        # Double declining balance method
        rate = 2 / useful_life
        value = original_cost
        for _ in range(age):
            value = value * (1 - rate)
        return value
    
    else:
        return original_cost


def calculate_present_value(
    future_value: float,
    years: int,
    discount_rate: float
) -> float:
    """Calculate present value of future cash flows.
    
    Args:
        future_value: Future value amount
        years: Number of years
        discount_rate: Discount rate (as decimal, e.g., 0.08 for 8%)
    
    Returns:
        Present value
    """
    return future_value / ((1 + discount_rate) ** years)


def calculate_npv(
    cash_flows: list,
    discount_rate: float
) -> float:
    """Calculate net present value.
    
    Args:
        cash_flows: List of cash flows
        discount_rate: Discount rate (as decimal)
    
    Returns:
        Net present value
    """
    npv = 0
    for year, cf in enumerate(cash_flows):
        npv += cf / ((1 + discount_rate) ** year)
    return npv
