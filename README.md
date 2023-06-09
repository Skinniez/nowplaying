# Discord Spotify Song Announcer Bot

A simple Discord bot that announces the currently playing song on Spotify.

## Prerequisites

- Python 3.6 or higher
- A Discord bot token

## Dependencies

- discord.py
- python-dotenv
- pywin32
- pypiwin32

You can install these dependencies by running:

```bash
pip install -r requirements.txt` 

## Setup

1.  Clone or download this repository.
    
2.  Create a `.env` file in the same directory as the bot script (`songbot.py`). Add your Discord bot token in the file:
    

`DISCORD_TOKEN=your_bot_token_here` 

Replace `your_bot_token_here` with your actual Discord bot token.

3.  Install the required dependencies using the command mentioned in the "Dependencies" section.

## Usage

To start the bot, run the following command in your terminal or command prompt:

bashCopy code

`python songbot.py` 

The bot will now be online and ready to announce the currently playing song on Spotify.

### Commands

-   `!song`: The bot will announce the currently playing song on Spotify.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
