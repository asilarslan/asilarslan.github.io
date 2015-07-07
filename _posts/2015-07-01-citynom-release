---
layout: post
title: CityNom Release
date: '2015-06-30 16:30:02'
---

Android Material Design is the most powerful design i have seen. And we can create custom material actinbar with toolbar. First of all, we must create `tool_bar.xml` in layout folder.

{% highlight xml %}
<span style="font-size: x-small;"><?xml version="1.0" encoding="utf-8"?>
<android.support.v7.widget.Toolbar xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:background="@color/ColorPrimary"
    android:elevation="4dp"
 
    >
 
</android.support.v7.widget.Toolbar>
 
</span>
{% endhighlight %}

After we include this toolbar activity to my layout

{% highlight xml %}
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools" android:layout_width="match_parent"
    android:layout_height="match_parent">

    <include layout="@layout/tool_bar" />

</RelativeLayout>
{% endhighlight %}

After we get this toolbar to my activity

{% highlight java %}
private Toolbar toolbar;                              // Declaring the Toolbar Object
 
@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
  setContentView(R.layout.activity_main);
 
  toolbar = (Toolbar) findViewById(R.id.tool_bar); // Attaching the layout to the toolbar object
  setSupportActionBar(toolbar);                   // Setting toolbar as the ActionBar with setSupportActionBar() call
 
}
{% endhighlight %}

We can find other refence from https://developer.android.com/reference/android/widget/Toolbar.html
