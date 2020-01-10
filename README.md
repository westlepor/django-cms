
![amfoss-cms-cover](https://user-images.githubusercontent.com/21276922/51844359-12628580-233b-11e9-891a-d4d826bd1d6e.png)

Club Management System (CMS) is django-based web-app which lays framework for the amfoss website, the amfoss webapp, and the amfoss app. 


## [Installation Instructions](https://github.com/amfoss/cms/wiki/Installation)
The portal is primarily a django based application, and to set it up we require to have 
python environment with django and other project dependencies installed. Though one can
work with the project without an virtual environment,  it is recommended to use one so 
as to avoid conflicts with other projects.

0. Make sure that you have `Python 3`, `python-3-devel`, `gcc`, `virtualenv`, and `pip` installed.     
1. Clone the repository
   
    ```
        $ git clone https://github.com/amfoss/cms.git
        $ cd cms
    ```
2. Create a python 3 virtualenv, and activate the environment.
    ```bash
        $ virtualenv -p python3 .
        $ source bin/activate
    ```   
3. Install the project dependencies from `requirements.txt`
    ```
        $ pip install -r requirements.txt
    ```

You have now successfully set up the project on your environment. If you encounter any problems during installation, you can refer to [installation page on our wiki](https://github.com/amfoss/cms/wiki/Installation).

### After Setting Up
From now when you start your work, run ``source bin/activate`` inside the project repository and you can work with the django application as usual - 

* `python manage.py migrate` - set up database
* `python manage.py createsuperuser` - create admin user
* `python manage.py runserver`  - run the project locally

*Make sure you pull new changes from remote regularly.*


## Data Models

### Activities
The activity app tracks the activities of the club members.

1. **Certificates** - carries certificates recieved by club members, also allows to upload them as attachments.
2. **Courses** - records courses completed by club members, includes link to certificate.
3. **Events** - logs events attended by student members such as Conference, Hackathons, Internships, Exchange Programmes etc.
4. **Honours** - records achievements and honours recieved by club members, includes link to project, certificate.
5. **Projects** - holds projects of the club, club teams and club members
6. **Publications** - records publications made by club members
7. **Talks** - records talks given by club members

### Members
The members app manages the profile and data of the club members

1. **Groups** - manages groups inside the club
2. **Leave Records** - records and manages the leave requests of club members
3. **Mentor Groups** - manages mentor-menteee relationship of club members
4. **Profiles** - manages the member profile
5. **Responsibilities** - manages the various responsibilities held by a group of members
6. **Teams** - manages the various internal teams inside the club

### Status
The status app manages the reporting system in the club
 
1. **Log** - holds status updates posted by members, under different threads, for various subjects. 
2. **Thread** - manages status update threads

## API

The amFOSS CMS ships with GraphQL-based APIs. To help developers, GraphiQL, a tabbed interface (playground) for editing and testing our GraphQL queries/mutations, also has been furnished .

Documentation on the supported APIs has been provided in the [wiki page](https://github.com/amfoss/cms/wiki/APIs).

## Integrations

1. **Attendance Module** - the amFOSS attendance module is a raspberry-pi which live records the attendance of club members when they are in the FOSSLab. The AmFOSS CMS fetches attendance details from it and logs it.
2. **Telegram Bot** - the amFOSS Telegram Bot is the bot assistant of the amFOSS Telegram group. The AmFOSS CMS triggers the bot to send notifications, statistics etc. to the group.
4. **GitHub** - Integrates with GitHub to actively track the FOSS contributions made by club members

## Tech Stack

* **Language:**  Python 3.7
* **Framework:** Django 2.2
* **API:** GraphQL (Graphene + JWT)


[build-badge]:https://api.travis-ci.org/amfoss/cms.svg?branch=master
[build]:https://travis-ci.org/amfoss/cms
[contributors-badge]:https://img.shields.io/github/contributors/amfoss/cms.svg
[contributors]: https://github.com/amfoss/cms/graphs/contributors
[watchers-badge]:https://img.shields.io/github/watchers/amfoss/cms.svg?style=social
[watchers]: https://github.com/amfoss/cms/watchers
[stars-badge]:https://img.shields.io/github/stars/amfoss/cms.svg?style=social
[stargazers]:https://github.com/amfoss/cms/stargazers
[forks-badge]: https://img.shields.io/github/forks/amfoss/cms.svg?style=social
[forks]: https://github.com/amfoss/cms/network/members
[license-badge]: https://img.shields.io/github/license/amfoss/cms.svg
[license]: https://github.com/amfoss/gitlit/blob/master/LICENSE
[issues-badge]: https://img.shields.io/github/issues/amfoss/cms.svg
[issues]: https://github.com/amfoss/cms/issues
[pr-badge]:https://img.shields.io/github/issues-pr/amfoss/cms.svg
[prs]: https://github.com/amfoss/cms/pulls

