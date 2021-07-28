import re
from PIL import Image,ImageTk
import decimal
import json
from flask import render_template, url_for, flash, redirect,request,jsonify,Blueprint,session
from main import app,db,bcrypt,fujs,mail,ALLOWED_EXTENSIONS
from main.forms import (RegistrationForm, LoginForm,editProfile
                    ,SendEmail,addPost, RequestResetForm,editPost,
                        ResetPassword,ConfirmEmail,editUser,filterPosts)
from main.models import User,Post,Likes
from flask_login import current_user,login_user,login_required,logout_user
from time import localtime,strftime
from flask_mail import Message
import requests
import secrets
import os
import stripe
from werkzeug.utils import secure_filename
app.config["STRIPE_PUBLIC_KEY"] = "stripe_public_key"
app.config["STRIPE_SECRET_KEY"] = "stripe_secret_key"
stripe.api_key = app.config["STRIPE_SECRET_KEY"]

def save_picture(form_picture,width,height):
    random_hex = secrets.token_hex(8)
    _,f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path  = os.path.join(app.root_path,"static/images/products/",picture_fn)
    output_size = (width,height)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    newPic = Image.open(picture_path)
    newPic = newPic.resize((width,height),Image.ANTIALIAS)
    newPic.save(picture_path)
    return picture_fn

@app.route("/",methods=["GET","POST"])
@app.route("/home/",methods=["GET","POST"])
def home(): 
    if current_user.is_authenticated:
        user = User.query.filter_by(id=current_user.id).first()
    else:
        user = None
    form = filterPosts()
    posts = Post.query.all()
    query = db.session.query(Post)
    if request.method =='POST':
        title = form.title.data
        type = form.type.data
        category = form.category.data
        location = form.location.data

        if title != "":
            search = "%{}%".format(title)
            query = query.filter(Post.title.ilike(search))
        if type != "---":
            query = query.filter(Post.type == type)
        if category != "---":
            query = query.filter(Post.category == category)
        if location != "":
            query = query.filter(Post.location == location)   
        posts = query.all()
        return render_template("main.html", posts=posts,form=form)
    return render_template("main.html", posts=posts,form=form)

@app.route("/admin/",methods=["GET","POST"])
def admin():
   
    if current_user.is_authenticated and current_user.email == 'alessiogiovannini@hotmail.it':
        Users = User.query.all()
        Products = Product.query.all()
        orders = Orders.query.all()
        return render_template("admin.html",Users=Users,Products=Products,orders=orders)
    else:
        flash("You're not authorized to view this page","error")
        return redirect(url_for("home"))
    
@app.route("/login/",methods=["GET","POST"])
def login():
   
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()  
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        if user and bcrypt.check_password_hash(user.password,form.password.data) :
            login_user(user)
            print(request.referrer)
            return redirect(url_for('home'))

        else:
            flash("Login Unsuccessful. Please check email and password","error")
            print(request.referrer)
            return render_template("login.html",title="Login",form=form)
    
    return render_template("login.html",title="Login",form=form)

@app.route("/like_post/<int:id>/<action>",methods=["GET","POST"])
def like_post(id,action):
    posts = Post.query.all()
    post = Post.query.filter_by(id=id).first_or_404()
    if action == 'like':
        current_user.like_post(post)
        db.session.commit()
    if action == 'unlike':
        current_user.unlike_post(post)
        db.session.commit()
    return redirect(request.referrer)
        
