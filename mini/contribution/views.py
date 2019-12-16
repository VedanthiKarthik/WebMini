from django.shortcuts import render,redirect
from calc.models import Courses
from django.contrib import messages

from urllib.request import urlopen,Request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
# Create your views here.


# Step 2
# Create Generic URL retrieval function
def get_site_file(url):
    """
    url - base url to access desired web file
    """    
    try:
        html = urlopen(url)
        bs = BeautifulSoup(html, 'html.parser')
        return bs
    
    except HTTPError as e:
        print(e)

def contribution(request):
    if request.method == 'POST':
         course_url             = request.POST['course_url']
         description            = request.POST['description']
         rating                 = request.POST['rating']
        #  price                  = request.POST['rating']
         crs_list=Courses.objects.all()
         
         for course in crs_list:
             if course.course_urls==course_url:
                 messages.info(request,"course already exist")
                 return redirect('contribution')
         site=course_url.split('.')[1]
         if(site=='udemy'):
             req = Request(course_url, headers={'User-Agent': 'Mozilla/5.0'})
             page_content = get_site_file(req)  #urlopen(req).read()
             try:
                  discovery_course = page_content.find("title")
                  discovery_course_imga = page_content.findAll("img")
                                       # {"class",'styles--introduction-asset--Q9xDo'})#styles--introduction-asset__img--9iitL
                #   discovery_course_rating = page_content.find("span", \
                #                          {'aria-label':'Rating: 4.0 out of 5'})
             except AttributeError as e:
                 messages.info(request,'Course already exist')
                 return redirect('contribution')
                 print(discovery_course.get_text())
                #  print(discovery_course_rating)
         else:
             page_content = get_site_file(course_url)
             try:
                  discovery_course = page_content.find('title')
                #   discovery_course_title = page_content.find("img", \
                #                          {'class':domains_list[domain][1]})
                  rating = page_content.find("span", \
                                         {'data-test':'number-star-rating'})
                  rating=rating.get_text()
    
             except AttributeError as e:
                   print('Something seems to be missing with the tag')
             # print(discovery_course_name)
             # print(discovery_course_title)
            #  print(discovery_course_title['src'])
            #  print(discovery_course_rating.get_text())
            #  discovery_course_name.get_text()



         l=[rating,description,course_url,discovery_course.get_text(),site]
         c= Courses(title=discovery_course.get_text(),price=122,rating=rating,course_urls=course_url,description=description)
         c.save()
         messages.info(request,"Thanks for your contribution")
         return redirect('contribution')
    else:
        return render(request,'contribution.html')


def showall(request):
    crs_list=Courses.objects.all()[::-1]
    return render(request,'showcourse.html',{'courses':crs_list})

def about(request):
    return render(request,'about.html')