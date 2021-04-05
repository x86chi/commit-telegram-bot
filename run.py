import os

from commitTelegramBot import CommitTelegramBot

if os.path.exists('.env'):
    from dotenv import load_dotenv
    load_dotenv()


def get_env(key: str):
    value = os.getenv(key)

    if isinstance(value, str):
        return value

    raise ValueError(f'There is no environment variable named "{key}"')


environment_variables = (get_env('github_token'),
                         get_env('github_username'),
                         get_env('bot_token'),
                         get_env('chat_id'))

bot = CommitTelegramBot(*environment_variables)


def test_fetch():
    fetched = bot.fetch()
    for key in ['totalCommitContributions',
                'totalIssueContributions', 'totalPullRequestContributions']:
        assert isinstance(fetched[key], int)


def test_bot_run():
    bot.handler()


if __name__ == "__main__":
    bot.handler()