from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import dp


from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.utils.fitimage import FitImage
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivy.core.window import Window
w=Window.size = 400,800
# w=Window.size
# from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivy.factory import Factory

import glob

from kivymd.toast import toast




class WelcomeScreen(Screen):
    pass


class MainPage(Screen):
    pass

class ProductsPage(Screen):
    pass

class ProductsDeatailsPage(Screen):
    pass


class AboutPage(Screen):
    pass


class ProfilePage(Screen):
    pass


sm = ScreenManager()

sm.add_widget(WelcomeScreen(name='WelcomeScreen'))
sm.add_widget(MainPage(name='MainPage'))
sm.add_widget(AboutPage(name='AboutPage'))
sm.add_widget(ProfilePage(name='ProfilePage'))
sm.add_widget(ProductsPage(name='ProductsPage'))
sm.add_widget(ProductsDeatailsPage(name='ProductsDeatailsPage'))

from kivy.uix.anchorlayout import AnchorLayout
    
# class DetailsContent(MDBoxLayout):
#     window_height= w[1]
#     pass
        
class Main(MDApp):
    path_to_kv_file='kv_file.kv'
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.onBackKey)
        self.count_back=0


    def build(self):
        self.theme_cls.primary_palette = "DeepOrange"
        self.theme_cls.primary_hue = "A400"
        self.theme_cls.theme_style = "Light"
        # self.theme_cls.theme_style = "Dark"
        self.custom_name = 'Company Name'
        self.screen_list = []

        # text_file = open('hotreloader.kv','r')
        # KV= text_file.read()
        # self.builder = Builder.load_string(KV)
        
        self.builder = Builder.load_file('kv_file.kv')


        self.mainPageShirt_list = []
        self.mainPageItems('shirts',self.mainPageShirt_list)

        self.mainPagejacket_list = []
        self.mainPageItems('jackets',self.mainPagejacket_list)

        self.mainPageHoody_list = []
        self.mainPageItems('hoody',self.mainPageHoody_list)

        self.show_shirts()
        self.show_jacket_test()
        self.show_hoody()

        # self.show_products()

        return self.builder
    def mainPageItems(self,src_path,list_):
        path  = 'src/'+src_path+'/'
        contents_list = (glob.glob(str(path)+'*'))
        # print(contents_list)

        for i in contents_list:
            j = i.split('\\')
            list_.append(j[-1])

    
    
    def update_kv_files(self,text):
        
        with open(self.path_to_kv_file,"w+") as kv_file:
            kv_file.write(text)
    def toggle_nav(self):
            self.root.ids.nav_drawer.set_state('toggle')

    def show_products(self,src_path,items=0):
    
        self.builder.ids.screen_manager.get_screen('ProductsPage').ids.ProductsPage.clear_widgets()

        path  = 'src/'+src_path+'/'
        
        contents_list = (glob.glob(str(path)+'*'))
        self.shirts_list=[]
        for i in contents_list:
            j = i.split('\\')
            self.shirts_list.append(j[-1])

        if items==0:
            shirts=len(self.shirts_list)
            
        else:
             shirts = items

        for i in range(shirts):
            card = MDCard(
                    orientation= 'vertical',
                    radius= [25,],
                        elevation=10,
                        padding=10,
                        
                        size_hint = (None,None),
                        width= w[0]/2.2,
                        height= w[1]/2.5,
                        md_bg_color=(1,1,1,1),
                        on_release=lambda x: self.change_screen('ProductsDeatailsPage','left')
                )
            fit_image = FitImage(
                            radius= [25,],
                            source=str(path)+self.shirts_list[i],
                            size_hint=(1,.7)
            )
            label = MDLabel(
                            text='Price= 20$',
                            font_style= 'H6',
                            halign='center',
                            size_hint=(1,.2),
            )

            card.add_widget(fit_image)
            card.add_widget(label)
            
            self.card = self.builder.ids.screen_manager.get_screen('ProductsPage').ids.ProductsPage.add_widget(
                card
                )
            
    def show_shirts(self):
        
        for i in range(4):
            card = MDCard(
                        elevation=10,
                        radius= [10,],
                                              
                        size_hint = (None,.9),
                        width= dp(100),
                       
                )
            fit_image = FitImage(
                            radius= [10,],
                            size_hint=(1,1),
                            # size = (dp(100),dp(100)),                            
                            source=str('src/shirts/')+self.mainPageShirt_list[i],
                            
            )
            

            card.add_widget(fit_image)
            # ard.add_widget(label)
            
            self.card = self.builder.ids.screen_manager.get_screen('MainPage').ids.mainPageShirts.add_widget(
                card
                )
    def show_jacket_test(self):
        # print('run')
        for i in range(4):
            card = MDCard(
                        elevation=10,
                        radius= [10,],
                                              
                        size_hint = (None,.9),
                        width= dp(100),
                       
                )
            fit_image = FitImage(
                            radius= [10,],
                            size_hint=(1,1),
                            # size = (dp(100),dp(100)),                            
                            source=str('src/jackets/')+self.mainPagejacket_list[i],
                            
            )
            

            card.add_widget(fit_image)
            # ard.add_widget(label)
            
            self.card = self.builder.ids.screen_manager.get_screen('MainPage').ids.mainPageJackets.add_widget(
                card
                )

    def show_hoody(self):
        # print('run')
        for i in range(4):
            card = MDCard(
                        elevation=10,
                        radius= [10,],
                                              
                        size_hint = (None,.9),
                        width= dp(100),
                        # on_touch_down=self.show_dialog('aa','aaaa')                
                        
                        
                       
                )
            fit_image = FitImage(
                            radius= [10,],
                            size_hint=(1,1),
                            # size = (dp(100),dp(100)),                            
                            source=str('src/hoody/')+self.mainPageHoody_list[i],
            )
            
            
            card.add_widget(fit_image)
            # ard.add_widget(label)
            
            self.cards = self.builder.ids.screen_manager.get_screen('MainPage').ids.mainPageHoddy.add_widget(
                card
                )
    def checking(self):
        print('test')
    
    

    def go_to_products(self,item):
            # print('run')
            if not self.builder.ids.screen_manager.current in self.screen_list:
                self.screen_list.append(self.builder.ids.screen_manager.current)
            self.builder.ids.screen_manager.get_screen('ProductsPage').ids.ProductsPage.clear_widgets()
            # print('cleared')
            self.show_products(item)
            self.builder.ids.screen_manager.transition.direction  = 'left'  
            self.builder.ids.screen_manager.current = 'ProductsPage'
            self.count_back=0

            
    def change_screen(self,screen,animation):
        if not self.builder.ids.screen_manager.current in self.screen_list:
            self.screen_list.append(self.builder.ids.screen_manager.current)
        self.count_back=0
        self.builder.ids.screen_manager.current = screen
        self.builder.ids.screen_manager.transition.direction=animation
        
    def onBackKey(self,window,key,*args):
        # print(self.screen_list)
        # print(key)
        # print('run')
        if key == 27 and self.screen_list ==[] and self.count_back ==0:
            self.count_back = 1
            toast('Press Back Again to exit',duration=1)
            return True
        

        if key == 27 and self.screen_list ==[] and self.count_back ==1:
            return False
            
        elif key ==27:
            self.builder.ids.screen_manager.current = self.screen_list.pop()
            self.builder.ids.screen_manager.transition.direction='right'
            return True

        
    def show_dialog(self, title, text):
        title = title
        text = text
        cancel_btn_username_dialouge = MDFlatButton(
            text="Okay", on_release=self.close_dialog)
        self.dialog = MDDialog(title=text, text=text, size_hint=(
            0.7, 0.2), buttons=[cancel_btn_username_dialouge])
        self.dialog.open()

    def close_dialog(self, obj):
            self.dialog.dismiss()
if __name__=='__main__':
    Main().run()