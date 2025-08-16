expenses = [
    {"item": "Groceries", "amount": 1200},
    {"item": "Transport", "amount": 300},
    {"item": "Utilities", "amount": 1500}
]

total = sum(e["amount"] for e in expenses)
print(f"Total expenses: ₹{total}")

import streamlit as st

st.title("💸 Personal Expense Tracker")

# Input form
item = st.text_input("Item")
amount = st.number_input("Amount (Rs)", min_value=0.0)

if "expenses" not in st.session_state:
    st.session_state.expenses = []

if st.button("Add Expense"):
    st.session_state.expenses.append({"item": item, "amount": amount})
    st.success(f"Added: {item} - Rs{amount}")

# Display expenses
st.subheader("Your Expenses")
total = sum(e["amount"] for e in st.session_state.expenses)
for e in st.session_state.expenses:
    st.write(f"{e['item']}: Rs{e['amount']}")

st.write(f"**Total expenses:** Rs{total}")
import pandas as pd
import altair as alt

if st.session_state.expenses:
    df = pd.DataFrame(st.session_state.expenses)
    chart = alt.Chart(df).mark_arc().encode(
        theta="amount",
        color="item"
    )
    st.altair_chart(chart, use_container_width=True)
if st.button("Save to CSV"):
    df = pd.DataFrame(st.session_state.expenses)
    df.to_csv("expenses.csv", index=False)
    st.success("Expenses saved to expenses.csv")
import os

if os.path.exists("expenses.csv"):
    st.session_state.expenses = pd.read_csv("expenses.csv").to_dict("records")
# Convert to DataFrame
df = pd.DataFrame(st.session_state.expenses)

if not df.empty:
    st.subheader("📊 Spending by Category")
    chart = alt.Chart(df).mark_bar().encode(
        x="item",
        y="amount",
        tooltip=["item", "amount"]
    ).properties(width=600)

    st.altair_chart(chart)
def categorize(item):
    item = item.lower()
    if "uber" in item or "bus" in item:
        return "Transport"
    elif "pizza" in item or "groceries" in item:
        return "Food"
    elif "electricity" in item or "water" in item:
        return "Utilities"
    else:
        return "Other"
category = categorize(item)
st.session_state.expenses.append({"item": item, "amount": amount, "category": category})