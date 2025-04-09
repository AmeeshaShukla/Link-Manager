from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ChangePasswordForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Link, Contact
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def index(request):
    return render(request, 'link/index.html')

def signup(request):   
   if request.method=="POST":
      # Get the post parameters
      username=request.POST['username']
      email=request.POST['email']
      fname=request.POST['fname']
      lname=request.POST['lname']
      pass1=request.POST['password1']
      pass2=request.POST['password2']
      
      punctuations='''!()/[]{}:;'",<>/?\~`$^&%*-=+'''
      # check for errorneous input
      if len(username)> 20:
         messages.error(request,"Username must be under 20 characters!!")
         return redirect('SignUp')
      
      for char in username:
         if char in punctuations:
            messages.error(request,"Username should only contain letters and number!! ")
            return redirect('SignUp')

      if User.objects.filter(username=username).exists(): 
         messages.error(request,"Username already exists!! Try some different name. ")
         return redirect('SignUp')    

      if User.objects.filter(email=email).exists(): 
         messages.error(request,"An account is already registered with the same email id!!")
         return redirect('SignUp')    

      if len(pass1)<8:
         messages.error(request,"Password length should be atleast 8 characters!!")
         return redirect('SignUp')
         
      if pass1!=pass2:
         messages.error(request,"Passwords do not match!!")
         return redirect('SignUp')

  
      # Create the user
      myuser = User.objects.create_user(username, email, pass1)
      myuser.first_name= fname
      myuser.last_name= lname
      myuser.save()
      messages.success(request, " Your Account has been successfully created.")
      return redirect('LinkHome')
   else:
      return render (request,'link/signup.html')            

