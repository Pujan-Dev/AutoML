# 🚀 Quick Setup Guide

## Installation

### Step 1: Install Dependencies

```bash
pip install streamlit pandas numpy scikit-learn plotly
```

### Step 2: Run the Application

```bash
streamlit run main.py
```

The app will automatically open in your browser at `http://localhost:8501`

---

## What You Get

✅ **Fully Automated ML Pipeline**
- Automatic data cleaning & preprocessing
- Smart problem type detection (Classification vs Regression)
- 7-8 different ML models trained automatically
- Cross-validation for robust evaluation
- Beautiful interactive visualizations

✅ **No Machine Learning Knowledge Required**
- Just upload your CSV file
- Select your target column
- Click "Run AutoML"
- Get comprehensive results

✅ **Professional Output**
- Model comparison table with all metrics
- Performance visualizations
- Detailed summary reports
- CSV export of results

---

## Testing with Sample Data

The workspace includes two sample CSV files:

1. **iris.csv** - Classification example
   - Target: `species`
   - Task: Predict iris flower species
   - Expected best model: Random Forest (98%+ accuracy)

2. **air.csv** - Regression example
   - Target: `AQI_value` (or similar)
   - Task: Predict air quality index
   - Expected best model: Gradient Boosting (R² > 0.9)

### Try it now:
1. Run `streamlit run main.py`
2. In the sidebar, upload `iris.csv`
3. Select `species` as target column
4. Click "🚀 Run AutoML"
5. See the magic happen! ✨

---

## Data Cleaning Features

The app automatically handles:

| Issue | Solution |
|-------|----------|
| Duplicate rows | Removed |
| Missing categorical values | Filled with mode |
| Missing numerical values | Filled with median |
| Infinite values | Replaced with median |
| Outliers | Clipped using IQR method |
| Mixed data types | Proper encoding & scaling |
| Empty columns | Skipped |

---

## Models Included

### For Classification:
- Logistic Regression
- Random Forest
- Gradient Boosting
- SVM
- K-Nearest Neighbors
- Decision Tree
- Naive Bayes

### For Regression:
- Linear Regression
- Ridge Regression
- Lasso Regression
- Random Forest
- Gradient Boosting
- SVR
- K-Nearest Neighbors
- Decision Tree

---

## Metrics Explained

### Classification Metrics:
- **Accuracy**: Overall correctness
- **Precision**: Correct positive predictions
- **Recall**: How many true positives found
- **F1-Score**: Balance between precision & recall
- **CV Mean/Std**: Cross-validation performance

### Regression Metrics:
- **R² Score**: Proportion of variance explained (0-1, higher is better)
- **MAE**: Mean Absolute Error
- **MSE**: Mean Squared Error
- **RMSE**: Root Mean Squared Error
- **CV Mean/Std**: Cross-validation performance

---

## Troubleshooting

**Problem**: `ModuleNotFoundError: No module named 'plotly'`
```bash
pip install plotly
```

**Problem**: `ModuleNotFoundError: No module named 'sklearn'`
```bash
pip install scikit-learn
```

**Problem**: Port 8501 already in use
```bash
streamlit run main.py --server.port 8502
```

**Problem**: Dataset too small
- Need at least 10 samples
- More samples = better models

**Problem**: All models showing errors
- Check if CSV has the target column
- Check for special characters in column names
- Try with sample CSV files first

---

## Advanced Usage

### Supported File Format
- CSV files only
- Must have target column
- No NaN/None in column names

### Data Size Recommendations
- Minimum: 10 samples
- Optimal: 100-10,000 samples
- Maximum: Should work, but may be slow

### Column Types
- **Numerical**: int, float
- **Categorical**: text, strings, objects
- **Binary**: Yes/No, 0/1, True/False

---

## What Happens Behind the Scenes

```
Your CSV File
     ↓
🧹 Clean Data
   • Remove duplicates
   • Handle missing values
   • Detect/handle outliers
     ↓
🔍 Detect Problem Type
   • Classification or Regression?
     ↓
⚙️ Preprocess Features
   • Encode categorical variables
   • Scale numerical variables
   • Handle missing values
     ↓
🤖 Train 7-8 Models
   • 5-fold Cross-Validation
   • Full training on 80% data
     ↓
📊 Evaluate on 20% Test Data
   • Calculate performance metrics
   • Track cross-validation scores
     ↓
🏆 Find Best Model
   • Select model with highest score
   • Generate comprehensive report
     ↓
💾 Display & Export Results
   • Beautiful visualizations
   • CSV download
   • Detailed recommendations
```

---

## Performance Tips

For faster results:
- Use smaller datasets (< 1000 rows)
- Have fewer features (< 100 columns)
- Use CSV format (fastest to read)

For better models:
- Use larger datasets (> 100 rows)
- Include relevant features
- Ensure good data quality

---

## Next Steps

1. ✅ Run the app on sample data
2. ✅ Upload your own CSV file
3. ✅ Try different target columns
4. ✅ Download and analyze results
5. ✅ Share with team members

---

## Support

If you encounter any issues:
1. Check the error message in the Streamlit UI
2. Review this setup guide
3. Verify your CSV format
4. Try with sample data first

---

**Happy ML experimentation! 🚀**
