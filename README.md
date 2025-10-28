# CPS Counter

I made this simple desktop application in order to get started with the PyQt5 library as part of the Human-Computer Interaction (HCI) course in semester 5.  
The python script allows you to measure your **clicks per second (CPS)** within a fixed time window.

## 🧪 Features

- Measures how many times you can click a button within a set duration (`seconds_limit`, default **5 seconds**).  
- Displays a **real-time timer** and **CPS counter** while you are clicking.  
- Shows your **final CPS** with a short commentary once the time is over :
  - Below **7 CPS** : "It’s very bad, to be honest..."   
  - Between **7 and 10 CPS** : "It’s good, but I’m sure you can do better !"  
  - Above **10 CPS** : "Great job !"  
- Includes a **Retry** button to easily restart the test.

## 🖥️ Technologies

- **Language :** Python  
- **Framework :** PyQt5  
- **Platform :** Cross-platform (Windows, Linux, macOS)

## 🚀 Getting Started

### Prerequisites

Make sure Python and PyQt5 are installed.

```bash
pip install PyQt5
```

### Run the App

Clone this repository and launch the program:

```bash
git clone https://github.com/samdmn/cps-counter.git
cd cps-counter
python main.py
```

### ⚙️ Customization

You can easily modify :

`seconds_limit` in `MainWindow.__init__()` to change the test duration.

**Colors, fonts, or layout** by editing the `setStyleSheet()` sections.

**Feedback messages** in the `commentary()` method.

## ✅ Why Use This?

Fun little application to test your click speed (if you play Minecraft you may already be familiar with this).

Can be expanded into more complex projects (games, tests, etc.).