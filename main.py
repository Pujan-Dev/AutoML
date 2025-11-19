
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold, KFold
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression, LinearRegression, Ridge, Lasso
from sklearn.svm import SVC, SVR
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, GradientBoostingClassifier, GradientBoostingRegressor
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score, 
                             r2_score, mean_squared_error, mean_absolute_error, roc_auc_score,
                             confusion_matrix, classification_report)
import plotly.express as px
import plotly.graph_objects as go
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="AutoML CSV Evaluator", layout="wide")
st.title("🤖 Advanced AutoML CSV Evaluator")
st.markdown("---")

# ============================================
# HELPER FUNCTIONS
# ============================================

@st.cache_data
def load_data(file):
    """Load CSV file safely"""
    try:
        return pd.read_csv(file)
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

def detect_problem_type(y):
    """Detect if it's classification or regression"""
    if y.dtype == "object" or y.dtype == "category":
        return "classification"
    unique_vals = y.nunique()
    if unique_vals <= 20 and all(isinstance(val, (int, np.integer)) for val in y.unique()):
        return "classification"
    return "regression"

def auto_clean_data(df, target_col):
    """Automatic data cleaning pipeline"""
    st.info("🧹 Starting automatic data cleaning...")
    
    X = df.drop(columns=[target_col]).copy()
    y = df[target_col].copy()
    
    # Remove rows with missing target FIRST
    y_missing_initial = y.isnull().sum()
    if y_missing_initial > 0:
        valid_idx = ~y.isnull()
        X = X[valid_idx]
        y = y[valid_idx]
        st.success(f"✓ Removed {y_missing_initial} rows with missing target")
    
    # Remove duplicates
    initial_rows = len(X)
    X_dedup = X.drop_duplicates()
    y_dedup = y[X_dedup.index]
    X = X_dedup
    y = y_dedup
    st.success(f"✓ Removed duplicates: {initial_rows - len(X)} rows removed")
    
    # Detect column types
    categorical_cols = X.select_dtypes(include=["object", "category"]).columns.tolist()
    numerical_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()
    
    # Handle missing values BEFORE any other processing
    missing_before = X.isnull().sum().sum()
    
    # Fill missing categorical with mode
    for col in categorical_cols:
        if X[col].isnull().any():
            mode_val = X[col].mode()
            X[col].fillna(mode_val[0] if len(mode_val) > 0 else "Unknown", inplace=True)
    
    # Fill missing numerical with median
    for col in numerical_cols:
        if X[col].isnull().any():
            median_val = X[col].median()
            # If median is NaN (all values are NaN), use 0
            if pd.isna(median_val):
                X[col].fillna(0, inplace=True)
            else:
                X[col].fillna(median_val, inplace=True)
    
    missing_after = X.isnull().sum().sum()
    st.success(f"✓ Handled missing values: {missing_before} → {missing_after}")
    
    # Handle infinite values
    for col in numerical_cols:
        if X[col].dtype in ['float64', 'float32']:
            # Replace infinities with max/min finite values
            finite_vals = X[col][np.isfinite(X[col])]
            if len(finite_vals) > 0:
                max_val = finite_vals.max()
                min_val = finite_vals.min()
                X[col] = X[col].replace([np.inf], max_val)
                X[col] = X[col].replace([-np.inf], min_val)
                # Fill any remaining NaN
                X[col].fillna(X[col].median(), inplace=True)
            else:
                X[col].fillna(0, inplace=True)
    
    # Handle outliers (IQR method) for numerical columns
    outlier_count = 0
    for col in numerical_cols:
        Q1 = X[col].quantile(0.25)
        Q3 = X[col].quantile(0.75)
        IQR = Q3 - Q1
        if IQR > 0:  # Only apply if there's variance
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = ((X[col] < lower_bound) | (X[col] > upper_bound)).sum()
            if outliers > 0:
                X[col] = X[col].clip(lower_bound, upper_bound)
                outlier_count += outliers
    
    if outlier_count > 0:
        st.success(f"✓ Handled {outlier_count} outliers across numerical columns")
    
    # Final validation - ensure no NaN or infinite values remain
    nan_count = X.isnull().sum().sum()
    if nan_count > 0:
        st.warning(f"⚠️ Filling {nan_count} remaining NaN values with column median/mode")
        for col in X.columns:
            if X[col].isnull().any():
                if col in numerical_cols:
                    X[col].fillna(X[col].median(), inplace=True)
                else:
                    X[col].fillna("Unknown", inplace=True)
    
    # Ensure no infinite values
    for col in numerical_cols:
        inf_mask = np.isinf(X[col])
        if inf_mask.any():
            X.loc[inf_mask, col] = 0
    
    # Convert data types
    for col in categorical_cols:
        X[col] = X[col].astype(str)
    
    st.success(f"✓ Data cleaning complete! Final dataset: {X.shape[0]} rows × {X.shape[1]} columns")
    return X, y, categorical_cols, numerical_cols

