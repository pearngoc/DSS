# Chapter 2_Extra Topic

Source: `Chapter 2_Extra Topic.pdf`  
Slides: 24

## Slide 1

**EXTRA TOPIC:**

**DATA PRE-PROCESSING**

> This slide also contains a figure that is not represented as text.

## Slide 2 — Outline

- Data Cleaning
  - Missing Data
  - Outliers
- Data Transformation
> This slide also contains a figure that is not represented as text.

## Slide 3 — Missing Data

**Address absences (random or not) in the dataset**

- **Step #1: Detect missing values**
- **Step #2: Select a handling method**
- **Step #3: Apply the selected handling method**
- Imputation by appropriate values (mean imputation, etc.)
- Interpolation with a constant
- Deletion
- Ignorance

## Slide 4 — Criteria for Handling Methods

- The nature of the missingness is important.
- Different contexts and types of analysis might require different treatments for missing values.
- Some default handling methods:
  - Missing values will be treated as 0 when summing data.
  - The sum will be equal to NaN, if all values are missing.
  - cumsum() and cumprod() methods ignore missing values but preserve them in the resulting arrays.
  - Missing values in GroupBy methods are excluded (like R).
  - In some descriptive statistics methods, the skipna option is to used if missing data should be excluded, i.e., this value is set to True by default (unlike R).

## Slide 5 — Outliers

Manage **abnormal values (outliers)** which **can lead** to **undesired or less robust outcomes**.

- **Step #1: Detect outliers**
- Visualization
- Statistical methods (IQR, Z-score)
- **Step #2: Manage outliers**
- Remove outliers
- Replace outliers by reasonable values
- Retain (do nothing)

Link: https://www.scribbr.com/statistics/outliers/

## Slide 6 — Outliers

- The nature and reason for outliers is important in determining appropriate handling methods.
  - Error outliers: Result from data entry errors, processing errors, measurement errors, or data corruption.
  - Valid (or true) outliers: Natural variation in a sample.
- Outliers that result from errors should be:
  - Removed
  - Replaced by reasonable values (cf. Data Transformation)
- Valid (or true) outliers should be:
  - Removed
  - Retained
  - Replaced by reasonable values (cf. Data Transformation)

Link: https://www.scribbr.com/statistics/outliers/

## Slide 7 — Outlier Visualization

**Scatter plot Histogram**

**Boxplot**

> This slide also contains a figure that is not represented as text.

## Slide 8 — IQR Method

- Steps for the IQR method:
  - Sort your data from low to high
  - Identify the values for Q1, Q2 (or the median), and Q3.
  - Calculate the IQR = Q3 – Q1
  - Calculate the upper fence (UF) = Q3 + (1.5 * IQR)
  - Calculate the lower fence (LF) = Q1 – (1.5 * IQR)
  - All values that fall outside the calculated fences (out of the range [LF, UF]) will be considered as outliers.

## Slide 9 — Z-Score Method

- Steps for the Z-Score Method
  - Convert extreme data points into z-scores.
  - All values that have a high enough or low enough z-scores (out of the range [-3𝜎, 3𝜎]) will be considered as outliers.

**Outliers**

## Slide 10 — Outline

- Data Cleaning
- Data Transformation
  - Standardization
  - Normalization
> This slide also contains a figure that is not represented as text.

## Slide 11 — Data Standardization

**Convert data to a common format or structure**

- **Step #1: Select standard formats**
- **Step #2: Define transform methods**
- **Step #3: Apply defined methods to convert data**
- Formatting q Encoding (Categorical data)
- Patterns q Data type convert
- Domain Values q Etc.

## Slide 12 — Examples of Standardization

**Employee Data Sample**

> This slide also contains a figure that is not represented as text.

## Slide 13 — Examples of Standardization

**String Formatting**

> This slide also contains a figure that is not represented as text.

## Slide 14 — Examples of Standardization

**Date Formatting**

> This slide also contains a figure that is not represented as text.

## Slide 15 — Examples of Standardization

**Domain Value Standardization**

> This slide also contains a figure that is not represented as text.

## Slide 16 — Examples of Standardization

**Ordinal (Orderable)**

**Encoding Categorical Data**

**Nominal (Unordered)**

Link: https://pbpython.com/categorical-encoding.html

Dataset: https://archive.ics.uci.edu/dataset

/10/automobile

(UCI Machine Learning

Repository)

## Slide 17 — Examples of Standardization

**Ordinal (Orderable)**

**Encoding Categorical Data**

**Nominal (Unordered)**

**#1 Find and replace**

Link: https://pbpython.com/categorical-encoding.html

Dataset: https://archive.ics.uci.edu/dataset/10/automobile

(UCI Machine Learning Repository)

## Slide 18 — Examples of Standardization

**Ordinal (Orderable)**

**Encoding Categorical Data**

**Nominal (Unordered)**

**#2 Label Encoding (Ordinal encoding for ordinal data)**

- Converting each value in a column to a number.
  - convertible -> 0; hardtop -> 1; hatchback -> 2; sedan -> 3; wagon -> 4
- Easy, simple, and adaptable for various data types
- Numeric values can be misinterpreted.
- Assigned values might not accurately represent real-life data nature.

Link: https://pbpython.com/categorical-encoding.html

Dataset: https://archive.ics.uci.edu/dataset/10/automobile

(UCI Machine Learning Repository)

## Slide 19 — Examples of Standardization

**Ordinal (Orderable)**

**Encoding Categorical Data**

**Nominal (Unordered)**

**#3 One Hot Encoding**

- Convert each category value into a new column
- Assigns 1 or 0 (True/False) value to the new column
- Not weighting a value improperly
- Adaptable for various data types
- May have to add too many columns

Link: https://pbpython.com/categorical-encoding.html

Dataset: https://archive.ics.uci.edu/dataset/10/automobile

(UCI Machine Learning Repository)

## Slide 20 — Examples of Standardization

**Ordinal (Orderable)**

**Encoding Categorical Data**

**Nominal (Unordered)**

**#4 Customer Binary Coding (Combining Label and One Hot Coding)**

**Dominant**

Link: https://pbpython.com/categorical-encoding.html

Dataset: https://archive.ics.uci.edu/dataset/10/automobile

(UCI Machine Learning Repository)

## Slide 21 — Data Normalization

**Scale numeric data to fall within specified range**

- **Step #1: Determine desired scales**
- **Step #2: Apply scaling methods**
- Decimal scaling
- Min-max scaling
- Z-score scaling
- Robust scaling
- Etc.

## Slide 22 — Data Normalization

- **Decimal Scaling**: Scale data so that it can fall within a specified range.
- **Min-max Scaling:** The scaled data usually falls in the

[0,1] range.

- **Z-score Normalization**: Scale the data based on mean (µ) and standard deviation (σ).
- **Robust Scaling**: Scale the data based on median and IQR à It’s suitable for the data with many “true” outliers that should not be removed.
- Etc.

## Slide 23 — Examples of Normalization

**Min-Max Scaling**

> This slide also contains a figure that is not represented as text.

## Slide 24 — Examples of Normalization

**Z-Score Normalization**

> This slide also contains a figure that is not represented as text.
