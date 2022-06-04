from pydoc import describe
from django.db import IntegrityError
from django.shortcuts import render
from .models import *
import random
from django.core.mail import send_mail
def index(request):
    return render(request,"my_app/index.html")

def register(request):
    if request.POST:
        try:
            role = request.POST["role"]
            name = request.POST["name"]
            email = request.POST["email"]
            phone = request.POST["phone"]
            city = request.POST["city"]
            data = ["sdf78",'skf858','ghd65','ghf32','tgf20']
            password = random.choice(data)+email[3:7]
            print("----------->",password)
            uid = User.objects.create(role=role,password=password,email=email)
            if role=="Ngo":
                nid = Ngo.objects.create(user_id=uid,name =name,contact_person_number = phone,city=city)
                if nid:
                    send_mail("confirmation mail","your system generated password is "+password,"17janpython@gmail.com",[email])

                    s_msg = "Succesfuly account created!!"
                    context = {
                        "s_msg":s_msg
                    }
                    return render(request,"my_app/register.html",context)
            elif role == "Food_donor":
                fd_id = Customer.objects.create(user_id = uid,name = name, contact_number = phone ,city = city)
                if fd_id:
                    send_mail("confirmation mail","your system generated password is "+password,"17janpython@gmail.com",[email])
                    s_msg = "Succesfuly account created!!"
                    context = {
                        "s_msg" : s_msg,
                    }
                return render(request,"my_app/register.html",context)
        except IntegrityError:
            e_msg = "User already exist!!"    
            context = {
                "e_msg" : e_msg
            }
            return render(request,"my_app/register.html",context)
        except Exception as e:
            print("-->e msg",e)
            e_msg = "Somthing went wrong!"
            context = {
                "e_msg" : e_msg
            }        
            return render(request,"my_app/register.html",context)
    else:
        print("only page loaded")
        return render(request,"my_app/register.html")

def index1(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session["email"])
        nid = Ngo.objects.get(user_id = uid)
        return render(request,"my_app/ngo/index1.html",{"uid":uid,"nid":nid})   
    else:
      return render(request,"my_app/ngo/index1.html")   

def change_password(request):
    if "email" in request.session:
        email = request.session["email"]
        del request.session["email"]
        return render(request,"my_app/change_password.html")
        
    # if request.POST:
        # if "email" in request.session:
        #     email = request.session["email"]
        #     del request.session["email"]
    elif request.POST:
        email = request.POST["email"]
        currentpassword = request.POST["oldpassword"]
        newpassword = request.POST["newpassword"]
        newnewconfirmpassword = request.POST["confirmpassword"]
        uid = User.objects.get(email = email)
        if uid.password == currentpassword and  newpassword == newnewconfirmpassword:
            # update
            uid.password = newpassword
            uid.is_verify = True
            uid.save()
            s_msg = "Successfully password updated."
            return render(request,"my_app/login.html",{"s_msg" : s_msg,"email":email})
        else:
            e_msg = "Password does not match"  
            return render(request,"my_app/change_password.html",{"e_msg":e_msg,'email':email})
    else:
        msg = {"please Enter valid password "}
        return render(request,"my_app/login.html",{"msg":msg})

def login(request):
    if "email" == request.session:
        # email = request.session["email"]
        uid = User.objects.get(email = request.session["email"])
        if uid.role == "Ngo":
            nid = Ngo.objects.get(user_id = uid)
            return render(request,"my_app/ngo/index1.html",{"uid":uid,"nid":nid}) 
        elif uid.role=="Food Donor":
            fd_id=Customer.objects.get(user_id=uid)
            context={
                            "uid":uid,
                            "fd_id":fd_id,
                    }
            return render(request,'myapp/index1.html',context)    
            
    else:
        if request.POST:
            email = request.POST["email"]
            password = request.POST["password"]
            try:
                uid = User.objects.get(email=email) 
                if uid.role == "Ngo" and uid.password == password:
                    # request.session["email"] = uid.email
                    nid = Ngo.objects.get(user_id = uid)
                    if uid.is_verify:
                        context = {
                            "uid" : uid,
                            "nid" : nid,
                        }
                        request.session["email"] = uid.email
                        return render(request,"my_app/ngo/index1.html",context)   
                    else:
                        return render(request,"my_app/change_password.html",{"email" : email})   
                elif uid.role=="Food_donor" and uid.password==password:
                    fd_id=Customer.objects.get(user_id=uid) 
                    if uid.is_verify:
                        context={
                            "uid":uid,
                            "fd_id":fd_id,
                            "status" :"login",
                            }
                        request.session["email"] = uid.email
                        return render(request,'my_app/request-pickup.html',context)
                    else:
                        return render(request,"my_app/change_password.html",{"email" : email})    
                else:
                    e_msg = "Invalid email or password!!"
                    context = {
                        "e_msg" : e_msg
                    }    
                    return render(request,"my_app/login.html",context)
            except:
                e_msg = "Invalid email or password!!"
                context = {
                    "e_msg" : e_msg
                }    
                return render(request,"my_app/login.html",context)
        else:
            return render(request,"my_app/login.html")   
                        
def logout(request):
    if "email" in request.session:
        del request.session["email"]
        return render(request,"my_app/login.html")
    else:
        return render(request,"my_app/login.html")    