# ============================================
# 1. Upload CSV
# ============================================
st.sidebar.header("📁 Data Input")
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = load_data(uploaded_file)
    
    if df is not None:
        # Display data info
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Rows", df.shape[0])
        with col2:
            st.metric("Total Columns", df.shape[1])
        with col3:
            st.metric("Missing Values", df.isnull().sum().sum())
        
        with st.expander("📊 Dataset Preview"):
            st.dataframe(df.head(10), use_container_width=True)
            st.write("**Data Types:**", df.dtypes.to_dict())
        
        # ============================================
        # 2. Data Sampling for Large Datasets
        # ============================================
        st.sidebar.header("⚙️ Data Options")
        
        # Check if dataset is large
        if df.shape[0] > 1000:
            st.sidebar.info(f"📊 Large dataset detected ({df.shape[0]} rows)")
            
            sample_choice = st.sidebar.radio(
                "How to handle large data?",
                ["Use Full Data", "Sample Data", "Select Columns Only"],
                help="Sampling or selecting columns can speed up processing"
            )
            
            if sample_choice == "Sample Data":
                st.sidebar.subheader("📉 Data Sampling")
                sample_size = st.sidebar.slider(
                    "Select number of rows to use",
                    min_value=100,
                    max_value=df.shape[0],
                    value=min(5000, df.shape[0]),
                    step=100,
                    help="Larger samples = slower processing but better models"
                )
                df_working = df.sample(n=sample_size, random_state=42).reset_index(drop=True)
                st.sidebar.success(f"✓ Using {sample_size} rows ({100*sample_size/df.shape[0]:.1f}% of data)")
            else:
                df_working = df.copy()
        else:
            df_working = df.copy()
        
        # ============================================
        # 3. Column Selection
        # ============================================
        st.sidebar.subheader("📋 Column Selection")
        
        # Show current columns
        with st.sidebar.expander("View/Select Columns"):
            st.write(f"**Current columns ({len(df_working.columns)}):**")
            
            # Option to remove specific columns
            columns_to_remove = st.multiselect(
                "Remove columns (optional):",
                options=df_working.columns,
                help="Select columns you want to exclude from analysis"
            )
            
            if columns_to_remove:
                df_working = df_working.drop(columns=columns_to_remove)
                st.success(f"✓ Removed {len(columns_to_remove)} columns")
                st.write(f"**Remaining columns ({len(df_working.columns)}):**")
                st.write(", ".join(df_working.columns))
        
        # ============================================
        # 4. Select target column
        # ============================================
        st.sidebar.header("🎯 Target Configuration")
        target_column = st.sidebar.selectbox("Select the target column", df_working.columns)
        
        # Problem type detection
        problem_type = detect_problem_type(df_working[target_column])
        st.sidebar.success(f"📌 Problem Type: **{problem_type.upper()}**")
        
        if st.sidebar.button("🚀 Run AutoML", key="automl_button"):
            # ============================================
            # 5. Data Cleaning
            # ============================================
            st.header("📋 Step 1: Data Cleaning & Preprocessing")
            
            # Show what we're working with
            st.info(f"📊 Processing: {df_working.shape[0]} rows × {df_working.shape[1]} columns")
            
            X, y, categorical_cols, numerical_cols = auto_clean_data(df_working, target_column)
            
            # ============================================
            # 4. Check dataset size
            # ============================================
            if X.shape[0] < 10:
                st.error("❌ Dataset too small! Need at least 10 samples.")
                st.stop()
            
            if X.shape[0] > 10000:
                st.warning("⚠️ Dataset is large. Processing may take time...")
            
            # ============================================
            # 5. Build preprocessing pipeline
            # ============================================
            st.header("🔧 Step 2: Model Training")
            st.info("Building and training models with cross-validation...")
            
            # Enhanced preprocessing with better error handling
            numeric_transformer = None
            categorical_transformer = None
            
            if numerical_cols:
                numeric_transformer = Pipeline([
                    ('imputer', SimpleImputer(strategy='median', add_indicator=False)),
                    ('scaler', StandardScaler())
                ])
            
            if categorical_cols:
                categorical_transformer = Pipeline([
                    ('imputer', SimpleImputer(strategy='most_frequent', fill_value='Unknown')),
                    ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False, max_categories=100))
                ])
            
            transformers = []
            if numeric_transformer:
                transformers.append(('num', numeric_transformer, numerical_cols))
            if categorical_transformer:
                transformers.append(('cat', categorical_transformer, categorical_cols))
            
            preprocessor = ColumnTransformer(transformers, remainder='drop', verbose=False) if transformers else None
            
            # ============================================
            # 6. Define models based on problem type
            # ============================================
            if problem_type == "classification":
                models = {
                    "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
                    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1),
                    "Gradient Boosting": GradientBoostingClassifier(random_state=42),
                    "SVM": SVC(probability=True, random_state=42),
                    "K-Nearest Neighbors": KNeighborsClassifier(n_neighbors=5),
                    "Decision Tree": DecisionTreeClassifier(random_state=42),
                    "Naive Bayes": GaussianNB()
                }
                cv_strategy = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
            else:
                models = {
                    "Linear Regression": LinearRegression(),
                    "Ridge Regression": Ridge(random_state=42),
                    "Lasso Regression": Lasso(random_state=42),
                    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1),
                    "Gradient Boosting": GradientBoostingRegressor(random_state=42),
                    "SVR": SVR(),
                    "K-Nearest Neighbors": KNeighborsRegressor(n_neighbors=5),
                    "Decision Tree": DecisionTreeRegressor(random_state=42)
                }
                cv_strategy = KFold(n_splits=5, shuffle=True, random_state=42)
            
            # ============================================
            # 7. Split data
            # ============================================
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42, 
                stratify=y if problem_type == "classification" else None
            )
            
            st.success(f"✓ Train set: {X_train.shape[0]} | Test set: {X_test.shape[0]}")
            
            # ============================================
            # 8. Train and evaluate models
            # ============================================
            results = {}
            best_model_name = None
            best_score = -np.inf
            
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for idx, (name, model) in enumerate(models.items()):
                status_text.text(f"Training {name}...")
                progress = (idx + 1) / len(models)
                progress_bar.progress(progress)
                
                try:
                    # Build pipeline
                    if preprocessor:
                        pipeline = Pipeline([
                            ('preprocessor', preprocessor),
                            ('model', model)
                        ])
                    else:
                        pipeline = model
                    
                    # Try cross-validation with error handling
                    try:
                        if problem_type == "classification":
                            cv_scores = cross_val_score(pipeline, X_train, y_train, cv=cv_strategy, scoring='f1_weighted', n_jobs=-1, error_score=np.nan)
                        else:
                            cv_scores = cross_val_score(pipeline, X_train, y_train, cv=cv_strategy, scoring='r2', n_jobs=-1, error_score=np.nan)
                        
                        # If all CV scores are NaN, try fitting directly
                        if np.all(np.isnan(cv_scores)):
                            st.warning(f"⚠️ {name}: Cross-validation failed, using direct fit instead")
                            pipeline.fit(X_train, y_train)
                            cv_scores = np.array([0.0])  # Placeholder
                    except Exception as cv_err:
                        st.warning(f"⚠️ {name}: Cross-validation failed, using direct fit: {str(cv_err)[:100]}")
                        pipeline.fit(X_train, y_train)
                        cv_scores = np.array([0.0])  # Placeholder
                    
                    # Train on full training set (if not already done)
                    try:
                        pipeline.fit(X_train, y_train)
                    except Exception as fit_err:
                        # Try to fit just the model without preprocessing
                        if preprocessor:
                            X_train_processed = preprocessor.fit_transform(X_train)
                            model.fit(X_train_processed, y_train)
                        else:
                            raise fit_err
                    
                    # Make predictions
                    try:
                        y_pred = pipeline.predict(X_test)
                    except Exception as pred_err:
                        if preprocessor:
                            X_test_processed = preprocessor.transform(X_test)
                            y_pred = model.predict(X_test_processed)
                        else:
                            raise pred_err
                    
                    # Calculate metrics
                    if problem_type == "classification":
                        accuracy = accuracy_score(y_test, y_pred)
                        precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
                        recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
                        f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)
                        
                        results[name] = {
                            "Accuracy": accuracy,
                            "Precision": precision,
                            "Recall": recall,
                            "F1 Score": f1,
                            "CV Mean": cv_scores.mean(),
                            "CV Std": cv_scores.std()
                        }
                        
                        if accuracy > best_score:
                            best_score = accuracy
                            best_model_name = name
                    else:
                        r2 = r2_score(y_test, y_pred)
                        mse = mean_squared_error(y_test, y_pred)
                        rmse = np.sqrt(mse)
                        mae = mean_absolute_error(y_test, y_pred)
                        
                        results[name] = {
                            "R² Score": r2,
                            "MAE": mae,
                            "MSE": mse,
                            "RMSE": rmse,
                            "CV Mean": cv_scores.mean(),
                            "CV Std": cv_scores.std()
                        }
                        
                        if r2 > best_score:
                            best_score = r2
                            best_model_name = name
                
                except Exception as e:
                    results[name] = {"Error": str(e)}
                    st.warning(f"⚠️ {name} failed: {str(e)}")
            
            progress_bar.empty()
            status_text.empty()
            
            # ============================================
            # 9. Display Results
            # ============================================
            st.header("📊 Step 3: Results & Analysis")
            
            results_df = pd.DataFrame(results).T
            results_df = results_df.round(4)
            
            col1, col2 = st.columns([3, 1])
            with col1:
                st.subheader("Model Comparison")
                st.dataframe(results_df, use_container_width=True)
            with col2:
                st.metric("🏆 Best Model", best_model_name or "N/A", best_score)
            
            # Visualization
            if "Error" not in results_df.columns:
                metric_col = "Accuracy" if problem_type == "classification" else "R² Score"
                if metric_col in results_df.columns:
                    fig = px.bar(
                        x=results_df.index,
                        y=results_df[metric_col],
                        labels={metric_col: "Score", "index": "Model"},
                        title=f"Model {metric_col} Comparison",
                        color=results_df[metric_col],
                        color_continuous_scale="Viridis"
                    )
                    fig.update_layout(height=400, showlegend=False)
                    st.plotly_chart(fig, use_container_width=True)
            
            # ============================================
            # 10. Download Results
            # ============================================
            st.header("💾 Step 4: Export Results")
            
            csv = results_df.to_csv()
            st.download_button(
                label="📥 Download Results as CSV",
                data=csv,
                file_name='automl_results.csv',
                mime='text/csv'
            )
            
            # Summary report
            with st.expander("📄 Detailed Summary Report", expanded=True):
                report = f"""
                # AutoML Analysis Report
                
                ## Dataset Information
                - **Original Dataset**: {df.shape[0]} rows × {df.shape[1]} columns
                - **Working Dataset**: {df_working.shape[0]} rows × {df_working.shape[1]} columns
                - **Samples After Cleaning**: {len(y)}
                - **Features Used**: {X.shape[1]}
                - **Problem Type**: {problem_type.upper()}
                - **Target Variable**: {target_column}
                
                ## Data Processing Summary
                - **Categorical Features**: {len(categorical_cols)} {categorical_cols if categorical_cols else '(None)'}
                - **Numerical Features**: {len(numerical_cols)} {numerical_cols if numerical_cols else '(None)'}
                - **Training Set**: {len(X_train)} samples (80%)
                - **Test Set**: {len(X_test)} samples (20%)
                
                ## Model Performance
                - **Best Model**: {best_model_name}
                - **Best Score**: {best_score:.4f}
                - **Models Evaluated**: {len(results)}
                
                ## Recommendations
                """
                
                if best_model_name:
                    report += f"✓ Use **{best_model_name}** for production\n"
                
                if problem_type == "classification":
                    report += f"✓ This is a **Classification** task\n"
                else:
                    report += f"✓ This is a **Regression** task\n"
                
                # Add sampling info if data was sampled
                if df_working.shape[0] < df.shape[0]:
                    report += f"✓ Data was sampled to {df_working.shape[0]} rows for faster processing\n"
                
                st.markdown(report)

