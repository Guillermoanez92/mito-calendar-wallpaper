import json
import base64
from renderer.calendar import render_calendar


def main(request):
    try:
        # Support both GET and POST
        if request.method == "POST":
            body = json.loads(request.body or "{}")
        else:
            body = {}

        timezone = body.get("timezone", "America/Mexico_City")

        image_bytes = render_calendar(timezone)
        encoded = base64.b64encode(image_bytes).decode("utf-8")

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "image/png",
                "Content-Disposition": "inline; filename=calendar.png",
            },
            "body": encoded,
            "isBase64Encoded": True,
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "text/plain"},
            "body": str(e),
        }
