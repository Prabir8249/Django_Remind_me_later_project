from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Reminder
import json
from datetime import datetime

@csrf_exempt
def reminder(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        date = data.get('date')
        time = data.get('time')
        message = data.get('message')
        method = data.get('method')

        # Convert date and time to datetime object
        reminder_time = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")

        # Create a new reminder
        new_reminder = Reminder(time=reminder_time, message=message, method=method)
        new_reminder.save()

        return JsonResponse({"message": "Reminder created successfully."}, status=201)

    else:
        return JsonResponse({"error": "Invalid request method."}, status=400)
