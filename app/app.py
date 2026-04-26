from flask import Flask, render_template_string
import psutil
import datetime

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Status Board</title>
    <style>
        body { font-family: monospace; background: #0d1117; color: #58a6ff; padding: 40px; }
        h1 { color: #f0f6fc; }
        .stat { background: #161b22; padding: 15px; margin: 10px 0; border-radius: 6px; }
        .label { color: #8b949e; }
    </style>
</head>
<body>
    <h1>🖥️ DevOps Status Board</h1>
    <div class="stat"><span class="label">CPU Usage:</span> {{ cpu }}%</div>
    <div class="stat"><span class="label">RAM Usage:</span> {{ ram }}%</div>
    <div class="stat"><span class="label">Disk Usage:</span> {{ disk }}%</div>
    <div class="stat"><span class="label">Uptime Since:</span> {{ uptime }}</div>
</body>
</html>
"""

@app.route("/")
def index():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    uptime = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    return render_template_string(HTML, cpu=cpu, ram=ram, disk=disk, uptime=uptime)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
