from django.shortcuts import render,redirect,get_object_or_404

from .models import Employee


def home(req):
    emps = Employee.objects.all()

    return render(req, "home.html",{"emps":emps})

def add(req):
    if req.method=="POST":
        name= req.POST["name"]
        roll = req.POST["roll"]
        Employee.objects.create(name=name,roll = roll)

        return redirect("home")

    return render (req,"add.html" )  


def update(req,id):
    emp= get_object_or_404(Employee,id=id)
    if req.method=="POST":
        emp.name = req.POST["name"]
        emp.roll = req.POST["roll"]
        emp.save()

        return redirect("home")

    return render(req,"update.html",{"emp":emp})   


def delete(req,id):
        emp= get_object_or_404(Employee,id=id)
        emp.delete()
        return redirect("home")


def detail(req,id):
    em = get_object_or_404(Employee,id=id)

    return render(req, "detail.html",{"em":em})