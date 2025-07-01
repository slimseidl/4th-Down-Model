# NFL 4th Down Decision-Making Tool

A data-driven web application that supports 4th down decision-making in the NFL using historical play-by-play data and a rules-based approach. This interactive tool helps users explore when teams *should* go for it on 4th down based on field position, distance to go, and historical success rates.

## 🔍 Project Overview

NFL coaches often face critical 4th down decisions that can influence game outcomes. This project explores historical 4th down play data to build an evidence-based decision support tool for "go-for-it" situations.

## 🛠️ Features

- Analyze 4th down conversion rates by distance and field position
- Use a binned decision table for recommendations
- Interactive Streamlit interface
- EPA comparison by play type (run/pass)
- Historical team tendencies & aggressiveness visualization

## 📊 Data Source

- **nflfastR**: [https://github.com/nflverse/nflfastR](https://github.com/nflverse/nflfastR)  
  Play-by-play data from previous 14 years was imported and filtered for 4th down attempts.



## ⚙️ Setup Instructions

1. **Clone the repository**

   bash:
   git clone https://github.com/slimseidl/NFL-4th-Down.git
   cd NFL-4th-Down

2. **Create Virtual Env (Recommended)**

    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3. **Install Reqs**
    pip install -r requirements.txt

4. **Run the App**
    streamlit run app/StreamlitApp.py
