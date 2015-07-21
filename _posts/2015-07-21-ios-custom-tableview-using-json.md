---
layout: post
title: IOS Custom Table View with image and text using Json
date: '2015-07-21 00:00:00'
---

I am going to explain even more customized table view like Facebook, Google+ news feed where it contains multiple images and texts.
I am going to use this example json to load the list data. This json contains array of objects where the each object contains information user profile image, user name, user url, user status and time stamp.

{% highlight json %} 
  {
    "feed": [
        {
            "id": 1,
            "name": "Asil Arslan",
            "status": "Lorem Ipsum, dizgi ve baskı endüstrisinde kullanılan mıgır metinlerdir. Lorem Ipsum, adı bilinmeyen bir matbaacının bir hurufat numune kitabı oluşturmak üzere bir yazı galerisini alarak karıştırdığı 1500'lerden beri endüstri standardı sahte metinler olarak kullanılmıştır.",
            "profilePic": "http://mobilprojem.com/feed/img/me.jpg",
            "timeStamp": "1437496200",
            "url": "null"
        },
        
        ...
        
      ]
   }
{% endhighlight %}
