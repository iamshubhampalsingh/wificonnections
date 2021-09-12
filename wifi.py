import oneplus.setting as settings
###########################################################################    
def switchwifiOn(device):
    settings.gotoSettings(device)
    print("To Switch Wifi On")
    wifiStatus=__getwifiStatus(device)
    if wifiStatus==True:
        print("Wifi is Already On")
    else:
        __switchWifi(device)
###########################################################################    
def switchwifiOff(device):
    settings.gotoSettings(device)
    print("To switch Wifi Off")
    wifiStatus=__getwifiStatus(device)
    if wifiStatus==False:
        print("Wifi is Already Off")
    else:
        __switchWifi(device)
############################################################################# 
def connecttoWifi(device,wifiName,password):
    settings.gotoSettings(device)
    if __getwifiStatus(device)==True:
        __clickWifiMenu(device)
        __selectWifi(device, wifiName)
        __setPassword(device, password)
        __clickConnectWifi(device)
    else:
        __switchWifi(device)
        __clickWifiMenu(device)
        __selectWifi(device, wifiName)
        __setPassword(device, password)
        __clickConnectWifi(device)
    
    

    
    
###########################################################################################    
def __getwifiStatus(device):
    __clickWifiNetwork(device)
    wifiStatus=device(className="android.widget.FrameLayout",resourceId="com.android.settings:id/action_bar_root",index="0").child(className="android.widget.FrameLayout",resourceId="android:id/content",index="0").child(className="android.widget.FrameLayout",resourceId="com.android.settings:id/content_parent",index="0").child(className="android.widget.FrameLayout",resourceId="com.android.settings:id/content_frame",index="0").child(className="android.widget.LinearLayout",index="0").child(className="android.widget.FrameLayout",resourceId="com.android.settings:id/main_content",index="0").child(className="android.widget.LinearLayout",resourceId="com.android.settings:id/container_material",index="0").child(className="android.widget.FrameLayout",resourceId="android:id/list_container",index="0").child(className="android.widget.RelativeLayout",index="0").child(className="androidx.recyclerview.widget.RecyclerView",resourceId="com.android.settings:id/recycler_view",index="0").child(className="android.widget.LinearLayout",index="1").child(className="android.widget.LinearLayout",resourceId="com.android.settings:id/two_target_divider",index="1").child(className="android.widget.LinearLayout",resourceId="android:id/widget_frame",index="1").child(className="android.widget.Switch",resourceId="com.android.settings:id/switchWidget",index="0").get_text()
    if wifiStatus=='ON':
        print("Wifi is On")
        return True
    if wifiStatus=='OFF':
        print("Wifi is Off")
        return False


def __clickWifiNetwork(device):
    device(className="androidx.recyclerview.widget.RecyclerView",resourceId="com.android.settings:id/recycler_view").child(className="android.widget.LinearLayout").child(className="android.widget.LinearLayout").child(className="android.widget.FrameLayout",resourceId="com.android.settings:id/icon_frame").click()

def __clickWifiMenu(device):
    device(className="android.widget.FrameLayout",resourceId="com.android.settings:id/action_bar_root",index="0").child(className="android.widget.FrameLayout",resourceId="android:id/content",index="0").child(className="android.widget.FrameLayout",resourceId="com.android.settings:id/content_parent",index="0").child(className="android.widget.FrameLayout",resourceId="com.android.settings:id/content_frame",index="0").child(className="android.widget.LinearLayout",index="0").child(className="android.widget.FrameLayout",resourceId="com.android.settings:id/main_content",index="0").child(className="android.widget.LinearLayout",resourceId="com.android.settings:id/container_material",index="0").child(className="android.widget.FrameLayout",resourceId="android:id/list_container",index="0").child(className="android.widget.RelativeLayout",index="0").child(className="androidx.recyclerview.widget.RecyclerView",resourceId="com.android.settings:id/recycler_view",index="0").child(className="android.widget.LinearLayout",index="1").child(className="android.widget.LinearLayout",index="0").child(className="android.widget.RelativeLayout",resourceId="com.android.settings:id/text_layout",index="0").child(className="android.widget.TextView",resourceId="android:id/title",index="0").click()
    print("To open wifi interface")

