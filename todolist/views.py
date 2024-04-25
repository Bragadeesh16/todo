from django.shortcuts import render,redirect
from .froms import todo_from
from .models import todo

def todo_lists(request):
    data = todo.objects.all()
    form = todo_from()
    if request.method == 'POST':
        form = todo_from(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo-list')
        else:
            form = todo_from()

    return render(request,'todo_list.html',{'data':data,'form':form})

def todo_edit(request,pk):
    data = todo.objects.get(pk = pk)
    form = todo_from()
    if request.method == 'POST':
        form = todo_from(request.POST,instance=data)
        form.save()
        return redirect('todo-list')

    else:
        form = todo_from(instance=data)

    return render(request,'todo_edit.html',{'form':form,'pk':pk})    

def todo_delete(reqest,pk):
    data = todo.objects.get(pk = pk)
    data.delete()
    return redirect('todo-list')