from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from .models import Job, Resource, ContactMessage, JobCategory, ResourceCategory
from .forms import JobForm, ResourceForm, ContactForm


# ─── Public Views ────────────────────────────────────────────────────────────

def home(request):
    latest_jobs = Job.objects.filter(is_active=True)[:6]
    latest_resources = Resource.objects.filter(is_active=True)[:4]
    context = {
        'latest_jobs': latest_jobs,
        'latest_resources': latest_resources,
    }
    return render(request, 'home.html', context)


def job_list(request):
    jobs = Job.objects.filter(is_active=True)
    category = request.GET.get('category', '')
    search = request.GET.get('q', '')

    if category:
        jobs = jobs.filter(category=category)
    if search:
        jobs = jobs.filter(Q(title__icontains=search) | Q(description__icontains=search) | Q(company__icontains=search))

    context = {
        'jobs': jobs,
        'categories': JobCategory.choices,
        'selected_category': category,
        'search': search,
    }
    return render(request, 'job_list.html', context)


def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk, is_active=True)
    related_jobs = Job.objects.filter(category=job.category, is_active=True).exclude(pk=pk)[:3]
    return render(request, 'job_detail.html', {'job': job, 'related_jobs': related_jobs})


def resource_list(request):
    resources = Resource.objects.filter(is_active=True)
    category = request.GET.get('category', '')
    search = request.GET.get('q', '')

    if category:
        resources = resources.filter(category=category)
    if search:
        resources = resources.filter(Q(title__icontains=search) | Q(description__icontains=search))

    context = {
        'resources': resources,
        'categories': ResourceCategory.choices,
        'selected_category': category,
        'search': search,
    }
    return render(request, 'resource_list.html', context)


def resource_download(request, pk):
    resource = get_object_or_404(Resource, pk=pk, is_active=True)
    resource.download_count += 1
    resource.save(update_fields=['download_count'])
    url = resource.get_download_url()
    if not url:
        raise Http404("File not available")
    return redirect(url)


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent! We will get back to you soon.')
            return redirect('job:contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def privacy_policy(request):
    return render(request, 'privacy_policy.html')


# ─── Admin Dashboard Views ────────────────────────────────────────────────────

@staff_member_required
def admin_dashboard(request):
    total_jobs = Job.objects.count()
    active_jobs = Job.objects.filter(is_active=True).count()
    total_resources = Resource.objects.count()
    unread_messages = ContactMessage.objects.filter(is_read=False).count()
    recent_messages = ContactMessage.objects.filter(is_read=False)[:5]
    context = {
        'total_jobs': total_jobs,
        'active_jobs': active_jobs,
        'total_resources': total_resources,
        'unread_messages': unread_messages,
        'recent_messages': recent_messages,
    }
    return render(request, 'admin/dashboard.html', context)


@staff_member_required
def admin_job_list(request):
    jobs = Job.objects.all()
    return render(request, 'admin/job_list.html', {'jobs': jobs})


@staff_member_required
def admin_job_add(request):
    form = JobForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Job posted successfully!')
        return redirect('job:admin_job_list')
    return render(request, 'admin/job_form.html', {'form': form, 'title': 'Add Job'})


@staff_member_required
def admin_job_edit(request, pk):
    job = get_object_or_404(Job, pk=pk)
    form = JobForm(request.POST or None, instance=job)
    if form.is_valid():
        form.save()
        messages.success(request, 'Job updated successfully!')
        return redirect('job:admin_job_list')
    return render(request, 'admin/job_form.html', {'form': form, 'title': 'Edit Job', 'job': job})


@staff_member_required
def admin_job_delete(request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.method == 'POST':
        job.delete()
        messages.success(request, 'Job deleted.')
        return redirect('job:admin_job_list')
    return render(request, 'admin/confirm_delete.html', {'object': job, 'type': 'Job'})


@staff_member_required
def admin_resource_list(request):
    resources = Resource.objects.all()
    return render(request, 'admin/resource_list.html', {'resources': resources})


@staff_member_required
def admin_resource_add(request):
    form = ResourceForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Resource added successfully!')
        return redirect('job:admin_resource_list')
    return render(request, 'admin/resource_form.html', {'form': form, 'title': 'Add Resource'})


@staff_member_required
def admin_resource_edit(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    form = ResourceForm(request.POST or None, request.FILES or None, instance=resource)
    if form.is_valid():
        form.save()
        messages.success(request, 'Resource updated successfully!')
        return redirect('job:admin_resource_list')
    return render(request, 'admin/resource_form.html', {'form': form, 'title': 'Edit Resource', 'resource': resource})


@staff_member_required
def admin_resource_delete(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    if request.method == 'POST':
        resource.delete()
        messages.success(request, 'Resource deleted.')
        return redirect('job:admin_resource_list')
    return render(request, 'admin/confirm_delete.html', {'object': resource, 'type': 'Resource'})


@staff_member_required
def admin_messages(request):
    msgs = ContactMessage.objects.all()
    ContactMessage.objects.filter(is_read=False).update(is_read=True)
    return render(request, 'admin/messages.html', {'messages_list': msgs})