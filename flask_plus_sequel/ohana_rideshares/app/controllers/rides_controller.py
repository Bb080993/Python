from app import app
from flask import Flask, render_template, redirect, request, session, flash
from app.models.ride_model import Ride
from flask_bcrypt import Bcrypt
bcrypt=Bcrypt(app)

@app.route("/rides/new")
def new_ride():
    if not "user_id" in session:
        return redirect("/")

    return render_template("new_ride.html")

@app.route("/add_ride", methods=["POST"])
def add_ride():
    if not "user_id" in session:
        return redirect("/")
    if not Ride.validate_ride(request.form):
        return redirect("/rides/new")
    data={
        "rider_id": request.form["rider_id"],
        "destination": request.form["destination"],
        "pickup_location": request.form["pickup_location"],
        "date": request.form["date"],
        "details":request.form["details"]
    }
    Ride.add_ride(data)
    return redirect("/dashboard")

@app.route("/delete/<int:id>")
def delete_ride_request(id):
    if not "user_id" in session:
        return redirect("/")
    data={
        "id":id
    }
    Ride.delete_request(data)

    return redirect("/dashboard")

@app.route("/add_driver/<int:driver_id>/<int:ride_id>")
def add_drive(driver_id, ride_id):
    if not "user_id" in session:
        return redirect("/")
    data={
        "driver_id": driver_id,
        "id": ride_id
    }
    Ride.insert_driver_id(data)

    return redirect("/dashboard")

@app.route("/cancel/<int:ride_id>")
def cancel_driver(ride_id):
    if not "user_id" in session:
        return redirect("/")
    data={
        "id":ride_id
    }
    Ride.driver_cancelled(data)
    return redirect("/dashboard")

@app.route("/rides/<int:ride_id>")
def details(ride_id):
    if not "user_id" in session:
        return redirect("/")
    data={
        "id": ride_id
    }
    one_ride=Ride.get_one_booked_requests(data)
    return render_template("details.html", one_ride=one_ride)


@app.route("/rides/edit/<int:id>")
def edit_ride_page(id):
    if not "user_id" in session:
        return redirect("/")
    data={
        "id":id
    }
    one_ride=Ride.get_one_booked_requests(data)
    return render_template("edit.html", one_ride=one_ride)

@app.route("/edit_ride", methods=["POST"])
def edit_ride():
    if not "user_id" in session:
        return redirect("/")
    data={
        "id": request.form["id"],
        "pickup_location": request.form["pickup_location"],
        "details": request.form["details"]
    }
    if not Ride.validate_update(data):
        return redirect(f"/rides/edit/{request.form['id']}")
    Ride.update_ride(data)

    return redirect(f"/rides/{request.form['id']}")