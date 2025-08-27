# SCT_DS_2
# Titanic EDA Dashboard

An interactive dashboard built with **Streamlit** and **Plotly** to explore the Titanic dataset.  
This project allows users to analyze survival patterns, relationships, and trends with a modern UI and sidebar navigation.  

---

## Features
- Interactive **sidebar menu** to select visualizations  
- **Dark theme** professional UI with clean layout  
- Explore relationships between **Age, Gender, Class, Fare, and Survival**  
- **Correlation heatmap** for numeric features  
- Key insights displayed alongside visuals  

---

## Tech Stack
- **Python 3.9+**  
- [Streamlit](https://streamlit.io/) 鈥� Web app framework  
- [Plotly](https://plotly.com/python/) 鈥� Interactive visualizations  
- [Seaborn](https://seaborn.pydata.org/) 鈥� Dataset access  
- [Pandas](https://pandas.pydata.org/) 鈥� Data manipulation  

---

##  Environment Setup

1. **Clone this repository** (or copy the files into a folder):  
   ```bash
   git clone https://github.com/your-username/titanic-eda-dashboard.git
   cd titanic-eda-dashboard
   ```

2. **Create a virtual environment** (recommended):  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Mac/Linux
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```
   If you dont have a `requirements.txt`, install directly:  
   ```bash
   pip install streamlit plotly seaborn pandas
   ```

---

##  How to Run

Run the Streamlit app:
```bash
streamlit run task2.py
```

Streamlit will open the dashboard in your default browser at:
```
http://localhost:8501
```

---

## Available Visualizations
- 鉁� Survival Count 
- 鉁� Survival by Gender 
- 鉁� Survival by Passenger Class 
- 鉁� Age Distribution & Boxplots 
- 鉁� Age vs Survival 
- 鉁� Fare Distribution
- 鉁� Survival by Embark Town 
- 鉁� Correlation Heatmap

---

##  Example Insights
- **Women** had a much higher survival rate than men.  
- **Higher-class passengers (Pclass 1)** had better survival chances.  
- **Children** tended to survive more.  
- **Higher fares** correlated with survival (wealthier passengers).  

---

## Project Structure
```
 task2.py         # Main Streamlit dashboard script
 README.md        # Project documentationnal)
` requirements.txt # Dependencies (optional)
`
