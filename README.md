
# 🤖 Advanced AutoML CSV Evaluator

An intelligent, end-to-end machine learning automation tool that handles **any kind of CSV data** with automatic cleaning, preprocessing, model selection, and evaluation.

## ✨ Key Features

### 🧹 Automatic Data Cleaning
- **Duplicate removal** - Identifies and removes duplicate rows
- **Missing value handling** - Fills categorical with mode, numerical with median
- **Outlier detection** - Uses IQR method to clip outliers in numerical columns
- **Infinite value handling** - Replaces inf/-inf with median values
- **Data type detection** - Automatically identifies categorical vs numerical columns

### 🤖 Smart Problem Detection
- **Automatic Classification Detection** - Detects categorical targets & discrete values (< 20 unique)
- **Automatic Regression Detection** - Identifies continuous numerical targets
- **Adaptive Model Selection** - Chooses appropriate models based on problem type

### 📊 Comprehensive Model Library

**Classification Models:**
- Logistic Regression
- Random Forest Classifier
- Gradient Boosting Classifier
- Support Vector Machines (SVM)
- K-Nearest Neighbors
- Decision Tree Classifier
- Naive Bayes

**Regression Models:**
- Linear Regression
- Ridge Regression
- Lasso Regression
- Random Forest Regressor
- Gradient Boosting Regressor
- Support Vector Regression (SVR)
- K-Nearest Neighbors Regressor
- Decision Tree Regressor

### 📈 Advanced Evaluation
- **Cross-Validation (5-fold)** - Robust model evaluation with CV scores
- **Multiple Metrics**
  - Classification: Accuracy, Precision, Recall, F1-Score, CV metrics
  - Regression: R² Score, MAE, MSE, RMSE, CV metrics
- **Visual Comparisons** - Interactive Plotly charts comparing model performance
- **Best Model Selection** - Automatically identifies and highlights the best performing model

### 💾 Export & Reporting
- Download results as CSV
- Detailed summary reports with dataset information
- Feature and target variable analysis
- Actionable recommendations

## 🚀 Quick Start

### Installation

```bash
pip install streamlit pandas numpy scikit-learn plotly
```

### Running the App

```bash
streamlit run main.py
```

The app will open at `http://localhost:8501`

## 📋 How to Use

1. **Upload CSV** - Use the sidebar file uploader to select your CSV file
2. **Preview Data** - View dataset information (rows, columns, missing values, data types)
3. **Select Target** - Choose the column you want to predict
4. **Automatic Detection** - The app automatically detects if it's classification or regression
5. **Run AutoML** - Click "🚀 Run AutoML" to start training
6. **View Results** - See model comparison table and performance visualizations
7. **Download** - Export results as CSV for further analysis

## 📊 Sample Datasets

Two sample datasets are included:

- `iris.csv` - Classification (predicting flower species)
- `air.csv` - Regression (predicting air quality metrics)

## 🔧 What Happens Under the Hood

```
Upload CSV
    ↓
🧹 Auto Clean Data (duplicates, missing values, outliers)
    ↓
🔍 Detect Problem Type (Classification vs Regression)
    ↓
⚙️ Build Preprocessing Pipeline
    • Impute numerical features (median)
    • Impute categorical features (mode)
    • One-hot encode categorical variables
    • Scale numerical features
    ↓
🤖 Train Multiple Models (7-8 models depending on task type)
    • 5-fold Cross-Validation for each model
    • Full training set fitting
    ↓
📊 Evaluate on Test Set
    • Calculate metrics (Accuracy/Precision/Recall/F1 for classification)
    • Calculate metrics (R²/MAE/MSE/RMSE for regression)
    ↓
🏆 Select Best Model & Display Results
    • Model comparison table
    • Performance visualization
    • Detailed report generation
    ↓
💾 Export Results (CSV download available)
```

## 📝 Example Workflow

**Classification Example (Iris Dataset):**
- Upload: `iris.csv`
- Target: `species`
- Auto-detected: Classification
- Models trained: 7
- Best model: Random Forest (98.3% accuracy)
- Metrics: Accuracy, Precision, Recall, F1-Score

**Regression Example (Air Quality Dataset):**
- Upload: `air.csv`
- Target: `AQI_value`
- Auto-detected: Regression
- Models trained: 8
- Best model: Gradient Boosting (R² = 0.92)
- Metrics: R², MAE, MSE, RMSE

## 🛡️ Error Handling

The app gracefully handles:
- Missing values in any column
- Mixed data types (strings, numbers, booleans)
- Datasets with too few or too many samples
- Categorical variables with high cardinality
- Models that fail to train (skips with warning)
- Infinite and NaN values

## 📦 Dependencies

```
streamlit>=1.28.0
pandas>=1.5.0
numpy>=1.23.0
scikit-learn>=1.3.0
plotly>=5.14.0
```

## 🎯 Use Cases

- **Quick model prototyping** - Test multiple algorithms rapidly
- **Data exploration** - Understand which models work best for your data
- **Baseline establishment** - Get baseline results before fine-tuning
- **Non-technical users** - No ML expertise needed
- **Competition prep** - Quick EDA and model benchmarking
- **Production POC** - Validate model viability quickly

## 🔮 Advanced Features

- Automatic problem type detection
- Cross-validation for robust evaluation
- Missing data handling (statistical imputation)
- Categorical encoding (one-hot encoding)
- Feature scaling (StandardScaler)
- Outlier detection and handling
- Parallel model training (n_jobs=-1)
- Interactive visualizations

## 📄 Output Format

The CSV results file contains:
- Model name
- All performance metrics
- Cross-validation mean and std
- Easy comparison across models

Example:
```
Model,Accuracy,Precision,Recall,F1 Score,CV Mean,CV Std
Logistic Regression,0.9667,0.9667,0.9667,0.9667,0.9667,0.0211
Random Forest,0.9833,0.9833,0.9833,0.9833,0.9833,0.0178
...
```

## ⚠️ Limitations

- Currently optimized for tabular CSV data
- Time series and sequential data need preprocessing
- Image and text data not supported (use specialized models)
- Very large datasets (>100k rows) may be slow
- Categorical columns with >1000 unique values may cause memory issues

## 🚀 Future Enhancements

- Hyperparameter tuning with Bayesian optimization
- Feature importance analysis
- SHAP value explanations
- Time series specialized models
- Ensemble model creation
- Model persistence and loading
- Prediction on new data
- Automated feature engineering
- Class imbalance handling
- GPU support for large datasets

## 📞 Support

For issues or questions, please open an issue in the repository.

---

**Made with ❤️ for making AutoML accessible to everyone!**
