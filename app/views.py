from django.shortcuts import render
from app.forms import FrontForm, NoTeenForm, XYZForm, CenteredAvgForm

# Create your views here.


def front_view(request):
    form = FrontForm(request.GET)
    if form.is_valid():
        if len(form.cleaned_data["string"]) <= 3:
            return render(
                request,
                "front.html",
                {
                    "form": form,
                    "string": form.cleaned_data["string"],
                    "n": form.cleaned_data["n"],
                    "repeated": form.cleaned_data["string"] * form.cleaned_data["n"],
                },
            )
        else:
            return render(
                request,
                "front.html",
                {
                    "form": form,
                    "string": form.cleaned_data["string"],
                    "n": form.cleaned_data["n"],
                    "repeated": form.cleaned_data["string"][:3]
                    * form.cleaned_data["n"],
                },
            )
    else:
        return render(request, "front.html", {"form": form})


def no_teen_view(request):
    form = NoTeenForm(request.GET)
    if form.is_valid():
        data = form.cleaned_data

        if [13, 14, 17, 18, 19].count(data["a"]) > 0:
            data["a"] = 0

        if [13, 14, 17, 18, 19].count(data["b"]) > 0:
            data["b"] = 0

        if [13, 14, 17, 18, 19].count(data["c"]) > 0:
            data["c"] = 0

        return render(
            request,
            "no_teen.html",
            {
                "form": form,
                "a": data["a"],
                "b": data["b"],
                "c": data["c"],
                "total": data["a"] + data["b"] + data["c"],
            },
        )

    else:
        return render(request, "no_teen.html", {"form": form})


def xyz_view(request):
    form = XYZForm(request.GET)
    if form.is_valid():
        return render(
            request,
            "xyz.html",
            {
                "form": form,
                "xyz": form.cleaned_data["string"].count("xyz")
                > form.cleaned_data["string"].count(".xyz"),
            },
        )
    else:
        return render(request, "xyz.html", {"form": form})


def centered_avg_view(request):
    form = CenteredAvgForm(request.GET)
    if form.is_valid():
        centered_list = []
        for i in form.cleaned_data:
            if form.cleaned_data[i] != None:
                centered_list.append(form.cleaned_data[i])

        centered_list.sort()
        centered_list.pop(0)
        centered_list.pop(len(centered_list) - 1)

        sum = 0
        for i in centered_list:
            sum += i
        avg = sum / len(centered_list)

        return render(
            request,
            "centered_avg.html",
            {
                "form": form,
                "avg": avg,
            },
        )
    else:
        return render(request, "centered_avg.html", {"form": form})