def ngo_profile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session["email"])
        nid = Ngo.objects.get(user_id = uid)
        return render(request,"my_app/ngo/profile.html",{"uid":uid,"nid":nid})   
    else:
      return render(request,"my_app/login.html")        

def ngo_update_password(reqeust):
    if reqeust.POST:
        email = reqeust.POST["email"]
        currentpassword = reqeust.POST["currentpassword"]
        newpassword = reqeust.POST["newpassword"]
        newnewconfirmpassword = reqeust.POST["newconfirmpassword"]
        uid = User.objects.get(email=email)
        if uid.password == currentpassword and newpassword == newnewconfirmpassword:
            # update
            uid.password = newpassword
            uid.is_verify = True
            uid.save()
            return render(reqeust,"my_app/login.html")
        else:
            e_msg = "Invalid old password does not match!!"    
            return render(reqeust,"my_app/change_password.html",{"email":email,"e_msg":e_msg})
    else:
        e_msg = "Invalid old password does not match!!"    
        return render(reqeust,"my_app/change_password.html",{"e_msg":e_msg})

def update_profile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session["email"])
        nid = Ngo.objects.get(user_id = uid)
        nid.name = request.POST["name"]        
        nid.email = request.POST["email"]
        # nid.role = request.POST["role"]
        contact_person_number = request.POST["contact_person_number"]
        contact_person_name = request.POST["contact_person_name"]
        # registration_no = request.POST["registration_no"]
        # no_member =request.POST["no_member"]
        # working_hourse = request.POST["working_hourse"]
        city = request.POST["city"]
        # address =request.POST["address"]
        if "logo" in request.FILES:
            nid.logo = request.FILES["logo"]
            nid.save()
        nid.save()    
        return render(request,"my_app/ngo/profile.html",{"uid":uid,"nid":nid})   
    else:
      return render(request,"my_app/login.html")   

def all_ngo(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session["email"])
        nid=Ngo.objects.get(user_id=uid)
        all_ngo=Ngo.objects.exclude(user_id=uid)
        context={
            "uid":uid,
            "nid":nid,
            "all_ngo":all_ngo,
            }
        return render(request,'my_app/ngo/all_ngo.html',context)
    else:
        return render(request,"my_app/login.html")

def specific_ngo_profile(request,pk):
    if "email" in request.session:
        uid = User.objects.get(email = request.session["email"])
        nid = Ngo.objects.get(user_id = uid)

        specific_ngo = Ngo.objects.get(id = pk)

        context = {
            "uid" : uid,
            "nid" : nid,
            "specific_mgo" : specific_ngo
        }
        return render(request,'my_app/ngo/specific_ngo_profile.html',context)
    else:
        return render(request,"my_app/login.html")    


def request_pickup(request):
    # if "email" in request.session:
    #     uid = User.objects.get(email = request.session["email"])
    if request.POST:
        uid = User.objects.get(email = request.session["email"])
        if uid.role == "Food_donor":
            cid = Customer.objects.get(user_id = uid)
            uid = User.objects.get(email = request.session["email"])
            fid  = FoodPickup.objects.create(user_id = uid,
                                            # donor_id = cid,
                                            food_category = request.POST["food_category"],
                                            food_description = request.POST["food_description"],
                                            pick_up_location = request.POST["pick_up_location"],
                                            food_donor_purpose = request.POST["food_donor_purpose"],
                                            pick_up_address = request.POST["pick_up_address"],
                                            pick_up_time = request.POST["pick_up_time"],
                                            food_status = "PENDING")
                                            # add hotel id 
            if fid:
                s_msg = "SUCCESSFULLY FOOD PICKUP REQUEST SEND"
                context = {
                    "uid" : uid,
                    "cid" : cid,
                    "status" : "login",
                    "s_msg" : s_msg,
                }                                
                return render(request,"my_app/request-pickup.html",context)
    else:
        uid = User.objects.get(email = request.session["email"])
        cid = Customer.objects.get(user_id = uid)
        context = {
                        "uid" : uid,
                        "cid" : cid,
                        "status" : "login",
                    }  
        return render(request,"my_app/request-pickup.html",context)

def view_request(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session["email"])
        nid = Ngo.objects.get(user_id = uid)
        all_request = FoodPickup.objects.filter(food_status = "PENDING")
        context = {
            "uid" : uid,
            "nid" : nid,
            "all_request" : all_request,
        }
    return render(request,"my_app/ngo/Views Request.html",context)

def past_request(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session["email"])
        nid = Ngo.objects.get(user_id = uid)
        all_request = FoodPickup.objects.exclude(food_status = "PENDING")
        context = {
            "uid" : uid,
            "nid" : nid,
            "all_request" : all_request,
        }
    return render(request,"my_app/ngo/past request.html",context)

def New_post(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session["email"])
        nid = Ngo.objects.get(user_id = uid)
        if request.POST:
            title = request.POST["Title"]
            describe = request.POST["Description"]                
            pic = request.POST["picture"]                
            video = request.POST["videofile"]                
            audio = request.POST["audiofile"]      
            pid = POST_NGO.objects.create(title = title,description = describe,picture=pic,videofile = video,audiofile = audio)          
            context = {
                "uid" : uid,
                "nid" : nid,

            }
            return render(request,"my_app/ngo/new_post.html",context)
        else:
            context = {
            "uid" : uid,
            "nid" : nid,
                 }
            return render(request,"my_app/ngo/new_post.html",context)
    else:
        return render(request,"my_app/ngo/new_post.html")
    