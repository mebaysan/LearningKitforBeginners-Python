from django.shortcuts import render
from reports.forms import ProblemReportedForm, ReportForm


# Create your views here.

def report_view(request):
    r_form = ReportForm()
    p_form = ProblemReportedForm()
    context = {
        'r_form': r_form,
        'p_form': p_form
    }
    return render(request, 'reports/report.html', context)
