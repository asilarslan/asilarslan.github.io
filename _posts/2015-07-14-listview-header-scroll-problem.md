---
layout: post
title: ListView Header Scroll Problem in Android
date: '2015-07-16 23:16:00'
---

When i scroll on header with listview. Listview scroll header background. But i want scroll with header. We add header view for listviews header for scrolling.

{% highlight xml %}
<LinearLayout>
  <LinearLayout>
  <!--Header-->
  <LinearLayout/>
  <ListView/>
<LinearLayout/>

{% endhighlight %}

We convert 2 view, such as;

{% highlight xml %}
<LinearLayout>
  <LinearLayout>
  <!--Header-->
  <LinearLayout/>
<LinearLayout/>

{% endhighlight %}

{% highlight xml %}
<LinearLayout>
  <ListView/>
<LinearLayout/>

{% endhighlight %}

after implement header with listview

{% highlight java %}
private ListView lv;
private View post;

@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_post_detail);

    post=getLayoutInflater().inflate(R.layout.view_post, null);

    lv = (ListView)findViewById(R.id.listView);
    lv.addHeaderView(post);
    lv.setAdapter(new CommentAdapter(this));
    
    ...
}
{% endhighlight %}
