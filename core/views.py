from django.shortcuts import render
from .services.dashboard_service import get_dashboard_data
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    context = {
        "active_nav": "dashboard",
        "dashboard": get_dashboard_data(),
    }

    return render(request, "core/dashboard.html", context)

