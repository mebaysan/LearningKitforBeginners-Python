from django.shortcuts import render
from reports.forms import ProblemReportedForm, ReportForm
from reports.models import Report


# Create your views here.

def report_view(request, production_line):
    r_form = ReportForm(request.POST or None)
    p_form = ProblemReportedForm(request.POST or None)
    queryset = Report.objects.filter(production_line__name=production_line)

    if p_form.is_valid():
        print(request.POST)

    context = {
        'r_form': r_form,
        'p_form': p_form,
        'object_list': queryset
    }
    return render(request, 'reports/report.html', context)
