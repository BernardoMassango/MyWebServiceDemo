from flask import Flask, jsonify, request

app = Flask(__name__)

# Root
@app.route("/")
def hello():
    return "Hello from Safety Condition Tracker - Hello World"

# 1. Configuração
@app.route("/config", methods=["GET"])
def config():
    return jsonify({
        "activity_name": "Safety Condition Tracker",
        "version": "1.0",
        "description": "Registo de condições inseguras"
    })

# 2. Parâmetros
@app.route("/json-params", methods=["GET"])
def json_params():
    return jsonify({
        "frequency": "daily",
        "max_reports_per_user": 5,
        "allow_photos": True,
        "enable_notifications": True
    })

# 3. Deploy
@app.route("/deploy", methods=["POST"])
def deploy():
    data = request.get_json(silent=True)
    return jsonify({
        "status": "ok",
        "message": "Activity deployed successfully",
        "received": data
    })

# 4. Analytics disponíveis
@app.route("/analytics-list", methods=["GET"])
def analytics_list():
    return jsonify([
        {
            "id": "reports_submitted",
            "description": "Número de relatórios submetidos"
        },
        {
            "id": "active_users",
            "description": "Número de utilizadores ativos"
        }
    ])

# 5. Pedido de analytics
@app.route("/analytics", methods=["GET", "POST"])
def analytics():
    return jsonify({
        "reports_submitted": 12,
        "active_users": 5
    })

# Health check (opcional, mas útil)
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