@app.route("/register/",methods=["GET","POST"])
def register():

    form = RegistrationForm()
    form.type.choices = ['Person','Kennel']
    if request.method =="POST":
        if form.validate_on_submit():
            
            if form.termsConditions.data == False:
                flash("You must accept the terms and conditions", "error")
            else:
                firstname = form.firstname.data
                lastname = form.lastname.data
                email  =form.email.data
                password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
                address = form.address.data
                city = form.city.data
                country = form.country.data
                zipCode = form.zip_code.data
                type = form.type.data

                picture = save_picture(form.picture.data,200,200)
                new_user = User(firstname=firstname,picture=picture,type=type,email=email,password=password,lastname = lastname,address=address,city=city,country=country,zip_code=zipCode)
                db.session.add(new_user)
                db.session.commit()
                flash("Congratulations, account created for {}, you can now sign in.".format(form.firstname.data), "success")
                return redirect(url_for("login"))
        else:
            print(form.picture.data)
            print("hello!")
            flash("An error occurred while creating the account.", "error")
            return render_template("register.html",title="Register",form=form)
    return render_template("register.html",title="Register",form=form)

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/add_post/",methods=["GET","POST"])
def add_post():
    form = addPost()
    if request.method=="GET":

        if current_user.is_authenticated:
            user = User.query.filter_by(id=current_user.id).first()
            if user.verified == False:
                return redirect(url_for("confirm_email"))
        else:
            flash('You need an account!','error')
            return redirect(url_for("login"))
    
    if request.method =="POST":
        if form.validate_on_submit():
            title = form.title.data
            text  =form.text.data
            type = form.type.data
            category = form.category.data
            location = form.location.data
            print(form.picture.data)
            if form.picture.data != None:
                picture = save_picture(form.picture.data,500,500)
            else:
                picture=''
            post = Post(   
                            title=title,
                            text = text,
                            picture=picture,
                            type=type,
                            category=category,
                            location=location,
                            active= True,
                            author_id = current_user.id
                            )

            db.session.add(post)
            db.session.commit()
            flash("New post created: {}".format(title), "success")
            return redirect(url_for("home"))

        elif form.validate_on_submit()==False:
            flash("Error! Post not created", "error")
            return render_template("add_post.html", form=form)

            
    return render_template("add_post.html", form=form)



@app.route("/profile/<int:id>",methods=["GET","POST"])
def profile(id):
    if not current_user.is_authenticated:
        flash("Error! You're not authorized to see this page", "error")
        return redirect(url_for("home"))
    posts = Post.query.filter_by(author_id=id).all()
    user = User.query.get_or_404(id)
    return render_template("profile.html", user=user,posts=posts)


@app.route("/edit_user/<int:id>",methods=["GET","POST"])
def edit_user(id):
    if not current_user.is_authenticated and not current_user.email == "alessio.giovannini@hotmail.it":
        flash("Error! You're not authorized to see this page", "error")
        return redirect(url_for("home"))
    user = User.query.get_or_404(id)
    form = editUser()
    if request.method =="GET":
        form.firstname.data = user.firstname
        form.lastname.data = user.lastname
        form.address.data = user.address 
        form.city.data = user.city
        form.country.data = user.country
        form.zip_code.data = user.zip_code
        form.picture.data = user.picture

    if request.method =="POST":
        if form.validate_on_submit():
            user.firstname = form.firstname.data
            user.lastname =form.lastname.data
            user.price  = form.address.data
            user.country=form.country.data
            user.zip_code=form.zip_code.data
            user.picture = save_picture(form.picture.data,200,200)
            db.session.commit()
            flash("Congratulations, user updated", "success")
            return redirect(url_for("profile",id=id))
        elif form.validate_on_submit()==False:
            for error in form.errors:
                print(error)
            flash("Error! User not updated", "error")
            return render_template("edit_user.html", form=form)
    return render_template("edit_user.html", form=form)

@app.route("/remove_item/<int:id>",methods=["GET","POST"])
def remove_item(id):
    totalSum = 0
    itemsCart = 0   
    for i in session['cart']:
        if i[4] == id:
            item = next(item for item in session['cart'] if item[4] == id)
            session['cart'].remove(item)
            session.modified = True
    for i in session['cart']:
        totalSum = totalSum + i[3]
        itemsCart = itemsCart +1
    return render_template('cart.html',session=session,totalSum=totalSum,itemsCart=itemsCart)
@app.route("/logout/")
def logout():
    logout_user()
    flash("You have been logged out successfully","success")
    return redirect(url_for("home"))

@app.route("/clearCart/",methods=["GET","POST"])
def clearCart():

        
    if "cart" in session:

        session["cart"] = []
        session.modified = True
        flash("Items have been removed","success")
        if 'url' in session:
            return redirect(session['url'])
    return render_template("home.html")

@app.route("/add_to_cart",methods=["POST"])
def add_to_cart():
    
    data = request.get_json()
    product_id = data["product_id"]
    productToAdd = Product.query.get_or_404(product_id)
    form = addtoShoppingCart()
    quantity = data["quantity"]
    print(quantity)
    totalSum = 0
    itemsCart = 0
    for i in session["cart"]:
        totalSum = totalSum + i[3]
        itemsCart = itemsCart+1
    
    return render_template("product.html", product=productToAdd,form=form,session=session,totalSum=totalSum,itemsCart=itemsCart)



