from flask import Flask, request, jsonify
from flask_cors import CORS


def create_app() -> Flask:
    app = Flask(__name__)
    # In dev, Vite proxy handles CORS, but allow CORS for flexibility
    CORS(app)

    @app.get("/api/health")
    def health() -> tuple[dict, int]:
        return {"status": "ok"}, 200

    @app.post("/api/generate-fyp-ideas")
    def generate_fyp_ideas():
        payload = request.get_json(silent=True) or {}
        profile = payload.get("profile", {})

        # Placeholder logic: echo back simple structured ideas/resources.
        # Replace with your actual generation logic or database calls.
        interest = (profile.get("interest") or "").strip()
        field_of_study = (profile.get("fieldOfStudy") or "").strip()

        sample_ideas = [
            {
                "id": "idea-1",
                "title": f"{field_of_study} Capstone around {interest or 'emerging tech'}",
                "description": "Design and evaluate a prototype demonstrating core concepts.",
                "difficulty": "intermediate",
                "category": "capstone",
                "requiredSkills": ["research", "documentation", "presentation"],
                "potentialImpact": "Showcases applied knowledge and portfolio readiness.",
            }
        ]

        sample_resources = [
            {
                "id": "res-1",
                "title": "Project Planning Template",
                "type": "tool",
                "url": "https://example.com/template",
                "description": "A template to plan milestones, deliverables, and risks.",
                "relevance": 0.8,
            }
        ]

        return jsonify({"ideas": sample_ideas, "resources": sample_resources})

    return app


if __name__ == "__main__":
    # Default dev server at http://localhost:5000
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)


