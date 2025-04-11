## 1. Overview

- **Project Name:** work in progress
- **Tech Stack:**
  - **Language:** Python 3.10 +
  - **Discord API:** `discord interaction`
  - **Flask:** For API communication
  - **Database:** MSSQL
  - **Hosting:** Raspbian on Raspberry Pi

---

## 2. System Architecture

- **High-Level Overview:**
    - Diagram:
    ```
    Discord Client ↔ Flask API ↔ Database
    ```
- **Bot Runtime:**
    - Runs on Raspberry Pi
    - Git pull + restart service for CI/CD
- **API Server:**
    - Flask server exposed via local IP only
    - Handles DB logic, isolated from bot logic

---

## 3. Modules / Folder Structure
subject to change
```lua
/bot
  |-- bot.py
  |-- game.py
  |-- commands/
  |     |-- battle.py
  |     |-- inventory.py
  |     |-- shop.py
  |-- utils/
  |     |-- enum.py
  |     |-- parser.py
  |     |-- lootgen.py
.env
```

Describe each main folder or module and its role.

---

## 4. Database Schema

- **Tables and Relations:**
# TODO: what does the schema look like

| Table         | Purpose                                                                                                    |
| ------------- | ---------------------------------------------------------------------------------------------------------- |
| `players`     | ID(pk),Discord snowflake ID, pstatID(fk), level, xp                                                        |
| `inventory`   | ID(pk), item 1(fk), item 2(fk), ...(fk), item 10(fk)                                                       |
| `equipment`   | ID(pk), head(fk), chest(fk), legs(fk), boots(fk), main hand 1(fk), main hand 2(fk), ring(fk), neckless(fk) |
| `items`       | item_ID(pk), name, type, Rarity, list of istatID(fk)                                                       |
| `Player stat` | pstatID(pk), ATK, DEF, SPD, HP, MP                                                                         |
| `item stat`   | istatID(pk), ATK, DEF, SPD, LSC, LS, MPC, list of AttributeID(AID)(fk)                                     |
| `attribute`   | AID(pk), name, value                                                                                       |

---

## 5. Key Systems & Logic

Break down the key systems:

### Combat System
- How turn-based combat is resolved
- Timeout handling
- Stat modifiers, crit chance logic, etc.

### Loot System
- Weighted RNG using `random.choices`
- Loot rarity logic → affects stat ranges
- Special affix probability (e.g., `1%` chance for a magic effect)

### XP/Leveling
- Based on D&D 5e XP thresholds
- XP reward formula = need to figure out

### Flask API
- Routes:
    - `POST /get_player`
    - `POST /battle_result`
- Only accessible via local IP

---

## 6. Environment / Deployment

- **Secrets:** Stored in `.env` (gitignored)
- **Dependencies:** Listed in `requirements.txt`
- **CI/CD Plan:** GitHub Actions CI &rarr; github webhook &rarr; pull to local &rarr; restart bot
- **Deployment Notes:**
    - On-prem bot + API
    - Uses `pm2` to ensure uptime

---

## 7. Security

- Bot token, DB passwords in `.env`
- Flask API accepts only local requests (127.0.0.1 or LAN IP)

---

## 8. TODOs / Technical Debt

- [ ] Add unit tests for loot generator
- [ ] Optimize stat balance
- [ ] Rate limit `/battle` command

---

## 9. Notes for Contributors

- Use Python 3.10 +
- Follow PEP8
- Run `black .` before commits
- Don’t push `.env` or actual token