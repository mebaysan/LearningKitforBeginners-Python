from django.shortcuts import render
from reports.forms import ProblemReportedForm, ReportForm
from reports.models import Report


# Create your views here.

def report_view(request, production_line):
    r_form = ReportForm()
    p_form = ProblemReportedForm()
    queryset = Report.objects.filter(production_line__name=production_line)
    context = {
        'r_form': r_form,
        'p_form': p_form,
        'object_list': queryset
    }
    return render(request, 'reports/report.html', context)
