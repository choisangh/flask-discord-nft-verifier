import requests


class Discord:
    def __init__(self, config):
        self.CLIENT_ID = config.CLIENT_ID
        self.CLIENT_SECRET = config.CLIENT_SECRET
        self.API_URI = config.API_URI
        self.BOT_TOKEN = config.BOT_TOKEN
        self.DISCORD_ROLE_ID = config.DISCORD_ROLE_ID
        self.DISCORD_SERVER_ID = config.DISCORD_SERVER_ID

    @staticmethod
    def get_user_data(token):
        """
        사용자 정보 가져 오는 매서드
        :param token: 액세스 토큰
        :return: 사용자 정보
        """
        authorization = f'Bearer {token}'
        headers = {"Authorization": authorization, "accept": 'application/json'}
        r = requests.get('https://discord.com/api/users/@me', headers=headers)
        return r.json()

    def get_token(self, code, REDIRECT_URI):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        data = {
            'client_id': self.CLIENT_ID,
            'client_secret': self.CLIENT_SECRET,
            'code': code,
            'grant_type': 'client_credentials',
            'redirect_uri': REDIRECT_URI,
            'scope': 'identify'
        }
        r = requests.post('%s/oauth2/token' % self.API_URI, data=data, headers=headers)
        r.raise_for_status()
        return r.json()

    def add_role(self, user_id):
        """
        디스코드 봇을 통해 특정 사용자의 역할을 변경하는 매서드
        :param user_id: 유저의 디스코드 고유 아이디
        :param role_id: 역할의 고유 아이디
        :return:
        """
        headers = {"Authorization": f'Bot {self.BOT_TOKEN}'}
        url = self.API_URI + f'/guilds/{self.DISCORD_SERVER_ID}/members/{user_id}/roles/{self.DISCORD_ROLE_ID}'
        requests.put(url,
                     headers=headers)
