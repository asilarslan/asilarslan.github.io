---
layout: post
title: Create Right Navigation Drawer
date: '2015-07-09 22:16:00'
---

Android Left Navigation Drawer useful for navigate between activities, fragments or others. But Right Navigation Drawer useful for may be Notifications. Many Application using right navigation drawer for notification, such as [Google Plus](https://play.google.com/store/apps/details?id=com.google.android.apps.plus),  [Stack Excange](https://play.google.com/store/apps/details?id=com.stackexchange.marvin).

If you create default left navigation drawer, check [Android Developer Documents](https://developer.android.com/training/implementing-navigation/nav-drawer.html). Now we create right navigation drawer. First of we create default left navigation activity, when opening Android Studio.

After we apply ListVİew `android:layout_gravity="right"`

{% highlight xml %}
<android.support.v4.widget.DrawerLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/drawer_layout"
    android:layout_width="match_parent"
    android:layout_height="match_parent">
    <!-- The main content view -->
    <FrameLayout
        android:id="@+id/content_frame"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />
    <!-- The navigation drawer -->
    <ListView android:id="@+id/right_drawer"
        android:layout_width="280dp"
        android:layout_height="match_parent"
        android:choiceMode="singleChoice"
        android:divider="@android:color/transparent"
        android:dividerHeight="0dp"
        android:background="#111"
        android:layout_gravity="right"/>
</android.support.v4.widget.DrawerLayout>
{% endhighlight %}

After, we create notification menu click event 

{% highlight java%}
@Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        if (id == R.id.action_notification) {
            if (mDrawerLayout.isDrawerOpen(Gravity.RIGHT)) {
                mDrawerLayout.closeDrawer(Gravity.RIGHT);
            } else {
                mDrawerLayout.openDrawer(Gravity.RIGHT);
            }
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
{% endhighlight %}

You can find other refence from [Sample Application](https://github.com/asilarslan/MaterialNotification)
