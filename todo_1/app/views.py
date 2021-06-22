from django.shortcuts import redirect, render
from .models import TodoModel

# Create your views here.
def index(request):
    td = TodoModel.objects.all()
    return render(request , 'index.html',{'td':td})

def add(request):
    if request.method == 'POST':
        work = request.POST.get('n1')
        td = TodoModel(work=work)
        td.save()
        return redirect(index)

def delete(request,id):
    TodoModel.objects.get(id=id).delete()
    return redirect(index)

