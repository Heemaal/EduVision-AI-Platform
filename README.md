
# Instructor Effectiveness Analysis & Recommendation System

## 📌 Project Overview
This project is an end-to-end machine learning solution designed to analyze instructor effectiveness in educational settings. By leveraging a dataset of 2,000 records, we built a robust system that:

- 📊 **Analyzes** instructor performance and student engagement metrics
- 🤖 **Predicts** key performance indicators (e.g., average feedback score, student completion rate) using regression models
- 🎯 **Generates actionable insights** to identify at-risk course batches and improvement areas
- 🧠 **Recommends** instructors based on specific student needs and learning patterns
- 🧪 **Incorporates a quiz system** to assess student understanding and tailor recommendations

## 🧰 Tech Stack
- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Streamlit
- **Frameworks:** Streamlit (for web app)
- **Machine Learning:** Regression models (Linear Regression, Random Forest, XGBoost) with hyperparameter tuning
- **Data Visualization:** Histograms, Boxplots, Pairplots, Correlation Heatmaps

## 📈 Machine Learning Pipeline
### 1. Data Preprocessing
- Handled missing values and removed duplicates
- Performed feature engineering to create new relevant features (e.g., dropout risk, engagement score)

### 2. Exploratory Data Analysis (EDA)
- Analyzed distributions of key metrics (completion rate, dropout rate, watch time, etc.)
- Identified correlations between features and target variables
- Generated visual insights to guide model selection and feature engineering

### 3. Model Training
- **Targets:** `avg_feedback_score` and `completion_rate`
- **Models Used:**
  - Linear Regression
  - Random Forest Regressor
  - XGBoost Regressor
- **Hyperparameter Tuning:** GridSearchCV / RandomizedSearchCV
- **Evaluation Metrics:** MAE, RMSE, R² Score

### 4. Model Deployment & Integration
- Saved the best-performing model (`feedback_model.pkl`)
- Integrated the model into a Streamlit web app for real-time predictions and recommendations

## 🎨 Streamlit Web Application Features
- **📊 Instructor Effectiveness Dashboard:**
  - Visualize key metrics and trends
  - Explore batch-wise performance analysis

- **🎯 Recommendation Engine:**
  - Takes inputs: course name, desired completion rate, average score preference
  - Recommends top instructors and suggests improvement areas

- **📝 Interactive Quiz System:**
  - Dynamic quiz generation 
  - Personalized feedback and recommendation
  - Suggests remedial actions based on quiz performance

  Running command : python -m streamlit run app.py

📬 Contact & Contributions
Feel free to fork this repository and submit pull requests for any improvements.
