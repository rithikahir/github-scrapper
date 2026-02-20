# GitHub Profile Scraper using Playwright (Python)

## 📌 Assignment Overview

This project is a browser automation script built with **Playwright (Python)** that scrapes public profile information from a GitHub user page and stores the extracted data into a **Supabase** database.

⚠️ The GitHub API is **not used**. All data is collected by automating the browser and extracting information from the DOM.

---

## 🚀 Features

- Automates Chromium browser using Playwright
- Scrapes GitHub profile details:
  - Username
  - Name (if available)
  - Bio (if available)
  - Followers count
  - Following count
  - Number of repositories

- Stores data into Supabase table
- Handles optional fields safely

---

## 🛠️ Tech Stack

- Python
- Playwright (Browser Automation)
- Supabase (Database)

---

## 📂 Project Structure

```
github-scraper/
│
├── main.py          # Main scraper script
├── .gitignore
├── README.md
└── venv/            # Virtual environment (ignored)
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```
git clone <your-repo-url>
cd github-scraper
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies

```
pip install playwright supabase python-dotenv
playwright install
```

### 4️⃣ Environment Variables

Create a `.env` file in the root folder:

```
SUPABASE_URL=your_project_url
SUPABASE_KEY=your_anon_key
```

---

## ▶️ How To Run

```
python main.py
```

When executed:

- Browser opens automatically
- Profile data is scraped
- Data is inserted into Supabase table

---

## 🗄️ Supabase Table Structure

```
create table github_profiles (
  id uuid default uuid_generate_v4() primary key,
  username text,
  name text,
  bio text,
  followers text,
  following text,
  repositories text
);
```

---

## ✅ Assumptions Made

- Target GitHub profile is public.
- GitHub UI selectors remain stable.
- Some fields like `name` or `bio` may be empty.

---

## 🔮 Possible Improvements

- Add error handling and retry logic
- Convert follower counts to integers
- Support scraping multiple profiles
- Add logging system
- Dockerize the application

---

## 👨‍💻 Author

Rithik

# github-scrapper
