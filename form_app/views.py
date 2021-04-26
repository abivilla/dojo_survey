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
        context = {
            "name": name,
            "location": location,
            "language": language,
            "comment": comment
        }
        return render(request,"result.html", context)
