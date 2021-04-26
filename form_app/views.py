from django.shortcuts import render, redirect

# Create your views here.
def form(request):
    return render(request,"form.html")
    
    

def result(request):
    if request.method == "POST":
        name = request.POST["name"]
        location = request.POST["dojo_loc"]
        language = request.POST["fav_lang"]
        comment = request.POST["comment"]

        request.session["name"] = name
        request.session["location"] = location
        request.session["language"] = language
        request.session["comment"] = comment
    return redirect("/display")

def display(request):
    
    return render(request,"result.html")
