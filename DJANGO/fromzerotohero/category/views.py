from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import csv
from django.http import HttpResponse
from category.models import Category


@login_required(login_url="/login")
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="categories.csv"'
    categories = Category.objects.all()
    writer = csv.writer(response)
    writer.writerow(['Category Name', 'Category Count'])
    for cat in categories:
        writer.writerow([cat.name, cat.count])
    return response


@login_required(login_url='/login')
def import_csv(request):
    if request.method == "POST":
        csv_file = request.FILES.get('csv_file')
        if not csv_file.name.endswith('.csv'):
            error = "Please add 'CSV' File!"
            link = request.META.get('HTTP_REFERER')
            context = {
                'error': error,
                'link': link
            }
            return render(request, 'back/error.html', context=context)
        file_data = csv_file.read().decode('utf-8')
        lines = file_data.split("\n")  # alt satıra \n ile geçer
        lines.pop(0)  # burada biz gelen csv'de ilk satırda kolon isimleri olduğundan listeden çıkardık
        lines.pop(len(lines) - 1)  # son eleman '' döndüğünden çıkardık
        for line in lines:
            fields = line.split(',')  # yan yana kolonlar birbirinden ',' ile ayrılır
            try:
                if len(Category.objects.filter(name=fields[0])) == 0:  # eğer o isimde bir kategori yoksa
                    cat = Category(name=fields[0], count=0)
                    cat.save()
            except:
                print("exception!!!")
    return redirect('panel:category_list')
