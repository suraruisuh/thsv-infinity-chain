# 🤖 THSV Infinity Chain

THSV Infinity Chain is a modular, Python-based Discord bot designed to bring life to your server with engaging number-based games, utility functions, and a rich leaderboard system. Built for community fun, friendly competition, and long-term growth.

---

## 🚀 Features

- **Modular Architecture** for maintainability and scalability
- **MongoDB Integration** (configurable for MySQL)
- **Detailed Logging System**
  - `LOG_CHANNEL`: Syncs & checks
  - `ERROR_CHANNEL`: Detailed errors
  - `STATUS_CHANNEL`: Online/offline/restart
- **Line-by-Line Code Comments** for maximum clarity
- **Utility Tools**:
  - Calculator
  - Role Verification System
  - Message Deletion

---

## 🎮 Included Games

### 1. Brain Count (Start Here)
**Count from 1 to ∞ using math expressions.**

- Start with 1 (only number allowed directly)
- Every next number must be a math expression
- No back-to-back turns
- Mistakes reset the chain

```txt
User1: 1
User2: 1+1 ✅
User3: 6/2 ✅
User3 again: 2*2 ❌ (Same user twice!)
```

> **Leaderboard Support**: Longest chain, most valid entries, fastest input, guild rankings

---

### 2. 24 Game
**Use 4 numbers and basic math to make 24.**

- Each number used once
- Use + − × ÷ and parentheses

```txt
Bot: 3, 8, 3, 8
User: 8 / (3 - 8/3) = 24 ✅
```

---

### 3. Math Dice
**Reach target number using dice values and operations.**

```txt
Bot: Target: 21 | Dice: 3, 2, 5
User: (5×3)+2 = 17
```

---

### 4. Countdown Numbers Game
**Use 6 numbers to get close to a random target (100–999).**

```txt
Bot: 3, 7, 25, 10, 100, 4 | Target: 952
User: ((10+100)×7)+(3×4) = 952 ✅
```

---

### 5. Numberle / Nerdle
**Guess the hidden math equation in 6 tries.**

- Equation must be valid and use `=`
- Emoji feedback after each guess

```txt
Bot: 5+5+5=15
Bot: ❌ ⚠️ ✅ ✅ ❌ ⚠️ ⚠️ ✅
```

---

### 6. Futoshiki Puzzle
**Grid-based logic puzzle with inequality constraints.**

```txt
Bot: A1 < A2
User: place 3 at A1 ✅
```

> Note: Visual formatting or embedded image rendering may be added in future.

---

## 📊 Leaderboards & Stats

- **Paginated Displays**
- **Streaks & Icons** (🔥 for longest chains)
- **Filters** (Daily/Weekly/All-Time)
- **Server & Global Rankings**
- **Player Stats** via `/mystats`
- **Challenges**: 1v1s to climb the ranks
- **Custom Titles** & Emoji Flairs

---

## 🛠 Setup & Deployment

1. **Clone Repo**
```bash
git clone https://github.com/YourName/THSV-Infinity-Chain.git
```

2. **Install Requirements**
```bash
pip install -r requirements.txt
```

3. **Set Up MongoDB**
- Recommended for game data and flexible storage
- Or configure for MySQL (optional)

4. **Add Bot Token & Channel IDs**
- Configure `.env` file or `config.json`

5. **Deploy to PebbleHost**
- Upload your code and install dependencies
- Use screen or systemd to keep bot running

---

## 🧭 Recommended Development Roadmap

| Phase      | Games to Launch           | Why                                    |
|------------|----------------------------|-----------------------------------------|
| Phase 1    | ✅ Brain Count            | Low complexity, high engagement         |
| Phase 2    | ➕ 24 Game / Math Dice    | Mid-tier logic, adds variety            |
| Phase 3    | 🔢 Countdown Game        | More depth, requires scoring logic      |
| Advanced   | 🧩 Numberle & Futoshiki  | Rich logic, solo/co-op puzzle experience|

---

## 📄 License
MIT — Free to use, modify, and improve. Give credit if you fork or deploy publicly.

---

## 💬 Contact & Contributions
Want to contribute, report bugs, or suggest games? Open an issue or create a pull request.

Built with ❤️ by Surakage
