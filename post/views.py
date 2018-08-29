from django.shortcuts import render
import xlrd, datetime
from .models import Post, Workshop, Workshift
from .form import DataForm

# Create your views here.


def index(request):
    return render(request, 'post/index.html')

#从excel一次过导入数据到数据库
def import_data(request):
    data = xlrd.open_workbook('post/g_data.xlsx')
    #选择要导入的工作表
    table = data.sheet_by_index(5)
    nrows = table.nrows
    ncols = table.ncols
    colnames = table.row_values(0)
    work_data=[]
    #导入的车间
    t_workshop=Workshop.objects.get(name='印刷车间')
    for i in range(2, nrows):
        row = table.row_values(i)
        #格式化日期
        date = str(int(row[0])) + '-' + str(int(row[1])) + '-' + str(int(row[2]))
        t_workshift=Workshift.objects.get(name=row[3])
        work_data.append(Post(date=date,workshop=t_workshop, workshift=t_workshift,
                         machine_num=row[4],order_num=row[5],
                         product_num=row[6],
                         product_units=int(row[7]),
                         waste_num=row[8],operator=row[9], remarks=row[10]))

    Post.objects.bulk_create(work_data)
    
#录入数据到数据库
def post_data(request):
    form = DataForm(request.POST)
    data_show = Post.objects.order_by('-create_time')[:5]
    test_flag = "pre"
    if request.method == "POST":
        if form.is_valid():
            test_flag = "good"
            a_date=form.cleaned_data['date'] 
            a_workshop=form.cleaned_data['workshop']         
            a_workshift=form.cleaned_data['workshift']      
            a_machine_num=form.cleaned_data['machine_num']
            a_order_num=form.cleaned_data['order_num']
            a_product_num=form.cleaned_data['product_num']
            a_product_units=form.cleaned_data['product_units']
            a_waste_num=form.cleaned_data['waste_num']
            a_operator=form.cleaned_data['operator']
            a_remarks=form.cleaned_data['remarks']            
            Post.objects.create(date=a_date,workshop=a_workshop,workshift=a_workshift,
                                  machine_num=a_machine_num,order_num=a_order_num,
                                  product_num=a_product_num,product_units=a_product_units,
                                  waste_num=a_waste_num,operator=a_operator,
                                  remarks=a_remarks)
        else:
            '''form = DataForm()'''
            error = form.errors
            test_flag = "bad"
    return render(request, 'post/post_data.html' ,locals())

#取数据并显示到页面
def data_table(request):
    data = Post.objects.all()
    return render(request, 'post/data.html', locals())

#图表化数据
def chart(request):
    #计算最近十日
    date_n_10 = date_cla()
    date_set = date_chart(date_n_10)
    #计算吹膜车间某日总产量
    n_day_sum = product_count(date_n_10,2)
    #计算吹膜车间各班次产量
    product_sum_mo= shift_count(date_n_10,2,1)    
    product_sum_ng = shift_count(date_n_10,2,2)
    product_sum_no = shift_count(date_n_10,2,3)    
    #计算制袋A车间某日总产量
    n_day_sum_c1 = product_count(date_n_10,4)
    #计算制袋B车间各班次产量
    product_sum_c1_mo= shift_count(date_n_10,4,1)    
    product_sum_c1_ng = shift_count(date_n_10,4,2)
    product_sum_c1_no = shift_count(date_n_10,4,3)    
    #计算制袋A车间某日总产量
    n_day_sum_c2 = product_count(date_n_10,4)
    #计算制袋B车间各班次产量
    product_sum_c2_mo= shift_count(date_n_10,4,1)    
    product_sum_c2_ng = shift_count(date_n_10,4,2)
    product_sum_c2_no = shift_count(date_n_10,4,3)   
    
    
    data = Post.objects.filter(order_num='AB001').order_by('-date')[:5]
    date1 = data[0].date.strftime('%y%m%d')
    date2 = data[1].date.strftime('%y%m%d')
    date3 = data[2].date.strftime('%y%m%d')
    date4 = data[3].date.strftime('%y%m%d')
    date5 = data[4].date.strftime('%y%m%d')
    data1 = int(data[0].product_num)
    data2 = int(data[1].product_num)
    data3 = int(data[2].product_num)
    data4 = int(data[3].product_num)
    data5 = int(data[4].product_num)
    return render(request, 'post/chart.html', locals())

#计算某个日期某车间的生产总量
def product_count(date,w_shop):
    sum_t = []
    date_t = []
    for i in range(len(date)):
        date_t.append(Post.objects.filter(date=date[i]).filter(workshop=w_shop))
    for j in range(len(date_t)):
        sum_s = 0
        for k in range(len(date_t[j])):
            sum_s += date_t[j][k].product_num
        sum_t.append(int(sum_s))
    '''
    data = Post.objects.filter(date=date).filter(workshop=w_shop)
    sum = 0
    for i in range(len(data)):
        sum += data[i].product_num
    '''
    return sum_t

#计算某车间，某班次的产量
def shift_count(date, w_shop, w_shift):
    date_t = []
    sum_t = []
    for j in range(len(date)):
        date_t.append(Post.objects.filter(date=date[j]).filter(workshop=w_shop,workshift=w_shift))
    for k  in range(len(date_t)):
        sum_s = 0
        for l in range(len(date_t[k])):
            sum_s += date_t[k][l].product_num
        sum_t.append(int(sum_s))
    '''
    data = Post.objects.filter(date=date).filter(workshop=w_shop,workshift=w_shift)
    sum = 0
    for i in range(len(data)):
        sum += data[i].product_num
    '''
    return sum_t

#计算最近十日,倒序
def date_cla():
    date_last_10 = []
    nearest_day = Post.objects.order_by('-date')[0].date
    date_last_10.append(nearest_day)
    for i in range(1,10):
        date_last_10.append(nearest_day + datetime.timedelta(-i))
    return date_last_10

#将日期转换成echart能识别的格式    
def date_chart(date_list):
    date = []
    for i in range(10):
        date.append(date_list[i].strftime('%y%m%d'))        
    return date

