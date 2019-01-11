from django.shortcuts import render, redirect, HttpResponse
from .forms import TestForm, ShippingForm, ShippingArrForm, DeliverForm
from .models import Post

# Create your views here.

rows = (
    ("y", "y", "y", "y", "y", "n", "y", "y", "y", "n", "y", "y", "y", "y", "y", "y", "y",),
    ("y", "y", "y", "y", "y", "y", "y", "n", "y", "y", "y", "y", "n", "y", "y", "y", "y",),
    ("y", "y", "y", "y", "y", "n", "y", "y", "y", "y", "y", "y", "y", "y", "n", "n", "n",),
    ("y", "y", "y", "y", "y", "n", "n", "y", "y", "n", "y", "n", "y", "y", "y", "n", "n",),
    ("y", "y", "y", "y", "y", "y", "n", "y", "y", "y", "n", "y", "n", "y", "y", "n", "n",),
    ("y", "y", "y", "y", "y", "n", "y", "y", "y", "y", "y", "n", "y", "n", "y", "n", "n",),
    ("y", "y", "y", "y", "y", "y", "n", "n", "y", "n", "n", "y", "n", "y", "n", "n", "n",),
    ("y", "y", "y", "y", "y", "n", "n", "n", "y", "n", "n", "n", "n", "y", "n", "n", "n",),
    ("y", "y", "y", "y", "y", "n", "y", "n", "n", "y", "n", "y", "n", "y", "n", "n", "n",),
    ("y", "y", "y", "y", "y", "y", "n", "y", "n", "n", "n", "n", "n", "n", "y", "n", "n",),
)
rows_perc = (85, 85, 85, 85, 80, 80, 50, 50, 30, 30,)
valves = [
    ["#1", "3 w", "10.000€", ],
    ["#2", "2 w", "12.000€", ],
    ["#3", "1 w", "14.000€", ],
    ["#4", "2.5 w", "18.000€", ],
    ["#5", "2 w", "12.000€", ],
    ["#6", "1 w", "15.000€", ],
    ["#7", "0.5 w", "5.000€", ],
    ["#8", "1.5 w", "3.000€", ],
    ["#9", "1 w", "2.000€", ],
    ["#10", "3 w", "1.000€", ],
]
downloads = {
    '0': '2D.dwg',
    '1': '2D.dxf',
    '2': '3D.igs',
    '3': '3D.pdf',
    '4': '3D.stp',
    '5': 'DataSheet.pdf',
    '6': 'ITP.pdf',
    '7': 'Pressure_Test.jpg',
}
shippings_labels = [
    "Shipping Method",
    "Shipping Arrangement",
    "Payment Terms",
]


def home(request):
    Post.objects.all().delete()
    if request.method == 'POST':
        my_form = TestForm(request.POST)
        context = {
            "form": my_form,
        }
        if my_form.is_valid():
            my_form.save()
        return redirect('result')
    else:
        my_form = TestForm()
        context = {
            "form": my_form,
        }
        return render(request, 'home.html', context)

def result(request):
    red = []
    green = []
    colorz = []
    for row in rows_perc:
        if row <= 50:
            red.append(hex(15))
            green.append(hex(int(row*0.3)))
        else:
            green.append(hex(15))
            red.append(hex(int((100-row)*0.3)))
    for i in range(0, len(red)):
        red[i] = red[i].replace('0x', '')
        green[i] = green[i].replace('0x', '')
        colorz.append('#' + red[i] + green[i] + '0')
    for idx, valve in enumerate(valves):
        valve.append(str(rows_perc[idx]) + "%")
        valve.append(colorz[idx])
    my_form = TestForm()
    context = {
        'form': my_form,
        'rows': rows,
        'valves': valves,
    }
    if request.GET.get('buybtn'):
        request.session['buy_choice'] = request.GET.get('buybtn')
        return redirect('valve')
    else:
        return render(request, 'result.html', context)

def valve(request):
    results = []
    paramz = []
    checks = []
    check_style = []
    my_form = TestForm()
    for ob in my_form:
        paramz.append(ob.label)
    posts = Post.objects.all()
    post = posts[0]
    for attr, value in post.__dict__.items():
        results.append(value)
    del results[0]
    del results[0]
    buy_choice = request.session.get('buy_choice')
    checks = rows[int(buy_choice)]
    buy_perc = str(rows_perc[int(buy_choice)]) + '%'
    for ob in checks:
        if ob == 'y':
            check_style.append('btn-success')
        else:
            check_style.append('btn-danger')
    zipped = list(zip(paramz, results, check_style))
    context = {
        'zipped': zipped,
        'buy_perc': buy_perc,
        'downloads': downloads,
    }
    return render(request, 'valve.html', context)

def contact(request):
    buy_choice = request.session.get('buy_choice')
    buy_perc = str(rows_perc[int(buy_choice)]) + '%'
    context = {
        'buy_perc': buy_perc,
    }
    return render(request, 'contact.html', context)

def shipping(request):
    if request.method == 'POST':
        product = Post.objects.all()[0]
        product.shipping = request.POST['shipping']
        product.save(update_fields=['shipping'])
        return redirect('shipping_arrangement')
    else:
        my_form = ShippingForm()
        context = {
            "form": my_form,
        }
    return render(request, 'shipping.html', context)

def shipping_arrangement(request):
    if request.method == 'POST':
        product = Post.objects.all()[0]
        product.shipping_arr = request.POST['shipping_arr']
        print(product.save(update_fields=['shipping_arr']))
        return redirect('deliver')
    else:
        my_form = ShippingArrForm()
        context = {
            "form": my_form,
        }
    return render(request, 'shipping_arrangement.html', context)

def deliver(request):
    if request.method == 'POST':
        product = Post.objects.all()[0]
        product.deliver = request.POST['deliver']
        print(product.save(update_fields=['deliver']))
        return redirect('summary')
    else:
        my_form = DeliverForm()
        context = {
            "form": my_form,
        }
    return render(request, 'deliver.html', context)

def summary(request):
    results = []
    paramz = []
    my_form = TestForm()
    for ob in my_form:
        paramz.append(ob.label)
    posts = Post.objects.all()
    post = posts[0]
    for attr, value in post.__dict__.items():
        results.append(value)
    del results[0]
    del results[0]
    zipped = list(zip(paramz, results))
    shippings = results[17:]
    ship_zip = zip(shippings_labels, shippings)
    context = {
        'zipped': zipped,
        'ship_zip': ship_zip,
    }
    return render(request, 'summary.html', context)

def terms(request):
    return render(request, 'terms.html', {})

def testing(request):
    return render(request, 'testing.html', {})

def feedbacks(request):
    return render(request, 'feedbacks.html', {})

def thankyou(request):
    return render(request, 'thankyou.html', {})

def download(request):
    download_id = request.GET.get('id')
    download_link = 'static/downloadables/' + downloads[download_id]
    response = HttpResponse(open(download_link, 'rb').read())
    # response['Content-Type'] = 'text/plain'
    disposition = 'attachment; filename=' + downloads[download_id]
    response['Content-Disposition'] = disposition
    return response