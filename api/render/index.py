import json
from renderer.calendar import render_calendar


def main(request):
    try:
        body = json.loads(request.body or "{}")
        timezone = body.get("timezone", "America/Mexico_City")

        image_bytes = render_calendar(timezone)

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "image/png"
            },
            "body": image_bytes,
            "isBase64Encoded": False,
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "text/plain"},
            "body": f"Error: {str(e)}",
        }
