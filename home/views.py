from django.shortcuts import render
from .models import Heartbeat, HeartbeatCount

def live_heartbeat_view(request):
    data = []
    heartbeats = Heartbeat.objects.all().order_by('-date')[:50]  # فقط ۵۰ تا آخر

    for hb in heartbeats:
        try:
            count = HeartbeatCount.objects.get(rate_id=hb.id)
            count_number = count.heartbeats_count_number
        except HeartbeatCount.DoesNotExist:
            count_number = 0

        data.append({
            'user_id': hb.user_id,
            'date': hb.date,
            'heart_beats': hb.heart_beats,
            'heartbeats_count_number': count_number,
        })

    return render(request, 'home/live_heartbeat.html', {'data': data})
