from flask import Flask

app = Flask(__name__)

@app.route("/getscript")
def get_script():
    lua_script = """
-- noth
"""
    return lua_script, 200, {"Content-Type": "text/plain"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
