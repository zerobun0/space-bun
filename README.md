# Space Bun

Arcade space shooter built with HTML5 Canvas.

## Play Online

GitHub Pages live URL:

https://zerobun0.github.io/space-bun/

## Features

- No login required
- Persistent local save using browser storage
- Optional online account (email/password)
- Optional online leaderboard and cloud best-score sync
- Campaign mode with 10 levels
- Survival mode with endless scaling
- Easy and Hard difficulty options
- Random drops and perks:
  - Tri-Shot
  - Rapid Fire
  - Shield
  - Repair
  - Extra Life
  - Shockwave Bomb

## Controls

- Move: WASD or Arrow Keys
- Aim: Mouse
- Shoot: Hold Left Click

## Local Development

Simple static run (recommended):

```bash
python -m http.server 8000
```

Then open:

http://localhost:8000

Optional Streamlit wrapper run:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Online Scoring Setup (Firebase)

This project now supports optional online accounts and leaderboard.

Password reset is intentionally not implemented: if a user forgets the password,
they must create a new account.

1. Create a Firebase project.
2. Enable Authentication > Email/Password.
3. Create Firestore database.
4. Open `index.html` and fill `FIREBASE_CONFIG` with your Firebase web config.
5. Deploy again to GitHub Pages.

Expected Firestore collection:

- `spacebun_users`

Each document key is the Firebase Auth `uid`, with fields like:

- `email`
- `campaignBest`
- `survivalBest`
- `maxLevelReached`
- `combinedBest`

Suggested Firestore rules for basic write protection by signed-in user:

```txt
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /spacebun_users/{userId} {
      allow read: if true;
      allow write: if request.auth != null && request.auth.uid == userId;
    }
  }
}
```

## Deploy To GitHub Pages

1. Push to `main` branch on `zerobun0/space-bun`.
2. In GitHub repo settings, open Pages.
3. Set source to `Deploy from a branch`.
4. Select branch `main` and folder `/ (root)`.
5. Save.

After publish, the game is available at:

https://zerobun0.github.io/space-bun/

## Project Files

- `index.html` - game UI and gameplay logic
- `app.py` - optional Streamlit wrapper
- `requirements.txt` - optional Python dependencies for Streamlit run
