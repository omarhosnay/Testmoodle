from django.shortcuts import render
from django.http.request import HttpRequest
from urllib.request  import urlopen
import json


# global token
# global url
# Create your views here.


def index(req:HttpRequest):
    
    
    if req.method == 'POST':

        
        
        '''
        main vars
        '''
        token            = 'b7d481ee5afe361cc31f5ee05bb8968c'
        url              = 'https://moodle-138098-0.cloudclusters.net/webservice/rest/server.php?'
        available_cources = []
        avilable_Category_for_cources = []
        categories = []

        
        
        
        '''
        <i class="fa-regular fa-star"></i>  not favrite

        <i class="fa-solid fa-star"></i>    is favorite
        '''
        
        
        '''
        Get courses
        '''
        urlcourse        = f'{url}wstoken={token}&wsfunction=core_enrol_get_users_courses&userid=2&moodlewsrestformat=json'
        datacourse       = urlopen(urlcourse).read()
        formattedcourses = json.loads(datacourse)
        for i in formattedcourses:
            available_cources.append(i)
        
        
        
        '''
        Get categories
        '''
        
        urlCate = f'{url}wstoken={token}&wsfunction=core_course_get_categories&moodlewsrestformat=json'
        dataCate = urlopen(urlCate).read()
        formattedCate = json.loads(dataCate)

        
        
        '''
        Match the ctegorie with the course
        '''
        print(formattedCate)
        for course in available_cources :
            categoryforcourse = course['category']
            for category in formattedCate:
                idcat = category['id']
                if idcat == categoryforcourse:
                    categories.append(category['name'])
                    
            avilable_Category_for_cources.append({
                'name' : f"{course['shortname']}",
                'categories' : categories,
                })
        print(avilable_Category_for_cources)
        var = {
            'data' : avilable_Category_for_cources
            
        }
        return render (req, 'core/index.html', var)
        
        
        
        
                
    return render(req, 'core/index.html')