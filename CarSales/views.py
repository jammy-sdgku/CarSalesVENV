import os
import pymongo
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from .forms import CarForm

carsalesClient = pymongo.MongoClient(os.environ["carsalesClient"])

def connectDB():
    return carsalesClient["CarSales"]

def carslist(request):
    cars = []
    carsalesDB = connectDB()
    tblCars = carsalesDB["TblCars"]

    for car in tblCars.find():
        cars.append({"id": car["ID"], "name": car["Name"], "year": car["Year"], "price": car["Price"]})
    return render(request, 'carslist.html', {'cars':cars})

def addcar(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tblCars = connectDB()["TblCars"]
            tblCars.insert_one({
                "ID": data["id"],
                "Name": data["name"],
                "Year": data["year"],
                "Price": data["price"],
            })
            return redirect("carslist")
    else:
        form = CarForm()

    return render(request, "addcar.html", {
        "form": form,
        "car": form.data,
    })

def updatecar(request, id):
    cr = []
    carsalesDB = connectDB()
    tblCars = carsalesDB["TblCars"]
    if request.method == 'GET':
        for car in tblCars.find( { "ID": id } ):
            cr.append({"id": car["ID"], "name": car["Name"], "year": car["Year"], "price": car["Price"]})
        return render(request, 'addcar.html', {'car':cr[0]})
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            name = str(form.cleaned_data.get("name"))
            year = int(form.cleaned_data.get("year"))
            price = float(form.cleaned_data.get("price"))
            condition = { "ID": id }
            updatedval = { "$set": { "Name": name, "Year": year, "Price": price } }
            tblCars.update_one(condition, updatedval)
        return redirect('carslist')
    
@require_POST
def deletecar(request, id):
    tblCars = connectDB()["TblCars"]
    result = tblCars.delete_one({"ID": id})

    if result.deleted_count == 1:
        messages.success(request, "The vehicle was deleted successfully.")
    else:
        messages.error(request, "The vehicle was not found. It may already have been deleted.")

    return redirect("carslist")