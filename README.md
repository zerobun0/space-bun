# Space Bun

Arcade space shooter built with HTML5 Canvas and wrapped in Streamlit for easy hosting.

## Features

- No login required.
- Persistent local save using browser storage.
- Campaign mode with 10 levels.
- Survival mode with endless scaling.
- Easy and Hard difficulty options.
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

## Run Locally

1. Create and activate a Python virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start app:

```bash
streamlit run app.py
```

4. Open http://localhost:8501 (or the URL shown by Streamlit).

## Deploy To Streamlit Community Cloud

1. Push this repo to GitHub.
2. In Streamlit Community Cloud, create a new app from this repository.
3. Set main file path to `app.py`.
4. Deploy.

Suggested repository name: `space-bun`.

After deploy finishes, Streamlit gives you a public URL you can share with friends.

## Project Files

- `index.html` - game UI and gameplay logic.
- `app.py` - Streamlit wrapper that serves the game.
- `requirements.txt` - Python dependencies.