@app.route("/post/<int:id>",methods=["GET","POST"])
def post(id):
    post = Post.query.get_or_404(id)
    return render_template("post.html", post=post)

@app.route("/edit_post/<int:id>",methods=["GET","POST"])
def edit_post(id):
    post = Post.query.get_or_404(id)
    if current_user.is_authenticated:
        user = User.query.filter_by(id=current_user.id).first()
        if user.verified == False:
            return redirect(url_for("confirm_email"))
        print(post.author)
        if current_user.id != post.author_id:
            flash("You're not the author of this post!",'error')
            return render_template('main.html')
    form = editPost()
    if request.method =="GET":
            form.title.data = post.title
            form.text.data = post.text
            form.picture.data = post.picture
            form.type.data = post.type
            form.location.data = post.location
            form.category.data = post.category  
    if request.method =="POST":
        if form.validate_on_submit():
            post.title = form.title.data
            post.text = form.text.data
            post.type = form.type.data
            post.location = form.location.data
            post.category = form.category.data
            if form.picture.data:
                post.picture = save_picture(form.picture.data,500,500)
            db.session.commit()
            flash("Congratulations, post updated", "success")
            return redirect(url_for("post",id=id))
        elif form.validate_on_submit()==False:
            flash("Error! Post not updated", "error")
            return render_template("edit_post.html", form=form)
        
    return render_template("edit_post.html", form=form)

@app.route("/editProfile/<string:id>/",methods=["GET","POST"])
def editProfile(id):
    form = EditProfile()
    user = User.query.filter_by(id=id).first()
    if request.method == "GET":
        form.firstname.data = user.firstname
        form.lastname.data = user.lastname
        form.address.data = user.address
        form.city.data = user.city
        form.country.data = user.country
        form.zip_code.data = user.zip_code
    if request.method == "POST":

        if form.validate_on_submit():
            user.firstname = form.firstname.data
            user.lastname = form.lastname.data
            user.address = form.address.data
            user.city = form.city.data
            user.country = form.country.data
            user.zip_code =form.zip_code.data
            db.session.commit()
            flash("User updated!","success")
            return redirect(url_for("profile",id=id))
    return render_template("register.html",user= user,form=form)

@app.route("/cart/",methods=["GET","POST"])
def cart():
    totalSum = 0
    itemsCart = 0
    session['url'] = url_for('cart')
    for i in session["cart"]:
        totalSum = totalSum + i[3]
        itemsCart = itemsCart+1
    
    return render_template("cart.html",session=session,totalSum=totalSum,itemsCart=itemsCart)




@app.route("/sendEmail/<string:id>/<string:post_id>/",methods=["GET","POST"])
@login_required
def send_email(id,post_id):
    form = SendEmail()
    if form.validate_on_submit() and request.method=="POST" :
        recipientUser = User.query.get(id).email
        senderEmail = User.query.get(current_user.id)
        msg = Message("Hey There",recipients="alessiogiovannini@hotmail.it".split(),cc=senderEmail.email.split())
        msg.html = "form.description.data" + str(request.base_url)
        msg.html = "<p>Hello!</p><p></p>"+ senderEmail.firstname + " is interested in your add and I think it would be great if you could exchange more information between you two.</p><p></p><p>Link: "+str(request.base_url) +"</p><p></p><p>Text from "+ senderEmail.firstname +":<p></p>"+ form.description.data +"</p><p></p>"
        mail.send(msg)
        flash("Message sent","success")
        return redirect(url_for("home"))

    if request.method=="GET":
        recipientUser = User.query.get(id).email
        senderEmail = User.query.get(current_user.id)
        form.recipient.data= recipientUser
        return render_template("send_email.html",form=form)
    return render_template("send_email.html",form=form)


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message("Password Reset Request",sender="alesisio982017@gmail.com",recipients=[user.email])
    msg.body = """To reset your password, visit the following link:
{}

If you did not make this request then simply ignore this email and no change will be made.

""".format(url_for("reset_token",token=token,_external = True))
    mail.send(msg)



