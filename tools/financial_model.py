"""Reproduce planning estimates. No agent, telemetry or model integration."""
from math import ceil

DAYS = 30
INPUT_TOKENS = 4_000
OUTPUT_TOKENS = 1_000
INPUT_USD_PER_MILLION = 1.0  # Assumed budget rate, not a vendor quote.
OUTPUT_USD_PER_MILLION = 4.0
HOURLY_COST = 50.0
CONTINGENCY = 0.20
INCIDENTS = 100
DEVELOPMENT = (200 + 40 + 40) * HOURLY_COST
PRICE_HYPOTHESIS = 699.0
SCENARIOS = {
    "low": (50, 100.0, 10.0, 2),
    "base": (100, 150.0, 20.0, 4),
    "high": (500, 300.0, 40.0, 8),
}


def monthly_cost(briefs_per_day, infrastructure, backup, maintenance_hours):
    briefs = briefs_per_day * DAYS
    inference = briefs * (
        INPUT_TOKENS * INPUT_USD_PER_MILLION
        + OUTPUT_TOKENS * OUTPUT_USD_PER_MILLION
    ) / 1_000_000
    cash_subtotal = infrastructure + backup + inference
    cash = cash_subtotal * (1 + CONTINGENCY)
    total = cash + maintenance_hours * HOURLY_COST
    return inference, cash, total


def main():
    print("North Maple Systems IT Operations Agent: unvalidated planning estimates, USD, 50 servers")
    for name, inputs in SCENARIOS.items():
        inference, cash, total = monthly_cost(*inputs)
        print(f"{name}: inference={inference:.2f}, cash={cash:.2f}, total={total:.2f}/month")
    base = monthly_cost(*SCENARIOS["base"])[2]
    for minutes in (0, 5, 10, 20):
        benefit = INCIDENTS * minutes / 60 * HOURLY_COST
        net = benefit - base
        payback = f"{DEVELOPMENT / net:.2f} months" if net > 0 else "no payback"
        print(f"{minutes} min saved: value={benefit:.2f}, net={net:.2f}, {payback}")
    yearly_cost = DEVELOPMENT + 12 * base
    yearly_benefit = INCIDENTS * 10 / 60 * HOURLY_COST * 12
    print(f"Development: {DEVELOPMENT:.2f}; first-year cost: {yearly_cost:.2f}")
    print(f"First-year net: {yearly_benefit - yearly_cost:.2f}; ROI: {(yearly_benefit / yearly_cost - 1) * 100:.2f}%")
    print(f"Break-even incidents at 10 minutes: {ceil(base / (10 / 60 * HOURLY_COST))}")
    print(f"Break-even minutes at 100 incidents: {base / (INCIDENTS * HOURLY_COST) * 60:.2f}")
    contribution = PRICE_HYPOTHESIS - base
    print(f"Price hypothesis {PRICE_HYPOTHESIS:.2f}: contribution={contribution:.2f}, margin={contribution / PRICE_HYPOTHESIS * 100:.2f}%")
    print(f"Price for 60% contribution margin: {base / 0.40:.2f}")
    print(f"Development recovery: {ceil(DEVELOPMENT / contribution)} customer-months before overhead")


if __name__ == "__main__":
    main()
