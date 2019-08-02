# Ambassador Coding Challenge

Thank you for the opportunity to take part in this coding challenge. I very much enjoyed it and learned a lot in the process. I decided to take the back-end approach and create a browsable API. As you navigate to the API you'll notice that you can perform all CRUD actions on the link pages. I also went ahead and created a very simple front end page and landing page to show some full stack abilites. The links on the home page are clickable and you can create, edit, delete those links from the API. 

## Navigating App & Requirements

I deployed my app to heroku under the following link: [coding-challenge](https://mysterious-taiga-47695.herokuapp.com/)
You should be able to navigate the full app from this link. However, there are a few instructions you will need to input in the URL in order to get to and from the backend. To access the API just add a /api in the url: [API](https://mysterious-taiga-47695.herokuapp.com/api/). You can navigate into the API entries from the [Referrals Link](https://mysterious-taiga-47695.herokuapp.com/api/referrals/). As you navigate in and out of the API entries you'll see the ability to create entries, delete entries, and edit exisitng entries.

The [Home Page](https://mysterious-taiga-47695.herokuapp.com/) of the app represents a simple table with all of the referral links. As you click on each link you will be taken to the landing page where a basic message is displayed. One of the requirements that I was unable to accomplish was displaying the number of visits to the landing page. I was able to get a counter going from the following code but was having a hard time appending this information to the table for each link viewed.
```
def landing_page(request, pk):
    referral = Referral.objects.get(pk=pk)
    if PageView.objects.count() <= 0:
        x = PageView.objects.create()
        x.save()
    else:
        x = PageView.objects.all()[0]
        x.hits += 1
        x.save()
    print(x.hits)
    return render(request, 'landing.html', {'referral': referral})
```
## Technologies Used

I decided to create my app by using Python and the Django framework. I have experience from my coding boot camp in using these applications. I also used the Django Rest Framework and created a Rest_API. You will see in my source code that I utilized serializers from the rest_framework as well as routers, and viewsets. These modules made it very efficient to create the Rest API with minimal lines of code. The ModelViewSet module was particularly useful because it allowed me to use the built in CRUD actions instead of writing separate functions to create my own actions.  

For the front-end display I created a few HTML documents and employed some HTML commands to get it functioning. To style the table I used the most recent Bootstrap library. 

In order to deploy the app I used Heroku as instructed. The app is up and running and you can view all of the source code here on my github page. 

## Other Projects

Below are some links to projects that I've worked on. 

* [Web Scraping Application:](https://github.com/mjtabor1/TTA-Python-Projects/tree/master/TravelScrape)
...Description: You'll find the full details of the app and what I contributed too in the projects readme file. 
