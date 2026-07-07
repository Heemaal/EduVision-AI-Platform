import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. Load the data
df = pd.read_csv('dataset.csv')

# 2. Replicate your exact Feature Engineering
df['engagement_score'] = (df['avg_watch_time'] + df['assignment_submission_rate'] + df['forum_activity_rate']) / 3
df['learning_performance'] = (df['avg_quiz_score'] + df['avg_score_improvement']) / 2

# 3. Train Completion Rate Model (Using your 10 features)
features_comp = [
    'dropout_rate', 'avg_score_improvement', 'avg_quiz_score', 'avg_watch_time', 
    'assignment_submission_rate', 'forum_activity_rate', 'avg_feedback_score', 
    'feedback_response_rate', 'engagement_score', 'learning_performance'
]
lr_completion = LinearRegression().fit(df[features_comp], df['completion_rate'])

# 4. Train Feedback Score Model (Using your 10 features)
features_feed = [
    'completion_rate', 'dropout_rate', 'avg_score_improvement', 'avg_quiz_score', 'avg_watch_time', 
    'assignment_submission_rate', 'forum_activity_rate', 'feedback_response_rate', 
    'engagement_score', 'learning_performance'
]
lr_feedback = LinearRegression().fit(df[features_feed], df['avg_feedback_score'])

# 5. Train Dropout Rate Model (Using your 10 features)
features_drop = [
    'completion_rate', 'avg_score_improvement', 'avg_quiz_score', 'avg_watch_time', 
    'assignment_submission_rate', 'forum_activity_rate', 'avg_feedback_score', 
    'feedback_response_rate', 'engagement_score', 'learning_performance'
]
lr_dropout = LinearRegression().fit(df[features_drop], df['dropout_rate'])

# (No return statements needed! Python just remembers these variables)