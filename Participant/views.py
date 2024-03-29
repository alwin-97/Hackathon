from django.shortcuts import render,redirect, get_object_or_404
from Organizer.models import OrganiseEvent, EventDetails, ShareResource
from Participant.models import ParticipateEvent
from accounts.models import  UserProfile
from django.contrib.auth.models import User
from django.utils import timezone
from Blog.models import BlogsInfo
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.http import HttpResponse
import io

def about(request):
	return  render(request,'participant_index.html')


def participate(request):
	even = EventDetails.objects
	return render(request,'participant_index.html',{'even':even})


def part_profile(request):
	return render(request,'part_profile.html',{})

def part_editProfile(request):
	part_profiles=UserProfile.objects	
	return render(request,'part_editProfile.html',{'part_profiles':part_profiles})

def part_updateProfile(request):
	if request.method=='POST':	
		submitbutton = request.POST.get('Submit')
		if submitbutton :
			user = request.POST['user']	
			fname =  request.POST['fname']
			lname =  request.POST['lname']
			email =  request.POST['email']
			
			profiles=User(id=request.user.id,username=user,first_name= fname,last_name=lname,email=email)
			profiles.save()
			profiles.refresh_from_db()		
			edit_profile=UserProfile.objects
			return render(request,'part_profile.html',{'part_profile':edit_profile})


def deleteparticipant(request):
	User.objects.filter(username=request.user.username).delete()
	#messages.success(request,'Profile have been Successfully deleted')
	return render(request, 'login.html' ,{'error':'Profile have been Successfully deleted'})

def event_details(request):
	events = OrganiseEvent.objects
	return render(request,'event_details.html',{'events':events})

def participated_event(request):
	part_event = ParticipateEvent.objects.filter(us= request.user.id)
	events = OrganiseEvent.objects.filter(us= request.user.id)
	return render(request,'participated_event.html',{'part_event':part_event})


def partblogsDetails(request):
    blogsInfo = BlogsInfo.objects.filter(us=request.user.id)
    return render(request, 'part-blog_edit.html', {'blogsInfo': blogsInfo})

def partblog(request):
	 return render(request,'part-blog_write.html')

def partWriteBlog(request):
	if request.method =='POST':
		title = request.POST['blog_title']
		pubDateTime = timezone.now()
		description = request.POST['description']
		imageSecond = request.POST['image_second']
		imageFirst = request.POST['image_first']
		blogCategory = request.POST['blog_category']
		refrenceLinks = request.POST['refrence_link']
		UserType = 'Participant'
		if request.user.is_authenticated:
			authorName = request.user.first_name + " " + request.user.last_name
		if title =='':
			return render(request,'part-blog_write.html', {'error':"Title is not given"})	
		else:
			title = request.POST['blog_title']		
		if pubDateTime =='':			
			pubDateTime = timezone.now()
		if description=='':
			return render(request,'part-blog_write.html', {'error':"Description is not written"})	
		else:
			description = request.POST['description']		
		if imageFirst=='':
			return render(request,'part-blog_write.html', {'error':"Image first is not given"})	
		else:
			imageFirst = request.POST['image_first']			
		if imageSecond=='':
			return render(request,'part-blog_write.html', {'error':"Image Two is not given"})	
		else:
			imageSecond = request.POST['image_second']	
		if blogCategory=='':
			return render(request,'part-blog_write.html', {'error':"Blog Category is not selected"})	
		else:
			blogCategory = request.POST['blog_category']		
		if refrenceLinks=='':
			return render(request,'part-blog_write.html', {'error':"Refrence links not given"})	
		else:
			refrenceLinks = request.POST['refrence_link']
		blogsInfo=BlogsInfo(title=title,pubDateTime=pubDateTime,description=description,imageSecond=imageSecond,imageFirst=imageFirst,
			UserType=UserType,authorName=authorName,blogCategory=blogCategory,refrenceLinks=refrenceLinks,us_id=request.user.id)
		
		blogsInfo.save()
		print("author name:" + authorName)
		return render(request,'part-blog_write.html', {'error':"Event is not selected"})	



def req_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'as_attachment=True; filename="mypdf.pdf"'
    response['Content-Disposition'] = 'inline'
    filename = "mypdf.pdf"

    buffer = io.BytesIO()
    buffer.pagesize = A4
    p = canvas.Canvas(buffer)
    p.setLineWidth(.3)
    p.setFont('Helvetica', 12)

    p.line(80, 770, 480, 770)
    p.drawString(80, 755, 'HACKATHON USER DETAILS :')
    p.line(80, 750, 480, 750)
    # Start writing the PDF here
    p.drawString(80, 725, 'Email ')
    p.drawString(200, 725, ': ')
    p.drawString(250, 725, request.user.email)
    p.line(80, 700, 480, 700)
    p.drawString(80, 675, 'User Name ')
    p.drawString(200, 675, ': ')
    p.drawString(250, 675, request.user.username)
    p.drawString(80, 650, 'First Name ')
    p.drawString(200, 650, ': ')
    p.drawString(250, 650, request.user.first_name)
    p.drawString(80, 625, 'Last Name ')
    p.drawString(200, 625, ': ')
    p.drawString(250, 625, request.user.last_name)
    p.line(80, 550, 480, 550)
    p.drawString(
        80, 532, 'DATA RETRIVED FROM DATA BASE IF ERROR CONTACT ADMIN')
    p.line(80, 525, 480, 525)
    # End writing

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response

