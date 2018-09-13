import random


def randomChoiceHeaders():
    ua_list =[
        "A8TV_IPhone / 300400 CFNetwork / 901.1 Darwin / 17.6.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        "Dalvik/2.1.0 (Linux; U; Android 8.0.0; HWI-AL00 Build/HUAWEIHWI-AL00)",
        "A8TV_IPhone/4.5.0 (iPhone; iOS 11.3.1; Scale/3.00)"
    ]

    user_agent = random.choice(ua_list)
    return user_agent