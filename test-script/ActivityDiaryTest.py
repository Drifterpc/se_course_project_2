import time

import uiautomator2 as u2

def wait(seconds = 2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)

if __name__ == '__main__':

    d = u2.connect("emulator-5554")

    # print(d.info)

    d.app_start('de.rampro.activitydiary.debug')
    d.implicitly_wait(10)

    # 点击导航栏
    out = d(description="Open navigation").click()
    if not out:
        print("Success: 点击导航栏")
    wait()

    # 点击“histoy today”模块
    out = d(resourceId="de.rampro.activitydiary.debug:id/design_menu_item_text", text="history today").click()
    if not out:
        print("Success: 点击“histoy today”模块")
    wait()

    # 点击第一个事件
    out = d.xpath('//*[@resource-id="de.rampro.activitydiary.debug:id/main_lv"]/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]').click()
    if not out:
        print("Success: 点击第一个事件")
    wait()

    # 点击退出
    out = d(resourceId="de.rampro.activitydiary.debug:id/desc_back_iv").click()
    if not out:
        print("Success: 点击退出")
    wait()

    while True:
        d.swipe_ext('up')
        page_connect = d.dump_hierarchy()[(len(d.dump_hierarchy())) // 2:]
        # time.sleep(0.5)
        new_page_connect = d.dump_hierarchy()[(len(d.dump_hierarchy())) // 2:]
        if page_connect == new_page_connect:
            break

    while True:
        d.swipe_ext('up')
        page_connect = d.dump_hierarchy()[(len(d.dump_hierarchy())) // 2:]
        # time.sleep(0.5)
        new_page_connect = d.dump_hierarchy()[(len(d.dump_hierarchy())) // 2:]
        if page_connect == new_page_connect:
            break

    # d.swipe_ext("down")

    # 点击加载更多
    out = d(text="点击加载更多").click()
    if not out:
        print("Success: 点击加载更多")
    wait()

    # 点击新加载出来的事件
    out = d.xpath('//*[@resource-id="de.rampro.activitydiary.debug:id/history_lv"]/android.widget.LinearLayout[5]/android.widget.LinearLayout[2]').click()
    if not out:
        print("Success: 点击新加载出来的事件")
    wait()

    # 点击退出事件
    out = d(resourceId="de.rampro.activitydiary.debug:id/desc_back_iv").click()
    if not out:
        print("Success: 击退出事件")
    wait()

    # 点击退出新加载的页面
    out = d(resourceId="de.rampro.activitydiary.debug:id/history_iv_back").click()
    if not out:
        print("Success: 点击退出新加载的页面")
    wait()

    # 点击日历
    out = d(resourceId="de.rampro.activitydiary.debug:id/main_imgbtn").click()
    if not out:
        print("Success: 点击日历")
    wait()

    # 点击切换月份
    out = d(resourceId="android:id/next").click()
    if not out:
        print("Success: 点击切换月份")
    wait()

    # 点击切换日期
    out = d(text="10").click()
    if not out:
        print("Success: 击切换日期")
    wait()

    # 点击ok
    out = d(resourceId="android:id/button1").click()
    if not out:
        print("Success: 点击ok")
    wait()

    # 点击切换日期后的事件
    out = d.xpath('//*[@resource-id="de.rampro.activitydiary.debug:id/main_lv"]/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]').click()
    if not out:
        print("Success: 点击切换日期后的事件")
    wait()

    #点击退出事件
    out = d(resourceId="de.rampro.activitydiary.debug:id/desc_back_iv").click()
    if not out:
        print("Success: 点击退出事件")
    wait()

    #点击退出“history today”模块
    out = d.xpath('//*[@resource-id="com.android.systemui:id/ends_group"]/android.widget.RelativeLayout[2]').click()
    if not out:
        print("Success: 点击退出“history today”模块")
    wait()