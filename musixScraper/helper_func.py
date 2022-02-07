import aiohttp
import lxml.html

from constants import USER_AGENT_HEADER


async def parse_from_url(url: str) -> lxml.html.HtmlElement:
    """parses the resp.text()"""
    async with aiohttp.ClientSession(raise_for_status=True, headers=USER_AGENT_HEADER) as session:
        async with session.get(url) as resp:
            return lxml.html.document_fromstring(await resp.text())
