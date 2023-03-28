from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '𝐒𝐢𝐭𝐮𝐌𝐨_𝐌𝐝𝐢𝐬𝐤_𝐁𝐨𝐭𝐬'


if __name__ == "__main__":
    app.run()
