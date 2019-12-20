from pywinauto import Desktop
from pywinauto.application import Application as App
import pywinauto
import time

app = App().start("C:/Users/kevs_/Downloads/vlc-3.0.6-win32.exe")
ctrl = app["Installer Language"]
mainctrl =app["VLC Installer"]
for i in range (0,20):
    ctrl.NextButton.click()
    ctrl.IAgree.click()
    ctrl.Select.click()
    ctrl.Ok.click()
    ctrl.Finish.click()
    mainctrl.NextButton.click()
    mainctrl.IAgree.click()
    mainctrl.Select.click()
    mainctrl.Ok.click()
    mainctrl.Finish.click()
    time.sleep(3)


'''
popup_dialog = Desktop(backend="win32").window(title="Some title")
# wait up to 10 seconds, return False if timed out
if popup_dialog.exists(timeout=10):
    popup_dialog.Trust.click() # or maybe .click_input()
    popup_dialog.wait_not('visible') # make sure it's gone (raise exception otherwise)
'''
