# ==========================================================
# EduVision AI
# Smart Educational Analytics Platform
# Developed by: Heemaal Jaglan
# ==========================================================

import streamlit as st
import plotly.graph_objects as go
import ML_backend
from streamlit_option_menu import option_menu

# ----------------------------------------------------------
# PAGE CONFIGURATION
# ----------------------------------------------------------

st.set_page_config(
    page_title="EduVision AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------------------------------------------------------
# SESSION STATE
# ----------------------------------------------------------

if "theme" not in st.session_state:
    st.session_state.theme = "Light"

# ----------------------------------------------------------
# THEME SWITCH
# ----------------------------------------------------------

theme = st.toggle("🌙 Dark Mode")

if theme:

    background = "#0F172A"
    card = "#1E293B"
    text = "#FFFFFF"
    blue = "#38BDF8"
    success = "#22C55E"

else:

    background = "#F8FAFC"
    card = "#FFFFFF"
    text = "#111827"
    blue = "#2563EB"
    success = "#16A34A"

# ----------------------------------------------------------
# CUSTOM CSS
# ----------------------------------------------------------

st.markdown(
f"""
<style>

html,body,[class*="css"]{{
font-family:'Segoe UI',sans-serif;
}}

.stApp{{
background:{background};
color:{text};
}}

header{{
visibility:hidden;
}}

#MainMenu{{
visibility:hidden;
}}

footer{{
visibility:hidden;
}}

.block-container{{
padding-top:1rem;
padding-left:3rem;
padding-right:3rem;
}}

.hero{{
background:linear-gradient(135deg,#2563EB,#38BDF8);
padding:60px;
border-radius:25px;
text-align:center;
color:white;
box-shadow:0px 10px 30px rgba(0,0,0,.20);
margin-bottom:30px;
}}

.hero h1{{
font-size:60px;
margin-bottom:10px;
}}

.hero h3{{
font-size:26px;
font-weight:400;
}}

.hero p{{
font-size:18px;
margin-top:20px;
}}

.card{{
background:{card};
padding:30px;
border-radius:20px;
box-shadow:0px 8px 25px rgba(0,0,0,.10);
transition:0.3s;
min-height:420px;
margin-bottom:40px;
overflow:hidden;
}}

.card:hover{{
transform:translateY(-8px);
}}

.stats{{
background:linear-gradient(135deg,#2563EB,#3B82F6);
padding:25px;
border-radius:20px;
text-align:center;
color:white;
box-shadow:0px 8px 20px rgba(0,0,0,.15);
}}

.bigtitle{{
font-size:42px;
font-weight:700;
text-align:center;
margin-top:30px;
margin-bottom:30px;
}}

.sectiontitle{{
font-size:34px;
font-weight:700;
margin-top:40px;
margin-bottom:25px;
}}

.result-card{{
background:{success};
padding:30px;
border-radius:20px;
text-align:center;
color:white;
font-size:22px;
}}

.question-card{{
    width:95%;
    margin:auto;
    padding:40px;
    border-radius:20px;
    background:linear-gradient(135deg,#ffffff,#f8fbff);
    border:2px solid #3b82f6;
    box-shadow:0px 8px 20px rgba(0,0,0,0.15);
}}

.question-title{{
    font-size:32px;
    font-weight:bold;
    text-align:center;
    margin-bottom:20px;
}}

.question-number{{
    text-align:center;
    color:#2563eb;
    font-size:20px;
    font-weight:bold;
    margin-bottom:15px;
}}

.question-subtitle{{
    text-align:center;
    color:gray;
    font-size:18px;
}}

</style>
""",
unsafe_allow_html=True
)

# ----------------------------------------------------------
# TOP NAVIGATION
# ----------------------------------------------------------

selected = option_menu(
    menu_title=None,
    options=[
        "Home",
        "Completion",
        "Feedback",
        "Dropout",
        "🧠 AI Study Quiz"
    ],
    icons=[
        "house-fill",
        "mortarboard-fill",
        "star-fill",
        "exclamation-triangle-fill"
    ],
    orientation="horizontal",
    default_index=0
)

# ==========================================================
# HOME PAGE
# ==========================================================

if selected=="Home":

    st.markdown("""
<div class="hero">

<h1>🎓 EduVision AI</h1>

<h3>Smart Educational Analytics Powered by Machine Learning</h3>

<p>

Helping educators predict student success,
improve teaching effectiveness,
and reduce dropout rates using Artificial Intelligence.

</p>

</div>
""",unsafe_allow_html=True)

    st.markdown(
"<div class='bigtitle'>Platform Overview</div>",
unsafe_allow_html=True)

    c1,c2,c3,c4=st.columns(4)

    with c1:

        st.markdown("""
<div class="stats">

<h2>3</h2>

Machine Learning Models

</div>
""",unsafe_allow_html=True)

    with c2:

        st.markdown("""
<div class="stats">

<h2>95%</h2>

Prediction Accuracy

</div>
""",unsafe_allow_html=True)

    with c3:

        st.markdown("""
<div class="stats">

<h2>Real Time</h2>

Analytics

</div>
""",unsafe_allow_html=True)

    with c4:

        st.markdown("""
<div class="stats">

<h2>AI</h2>

Recommendations

</div>
""",unsafe_allow_html=True)

    st.markdown("<div class='sectiontitle'>Our AI Services</div>",unsafe_allow_html=True)

    a,b,c=st.columns(3)

    with a:

        st.markdown("""

<div class="card">

<h2>🎓 Completion Prediction</h2>

<p>
Predict how many students are expected to successfully complete a course using engagement, assignment submissions and quiz performance.
</p>

<ul style="line-height:2;">
<li>Early Intervention</li>
<li>Student Success Analysis</li>
<li>Performance Forecasting</li>
</ul>

""",unsafe_allow_html=True)

    with b:

        st.markdown("""

<div class="card">

<h2>⭐ Feedback Prediction</h2>

<p>
Estimate instructor feedback ratings using student engagement,
assessment performance and classroom interactions.
</p>

<ul style="line-height:2;">
<li>Instructor Performance</li>
<li>Teaching Quality</li>
<li>Student Satisfaction</li>
</ul>

</div>

""", unsafe_allow_html=True)

    with c:

     st.markdown("""

<div class="card">

<h2>⚠ Dropout Prediction</h2>

<p>
Identify students who are likely to leave the course early
and receive AI-powered intervention recommendations.
</p>

<ul style="line-height:2;">
<li>Risk Detection</li>
<li>Student Retention</li>
<li>AI Recommendations</li>
</ul>

</div>

""", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown("<div class='sectiontitle'>Why EduVision AI?</div>", unsafe_allow_html=True)

    st.markdown("""
<div class="card">

<h3>🚀 Why Choose EduVision AI?</h3>

<ul style="font-size:18px; line-height:2; padding-left:20px;">

<li>Predict academic outcomes before the semester ends.</li>

<li>Identify students requiring additional support.</li>

<li>Improve instructor effectiveness using AI.</li>

<li>Support data-driven educational decisions.</li>

<li>Built using Python • Streamlit • Scikit-Learn • Plotly.</li>

</ul>

</div>
                      
""", unsafe_allow_html=True)

# ==========================================================
# COMPLETION PREDICTION PAGE
# ==========================================================

elif selected == "Completion":

    st.markdown("<div class='bigtitle'>🎓 Course Completion Prediction</div>", unsafe_allow_html=True)

    st.write("""
This AI model predicts the expected course completion rate by analyzing
student engagement, learning behaviour, quiz performance and instructor
interaction metrics.

Higher completion rates generally indicate healthier learning engagement.
""")

    st.divider()

    left, right = st.columns([1,1])

    # -----------------------------
    # LEFT COLUMN
    # -----------------------------

    with left:

        st.subheader("📚 Academic Performance")

        avg_score_imp = st.slider(
            "📈 Score Improvement (%)",
            0.0,
            50.0,
            25.0
        )

        avg_quiz = st.slider(
            "📝 Average Quiz Score",
            0.0,
            100.0,
            75.0
        )

        st.subheader("🎯 Student Engagement")

        avg_watch = st.slider(
            "🎥 Video Watch Time",
            0.0,
            1.0,
            0.70
        )

        assign_sub = st.slider(
            "📄 Assignment Submission Rate",
            0.0,
            1.0,
            0.80
        )

    # -----------------------------
    # RIGHT COLUMN
    # -----------------------------

    with right:

        st.subheader("💬 Interaction")

        forum_act = st.slider(
            "💬 Forum Activity",
            0.0,
            1.0,
            0.50
        )

        feed_resp = st.slider(
            "📨 Feedback Response Rate",
            0.0,
            1.0,
            0.60
        )

        st.subheader("📊 Additional Inputs")

        est_dropout = st.slider(
            "⚠ Estimated Dropout Rate",
            0.0,
            1.0,
            0.30
        )

        est_feedback = st.slider(
            "⭐ Estimated Feedback Score",
            0.0,
            5.0,
            4.0
        )

    st.write("")
    st.write("")

    predict = st.button(
        "🚀 Predict Completion Rate",
        use_container_width=True
    )

    if predict:

        engagement_score = (
            avg_watch +
            assign_sub +
            forum_act
        ) / 3

        learning_score = (
            avg_quiz +
            avg_score_imp
        ) / 2

        data = [[

            est_dropout,

            avg_score_imp,

            avg_quiz,

            avg_watch,

            assign_sub,

            forum_act,

            est_feedback,

            feed_resp,

            engagement_score,

            learning_score

        ]]

        prediction = (
            ML_backend.lr_completion.predict(data)[0]
        ) * 100

        st.write("")

        st.success("Prediction Generated Successfully")

        # ------------------------------------
        # Plotly Gauge
        # ------------------------------------

        fig = go.Figure(

            go.Indicator(

                mode="gauge+number",

                value=prediction,

                number={'suffix':"%"},

                title={'text':"Predicted Completion Rate"},

                gauge={

                    'axis':{'range':[0,100]},

                    'bar':{'color':"#2563EB"},

                    'steps':[

                        {'range':[0,40],'color':"#FCA5A5"},

                        {'range':[40,70],'color':"#FCD34D"},

                        {'range':[70,100],'color':"#86EFAC"}

                    ]

                }

            )

        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        progress_value = max(0, min(100, int(prediction)))
        st.progress(progress_value)

        st.metric(
            "Completion Rate",
            f"{prediction:.1f}%"
        )

        st.subheader("🤖 AI Insights")

        if prediction >= 85:

            st.success("""
Excellent course health detected.

Students demonstrate outstanding engagement,
strong academic performance and minimal risk.

Recommendation:
Maintain the current teaching strategy and
continue encouraging collaborative learning.
""")

            st.balloons()

        elif prediction >= 70:

            st.info("""
Overall performance is good.

Some students may require additional
engagement activities.

Recommendation:

• Increase discussion forums

• Introduce weekly quizzes

• Encourage assignment participation
""")

        elif prediction >= 50:

            st.warning("""
Moderate completion probability detected.

Recommendation:

• Improve instructor interaction

• Increase feedback frequency

• Monitor inactive students
""")

        else:

            st.error("""
Critical completion risk detected.

Immediate intervention is recommended.

Suggested Actions

• Contact inactive students

• Reduce assignment difficulty

• Schedule mentoring sessions

• Increase classroom engagement
""")

# ==========================================================
# FEEDBACK PREDICTION PAGE
# ==========================================================

elif selected == "Feedback":

    st.markdown(
        "<div class='bigtitle'>⭐ Instructor Feedback Prediction</div>",
        unsafe_allow_html=True
    )

    st.write("""
This Machine Learning model predicts the expected instructor feedback
score based on student engagement, academic performance,
assignment completion and instructor responsiveness.

A higher feedback score generally reflects better teaching quality
and student satisfaction.
""")

    st.divider()

    left, right = st.columns(2)

    # -----------------------------
    # LEFT COLUMN
    # -----------------------------

    with left:

        st.subheader("📚 Academic Performance")

        avg_score_imp = st.slider(
            "📈 Score Improvement (%)",
            0.0,
            50.0,
            30.0,
            key="fb1"
        )

        avg_quiz = st.slider(
            "📝 Average Quiz Score",
            0.0,
            100.0,
            80.0,
            key="fb2"
        )

        st.subheader("🎯 Student Engagement")

        avg_watch = st.slider(
            "🎥 Video Watch Time",
            0.0,
            1.0,
            0.80,
            key="fb3"
        )

        assign_sub = st.slider(
            "📄 Assignment Submission Rate",
            0.0,
            1.0,
            0.85,
            key="fb4"
        )

    # -----------------------------
    # RIGHT COLUMN
    # -----------------------------

    with right:

        st.subheader("💬 Instructor Interaction")

        forum_act = st.slider(
            "💬 Forum Activity",
            0.0,
            1.0,
            0.60,
            key="fb5"
        )

        feed_resp = st.slider(
            "📨 Feedback Response Rate",
            0.0,
            1.0,
            0.70,
            key="fb6"
        )

        st.subheader("📊 Additional Inputs")

        est_completion = st.slider(
            "🎓 Estimated Completion Rate",
            0.0,
            1.0,
            0.70,
            key="fb7"
        )

        est_dropout = st.slider(
            "⚠ Estimated Dropout Rate",
            0.0,
            1.0,
            0.20,
            key="fb8"
        )

    st.write("")

    predict_feedback = st.button(
        "⭐ Predict Feedback Score",
        use_container_width=True
    )

    if predict_feedback:

        engagement_score = (
            avg_watch +
            assign_sub +
            forum_act
        ) / 3

        learning_score = (
            avg_quiz +
            avg_score_imp
        ) / 2

        data = [[

            est_completion,

            est_dropout,

            avg_score_imp,

            avg_quiz,

            avg_watch,

            assign_sub,

            forum_act,

            feed_resp,

            engagement_score,

            learning_score

        ]]

        prediction = ML_backend.lr_feedback.predict(data)[0]

        prediction = max(0, min(5, prediction))

        st.success("Prediction Generated Successfully")

        # -----------------------------------
        # Plotly Gauge
        # -----------------------------------

        fig = go.Figure(

            go.Indicator(

                mode="gauge+number",

                value=prediction,

                number={"suffix":"/5"},

                title={"text":"Predicted Feedback Score"},

                gauge={

                    "axis":{"range":[0,5]},

                    "bar":{"color":"gold"},

                    "steps":[

                        {"range":[0,2],"color":"#FCA5A5"},

                        {"range":[2,4],"color":"#FCD34D"},

                        {"range":[4,5],"color":"#86EFAC"}

                    ]

                }

            )

        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        confidence = min(99, max(70, int(prediction * 20)))

        st.metric(
            "Predicted Rating",
            f"{prediction:.2f}/5"
        )

        st.progress(confidence)

        st.caption(f"Prediction Confidence : {confidence}%")

        st.subheader("🤖 AI Teaching Insights")

        if prediction >= 4.5:

            st.success("""

🌟 Outstanding Teaching Performance

Students are highly satisfied with the
overall learning experience.

Recommendations

✔ Continue interactive sessions

✔ Maintain current teaching style

✔ Share best practices with peers

""")

            st.balloons()

        elif prediction >= 4:

            st.info("""

Very Good Performance

Students appreciate the teaching quality.

Suggestions

✔ Increase classroom discussions

✔ Provide additional learning resources

✔ Encourage collaborative learning

""")

        elif prediction >= 3:

            st.warning("""

Average Student Satisfaction

Students are learning,
but improvements are possible.

Suggestions

✔ Improve feedback turnaround time

✔ Increase student interaction

✔ Conduct regular doubt sessions

""")

        else:

            st.error("""

Low Predicted Feedback Score

Immediate improvements are recommended.

Priority Actions

✔ Increase engagement

✔ Improve communication

✔ Provide personalized feedback

✔ Review teaching methodology

""")

# ==========================================================
# DROPOUT PREDICTION PAGE
# ==========================================================

elif selected == "Dropout":

    st.markdown(
        "<div class='bigtitle'>⚠ Student Dropout Prediction</div>",
        unsafe_allow_html=True
    )

    st.write("""
The Dropout Prediction model estimates the percentage of students who
are at risk of leaving the course before completion.

This helps educators identify struggling students early and take
preventive actions to improve student retention.
""")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📚 Academic Performance")

        avg_score_imp = st.slider(
            "📈 Score Improvement (%)",
            0.0,
            50.0,
            15.0,
            key="dr1"
        )

        avg_quiz = st.slider(
            "📝 Average Quiz Score",
            0.0,
            100.0,
            50.0,
            key="dr2"
        )

        st.subheader("🎯 Student Engagement")

        avg_watch = st.slider(
            "🎥 Video Watch Time",
            0.0,
            1.0,
            0.40,
            key="dr3"
        )

        assign_sub = st.slider(
            "📄 Assignment Submission Rate",
            0.0,
            1.0,
            0.50,
            key="dr4"
        )

    with col2:

        st.subheader("💬 Instructor Interaction")

        forum_act = st.slider(
            "💬 Forum Activity",
            0.0,
            1.0,
            0.20,
            key="dr5"
        )

        feed_resp = st.slider(
            "📨 Feedback Response Rate",
            0.0,
            1.0,
            0.40,
            key="dr6"
        )

        st.subheader("📊 Additional Inputs")

        est_completion = st.slider(
            "🎓 Estimated Completion Rate",
            0.0,
            1.0,
            0.50,
            key="dr7"
        )

        est_feedback = st.slider(
            "⭐ Estimated Feedback Score",
            0.0,
            5.0,
            3.50,
            key="dr8"
        )

    st.write("")

    predict_dropout = st.button(
        "⚠ Predict Dropout Risk",
        use_container_width=True
    )

    if predict_dropout:

        engagement_score = (
            avg_watch +
            assign_sub +
            forum_act
        ) / 3

        learning_score = (
            avg_quiz +
            avg_score_imp
        ) / 2

        data = [[

            est_completion,

            avg_score_imp,

            avg_quiz,

            avg_watch,

            assign_sub,

            forum_act,

            est_feedback,

            feed_resp,

            engagement_score,

            learning_score

        ]]

        prediction = ML_backend.lr_dropout.predict(data)[0] * 100

        prediction = max(0, min(100, prediction))

        st.success("Prediction Generated Successfully")

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=prediction,
                number={"suffix":"%"},
                title={"text":"Predicted Dropout Risk"},
                gauge={
                    "axis":{"range":[0,100]},
                    "bar":{"color":"red"},
                    "steps":[
                        {"range":[0,25],"color":"#86EFAC"},
                        {"range":[25,60],"color":"#FCD34D"},
                        {"range":[60,100],"color":"#FCA5A5"}
                    ]
                }
            )
        )

        st.plotly_chart(fig, use_container_width=True)

        st.metric(
            "Dropout Risk",
            f"{prediction:.1f}%"
        )

        st.progress(int(prediction))

        st.subheader("🤖 AI Risk Analysis")

        if prediction <= 20:

            st.success("""

🟢 LOW RISK

Excellent student retention.

Recommendations

✔ Maintain current teaching strategy

✔ Continue regular assessments

✔ Encourage peer learning

""")

            st.balloons()

        elif prediction <= 50:

            st.warning("""

🟡 MODERATE RISK

Some students require attention.

Suggestions

✔ Increase student interaction

✔ Conduct weekly doubt sessions

✔ Send reminder notifications

""")

        else:

            st.error("""

🔴 HIGH RISK

Immediate intervention required.

Recommended Actions

✔ Contact inactive students

✔ Schedule mentoring

✔ Reduce course difficulty

✔ Increase instructor interaction

✔ Monitor attendance weekly

""")

            st.snow()

# ==========================================================
# AI STUDY & TEACHING QUIZ
# ==========================================================

elif selected == "🧠 AI Study Quiz":

    st.markdown(
        "<div class='bigtitle'>🧠 AI Study Assessment</div>",
        unsafe_allow_html=True
    )

    st.write("""
Welcome to the **AI Study Assessment**.

This intelligent assessment analyzes your study habits or practices
and provides personalized recommendations to improve learning outcomes.

Choose your assessment below and let EduVision AI analyse your profile.
""")

    st.divider()

    # Button to show the quiz
    if st.button("👨‍🎓 Start Student Quiz", key="start_quiz"):
        
        # Store in session state that quiz is active
        st.session_state.quiz_active = True

    # Check if quiz should be displayed
    if st.session_state.get("quiz_active", False):

        st.markdown("## 👨‍🎓 Student Learning Assessment")

        st.info("""
Answer all the questions honestly.

Based on your responses, EduVision AI will evaluate your learning habits,
identify your strengths and weaknesses, and generate a personalized study plan.
""")

        st.divider()

        # ===========================
        # Question 1 Card
        # ===========================
        def generate_student_analysis(q1, q2, q3, q4, q5):

            strengths = []
            weaknesses = []
            recommendations = []

            # Study Hours Analysis
            if q1 in ["2 to 4 hours", "More than 4 hours"]:
                strengths.append(
                    "You maintain a good amount of daily study time which shows commitment towards learning."
                )
            else:
                weaknesses.append(
                    "Your daily study hours are lower than recommended for consistent academic growth."
                )
                recommendations.append(
                    "Increase your focused study duration gradually. Start by adding 30-60 minutes daily."
                )

            # Extra Activities Analysis
            if q2 in ["No participation", "Less than 1 hour"]:
                strengths.append(
                    "You maintain good control over your schedule and avoid excessive distractions."
                )
            else:
                weaknesses.append(
                    "Extra-curricular activities may be reducing your available study time."
                )
                recommendations.append(
                    "Create a balance between academics and activities by scheduling dedicated study hours."
                )

            # Timetable Analysis
            if q3 in ["Usually", "Always"]:
                strengths.append(
                    "You have good planning skills and follow a structured learning approach."
                )
            else:
                weaknesses.append(
                    "Your study routine lacks proper planning and consistency."
                )
                recommendations.append(
                    "Create a daily timetable with specific learning goals and revision time."
                )

            # AI Usage Analysis
            if q4 == "Combination of AI & Traditional Learning":
                strengths.append(
                    "You use a balanced learning approach by combining AI tools with traditional methods."
                )
            elif q4 == "Mostly AI Tools (ChatGPT, Gemini)":
                strengths.append(
                    "You actively use modern AI tools for learning."
                )
                recommendations.append(
                    "Do not completely depend on AI. Verify concepts through books, practice and self-learning."
                )
            elif q4 == "Only Classroom Learning":
                weaknesses.append(
                    "Your learning approach depends mainly on classroom resources."
                )
                recommendations.append(
                    "Explore AI tools, online resources and self-practice for better understanding."
                )
            else:
                strengths.append(
                    "You follow traditional learning methods which can build strong conceptual understanding."
                )

            # Sleep Analysis
            if q5 == "7–9 hours":
                strengths.append(
                    "Your sleep routine supports better concentration and learning ability."
                )
            elif q5 in ["Less than 5 hours", "5–7 hours"]:
                weaknesses.append(
                    "Your sleep duration may affect focus, memory and productivity."
                )
                recommendations.append(
                    "Maintain 7-9 hours of sleep for better academic performance."
                )
            else:
                recommendations.append(
                    "Maintain a balanced sleep schedule and avoid oversleeping."
                )

            return strengths, weaknesses, recommendations

        st.markdown("""
        <div class="question-card">

        <div class="question-number">
        Question 1 of 5
        </div>

        <div class="question-title">
        📚 How many hours do you study every day?
        </div>

        <div class="question-subtitle">
        Select the option that best matches your daily study routine.
        </div>

        </div>
        """, unsafe_allow_html=True)

        q1 = st.radio(
            "",
            [
                "Less than 1 hour",
                "1 to 2 hours",
                "2 to 4 hours",
                "More than 4 hours"
            ],
            horizontal=True,
            label_visibility="collapsed",
            key="q1"
        )

        # ===========================
        # Question 2 Card
        # ===========================

        st.markdown("""
        <div class="question-card">

        <div class="question-number">
        Question 2 of 5
        </div>

        <div class="question-title">
        🏃 How much time do you spend on extra-curricular activities?
        </div>

        <div class="question-subtitle">
        Select the option that best matches your daily involvement in extra-curricular activities.
        </div>

        </div>
        """, unsafe_allow_html=True)

        q2 = st.radio(
            "",
            [
                "No participation",
                "Less than 1 hour",
                "1–2 hours",
                "More than 2 hours"
            ],
            horizontal=True,
            label_visibility="collapsed",
            key="q2"
        )

        st.markdown("""
        <div class="question-card">

        <div class="question-number">
        Question 3 of 5
        </div>

        <div class="question-title">
        📅 Do you follow a proper timetable for your studies?
        </div>

        <div class="question-subtitle">
        Select the option that best describes your study planning habit.
        </div>

        </div>
        """, unsafe_allow_html=True)

        q3 = st.radio(
            "",
            [
                "Never",
                "Sometimes",
                "Usually",
                "Always"
            ],
            horizontal=True,
            label_visibility="collapsed",
            key="q3"
        )

        st.markdown("""
        <div class="question-card">

        <div class="question-number">
        Question 4 of 5
        </div>

        <div class="question-title">
        🤖 Which study method do you mostly use?
        </div>

        <div class="question-subtitle">
        Select the learning approach you use most frequently for studying.
        </div>

        </div>
        """, unsafe_allow_html=True)

        q4 = st.radio(
            "",
            [
                "Mostly AI Tools (ChatGPT, Gemini)",
                "Combination of AI & Traditional Learning",
                "Mostly Books & Notes",
                "Only Classroom Learning"
            ],
            horizontal=True,
            label_visibility="collapsed",
            key="q4"
        )

        # ===========================
        # Question 5 Card
        # ===========================

        st.markdown("""
        <div class="question-card">

        <div class="question-number">
        Question 5 of 5
        </div>

        <div class="question-title">
        😴 How many hours do you sleep every day?
        </div>

        <div class="question-subtitle">
        Select the option that best matches your average daily sleep duration.
        </div>

        </div>
        """, unsafe_allow_html=True)

        q5 = st.radio(
            "",
            [
                "Less than 5 hours",
                "5–7 hours",
                "7–9 hours",
                "More than 9 hours"
            ],
            horizontal=True,
            label_visibility="collapsed",
            key="q5"
        )

        submit = st.button("Generate My Study Analysis 🚀", key="submit_quiz")

        if submit:

            strengths, weaknesses, recommendations = generate_student_analysis(
                q1,
                q2,
                q3,
                q4,
                q5
            )

            st.divider()

            st.header("📊 Your Personalized Study Analysis")

            st.subheader("💪 Your Strengths")
            for item in strengths:
                st.success(item)

            st.subheader("⚠️ Your Weak Points")
            for item in weaknesses:
                st.warning(item)

            st.subheader("🚀 Recommendations For Improvement")
            for item in recommendations:
                st.info(item)

            # Option to reset and take quiz again
            if st.button("🔄 Take Quiz Again", key="reset_quiz"):
                st.session_state.quiz_active = False
                st.rerun()

    else:
        # Show a message when quiz is not active
        st.info("👆 Click the 'Start Student Quiz' button above to begin your assessment.")

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.markdown(
"""
<div style="text-align:center; padding:20px;">

<h3>🎓 EduVision AI</h3>

<p>
Smart Educational Analytics Powered by Machine Learning
</p>

<p>

Python • Streamlit • Plotly • Scikit-Learn • Machine Learning

</p>

<p>

Developed by <b>Heemaal Jaglan</b>

</p>

<p>

© 2026 All Rights Reserved

</p>

</div>
""",
unsafe_allow_html=True
)