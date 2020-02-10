from aiohttp import ClientSession


class Core:
    def __init__(self):
        self.endpoint = "https://www.wikidata.org/w/api.php"

    async def get_entity_number_by_query(self, query: str, language='ru'):
        params = {
            'action': 'wbsearchentities',
            'format': 'json',
            'language': language,
            'search': query
        }

        async with ClientSession() as session:
            async with session.get(self.endpoint, params=params) as response:
                response = await response.json()

        return response.json()['search'][0]['id']

    async def get_entity_info(self, entity_number):
        params = {
            'action': 'wbgetentities',
            'format': 'json',
            'ids': entity_number,
            'sites': 'ruwiki'
        }

        async with ClientSession() as session:
            async with session.get(self.endpoint, params=params) as response:
                response = await response.json()

        return response['entities'][entity_number]


if __name__ == '__main__':
    core = Core()
    res = await core.get_entity_number_by_query('Серж Танкиян')

