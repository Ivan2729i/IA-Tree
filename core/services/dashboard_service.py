from django.utils import timezone


MONTHS = [
    "Ene", "Feb", "Mar", "Abr", "May", "Jun",
    "Jul", "Ago", "Sep", "Oct", "Nov", "Dic",
]


def get_dashboard_data():
    now = timezone.localtime(timezone.now())

    current_month_index = now.month - 1
    previous_month_index = 11 if now.month == 1 else now.month - 2

    return {
        "metrics": {
            "total": 0,
            "current_month": 0,
            "previous_month": 0,
            "without_findings": 0,
            "with_findings": 0,
        },

        "period": {
            "year": now.year,
            "current_month": MONTHS[current_month_index],
            "previous_month": MONTHS[previous_month_index],
        },

        "monthly_evaluations": [
            {"month": month, "total": 0}
            for month in MONTHS
        ],

        "status_distribution": {
            "without_findings": 0,
            "with_findings": 0,
        },

        "recent_analyses": [],
    }