def __switchWifi(device):
    device(className="android.widget.FrameLayout",resourceId="com.android.settings:id/action_bar_root",index="0").child(className="android.widget.FrameLayout",resourceId="android:id/content",index="0").child(className="android.widget.FrameLayout",resourceId="com.android.settings:id/content_parent",index="0").child(className="android.widget.FrameLayout",resourceId="com.android.settings:id/content_frame",index="0").child(className="android.widget.LinearLayout",index="0").child(className="android.widget.FrameLayout",resourceId="com.android.settings:id/main_content",index="0").child(className="android.widget.LinearLayout",resourceId="com.android.settings:id/container_material",index="0").child(className="android.widget.FrameLayout",resourceId="android:id/list_container",index="0").child(className="android.widget.RelativeLayout",index="0").child(className="androidx.recyclerview.widget.RecyclerView",resourceId="com.android.settings:id/recycler_view",index="0").child(className="android.widget.LinearLayout",index="1").child(className="android.widget.LinearLayout",resourceId="com.android.settings:id/two_target_divider",index="1").child(className="android.widget.LinearLayout",resourceId="android:id/widget_frame",index="1").child(className="android.widget.Switch",resourceId="com.android.settings:id/switchWidget",index="0").click()

def __listAvailableWifi(device):
    device(className="android.widget.FrameLayout",resourceId="com.android.settings:id/action_bar_root",index="0").child(className="android.widget.FrameLayout",resourceId="android:id/content",index="0").child(className="android.widget.FrameLayout",resourceId="com.android.settings:id/content_parent",index="0").child(className="android.widget.FrameLayout",resourceId="com.android.settings:id/content_frame",index="0").child(className="android.widget.LinearLayout",index="0").child(className="android.widget.FrameLayout",resourceId="com.android.settings:id/main_content",index="0").child(className="android.widget.LinearLayout",resourceId="com.android.settings:id/container_material",index="0").child(className="android.widget.FrameLayout",resourceId="android:id/list_container",index="0").child(className="android.widget.RelativeLayout",index="0").child(className="androidx.recyclerview.widget.RecyclerView",resourceId="com.android.settings:id/recycler_view",index="0").child(className="android.widget.LinearLayout",index="1").child(className="android.widget.LinearLayout",index="0").child(className="android.widget.RelativeLayout",resourceId="com.android.settings:id/text_layout",index="0").child(className="android.widget.TextView",resourceId="android:id/title",index="0").click()

def __selectWifi(device,wifiName):
    device(className="android.widget.FrameLayout",resourceId="com.android.settings:id/main_content",index="1").child(className="android.widget.LinearLayout",resourceId="com.android.settings:id/container_material",index="0").child(className="android.widget.FrameLayout",resourceId="android:id/list_container",index="1").child(className="android.widget.RelativeLayout",index="0").child(className="androidx.recyclerview.widget.RecyclerView",resourceId="com.android.settings:id/recycler_view",index="0").child(className="android.widget.LinearLayout").child(className="android.widget.LinearLayout").child(className="android.widget.RelativeLayout",index="1").child(className="android.widget.LinearLayout",resourceId="com.android.settings:id/layout_title",index="0").child(className="android.widget.TextView",resourceId="android:id/title",text=wifiName).click()

def __setPassword(device,password):
    device(className="android.widget.FrameLayout",resourceId="com.android.settings:id/main_content",index="0").child(className="android.widget.RelativeLayout",index="0").child(className="android.widget.ScrollView",resourceId="com.android.settings:id/dialog_scrollview",index="0").child(className="android.widget.LinearLayout",resourceId="com.android.settings:id/l_wifidialog",index="0").child(className="android.widget.LinearLayout",resourceId="com.android.settings:id/security_fields",index="1").child(className="android.widget.LinearLayout",resourceId="com.android.settings:id/password_layout",index="0").child(className="android.widget.EditText",resourceId="com.android.settings:id/password",index="1").set_text(password)

def __clickConnectWifi(device):
    device(className="android.widget.FrameLayout",resourceId="com.android.settings:id/main_content",index="0").child(className="android.widget.RelativeLayout",index="0").child(className="android.widget.ScrollView",resourceId="com.android.settings:id/add_network_button_bar",index="1").child(className="android.widget.RelativeLayout",index="0").child(className="android.widget.Button",resourceId="android:id/button1",index="1").click()

