
# 🤖 Advanced AutoML CSV Evaluator

[![GitHub](https://img.shields.io/badge/GitHub-Pujan--Dev-black?style=flat-square&logo=github)](https://github.com/Pujan-Dev)
[![Portfolio](https://img.shields.io/badge/Portfolio-neupanepujan.com.np-blue?style=flat-square&logo=globe)](https://neupanepujan.com.np)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)](https://www.python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red?style=flat-square&logo=streamlit)](https://streamlit.io)

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

### Prerequisites
- Python 3.8 or higher
- pip or conda package manager

### Installation (Local)

**Option 1: Using pip**
```bash
# Clone the repository
git clone https://github.com/Pujan-Dev/AutoML.git
cd AutoML

# Install dependencies
pip install -r requirements.txt
```

**Option 2: Using conda**
```bash
conda create -n automl python=3.9
conda activate automl
pip install -r requirements.txt
```

### Running the App

```bash
streamlit run main.py
```

The app will automatically open at `http://localhost:8501` in your browser.

### Running with Docker

```bash
# Build the Docker image
docker build -t automl:latest .

# Run the container
docker run -p 8501:8501 automl:latest
```

Then visit `http://localhost:8501` in your browser.

## 📋 How to Use

### Step-by-Step Guide

1. **Upload CSV** 
   - Use the sidebar file uploader to select your CSV file
   - Supports any tabular CSV format

2. **Preview Data** 
   - View dataset information (rows, columns, missing values, data types)
   - Expand the "Dataset Preview" section to see sample rows

3. **Configure Data Options** 
   - For large datasets (>1000 rows), choose to sample or select columns
   - Remove unnecessary columns from analysis

4. **Select Target Column** 
   - Choose the column you want to predict
   - The app automatically detects classification vs regression

5. **Run AutoML** 
   - Click the "🚀 Run AutoML" button to start training
   - Watch the progress as models are trained sequentially

6. **Review Results** 
   - See model comparison table with all metrics
   - View performance visualization chart
   - Identify the best model (highlighted with 🏆)

7. **Export Results** 
   - Download detailed results as CSV
   - View comprehensive summary report with recommendations

## 📊 Sample Datasets

sample datasets are :

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

All dependencies are listed in `requirements.txt`:

```
streamlit>=1.28.0
pandas>=1.5.0
numpy>=1.23.0
scikit-learn>=1.3.0
plotly>=5.14.0
```

For development, install with:
```bash
pip install -r requirements.txt
```

### Version Compatibility

- **Python**: 3.8, 3.9, 3.10, 3.11
- **Streamlit**: 1.28.0+
- **scikit-learn**: 1.3.0+
- **pandas**: 1.5.0+
- **numpy**: 1.23.0+
- **plotly**: 5.14.0+

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

## 🎨 UI Features

- **Light & Dark Mode** - Toggle between light and dark themes in the sidebar under "Appearance"
- **Responsive Design** - Works seamlessly on desktop, tablet, and mobile browsers
- **Interactive Charts** - Hover over visualizations for detailed metrics
- **Real-time Updates** - Live progress indicators during model training
- **Exportable Results** - Download analysis results in CSV format

## ⚙️ Configuration

### Theme Selection
In the sidebar under "Appearance", you can toggle between:
- **Light Mode** - Clean, bright interface for daytime use
- **Dark Mode** - Easy on the eyes for extended sessions

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

## 📞 Support & Contact

For issues or questions, please open an issue in the repository.

---

### 🔗 Links

- **GitHub**: [github.com/Pujan-Dev](https://github.com/Pujan-Dev)
- **Portfolio**: [neupanepujan.com.np](https://neupanepujan.com.np)

---

**Made with ❤️ for making AutoML accessible to everyone!**
