import streamlit as st

st.title("Loan Comparison Tool")

st.header("Loan 1")
loan1 = st.number_input("Loan 1 amount (RM)", key="l1")
months1 = st.number_input("Loan 1 months", key="m1")
monthly1 = st.number_input("Loan 1 monthly (RM)", key="p1")

total1 = monthly1 * months1
interest1 = total1 - loan1

st.header("Loan 2")
loan2 = st.number_input("Loan 2 amount (RM)", key="l2")
months2 = st.number_input("Loan 2 months", key="m2")
monthly2 = st.number_input("Loan 2 monthly (RM)", key="p2")

total2 = monthly2 * months2
interest2 = total2 - loan2

st.subheader("Result")

st.write(f"Loan 1 Total: RM {total1:,.2f} | Interest: RM {interest1:,.2f}")
st.write(f"Loan 2 Total: RM {total2:,.2f} | Interest: RM {interest2:,.2f}")

if total1 < total2:
    st.success("Loan 1 is cheaper")
elif total2 < total1:
    st.success("Loan 2 is cheaper")
else:
    st.info("Both loans are equal")