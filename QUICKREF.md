# ⚡ Quick Reference Card

## 🚀 Start Here (2 Minutes)

```bash
# Step 1: Install
pip install -r requirements.txt

# Step 2: Run
streamlit run main.py

# Step 3: Use
- Open http://localhost:8501
- Upload CSV
- Select target column
- Click "Run AutoML"
- View results & download CSV
```

---

## 📊 What the App Does

| Step | Action | Output |
|------|--------|--------|
| 1 | Upload CSV | Data preview |
| 2 | Select target | Problem type detected |
| 3 | Click Run | Data cleaned automatically |
| 4 | Train models | 7-8 models trained with CV |
| 5 | View results | Comparison table + chart |
| 6 | Download CSV | Results exported |

---

## 🤖 Models Available

**Classification (7 models)**
- Logistic Regression
- Random Forest
- Gradient Boosting
- SVM
- K-Nearest Neighbors
- Decision Tree
- Naive Bayes

**Regression (8 models)**
- Linear Regression
- Ridge
- Lasso
- Random Forest
- Gradient Boosting
- SVR
- K-Nearest Neighbors
- Decision Tree

---

## 📈 Metrics You Get

**For Classification:**
- Accuracy, Precision, Recall, F1-Score
- CV Mean & Std

**For Regression:**
- R², MAE, MSE, RMSE
- CV Mean & Std

---

## 🧹 Automatic Cleaning

✅ Removes duplicates  
✅ Fills missing values (median/mode)  
✅ Clips outliers (IQR method)  
✅ Fixes infinite values  
✅ Converts data types  

---

## 🎯 Problem Detection

**Classification:**
- Categorical target
- Numeric target with ≤20 unique values

**Regression:**
- Continuous numeric target
- >20 unique values

---

## 📁 File Guide

| File | Purpose |
|------|---------|
| **main.py** | App code (run this) |
| **SETUP.md** | Setup instructions |
| **README.md** | Full documentation |
| **IMPROVEMENTS.md** | What changed |
| **DELIVERY.md** | Complete overview |
| **INDEX.md** | Project guide |
| **requirements.txt** | Dependencies |
| **run.sh** | Quick setup script |
| **iris.csv** | Test data (classification) |
| **air.csv** | Test data (regression) |

---

## ⚙️ System Requirements

```
Python: 3.8+
RAM: 2GB minimum
Disk: 1GB minimum
Dependencies: 5 packages
Installation time: 2-5 minutes
```

---

## 💻 Sample Commands

```bash
# Full setup & run
bash run.sh

# Just install
pip install -r requirements.txt

# Run with custom port
streamlit run main.py --server.port 8502

# Run with different host
streamlit run main.py --server.address 0.0.0.0
```

---

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| Module not found | `pip install -r requirements.txt` |
| Port in use | `streamlit run main.py --server.port 8502` |
| Slow processing | Use smaller dataset |
| Models failing | Check CSV format |
| Data too small | Need ≥10 rows |

---

## 📊 Dataset Requirements

```
Minimum rows: 10
Optimal rows: 100-10,000
Maximum rows: 100,000+ (slower)

Minimum columns: 1
Maximum columns: No limit

Data types:
✅ Numbers (int, float)
✅ Text (categorical)
✅ Yes/No, True/False
✅ Mixed types
```

---

## 🎓 Key Concepts

**Classification** - Predicting categories
- Binary: Yes/No, True/False
- Multi-class: Categories A, B, C...

**Regression** - Predicting numbers
- House prices, temperature, etc.

**Cross-Validation** - Test robustness
- Splits data 5 ways
- Average results = more reliable

**Metrics** - Measure performance
- Accuracy/R² = main scores
- Precision/Recall = detail metrics

---

## 💡 Tips & Tricks

1. **Classify or Regress?**
   - App auto-detects, but you can check
   - Discrete values? → Classification
   - Continuous values? → Regression

2. **Best Model?**
   - Check the badge at top right
   - Look at the metrics table
   - Consider CV scores for consistency

3. **Export Results?**
   - Click "Download Results as CSV"
   - Open in Excel/Sheets
   - Share with team

4. **Slow Processing?**
   - Use fewer rows (sample your data)
   - Use fewer columns (drop irrelevant ones)
   - Smaller datasets train faster

5. **Better Models?**
   - More data = better models
   - Clean data = better results
   - Relevant features = better predictions

---

## 📊 Expected Results

**Classification (iris.csv):**
```
✅ 7 models trained
✅ ~98% best accuracy
✅ Training time: ~10 seconds
✅ Best model: Random Forest
```

**Regression (air.csv):**
```
✅ 8 models trained
✅ ~0.9+ R² score
✅ Training time: ~15 seconds
✅ Best model: Gradient Boosting
```

---

## 🔐 Privacy & Security

- ✅ All processing **local** (no servers)
- ✅ Data **never stored**
- ✅ No **external API calls**
- ✅ Results **in your control**
- ✅ Export when you want

---

## 📞 Help Resources

1. **Setup issues** → `SETUP.md`
2. **Feature questions** → `README.md`
3. **Technical details** → `IMPROVEMENTS.md`
4. **Overview** → `INDEX.md`
5. **Code comments** → `main.py`

---

## ✨ What Makes This Special

✅ **Automatic** - Cleans & preprocesses for you  
✅ **Smart** - Detects problem type automatically  
✅ **Comprehensive** - 15 different models  
✅ **Robust** - 5-fold cross-validation  
✅ **Beautiful** - Interactive visualizations  
✅ **Professional** - Export-ready results  
✅ **Safe** - Local processing, no data loss  
✅ **Easy** - No ML knowledge needed  

---

## 🎯 Perfect For

- 🎓 Learning ML concepts
- 🚀 Quick prototyping
- 📊 Data exploration
- 🏆 Model benchmarking
- 🤝 Team sharing
- 🔍 Problem investigation
- 💼 Business analysis
- 📈 Trend analysis

---

## 📋 Before You Start

- [ ] Python 3.8+ installed?
- [ ] Disk space available? (1GB+)
- [ ] CSV file ready?
- [ ] Target column identified?
- [ ] About 10+ data rows?

**If yes to all, you're ready! 🚀**

---

## ⏱️ Timeline

```
Step 1: Install     - 2-5 minutes
Step 2: Run app     - 30 seconds
Step 3: Upload CSV  - 30 seconds
Step 4: Run AutoML  - 10-30 seconds
Step 5: View results- 10 seconds
Step 6: Download    - 10 seconds

Total time: ~5-10 minutes ⏱️
```

---

## 🎉 You're All Set!

Everything is ready to use. Just run:

```bash
streamlit run main.py
```

**Enjoy your AutoML experience! 🚀**

---

*Quick Reference - Version 1.0 - November 2024*
