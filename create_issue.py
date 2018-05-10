import os
import asyncio
import aiohttp
from gidgethub.aiohttp import GitHubAPI


async def main():
    user = 'octaflop'
    repo = 'gbot'
    # issue_id = 1
    # user = 'mariatta'
    # repo = 'strange-relationship'
    # issue_id = 80
    # await add_issue(user, repo)
    # await comment_on_issue(user, repo, issue_id)
    # await react_issue(user, repo, issue_id)
    # await close_issue(user, repo, issue_id)
    issues = await get_issues(user, repo)
    print(issues)


async def add_issue(user, repo):
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, "octaflop", oauth_token=os.getenv("GH_AUTH"))
        await gh.post(f'/repos/{user}/{repo}/issues',
                      data={
                          'title': 'We got a problem ',
                          'body': 'Use more emoji!',
                      })


async def comment_on_issue(user, repo, issue_id):
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, "octaflop", oauth_token=os.getenv("GH_AUTH"))
        await gh.post(f'/repos/{user}/{repo}/issues/{issue_id}/comments',
                      data={
                          'body': 'Moi, aussie!',
                      })


async def react_issue(user, repo, issue_id):
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, "octaflop", oauth_token=os.getenv("GH_AUTH"))
        await gh.post(f'/repos/{user}/{repo}/issues/{issue_id}/reactions',
                      data={
                          'content': 'heart',
                      },
                      accept='application/vnd.github.squirrel-girl-preview+json')


async def close_issue(user, repo, issue_id):
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, "octaflop", oauth_token=os.getenv("GH_AUTH"))
        await gh.patch(f'/repos/{user}/{repo}/issues/{issue_id}',
                       data={
                           'state': 'closed',
                       })


async def get_issues(user, repo):
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, "octaflop", oauth_token=os.getenv("GH_AUTH"))
        url = f'/repos/{user}/{repo}/issues'
        print(url)
        issues = gh.getiter(url)
        return [i async for i in issues]


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
