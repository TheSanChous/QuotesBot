import aiohttp
import json

languages = {
    "ru": "ru",
    "en": "en",
}


class TranslationService:
    apiUrl = "https://dev-api.itranslate.com/translation/v2/"

    @staticmethod
    async def translate(text: str, to: str, _from: str = languages['en']):
        if len(text) < 80:
            return await TranslationService.translate_chunk(text, to, _from)

        result = ""
        chunk = ""
        for word in text.split():
            chunk += word
            if len(chunk) > 80 or word.endswith('.'):
                result = result + await TranslationService.translate_chunk(chunk, to, _from)
                chunk = ""
        return result

    @staticmethod
    async def translate_chunk(text: str, to: str, _from: str) -> str:
        async with aiohttp.ClientSession() as session:
            session.headers.add('Authorization', 'Bearer 603160b7-cee1-4c13-bcd7-37420b55211d')
            session.headers.add('Content-Type', 'application/json')
            async with session.post(TranslationService.apiUrl, data=json.dumps({
                "source": {
                    "dialect": _from,
                    "text": text
                },
                "target": {
                    "dialect": to
                }
            })) as res:
                if res.status is not 200:
                    raise Exception(await res.json())
                result = await res.json()
                return result['target']['text']
