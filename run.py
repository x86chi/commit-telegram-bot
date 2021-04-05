import os

from commitTelegramBot import CommitTelegramBot

if os.path.exists('.env'):
    from dotenv import load_dotenv
    load_dotenv()

environment_variables = [os.getenv('github_token'),
                         os.getenv('github_username'),
                         os.getenv('bot_token'),
                         os.getenv('chat_id')]

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
