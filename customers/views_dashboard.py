from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta

from .models import Customer

def dashboard(request):
    # Timeframe selection (default: last 30 days)
    timeframe_days = int(request.GET.get("days", 30))
    since = timezone.now() - timedelta(days=timeframe_days)

    total_customers = Customer.objects.count()
    new_signups = Customer.objects.filter(date_joined__gte=since).count()

    context = {
        "total_customers": total_customers,
        "new_signups": new_signups,
        "timeframe_days": timeframe_days,
    }
    return render(request, "customers/dashboard.html", context)