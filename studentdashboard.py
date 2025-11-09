# ==============================
# 🎓 STUDENT PERFORMANCE ANALYTICS DASHBOARD (Menu Version)
# ==============================

# --- Imports ---
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Enable inline charts
%matplotlib inline

# --------------------------
# 1. GENERATE / LOAD DATA
# --------------------------
np.random.seed(42)
n_students = 30
data = {
    "Student_ID": [f"S{i+1:03d}" for i in range(n_students)],
    "Name": [f"Student_{i+1}" for i in range(n_students)],
    "CGPA": np.round(np.random.uniform(6.0, 10.0, n_students), 2),
    "SGPA": np.round(np.random.uniform(5.5, 10.0, n_students), 2),
    "Extracurricular_Score": np.random.randint(0, 10, n_students),
    "Behaviour_Score": np.random.randint(5, 10, n_students),
}

df = pd.DataFrame(data)

# Weighted overall performance
df["Overall_Performance"] = (
    0.5 * df["CGPA"]
    + 0.3 * df["SGPA"]
    + 0.1 * df["Extracurricular_Score"]
    + 0.1 * df["Behaviour_Score"]
).round(2)

# --------------------------
# 2. MENU SYSTEM
# --------------------------
print("🎓 STUDENT PERFORMANCE ANALYTICS DASHBOARD 🎯")
print("=============================================")
print("1️⃣  View Overall Class Analytics")
print("2️⃣  View Individual Student Performance")
choice = input("\nEnter your choice (1 or 2): ").strip()

# --------------------------
# 3. OPTION 1: OVERALL ANALYTICS
# --------------------------
if choice == "1":
    print("\n📊 CLASS PERFORMANCE OVERVIEW\n")
    display(df.head())

    # CGPA Distribution
    plt.figure(figsize=(7, 4))
    plt.hist(df["CGPA"], bins=8, color="skyblue", edgecolor="black")
    plt.title("CGPA Distribution")
    plt.xlabel("CGPA")
    plt.ylabel("Number of Students")
    plt.show()
    plt.close()

    # Interactive Scatter Plot (CGPA vs SGPA)
    fig = px.scatter(
        df,
        x="SGPA",
        y="CGPA",
        color="Extracurricular_Score",
        size="Behaviour_Score",
        hover_name="Name",
        title="CGPA vs SGPA with Extracurricular & Behaviour Influence",
    )
    fig.show()

    # Average Scores
    avg_scores = df[["CGPA", "SGPA", "Extracurricular_Score", "Behaviour_Score"]].mean()
    plt.figure(figsize=(7, 4))
    avg_scores.plot(kind="bar", color=["#5DADE2", "#48C9B0", "#F5B041", "#AF7AC5"])
    plt.title("Average Scores Overview")
    plt.ylabel("Average Score")
    plt.show()
    plt.close()

    # Correlation Heatmap
    plt.figure(figsize=(6, 5))
    sns.heatmap(df[["CGPA", "SGPA", "Extracurricular_Score", "Behaviour_Score", "Overall_Performance"]].corr(),
                annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Between Metrics")
    plt.show()
    plt.close()

    # Top and Bottom Performers
    top_5 = df.sort_values(by="Overall_Performance", ascending=False).head(5)
    bottom_5 = df.sort_values(by="Overall_Performance", ascending=True).head(5)

    print("\n🏆 TOP 5 PERFORMERS:")
    display(top_5[["Name", "CGPA", "SGPA", "Overall_Performance"]])

    print("\n⚠️ BOTTOM 5 PERFORMERS:")
    display(bottom_5[["Name", "CGPA", "SGPA", "Overall_Performance"]])

    # Model Training
    X = df[["SGPA", "Extracurricular_Score", "Behaviour_Score"]]
    y = df["CGPA"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    print(f"\n🔮 Model Accuracy (R²): {r2:.2f}")

# --------------------------
# 4. OPTION 2: INDIVIDUAL STUDENT PERFORMANCE
# --------------------------
elif choice == "2":
    print("\n🎯 STUDENT PERFORMANCE CHECKER\n")
    roll_no = input("Enter Student Roll Number (e.g., S005): ").strip().upper()

    if roll_no in df["Student_ID"].values:
        student = df[df["Student_ID"] == roll_no].iloc[0]
        print(f"\n📘 Student Details for {roll_no}")
        print("----------------------------------")
        print(f"Name: {student['Name']}")
        print(f"CGPA: {student['CGPA']}")
        print(f"SGPA: {student['SGPA']}")
        print(f"Extracurricular Score: {student['Extracurricular_Score']}")
        print(f"Behaviour Score: {student['Behaviour_Score']}")
        print(f"Overall Performance: {student['Overall_Performance']}")

        # Performance Category
        if student["Overall_Performance"] >= 9:
            remark = "🌟 Excellent Performance"
        elif student["Overall_Performance"] >= 8:
            remark = "👍 Good Performance"
        elif student["Overall_Performance"] >= 7:
            remark = "🙂 Average Performance"
        else:
            remark = "⚠️ Needs Improvement"

        print(f"Remark: {remark}")

        # Mini bar chart
        scores = {
            "CGPA": student["CGPA"],
            "SGPA": student["SGPA"],
            "Extracurricular": student["Extracurricular_Score"],
            "Behaviour": student["Behaviour_Score"]
        }
        plt.figure(figsize=(6, 4))
        plt.bar(scores.keys(), scores.values(), color=["#5DADE2", "#48C9B0", "#F5B041", "#AF7AC5"])
        plt.title(f"Performance Breakdown for {student['Name']}")
        plt.ylim(0, 10)
        plt.ylabel("Score")
        plt.show()
        plt.close()
    else:
        print("❌ Roll Number not found. Please try again.")

else:
    print("\n❌ Invalid choice. Please enter 1 or 2.")