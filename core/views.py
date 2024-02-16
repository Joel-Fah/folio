import json
import random
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages
from django.utils.html import format_html
from django.views.generic import TemplateView, DetailView, ListView
from .models import Project, Tag, AcademicAchievement, Certification, Volunteering, Message
from .forms import MessageForm

# Create your views here.


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['tags'] = Tag.objects.all()
        return context


class ProjectDetailView(DetailView):
    template_name = 'project_detail.html'
    model = Project

    def get_queryset(self):
        return Project.objects.filter(id=self.kwargs['id'], slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = Project.objects.get(
            id=self.kwargs['id'], slug=self.kwargs['slug'])
        context["duration"] = self.calculate_duration(
            project.started_at, project.ended_at)
        return context

    def calculate_duration(self, started_at, ended_at):
        # Calculate the difference between the end and start dates
        difference = ended_at - started_at

        # Calculate the duration in days
        days = difference.days

        # Calculate the duration in weeks
        weeks = days // 7

        # Calculate the duration in months
        months = days // 30

        # Calculate the duration in years
        years = days // 365

        # Determine the lowest readable value
        if years > 0:
            duration = f'{years} {"year" if years == 1 else "years"}'
        elif months > 0:
            duration = f'{months} {"month" if months == 1 else "months"}'
        elif weeks > 0:
            duration = f'{weeks} {"week" if weeks == 1 else "weeks"}'
        else:
            duration = f'{days} {"day" if days == 1 else "days"}'

        return duration


class WorksView(ListView):
    model = Project
    template_name = 'projects_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tool"] = random.choice(['angle-tool', 'hammer', 'tools', 'ruler-combine',
                                        'color-filter', 'color-picker', 'frame-alt-empty', 'crop', 'component'])
        context["emoji"] = random.choice(
            ['emoji-satisfied', 'emoji-surprise-alt', 'emoji-surprise', 'emoji-blink-left', 'emoji-blink-right'])
        context['academics'] = AcademicAchievement.objects.all()
        context['certifications'] = Certification.objects.all()
        context['volunteerings'] = Volunteering.objects.all()
        return context


# A list of quotes to be displayed on the connect page
quotes = [
    "In the tapestry of life, every thread of connection weaves a unique pattern. Your network, forged through meaningful relationships, is not just a collection of contacts—it's the very fabric of your success, a testament to your net worth. -- <strong>Porter Gale</strong>",
    "Success isn't merely a monetary pursuit; it's a purposeful journey of making a lasting impact. Strive not only for personal gain but for the greater good, as the true measure of success lies in the positive differences we create in the lives of others. -- Anonymous",
    "Time, an invaluable currency, should be invested wisely in crafting your own narrative. Don't squander it living someone else's story; instead, channel your energy into meaningful pursuits that align with your passions and purpose. -- <strong>Steve Jobs</strong>",
    "Embark on your journey of productivity not with idle talk but with purposeful action. The key to progress lies not in mere discussions but in the relentless execution of your plans, transforming ideas into tangible achievements. -- <strong>Walt Disney</strong>",
    "Success is not an accidental feat but a deliberate act of disciplined productivity. Those who thrive are not merely seekers of success; they are the architects of their own accomplishments, diligently building the foundations of their dreams. -- <strong>Henry David Thoreau</strong>",
    "When you consider the importance of Word-of-Mouth, referrals, recommendations, and knowledge-sharing do you even have a choice? Your network is your everything. -- <strong>Vedran Rasic</strong>",
    "Technology is nothing. What's important is that you have faith in people, that they're basically good and smart, and if you give them tools, they'll do wonderful things with them. -- <strong>Steve Jobs</strong>",
    "The true value of networking doesn't come from how many people we can meet but rather how many people we can introduce to others. -- <strong>Simon Sinek</strong>",
    "Networking is not about just connecting people. It's about connecting people with people, people with ideas, and people with opportunities. -- <strong>Michele Jennae</strong>",
    "Strive for a pixel-perfect impact in your career, where every detail contributes to personal and societal growth. Each purposeful action and positive influence shapes a meaningful and impactful journey, resembling a masterpiece on the canvas of our careers. -- <strong>My humble self</strong>"
]

# Shuffle list
random.shuffle(quotes)


class ConnectView(TemplateView):
    template_name = 'connect.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["quote"] = ("|").join(quotes)
        return context


class MessageView(ListView):
    template_name = 'messages_list.html'
    model = Message

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = Message.objects.create(
            message='In the canvas of our careers, strive for a pixel-perfect impact, where every detail matters and contributes to the larger picture of growth—both personal and societal. Just as each pixel shapes the image, every purposeful action and positive influence you create contributes to the masterpiece of a meaningful and impactful journey.') if not Message.objects.exists() else random.choice(Message.objects.all())
        context["form"] = MessageForm()
        context["tool"] = random.choice(['angle-tool', 'hammer', 'tools', 'ruler-combine',
                                        'color-filter', 'color-picker', 'frame-alt-empty', 'crop', 'component'])
        context["emoji"] = random.choice(
            ['emoji-satisfied', 'emoji-surprise-alt', 'emoji-surprise', 'emoji-blink-left', 'emoji-blink-right'])
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = MessageForm(request.POST)

            if form.is_valid():
                name = form.cleaned_data['name']

                # Save message in DB
                new_message = form.save()

                # Send out success message
                message = format_html("Thanks <strong>{}</strong> for your message.<br> <a href='{}' target='_blank' class='page-link block font-semibold underline hover:no-underline'>{}</a>",
                                      name,
                                      reverse('core:message_details',
                                              args=[new_message.id]),
                                      "View message"
                                      )

                messages.success(
                    request,
                    message
                )

                return redirect('core:messages')
            else:
                form = MessageForm()

                format_html(messages.error(
                    request,
                    f'Oops! a problem occurred when uploading your message.'
                ))
        return render(request, self.template_name, {'form': form})


class MessageDetailView(DetailView):
    model = Message
    template_name = 'messages_detail.html'

    def get_queryset(self):
        return Message.objects.filter(id=self.kwargs['pk'])


# Custom error pages (404, 500)


def custom_page_not_found_view(request, exception):
    return render(request, 'errors/404.html', status=404)


def custom_error_view(request):
    return render(request, 'errors/500.html', status=500)
