<h1 align="center">Waifu Jack Bot</h1>

<div align="center">
    <img
        src="public/img/waifujack.jpeg"
        width="200"
        height="200"
        alt="Waifu Jack Bot Logo"
    >

[@waifujack_bot](https://telegram.me/waifujack_bot)

<a href="https://github.com/mathleite/waifujack_bot">
        <img src="https://github.com/mathleite/waifujack_bot/workflows/CI/badge.svg" alt="Workflow status badge">
</a>

Used with [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) package.

Our *Waifujack bot* can get any images for you :D
</div>

## Installing
You can install it easily with [Docker Compose](https://docs.docker.com/compose/):
```
~$ docker-compose up --build -d
```

## Start
Run *Waifujack bot* with:
```
~$ docker exec -it waifujack python3 __init__.py
```

### Tests
Run *tests* with:
```
~$ docker exec -it waifujack python3 -m unittest
```

## Commands
You can `search` everything you want with:
* **/search** *some* *image* *hd*