def handlelogin(request):
    if request.method =='POST':
        loginusername=request.POST.get('LoginUsername')
        loginpassword=request.POST.get('LoginPassword')
        user= authenticate(request, username=loginusername,password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged In Successfully  .")
            return redirect('LinkHome')
        else:
            messages.error(request, 'Invalid Credentials, Please try again.')
            return redirect('Login')
    else:
       return render (request,'link/login.html')        

    # return render(request,'Login')  

@login_required(login_url='/link/login/')
def handlelogout(request):
    logout(request)
    messages.info(request,"Logged Out Successfully.")
    return redirect('Login')   

@login_required(login_url='/link/login/')
def PasswordChange(request):
	user = request.user
	if request.method == 'POST':
		form = ChangePasswordForm(request.POST)
		if form.is_valid():
			new_password = form.cleaned_data.get('new_password')
			user.set_password(new_password)
			user.save()
			update_session_auth_hash(request, user)
			messages.success(request, "Password Updated Successfully.")
	else:
		form = ChangePasswordForm(instance=user)

	context = {
		'form':form,
	}

	return render(request, 'link/change-password.html', context)

def about(request):
   return render (request,'link/about.html') 

@login_required(login_url='/link/login/')
def contact(request):
   if request.method == "POST":
      Name = request.POST.get('name', '')
      Email = request.POST.get('email', '')
      Phone = request.POST.get('phone', '')
      Desc = request.POST.get('message', '')

      contact = Contact(name=Name, email=Email, phone=Phone, desc=Desc)
      print(type(contact))
      contact.save()
      messages.info(request,"Our contact team will soon respond to your query.")
   return render (request,'link/contact.html') 

   if request.method == 'POST':  
      Airbnb=(request.POST.get('Airbnb','off'))
      Amazon=(request.POST.get('Amazon','off'))
      Blog=(request.POST.get('Blog','off'))
      Book=(request.POST.get('Book','off'))
      Cloud=(request.POST.get('Cloud','off'))
      Codepen=(request.POST.get('Codepen','off'))
      Discord=(request.POST.get('Discord','off'))
      Email=(request.POST.get('Email','off'))
      Facebook=(request.POST.get('Facebook','off'))
      Github=(request.POST.get('Github','off'))
      Google_Drive=(request.POST.get('Google-Drive','off'))
      Google_Forms=(request.POST.get('Google-Forms','off'))
      Google_Play=(request.POST.get('Google-Play','off'))
      HackerRank=(request.POST.get('HackerRank','off'))
      Instagram=(request.POST.get('Instagram','off'))
      LinkedIn=(request.POST.get('LinkedIn','off'))
      QR_Code=(request.POST.get('QR-Code','off'))
      Quora=(request.POST.get('Quora','off'))
      Reddit=(request.POST.get('Reddit','off'))
      Slideshare=(request.POST.get('Slideshare','off'))
      Snapchat=(request.POST.get('Snapchat','off'))
      Spotify=(request.POST.get('Spotify','off'))
      Telegram=(request.POST.get('Telegram','off'))
      Twitch=(request.POST.get('Twitch','off'))
      Twitter=(request.POST.get('Twitter','off'))
      Vimeo=(request.POST.get('Vimeo','off'))
      Whatsapp=(request.POST.get('Whatsapp','off'))
      Website=(request.POST.get('Website','off'))
      YouTube=(request.POST.get('YouTube','off'))
      params={}
      if Amazon =="on":
         dict1={'amazon':'Amazon'}
         params.update(dict1)
      
      if Airbnb=="on":
         dict1={'airbnb':'Airbnb'}
         params.update(dict1)
         
      if Blog=="on":
         dict1={'blog':'Blog'}
         params.update(dict1)
      
      if Book=="on":
         dict1={'book':'Book'}
         params.update(dict1)
      
      if Cloud=="on": 
         dict1={'cloud':'Cloud'}
         params.update(dict1)
      
      if Codepen =="on": 
         dict1={'codepen':'Codepen'}
         params.update(dict1)
      
      if Discord=="on": 
         dict1={'discord':'Discord'}
         params.update(dict1)
      
      if Email=="on": 
         dict1={'email':'Email'}
         params.update(dict1)
      
      if Facebook=="on": 
         dict1={'facebook':'Facebook'}
         params.update(dict1)
      
      if Github=="on": 
         dict1={'github':'Github'}
         params.update(dict1)
      
      if Google_Drive=="on": 
         dict1={'google_drive':'Google-Drive'}
         params.update(dict1)
      
      if Google_Forms=="on": 
         dict1={'google_forms':'Google-Forms'}
         params.update(dict1)

      if Google_Play=="on": 
         dict1={'google_play':'Google-Play'}
         params.update(dict1)
      
      if HackerRank=="on": 
         dict1={'hackerRank':'HackerRank'}
         params.update(dict1)
      
      if Instagram=="on": 
         dict1={'instagram':'Instagram'}
         params.update(dict1)
      
      if LinkedIn=="on": 
         dict1={'linkedin':'LinkedIn'}
         params.update(dict1)
      
      if QR_Code=="on": 
         dict1={'qr_code':'QR-Code'}
         params.update(dict1)
      
      if Quora=="on": 
         dict1={'quora':'Quora'}
         params.update(dict1)
      
      if Reddit=="on": 
         dict1={'reddit':'Reddit'}
         params.update(dict1)
      
      if Slideshare=="on": 
         dict1={'slideshare':'Slideshare'}
         params.update(dict1)
      
      if Snapchat=="on": 
         dict1={'snapchat':'Snapchat'}
         params.update(dict1)
      
      if Spotify=="on": 
         dict1={'spotify':'Spotify'}
         params.update(dict1)
      
      if Telegram=="on": 
         dict1={'telegram':'Telegram'}
         params.update(dict1)
      
      if Twitch=="on": 
         dict1={'twitch':'Twitch'}
         params.update(dict1)
      
      if Twitter=="on": 
         dict1={'twitter':'Twitter'}
         params.update(dict1)
      
      if Vimeo=="on": 
         dict1={'vimeo':'Vimeo'}
         params.update(dict1)
      
      if Whatsapp=="on": 
         dict1={'whatsapp':'Whatsapp'}
         params.update(dict1)

      if Website=="on": 
         dict1={'website':'Website'}
         params.update(dict1)
      
      if YouTube=="on": 
         dict1={'youtube':'YouTube'}
         params.update(dict1)

   else:
      return redirect('Select') 
   
   return render(request,'link/addlinks.html',params)

def profile(request,namers):
   if request.method == 'POST':
      AmazonLink=(request.POST.get('Amazonlink', ''))
      AirbnbLink=(request.POST.get('Airbnblink' , ''))
      BlogLink=(request.POST.get('Bloglink' , ''))
      BookLink=(request.POST.get('Booklink' , ''))
      CloudLink=(request.POST.get('Cloudlink' , ''))
      CodepenLink=(request.POST.get('Codepenlink' , ''))
      DiscordLink=(request.POST.get('Discordlink' , ''))
      EmailLink=(request.POST.get('Emaillink' , ''))
      FacebookLink=(request.POST.get('Facebooklink' , ''))
      GithubLink=(request.POST.get('Githublink' , ''))
      Google_DriveLink=(request.POST.get('Gdrivelink' , ''))
      Google_FormsLink=(request.POST.get('Gformslink' , ''))
      Google_PlayLink=(request.POST.get('Gplaylink' , ''))
      HackerRankLink=(request.POST.get('Hackerranklink' , ''))
      InstagramLink=(request.POST.get('Instagramlink' , ''))
      LinkedInLink=(request.POST.get('Linkedinlink' , ''))
      QR_CodeLink=(request.POST.get('Qcodelink' , ''))
      QuoraLink=(request.POST.get('Quoralink' , ''))
      RedditLink=(request.POST.get('Redditlink' , ''))
      SlideshareLink=(request.POST.get('Slidesharelink' , ''))
      SnapchatLink=(request.POST.get('Snapchatlink' , ''))
      SpotifyLink=(request.POST.get('Spotifylink' , ''))
      TelegramLink=(request.POST.get('Telegramlink' , ''))
      TwitchLink=(request.POST.get('Twitchlink' , ''))
      TwitterLink=(request.POST.get('Twitterlink' , ''))
      WhatsappLink=(request.POST.get('Whatsapplink' , ''))
      WebsiteLink=(request.POST.get('Websitelink' , ''))
      YouTubeLink=(request.POST.get('Youtubelink' , ''))
      
      try:  
         obj=Link.objects.get(owner=request.user.id)
         if obj.amazon != None and len(AmazonLink) !=0:
            obj.amazon=AmazonLink
            obj.save()
         else:
            pass

         if obj.airbnb!=None and len(AirbnbLink)!=0:
            obj.airbnb=AirbnbLink
            obj.save()     
         else:
            pass
         
         if obj.blog!=None and len(BlogLink) !=0:
            obj.blog=BlogLink
            obj.save()     
         else:
            pass
         
         if obj.book!=None and len(BookLink) !=0:
            obj.book=BookLink
            obj.save()     
         else:
            pass
         
         if obj.cloud!=None and len(CloudLink) !=0:
            obj.cloud=CloudLink
            obj.save()
         else:
            pass
         
         if obj.codepen!=None and len(CodepenLink) !=0:
            obj.codepen=CodepenLink
            obj.save()
         else:
            pass
         
         if obj.discord!=None and len(DiscordLink) !=0:
            obj.discord=DiscordLink
            obj.save()
         else:
            pass
         
         if obj.email!=None and len(EmailLink) !=0:
            obj.email=EmailLink
            obj.save()
         else:
            pass
         
         if obj.facebook!=None and len(FacebookLink) !=0:
            obj.facebook=FacebookLink
            obj.save()
         else:
            pass
         
         if obj.github!=None and len(GithubLink) !=0:
            obj.github=GithubLink
            obj.save()
         else:
            pass
         
         if obj.google_drive!=None and len(Google_DriveLink) !=0:
            obj.google_drive=Google_DriveLink
            obj.save()
         else:
            pass

         if obj.google_forms!=None and len(Google_FormsLink) !=0:
            obj.google_forms=Google_FormsLink
            obj.save()
         else:
            pass
         
         if obj.google_play!=None and len(Google_PlayLink) !=0:
            obj.google_play=Google_PlayLink
            obj.save()
         else:
            pass
         
         if obj.hackerRank!=None and len(HackerRankLink) !=0:
            obj.hackerRank=HackerRankLink
            obj.save()
         else:
            pass
         
         if obj.instagram!=None and len(InstagramLink) !=0:
            obj.instagram=InstagramLink
            obj.save()
         else:
            pass
         
         if obj.linkedin!=None and len(LinkedInLink) !=0:
            obj.linkedin=LinkedInLink
            obj.save()
         else:
            pass
         
         if obj.qr_code!=None and len(QR_CodeLink) !=0:
            obj.qr_code=QR_CodeLink
            obj.save()
         else:
            pass
         
         if obj.quora!=None and len(QuoraLink) !=0:
            obj.quora=QuoraLink
            obj.save()
         else:
            pass
         
         if obj.reddit!=None and len(RedditLink) !=0:
            obj.reddit=RedditLink
            obj.save()
         else:
            pass
         
         if obj.slideshare!=None and len(SlideshareLink) !=0:
            obj.slideshare=SlideshareLink
            obj.save()
         else:
            pass
         
         if obj.snapchat!=None and len(SnapchatLink) !=0:
            obj.snapchat=SnapchatLink
            obj.save()
         else:
            pass
         
         if obj.spotify!=None and len(SpotifyLink) !=0:
            obj.spotify=SpotifyLink
            obj.save()
         else:
            pass
         
         if obj.telegram!=None and len(TelegramLink) !=0:
            obj.telegram=TelegramLink
            obj.save()
         else:
            pass
         
         if obj.twitch!=None and len(TwitchLink) !=0:
            obj.twitch=TwitchLink
            obj.save()
         else:
            pass
         
         if obj.twitter!=None and len(TwitterLink) !=0:
            obj.twitter=TwitterLink
            obj.save()
         else:
            pass
         
         if obj.whatsapp!=None and len(WhatsappLink) !=0:
            obj.whatsapp=WhatsappLink
            obj.save()
         else:
            pass

         if obj.website!=None and len(WebsiteLink) !=0:
            obj.website=WebsiteLink
            obj.save()
         else:
            pass
         
         if obj.youtube!=None and len(YouTubeLink) !=0:
            obj.youtube=YouTubeLink
            obj.save()
         else:
            pass
         
      except ObjectDoesNotExist:
         addlink=Link(amazon=AmazonLink, airbnb=AirbnbLink, blog=BlogLink, book=BookLink, cloud=CloudLink,codepen=CodepenLink, discord=DiscordLink, email=EmailLink, facebook=FacebookLink, github=GithubLink, google_drive=Google_DriveLink,google_forms=Google_FormsLink, google_play=Google_PlayLink, hackerRank=HackerRankLink,instagram=InstagramLink, linkedin=LinkedInLink, qr_code=QR_CodeLink, quora=QuoraLink, reddit=RedditLink, slideshare=SlideshareLink, spotify=SpotifyLink, snapchat=SnapchatLink, telegram=TelegramLink, twitch=TwitchLink, twitter=TwitterLink ,whatsapp=WhatsappLink ,website=WebsiteLink, youtube=YouTubeLink,owner=request.user)
         addlink.save()

   user = get_object_or_404(User, username=namers)
   linkers=Link.objects.get(owner=user)
   print(user)
   context={'linkers':linkers,'namers':namers}
   return render(request,'link/main.html',context)
   
@login_required(login_url='/link/login/')
def updatelinks(request):
   linkers=Link.objects.get(owner=request.user.id)
   context={'linkers':linkers}
   return render(request,'link/updatelinks.html',context)

@login_required(login_url='/link/login/')
def deletelinks(request):

   if request.method == 'POST':
      Airbnb=(request.POST.get('Airbnb','off'))
      Amazon=(request.POST.get('Amazon','off'))
      Blog=(request.POST.get('Blog','off'))
      Book=(request.POST.get('Book','off'))
      Cloud=(request.POST.get('Cloud','off'))
      Codepen=(request.POST.get('Codepen','off'))
      Discord=(request.POST.get('Discord','off'))
      Email=(request.POST.get('Email','off'))
      Facebook=(request.POST.get('Facebook','off'))
      Github=(request.POST.get('Github','off'))
      Google_Drive=(request.POST.get('Google-Drive','off'))
      Google_Forms=(request.POST.get('Google-Forms','off'))
      Google_Play=(request.POST.get('Google-Play','off'))
      HackerRank=(request.POST.get('HackerRank','off'))
      Instagram=(request.POST.get('Instagram','off'))
      LinkedIn=(request.POST.get('LinkedIn','off'))
      QR_Code=(request.POST.get('QR-Code','off'))
      Quora=(request.POST.get('Quora','off'))
      Reddit=(request.POST.get('Reddit','off'))
      Slideshare=(request.POST.get('Slideshare','off'))
      Snapchat=(request.POST.get('Snapchat','off'))
      Spotify=(request.POST.get('Spotify','off'))
      Telegram=(request.POST.get('Telegram','off'))
      Twitch=(request.POST.get('Twitch','off'))
      Twitter=(request.POST.get('Twitter','off'))
      Whatsapp=(request.POST.get('Whatsapp','off'))
      Website=(request.POST.get('Website','off'))
      YouTube=(request.POST.get('YouTube','off'))

      linkers=Link.objects.get(owner=request.user.id)
      
      if Amazon == 'on':
         linkers.amazon=''
         print("Deleted Executed")
         print('length of linkers.amazon is',len(linkers.amazon))
         linkers.save()
         
      if Airbnb == 'on':
         linkers.airbnb=''
         linkers.save()
         
      if Blog == 'on':
         linkers.blog=''
         linkers.save()
         
      if Book == 'on':
         linkers.book=''
         linkers.save()
         
      if Cloud == 'on':
         linkers.cloud=''
         linkers.save()
         
      if Codepen == 'on':
         linkers.codepen=''
         linkers.save()
         
      if Discord == 'on':
         linkers.discord=''
         linkers.save()
         
      if Email == 'on':
         linkers.email=''
         linkers.save()
         
      if Facebook == 'on':
         linkers.facebook=''
         linkers.save()
         
      if Github == 'on':
         linkers.github=''
         linkers.save()
         
      if Google_Drive == 'on':
         linkers.google_drive=''
         linkers.save()

      if Google_Forms == 'on':
         linkers.google_forms=''
         linkers.save()
         
      if Google_Play == 'on':
         linkers.google_play=''
         linkers.save()
         
      if HackerRank == 'on':
         linkers.hackerRank=''
         linkers.save()
         
      if Instagram == 'on':
         linkers.instagram=''
         linkers.save()
         
      if LinkedIn == 'on':
         linkers.linkedin=''
         linkers.save()
         
      if QR_Code == 'on':
         linkers.qr_code=''
         linkers.save()
         
      if Quora == 'on':
         linkers.quora=''
         linkers.save()
         
      if Reddit == 'on':
         linkers.reddit=''
         linkers.save()
         
      if Slideshare == 'on':
         linkers.slideshare=''
         linkers.save()
         
      if Snapchat == 'on':
         linkers.snapchat=''
         linkers.save()
         
      if Spotify == 'on':
         linkers.spotify=''
         linkers.save()
         
      if Telegram == 'on':
         linkers.telegram=''
         linkers.save()
         
      if Twitch == 'on':
         linkers.twitch=''
         linkers.save()
         
      if Twitter == 'on':
         linkers.twitter=''
         linkers.save()
         
      if Whatsapp == 'on':
         linkers.whatsapp=''
         linkers.save()
         
      if Website == 'on':
         linkers.website=''
         linkers.save()
         
      if YouTube == 'on':
         linkers.youtube=''
         linkers.save()
         
      messages.success(request, "Links Deleted Successfully.")
   
   linkers=Link.objects.get(owner=request.user.id)
   context={'linkers':linkers}
   return render(request,'link/deletelinks.html',context)

def test(request):
   return render(request,'link/test.html')   