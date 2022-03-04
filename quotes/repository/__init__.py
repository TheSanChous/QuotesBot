import json

import aiohttp

from quotes.repository.quote import Quote
from data.config import QUOTES_TOKEN


class QuotesRepository:
    apiUrl = "https://favqs.com/api/"
    quoteOfTheDay = "qotd/"
    findFilter = "quotes/?filter={0}&page={1}"
    findTag = "quotes/?filter={0}&type=tag&page={1}"
    getQuote = "quotes/"

    @staticmethod
    async def get_random() -> Quote:
        async with aiohttp.ClientSession() as session:
            session.headers.add('Authorization', f'Token token="{QUOTES_TOKEN}"')
            async with session.get(QuotesRepository.apiUrl+QuotesRepository.quoteOfTheDay) as response:
                squote = await response.text()
                return Quote(json.loads(squote)['quote'])