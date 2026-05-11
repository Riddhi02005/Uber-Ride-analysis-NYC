# 🚗 Uber NYC Ride Analysis — Data Analytics Project

![Python](https://img.shields.io/badge/Python-3.x-blue)
![PowerBI](https://img.shields.io/badge/PowerBI-Dashboard-yellow)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

## 📌 Project Overview
Analyzed **4.5 million+** Uber ride records from New York City (April–September 2014)
to uncover demand patterns, peak hours, high-demand locations, and growth trends —
simulating a real-world Uber data analyst workflow.

---

## 🎯 Key Objectives
- Identify **peak booking hours** and **busiest days**
- Analyze **high-demand geographic zones** in NYC
- Track **monthly ride growth** trends
- Build an **interactive Power BI dashboard** for business insights

---

## 📊 Key Insights Discovered
| Insight | Finding |
|--------|---------|
| 🕐 Peak Hour | 5PM – 6PM (Evening Rush) |
| 📅 Busiest Day | Thursday & Friday |
| 📈 Growth | 40%+ demand increase Apr → Sep |
| 📍 Hotspot | Midtown & Lower Manhattan |
| 🚗 Top Base | B02617 handled most dispatches |

---

## 🛠️ Tools & Technologies
| Tool | Purpose |
|------|---------|
| Python | Data cleaning & EDA |
| Pandas & NumPy | Data manipulation |
| Matplotlib & Seaborn | Static visualizations |
| Folium | Interactive maps & heatmaps |
| Power BI | Business intelligence dashboard |
| Jupyter Notebook | Development environment |

---

## 📁 Project Structure
```
uber-ride-analysis/
│
├── data/
│   ├── uber_cleaned.csv
│   └── uber_powerbi.csv
│
├── notebooks/
│   └── uber_analysis.ipynb
│
├── visuals/
│   ├── MASTER_DASHBOARD.png
│   ├── trips_by_hour.png
│   ├── trips_by_day.png
│   ├── trips_by_month.png
│   ├── heatmap_hour_day.png
│   ├── hourly_by_month.png
│   ├── daily_growth_timeline.png
│   ├── key_insights_card.png
│   ├── uber_heatmap.html
│   ├── peak_hour_map.html
│   └── hotspot_map.html
│
├── dashboard/
│   └── uber_dashboard.pbix
│
└── README.md
```

---

## 📸 Dashboard Preview
![Master Dashboard](visuals/MASTER_DASHBOARD.png)

---

## 🚀 How to Run
```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/uber-ride-analysis.git

# 2. Install dependencies
pip install pandas numpy matplotlib seaborn folium plotly jupyter

# 3. Open notebook
jupyter notebook notebooks/uber_analysis.ipynb
```

---

## 📚 Dataset
- **Source:** [Kaggle — Uber Pickups in NYC](https://www.kaggle.com/datasets/fivethirtyeight/uber-pickups-in-new-york-city)
- **Size:** 4.5M+ records
- **Period:** April – September 2014
- **Features:** DateTime, Latitude, Longitude, Base Code

---

## 👨‍💻 Author
**Your Name**
- LinkedIn: [your-linkedin](https://linkedin.com/in/your-profile)
- GitHub: [your-github](https://github.com/your-username)