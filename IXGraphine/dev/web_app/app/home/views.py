from flask import render_template, session, request
from . import home
import os
import subprocess
from wtforms import Form, StringField, SelectField

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    #os.system('apt-cache search crypto')
    tag = 'crypto'
    out = subprocess.Popen(['apt-cache', 'search', 'crypto'], 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    #print(stdout)
    col=len(str(stdout).replace('\\n', '\n').split(str("\n")))
    #print(col)
    crypto=str(stdout).replace('\\n', '\n').split(str("\n"))
    if request.method == "POST":
        searchitem = request.form["appname"]
        session['appname'] = searchitem
        out = subprocess.Popen(['apt-cache', 'search', 'crypto'], 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
        stdout,stderr = out.communicate()
        #print(stdout)
        col=len(str(stdout).replace('\\n', '\n').split(str("\n")))
        #print(col)
        crypto=str(stdout).replace('\\n', '\n').split(str("\n"))
        return render_template('page/home/index.html',tag=tag,crypto=crypto,col=col, title="Search Results")
    return render_template('page/home/index.html',tag=tag,crypto=crypto,col=col, title="Home Page")

@home.route('install/<tag>/<appid>')
def install(tag,appid):
    print("Installing...")
    cmd = "(sudo apt install "+appid+" -y) | zenity --text-info"
    result = subprocess.check_output(cmd, shell=True)
    result=str(result).split(" ")  
    """
    Render the app page for the appid which isnt an id but an index of the list because im dumb but yeah
    """
    print("Install appid:",appid)
    print("Grabbing application list...")
    out = subprocess.Popen(['apt-cache', 'search', str(tag)], 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    col=len(str(stdout).replace('\\n', '\n').split(str("\n")))
    crypto=str(stdout).replace('\\n', '\n').split(str("\n"))
    """
    This is hella inffectient and may break if a new application with the tag was added, update this upon v0.30
    """
    print("Indexing...")
    appname = [s for s in crypto if str(appid.split(" ")[0]) in s]
    index = crypto.index(str(appname[0]))
    print("Got index: ",index)
    print("Building version data...")
    out = subprocess.Popen(['apt-cache','policy', str(appid.split(" ")[0])], 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    data=str(stdout).replace('\\n', '\n').split(str("\n"))
    #print(data)
    version = data
    cmd = str('apt show -a '+appid.split(" ")[0])
    out = subprocess.Popen(cmd.split(" "), 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    data=str(stdout).replace('\\n', '\n').split(str("\n"))
    #print(data)
    data.pop(0)
    sdata = data
    data = [s for s in data if "Description:" in s]
    size = [v for v in sdata if "Installed-Size:" in v]
    return render_template('page/apps/app_page.html',size=size,data=data[0],version=version,appid=appid,index=index, title=str(appid))

@home.route('appinstall/<tag>/<appid>')
def appinstall(tag,appid):
    """
    Render the app page for the appid which isnt an id but an index of the list because im dumb but yeah
    """
    print("Install appid:",appid)
    print("Grabbing application list...")
    out = subprocess.Popen(['apt-cache', 'search', str(tag)], 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    col=len(str(stdout).replace('\\n', '\n').split(str("\n")))
    crypto=str(stdout).replace('\\n', '\n').split(str("\n"))
    """
    This is hella inffectient and may break if a new application with the tag was added, update this upon v0.30
    """
    print("Indexing...")
    appname = [s for s in crypto if str(appid.split(" ")[0]) in s]
    index = crypto.index(str(appname[0]))
    print("Got index: ",index)
    print("Building version data...")
    out = subprocess.Popen(['apt-cache','policy', str(appid.split(" ")[0])], 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    data=str(stdout).replace('\\n', '\n').split(str("\n"))
    #print(data)
    version = data
    cmd = str('apt show -a '+appid.split(" ")[0])
    out = subprocess.Popen(cmd.split(" "), 
           stdout=subprocess.PIPE, 
           stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    data=str(stdout).replace('\\n', '\n').split(str("\n"))
    #print(data)
    data.pop(0)
    sdata = data
    data = [s for s in data if "Description:" in s]
    size = [v for v in sdata if "Installed-Size:" in v]
    return render_template('page/apps/app_page.html',size=size,tag=tag,data=data[0],version=version,appid=appid,index=index, title=str(appid))

@home.route('/dashboard')
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('page/home/dashboard.html', title="Dashboard")
