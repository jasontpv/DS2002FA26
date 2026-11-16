# DS2002 — FastAPI on PythonAnywhere

A small app for the deploy lecture. Three routes:

| Method | Path | What it returns |
|--------|------|-----------------|
| GET | `/` | `{"message": "Hello from FastAPI"}` |
| GET | `/time` | The server clock, in UTC |
| GET | `/uva` | Latest Virginia men's game: opponent, score, and leaders in points, rebounds, steals, and blocks |

`/uva` reads Yahoo Sports with Beautiful Soup. The free PythonAnywhere account allows `sports.yahoo.com` and blocks ESPN.

1. `GET https://sports.yahoo.com/ncaab/teams/virginia/schedule/` for the latest game, the opponent, and the score.
2. `GET` that game's page and parse the Virginia table for points, rebounds, steals, and blocks.

## Run it on your laptop

```bash
./start.sh
```

Then open http://127.0.0.1:8000/docs

## Instructor account

Beginner account `ds2002jason` is confirmed for `jason@truepathvision.com`. The password, username, and API token are in `.env`, which git ignores.

The site is https://ds2002jason.pythonanywhere.com

- https://ds2002jason.pythonanywhere.com/ returns the hello JSON
- https://ds2002jason.pythonanywhere.com/time returns the UTC clock
- https://ds2002jason.pythonanywhere.com/docs is the Swagger page
- https://ds2002jason.pythonanywhere.com/uva reads the latest Virginia game from Yahoo Sports.

## Put it on PythonAnywhere

Beginner (free) account. Your username becomes the public host: `https://USERNAME.pythonanywhere.com` on the US site.

ASGI hosting is still beta. There is no static-file mapping. `/docs` works because FastAPI builds that page itself. The Web tab does not manage this site. You use the `pa` command, and you reload after every code change.

In a Bash console:

```bash
pip install --upgrade pythonanywhere
mkvirtualenv my_venv --python=python3.10
pip install "uvicorn[standard]" fastapi requests beautifulsoup4
mkdir -p ~/my_fastapi
```

Copy `main.py` to `~/my_fastapi/main.py`. Create an API token on the Account page so `pa` can log in. Then, with your real username in both places:

```bash
pa website create --domain USERNAME.pythonanywhere.com --command '/home/USERNAME/.virtualenvs/my_venv/bin/uvicorn --app-dir /home/USERNAME/my_fastapi --uds ${DOMAIN_SOCKET} main:app'
```

After you edit the file:

```bash
pa website reload --domain USERNAME.pythonanywhere.com
```

Open `/`, `/time`, and `/uva`, then `/docs`.

Logs, if a reload looks quiet: `/var/log/USERNAME.pythonanywhere.com.error.log`
