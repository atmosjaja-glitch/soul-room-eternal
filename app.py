import threading
from flask import Flask, render_template
import backup

app = Flask(__name__)

@app.route("/")
def chat():
    return render_template("chat.html")

if __name__ == "__main__":
    # Run backup in background
    threading.Thread(target=backup.run_backup, daemon=True).start()
    print("☁️ Backup started in background...")
    app.run(debug=True)
