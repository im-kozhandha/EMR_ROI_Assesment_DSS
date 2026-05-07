# EMR ROI & Paperless Assessment Tool

## Overview

This project is a simple decision-making tool built using Streamlit. It helps hospital owners understand whether switching from paper records to EMR (Electronic Medical Records) is financially worth it.

Instead of guessing, the tool shows actual numbers like savings, ROI, and how long it will take to recover the investment.

---

## Why I built this

Hospitals are often unsure about moving to EMR because:

* It costs a lot initially
* They are worried about disruption
* They don’t know if it will actually give returns

So I built this tool to make that decision easier using data.

---

## What the tool does

You enter basic details about your hospital, and it calculates:

* Monthly savings
* ROI (profit compared to cost)
* Payback period (how long to recover investment)
* Break-even point (minimum digitization needed to avoid loss)

It also shows graphs to make the results easier to understand.

---

## Inputs required

The user provides:

* Patients per day
* Time per patient (paper vs EMR)
* Error rate
* Cost per error
* Monthly paper cost
* EMR setup cost
* Monthly maintenance cost
* Digitization level

---

## How the calculations work (simple idea)

The tool calculates savings from 3 main areas:

1. Time saved
2. Errors reduced
3. Paper usage reduced

These are combined to get total benefit.

Then:

* ROI = how much profit you get compared to cost
* Payback = how fast you recover your investment
* Break-even = minimum level where you stop losing money

---

## Outputs

The dashboard shows:

* ROI percentage
* Payback period
* Monthly savings
* Break-even digitization
* ROI vs digitization graph
* Breakdown of where savings come from

---

## Assumptions

* 26 working days per month
* Staff cost per hour is fixed
* Savings increase linearly with digitization
* No long delay in adoption

---

## Limitations

* Uses estimated values (not real hospital data)
* Doesn’t consider human resistance to change
* Assumes everything improves smoothly

---

## Testing done

I tested the model with different scenarios:

* 0% digitization → no savings
* 100% digitization → maximum savings
* High error → higher ROI
* No time difference → no time benefit
* High setup cost → slower recovery

---

## Future improvements

* Use real hospital data
* Add ML to predict ROI
* Compare different scenarios
* Suggest best digitization level automatically

---

## Final note

This tool is meant to support decision-making, not give exact predictions. It helps hospital owners understand whether EMR adoption makes sense financially.
