from flask import Flask
import os

app = Flask(__name__)
APP_VERSION = os.environ.get('APP_VERSION', 'v2.0')

@app.route('/')
def home():
    return f'''
    <html><body style="font-family:Arial;text-align:center;padding:50px">
    <h1>🚀 CI/CD 실습 앱</h1>
    <h2>현재 버전: {APP_VERSION}</h2>
    <p>GitHub push → Actions → DockerHub → ArgoCD → Kubernetes!</p>
    </body></html>
    '''

@app.route('/health')
def health():
    return {'status': 'ok', 'version': APP_VERSION}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
