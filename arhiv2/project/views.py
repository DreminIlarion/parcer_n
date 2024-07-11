import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .models import Komerc
from django.core.paginator import Paginator

import csv
import xlwt

def base(request):
    return render(request,'project/base.html')

def home(request):
    return render(request,'project/home.html')

def new(request):
    return render(request,'project/new.html')

def is_valid_q(param):
    return param != '' and param is not None

def nedv(request):
    date = Komerc.objects.all()
    

    title_forall_query = request.GET.get("title_forall")
    min_price_query = request.GET.get("min_price")
    max_price_query = request.GET.get("max_price")
    min_date_query = request.GET.get("min_date")
    max_date_query = request.GET.get("max_date")
    title_category = request.GET.get("category")
    title_appointment = request.GET.get("appointment")

    if is_valid_q(title_forall_query):
        date=date.filter(information__icontains=title_forall_query.strip())
    
    if is_valid_q(min_price_query):
        date= date.filter(price__gte=min_price_query)

    if is_valid_q(max_price_query):
        date= date.filter(price__lt=max_price_query)
    
    if is_valid_q(min_date_query):
        date= date.filter(datas__gte=min_date_query)

    if is_valid_q(max_date_query):
        date= date.filter(datas__lt=max_date_query)
    
    if is_valid_q(title_category) and title_category != 'Все':
        date= date.filter(category__icontains=title_category)

    if is_valid_q(title_appointment) and title_appointment != 'Все':
        date= date.filter(url__icontains=title_appointment)



    paginator = Paginator(date, 14)  # Show 10 contacts per page.
    
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
 
    context = {
        'page_obj':page_obj,
        'date':date,
    }
    return render(request,'project/nedv.html',context)


def get_obyav(request,obyav_id):

    obyav= Komerc.objects.get(pk=obyav_id)
    pohojee = Komerc.objects.filter(address__contains=f'{obyav.address[25:]}')

    context = {
        'obyav':obyav,
        'pohojee':pohojee,
    }
    return render(request,'project/objyav.html',context)


def export_to_exel(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Expenses' + str(datetime.datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Expenses')

    row_now = 0
    
    columns = ['Описание', 'Цена(₽/м^2)', 'Площадь(м^2)', 'Адресс', 'Дата публикации', 'url', 'Источник', 'Кадастровый номер', 'Фото']

    for col_nm in range(len(columns)):
        ws.write(row_now,col_nm,columns[col_nm])

    rows =  Komerc.objects.all().values_list('information', 'price', 'area', 'address', 'datas', 'url', 'category', 'cadastral_number', 'photo')

    for row in rows:
        row_now += 1

        for col_nm in range(len(row)):
            ws.write(row_now,col_nm, str(row[col_nm]))
    wb.save(response)

    return response


    # objav = Komerc.objects.all()
    # response = HttpResponse('text/csv')
    # response['Content-Disposition'] = 'attachment; filename=obyav.csv'
    # writer = csv.writer(response)
    # writer.writerow(['Описание', 'Цена', 'Площадь', 'Адресс', 'Дата публикации', 'url'])
    # objav_fields= objav.values_list('information', 'price', 'area', 'address', 'datas', 'url')
    # for objav in objav_fields:
    #     writer.writerow(objav)
    # return response

def register(request):
    date = Komerc.objects.all()
    

    title_forall_query = request.GET.get("title_forall")
    min_price_query = request.GET.get("min_price")
    max_price_query = request.GET.get("max_price")
    min_date_query = request.GET.get("min_date")
    max_date_query = request.GET.get("max_date")
    title_category = request.GET.get("category")
    title_appointment = request.GET.get("appointment")

    if is_valid_q(title_forall_query):
        date=date.filter(information__icontains=title_forall_query.strip())
    
    if is_valid_q(min_price_query):
        date= date.filter(price__gte=min_price_query)

    if is_valid_q(max_price_query):
        date= date.filter(price__lt=max_price_query)
    
    if is_valid_q(min_date_query):
        date= date.filter(datas__gte=min_date_query)

    if is_valid_q(max_date_query):
        date= date.filter(datas__lt=max_date_query)
    
    if is_valid_q(title_category) and title_category != 'Все':
        date= date.filter(category__icontains=title_category)

    if is_valid_q(title_appointment) and title_appointment != 'Все':
        date= date.filter(url__icontains=title_appointment)



    paginator = Paginator(date, 20)  # Show 10 contacts per page.
    
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
 
    context = {
        'page_obj':page_obj,
        'date':date,
    }
    return render(request, 'project/register.html',context)