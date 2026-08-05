from django.shortcuts import render, redirect
from vuva_admin.models import Event, Missionary
from vuva_missionary.models import (
    MissionaryPrayerRequest,
    MissionaryReport
)

# =========================
# Missionary Home
# =========================
def missionary_home(request):

    missionary_id = request.session.get('missionary_id')

    if not missionary_id:
        return redirect('login')

    missionary = Missionary.objects.get(id=missionary_id)

    return render(request, 'missionary_home.html', {
        'missionary': missionary
    })


# =========================
# Events Page
# =========================
def vuva_events(request):
    events = Event.objects.all().order_by('-created_at')
    return render(request, 'vuva_events.html', {'events': events})


# =========================
# Prayer Request
# =========================
def missionary_prayer_requests(request):

    missionary_id = request.session.get('missionary_id')

    if not missionary_id:
        return redirect('login')

    missionary = Missionary.objects.get(id=missionary_id)

    if request.method == 'POST':
        prayer_text = request.POST.get('request')

        if prayer_text:
            MissionaryPrayerRequest.objects.create(
                missionary=missionary,
                request=prayer_text
            )
            return redirect('missionary_prayer_requests')

    return render(request, 'missionary_prayer_requests.html', {
        'missionary': missionary
    })


# =========================
# REPORT UPLOAD (MAIN PART)
# =========================
def missionary_reports(request):

    missionary_id = request.session.get('missionary_id')

    if not missionary_id:
        return redirect('login')

    missionary = Missionary.objects.get(id=missionary_id)

    if request.method == "POST":

        report_file = request.FILES.get('report_file')

        if report_file:
            MissionaryReport.objects.create(
                missionary=missionary,
                report_file=report_file
            )

            return redirect('missionary_reports')

    return render(request, 'missionary_reports.html', {
        'missionary': missionary
    })


# =========================
# Logout
# =========================
def missionary_logout(request):
    request.session.flush()
    return redirect('login')