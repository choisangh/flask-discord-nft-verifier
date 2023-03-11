from flask import Flask, render_template, request
from discordmanager import Discord
from web3manager import Web3Manager
from config import DiscordConfig, WebConfig, Web3Config

app = Flask(__name__, template_folder="template", static_folder="static")
discord = Discord(DiscordConfig)
web3_manager = Web3Manager(Web3Config)


@app.route('/')
def index():
    code = request.args.get('code')
    token_json = discord.get_token(code, WebConfig.REDIRECT_URI)  # access 토큰
    user_json = discord.get_user_data(token_json['access_token'])
    return render_template('index.html', discordId=user_json['id'])


@app.route('/verify', methods=['POST'])
def verify_post():
    # POST request에서 Discord ID, 서명값, 지갑 주소를 가져오기
    discord_id = request.form.get('discordid')
    signature = request.form.get('signature')
    wallet_address = request.form.get('wallet')
    message = request.form.get('message')
    print(f"discord_id : {discord_id}")
    print(f"signature : {signature}")
    print(f"wallet_address : {wallet_address}")
    print(f"message : {message}")
    # # Discord ID와 서명값을 확인하고, 서명 검증에 성공하면 인증 정보를 저장

    # 서명 검증 수행
    is_verified = web3_manager.verify_signature(message, signature, wallet_address)
    if not is_verified:
        return 'Signature verification failed', 400

    # 검증에 성공하면 Discord 봇에서 해당 사용자에게 역할 부여
    discord.add_role(discord_id)
    return 'Verification success', 200


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded=True)