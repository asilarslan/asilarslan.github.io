---
layout: post
title: Changing locale and reload resources
date: '2013-09-22 00:00:00'
---
When the language is switched, You would like all the textviews etc to change language immediately
{% highlight java %}
public void setLocale(String lang) {

        Locale locale= new Locale(lang);
        Locale.setDefault(locale);

        Configuration config = new Configuration();
        config.locale = locale;

        Resources res = getResources();
        DisplayMetrics dm = res.getDisplayMetrics();
        Configuration conf = res.getConfiguration();
        conf.locale = locale;
        res.updateConfiguration(conf, dm);

        onConfigurationChanged(conf);

    }


    @Override
    public void onConfigurationChanged(Configuration newConfig)
    {
        initPager();
        initSplashMenu();
        initLangButton();

        super.onConfigurationChanged(newConfig);

    }
{% endhighlight %}
