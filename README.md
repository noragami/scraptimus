# scraptimus
========
[![MIT License][License Image]][License]
[![Python Version][Python Image]][Python]
![Project Status: Active][Project Status Image]

 ______  ______  ______  ______  ______  ______  __  __    __  __  __  ______    
/\  ___\/\  ___\/\  == \/\  __ \/\  == \/\__  _\/\ \/\ "-./  \/\ \/\ \/\  ___\   
\ \___  \ \ \___\ \  __<\ \  __ \ \  _-/\/_/\ \/\ \ \ \ \-./\ \ \ \_\ \ \___  \  
 \/\_____\ \_____\ \_\ \_\ \_\ \_\ \_\     \ \_\ \ \_\ \_\ \ \_\ \_____\/\_____\ 
  \/_____/\/_____/\/_/ /_/\/_/\/_/\/_/      \/_/  \/_/\/_/  \/_/\/_____/\/_____/ 

========
## What's this?
It's a Python command line scraper for accessing the list of games found at [Co-optimus website](https://www.co-optimus.com).


## Disclaimer 
I'm not affiliate with Co-optimus in any way.
These pieces of software are written for studying/learning purpose.
The data retrieved from this software is property of Co-optimus.
Please do not use any of the data retrieved from this software without the explicit consent of Co-optimus.


## How do I use this?
Clone the repository & run `python setup.py develop`. (Or [download](/noragami/scraptimus/archive/master.zip) it & run `python setup.py install`, which copies the code to your local Python packages folder)

    usage: python -m scraptimus [-h] [-f FILENAME] [-j | -c] [-s STARTPAGE]
                                [-e ENDPAGE]

    Scrape and export to a file the list of games found at Co-optimus website.
    Default format is json.

    optional arguments:
    -h, --help            show this help message and exit
    -f FILENAME, --filename FILENAME
                            Override the default filename
    -j, --json            Export to a json file
    -c, --csv             Export to a csv file
    -s STARTPAGE, --startpage STARTPAGE
                            Define where to start. Default is 1
    -e ENDPAGE, --endpage ENDPAGE
                            Define where to end. Default is all the pages

Result example:

CSV:
```
id|title|genre|system|online|couch|combo|features|review_score|user_rating|release_date
1267|'Splosion Man|Platformer|360|4|4|0|4players-icon,online-icon,couch-icon|4.5|3.5|07/22/2009
1440|0 Day Attack on Earth|Twin Stick Shooter|360|4|0|0|4players-icon,online-icon|2.0|2.0|12/23/2009
1541|007: Everything or Nothing|Action/Adventure|XBOX|0|2|0|2players-icon,couch-icon,split-icon||2.5|02/17/2004
[...]
```

JSON:
```
[
    {
        "id": "1267",
        "title": "'Splosion Man",
        "genre": "Platformer",
        "system": "360",
        "online": 4,
        "couch": 4,
        "combo": 0,
        "features": "4players-icon,online-icon,couch-icon",
        "review_score": 4.5,
        "user_rating": 3.5,
        "release_date": "07/22/2009"
    },
    {
        "id": "1440",
        "title": "0 Day Attack on Earth",
        "genre": "Twin Stick Shooter",
        "system": "360",
        "online": 4,
        "couch": 0,
        "combo": 0,
        "features": "4players-icon,online-icon",
        "review_score": 2.0,
        "user_rating": 2.0,
        "release_date": "12/23/2009"
    },
    {
        "id": "1541",
        "title": "007: Everything or Nothing",
        "genre": "Action/Adventure",
        "system": "XBOX",
        "online": 0,
        "couch": 2,
        "combo": 0,
        "features": "2players-icon,couch-icon,split-icon",
        "review_score": null,
        "user_rating": 2.5,
        "release_date": "02/17/2004"
    },
    {...}
]
```


### Licence
MIT

[License Image]: https://img.shields.io/badge/license-MIT-brightgreen.svg "MIT License"
[License]: https://github.com/noragami/scraptimus/blob/master/LICENSE "MIT License"

[Python Image]: https://img.shields.io/badge/python-3.5-blue.svg "Python Version: 3.5"
[Python]: https://docs.python.org/3.5/whatsnew/changelog.html#python-3-5-0-final "Python 3.5 Changelog" 

[Project Status Image]: https://img.shields.io/badge/project-active-green.svg "Project Status: Active"
