import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split(
    '\n')
# str_all_profiles="All User Profile"
str_all_profiles = "Profil Tous les utilisateurs"
# str_keycontent = "Key Content"
str_keycontent = "Contenu de la cl\\x82"
profiles = [i.split(":")[1][1:-1] for i in data if str_all_profiles in i]
for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8',
                                                                                                       errors="backslashreplace").split(
            '\n')
        results = [b.split(":")[1][1:-1] for b in results if str_keycontent in b]
        try:
            print("{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            print("{:<30}|  {:<}".format(i, ""))
    except subprocess.CalledProcessError:
        print("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
