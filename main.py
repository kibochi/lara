import os
import time

def php():
    print("***********[-] Removing current version and updating to newer version***********")
    os.system("sudo apt-get purge php7.*")
    os.system("sudo apt-get autoclean")
    os.system("sudo apt-get autoremove -y")
    os.system("sudo apt-get update")
    os.system("sudo apt-get install php8.0 -y")
    os.system("sudo apt install php8.0-common php8.0-mysql php8.0-xml php8.0-curl php8.0-gd  php8.0-cli php8.0-dev php8.0-imap php8.0-mbstring php8.0-opcache php8.0-soap php8.0-zip php8.0-intl -y") 
    print("***********[x] Done***********")


def composer():
    print("***********[x] installing composer***********")
    os.system(''' php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"''')
    os.system(' php composer-setup.php')
    os.system(''' php -r "unlink('composer-setup.php');" ''')
    os.system('sudo mv composer.phar /usr/local/bin/composer')
    print("***********[x] Done***********")

    


    
    




def run():
    print("***********[x] Checking php version***********")
    os.system("php -v | head -n 1")
    q1 = input("Update [yes|no]?")
    
    if(q1 == 'yes'):
        php()
        time.sleep(2)
        composer()
        
    else:
        composer()
        


if __name__ == "__main__":
    run()
        
      
       
        


 