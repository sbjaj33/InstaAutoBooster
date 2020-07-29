from instapy import InstaPy
import eel

eel.init('web')

@eel.expose
def boostinstagram(username1,password1,tag1):

    session = InstaPy(username=username1, password=password1,headless_browser=True)
    session.login()
    session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)
    session.set_relationship_bounds(enabled=True, max_followers=8500)
    tagslist=tag1.split(',')
    session.like_by_tags(tagslist, amount=5)
    session.set_dont_like(["naked", "nsfw"])
    session.set_do_follow(True, percentage=50)
    session.set_do_comment(True, percentage=50)
    session.set_comments(["Nice!", "Sweet!", "Beautiful :heart_eyes:"])
    session.end()

eel.start('index.html',size=(1000,600))