@app.route("/purchase_details/",methods=["GET","POST"])
def purchase_details():
    if not current_user.is_authenticated:
        flash("You need an account in order to proceed!.","danger")
        return redirect(url_for("login"))
    elif current_user.verified == False:
        return redirect(url_for("confirm_email"))
    form = purchaseDetails()
    form.firstname.data = current_user.firstname
    form.lastname.data = current_user.lastname
    form.address.data = current_user.address
    form.email.data = current_user.email
    form.country.data = current_user.country
    form.zip_code.data = current_user.zip_code
    form.city.data = current_user.city
    # array_json = []
    # json_parameters = json.dumps({})
    # json_data = "["
    # for i in session["cart"]:
    #     string_purchase = "{"
    #     string_purchase = string_purchase + ""{0}":"{1}","{2}":{3}".format("price",i[5],"quantity",int(i[2])) + "},"
    #     json_data = json_data + string_purchase
    #     array_json.append(json_parameters)
    # json_data = json_data + "]"
    # Build a Stripe checkout list
    line_items_list = []
    for item in session["cart"]:
        line_item = {}
        line_item["price"] = item[5]
        line_item["quantity"] = int(item[2])
        line_items_list.append(dict(line_item))
    # line_items = [{"price": "price_1Iq38aDcWwYEXNjriZquwiiu", "quantity": 100}],
    print(line_items_list)
    session_stripe = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items = line_items_list,
            mode = "payment",
            success_url = url_for("payment_confirmed",_external=True) + "?session_id={CHECKOUT_SESSION_ID}",
            cancel_url = url_for("home",_external=True)  

    )
    
    return render_template("purchase_details.html",checkout_session_id = session_stripe["id"],form=form, checkout_public_key = app.config["STRIPE_PUBLIC_KEY"] )
    
@app.route("/payment_confirmed/")
def payment_confirmed():
    session_id = request.args.get("session_id")
    print(session_id)
    for i in session["cart"]:
        customerID = current_user.id
        productID = i[4]
        quantity = i[2]
        total_price = i[3]
        stripe_session_id = session_id
        order = Orders(customerID=customerID,productID= productID,quantity=quantity,total_price=total_price,stripe_session_id =stripe_session_id)
        db.session.add(order)
    db.session.commit()
    session["cart"] = []
    session.modified = True
    redirect(url_for("clearCart"))
    orders = Orders.query.filter(Orders.stripe_session_id == session_id)

    return render_template("payment_confirmed.html",session=session,orders=orders)

@app.route("/reset_password/",methods=["GET","POST"])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash("An email has been sent with instructions to reset your password.","success")
        return redirect(url_for("login"))
    return render_template("request_reset_password.html",title="Reset Password",form=form)


@app.route("/reset_password/<token>",methods=["GET","POST"])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    
    user = User.verify_reset_token(token)
    if user is None:
        flash("That is an invalid or expired token","error")
        return redirect(url_for("reset_password"))
    form = ResetPassword()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user.password = hash_password
        db.session.commit()
        flash("The password has been updated","success")
        return redirect(url_for("login"))

    return render_template("reset_password.html",title="Reset Password",form=form)

def send_confirmation_email(user):
    token = user.get_reset_token()
    msg = Message("Confirmation Email",sender="onlineshop420it@gmail.com",recipients=[user.email])
    msg.body = url_for("confirm_email_token",token=token,_external = True)
    mail.send(msg)
@app.route("/confirm_email/",methods=["GET","POST"])
def confirm_email():
    if not current_user.is_authenticated:
        return redirect(url_for("login"))
    form = ConfirmEmail()
    if request.method=="POST":
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            send_confirmation_email(user)
            flash("An email has been sent to confirm your email address.","success")
        
            return redirect(url_for("login"))
        
    if request.method=="GET":
        
        form.email.data = User.query.filter_by(id=current_user.id).first().email
        user = User.query.filter_by(id=current_user.id).first()
    return render_template("confirm_email.html",title="Confirm your email!",form=form,user=user)


@app.route("/confirm_email_token/<token>",methods=["GET","POST"])
def confirm_email_token(token):

    if not current_user.is_authenticated:
        return redirect(url_for("home"))
    user = User.verify_reset_token(token)
    if user is None:
    
        flash("That is an invalid or expired token","error")
        return redirect(url_for("confirm_email"))
    elif not user is None:
        user.verified = True
        db.session.commit()
        flash("Email Confirmed.","success")
        return redirect(url_for("home"))

    return render_template("index.html")
