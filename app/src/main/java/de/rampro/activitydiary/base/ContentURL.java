package de.rampro.activitydiary.base;

public class ContentURL {

    //    获取指定日期对应的历史上的今天的网址
    public static String getTodayHistoryURL(String version, int month, int day) {
        String url = "http://api.juheapi.com/japi/toh?v=" + version + "&month=" + month + "&day=" + day + "&key=ed068c28d5db85cb0e6d9e519560a48c";
        return url;
    }

    //    获取指定日期的老黄历的网址
    public static String getLaohuangliURL(String time) {
        String url = "http://v.juhe.cn/laohuangli/d?date=" + time + "&key=91a19dc709c7da5a46b7adea5e0ae62d";
        return url;
    }

//    http://api.juheapi.com/japi/tohdet?key=6a877b186ccd134296d131183b74c9f4&v=1.0&id=18401114

    //    根据指定事件id获取指定事件详情信息
    public static String getHistoryDescURL(String version, String id) {
        String url = "http://api.juheapi.com/japi/tohdet?key=ed068c28d5db85cb0e6d9e519560a48c&v=" + version + "&id=" + id;
        return url;
    }
}
