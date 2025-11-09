🎓 Student Performance Analytics Dashboard

A comprehensive Python-based analytics dashboard for analyzing and visualizing student performance metrics including CGPA, SGPA, extracurricular activities, and behavioral scores with interactive visualizations and machine learning predictions.

🌟 Features

 📊 Overall Class Analytics
- **CGPA Distribution** - Histogram visualization of grade point distribution across the class
- **Interactive Scatter Plots** - Dynamic CGPA vs SGPA analysis with extracurricular and behavior influence
- **Average Performance Metrics** - Comprehensive bar charts showing mean scores across all categories
- **Correlation Analysis** - Heatmap displaying relationships between different performance indicators
- **Top & Bottom Performers** - Automatic identification of top 5 and bottom 5 students
- **ML-Powered Predictions** - Linear regression model to predict CGPA based on multiple factors

 🎯 Individual Student Performance
- **Detailed Student Reports** - Complete performance breakdown with all metrics
- **Smart Categorization** - Automatic performance grading system
- **Visual Analytics** - Individual bar charts for each student's scores
- **Quick Search** - Roll number-based student lookup system

 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.x** | Core programming language |
| **Pandas** | Data manipulation and analysis |
| **NumPy** | Numerical computations |
| **Matplotlib** | Static data visualizations |
| **Seaborn** | Statistical graphics and heatmaps |
| **Plotly** | Interactive charts and graphs |
| **Scikit-learn** | Machine learning (Linear Regression) |

 📦 Installation

Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- Jupyter Notebook (optional, for .ipynb files)

Quick Start

1. **Install dependencies**

pip install pandas numpy matplotlib seaborn plotly scikit-learn jupyter

2. **Run the program**

python pyp-project-full.py
jupyter notebook pyp-project-full.ipynb


 💻 Usage

 Main Menu
Upon running the program, you'll see an interactive menu:

```
🎓 STUDENT PERFORMANCE ANALYTICS DASHBOARD 🎯
=============================================
1️⃣  View Overall Class Analytics
2️⃣  View Individual Student Performance

Enter your choice (1 or 2):
```

 Option 1: Overall Class Analytics
- Displays comprehensive class-wide statistics
- Shows multiple visualizations:
  - CGPA distribution histogram
  - Interactive CGPA vs SGPA scatter plot
  - Average scores bar chart
  - Correlation heatmap
- Lists top 5 and bottom 5 performers
- Displays ML model accuracy (R² score)

 Option 2: Individual Student Performance
- Enter student roll number (format: S001, S002, etc.)
- View complete student profile with:
  - All performance metrics
  - Overall performance score
  - Performance category and remarks
  - Visual breakdown chart

 📊 Data Structure

The system generates synthetic data for 30 students with the following metrics:

| Metric | Range | Weight |
|--------|-------|--------|
| **CGPA** | 6.0 - 10.0 | 50% |
| **SGPA** | 5.5 - 10.0 | 30% |
| **Extracurricular Score** | 0 - 10 | 10% |
| **Behaviour Score** | 5 - 10 | 10% |

 Overall Performance Formula
```
Overall Performance = (0.5 × CGPA) + (0.3 × SGPA) + 
                      (0.1 × Extracurricular) + (0.1 × Behaviour)
```

 🎯 Performance Categories

| Overall Score | Category | Emoji |
|---------------|----------|-------|
| ≥ 9.0 | Excellent Performance | 🌟 |
| 8.0 - 8.9 | Good Performance | 👍 |
| 7.0 - 7.9 | Average Performance | 🙂 |
| < 7.0 | Needs Improvement | ⚠️ |

 🧠 Machine Learning Model

- **Algorithm**: Linear Regression
- **Input Features**: 
  - SGPA
  - Extracurricular Score
  - Behaviour Score
- **Prediction Target**: CGPA
- **Evaluation Metric**: R² Score
- **Train/Test Split**: 80/20

 Class Analytics View
```
📊 CLASS PERFORMANCE OVERVIEW

   Student_ID       Name   CGPA  SGPA  Extracurricular_Score  Behaviour_Score
0        S001  Student_1   8.96  9.64                      3                9
1        S002  Student_2   9.50  7.25                      7                7
...

[Visualizations displayed]

🏆 TOP 5 PERFORMERS:
        Name   CGPA  SGPA  Overall_Performance
...
```

 Individual Student View
```
🎯 STUDENT PERFORMANCE CHECKER

Enter Student Roll Number (e.g., S005): S005

📘 Student Details for S005
----------------------------------
Name: Student_5
CGPA: 8.50
SGPA: 8.80
Extracurricular Score: 7
Behaviour Score: 8
Overall Performance: 8.59
Remark: 👍 Good Performance

[Bar chart displayed]
```

 🚀 Future Enhancements

- [ ] Web interface using Streamlit or Flask
- [ ] Import real student data from CSV/Excel
- [ ] Export reports as PDF
- [ ] Add attendance tracking
- [ ] Multi-semester trend analysis
- [ ] Email notification system for low performers
- [ ] Advanced ML models (Random Forest, Neural Networks)
- [ ] Database integration (SQLite/MySQL)

 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/YourFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add YourFeature'`)
5. Push to the branch (`git push origin feature/YourFeature`)
6. Open a Pull Request

 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

 👨‍💻 Author
Bhanu Sai Guggilapu, passionate CSE student 
Github:https://github.com/bhanu78sai
- Email: bhanusaiguggilapu78@gmail.com

## 🙏 Acknowledgments

- Built using Python's powerful data science ecosystem
- Inspired by educational institutions' need for performance analytics
- Thanks to the open-source community
