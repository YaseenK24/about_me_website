from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question
from plotly.offline import plot
import pandas as pd
import plotly.express as plt

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)


def index(request):
    return render(request, "index.html")


def two(request):
    return render(request, "two.html")


def three(request):
    return render(request, "three.html")


def four(request):
    return render(request, "four.html")


def six(request):
    return render(request, "six.html")


def five(request):
    if request.method == "POST":
        question_text = request.POST.get("question")
        if question_text:
            Question.objects.create(question_text=question_text)
            return redirect("five")  # Refresh after submission

    questions = Question.objects.all()



    #New Chart
    df = pd.read_csv('yahseno/data.csv')

    title = "All Time NBA Scoring Leaders"
    fig = plt.bar(df, x="Players", y="Points", title=title)

    fig.update_layout(
        font_family="Arial",
        font_color="Black",
        title_font_family="Robo Slab",
        title_font_color="Black",
        title=dict(text=title, font=dict(size=35), automargin=True)

    )
    plt_div = plot(fig, output_type='div')

    return render(request, "five.html", context={
        'plot_div': plt_div,
        'questions': questions
    })

