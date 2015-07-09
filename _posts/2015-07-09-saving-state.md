---
layout: post
title: Saving Activity State in Android
date: '2015-07-09 23:16:00'
---

We are using `Intent()`, when we want start other activity. Also we send data with start activities. We want use transition between more than 2 activities, such as FirstActivity, SecondActivity, ThirdActivity. 

FirstActivity (with intent extra) -> SecondActivity (with intent extra) -> ThirdActivity

No problems starting activies, but we want back previous parent activity using back actionbar button or device button return null values because SecondActiviy get intent from First Activity. Now we solving this problem with save state.

FirstActivity (null) <- SecondActivity (null) <- ThirdActivity

We call `onSaveInstanceState` and `onRestoreInstanceState` methods

{% highlight java %}
static final String STATE_SECOND_ACTIVITY = "secondActivity";

int mValue;

@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_second_activity);

    // Check whether we're recreating a previously destroyed instance
    if (savedInstanceState != null) {
        // Restore value of members from saved state
        mValue = savedInstanceState.getInt(STATE_SECOND_ACTIVITY);
    } else {
        //get value from FirstActiviy
        Intent i=getIntent();
        mValue=i.getIntExtra("firstActivity");
    }

        ...
}
{% endhighlight %}

{% highlight java %}
@Override
public void onSaveInstanceState(Bundle savedInstanceState) {
    // Save the user's current game state
    savedInstanceState.putInt(STATE_SECOND_ACTIVITY, mValue);

    // Always call the superclass so it can save the view hierarchy state
    super.onSaveInstanceState(savedInstanceState);
  }
    
{% endhighlight %}

{% highlight java %}
public void onRestoreInstanceState(Bundle savedInstanceState) {
    // Always call the superclass so it can restore the view hierarchy
    super.onRestoreInstanceState(savedInstanceState);

    // Restore state members from saved instance
    mValue = savedInstanceState.getInt(STATE_SECOND_ACTIVITY);
    }
{% endhighlight %}
