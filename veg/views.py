from django.shortcuts import render,redirect
from django.http import HttpResponse
from vegapp.models import recform


def show(request):
    if request.method=="POST":

        recname=request.POST.get('name')
        desc=request.POST.get('content')
        file=request.FILES['file']
        new=recform(rec_name=recname,rec_dec=desc,rec_img=file)
        new.save()
        return redirect("/")
    return render(request,"recipe.html")
def form(request):

    return render(request,"form.html")

def recipedta(request):
    data=recform.objects.all()
    return render(request,"recipedata.html",{'data':data})

def delete(request,id):
    deletedata=recform.objects.get(id = id)
    deletedata.delete()
    return redirect("recipe")

    # return HttpResponse(id)


