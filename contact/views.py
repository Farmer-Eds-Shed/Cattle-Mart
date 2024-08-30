from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.contrib import messages


def feedback(request):
    """
    Renders the Feedback page
    """
    if request.method == "POST":
        feedback_form = FeedbackForm(request.POST)

        if feedback_form.is_valid():
            feedback_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Request received! We endeavour"
                                 "to respond within 2 working days."
                                 )
            return redirect(request.path)
    else:
        feedback_form = FeedbackForm()

    return render(
        request,
        "contact/contact.html",
        {
            "feedback_form": feedback_form
        },
    )
