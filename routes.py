from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from models import Account, Transaction
from app import db
from datetime import datetime

bp = Blueprint('routes', __name__)

@bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        if name and not Account.query.filter_by(name=name).first():
            account = Account(name=name)
            db.session.add(account)
            db.session.commit()
            return redirect(url_for("routes.index"))
    accounts = Account.query.all()
    data = [
        {"id": a.id, "name": a.name, "balance": sum(t.amount for t in a.transactions)}
        for a in accounts
    ]
    return render_template("index.html", accounts=data)

@bp.route("/accounts/<int:account_id>/delete", methods=["POST"])
def delete_account(account_id):
    account = Account.query.get_or_404(account_id)
    db.session.delete(account)
    db.session.commit()
    return redirect(url_for("routes.index"))

@bp.route("/accounts/<int:account_id>")
def account_detail(account_id):
    account = Account.query.get_or_404(account_id)
    transactions = Transaction.query.filter_by(account_id=account_id).order_by(Transaction.date.desc()).all()
    balance = sum(t.amount for t in transactions)
    return render_template("account_detail.html", account=account, transactions=transactions, balance=balance, now=datetime.now) 